# Jackiw–Rossi / Callias embedding checklist + local diagnostic suite

Tony Kawas / 15 September 2026.

Two tools requested after the diagnosis that the remaining obstacle is topological/diagnostic mismatch rather than a broken free operator.

---

# Part I — Algebraic checklist for the continuum topological class

Before further numerics, the mass embedding must be shown to realise a continuum index-carrying defect. If this checklist fails, no lattice spectral flow will see a protected zero mode.

## I.1 Continuum prototypes

**Jackiw–Rebbi (1-D domain wall)**  
\[
H = -i\sigma_z\partial_x + m(x)\sigma_x,\qquad m(+\infty)=-m(-\infty)\ne0.
\]
Index = 1 (one normalisable zero mode of definite chirality).

**Jackiw–Rossi (2-D vortex)**  
Two anticommuting mass matrices with a vortex texture of winding n; Index = n.

**Callias / 3-D hedgehog (odd-dimensional)**  
Dirac operator on ℝ³ (or odd-dimensional open manifold) with a Hermitian mass endomorphism Φ(x) that is invertible at infinity and whose normalised map
\[
\hat\Phi:S^2_\infty\to\text{(space of normalised mass matrices)}
\]
has non-zero topological degree. The index equals that degree (Callias formula).

## I.2 Required algebraic structure (3-D hedgehog)

1. **Clifford algebra**  
   Kinetic matrices α_i (or γ_i) and mass matrices β^a must satisfy the appropriate anticommutation relations so that
   \[
   H^2 = -\nabla^2 + |\Phi|^2 + \text{(lower-order spin connection / gradient terms)}.
   \]
   In particular the mass matrices must anticommute with the kinetic Dirac matrices in the continuum limit.

2. **Number of mass matrices**  
   For a point defect in 3-D the target space of the normalised mass map must allow a non-trivial π₂. The classic SU(2) hedgehog uses three Pauli matrices (or an equivalent triplet of anticommuting Hermitian matrices).

3. **Asymptotic map**  
   \[
   \hat\Phi(\hat x) = \hat x^a\,T_a
   \]
   (or a higher-winding generalisation) must have
   \[
   \deg(\hat\Phi) = N_{\rm def}\in\mathbb Z\setminus\{0\}.
   \]

4. **Gap at infinity**  
   \(|\Phi(x)|\to v>0\) as \(|x|\to\infty\), uniformly in direction, so that the essential spectrum is bounded away from zero.

5. **Codimension / defect type**  
   The zero set of Φ must be a point (or a compact set of the correct codimension) for the Callias-type index to count bound states localised at that point.

6. **Chirality / grading**  
   There must exist a grading operator (continuum analogue of γ⁵ or a suitable involution) that anticommutes with H in the massless limit and with which the zero modes have definite eigenvalue. This is what allows a chiral index rather than a mere spectral asymmetry.

## I.3 Checklist applied to the present lattice embedding

| Requirement | Present block form \(M=v f(r)\,{\rm diag}(\sigma\cdot\hat n,\,-\sigma\cdot\hat n)\) | Status |
|-------------|----------------------------------------------------------------------------------|--------|
| Three anticommuting mass directions | Yes (Pauli matrices) | Pass |
| Asymptotic map of degree N_def | Yes (standard hedgehog / higher winding) | Pass |
| Gap at infinity | Yes (f→1, v>0) | Pass |
| Anticommutation with kinetic γ_i in continuum limit | Needs explicit verification in the chosen Dirac representation | Open |
| Correct continuum limit of H² | Needs verification that cross terms reproduce the continuum spin-connection / gradient pieces | Open |
| Grading operator with definite zero-mode chirality | γ⁵ used on the lattice; continuum identification must be confirmed | Open |

**Conclusion of the algebraic check**  
The geometric hedgehog and the gap condition are in place. The two open items are the precise continuum Dirac representation (does the block embedding arise from a legitimate continuum H that anticommutes correctly?) and the continuum limit of the graded structure. These must be settled by writing the continuum Hamiltonian that the lattice operator is discretising and confirming it belongs to the Callias / Jackiw–Rossi class.

## I.4 Minimal continuum target Hamiltonian (3-D)

