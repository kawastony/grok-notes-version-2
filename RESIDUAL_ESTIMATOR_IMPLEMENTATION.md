# Residual correlation estimator — implementation note

**Status:** Working synthetic demo of the protocol in RESIDUAL_CORRELATION_ESTIMATOR_SPARC.md. Real SPARC tables not present in this environment; logic is ready to point at prepared data.

Review paste considered: specialized kernels + estimator are the right next layer; channel identifiability and centering choice remain open (noted below).

---

## Implemented steps

1. Population fit: `mu_hat_i = mu_star + S X_i` via least squares.
2. Residuals: `e_i = mu_hat_i - (mu_star_hat + S_hat X_i)` — **no refit of μ_*** after residual definition.
3. `C_ee(ΔX)`: mean product of centered residuals in bins of |X_i − X_k|.
4. Shuffle null: permute e, rebuild max|C|; report p-value.
5. Optional exp fit: C(Δ) ≈ C₀ e^{−Δ/ξ}.
6. Radial stack: within-galaxy e(r) against population ℛ^model; stack C_μ(Δr); exp fit ξ_μ.

Synthetic demo output (seed 7):
- recovered μ_* ≈ 0.098 (truth 0.10), mean e ≈ 0
- shuffle p(max|C_ee|) ≈ 0.04 (structured component injected)
- radial ξ_μ fit available when profiles used

Artifact: `residual_estimator_demo_gal.csv` (local artifacts).

---

## Centering choice (review point)

Demo centers residuals **over the ensemble** after the population fit. Alternatives to report in real runs:
- path-centered (for lattice A_c),
- ensemble-centered (galaxies),
- patch-centered (meso map).

State which in every table.

---

## Channel identifiability (review point)

κ_Δ, κ_λ, κ_G may not separate if Δ, λ_soft, G12 co-vary. Protocol:
1. Report pairwise correlations among {f(Δ), g(λ), h} on lattice paths.
2. If corr high, fit a single activity direction (PCA / one κ on A_c) as primary.
3. Keep three-channel form only when partial correlations justify it.

---

## Real SPARC hook

Replace synthetic `mu_hat`, `X` with outputs of latent-r_p / common-intercept pipeline. Keep e defined from frozen (μ_*, S). Pre-register binning and ℛ^model family.
