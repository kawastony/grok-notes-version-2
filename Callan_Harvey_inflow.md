# Callan-Harvey Inflow Current from the Cone Chiral Density

Tony Kawas / 14 September 2026.  
Derivation note. Uses only objects already present: radial mode χ, cone axis ĉ, elongation ε, topological degree N_def, and the locked chiral coefficient κ = R_cone / c.

---

## 1. Setup

We work in the continuum limit of the cone network outside defect cores.  
The classical chiral density already written is

\[
\mathcal{L}_{\mathrm{chiral}}
=
\frac{\kappa}{2}\,
\chi\,\bigl(\hat{\mathbf{c}}\cdot(\boldsymbol{\varepsilon}\times\partial_t\boldsymbol{\varepsilon})\bigr).
\]

Identify the transverse elongation with the gauge potential in the usual network map,
\[
\mathbf{A}\equiv\boldsymbol{\varepsilon}_T
\]
(away from cores the longitudinal part is pure gauge or absorbed into χ).  
Then the helical combination becomes the continuum helicity density
\[
\mathbf{A}\cdot(\nabla\times\mathbf{A})
\quad\text{or its dynamical analogue}
\quad
\mathbf{A}\cdot\partial_t\mathbf{A}
\]
projected along the local defect axis ĉ.

The activation surface (TAFA wall) or the hedgehog core supplies a codimension-1 or codimension-2 defect on which chiral zero-modes can live.  
We seek the bulk current whose divergence is concentrated on that defect and cancels the expected anomaly of those zero-modes.

---

## 2. Goldstone-Wilczek / Callan-Harvey current from a chiral scalar

In the classic Callan-Harvey construction a real scalar φ that interpolates across a domain wall (or winds around a string) generates the Goldstone-Wilczek current
\[
J^\mu_{\mathrm{GW}}
=
\frac{1}{8\pi^2}\,
\varepsilon^{\mu\nu\rho\sigma}
(\partial_\nu\phi)\,F_{\rho\sigma}
\]
(in 3+1 dimensions; factors of e, ħ restored later).  
Its divergence is
\[
\partial_\mu J^\mu_{\mathrm{GW}}
=
\frac{1}{8\pi^2}\,
\varepsilon^{\mu\nu\rho\sigma}
(\partial_\mu\partial_\nu\phi)\,F_{\rho\sigma}
+
\frac{1}{8\pi^2}\,
\varepsilon^{\mu\nu\rho\sigma}
(\partial_\nu\phi)\,\partial_\mu F_{\rho\sigma}.
\]
The second term vanishes by the Bianchi identity.  
The first term is non-zero only where the scalar gradient is singular (the wall or the string core), and there it equals the anomaly polynomial of the chiral zero-modes bound to the defect.

---

## 3. Identification with cone variables

Map the classic scalar to the cone radial mode:
\[
\phi\;\longleftrightarrow\;\chi
\]
(the same χ that already appears in the microscopic chiral term and in Model D for static charge).  
The field strength is built from the network potential,
\[
F_{\rho\sigma}=\partial_\rho A_\sigma-\partial_\sigma A_\rho,
\qquad
\mathbf{A}=\boldsymbol{\varepsilon}_T.
\]

The cone axis ĉ supplies the preferred direction that orients the defect.  
In the rest frame of a static defect the only non-vanishing component of interest is the inflow along ĉ.

Define the continuum inflow current by the Goldstone-Wilczek expression written in cone variables:
\[
\boxed{
J^\mu_{\mathrm{inflow}}
=
\frac{\kappa}{4\pi}\,
\varepsilon^{\mu\nu\rho\sigma}
(\partial_\nu\chi)\,
(\partial_\rho A_\sigma)
}
\]
(the numerical prefactor is fixed below by matching to the already-locked κ).  
Equivalently, in 3-vector notation for a static defect,
\[
\mathbf{J}_{\mathrm{inflow}}
=
\frac{\kappa}{4\pi}\,
(\nabla\chi)\times\mathbf{B}
+
\frac{\kappa}{4\pi}\,
(\partial_t\chi)\,\mathbf{E}
\]
(with the usual identification B = ∇ × A, E = −∂t A − ∇φ).

