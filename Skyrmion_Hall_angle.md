# Skyrmion Hall angle — investigation and links to the cone/chirality program

Tony Kawas / 16 September 2026.

---

## 1. Definition

Under a drive current a skyrmion acquires a velocity with components parallel and perpendicular to the current. The **skyrmion Hall angle** is

\[
\theta_H = \tan^{-1}\Bigl(\frac{v_\perp}{v_\parallel}\Bigr).
\]

It quantifies the transverse deflection caused by the topological gyro coupling.

---

## 2. Origin in the Thiele equation

From
\[
\mathbf G\times\dot{\mathbf R} + \alpha\mathcal D\dot{\mathbf R} = \mathbf F_{\rm drive},
\]
with \(\mathbf G = 4\pi Q\,\hat{\mathbf z}\), the steady velocity satisfies (schematically)

\[
\tan\theta_H \sim \frac{G}{\alpha D} \propto \frac{Q}{\alpha D}
\]

(for spin-transfer drive; detailed factors depend on adiabatic vs non-adiabatic torque parameters \(\alpha,\beta\) or \(\xi\)).

**Key points:**
- \(\theta_H\) is proportional to the topological charge \(Q\).
- Sign of \(\theta_H\) flips with sign of \(Q\): skyrmions and antiskyrmions deflect toward opposite edges.
- When \(\alpha=\beta\) (or equivalent) the Hall angle can vanish for pure STT in some geometries; pinning or SOT can restore a finite angle.
- Skyrmioniums (net \(Q=0\)) can still show a residual Hall angle if the inner and outer topological contributions are spatially imbalanced.

---

## 3. Skyrmion vs antiskyrmion

| Property | Skyrmion | Antiskyrmion |
|----------|----------|--------------|
| Topological charge | \(Q=+1\) (typical) | \(Q=-1\) |
| Hall angle sign | One transverse direction | Opposite transverse direction |
| \(|\theta_H|\) | Similar magnitude | Similar; experiments report 6–12% differences attributable to extra transverse terms in a generalized Thiele equation |
| SOT anisotropy | Often isotropic | Can be strongly current-direction dependent |

Coupled skyrmion–antiskyrmion pairs can propagate with cancelled net Hall deflection — a dynamical analogue of a compensated topological pair.

---

## 4. Link to the Callias / microscopic-cone program

| Skyrmion Hall angle | Callias / cone program |
|---------------------|------------------------|
| \(\theta_H\propto Q\) | Transport asymmetry \(\propto N_{\rm def}\) / chiral residual |
| Opposite deflection for opposite \(Q\) | Opposite local charges of hedgehog / antihedgehog |
| Net Hall cancellation of a pair | Global index 0 of a compensated pair |
| Gyro term is topological | Index and anomaly inflow are topological |
| Chirality (DMI) sets texture and thus effective drive response | Cone chirality sets residual sign and preferred flow |

**Operational meaning**  
The Hall angle is the laboratory, real-time statement of “integer topological charge produces a directed transverse response.” That is the same organising principle as:

Topological sign → defect chirality → transport asymmetry → macroscopic handedness.

In magnets the response is a deflection angle; in the cone program it is a residual in galactic dynamics or an anomaly-inflow current.

---

## 5. What the Hall angle does and does not supply

**Useful**  
- Direct, measurable link between topological charge and directed motion.  
- Sign structure that distinguishes opposite charges.  
- Pair cancellation as a dynamical check of net-zero topology.

**Not a substitute**  
- Classical/semiclassical micromagnetics; does not compute a fermionic Callias index or protect lattice Dirac zero modes.  
- The 8-component Wilson + isospin embedding remains the correct path for a quantitative \(N_{\rm def}\) demonstration.

---

## Compact statement

The skyrmion Hall angle is the transverse deflection angle of a current-driven skyrmion, set by the topological gyro coupling and therefore proportional to the skyrmion charge \(Q\). Opposite charges deflect oppositely; compensated pairs can cancel the net Hall effect. It is the dynamical, continuum embodiment of topology → directed transport, and thus a close analogue of the chiral residual / anomaly-inflow step in the microscopic-cone program. It does not replace the lattice index calculation; the remaining bottleneck is still geometric scale separation on the fermionic pair.
