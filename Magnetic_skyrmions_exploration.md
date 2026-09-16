# Magnetic skyrmions — exploration and links to the cone/chirality program

Tony Kawas / 16 September 2026.

---

## 1. What a magnetic skyrmion is

A magnetic skyrmion is a localized, topologically nontrivial spin texture in which the magnetization direction covers the sphere (or a hemisphere for a meron) an integer number of times. The topological charge (skyrmion number) is

\[
Q = \frac{1}{4\pi}\int \mathbf n\cdot(\partial_x\mathbf n\times\partial_y\mathbf n)\,d^2x \in \mathbb Z.
\]

Typical values: \(Q=\pm 1\) (skyrmion / antiskyrmion), \(Q=0\) (skyrmionium), higher integers for multi-\(Q\) textures. In 3D the point-defect analogues are **hedgehogs** and **antihedgehogs** (emergent monopoles / antimonopoles).

---

## 2. Stabilization and chirality: Dzyaloshinskii–Moriya interaction

In non-centrosymmetric magnets or at interfaces, the antisymmetric Dzyaloshinskii–Moriya interaction (DMI)

\[
H_{\rm DMI} = \mathbf D_{ij}\cdot(\mathbf S_i\times\mathbf S_j)
\]

selects a fixed sense of spin rotation. That fixes the **chirality** (helicity) of the skyrmion:

- **Bloch-type** — spins rotate tangentially (bulk chiral magnets).
- **Néel-type** — spins rotate radially (interfacial DMI).
- **Anisotropic / antiskyrmion** — crystal symmetries (e.g. \(D_{2d}\)) or engineered DMI landscapes allow opposite or alternating chirality and tunable \(Q\).

Chirality is therefore not optional: it is built into the microscopic interaction that stabilizes the texture.

---

## 3. Transport signatures

Conduction electrons traversing a skyrmion accumulate a real-space Berry phase equivalent to an emergent magnetic field proportional to the topological charge density. Consequences:

- **Topological Hall effect (THE)** — transverse charge deflection without an external field.
- **Topological spin / orbital Hall effects** — spin- or orbital-polarized currents, including in antiferromagnetic skyrmion crystals where net emergent field cancels but orbital responses remain.

These are continuum, experimentally measured realisations of “topology → transport asymmetry.”

---

## 4. Relation to the Callias / microscopic-cone program

| Feature | Magnetic skyrmion / hedgehog | Callias hedgehog (8-component lattice) |
|---------|------------------------------|----------------------------------------|
| Order parameter | Unit magnetization \(\mathbf n\) | Normalized mass map \(\hat\Phi\) |
| Topology | \(Q\in\mathbb Z\) (\(\pi_2\) of spin sphere) | \(N_{\rm def}=\deg(\hat\Phi)\) |
| Chirality | Fixed by DMI sign | Orientation / winding of cone defect |
| 3D point defect | Hedgehog / antihedgehog (monopole) | Same geometric object as mass texture |
| Transport | Topological Hall, emergent field | Anomaly inflow, residual chiral term, galactic handedness |
| Pair / molecule | Skyrmion–antiskyrmion, skyrmionium | Hedgehog–antihedgehog soft-mode pair |

**Direct geometric parallel**  
The 3D magnetic hedgehog is the same map \(S^2\to S^2\) that defines the Callias mass texture. In magnets the map is carried by local moments; in the lattice Dirac theory it is carried by the isospin mass matrices \(\beta\otimes\boldsymbol\tau\). The integer that counts skyrmions is the same integer that counts fermionic zero modes.

**Chirality parallel**  
DMI selects a preferred handedness of the spin spiral; the cone program’s chiral residual selects a preferred orientation of energy/transport flow. Both are microscopic handedness → macroscopic observable asymmetry.

**Molecular regime**  
A skyrmion–antiskyrmion pair at finite separation hybridizes; the net \(Q\) can cancel while local textures remain. That is the magnetic analogue of the shared soft modes we observe at L ≤ 10.

---

## 5. What skyrmions add to the narrative

1. **Experimental existence** — skyrmions and hedgehogs are routinely imaged and manipulated in real materials; topology is not abstract.  
2. **Chirality as a material input** — DMI shows how broken inversion + spin–orbit naturally produces a fixed handedness.  
3. **Transport from topology** — THE is a measured, topology-driven Hall response; a concrete precedent for “defect chirality → observable asymmetry.”  
4. **3D hedgehog language** — the same geometric object appears in magnets and in the Callias mass map.

---

## 6. What they do not replace

Magnetic skyrmions are classical or semiclassical spin textures (or electronic bands coupled to them). They do not compute a fermionic Callias index or protect lattice Dirac zero modes. The 8-component Wilson + isospin embedding remains the correct framework for a quantitative \(N_{\rm def}\) demonstration and for the anomaly-inflow side of the cone program.

---

## Compact statement

Magnetic skyrmions and hedgehogs are experimentally established topological spin textures stabilized by chiral DMI. Their topological charge, chirality, pair hybridization, and topological Hall response form a close continuum analogue of the Callias mass map, the cone’s chiral residual, and the soft-mode physics seen on the lattice. They strengthen the cross-scale chirality narrative without replacing the fermionic index calculation. The lattice program’s remaining bottleneck is still geometric scale separation.
