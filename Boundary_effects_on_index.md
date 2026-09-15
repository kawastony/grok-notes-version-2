# Boundary effects on the spectral-flow index

Tony Kawas / 15 September 2026.

---

## 1. Why boundaries matter

The analytic index
\[
\mathrm{Index}(D) = n_+ - n_- = N_{\mathrm{def}}
\]
is a bulk topological invariant. On a finite lattice its numerical surrogate (spectral flow of H) is sensitive to the choice of boundary conditions because:

- boundaries can support additional zero or near-zero modes that are not present in the continuum on ℝ³;
- the starting point of a spectral-flow path must be gapped (or have a controlled kernel) for crossings to be unambiguously topological;
- open walls break translational invariance and can mix chiralities of bulk zero-modes.

---

## 2. Continuum expectations

| Geometry | Continuum statement |
|----------|---------------------|
| ℝ³ (no boundary) | Index(D) = N_def for a single hedgehog of degree N_def |
| Large box with APS boundary conditions | Index = bulk index + boundary spectral asymmetry (η-invariant) |
| Torus T³ | Net index must vanish unless the gauge/mass background carries compensating topology (e.g. hedgehog–anti-hedgehog pair with net charge zero, or a non-trivial flux) |
| Open cube (Dirichlet / bag) | Extra boundary modes appear; net spectral flow need not equal the bulk N_def |

On a torus a single hedgehog is topologically obstructed (the map S² → S² cannot be extended over the whole T³ without a compensating anti-defect). Consequently a pure periodic lattice with one hedgehog is expected either to force the core to “leak” or to produce a vanishing net index — the standard remedy is a hedgehog–anti-hedgehog pair.

---

## 3. Numerical diagnosis on the present operator

### 3.1 Open boundaries (L = 5)

- At vanishing hedgehog strength (s = 0) the continuum-like kinetic operator yields a **pathologically large kernel** (hundreds of exact zeros of H — in the extreme run the entire spectrum sat at zero).  
- Turning the hedgehog on moves the whole multiplet uniformly into the negative half-line.  
- Net spectral flow = 0.  
- Interpretation: the free open-boundary operator is not a healthy discretisation of the continuum Dirac operator; boundary-induced zeros dominate and mask any topological crossings.

### 3.2 Periodic boundaries (L = 5)

- The same continuum-like kinetic term again produced a huge free kernel at s = 0.  
- Spectral flow remained zero.  
- Interpretation: the present central-difference discretisation itself (independent of open vs periodic) is not yet giving a correct free spectrum; boundary condition alone cannot cure a defective bulk kinetic term.

### 3.3 Summary of the numerical obstacle

The dominant obstruction is **not** merely “open versus periodic”. It is that the free continuum-like operator used so far fails to reproduce a gapped (or correctly zero-mode-counted) free Dirac spectrum on either boundary condition. Until that is fixed, boundary-effect studies cannot cleanly isolate the topological contribution to the index.

---

## 4. How boundaries are expected to affect a healthy operator

Once a correct free kinetic term is in place, the following boundary effects on Index_sf are predicted:

### Open (Dirichlet / MIT bag)

- Additional surface modes appear.  
- Spectral flow receives a boundary contribution proportional to the η-invariant of the boundary Dirac operator.  
- Index_sf = N_def + (boundary correction).  
- The correction falls as the mode becomes more core-localised (L a ≫ w), so on large volumes Index_sf → N_def.

### Periodic (torus)

- A single hedgehog is topologically inconsistent; the net index must vanish or the configuration must contain a compensating anti-hedgehog.  
- With a hedgehog–anti-hedgehog pair of charges +N_def and −N_def one expects Index_sf = 0 globally, while local spectral flow around each core still sees ±N_def.  
- This is the cleanest setting for a controlled lattice demonstration: measure local spectral flow in a sub-volume surrounding one defect.

### APS boundary conditions

- The continuum Atiyah–Patodi–Singer theorem applies directly.  
- Index_sf = bulk N_def − (1/2)η_boundary.  
- Useful for analytic cross-checks but more involved to implement on the lattice.

---

## 5. Practical recommendations for the cone / Callan-Harvey program

1. **First repair the free kinetic term** so that, on a periodic lattice with no hedgehog, the spectrum of the massless operator consists of the expected Dirac zeros (only the p = 0 mode, or the correct lattice doubling pattern) and a gap above them.  
2. **Then compare open vs periodic** on that healthy operator with a single hedgehog (open) and with a hedgehog–anti-hedgehog pair (periodic).  
3. **Extract local spectral flow** around one core on the periodic pair configuration; that local integer should equal N_def.  
4. Only after the local index is confirmed should one return to the residual chirality extrapolation and the lattice measurement of the Callan-Harvey inflow current.

---

## 6. Relation to earlier chirality-mixing results

Previous isolation tests already showed that open and periodic boundaries produce residual 〈γ⁵〉 of similar magnitude (few percent). That is consistent with the present conclusion: boundary condition is a sub-leading effect compared with the quality of the bulk kinetic discretisation and the angular sampling of σ · r̂ at the origin.

---

## 7. Status

| Question | Answer |
|----------|--------|
| Do boundaries affect Index_sf? | Yes — in continuum via η-invariant / topological obstruction on the torus |
| Is the present Index_sf = 0 caused mainly by open walls? | No — the free kinetic term itself is pathological on both open and periodic lattices |
| What must be fixed first? | A healthy free Dirac spectrum (correct zeros and gap) |
| Then what? | Periodic hedgehog–anti-hedgehog pair + local spectral flow around one core |

The continuum Callan-Harvey construction and the analytic index theorem remain intact. Boundary effects are understood in principle; their clean numerical isolation waits on a correct free lattice Dirac operator.

---

## 8. Compact statement

Boundary conditions affect the spectral-flow index through surface modes (open) or topological obstruction (periodic single hedgehog). On the lattices studied so far the free continuum-like operator produces an unphysically large kernel under both boundary conditions, so the topological flow is masked. The priority is to restore a healthy free spectrum; afterwards a periodic hedgehog–anti-hedgehog pair will allow a local Index_sf = N_def measurement that is free of boundary contamination.
