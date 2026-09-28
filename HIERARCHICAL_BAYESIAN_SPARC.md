# Hierarchical Bayesian methods for SPARC midpoint + residuals

**Status:** Method exploration linking latent-r_p (PyMC/Stan starters) to residual-correlation tests and the micro→meso map.

---

## 1. Why hierarchical Bayes here

| Problem | Hierarchical Bayes role |
|---------|-------------------------|
| Short disks / censored r_p | Latent r_{p,i} with one-sided posteriors |
| Universal μ_* vs galaxy scatter | μ_i ~ N(μ_* + S X_i, τ_μ²) |
| Residual structure | Model e_i or spatial ζ_struct with covariance C_μ |
| Channel weights κ̂ | Hierarchical priors on relative κ; partial pooling |
| Null comparison | LOO / WAIC: dressing vs no-dressing vs free intercepts |

Point-estimate max-slope pipelines fail on truncation; hierarchical models absorb that uncertainty into posteriors.

---

## 2. Core population model (recap)

\[
\mathcal R_{ij}^{\mathrm{obs}} \sim \mathcal N\bigl(1 + A_i F(r_{ij}/r_{p,i}, w_i),\,\sigma_{ij}^2+\sigma_{\mathrm{int}}^2\bigr)
\]
\[
\mu_i = 1/r_{p,i},\qquad
\mu_i \sim \mathcal N(\mu_* + S X_i,\,\tau_\mu^2).
\]

Priors (weak, free μ_* by default):
- μ_* ~ HalfNormal or TruncatedNormal(0,1)
- S ~ Normal(0,1)
- τ_μ ~ HalfNormal(0.5)
- optional soft prior on μ_* only for sensitivity, not primary

---

## 3. Residual layer (Bayes)

After (or jointly with) the population model:

**Galaxy-level residuals**
\[
e_i = \mu_i - (\mu_* + S X_i)
\]
are already the η_i in the hierarchical equation; posterior of {e_i} is immediate.

**Structured residual model (extension)**
\[
e \sim \mathcal N(0,\, \tau_\mu^2 I + \sigma_C^2 C_\mu(\xi_\mu))
\]
with C_μ(ξ_μ) an exponential or Matérn correlation in X-space or in radial lag (for within-galaxy e(r)).

Infer ξ_μ jointly; compare LOO against white τ_μ² I only.

---

## 4. Linking micro κ̂ (optional hierarchy)

If lattice-derived activity features Z_i = (f(Δ), g(λ), h)_i exist per galaxy (or per environment bin):
\[
\mu_i \sim \mathcal N(\mu_* + S X_i + Z_i\cdot\kappa,\,\tau_\mu^2)
\]
with
\[
\kappa \sim \mathcal N(0,\,\tau_\kappa^2 I)\quad\text{or simplex prior on relative weights.}
\]

Test: does including Z improve LOO without shifting μ_* (non-propagation)?

If Z channels collinear → single activity score A_i = Z_i·u (PCA) and one κ.

---

## 5. Model comparison set

| Model | Structure |
|-------|-----------|
| M0 | μ_i ~ N(μ_*, τ²) — no dressing |
| M1 | μ_i ~ N(μ_* + S X_i, τ²) — Σ_b^{1/7} dressing |
| M2 | M1 + structured C_μ(ξ) |
| M3 | M1 + lattice activity Z·κ |
| M4 | free μ_{*,i} (no universal intercept) |

Primary evidence: LOO/WAIC. Secondary: posterior of μ_* vs external benchmark (e.g. 1/12.1 kpc) **after** free fit.

---

## 6. Implementation stack

| Piece | Tool |
|-------|------|
| Latent r_p + ℛ profile | PyMC or Stan (existing starters) |
| Structured residual cov | PyMC MVNormal / LKJ or Stan cov_exp_quad |
| LOO | ArviZ `az.compare` |
| Residual Ĉ diagnostics | `residual_correlation_estimator.py` on posterior means or draws |

Workflow:
1. Fit M1 (and M0, M4) with free μ_*.
2. Posterior predictive e_i; run shuffle / Ĉ diagnostics.
3. Fit M2; test ξ_μ > 0 vs white.
4. If lattice Z available, fit M3; check μ_* stability.

---

## 7. Guardrails

- Default: free μ_* (no hard 12.1 kpc prior).
- Structured C_μ is a **test of residual form**, not a back-door to fit μ_*.
- One-input boundary: absolute SI scale still calibrated or Pathway-1 bridged.
- Wilson / lattice artifacts must be controlled before Z enters M3.

---

## 8. Status

Hierarchical Bayes is the natural statistical home for latent-r_p, universal intercept tests, and residual correlation. Estimator script covers frequentist diagnostics; this note covers the Bayesian model ladder and LOO comparison plan.
