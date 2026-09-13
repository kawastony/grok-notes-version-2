# Residual-network chiral term

Tony Kawas / 14 September 2026.  
Concrete next step of the chirality program. Builds directly on the microscopic chiral term, the residual network Σ_res, and the locked surface data.

Status: research-program extension. Not a completed derivation of galactic handedness. The term is written so that it can be tested against existing data.

---

## 1. Starting point (already locked)

Microscopic chiral density:
\[
\mathcal{L}_{\mathrm{chiral}}
=
\frac{\kappa}{2}\,
\chi\,\bigl(\hat{\mathbf{c}}\cdot(\boldsymbol{\varepsilon}\times\partial_t\boldsymbol{\varepsilon})\bigr),
\qquad
\kappa=\frac{R_{\mathrm{cone}}}{c}=\frac{\sqrt{6}}{\varphi\,c}.
\]

Residual network field Σ_res already appears in the Layer-C notes as the coarse-grained carrier of residual strain after freeze. It inherits preferred directions from the pre-existing LSS tidal field at z∼0.3.

Disk normal n̂ is the macroscopic analogue of the microscopic cone axis ĉ.

---

## 2. Residual chiral term (proposed)

Promote the microscopic density to the residual network by the direct geometric replacement
\[
\boldsymbol{\varepsilon}\;\to\;\boldsymbol{\Sigma}_{\mathrm{res}},
\qquad
\hat{\mathbf{c}}\;\to\;\hat{\mathbf{n}}
\]
(with the same coefficient κ fixed by the activation surface):

\[
\boxed{
\mathcal{L}_{\mathrm{residual}}^{\mathrm{chiral}}
=
\frac{\kappa}{2}\,
\chi\,\bigl(\hat{\mathbf{n}}\cdot(\boldsymbol{\Sigma}_{\mathrm{res}}\times\partial_t\boldsymbol{\Sigma}_{\mathrm{res}})\bigr).
}
\]

No new free parameter is introduced. The only objects that enter are:

- κ = R_cone / c (already locked),
- χ (radial / freeze mode already required for charge and pause),
- n̂ (disk or residual-network normal already present),
- Σ_res (already defined in the residual program).

---

## 3. Continuum consequence

Variation with respect to Σ_res produces a gyroscopic residual force density
\[
\mathbf{f}_{\mathrm{res}}^{\mathrm{chiral}}
=
\kappa\,\chi\,(\hat{\mathbf{n}}\times\partial_t\boldsymbol{\Sigma}_{\mathrm{res}}).
\]

In the quasi-static galactic regime this appears as a parity-odd correction to the residual acceleration:
\[
\mathbf{a}_{\mathrm{res}}^{\mathrm{chiral}}
\propto
\kappa\,\chi\,(\hat{\mathbf{n}}\times\mathbf{v}_{\mathrm{res}}).
\]

One global sense of the product χ (n̂ · L̂) (where L̂ is the galactic angular-momentum direction) lowers the effective residual resistance; the opposite sense raises it. That is the macroscopic translation of the original chi-flow intuition.

---

## 4. Observables that can discriminate the term

| Observable | Expected chiral signature | Null hypothesis (no chiral term) |
|---|---|---|
| SPARC residual pattern after standard interpolator | Handedness-dependent residual torque correlated with spiral-arm winding sense or disk inclination | Residuals statistically independent of winding sense |
| Galaxy spin / spiral-winding statistics | Preferred correlation between residual amplitude and Z-wise vs S-wise classification | No residual–winding correlation beyond geometry |
| Stacked RAR near the transition | Small parity-odd shift in the median residual when galaxies are split by winding sense | Residuals symmetric under winding reversal |
| Intrinsic-alignment or tidal-alignment residuals | Additional parity-odd contribution aligned with the local tidal eigenframe | Standard tidal alignment only |

The strongest immediate test is a split of SPARC (or a high-quality subset) by spiral-arm winding sense (or by an independent spin proxy) and a comparison of the residual distributions.

---

## 5. What is forced vs what is still programmatic

**Forced by existing geometry**
- The functional form of the residual chiral density (unique parity-odd scalar built from χ, n̂ and Σ_res).
- The coefficient κ fixed by the same surface data that produce R_cone.
- The topological protection of the overall sign once N_def is chosen.

**Still programmatic**
- The precise identification Σ_res ↔ coarse-grained ε (motivated by the residual-network notes, not yet derived from a varied action).
- The quantitative size of the residual torque relative to the ordinary residual strain (depends on the still-open n_2 and on the amplitude of χ after freeze).
- Whether the term improves or worsens any real data residual.

---

## 6. Relation to the full chirality chain

\[
\begin{array}{c}
\text{Quantum topological sign }N_{\mathrm{def}}\\
\downarrow\\
\text{Microscopic defect chirality (already written)}\\
\downarrow\\
\text{Residual-network chiral term (this note)}\\
\downarrow\\
\text{Macroscopic handed residual torque}\\
\downarrow\\
\text{Galaxy-scale observables (testable)}
\end{array}
\]

This note supplies the first fully specified arrow that can be confronted with data. The remaining arrows stay research-program statements until analogous calculations are written.

---

## 7. One-sentence status

The residual chiral term is the unique, parameter-free promotion of the microscopic chiral density to the residual network; it generates a parity-odd residual torque whose presence or absence can be tested directly in SPARC residuals split by galaxy winding sense.

---

## 8. Recommended immediate check

1. Take the existing SPARC residual catalogue after the locked simple interpolator.  
2. Split the sample by an independent winding-sense or spin proxy (Z-wise / S-wise or equivalent).  
3. Compare the residual distributions (mean, median, or stacked RAR residual) between the two handedness bins.  
4. Report whether a statistically significant difference appears in the direction predicted by a fixed global sign of χ n̂.

A null result constrains the amplitude of χ after freeze or the coupling of Σ_res to the microscopic chirality. A positive result moves the chirality program from architecture to evidence.
