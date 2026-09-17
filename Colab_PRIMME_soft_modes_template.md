# Colab notebook template — PRIMME soft modes

Tony Kawas / 17 September 2026.

Copy each cell into a Google Colab notebook in order.

---

## Cell 1 — Install

```python
!pip install -q primme
import primme
print('primme OK', getattr(primme, '__version__', 'unknown'))
```

If this fails, stop and report the error. PRIMME must import before continuing.

---

## Cell 2 — Imports and algebra

```python
import numpy as np
from itertools import product
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import eigsh, LinearOperator
import time, gc, warnings
warnings.filterwarnings('ignore')

I2 = np.eye(2, dtype=complex)
sx = np.array([[0., 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
z2 = np.zeros((2, 2), dtype=complex)
alpha4 = [np.block([[z2, s], [s, z2]]) for s in (sx, sy, sz)]
beta4 = np.block([[I2, z2], [z2, -I2]])
ALPHA = [np.kron(a, I2).astype(complex) for a in alpha4]
BETA = np.kron(beta4, I2).astype(complex)
G5 = np.kron(beta4, I2).astype(complex)
MASS_B = [np.kron(beta4, t).astype(complex) for t in (sx, sy, sz)]
EYE8 = np.eye(8, dtype=complex)
R = 1.0
G5DIAG = np.diag(G5).real.copy()
print('Algebra OK')
```

---

## Cell 3 — Hedgehog + operators

```python
def hedgehog(x, y, z, cx, cy, cz, L, w):
    rx = (x - cx) - L * int(round((x - cx) / float(L)))
    ry = (y - cy) - L * int(round((y - cy) / float(L)))
    rz = (z - cz) - L * int(round((z - cz) / float(L)))
    rr = np.sqrt(rx*rx + ry*ry + rz*rz + 1e-16)
    f = np.tanh(rr / w)
    th = np.arccos(np.clip(rz / rr, -1., 1.))
    ph = np.arctan2(ry, rx)
    hx = np.sin(th)*np.cos(ph); hy = np.sin(th)*np.sin(ph); hz = np.cos(th)
    d = rr / np.sqrt(rr*rr + 0.08)
    hx, hy, hz = d*hx, d*hy, d*hz
    n = np.sqrt(hx*hx + hy*hy + hz*hz + 1e-30)
    return f, hx/n, hy/n, hz/n

def precompute_onsite(L, m0, v, w, sep):
    cx1, cy1, cz1 = L//2, L//2, (L//2 - sep//2) % L
    cx2, cy2, cz2 = L//2, L//2, (L//2 + sep//2) % L
    M = np.zeros((L, L, L, 8, 8), dtype=complex)
    base = m0*BETA + 3*R*EYE8
    for x, y, z in product(range(L), repeat=3):
        Md = base.copy()
        for sign, cx, cy, cz in [(+1, cx1, cy1, cz1), (-1, cx2, cy2, cz2)]:
            f, hx, hy, hz = hedgehog(x, y, z, cx, cy, cz, L, w)
            if f < 1e-14:
                continue
            Md = Md + sign*v*f*(hx*MASS_B[0] + hy*MASS_B[1] + hz*MASS_B[2])
        M[x, y, z] = Md
    return M, (cx1, cy1, cz1), (cx2, cy2, cz2)

def apply_H(psi_flat, L, M_on):
    psi = psi_flat.reshape((L, L, L, 8))
    out = np.einsum('xyzab,xyzb->xyza', M_on, psi)
    for mu, axis in enumerate([0, 1, 2]):
        Aplus = -0.5*(R*EYE8 - ALPHA[mu])
        Aminus = -0.5*(R*EYE8 + ALPHA[mu])
        out = out + np.einsum('ab,xyzb->xyza', Aplus, np.roll(psi, -1, axis=axis))
        out = out + np.einsum('ab,xyzb->xyza', Aminus, np.roll(psi, +1, axis=axis))
    out = np.einsum('ab,xyzb->xyza', G5, out)
    return out.reshape(-1)

def build_sparse_H(L, m0, v, w, sep):
    Nspin = 8
    N = Nspin * L**3
    cx1, cy1, cz1 = L//2, L//2, (L//2 - sep//2) % L
    cx2, cy2, cz2 = L//2, L//2, (L//2 + sep//2) % L
    rows, cols, data = [], [], []
    def add(i0, j0, mat):
        for s in range(8):
            for sp in range(8):
                val = mat[s, sp]
                if abs(val) > 1e-18:
                    rows.append(i0 + s)
                    cols.append(j0 + sp)
                    data.append(complex(val))
    base = m0*BETA + 3*R*EYE8
    for x, y, z in product(range(L), repeat=3):
        i0 = Nspin * (z + L*(y + L*x))
        Md = base.copy()
        for sign, cx, cy, cz in [(+1, cx1, cy1, cz1), (-1, cx2, cy2, cz2)]:
            f, hx, hy, hz = hedgehog(x, y, z, cx, cy, cz, L, w)
            if f < 1e-14:
                continue
            Md = Md + sign*v*f*(hx*MASS_B[0] + hy*MASS_B[1] + hz*MASS_B[2])
        add(i0, i0, Md)
        for mu, (dx, dy, dz) in enumerate([(1,0,0), (0,1,0), (0,0,1)]):
            jp = Nspin * (((z+dz)%L) + L*(((y+dy)%L) + L*((x+dx)%L)))
            jm = Nspin * (((z-dz)%L) + L*(((y-dy)%L) + L*((x-dx)%L)))
            add(i0, jp, -0.5*(R*EYE8 - ALPHA[mu]))
            add(i0, jm, -0.5*(R*EYE8 + ALPHA[mu]))
    D = coo_matrix((data, (rows, cols)), shape=(N, N), dtype=complex).tocsr()
    G = diags(np.tile(G5DIAG, L**3))
    GD = G @ D
    return 0.5*(GD + GD.getH()).tocsr()

print('Operators defined')
```

