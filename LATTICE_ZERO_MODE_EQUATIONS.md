# Lattice zero-mode equations — investigation

Target continuum problem: Callias-type L = Q + Φ on ℝ³ with hedgehog Φ. Lattice UV: 8-component Wilson–Dirac + isospin mass texture.

---

## 1. Continuum zero-mode equation

Exact zero mode of L:
\[
\bigl(\boldsymbol{\gamma}\cdot\boldsymbol{\nabla} + \Phi(\mathbf{r})\bigr)\psi = 0.
\]
For hedgehog Φ = v f(r) n̂·τ, the index theorem guarantees dim ker controlled by N_def. Explicit profiles exist in the literature for monopole harmonics / Jackiw–Rebbi-type bound states; the essential point for TAFA is existence and topological protection, not the closed form.

---

## 2. Lattice operator (schematic)

On a cubic lattice with spacing a, 8-component field ψ_{x,α} (Dirac ⊗ isospin):
\[
(H\psi)_x
= \sum_{\mu=1}^{3}\frac{1}{2a}\bigl(\alpha_\mu(\psi_{x+\hat\mu}-\psi_{x-\hat\mu})\bigr)
- \frac{r_W}{2a}\sum_{\mu}(\psi_{x+\hat\mu}-2\psi_x+\psi_{x-\hat\mu})
+ \beta\, m(x)\,\psi_x.
\]
Mass texture (hedgehog):
\[
m(x) = m_0 + v\, f(|x-x_c|)\, \hat{\mathbf{n}}(x-x_c)\cdot\boldsymbol{\tau}
\]
(with optional second core of opposite charge). Wilson term r_W lifts doublers; residual chiral mixing is a known systematic.

**Soft-mode equation on the lattice:**
\[
H\psi_a = \lambda_a \psi_a,
\qquad |\lambda_a| \ll \lambda_{\rm bulk}.
\]
Exact continuum zero modes become **near-zero** soft modes once Wilson, finite volume, and discretization are present.

---

## 3. Pair geometry

Two cores at c₁, c₂ with charges ±1:
\[
m(x) = m_0 + v\sum_{i=1}^{2} q_i f(|x-c_i|)\,\hat{\mathbf{n}}_i\cdot\boldsymbol{\tau}.
\]
Total continuum index → 0. Lattice: two soft eigenvalues; spatial weights can hybridize into a molecular tube when |c₁−c₂| is not ≫ ξ. Boost of one core (or v_coup change) induces spectral motion and G12 weight slide while each core’s topological diagnostic stays fixed if no annihilation occurs.

---

## 4. Numerical diagnostics (program targets)

| Diagnostic | Target |
|------------|--------|
| Soft multiplicity | Matches |N_def| (single) or 2 (compensated pair) |
| Localization | Weight peaks on cores / tube |
| Index / spectral flow | Net crossings = N_def under adiabatic path |
| Q per core | Stable under boost |
| Continuum trend | |λ_soft| → 0 or stable density as a→0 / L↑ |

---

## 5. Relation to TAFA layers

- **Micro:** soft modes = active bridge; index = identity lock.
- **Scale transfer:** spectral motion → Var(δμ); index fixed → ⟨μ̇⟩≈0 (Example 1).
- **Not automatic:** map from λ_a, ψ_a to galactic a_eff or cosmic ω_* — that still goes through the one-input bridge / calibration.

---

## 6. Status

Equations and diagnostics are specified. Continuum Callias explains *why* soft modes exist and why their count is stable. Lattice implements a UV version; residual Wilson/finite-volume effects must be controlled before claiming Index(D)=N_def at machine precision.
