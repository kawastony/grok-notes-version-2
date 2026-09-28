# Specialized coarse-graining: G12 + Δ only

**Status:** First reduction of COARSE_GRAINING_MICRO_TO_MESO.md. Concrete kernels for the dominant lattice observables. Still schematic in SI units; no derivation of μ_*.

---

## 1. Restricted micro inputs

Per defect-pair cell c, along path s:

| Symbol | Meaning |
|--------|--------|
| Δ^{(c)}(s) | Core separation |
| P₁^{(c)}(s), P₂^{(c)}(s) | Soft weight on core1 / core2 |
| G₁₂^{(c)}(s) ≡ d(P₁−P₂)/ds | Weight-slide rate (active exchange) |
| λ_soft^{(c)}(s) | Softest \|λ\| (or mean of soft multiplet) |
| Q₁, Q₂, ℐ | Topological lock (must stay fixed) |

Lock:
\[
L_c = \mathbf{1}\![|Q_i-Q_{i0}|<\varepsilon_Q\ \&\ |\mathcal{I}-\mathcal{I}_0|<\varepsilon_\mathcal{I}].
\]

Activity (specialized):
\[
A_c = \alpha_\Delta |\partial_s\Delta|
+ \alpha_G |G_{12}|
+ \alpha_\lambda |\partial_s\lambda_{\mathrm{soft}}|.
\]

---

## 2. Specialized kernels f, g, h

**Endpoint / separation (f)**  
Well deepens as cores approach (endpoint-compactification contact):
\[
f(\Delta) = \left(\frac{\Delta_0}{\Delta}\right)^p - 1,
\qquad p\in\{1,2\}\ \text{(try }p=1\text{ first)}.
\]
Zero at Δ=Δ₀ (reference separation); positive when compressed.

**Soft spectrum (g)**  
Softer modes ⇒ larger local dressing amplitude:
\[
g(\lambda_{\mathrm{soft}}) = \frac{\lambda_{\mathrm{ref}}}{\lambda_{\mathrm{soft}}+\epsilon}-1
\quad (\epsilon\to 0^+\ \text{regulator)}.
\]

**Weight redistribution (h)**  
Imbalance relative to equal share:
\[
h = (P_1-P_2)^2
\quad\text{or}\quad
h = |G_{12}|\ \text{(rate form along path)}.
\]
Squared imbalance is path-reparameterization friendlier for static snapshots.

---

## 3. Local δμ_c

\[
\delta\mu_c
=
L_c\Bigl(
\kappa_\Delta f(\Delta)
+\kappa_\lambda g(\lambda_{\mathrm{soft}})
+\kappa_G h(P_1,P_2,G_{12})
\Bigr)
- \overline{(\cdots)}
\]
where the bar subtracts the sample mean so ⟨δμ_c⟩=0 (non-propagation of the first moment).

Dimensionless path form (preferred until SI map exists):
\[
\widehat{\delta\mu}_c
=
L_c\Bigl(
\hat\kappa_\Delta f(\Delta)
+\hat\kappa_\lambda g(\lambda)
+\hat\kappa_G h
\Bigr)_{\mathrm{centered}}.
\]
Overall scale of δμ absorbed into meso σ later (one-input / calibration).

---

## 4. Meso field and variance

\[
\delta\mu(x)=\sum_c W_c(x)\,\delta\mu_c,
\qquad
W_c(x)\propto \rho_{\mathrm{def}}(x)\,e^{-|x-x_c|/\xi_{\mathrm{tube}}}.
\]

\[
\mathrm{Var}(\delta\mu)\propto \langle A_c^2\rangle\,\xi_{\mathrm{tube}}^{d_{\mathrm{eff}}}.
\]

Correlation length guess from lattice:
\[
\xi_\mu \sim \langle\Delta\rangle\ \text{or}\ \text{soft-tube half-width}.
\]

---

## 5. Lattice path → coefficients (how to fit κ̂)

From existing G12 path tables (boost / separation scans):
1. Require L_c=1 on accepted paths (Q fixed).
2. Regress centered residual proxies (if any meso proxy exists) or treat κ̂ as O(1) placeholders.
3. Report partial correlations: Var vs ⟨G₁₂²⟩, vs ⟨(Δ₀/Δ−1)²⟩, vs ⟨(λ_ref/λ)²⟩.
4. Prefer the channel with highest stable correlation across L=8,10,12.

Until meso data exist, publish **relative** channel weights, not absolute κ.

---

## 6. Falsifiers (specialized)

- Q not fixed on paths used to define A_c.
- ⟨δμ⟩ systematically nonzero after centering.
- Var(δμ) uncorrelated with all of {G₁₂², f(Δ)², g(λ)²}.
- ξ_μ incompatible with measured ⟨Δ⟩ / tube width order of magnitude.