---

## Cell 4 — Reference soft modes (sparse ARPACK) at L=8

```python
L, m0, v, w, sep = 8, 0.3, 2.0, 1.0, 5
print(f'Reference L={L} ...')
t0 = time.time()
Hs = build_sparse_H(L, m0, v, w, sep)
ev_ref, evec_ref = eigsh(Hs, k=4, sigma=0.0, which='LM', maxiter=4000, tol=1e-6)
ord = np.argsort(np.abs(ev_ref))
ev_ref, evec_ref = ev_ref[ord], evec_ref[:, ord]
print(f'sparse |λ| = {np.round(np.abs(ev_ref), 6)}  ({time.time()-t0:.1f}s)')
```

---

## Cell 5 — PRIMME on sparse H at L=8 (validation)

```python
print('PRIMME sparse L=8 ...')
t0 = time.time()
try:
    ev_p, evec_p = primme.eigsh(Hs, k=4, which='SM', tol=1e-6, maxiter=10000)
    ord = np.argsort(np.abs(ev_p))
    ev_p, evec_p = ev_p[ord], evec_p[:, ord]
    print(f'PRIMME |λ| = {np.round(np.abs(ev_p), 6)}  ({time.time()-t0:.1f}s)')
    print(f'max |λ| diff vs ARPACK = {np.max(np.abs(np.abs(ev_p) - np.abs(ev_ref))):.2e}')
    ovs = [float(np.max(np.abs(evec_ref[:, i].conj() @ evec_p))) for i in range(4)]
    print(f'subspace overlaps = {np.round(ovs, 4)}')
except Exception as e:
    print(f'PRIMME sparse failed: {type(e).__name__}: {e}')
```

**Success criterion:** |λ| diff ≲ 1e-4 and overlaps ≳ 0.99.

---

## Cell 6 — PRIMME matrix-free at L=8

```python
M_on, c1, c2 = precompute_onsite(L, m0, v, w, sep)
N = 8 * L**3

def matvec(x):
    return apply_H(x, L, M_on)

Hop = LinearOperator((N, N), matvec=matvec, dtype=np.complex128)

print('PRIMME matrix-free L=8 ...')
t0 = time.time()
try:
    ev_mf, evec_mf = primme.eigsh(Hop, k=4, which='SM', tol=1e-5, maxiter=20000)
    ord = np.argsort(np.abs(ev_mf))
    ev_mf, evec_mf = ev_mf[ord], evec_mf[:, ord]
    print(f'PRIMME MF |λ| = {np.round(np.abs(ev_mf), 6)}  ({time.time()-t0:.1f}s)')
    print(f'max |λ| diff vs ARPACK = {np.max(np.abs(np.abs(ev_mf) - np.abs(ev_ref))):.2e}')
except Exception as e:
    print(f'PRIMME MF failed: {type(e).__name__}: {e}')
    print('Try which="SA" on H^2 path or increase maxiter')
```

---

## Cell 7 — L=10 validation (sparse + optional MF)

