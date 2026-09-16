# Topological Hall effect — investigation and links to the cone/chirality program

Tony Kawas / 16 September 2026.

---

## 1. Mechanism

When conduction electrons traverse a non-coplanar spin texture (skyrmion, hedgehog, etc.), their spins adiabatically follow the local magnetization and accumulate a **real-space Berry phase**. That phase is equivalent to motion in an emergent magnetic field

\[
\mathbf B^{\rm em}_\alpha = \tfrac12\epsilon_{\alpha\beta\gamma}\,\mathbf n\cdot(\partial_\beta\mathbf n\times\partial_\gamma\mathbf n),
\]

which in 2D is proportional to the topological charge density:

\[
B^{\rm em}_z = 4\pi\,n_{\rm Sk}(\mathbf r).
\]

The Lorentz force from \(\mathbf B^{\rm em}\) deflects carriers transversely → **topological Hall resistivity** \(\rho^{\rm THE}_{xy}\). In the strong-coupling (adiabatic) limit,

\[
\rho^{\rm THE}_{xy}\propto\langle B^{\rm em}_z\rangle\propto N_{\rm Sk}.
\]

No external magnetic field and no spin–orbit coupling are required for the basic effect; the texture topology alone is enough.

---

## 2. Relation to other Hall effects

| Effect | Origin | Typical setting |
|--------|--------|-----------------|
| Ordinary Hall | External \(\mathbf B\) | Any conductor |
| Anomalous Hall (AHE) | Momentum-space Berry curvature + magnetization / SOC | Ferromagnets, some AFMs |
| **Topological Hall (THE)** | Real-space Berry curvature of a spin texture | Skyrmion lattices, chiral magnets |
| Topological spin / orbital Hall | Same texture; spin- or orbital-polarized currents | AFM skyrmions, bimerons |

In practice Hall data are often decomposed as
\[
\rho_{xy}=\rho^{\rm OHE}+\rho^{\rm AHE}+\rho^{\rm THE}.
\]
Genuine THE typically appears in the transition region of the magnetization curve; two-component AHE can mimic THE-like humps and must be distinguished (minor loops, temperature/gate dependence, real-space imaging).

---

## 3. Scale of the emergent field

For nanometer-scale skyrmions, \(|B^{\rm em}|\) can reach thousands of tesla. That opens the possibility of a quantized topological Hall regime (Landau levels of the emergent field) analogous to the quantum Hall effect. In antiferromagnetic skyrmion crystals the net emergent field can cancel while topological orbital Hall responses remain large.

---

## 4. Link to the Callias / microscopic-cone program

| THE / skyrmion | Callias / cone program |
|----------------|------------------------|
| Real-space Berry phase from spin texture | Anomaly inflow / chiral residual from defect orientation |
| Emergent field \(\propto\) topological charge density | Inflow current \(\propto\) defect degree / cone winding |
| Topology → transverse transport | Topology → transport asymmetry / galactic handedness |
| Skyrmion–antiskyrmion (net \(Q\approx0\), local charges ±) | Hedgehog–antihedgehog pair (global index 0, local \(N_{\rm def}\)) |
| DMI-fixed chirality selects THE sign | Cone chirality selects residual sign |

**Conceptual identity**  
THE is the continuum, experimentally measured statement of “integer topological charge of a defect texture produces a directed transport response.” That is the same organising principle used in the cone program:

Topological sign → microscopic defect chirality → transport asymmetry → macroscopic handedness.

The lattice Callias calculation aims to put a fermionic index and an anomaly-inflow current under that chain; THE is the bosonic / spin-texture realisation of the middle links.

---

## 5. What THE does and does not supply

**Useful**  
- Concrete, measured topology → transport map.  
- Emergent-field language that parallels anomaly inflow.  
- Pair / lattice physics (skyrmion crystals, net-zero pairs with local charges) that mirrors the hedgehog–antihedgehog setup.

**Not a substitute**  
- THE is a semiclassical or band-structure response of electrons coupled to a classical (or ordered) spin texture. It does not compute a Callias index or protect lattice Dirac zero modes.  
- The 8-component Wilson + isospin embedding and local diagnostics remain the correct path for a quantitative \(N_{\rm def}\) demonstration.

---

## Compact statement

The topological Hall effect is the transverse transport response of carriers to the real-space Berry phase (emergent field) of a topologically nontrivial spin texture. It is the continuum, experimentally established embodiment of topology → directed transport. In that sense it is the closest measured analogue of the anomaly-inflow / chiral-residual step in the microscopic-cone program. It strengthens the cross-scale chirality narrative without replacing the fermionic lattice index calculation.
