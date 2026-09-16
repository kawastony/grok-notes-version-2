# Bose–Einstein condensates — exploration and links to the cone/chirality program

Tony Kawas / 16 September 2026.

---

## 1. Mean-field description

At low temperature a dilute BEC is described by the Gross–Pitaevskii (GP) equation, a nonlinear Schrödinger equation with an external trap:

\[
 i\hbar\partial_t\psi = \Bigl(-\tfrac{\hbar^2}{2m}\Delta + V_{\rm ext} + g|\psi|^2\Bigr)\psi.
\]

The complex order parameter \(\psi\) is the macroscopic wave function; \(|\psi|^2\) is the condensate density. Multi-component (spinor) BECs are governed by coupled GP systems and support richer topology.

---

## 2. Topological defects in BECs

### Quantized vortices
Circulation is quantized in units of \(h/m\). A vortex of winding \(m\) has the form
\[
\psi = f(r)e^{im\phi}e^{-i\mu t/\hbar},
\]
with density vanishing at the core. Vortices form spontaneously in quenches through the BEC transition (Kibble–Zurek), under rotation, or at Dirac points of optical lattices with emergent spin–orbit coupling.

### Skyrmions and linked vortex rings
In two-component BECs a skyrmion can be realised as a pair of linked vortex rings (one in each component). The topological charge is that of a map \(S^3\to S^3\) (or a 2D skyrmion charge for planar spin textures). Hedgehog-like spin textures appear when an external magnetic field vanishes at a point; the skyrmion charge is then tied to the winding of the transverse spin.

### Hidden / fractional vortices
In spinor or multi-well geometries, phase singularities can carry angular momentum without a visible density core (“hidden vortices”), or fractional charges appear when the order-parameter manifold has a discrete point-group structure.

---

## 3. Relation to the Callias / microscopic-cone program

| Feature | BEC (GP / spinor) | Callias hedgehog (8-component lattice) |
|---------|-------------------|----------------------------------------|
| Order parameter | Complex scalar / spinor | Dirac spinor + isospin mass map |
| Topology | Phase winding, skyrmion charge | \(\pi_2\) degree of \(\hat\Phi\) |
| Core | Density zero of vortex / skyrmion | Localisation of fermionic zero modes |
| Pair physics | Vortex molecules, hybridized pairs | Soft hybridized modes at finite sep |
| Chirality | Chiral active BECs; spin–orbit; handed defect clustering | Cone chirality → transport asymmetry → galactic handedness |
| Equation | Nonlinear Schrödinger (GP) | Linear lattice Dirac + topological mass |

**Conceptual bridges**
1. **Core profiles** — The same radial families used for BEC vortex cores (tanh, Gaussian, variational surface-tension ansätze) are the profiles we tested for the hedgehog mass texture.  
2. **Molecular regime** — Two nearby BEC vortices hybridize; the lowest modes become bonding/antibonding combinations with shared density. That is the precise analogue of the shared soft modes we see at L ≤ 10.  
3. **Hedgehog / skyrmion** — Spinor BECs realise hedgehog spin textures whose topological charge is measured by a skyrmion number. Our Callias mass map is the fermionic counterpart of that bosonic texture.  
4. **Dirac-point vortices** — Recent experiments generate quantized vortices in a BEC at a Dirac point of a honeycomb lattice via emergent spin–orbit coupling — a direct meeting of Dirac physics and BEC topology.

---

## 4. Chirality and BECs

- Spin–orbit coupled and spinor BECs support chiral edge modes and handed defect dynamics.  
- In polar chiral active matter related to driven condensates, like-signed vortices cluster and can form large-scale Onsager-like dipoles — macroscopic parity breaking from microscopic chirality.  
- These are continuum, many-body illustrations of the same organising idea used in the cone program: orientation / winding at small scale → transport or clustering asymmetry at large scale.

---

## 5. What BECs do and do not supply

**Useful**  
- Experimental and theoretical laboratory for topological defects, core structure, and pair hybridization.  
- Concrete GP numerics and variational core shapes that can be imported as \(f(r)\).  
- A bosonic parallel to the soft-mode / molecular-regime story.

**Not a substitute**  
- GP is a bosonic mean-field equation; it does not compute a Callias index or protect fermionic zero modes.  
- The lattice Dirac + 8-component isospin embedding remains the correct framework for a quantitative \(N_{\rm def}\) demonstration and for the anomaly-inflow / residual-network side of the program.

---

## 6. Practical takeaways for the project

- The molecular regime we observe is expected; BEC vortex-pair literature predicts the same shared modes until separation exceeds a few healing lengths.  
- Further profile tuning alone is unlikely to replace larger separation (consistent with our alternative-core survey).  
- If external larger-volume runs become available, the BEC analogy suggests tracking splitting \(\Delta\lambda\) vs sep/healing-length as the clean diagnostic of decoupling.

---

## Compact statement

Bose–Einstein condensates, via the Gross–Pitaevskii equation, host quantized vortices, skyrmions, and hybridized vortex pairs whose topology and finite-separation physics closely parallel the soft-mode behaviour of the Callias hedgehog. They provide a bosonic laboratory and useful core-profile intuition, but do not replace the fermionic index calculation. The lattice program’s remaining task is still geometric scale separation.
