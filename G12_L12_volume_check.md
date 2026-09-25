# L=12 volume check (dS + Tr PQ)

**Date:** 2026-09-25  
**Status:** Attempted in sandbox — **not residual-gated success**.

## Goal

Repeat the boost-path subspace diagnostics at L=12, d=3:
- subspace dS(s)
- projector continuity Tr(PQ)
- endpoint G_subspace

to test whether L=10 results survive a larger volume.

## What failed in the sandbox

### 1. Sparse eigsh with shift-invert (sigma=0)

- Built H successfully (nnz≈193512, N=13824).
- Process **Killed** during factorization / ARPACK shift-invert (OOM).
- Same failure on a 5-point and a 3-point path.

### 2. LOBPCG on H² (folded spectrum)

Ran endpoint-only (s=0 and s=1) without shift-invert:

| s | reported \|λ\| | dS | H-residual scale |
|---|---------------|-----|------------------|
| 0.0 | ~0.017–0.023 | ~0 | ~0.017–0.023 |
| 1.0 | ~0.014–0.021 | +0.0025 | ~0.014–0.021 |

**Problems:**

- L=10 residual-gated soft multiplet sits at \|λ\|~10⁻³. LOBPCG here returned **~10⁻²** modes with residual **of the same order** as the eigenvalue — not soft, not residual-gated.
- Endpoint Tr(PQ)≈0.74 with singular values (0.55, 0.52, 0.32, 0.27) — not comparable to L=10 bottleneck continuity.
- G_subspace ≈ +0.049 has the **opposite sign** to L=10 d=3 (G≈−0.18) and must **not** be interpreted as a volume-confirmed result.

## Honest conclusion

| Claim | Status |
|-------|--------|
| L=12 residual-gated soft multiplet resolved in this sandbox | **No** |
| L=12 dS / Tr(PQ) path continuity validated | **No** |
| L=10 propagation results volume-checked | **Still open** |

L=12 needs either:
- more RAM for shift-invert ARPACK/PRIMME, or
- a better soft-mode eigensolver (PRIMME / JD with proper targeting), or
- Colab / external machine.

## Recommended Colab cell (shift-invert)

```python
# L=12 d=3 endpoint + mid boost: requires ~high-RAM runtime
# Reuse build_sparse_H from L10 notebook; then:
from scipy.sparse.linalg import eigsh

L, d, eps, v0 = 12, 3, 0.05, 2.0
s_vals = [0.0, 0.5, 1.0]
# ... set cores, defects as before ...

rows = []
V_prev = None
for s in s_vals:
    v1 = v0 * (1 + s * eps)
    H = build_sparse_H(L, defects, m0, [v1, v0], ww, r_wilson)
    ev, evec = eigsh(H, k=4, sigma=0.0, which='LM', maxiter=12000, tol=1e-8)
    # residual gate rel <= 1e-6, subspace dS, optional PT vs V_prev
    ...
```

Target: recover soft \|λ\| ≲ few×10⁻³ with rel ≲ 10⁻⁶, then compare dS and Tr(PQ) to L=10.

## Data

`data/G12_L12_dS_TrPQ.json` — LOBPCG attempt only; **do not treat as soft-sector physics**.

## Related

- `G12_PT_flow_and_d5.md` — L=10 results that remain the baseline
- `G12_subspace_and_d5_scan.md`
