# Soft-mode spectral motion — details

**Status:** Technical expansion of SOFT_MODE_DYNAMICS.md. Tied to lattice G12 / spectral-flow program.

---

## 1. Definition

Soft modes = eigenpairs (λ_a, ψ_a) of the lattice Hamiltonian (or Dirac operator) H with
\[
|\lambda_a| \ll \lambda_{\rm bulk}.
\]
Spectral motion = dependence of {λ_a} (and optionally eigenvectors) on a control path s:
\[
\lambda_a(s),\qquad
s \in \{\text{core boost, } v_{\rm coup},\text{ separation, Wilson mass,}\ldots\}.
\]

---

## 2. What moves vs what is conserved

| Quantity | Under continuous path s | Notes |
|----------|-------------------------|-------|
| λ_a(s) | **Moves** | Can approach/leave zero; avoided crossings |
| Spatial weight \|ψ_a\|² on cores | **Moves** | G12 weight slide |
| Index ℐ = n_+ − n_− (or net zero-mode count) | **Conserved** | Topological |
| Individual core charge Q_i | **Conserved** (if no singularity) | Homotopy |
| Gap to bulk | May shrink/grow | Continuum limit care |

**Spectral motion is the activity; index conservation is the identity lock.**

---

## 3. Spectral-flow picture

Along a path s ∈ [0,1]:
1. Track the lowest k eigenvalues (k ≥ expected index).
2. Count signed crossings of λ = 0 (or a small window).
3. Net crossings = Δℐ = 0 if topology of the background is preserved.
4. Individual λ_a may still wander — that wandering is spectral motion.

Lattice practice (prior runs):
- Boost / separation paths with fixed hedgehog+antihedgehog map → Q fixed, |λ| rearrange.
- G12 path: soft subspace projectors change; Tr(PQ) and geodesic length measure motion in the Grassmannian of the soft subspace, not a change of index.

---

## 4. Link to G12 / exchange

When two cores share soft weight:
\[
P_1(s) = \sum_{a\,{\rm soft}} \int_{\rm core1} |\psi_a(s)|^2,\quad
P_2(s) = \sum_{a\,{\rm soft}} \int_{\rm core2} |\psi_a(s)|^2.
\]
Spectral motion of the ψ_a induces
\[
G_{12} \sim \frac{d}{ds}(P_1 - P_2)
\]
(active exchange) while
\[
\sum_a \mathrm{sign}(\lambda_a)\ \text{or index}\ \text{stays fixed}.
\]

That is the micro content of “active bridge without identity change.”

---

## 5. Continuum and refinement caveats

- Soft λ must remain soft as a → 0 (or L → ∞ at fixed physical volume) or the mode is a lattice artifact.
- Wilson / domain-wall terms can mix chirality; residual chirality breaking is a known contamination source (prior chirality-mixing notes).
- Edge modes on finite volume can fake soft spectrum; interior localization checks required.

---

## 6. Observable contact (micro → galactic)

Spectral motion → time- or environment-dependent soft density → after coarse-graining, **structured variance** in meso dressing δμ, not a mean shift of μ_* (Example 1 non-propagation).

Candidate: residual correlation scale in hierarchical SPARC set by soft-tube width / defect separation, not by white noise.

---

## 7. Status

Spectral motion formalizes the “active” half of soft-mode dynamics. Index conservation formalizes the “locked” half. Together they underwrite the non-propagation guardrail in micro→galactic scale transfer.
