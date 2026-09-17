# PRIMME solver investigation

Tony Kawas / 17 September 2026.

---

## What PRIMME is

**PRIMME** = PReconditioned Iterative MultiMethod Eigensolver (Stathopoulos et al.).

- Large-scale **Hermitian / real symmetric** eigenproblems
- Matrix-free: only needs matvec (and optional preconditioner)
- Targets: largest, smallest, or **interior** eigenvalues
- Methods: GD+k, JDQMR, LOBPCG-like, dynamic selection
- Designed for hard problems where ARPACK/Lanczos struggle (interior spectrum, clustering, preconditioning)

Python package: `pip install primme` → `primme.eigsh` API similar to `scipy.sparse.linalg.eigsh`.

---

## Why it matters for this project

| Need | scipy ARPACK | LOBPCG | PRIMME |
|------|--------------|--------|--------|
| Soft modes near 0 (interior) | shift-invert (needs solve) | extremal only unless shifted | **native interior** (`which='SM'` or `sigma=0`) |
| Matrix-free | yes, but SI slow | yes | **yes** |
| Preconditioning | via SI | optional | **first-class** |
| Clustered soft pairs | fragile | sensitive to X0 | **block GD / locking** |

Our bottlenecks:
1. Sparse L≥12 OOM
2. Matrix-free `eigsh(sigma=0)` = iterative SI, too slow
3. H² SA/LOBPCG no convergence without preconditioner

PRIMME’s interior + matrix-free + optional preconditioner is the closest match among production libraries.

---

## Relevant API (Python)

```python
import primme
from scipy.sparse.linalg import LinearOperator

Hop = LinearOperator((N, N), matvec=apply_H, dtype=np.complex128)

# eigenvalues closest to 0
evals, evecs = primme.eigsh(
    Hop, k=4,
    which='SM',          # smallest magnitude ≈ near zero
    # or: sigma=0.0, which='SM'
    tol=1e-6,
    maxiter=10000,
    # OPinv=precond_LinearOperator,  # optional
)
```

Also supports:
- `method='PRIMME_JDQMR'` / `PRIMME_GD_plusK` / dynamic default
- block size for multiplicity
- locking of already converged vectors

---

## Preconditioning options for our H

Without a cheap approximate inverse, interior methods still need many matvecs. Possible preconditioners:

1. **Diagonal / Jacobi** of onsite blocks (cheap, weak)
2. **Polynomial** (Chebyshev) approximate inverse near 0
3. **Sparse incomplete factorization** of a coarse or truncated H (if memory allows at moderate L)
4. None first — test pure PRIMME interior on L=8/10 vs known soft modes

---

## Status in this environment

| Item | Status |
|------|--------|
| `primme` package installed | **No** (`pip install` timed out / not present) |
| scipy only | 1.17.x |
| Can evaluate PRIMME theory | Yes |
| Can run PRIMME on hedgehog H | **Not yet** — needs install |

---

## Recommended trial plan (when PRIMME available)

1. **L=8 validation** — `primme.eigsh(H_sparse or LinearOperator, k=4, which='SM')` vs ARPACK soft modes; check |λ| and subspace overlap.
2. **L=10 same**.
3. **L=12 matrix-free** — no sparse storage; only matvec + PRIMME workspace (vectors).
4. If slow: add Jacobi preconditioner from onsite blocks; retry.
5. Track χ_βn and ownership on any new soft modes.

---

## Relation to H² approach

PRIMME can also target **smallest algebraic** eigenvalues of K = H² (`which='SA'`), recovering soft modes of H without explicit shift-invert of H — same idea as our folded spectrum, but with a stronger Davidson/JDQMR iteration than plain LOBPCG.

---

## Compact statement

PRIMME is the most appropriate production solver for matrix-free near-zero modes of Hermitian H: interior targeting, block methods, preconditioning. It is not installed in the current sandbox (`pip install primme` did not complete). When available, validate on L=8/10 against ARPACK, then attempt L=12 matrix-free soft-mode extraction. Until then, L≤10 remains the reliable physics window.
