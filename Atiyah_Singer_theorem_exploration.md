# Atiyah–Singer index theorem — exploration and relation to Callias / lattice program

Tony Kawas / 16 September 2026.

---

## 1. Statement

The Atiyah–Singer (AS) index theorem (1963) equates two integers associated to an elliptic differential (or pseudodifferential) operator P on a **compact** oriented manifold X:

\[
\mathrm{Index}_{\rm analytic}(P) = \dim\ker P - \dim\coker P = \mathrm{Index}_{\rm topological}(P).
\]

The topological index is computed from the symbol of P and characteristic classes of X (Todd class, Â-genus, Chern character of the symbol class). In cohomological form:

\[
\mathrm{ind}\,P = \bigl\langle \mathrm{Todd}(TX\otimes\mathbb C)\smile \varphi^{-1}\mathrm{ch}(\sigma(P)),\,[X]\bigr\rangle.
\]

For the Dirac operator on a compact even-dimensional spin manifold the formula specialises to

\[
\mathrm{Index}(D) = \hat A(X)[X]
\]

(or more generally ⟨Â(TM) ch(E), [M]⟩ when coupled to a vector bundle E).

---

## 2. Analytic vs topological index

- **Analytic index** — dimension of the space of solutions minus the dimension of the cokernel; a spectral invariant.
- **Topological index** — a characteristic-class integral (or K-theory pushforward) built only from the principal symbol and the topology of the manifold and bundles.

AS asserts they are equal. That is why an integer computed from analysis equals an integer computed from topology — the foundation of index theory in geometry and physics.

---

## 3. Dirac operator and physics

For the chiral Dirac operator on a compact even-dimensional spin manifold:

\[
\nu_+ - \nu_- = \int_M \Omega(\mathcal R,\mathcal F),
\]

where ν± are the numbers of positive/negative chirality zero modes and Ω is the anomaly polynomial (Â-genus times Chern character of the gauge bundle). This is the continuum origin of the chiral anomaly and of the statement that the net number of zero modes is topological.

On **odd**-dimensional compact manifolds the ordinary Dirac index vanishes; that is one reason Callias-type theorems (potential invertible at infinity on non-compact odd-dimensional space) are needed for monopoles and hedgehogs in 3D.

---

## 4. Atiyah–Singer vs Callias

| | Atiyah–Singer | Callias |
|--|---------------|---------|
| Manifold | Compact | Non-compact (open), typically odd-dimensional |
| Operator | Elliptic (e.g. Dirac) | Dirac + potential invertible at infinity |
| Index determined by | Bulk characteristic classes | Asymptotic mass map on sphere at infinity |
| Even dimensions | Nontrivial in general | Index often vanishes for algebraic reasons |
| Odd dimensions | Index vanishes for ordinary Dirac | Nontrivial; degree of asymptotic U = Φ/|Φ| |
| Boundary extensions | APS (η-invariant) | Callias-type with APS boundary conditions |

Callias can be viewed as the open-space, odd-dimensional counterpart that recovers a topological index from asymptotic data when the bulk AS index would be zero or undefined. APS further extends AS to compact manifolds with boundary; combinations of APS + Callias handle non-compact manifolds with boundary.

---

## 5. Relation to the lattice / cone program

| AS / index theory | Lattice Callias program |
|-------------------|-------------------------|
| Analytic index = topological index | Target: lattice Index(D) = N_def |
| Zero modes counted by topology | Soft near-zero modes; spectral flow proxy for index |
| Compact even-dim Dirac | Continuum limit of lattice Dirac on large torus / open BC |
| Anomaly polynomial | Continuum source of anomaly inflow / chiral residual |
| APS boundary correction | Open-boundary single-defect runs; η-type finite-volume effects |

The lattice construction is a UV regularisation of a Callias (not pure AS) problem: non-compact odd-dimensional physics with a mass defect. AS supplies the broader index-theory language and the compact, even-dimensional archetype. The numerical goal — Index(D) = N_def — is the lattice analogue of “analytic index equals topological index,” with the topological side given by the hedgehog winding.

---

## 6. Why AS still matters for the program

1. **Conceptual parent** — Callias, APS, and lattice index theorems are descendants of the same idea: analysis = topology for elliptic operators.
2. **Anomaly matching** — the continuum anomaly polynomial that sources inflow is the same density that appears in AS for Dirac operators.
3. **Boundary / finite-volume corrections** — APS η-invariants and related spectral asymmetries organise finite-size and open-boundary effects seen on the lattice.
4. **K-theory formulation** — modern lattice index results (Wilson spectral flow, K-theory identification of the index) sit in the same K-theoretic framework that Atiyah–Singer made central.

---

## 7. Compact statement

The Atiyah–Singer theorem equates the analytic index of an elliptic operator on a compact manifold with a topological index built from characteristic classes. For Dirac operators this yields the Â-genus and the chiral anomaly polynomial. Callias is the non-compact, odd-dimensional counterpart relevant to hedgehogs; the lattice 8-component program aims at the discrete version of that Callias equality (Index = N_def). AS provides the overarching index-theory structure in which both Callias and the lattice target sit.
