# Renormalization group theory — investigation for the Callias / cone program

Tony Kawas / 16 September 2026.

---

## 1. RG in brief

The renormalization group organizes how couplings and observables change with scale. In lattice field theory the continuum limit is an RG fixed point: lattice spacing a → 0 with physical masses and volumes held fixed in units of a correlation length ξ.

Operators are classified by scaling dimension:
- **Relevant** — grow in the IR; must be tuned (e.g. mass).
- **Marginal** — logarithmic running.
- **Irrelevant** — die in the IR; lattice artefacts of dimension >4 are typically irrelevant and vanish as a → 0.

Topology can be protected along RG flows: topological defect lines, indices, and anomalies often constrain or survive the flow even when microscopic details change.

---

## 2. Wilson fermions and the continuum limit

The Wilson–Dirac operator explicitly breaks chiral symmetry at finite a. In the RG language:

- The Wilson term is an irrelevant operator (dimension 5) that lifts doublers.
- Chiral symmetry is restored in the continuum limit if the relevant mass is tuned to the critical line.
- O(a) artefacts remain unless improved (clover, etc.); they are irrelevant but can be numerically large at coarse a.

For topology: the index of a suitably defined lattice Dirac operator can equal the continuum topological charge for smooth enough backgrounds when a is small (overlap/Ginsparg–Wilson; also recent K-theory results relating Wilson spectral flow to the continuum index). Exact zero modes at finite a are not guaranteed for Wilson; near-zero modes and spectral flow are the practical proxies.

---

## 3. Callias defect as a relevant / topological insertion

The hedgehog mass texture is a **spatially varying relevant deformation**. Its asymptotic winding is topological and cannot be removed by local RG-irrelevant adjustments of the core profile. That is why:

- Changing f(r) (tanh, exp, compact, …) did not destroy the soft sector.
- Changing core width/amplitude modulated eigenvalues but did not eliminate softness.
- Opposite-charge pairs remain softest — the topological compensation is RG-stable in the sense that it is not an artefact of a single UV cutoff choice.

Under coarse-graining, the core details (width ∼ a or a few a) are UV; the winding number and the existence of soft modes tied to that winding are IR/topological data.

---

## 4. Finite-size and correlation length in RG language

The bulk mass m₀ is a relevant coupling. It sets

\[
\xi \sim 1/m_0
\]

(measured ≈ 3.3 lattice units at m₀ = 0.3). The dimensionless ratio sep/ξ controls hybridization:

- sep/ξ ≲ 2 → molecular regime (our L ≤ 10 window).
- sep/ξ ≫ 1 → isolated defect modes (exponential decoupling).

Finite-L corrections are finite-size scaling under the RG: the torus is an IR cutoff. Non-monotonic Δλ(sep) at small L is an IR finite-volume effect, not a failure of the topological class.

A continuum extrapolation is an RG trajectory: a → 0, L → ∞, m₀a fixed or tuned, sep/ξ fixed ≫ 1, then measure index, chirality, and localization.

---

## 5. What RG says about the chirality / cone program

| RG notion | Cone / Callias counterpart |
|-----------|----------------------------|
| Relevant mass deformation | Hedgehog mass texture (core details UV) |
| Topological invariant along flow | N_def / winding; anomaly inflow |
| Irrelevant lattice artefacts | Wilson O(a) terms; profile shape |
| IR correlation length ξ | Bulk gap scale; controls mode localization |
| Continuum fixed point | a → 0 with soft modes → exact Callias zeros |
| Defect RG / defect CFT | Microscopic cone as a defect; chiral residual as IR observable |

Chirality and anomaly inflow are robust under RG in the same way topological defect lines constrain 2D flows: they are not washed out by irrelevant operators. That supports treating the chiral residual as a continuum, scheme-independent structure once the lattice index is under control.

---

## 6. What RG does not fix at present

- It does not replace the need for larger L: sep/ξ is an IR geometric constraint.
- It does not by itself prove Index(D) = N_def on the lattice; that remains a spectral/index calculation (spectral flow, local diagnostics).
- Wilson artefacts are irrelevant in principle but can dominate at coarse a; improvement or overlap would be the RG-motivated next operator upgrade if resources allow.

---

## Compact statement

Renormalization group theory frames the lattice Callias program as a continuum limit: the hedgehog winding is a topological insertion stable under irrelevant deformations, the bulk mass sets the correlation length that controls mode hybridization, and Wilson artefacts are irrelevant but numerically present at small L. The soft sector’s robustness across profiles and (w,v) is consistent with topology surviving the RG. The remaining obstruction is IR geometric (sep ≲ ξ), not a missing relevant operator or a failed continuum fixed-point structure.
