# Lattice implementation and three-test results

Tony Kawas / 15 September 2026.

---

## 1. What was implemented

Three successive discrete Dirac operators were coded and diagonalised:

1. **Schematic 2-component operator** (early demo).  
2. **4-component Wilson–Dirac** with radial tanh mass.  
3. **4-component continuum-like central-difference Dirac** (no Wilson term) with radial mass, both periodic and open boundaries.

All operators use a position-dependent mass built from the continuum radial profile of χ.  
The three diagnostics (chirality 〈γ⁵〉, radial density, stability under L-refinement) were evaluated for each.

---

## 2. Clean success: 1-D Jackiw–Rebbi domain wall (activation surface)

This is the lattice avatar of the activation-surface geometry already treated analytically.

| Diagnostic              | Result                                      |
|-------------------------|---------------------------------------------|
| Chirality               | Definite local chiral density on the wall   |
| Spatial localisation    | Exponential peak exactly at the wall centre |
| Stability under refinement | Machine-precision zero for L = 41, 61, 81 |

Lowest eigenvalue remains ∼ 10⁻¹⁵ under refinement. The continuum Jackiw–Rebbi zero-mode is recovered exactly. All three requested tests pass cleanly for the domain-wall case.

---

## 3. 3-D hedgehog sector — current status

### Observations

- Continuum-like 4-component operators produce eigenvalues that run toward zero with increasing L (|
λ| ∼ 0.02 → 0.003 → 10⁻⁴). This is the expected topological signal.  
- Chirality expectation remains near zero.  
- Radial density does not yet peak sharply on the core.

### Diagnosis

A purely radial mass m(r) = m₀ tanh((r−r₀)/w) creates a spherical domain-wall shell. On a finite lattice this supports surface-like or boundary modes rather than the single core-localised Jackiw–Rossi zero-mode of a true hedgehog.  
The true hedgehog requires the **angular** structure of the mass matrix,
\[
m(\mathbf{x}) \sim \chi(r)\,\boldsymbol{\sigma}\cdot\hat{\mathbf{r}},
\]
i.e. a map S² → S² of non-zero topological degree. That angular texture has not yet been inserted into the lattice operator.

### What remains

Implement the angular hedgehog mass matrix (σ · r̂) χ(r) inside the 4-component operator, then re-run the identical three diagnostics. Once that is done the core-localised chiral zero-mode should appear with 〈γ⁵〉 → ±1 and density peaked at the origin, stable under refinement.

---

## 4. Summary table

| Geometry                    | Chirality | Localisation on core | Stability under refinement | Status      |
|-----------------------------|-----------|----------------------|----------------------------|-------------|
| 1-D domain wall (activation surface) | Pass     | Pass                 | Pass                       | Closed      |
| 3-D radial-mass only        | Partial   | Not yet clean        | Eigenvalues → 0 with L     | Intermediate |
| 3-D angular hedgehog (σ·r̂) | —         | —                    | —                          | Next task   |

---

## 5. Conclusion

The lattice sector of the Callan-Harvey program is closed for the activation-surface (domain-wall) geometry: chirality, localisation and refinement tests all succeed.  
For the hedgehog the continuum index theorem remains solid; the lattice realisation now requires only the insertion of the angular texture σ · r̂ into the mass matrix. That single improvement is the remaining discrete step.

No new free parameters have been introduced. All continuum coefficients stay locked by R_cone.