A standard continuum form that does carry index N_def is
\[
H = \boldsymbol\alpha\cdot\mathbf p + \beta\,v f(r)\,(\boldsymbol\tau\cdot\hat{\mathbf x}),
\]
where α, β are Dirac matrices and τ are isospin (or flavour) Pauli matrices acting on an internal space. The lattice mass texture must be the discretisation of the second term, and the kinetic term the discretisation of the first, in a representation where the continuum index theorem applies.

If the present 4-component block form can be shown to be unitarily equivalent to this structure (or to a known index-carrying model), the embedding passes. If not, the block form must be replaced.

---

# Part II — Local diagnostic suite for a hedgehog–anti-hedgehog run

Global spectral flow on a single periodic hedgehog is expected to vanish. The correct lattice proxy for N_def is a **local** measurement around one core.

## II.1 Geometry

- Periodic L³ lattice (L large enough that two cores and the asymptotic region fit).  
- Hedgehog of charge +N_def at position R₊.  
- Anti-hedgehog of charge −N_def at position R₋, with |R₊−R₋| ≫ core radius w.  
- Both defects use the same smooth profile f(r)=tanh(r/w) and the same verified Wilson kinetic term.

## II.2 Diagnostics (compute for each core separately)

### D1. Local spectral density

Define a ball B_R of radius R (w ≪ R ≪ pair separation) centred on one core.  
For the lowest N_modes eigenpairs of H, compute the probability mass inside B_R:
\[
P_i(B_R)=\sum_{x\in B_R}|\psi_i(x)|^2.
\]
Report the number of modes with P_i(B_R) > threshold (e.g. 0.5) and |λ_i| small.

### D2. Local chirality density

\[
C_i(B_R)=\sum_{x\in B_R}\psi_i^\dagger(x)\gamma^5\psi_i(x).
\]
A protected zero mode should show |C_i| close to ±P_i inside the ball.

### D3. Sub-volume spectral asymmetry

Restrict the operator (or the spectral projector of the lowest modes) to the sub-volume B_R and compute a local η-invariant / spectral asymmetry
\[
\eta_{\rm loc}=\sum_i{\rm sign}(\lambda_i)\,P_i(B_R)
\]
(or a smoothed version). For an isolated core this should approach ±N_def in the continuum limit.

### D4. Inverse participation ratio (IPR)

\[
{\rm IPR}_i=\sum_x|\psi_i(x)|^4.
\]
Core-localised modes have IPR ∼ 1/(core volume); delocalised modes have IPR ∼ 1/L³. Use IPR to discard bulk continuum states.

### D5. Local spectral flow (optional, stronger)

Inside a fixed sub-volume, adiabatically turn the local hedgehog strength from 0 to 1 while keeping the anti-hedgehog fixed (or vice versa), and count signed crossings of eigenvalues that remain localised on that core. This is the direct local analogue of Index_sf.

## II.3 Success criteria

| Diagnostic | Expected signal for charge +1 core |
|------------|------------------------------------|
| D1 | At least one mode with P(B_R) ≳ 0.5 and |λ| small |
| D2 | That mode has C(B_R) ≈ ±P(B_R) |
| D3 | η_loc ≈ ±1 |
| D4 | IPR consistent with core volume |
| D5 | Local Index_sf = +1 |

Opposite signs for the anti-hedgehog core. Global sum of the two local indices = 0.

## II.4 Practical order of implementation

1. Algebraic confirmation that the continuum embedding belongs to the Callias / JR class (Part I).  
2. Build the pair geometry on the verified Wilson operator.  
3. Compute D1–D4 on the lowest ∼10–20 eigenmodes (no flow required yet).  
4. If local density + chirality already show a clear core-localised chiral mode, the index is essentially established.  
5. Only then optionally run local spectral flow (D5) for a direct integer.

---

## Compact statement

**Embedding checklist:** the geometric hedgehog and asymptotic gap are in place; the remaining algebraic questions are whether the block mass matrix arises from a continuum Hamiltonian in the Callias / Jackiw–Rossi class and whether the grading is correctly realised. These must be settled before further numerics.

**Local diagnostics:** replace global Index_sf by local spectral density, local chirality, sub-volume asymmetry, IPR, and (optionally) local spectral flow around each core of a hedgehog–anti-hedgehog pair. That is the correct lattice proxy for N_def.

Together the two tools convert the present “global flow = 0” impasse into a concrete, falsifiable programme.
