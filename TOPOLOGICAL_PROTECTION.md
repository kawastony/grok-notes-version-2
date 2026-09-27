# Topological protection — investigation note

**Role in TAFA:** primary micro-side reason that lower bridge activity need not drive higher identity change.

---

## What is protected

| Object | Protection mechanism |
|--------|----------------------|
| Defect topological charge Q | Homotopy class (π₂ for hedgehogs); continuous deformation cannot change Q without singularity passage |
| Index / zero-mode count | Callias / Atiyah–Singer-type index; stable under continuous deformation of background |
| Chirality / texture orientation | Discrete or winding invariant; anti-alignment χ_βn observed in lattice |
| Soft-mode subspace dimension | Tied to index; soft eigenvalues can move, count of near-zero modes protected |

---

## Why this supports non-propagation

In Example 1 (micro → galactic):
- Q fixed under boost paths while soft eigenvalues and G12 weight **move**.
- Topology locks identity of each core; dynamics rearrange weight **between** cores.
- Meso average therefore sees exchange without net topological pumping into μ_*.

In spectral-flow language: levels can cross or approach zero, but the **index** (net chirality / zero-mode count) is invariant — activity without identity change at the topological level.

---

## Limits

- Protection is against continuous deformation; violent processes (pair creation/annihilation, lattice dislocations that change topology) can change Q.
- Protection does not by itself set the SI value of μ_* or ω_*.
- Numerical program must continue to verify Q stability under refinement and under the boosts used for G12.

---

## Status

Topological protection is the cleanest existing micro argument for the non-propagation guardrail in the first scale-transfer example. It does not replace timescale separation or equal/opposite exchange; it complements them.
