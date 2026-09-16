# Pair scale-up: L = 10 (and L = 12 attempt)

Tony Kawas / 16 September 2026.

---

## L = 10, sep = 6 — completed

N = 8 000. Assemble ∼0.4 s, eigsh ∼13 s.

| Mode | \|λ\| | P(+core) | P(−core) | Owner |
|------|-------|----------|----------|-------|
| 0 | 0.00065 | 0.037 | 0.037 | shared |
| 1 | 0.00085 | 0.028 | 0.028 | shared |
| 2 | 0.00294 | 0.025 | 0.025 | shared |
| 3 | 0.00305 | 0.067 | 0.067 | shared |

- Softest pair still near zero; Δλ ≈ 0.0015.  
- Weight remains equal on both cores (hybridized).  
- Absolute P_core lower than at L = 7 (fixed diagnostic ball R = 2 in a larger volume dilutes the fraction; modes not yet tightly core-bound).

## L = 12, sep = 8 — OOM

N = 13 824. Sparse H assembled; ARPACK shift-invert was killed (exit 137, memory). This environment’s RAM ceiling sits between L = 10 and L = 12 for the present dense-factorization path inside eigsh(sigma=0).

---

## Updated scaling table

| L | sep | softest \|λ\| | P per core | Owner | Notes |
|---|-----|--------------|------------|-------|-------|
| 6 | ∼3 | 0.001 | ∼0.05–0.15 | shared | |
| 7 | 4 | 0.008 | ∼0.25 | shared | peak P in this window |
| 8 | 5 | 0.0008 | ∼0.10 | shared | |
| **10** | **6** | **0.00065** | **∼0.03–0.07** | **shared** | |
| 12 | 8 | — | — | — | OOM |

---

## Interpretation

Through L = 10 the system remains in the **molecular regime**: soft hybridized modes, no preferred-core assignment. Softening continues; independent localization has not yet set in at sep = 6.

Possible reasons P_core did not rise:
1. Fixed ball R = 2 under-covers a mode that is still somewhat extended.  
2. Residual overlap at sep = 6 is still large compared with the mode size.  
3. Wilson/mass window still leaves the would-be zero modes only moderately localized.

---

## Practical path forward in this environment

- L ≤ 10 is the reliable ceiling for full ARPACK shift-invert here.  
- Options for larger L:  
  - iterative solvers without factorization (LOBPCG / Jacobi–Davidson on H² near 0),  
  - thicker diagnostic analysis at L = 10 with varied R and narrower core width w,  
  - or external batch resources for L ≥ 12.

**Immediate low-cost test:** re-run L = 10 with narrower core (w ∼ 0.9–1.0) and/or larger diagnostic R to see whether preferred-core assignment appears before leaving the available volume range.

---

## Compact statement

L = 10, sep = 6 still shows soft, equally shared modes. The molecular regime persists. L = 12 exceeds memory for the current eigensolver path. Next low-cost probes: narrower core width and adjusted diagnostic radius at L = 10, before requiring larger-volume resources.
