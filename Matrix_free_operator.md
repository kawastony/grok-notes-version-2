# Matrix-free Wilson–Dirac + hedgehog operator

Tony Kawas / 16 September 2026.

---

## Goal

Remove explicit sparse-matrix storage so that L ≥ 12 becomes feasible under the current memory ceiling.

---

## Implementation

Vectorized matvec (no site Python loop):

1. Precompute onsite 8×8 matrix M(x) at every site (mass + Wilson diagonal + hedgehog texture).
2. Apply
   \[
   (D\psi)(x) = M(x)\psi(x) + \sum_\mu \bigl[A_\mu \psi(x+\hat\mu) + B_\mu \psi(x-\hat\mu)\bigr]
   \]
   with NumPy `roll` for neighbors and `einsum` for 8×8 blocks.
3. Multiply by γ₅ to form Hermitian H = γ₅ D.

Wrapped as `scipy.sparse.linalg.LinearOperator` for Krylov solvers.

---

## Validation

| Check | Result |
|-------|--------|
| Hermitian residual \|⟨u\|Hw⟩ − ⟨Hu\|w⟩\| | O(10⁻¹⁶–10⁻¹⁷) at L = 6…14 |
| Matvec structure | Matches prior sparse assembly formula |

---

## Timing and memory (m₀=0.3, v=2, w=1)

| L | N = 8L³ | onsite build | matvec | OOM? |
|---|---------|--------------|--------|------|
| 6 | 1 728 | 0.01 s | 0.4 ms | no |
| 8 | 4 096 | 0.01 s | 0.6 ms | no |
| 10 | 8 000 | 0.03 s | 1.2 ms | no |
| **12** | **13 824** | 0.05 s | 1.9 ms | **no** |
| **14** | **21 952** | 0.07 s | 3.2 ms | **no** |

Previously L = 12 exited with OOM under explicit sparse assembly. Matrix-free removes that barrier.

---

## Remaining bottleneck: near-zero eigensolve

`eigsh(..., sigma=0)` on a `LinearOperator` uses iterative shift-invert (inner GMRES/MINRES). That is much slower than factorizing an explicit sparse matrix. At L ≥ 8 the shift-invert path times out in the present environment before converging soft modes.

**Next steps for soft-mode extraction at L ≥ 12:**

1. LOBPCG / Jacobi–Davidson style solvers aimed at the origin.
2. Explicit sparse CSR still for L ≤ 10 (fast shift-invert), matrix-free only when assembly OOMs.
3. Optional: polyharmonic or Chebyshev filters to amplify near-zero modes without shift-invert.
4. Numba/JAX acceleration of matvec if iteration counts become large.

---

## Compact statement

A vectorized matrix-free apply_H for the 8-component Wilson + Callias hedgehog is implemented and Hermitian to machine precision. Matvec runs at L = 12 and L = 14 without OOM (previously impossible). Soft-mode eigensolves at these sizes still need a solver strategy that does not rely on expensive iterative shift-invert, or longer runtimes.
