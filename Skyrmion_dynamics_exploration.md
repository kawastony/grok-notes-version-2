# Skyrmion dynamics — exploration and links to the cone/chirality program

Tony Kawas / 16 September 2026.

---

## 1. Collective-coordinate description: Thiele equation

When a skyrmion moves without strong deformation, its centre-of-mass \(\mathbf R(t)\) obeys the Thiele equation

\[
\mathbf G\times\dot{\mathbf R} + \alpha\mathcal D\dot{\mathbf R} = \mathbf F,
\]

where

- \(\mathbf G = 4\pi Q\,\hat{\mathbf z}\) is the gyrocoupling vector (\(Q\) = skyrmion number),
- \(\alpha\mathcal D\) is the dissipative tensor (Gilbert damping),
- \(\mathbf F\) collects driving forces (spin-transfer torque, spin–orbit torque, gradients of pinning potential, inter-skyrmion forces, thermal noise).

The gyro term is topological in origin: it is proportional to the skyrmion charge and is responsible for the **skyrmion Hall effect** — motion at an angle to the drive current.

---

## 2. Main dynamical regimes

### Current-driven motion
- **Spin-transfer torque (STT)** and **spin–orbit torque (SOT)** push the skyrmion along a racetrack or 2D film.  
- Finite Hall angle → transverse drift toward edges; pinning and geometry must compensate.  
- In altermagnets / frustrated systems, helicity can unlock and rotate (even at GHz–THz rates), producing nonlinear frequency combs.

### Skyrmion Hall effect
Transverse velocity component proportional to \(Q\). Opposite-\(Q\) partners (skyrmion / antiskyrmion) deflect in opposite directions — a dynamical signature of topological charge and chirality.

### Breathing and internal modes
Coupled oscillations of size and chirality angle (helicity). Frequency depends on field / anisotropy; large-amplitude unidirectional chirality rotation can be strongly damped and end in collapse; smaller oscillatory breathing can be long-lived. Breathing can be driven by modulating DMI or anisotropy.

### Pair and multi-skyrmion dynamics
- Attraction / repulsion, spiral and breathing after collision.  
- Bound pairs can rotate and breathe with a common period.  
- Annihilation of opposite-\(Q\) pairs is topologically allowed and releases the soft modes into the continuum — the dynamical counterpart of the global index summing to zero.

### Stochastic / pinned motion
Thermal and spin-current noise → diffusion, dwell times at pinning sites, first-passage times to racetrack edges. Relevant for device reliability.

---

## 3. Link to the Callias / microscopic-cone program

| Skyrmion dynamics | Callias / cone lattice program |
|-------------------|--------------------------------|
| Gyro term \(\propto Q\) | Index / local charge \(N_{\rm def}\) |
| Skyrmion Hall deflection | Transport asymmetry from defect chirality |
| Breathing (size + helicity) | Soft-mode spectrum of a single core |
| Opposite-\(Q\) pair annihilation | Global index 0 of hedgehog–antihedgehog |
| Hybridized pair rotation / shared modes | Molecular regime of shared soft eigenmodes at finite sep |
| Drive → directed motion | Chiral residual → preferred flow / galactic handedness |

**Dynamical parallel**  
The Thiele gyro term is the continuum, real-time embodiment of “integer topological charge produces a directed response.” In the lattice theory the same integer produces a protected zero mode and an anomaly-inflow current. Skyrmion Hall motion is the magnetic analogue of the transport asymmetry the cone program attributes to defect chirality.

**Molecular regime**  
Two nearby skyrmions hybridize and can rotate/breathe as a bound pair — the same finite-separation physics that keeps our lattice soft modes shared until separation is large.

---

## 4. What dynamics adds to the narrative

1. **Topology in motion** — charge is not only a static integral; it controls trajectories (Hall angle, pair deflection).  
2. **Chirality as a dynamical degree of freedom** — helicity can lock, oscillate, or rotate under drive.  
3. **Pair annihilation** — explicit realisation of opposite charges summing to a trivial total while local physics remains nontrivial until annihilation.  
4. **Experimental control** — currents, fields, and pinning landscapes manipulate skyrmions in real devices, showing that topological charge is operationally useful.

---

## 5. What it does not replace

Skyrmion dynamics is classical or semiclassical micromagnetics (LLG + Thiele). It does not compute a fermionic Callias index or protect lattice Dirac zero modes. The 8-component Wilson + isospin embedding and local diagnostics remain the correct path for a quantitative \(N_{\rm def}\) demonstration.

---

## Compact statement

Skyrmion dynamics, organised by the Thiele equation, turns topological charge into directed motion (skyrmion Hall effect), internal oscillations (breathing / helicity), and pair processes (hybridization, annihilation). It is the real-time, continuum counterpart of the topology → transport-asymmetry chain used in the microscopic-cone program. It strengthens the cross-scale chirality narrative without replacing the lattice index calculation; the remaining bottleneck is still geometric scale separation on the fermionic pair.
