# Residual correlation estimator for hierarchical SPARC

**Purpose:** Concrete, non-circular estimator of C_μ(r) and related residual structure after de-dressing — the meso observable targeted by the micro→meso map.

Depends on: non-circular μ̂ protocol (residual-inflection / latent-r_p), not on TAFA-predicted μ law for defining the residual itself.

---

## 1. Per-galaxy residual field

For galaxy i, radii r_{ij}:

\[
g_{\mathrm{obs}}=V_{\mathrm{obs}}^2/r,
\qquad
g_b=V_b^2/r,
\qquad
\mathcal{R}_{ij}=g_{\mathrm{obs}}/g_b.
\]

From hierarchical / latent model (or fixed de-dressing):
\[
\widehat\mu_i = \mu_* + S\,X_i + \eta_i,
\qquad
X_i=(\Sigma_{b,i}/\Sigma_{\mathrm{ref}})^{1/7}.
\]

Define a **local residual** that does not re-fit μ_*:
\[
e_{ij}
=
\ln\mathcal{R}_{ij}
-
\ln\mathcal{R}^{\mathrm{model}}_{ij}(\widehat\mu_i,S,X; r_{ij})
\]
where ℛ^model is the monotone transition profile already used in the latent-r_p model (logistic or equivalent), evaluated at the **posterior mean** (or fixed) (μ_*, S) from the population fit — not re-optimized per residual bin.

If only one μ̂_i per galaxy (first-pass):
\[
e_i = \widehat\mu_i - (\mu_* + S X_i)
\]
(galaxy-level residual of the intercept equation).

---

## 2. Galaxy-level correlation estimator (first pass)

Treat each galaxy residual e_i and a scale proxy ℓ_i (e.g. R_disk, R_eff, or r_p̂):

**Bin by separation of galaxy properties**, not on-sky angle (rotation curves are 1D):

Option A — residual–residual among galaxies with similar X:
\[
\hat C_{ee}(\Delta X)
=
\mathrm{mean}\{e_i e_k:\ |X_i-X_k|\in\mathrm{bin}\}
-
\bar e^2.
\]

Option B — residual vs micro-inspired scale:
\[
\hat C_{e\ell}(\Delta\ell)
=
\mathrm{mean}\{e_i e_k:\ |\ell_i-\ell_k|\in\mathrm{bin}\}.
\]

Null: white residuals ⇒ Ĉ ≈ 0 for ΔX, Δℓ > 0 after mean subtraction.

---

## 3. Radial correlation estimator (when full ℛ(r) used)

Within galaxy i, after subtracting the population model profile:
\[
\hat C_i(\Delta r)
=
\frac{1}{N_{\Delta r}}\sum_{|r_j-r_k|\approx\Delta r} e_{ij} e_{ik}.
\]

Stack:
\[
\hat C_\mu(\Delta r)
=
\mathrm{mean}_i\ \hat C_i(\Delta r)
\quad\text{(weight by N_points or inverse variance)}.
\]

Fit forms:
\[
C(\Delta r)\approx C_0 e^{-\Delta r/\xi_\mu}
\quad\text{or}\quad
C_0 (\Delta r/\xi_\mu)^{-\eta}e^{-\Delta r/\xi_\mu}.
\]

**Report:** ξ_μ, C_0, η (if used), bootstrap errors, and comparison to ⟨Δ⟩/tube-width order from lattice (qualitative only until unit map exists).

---

## 4. Pipeline (ordered)

1. Run latent-r_p / common-intercept fit → (μ_*, S, τ_μ), μ̂_i or full ℛ^model.
2. Form e_i or e_{ij} **without** refitting μ_*.
3. Compute Ĉ_ee, Ĉ_eℓ, and/or stacked Ĉ_μ(Δr).
4. Fit ξ_μ; test vs white-noise null (shuffle residuals, rebuild Ĉ).
5. Optional: split HSB/LSB/dwarf; demand ξ_μ stable if micro-inherited.

---

## 5. Link to specialized micro map

| Micro prediction | Estimator test |
|------------------|----------------|
| ⟨δμ⟩=0 | mean e ≈ 0 after de-dressing |
| Var(δμ)∝⟨A_c²⟩ | τ_μ or Var(e) correlates with activity proxies if available |
| ξ_μ ~ ⟨Δ⟩ / tube width | fitted ξ_μ in same ballpark as lattice separation scale (order-of-magnitude) |
| C_μ not white | shuffle-null rejected |

---

## 6. Circularity guards

- Do not define e using a μ(r) law that already assumes C_μ(r).
- Pre-register binning and ℛ^model family.
- Primary: shuffle null on residuals.
- Secondary: stability across estimator A/B/C for μ̂ from earlier protocol.

---

## 7. Status

Concrete estimator definitions ready for implementation when SPARC tables are prepared. Specialized micro kernels supply the *form* of the prediction (stable mean, structured C_μ); estimator supplies the *measurement*. Absolute SI match of ξ_μ to lattice Δ still requires the one dimensionful bridge.
