# Callias index theorem — exploration and link to the lattice program

Tony Kawas / 16 September 2026.

---

## 1. Setting

The Callias index theorem (Callias 1978, and many later extensions) concerns **Dirac operators on non-compact odd-dimensional manifolds** perturbed by a potential that is invertible at infinity. Unlike the Atiyah–Singer theorem on compact manifolds, the index is determined by the **asymptotic behaviour of the potential on a sphere (or hypersurface) at infinity**, not by a bulk characteristic class integrated over the whole space.

Canonical physical setting: a Dirac operator in three spatial dimensions coupled to a Higgs-like (or isospin) mass matrix that approaches a constant invertible value at spatial infinity, with nontrivial winding of that asymptotic map.

---

## 2. Continuum statement (Euclidean form)

Let n be odd (typically n = 3). Let Q be the free Dirac operator on ℝⁿ and Φ a Hermitian matrix-valued potential such that:

- Φ is smooth,
- Φ² is bounded below by a positive constant outside a compact set (invertible at infinity),
- derivatives of Φ decay suitably.

Define the perturbed operator

\[
L = Q + \Phi.
\]

Then L is Fredholm, and its analytic index

\[
\mathrm{Index}(L) = \dim\ker L - \dim\ker L^*
\]

is given by a topological integral of the asymptotic unitarization

\[
U(x) = \frac{\Phi(x)}{|\Phi(x)|} = \mathrm{sgn}(\Phi(x))
\]

over a large sphere S^{n−1}_R:

\[
\mathrm{Index}(L) = c_n \lim_{R\to\infty} \int_{S^{n-1}_R} \mathrm{tr}\bigl( U\, (dU)^{n-1} \bigr)
\]

(with an explicit combinatorial prefactor c_n; equivalent forms appear in Callias, Anghel, Gesztesy–Waurick, and others). Equivalently, the index equals the degree (winding) of the map

\[
U\big|_{S^{\infty}} : S^{n-1} \to \mathrm{unitary\ matrices}
\]

(or the Chern character evaluation of the positive eigenbundle of U on the sphere at infinity).

**Key structural fact:** the index is completely determined by asymptotic data; core details of Φ inside a compact region do not change the index as long as invertibility at infinity and the asymptotic class are preserved.

---

## 3. Hedgehog / monopole realisation (n = 3)

For an SU(2) or isospin mass texture of hedgehog form

\[
\Phi(\mathbf r) = v\, f(r)\, \hat{\mathbf n}(\theta,\phi)\cdot\boldsymbol\tau,
\]

with f(r) → 1 as r → ∞ and asymptotic map of degree N_def (winding of the unit vector field on the sphere), the Callias theorem yields

\[
\mathrm{Index}(L) = N_{\rm def}
\]

(up to conventional sign/normalisation). A single unit hedgehog supports a protected zero mode (or a definite imbalance of chiral zero modes). An antihedgehog has opposite index. A well-separated hedgehog–antihedgehog pair has total index zero, but two near-zero modes that hybridize when the separation is not large compared with the bulk correlation length.

This is precisely the continuum target of the 8-component lattice construction used in this repository.

---

## 4. Relation to anomaly inflow and axial anomalies

Callias’ original motivation was the axial anomaly on open spaces. The same asymptotic data that fix the index also determine the inflow of axial charge onto the defect. In modern language:

- bulk anomaly polynomial + defect boundary condition → inflow current onto the core,
- the Callias index counts the net zero modes that realise that inflow in the spectrum.

This is the continuum counterpart of the “topological sign → transport asymmetry” step in the microscopic-cone / chirality program.

---

## 5. Lattice realisation in this project

| Continuum Callias | Lattice (this work) |
|-------------------|---------------------|
| Dirac operator Q | 8-component Wilson–Dirac |
| Potential Φ | β ⊗ (v f(r) τ · n̂) mass texture |
| Asymptotic degree | N_def of the hedgehog map |
| Index(L) = N_def | Target: Index(D) = N_def (spectral flow / local diagnostics) |
| Zero modes | Soft near-zero eigenvalues |
| Pair Index = 0 | Compensated pair; hybridized soft sector |

**What has been established numerically**

- Algebraic embedding: only the 8-component (Dirac ⊗ isospin) class anticommutes correctly with the kinetic terms and admits a nontrivial mass sphere.
- Soft near-zero sector appears for single defects and, more strongly, for opposite-charge pairs.
- Softness is robust under profile shape, width, and amplitude (UV details) — consistent with the index depending only on asymptotics.
- At L ≤ 10, sep/ξ ∼ 1.5–2 the pair remains hybridized (molecular regime); independent core localization requires sep ≫ ξ.

**What remains open**

- Clean continuum extrapolation of Index(D) → N_def for multiple topological charges.
- Fully resolved opposite local charges on a large pair geometry.
- Spectral-flow index equal to N_def on lattices large enough that finite-volume and Wilson artefacts are under control.

---

## 6. Why the theorem matters for the cone / chirality program

1. **Topological protection** — the index is stable under continuous deformations that preserve invertibility at infinity and the asymptotic class. That justifies treating N_def as a robust microscopic input.
2. **Asymptotics over core** — core profile is irrelevant for the index; only the winding matters. Matches the lattice observation that f(r) changes do not destroy the soft sector.
3. **Pair structure** — total index of a compensated pair vanishes; local physics near each core remains nontrivial until separation exceeds the correlation length. Matches the molecular regime seen on the lattice.
4. **Bridge to transport** — anomaly inflow tied to the same asymptotic data supplies the continuum mechanism for “defect chirality → directed transport,” which the cone program elevates to galactic scales.

---

## 7. Compact statement

The Callias index theorem states that the Fredholm index of a Dirac operator on odd-dimensional open space, perturbed by a potential invertible at infinity, equals a topological invariant of the asymptotic mass map (degree / Chern character on the sphere at infinity). For a hedgehog of winding N_def the index is N_def. The lattice 8-component Wilson + isospin construction is a UV regularisation of that continuum problem; numerical soft modes and their robustness under core details are consistent with Callias, while independent core localization remains a finite-volume (sep ≫ ξ) task.
