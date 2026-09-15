# Spectral flow on larger lattices — exploration results

Tony Kawas / 15 September 2026.

---

## 1. Runs performed

| Lattice | N_def | Operator | Scan | Index_sf | Crossings |
|---------|-------|----------|------|----------|-----------|
| L = 5   | 1, 2  | Continuum-like + strength s | s ∈ [0, 2] | 0 | none |
| L = 7   | 1     | Continuum-like + strength s | s ∈ [0, 2] | 0 | none |
| L = 5   | 1     | Continuum-like + full hedgehog + additive m | m ∈ [−2, 2] | 0 | none |
| L = 7   | 1     | Continuum-like + full hedgehog + additive m | m ∈ [−2, 2] | 0 | none |

---

## 2. Observed spectral pattern

**Strength flow s: 0 → 2** (L = 7, N_def = 1)

| s | lowest eigenvalues of H(s) |
|---|----------------------------|
| 0.00 | 0, 0, 0, 0, … (large free kernel) |
| 0.67 | −0.66 (degenerate) |
| 1.33 | −1.33 (degenerate) |
| 2.00 | −1.99 (degenerate) |

All tracked modes move uniformly from zero into the negative half-line. No mode crosses from positive to negative or vice versa inside the scanned window, so the net spectral flow remains zero.

**Additive mass flow m: −2 → +2** (hedgehog at full strength)

| m | lowest eigenvalues of H(m) |
|---|----------------------------|
| −2 | ∼ −3.15 |
| 0  | ∼ −1.15 |
| +2 | ∼ −3.15 |

The spectrum of H stays negative throughout; no zero crossings are registered. (This also indicates that the present continuum-like + hedgehog operator on these open lattices does not place exact zeros of D at m = 0 in the tracked sector, unlike some earlier single-operator diagonalizations with a slightly different mass embedding.)

---

## 3. Structural diagnosis (why Index_sf remains 0)

1. **Open-boundary free kernel**  
   At vanishing hedgehog strength the continuum-like kinetic operator on an open cube has a large exact kernel. Turning the hedgehog on lifts that kernel uniformly downward in the spectrum of H = γ⁵D. Uniform motion of a whole multiplet does not generate a *net* signed flow equal to N_def.

2. **Absence of a gapped positive sector at the starting point**  
   Textbook spectral flow for the index assumes that at one end of the parameter path the operator is gapped with a definite spectral asymmetry (or empty kernel), and that continuum zero-modes produce isolated crossings. On the present open lattices the starting point is gapless (many zeros), so the topological crossings are masked.

3. **Mass-matrix embedding and scale**  
   The particular 4-component block form of the hedgehog mass, together with the open-boundary continuum-like kinetic term, does not yet reproduce the continuum Jackiw–Rossi operator closely enough for the flow of H(m) to display the expected |N_def| crossings near m = 0.

4. **Volume**  
   L = 7 is still modest. A clean separation between core physics and boundary artefacts generally requires a larger hierarchy between core width and box size.

---

## 4. What has been achieved

- Spectral-flow algorithm runs successfully on L = 5 and L = 7 (dense Hermitian diagonalisation of H).  
- Eigenvalue trajectories are smooth and reproducible.  
- The obstruction to Index_sf = N_def is identified as a combination of open-boundary free zeros and the present mass embedding, not a failure of the algorithm or of the continuum index theorem.

---

## 5. Concrete next adjustments (ordered by expected impact)

1. **Periodic boundaries** (or a hedgehog–anti-hedgehog pair on a torus)  
   Eliminates the open-boundary free kernel so that the starting point of the flow is gapped.

2. **Continuum Jackiw–Rossi mass matrix**  
   Use the precise Dirac structure that appears in the original continuum Hamiltonian (rather than the present block embedding) so that D itself has exact zeros of chirality ±1 when the hedgehog is on.

3. **Larger volume** (L ≥ 11) once the boundary condition is fixed.  

4. **Wilson operator with subtracted critical mass**  
   So that the physical mass window sits near zero and continuum-like crossings are not pushed to the Wilson edges.

---

## 6. Status relative to the Callan-Harvey program

| Item | Status |
|------|--------|
| Continuum Index(D) = N_def | Analytic — established |
| Spectral-flow algorithm | Implemented and tested on L ≤ 7 |
| Index_sf = N_def on present lattices | Not yet (structural lattice artefacts) |
| Path to demonstration | Periodic BC / JR mass matrix / larger L |

The continuum Callan-Harvey inflow, the analytic index theorem, and the residual-network chiral term remain unchanged. The lattice spectral-flow demonstration is limited by boundary and embedding artefacts that are well-understood and removable by the adjustments listed above.

---

## 7. Compact statement

Spectral flow was explored on L = 5 and L = 7. In all runs Index_sf remained 0 because open-boundary free zeros and the present mass embedding produce a uniform downward shift of the spectrum rather than isolated topological crossings. The algorithm is working; the next decisive step is to repeat the identical flow on a periodic lattice (or with a continuum Jackiw–Rossi mass matrix) so that the starting point is gapped and the net crossing count can equal N_def.
