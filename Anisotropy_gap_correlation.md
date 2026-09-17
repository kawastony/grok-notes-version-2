# Correlation: anisotropy A vs eigenvalue gap Δλ

Tony Kawas / 17 September 2026.

**Data:** softest two modes from L=6,8,10 separation scan (12 points).  
\(\Delta\lambda = |\lambda_1|-|\lambda_0|\), \(A=\langle z^2\rangle/\langle x^2+y^2\rangle\).

---

## Point table

| L | d | Δλ | A₀ | A₁ | A_mean | \|A₀−A₁\| |
|---|---|------|------|------|--------|----------|
| 6 | 1 | 0.00346 | 0.70 | 0.72 | 0.71 | 0.02 |
| 6 | 2 | 0.00231 | 0.92 | 0.89 | 0.91 | 0.04 |
| 6 | 3 | 0.00234 | 0.30 | 0.32 | 0.31 | 0.02 |
| 8 | 1 | 0.00094 | 1.05 | 1.05 | 1.05 | 0.00 |
| 8 | 2 | 0.00426 | 0.83 | 1.01 | 0.92 | 0.18 |
| 8 | 3 | 0.00225 | 0.72 | 0.75 | 0.73 | 0.03 |
| 8 | 4 | 0.00120 | 0.45 | 0.97 | 0.71 | 0.51 |
| 10 | 1 | 0.00093 | 0.81 | 0.92 | 0.87 | 0.11 |
| 10 | 2 | 0.00308 | 0.55 | 1.02 | 0.78 | 0.46 |
| 10 | 3 | 0.00009 | 0.82 | 0.66 | 0.74 | 0.16 |
| 10 | 4 | 0.00065 | 0.85 | 0.85 | 0.85 | 0.01 |
| 10 | 5 | 0.00043 | 0.81 | 0.74 | 0.78 | 0.07 |

---

## Pearson correlations

| Pair | r (all points) |
|------|----------------|
| Δλ vs A_mean | **−0.10** (none) |
| Δλ vs A₀ | −0.25 (weak) |
| Δλ vs \|A₀−A₁\| | +0.11 (none) |
| λ₀ vs A_mean | **−0.57** (moderate) |
| λ₀ vs A₀ | −0.42 (mild) |

### Per L (small n)

| L | corr(Δλ, A_mean) | corr(Δλ, A₀) |
|---|------------------|--------------|
| 6 | +0.16 | +0.13 |
| 8 | +0.03 | +0.07 |
| 10 | +0.04 | −0.95* |

\*L=10 corr(Δλ,A₀)=−0.95 with only 5 points — not reliable as a law; dominated by single outliers.

---

## Interpretation

1. **No global law** linking gap Δλ to mean elongation A_mean across the scan.
2. **Milder signal:** softer ground eigenvalue λ₀ tends to sit with **slightly larger** A_mean (r≈−0.57 for λ₀ vs A_mean). Softer modes mildly prefer more elongated support — suggestive only.
3. **Shape splitting** \|A₀−A₁\| is large at some points (L=8 d=4, L=10 d=2) without a clean Δλ correlation.
4. Elongation/gravity narrative is **not** supported as “larger A ↔ smaller gap” in this window.

---

## Compact statement

Across L=6,8,10, soft-mode anisotropy A and the soft gap Δλ are essentially **uncorrelated** (r≈−0.1). A moderate anticorrelation between the softest \|λ\| and A_mean (r≈−0.57) is the only mild spectral–shape link. A remains a valid shape diagnostic; it does not track hybridization splitting in a simple way at these volumes.
