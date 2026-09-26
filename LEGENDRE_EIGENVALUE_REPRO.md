# Legendre / junction eigenvalue ν₀ ≈ 2.31 — reproducibility

**Source claim (Paper 25 §5.2):**  
On the galactic junction sector [ψ₁,ψ₂]=[35°,70°] with mixed BC (Neumann at 35°, Dirichlet at 70°), numerical evaluation of the Legendre determinant yields ν₀ ≈ 2.31, and Δ_μ = ν₀ for a boundary operator on a d′=3 defect.

---

## Setup (as stated)

- Angular sector width Δψ = 35° = 7π/36 rad
- Inner (baryonic) BC: Neumann Φ′=0 at ψ₁=35°
- Outer (sovereign) BC: Dirichlet Φ=0 at ψ₂=70°
- Operator: spherical Laplace–Beltrami in the polar angle (Legendre form),
  or equivalent boundary/transmission operator whose principal eigenvalue is ν₀

---

## Analytic estimate (flat sector)

On a flat interval of length L=Δψ with Neumann–Dirichlet conditions, the lowest mode is
\[
\frac{\pi}{2L}=\frac{\pi}{2\cdot 7\pi/36}=\frac{18}{7}\approx 2.571.
\]
This is **O(1)-close** to 2.31 but not identical — curvature / measure sinθ and the precise Legendre determinant shift the number.

---

## Numerical SL attempt (this session)

Finite-difference discretization of
\[
-\frac{1}{\sin\theta}\partial_\theta\bigl(\sin\theta\,\partial_\theta\Phi\bigr)=\nu(\nu+1)\Phi
\]
on [35°,70°] with the stated mixed BC did **not** converge to ν≈2.31 under grid refinement (eigenvalues drifted upward — indicating either a BC/stencil bug or that Paper 25’s “Legendre determinant” refers to a different matching condition than the plain Laplace spectrum on the sector).

**Conclusion:** ν₀≈2.31 is **not independently reproduced** here as a plain SL ground state. It remains a **Paper 25 geometric input**. Reproducibility requires the exact determinant condition used in that paper (associated Legendre order, matching matrix across cone sheets, or transmission eigenvalue problem as coded in their notebook).

---

## Working definition (until code is matched)

\[
\Delta_\mu \equiv \nu_0 \approx 2.31
\quad\text{(Paper 25 geometric eigenvalue on the junction)}
\]

Pass/fail for future reproduction: recover |ν₀ − 2.31| < 0.02 from a fully specified determinant or SL problem with the same BC and measure.

---

## Link into γ

\[
\gamma=\frac{\Delta_\mu}{n_{\rm eff}\Delta_X}=\frac{2.31}{8\times 24/13}\approx 0.156
\]

Uncertainty in ν₀ propagates linearly into γ.