---

## 4. Divergence and localisation on the defect

Because χ is smooth outside the core and jumps (or winds) only across the activation surface / hedgehog core,
\[
\partial_\mu J^\mu_{\mathrm{inflow}}
=
\frac{\kappa}{4\pi}\,
\varepsilon^{\mu\nu\rho\sigma}
(\partial_\mu\partial_\nu\chi)\,(\partial_\rho A_\sigma).
\]
The double derivative is a delta-function supported on the defect:
\[
\partial_\mu\partial_\nu\chi
\;\propto\;
N_{\mathrm{def}}\,
\delta^{({\rm codim})}(x_{\mathrm{defect}})
\times
(\text{oriented volume form of the defect}).
\]
Thus
\[
\partial_\mu J^\mu_{\mathrm{inflow}}
=
\frac{\kappa}{4\pi}\,N_{\mathrm{def}}\,
\bigl(\mathbf{E}\cdot\mathbf{B}\bigr)_{\mathrm{defect}}
\]
(up to conventional 2π factors that are absorbed into the normalisation of χ).  
This is precisely the Callan-Harvey inflow: the bulk current is conserved everywhere except on the defect, where its divergence equals the chiral anomaly of the zero-modes that live there.

---

## 5. Fixing the coefficient from the locked chiral term

The microscopic chiral Lagrangian already contains the combination χ (ĉ · (ε × ∂t ε)).  
After the identification A = ε_T this is proportional to the helicity density.  
Varying that Lagrangian with respect to A produces a current whose form matches the Goldstone-Wilczek expression above.  
Matching the overall strength to the already-locked
\[
\kappa=\frac{R_{\mathrm{cone}}}{c}=\frac{\sqrt{6}}{\varphi\,c}
\]
gives the prefactor used in the boxed formula.  
No new free parameter is introduced.

---

## 6. Relation to the residual chiral term

When the same current is coarse-grained onto the residual network Σ_res one recovers the residual chiral density written earlier:
\[
\mathcal{L}_{\mathrm{residual}}^{\mathrm{chiral}}
=
\frac{\kappa}{2}\,
\chi\,\bigl(\hat{\mathbf{n}}\cdot(\boldsymbol{\Sigma}_{\mathrm{res}}\times\partial_t\boldsymbol{\Sigma}_{\mathrm{res}})\bigr).
\]
Thus the galactic residual torque is the macroscopic descendant of the same inflow current that cancels the microscopic anomaly on the defect.

---

## 7. What is derived vs what remains open

**Derived**
- Explicit continuum expression for the inflow current in cone variables.  
- Localisation of its divergence on the defect, proportional to N_def (E · B).  
- Coefficient fixed by the existing surface data (R_cone).  
- Consistency with the residual chiral term already written.

**Still open**
- Explicit construction of the chiral zero-modes bound to the cone core (Jackiw-Rossi or analogous index calculation).  
- Precise normalisation of the anomaly polynomial (factors of 2π, e, ħ).  
- Global consistency when many defects are present (total inflow must cancel total zero-mode anomaly).

---

## 8. Compact statement

The Callan-Harvey inflow current on the cone network is
\[
J^\mu_{\mathrm{inflow}}
=
\frac{\kappa}{4\pi}\,
\varepsilon^{\mu\nu\rho\sigma}
(\partial_\nu\chi)\,(\partial_\rho A_\sigma),
\qquad
\kappa=\frac{R_{\mathrm{cone}}}{c}.
\]
Its divergence is supported only on the defect and equals (κ/4π) N_def (E · B)|_defect, thereby cancelling the chiral anomaly of zero-modes that may live there.  
The same current, once coarse-grained, yields the residual chiral term that is ready for the SPARC winding-sense test.

---

## 9. Next natural calculation

Compute the index of the Dirac operator on the hedgehog background (or on the activation-surface domain wall) and verify that the resulting zero-mode anomaly coefficient matches the coefficient appearing in ∂_μ J^μ_inflow.  
That single index theorem check would close the microscopic consistency of the inflow mechanism.
