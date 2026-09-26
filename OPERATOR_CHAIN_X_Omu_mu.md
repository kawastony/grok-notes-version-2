# Operator chain: X → O_μ → μ → a_eff

**Goal:** turn placeholders into defined objects (Papers 24–25).  
**Status labels:** Defined | Geometric estimate | Open from full action

---

## 1. X — mismatch field

**Definition (Paper 25):** localized mismatch mode identified with the low-lying **inter-sector mass mismatch** in the defect sector.

**EFT content:** scalar in the minimal Euclidean defect Lagrangian
\[
\mathcal{L}_{\rm def}=\tfrac12(\partial X)^2+\tfrac12(\partial Y)^2+\frac{g_1}{2}X^2 Y+\frac{g_2}{6}Y^3
\]
in d = 6−ε. Physical branch: g_2 = 0.

**Sourcing (scaffold, Paper 24 / synthesis Paper 25):**
\[
X \sim \Sigma_b^{1/n}\quad\text{with }n=n_{\rm eff}.
\]
Paper 24’s compact scaffold used n=3 (cubic); Paper 25 synthesis uses n_eff=8 from winding. **Both are stated assumptions/estimates, not action theorems.**

**Scaling dimension (Paper 25 RG):**
\[
\eta_X^*\approx\frac{2\varepsilon}{13}\xrightarrow{\varepsilon=1}\frac{2}{13},\qquad
\Delta_X=\frac{d-2+\eta_X^*}{2}=\frac{24}{13}\approx 1.846.
\]

**Status:** Defined as EFT field + RG dimension. Microscopic identification with cone defect residual is motivated, not closed from full TAFA action.

---

## 2. O_μ — transmission / response operator

**Definition (Paper 25 §5.2):** boundary / transmission operator spanning the galactic junction (d′=3 cone sector).

**Geometry:** angular sector [ψ_1, ψ_2] = [35°, 70°] with mixed BC:
- inner (baryonic) ψ_1=35°: Neumann Φ′=0
- outer (sovereign) ψ_2=70°: Dirichlet Φ=0

**Eigenvalue:** numerical Legendre determinant → ν_0 ≈ 2.31.

**Scaling dimension:**
\[
\Delta_\mu = \nu_0 \approx 2.31
\]
for a boundary operator on a d′=3 defect.

**Scaffold (Paper 24):** O_μ ∼ (−∇²)^{−α} X with Δ_μ/Δ_X = 3/7 (chosen to recover 1/7 when combined with X∼Σ_b^{1/3}). That ratio is **scaffold bookkeeping**, not the same object as the geometric ν_0.

**Status:** Geometric eigenvalue Δ_μ≈2.31 is a concrete definition. Link of this operator to the fractional inverse-Laplacian scaffold is not yet derived as identity.

---

## 3. μ — observable response scale

**Phenomenology (Paper 24):** the scale controlling a_eff in
\[
a_{\rm eff}=A\sqrt{2\kappa_0}\,\Bigl(\frac{\Sigma_b}{\Sigma_{\rm ref}}\Bigr)^\gamma
\]
(or earlier radius-law forms). μ is the object that carries the structure dependence (Σ_b^γ or the falsified 1/R_d).

**BTFR embedding:**
\[
V_{\rm flat}^4 = G M_b\, a_{\rm eff}(μ,\ldots).
\]

**Status:** Operationally defined by the fit models. Microscopic operator → μ map is the open middle of the chain.

---

## 4. Chain equation (Paper 25 synthesis)

\[
\gamma = \frac{\Delta_\mu}{n_{\rm eff}\,\Delta_X}
= \frac{2.31}{8\times 1.846}\approx 0.156.
\]

Compared to data: 0.144±0.060 (within ~0.2σ).

**n_eff=8:** N_wind = 2π/Δψ = 72/7 ≈ 10.286, ⌊N_wind⌋−2 = 8 (boundary reduction estimate).

---

## 5. What is still open

| Link | Gap |
|------|-----|
| Full TAFA action → L_def | projector/kernel dependent |
| Why X ∼ Σ_b^{1/n} with n=8 (or 3) | sourcing rule not derived from action |
| O_μ (Legendre ν_0) ≡ fractional scaffold | not shown |
| μ as unique readout of O_μ[X] | phenomenological |
| A, κ_0 from same action | amplitude layer separate |

---

## One-sentence chain status

X and O_μ now have EFT/geometric definitions and dimensions; the map cone/action → those objects → μ → a_eff is **modeled consistently** but **not derived** from a single varied TAFA action.
