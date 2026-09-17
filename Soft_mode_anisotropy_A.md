# Soft-mode anisotropy A

Tony Kawas / 17 September 2026.

**Definition** (pair axis = z, origin = pair midpoint, min-image coordinates):

\[
A = \frac{\langle z^2\rangle}{\langle x^2+y^2\rangle}
\]

- \(A > 1\): more elongated along the pair axis  
- \(A < 1\): more extended in the transverse plane  
- \(A \sim 1\): roughly isotropic second moments

**Operator:** same as molecular scan (m₀=0.3, v=2, w=1).  
**Data:** `anisotropy_scan.json`

---

## Results (softest two modes)

### L = 6

| d | A₀ | A₁ | mean A |
|---|------|------|--------|
| 1 | 0.70 | 0.72 | 0.71 |
| 2 | 0.92 | 0.89 | 0.91 |
| 3 | 0.30 | 0.32 | **0.31** |

### L = 8

| d | A₀ | A₁ | mean A |
|---|------|------|--------|
| 1 | 1.05 | 1.05 | **1.05** |
| 2 | 0.83 | 1.01 | 0.92 |
| 3 | 0.72 | 0.75 | 0.73 |
| 4 | 0.45 | 0.97 | 0.71 |

### L = 10

| d | A₀ | A₁ | mean A |
|---|------|------|--------|
| 1 | 0.81 | 0.92 | 0.87 |
| 2 | 0.55 | 1.02 | 0.78 |
| 3 | 0.82 | 0.66 | 0.74 |
| 4 | 0.85 | 0.85 | 0.85 |
| 5 | 0.81 | 0.74 | 0.78 |

---

## Observations

1. **A is O(1)** — soft modes are not extremely needle-like or pancake-like at these volumes.
2. **Mild elongation** appears at small d on L=8 (A≈1.05).
3. **Transverse preference** at L=6, d=3 (max separation): A≈0.31.
4. **Mode splitting in shape:** sometimes A₀ and A₁ differ strongly (e.g. L=8 d=4: 0.45 vs 0.97; L=10 d=2: 0.55 vs 1.02) — soft pair is not always shape-degenerate.
5. **No monotonic “larger d → larger A”** law in this window.

---

## Link to elongation / gravity sketch

| Claim | Support from A scan |
|-------|---------------------|
| Soft support has a measurable shape | **Yes** |
| Shape varies with (L,d) | **Yes** |
| Elongation tracks a gravity-like force law | **Not tested** — no force observable |
| A is the paper cone opening angle | **No** — different definition |

A is a legitimate **interior shape diagnostic**. It does not by itself establish gravitational dynamics.

---

## Compact statement

Soft-mode anisotropy \(A=\langle z^2\rangle/\langle x^2+y^2\rangle\) is computable and O(1) across L=6,8,10. It varies with separation and can differ between the two softest modes. This supplies a concrete elongation proxy for future correlation with Δλ or P_rest; it is not evidence for gravity.
