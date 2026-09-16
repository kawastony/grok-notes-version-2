# Folded-spectrum (H²) soft-mode extraction

Tony Kawas / 16 September 2026.

---

## Method

Target soft modes of Hermitian H via

\[
K = H^2,\qquad K\psi = \lambda^2 \psi.
\]

Lowest eigenvalues of K correspond to smallest |λ| of H. After obtaining a low subspace U of K, recover signed eigenvalues by dense projection:

\[
H_{\rm sub} = U^\dagger H U,\qquad H_{\rm sub} C = \lambda C,\qquad \Psi = U C.
\]

---

## Validation (sparse K = H @ H)

| L | H soft \|λ\| (direct) | recovered from K | max \|λ\| diff | subspace overlap |
|---|----------------------|------------------|---------------|------------------|
| 6 | 0.00831, 0.00880, 0.01105, 0.01404 | identical | 2e-16 | 1.0 |
| 10 | 0.00078, 0.00150, 0.00220, 0.00264 | identical | 3e-16 | 1.0 |

**Concept is correct.** Sparse K + `eigsh(K, sigma=0)` recovers soft modes exactly.

---

## Matrix-free attempts

| Method | Result |
|--------|--------|
| `eigsh(K, which='SA')` matrix-free | No convergence (3000–8000 iter) |
| `lobpcg(K, largest=False)` | Wrong subspace; poor overlaps (~0.1–0.3); μ not matching λ² |
| `eigsh(K, which='SA')` sparse | Also fails without shift-invert |
| `eigsh(K, sigma=0)` sparse | **Works** |

**Diagnosis:** The bottom of the spectrum of K is not easily captured by pure extremal Lanczos/LOBPCG without shift-invert or a preconditioner. Shift-invert on K requires solving Kx = b (i.e. H²x = b), which is expensive matrix-free.

---

## Practical status

| Path | L ≤ 10 | L ≥ 12 |
|------|--------|--------|
| Explicit sparse H + shift-invert | Working (existing) | Memory risk |
| Sparse K = H@H + shift-invert | Working, validated | K denser (nnz grows); memory risk |
| Matrix-free H matvec | Working through L=14 | OK |
| Matrix-free H² extremal (SA / LOBPCG) | Not converging | Needs preconditioner or filter |
| Matrix-free H² + iterative shift-invert | Not yet | Hard without good preconditioner |

---

## What this means for Branch 6

Matrix-free removes the **operator storage** wall (L=12–14 matvec OK). It does **not** yet remove the **near-zero eigensolve** wall. Folded spectrum is conceptually right but still needs either:

1. Sparse factorization at moderate L, or
2. A preconditioned iterative method / polynomial filter for matrix-free K.

---

## Compact statement

H² folded-spectrum extraction is validated exactly against direct soft modes at L=6 and L=10 when K is stored sparsely and shift-inverted. Pure matrix-free extremal solvers (SA / LOBPCG) do not converge to the soft sector without preconditioning. The next numerical step is a preconditioner or Chebyshev filter for matrix-free K, or accepting sparse shift-invert up to the memory limit.
