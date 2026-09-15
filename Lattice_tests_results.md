# Lattice zero-mode tests: chirality, localization, refinement

Tony Kawas / 15 September 2026.  
Results of the three requested tests.

---

## Test protocol

Three diagnostics were run on discrete realisations of the Callan-Harvey zero-mode:

1. Chirality measurement 〈γ⁵〉 (or its 1-D analogue).  
2. Spatial localisation on the defect core / wall.  
3. Stability under lattice refinement (increasing L, decreasing a).

Because a fully correct 4-component Wilson hedgehog on a 3-D cubic lattice still requires careful tuning of the Wilson term relative to the position-dependent mass, the cleanest controlled demonstration is performed first on the classic 1-D Jackiw–Rebbi domain wall (the continuum limit of the activation-surface case). The same diagnostics are then applied to a schematic 3-D hedgehog; the latter remains under refinement.

---

## 1. Chirality measurement

**1-D Jackiw–Rebbi domain wall** (mass m(x) = m₀ tanh(x/w))

- Lowest eigenvalue: |E| ∼ 10⁻¹⁵ (machine precision zero).  
- The mode is an exact zero-mode of the continuum Dirac operator discretised on the line.  
- Local chirality density is peaked on the wall; the integrated chiral charge of the bound state is non-vanishing and of definite sign once the basis is aligned with the wall normal.

**3-D schematic hedgehog** (current operator)

- Chirality expectation of the lowest mode is partial (|〈χ〉| ∼ 0.3).  
- This indicates that the schematic kinetic term has not yet fully projected onto a single chiral sector; a proper 4-component Wilson or overlap operator is required for a sharp 〈γ⁵〉 = ±1.

---

## 2. Spatial localisation on the hedgehog / wall core

**1-D domain wall**

- Probability density peaks exactly at the wall centre.  
- Profile is exponential, matching the continuum Jackiw–Rebbi solution  
  ψ(z) ∝ exp(−∫ m(z′) dz′).  
- Central 9-site density (example L = 61):  
  [0.038, 0.069, 0.112, 0.155, 0.174, 0.155, 0.112, 0.069, 0.038]

**3-D schematic hedgehog**

- Radial density is highest near the origin and falls with r.  
- The fall-off is visible but still contaminated by the incomplete chiral projection of the schematic operator.

---

## 3. Stability under lattice refinement

**1-D domain wall**

| L  | a   | lowest \|E\|     | gap to next mode |
|----|-----|-----------------|------------------|
| 41 | 0.5 | ∼ 10⁻¹⁵        | continuum gap    |
| 61 | 0.4 | ∼ 10⁻¹⁵        | continuum gap    |
| 81 | 0.3 | ∼ 10⁻¹⁵        | continuum gap    |

The zero eigenvalue remains at machine precision under refinement; the mode is topologically protected and stable.

**3-D schematic**

| L | lowest \|λ\| |
|---|--------------|
| 5 | 0.10         |
| 7 | 0.13         |
| 9 | 0.13         |

The eigenvalue stays O(0.1) and does not yet run to zero with L. This is the expected signal that the discretisation of the kinetic term and the angular structure of the hedgehog still need improvement.

---

## Summary of the three tests

| Test                        | 1-D domain wall (activation surface) | 3-D hedgehog (current schematic) |
|-----------------------------|--------------------------------------|----------------------------------|
| Chirality                   | Definite, localised on wall          | Partial (needs better operator)  |
| Spatial localisation        | Exponential, peaks on defect         | Present, needs cleaner isolation |
| Stability under refinement  | Machine-precision zero, stable       | Not yet running to zero          |

---

## Conclusion and next discrete step

- The Callan-Harvey zero-mode is unambiguously present and stable for the activation-surface (domain-wall) geometry. Chirality, localisation and refinement tests all pass cleanly.  
- For the hedgehog the continuum index theorem is already established analytically; the lattice realisation requires a properly tuned 4-component Wilson (or overlap / domain-wall fermion) operator before the same three diagnostics become sharp.  
- That improved 3-D operator is the single remaining numerical task. Once it is in place, the three tests will be re-run and the lattice sector of the Callan-Harvey program will be closed.

No new free parameters have been introduced. All continuum coefficients remain locked by R_cone.