```python
L, sep = 10, 6
print(f'Reference L={L} ...')
Hs10 = build_sparse_H(L, m0, v, w, sep)
ev10, _ = eigsh(Hs10, k=4, sigma=0.0, which='LM', maxiter=5000, tol=1e-5)
ev10 = np.sort(np.abs(ev10))
print(f'sparse |λ| = {np.round(ev10, 6)}')

print('PRIMME sparse L=10 ...')
t0 = time.time()
try:
    ev_p10, _ = primme.eigsh(Hs10, k=4, which='SM', tol=1e-5, maxiter=15000)
    ev_p10 = np.sort(np.abs(ev_p10))
    print(f'PRIMME |λ| = {np.round(ev_p10, 6)}  ({time.time()-t0:.1f}s)')
    print(f'diff = {np.max(np.abs(ev_p10 - ev10)):.2e}')
except Exception as e:
    print(f'failed: {e}')
```

---

## Cell 8 — Stretch: matrix-free L=12

```python
L, sep = 12, 6
print(f'L={L} matrix-free PRIMME (N={8*L**3}) ...')
M_on12, _, _ = precompute_onsite(L, m0, v, w, sep)
N12 = 8 * L**3

def matvec12(x):
    return apply_H(x, L, M_on12)

Hop12 = LinearOperator((N12, N12), matvec=matvec12, dtype=np.complex128)

t0 = time.time()
try:
    ev12, evec12 = primme.eigsh(
        Hop12, k=4, which='SM',
        tol=1e-4, maxiter=30000,
        # method='PRIMME_JDQMR',  # optional
    )
    ord = np.argsort(np.abs(ev12))
    ev12 = ev12[ord]
    print(f'L=12 PRIMME |λ| = {np.round(np.abs(ev12), 6)}  ({time.time()-t0:.1f}s)')
    print('L=12 SUCCESS — soft modes extracted matrix-free')
except Exception as e:
    print(f'L=12 failed: {type(e).__name__}: {e}')
    print(f'elapsed {time.time()-t0:.1f}s')
```

---

## Cell 9 — Optional: mass-texture χ on soft modes

```python
# Run only if you have soft eigenvectors evec_s and L, M_on, sep
def chi_mass_texture(psi, L, w, sep):
    cx1, cy1, cz1 = L//2, L//2, (L//2 - sep//2) % L
    cx2, cy2, cz2 = L//2, L//2, (L//2 + sep//2) % L
    pr = psi.reshape((L, L, L, 8))
    acc = 0.0
    for x, y, z in product(range(L), repeat=3):
        vx = vy = vz = 0.0
        for sign, cx, cy, cz in [(+1, cx1, cy1, cz1), (-1, cx2, cy2, cz2)]:
            f, hx, hy, hz = hedgehog(x, y, z, cx, cy, cz, L, w)
            vx += sign*f*hx; vy += sign*f*hy; vz += sign*f*hz
        n = np.sqrt(vx*vx + vy*vy + vz*vz + 1e-30)
        M = (vx/n)*MASS_B[0] + (vy/n)*MASS_B[1] + (vz/n)*MASS_B[2]
        acc += np.vdot(pr[x, y, z], M @ pr[x, y, z]).real
    return float(acc)

# Example if evec_mf exists from Cell 6:
# for i in range(4):
#     print(i, chi_mass_texture(evec_mf[:, i], 8, w, 5))
```

---

## Success checklist

| Step | Criterion |
|------|-----------|
| Cell 1 | `import primme` works |
| Cell 5 | PRIMME sparse matches ARPACK (diff ≲ 1e-4) |
| Cell 6 | PRIMME matrix-free matches ARPACK |
| Cell 7 | L=10 same |
| Cell 8 | L=12 returns finite near-zero \|λ\| without crash |

---

## If PRIMME is slow or fails on MF

1. Increase `maxiter`
2. Loosen `tol` to 1e-4 first
3. Try `which='SA'` on operator `K(x) = H(H(x))` then project back to H (folded spectrum)
4. Report wall time and any PRIMME stats if `return_stats=True`

---

## Expected known reference values (m₀=0.3, v=2, w=1)

| L | sep | typical soft \|λ\| (order of magnitude) |
|---|-----|----------------------------------------|
| 8 | 5 | ~0.0004, 0.0016, 0.0019, 0.0032 |
| 10 | 6 | ~0.0008, 0.0015, 0.0022, 0.0026 |

Paste Colab outputs back for interpretation.
