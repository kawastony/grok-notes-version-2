# Topological index conservation — investigation

**Status:** Sharpens TOPOLOGICAL_PROTECTION.md with index-focused statements for the lattice Dirac/Hamiltonian setting.

---

## 1. Index in this setting

For an elliptic operator D (lattice Dirac / Wilson–Dirac / Callias-type) on a compactified or asymptotically regular background:
\[
\mathrm{Index}(D) = \dim\ker D - \dim\ker D^\dagger
\]
(or a spectral asymmetry / η-invariant proxy on the lattice).

In defect language:
\[
\mathrm{Index}(D) \leftrightarrow N_{\rm def}
\]
when the asymptotic mass map has winding / degree N_def (Callias-type theorems).

---

## 2. Conservation statement

Under continuous deformations of the background that
- preserve asymptotic invertibility of the mass map, and
- do not pass through configurations where the gap closes at infinity or topology changes by defect creation/annihilation,

\[
\frac{d}{ds}\mathrm{Index}(D(s)) = 0.
\]

Eigenvalues may flow; the **net** zero-mode count (or chiral imbalance) does not.

---

## 3. Lattice operational criteria

| Check | Pass condition |
|-------|----------------|
| Soft multiplicity | Number of |λ| < λ_cut stable along path |
| Core charges Q_i | Constant under boost / separation (no pair creation) |
| Asymptotic texture | n·r̂ → ±1 (or locked map) at large r |
| Chirality residual | Mixing small vs continuum expectation |
| Refinement | Index stable as L increases / a decreases |

Prior program targets: prove Index(D)=N_def for multiple charges; extrapolate chirality to continuum.

---

## 4. Relation to spectral motion

- **Index conservation** = identity lock (what is chosen/protected at the micro pause).
- **Spectral motion** = activity (how soft eigenvalues and weights rearrange).
- Non-propagation to galactic scale uses both: index fixed ⇒ no topological pumping into μ_*; spectral motion ⇒ nonzero Var(δμ).

---

## 5. Callias contact (disciplined)

Callias: Index related to degree of the asymptotic mass map on a sphere at infinity.

**Allowed reading:** A quasi-static, topologically locked asymptotic region makes that degree well-defined — consistent with “pause as boundary condition.”

**Not allowed as theorem:** “Cosmic DE pause proves Callias zero modes exist on the lattice.” The lattice index is fixed by the defect background on the simulated volume; cosmology enters only under an explicit identification of asymptotics with cosmic geometry (open, interpretive).

---

## 6. Failure modes (when index need not conserve)

- Defect–anti-defect annihilation (topology change).
- Gap closing at the asymptotic boundary.
- Lattice artifacts that mix chiral sectors strongly.
- Open boundaries with flux leaking off the volume.

---

## 7. Status

Index conservation is the formal backbone of topological protection in the micro layer. It is what allows soft-mode spectral motion to be “activity without identity change,” which is required by the non-propagation guardrail in scale-transfer Example 1.
