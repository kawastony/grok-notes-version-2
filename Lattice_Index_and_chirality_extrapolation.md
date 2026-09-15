# Lattice Index(D) = N_def and continuum chirality extrapolation

Tony Kawas / 15 September 2026.

---

## 1. Goal

1. Demonstrate on the lattice that the number of zero-modes equals the topological degree N_def for multiple charges.  
2. Perform a controlled continuum extrapolation of 〈γ⁵〉 → ±1.

---

## 2. Lattice Index(D) = N_def — present status

### Construction

Angular hedgehog of degree N_def realised by the map
\[
\hat{\mathbf{n}}(\theta,\phi) = \bigl(\sin\theta\cos(N_{\mathrm{def}}\phi),\;\sin\theta\sin(N_{\mathrm{def}}\phi),\;\cos\theta\bigr)
\]
inside the mass matrix
\[
M = m_0 f(r)\,\begin{pmatrix}\boldsymbol{\sigma}\cdot\hat{\mathbf{n}} & 0 \\ 0 & -\boldsymbol{\sigma}\cdot\hat{\mathbf{n}}\end{pmatrix}.
\]

### Numerical results

**Degree N_def = 1**

| L | # of eigenvalues with \|λ\| < 10^{-6} | 〈γ⁵〉 of those modes |
|---|--------------------------------------|----------------------|
| 7 | 4                                    | ±0.024 (paired)      |
| 9 | 4                                    | ±0.027 (paired)      |

A protected kernel of dimension 4 appears. The modes come in opposite-chirality pairs. The continuum Jackiw–Rossi theorem predicts a single chiral zero-mode (Index = 1). The lattice operator therefore realises a multiple of the continuum index (most likely from residual doubling / open-boundary pairing / the particular 4-component embedding of the mass matrix).

**Degree N_def = 2**

| L | lowest \|λ\| cluster |
|---|---------------------|
| 7 | ∼ 0.007 (4-fold)    |
| 9 | ∼ 0.005 (4-fold)    |

The eigenvalues are small and decrease with L, but have not yet reached numerical zero. Higher charge requires better core resolution (more lattice points inside the winding region) before the kernel becomes exact.

### Interpretation

- Topological protection is visible: a robust near-zero cluster exists and is stable under refinement for N_def = 1.  
- The multiplicity and the residual opposite-chirality pairing show that the present discretisation has not yet isolated a single continuum chiral zero-mode.  
- Strict lattice equality Index_lat(D) = N_def is therefore **not yet proven** for this operator; what is proven is the existence of a topologically protected kernel whose dimension is a multiple of N_def and whose eigenvalues remain at zero under volume change.

### Path to a clean lattice index theorem

1. Replace the continuum-like central-difference operator by a Ginsparg–Wilson / overlap operator (exact lattice chiral symmetry).  
2. Or adopt domain-wall fermions with the hedgehog mass as a 5-d boundary condition.  
3. Count the spectral flow of the Hermitian Wilson operator as the mass parameter is varied through the hedgehog background (standard lattice index technique).  
Any of these yields an integer index that can be compared directly with N_def for several charges.

---

## 3. Continuum extrapolation of chirality

### Fixed-physical-volume sequence (box size ∼ 9, N_def = 1, smoothed angular texture)

| L  | a     | lowest \|λ\| | best \|〈γ⁵〉\| among near-zeros |
|----|-------|-------------|-------------------------------|
| 7  | 1.286 | ∼ 10^{-9}   | 0.139                         |
| 9  | 1.000 | ∼ 10^{-9}   | 0.027                         |
| 11 | 0.818 | ∼ 10^{-12}  | 0.003                         |

In this particular sequence the residual mixing **decreases** as a decreases, consistent with an O(a) (or higher) artefact that is vanishing. However the absolute values remain small because the near-zero multiplet still contains opposite-chirality partners; the “best” single-mode 〈γ⁵〉 is not yet approaching ±1.

### What a clean extrapolation requires

1. An operator that produces a **single** (or N_def) chiral zero-mode rather than a multiplet of mixed chirality.  
2. Fixed physical core width w and fixed physical volume ℓ ≫ w.  
3. Sequence a → 0, L = ℓ/a → ∞.  
4. Monitor 〈γ⁵〉 of the isolated zero-mode(s); expect
   \[
   \langle\gamma^5\rangle(a) = \pm 1 + c_1 a + c_2 a^2 + \cdots.
   \]

Until the multiplet structure is removed, a numerical extrapolation to ±1 cannot be completed cleanly.

---

## 4. Summary of what is established vs what remains

| Claim | Status |
|-------|--------|
| Continuum Index(D) = N_def | Analytic (Jackiw–Rossi / Callan–Harvey) — established |
| Lattice protected near-zero kernel for N_def = 1 | Demonstrated (exact zeros, stable under L) |
| Lattice Index_lat = N_def for several charges | **Not yet** — multiplicity and higher-charge resolution still open |
| Continuum limit of 〈γ⁵〉 → ±1 | Trend consistent with vanishing artefact; clean single-mode extrapolation still requires a better lattice chiral operator |
| Callan-Harvey inflow coefficient | Continuum derivation unchanged; lattice measurement of the current remains future work |

---

## 5. Recommended next steps (in order)

1. **Spectral-flow index** on the Hermitian Wilson operator in the hedgehog background — yields an integer that can be compared with N_def for degree 1, 2, 3 without requiring a pure chiral eigenstate.  
2. Once the integer index is confirmed for several N_def, return to a Ginsparg–Wilson realisation to isolate single chiral zero-modes and complete the 〈γ⁵〉 → ±1 extrapolation.  
3. Only after that measure the lattice vector current and match it to the continuum Callan-Harvey inflow expression.

---

## 6. Compact statement

The lattice currently demonstrates a topologically protected zero-mode cluster for N_def = 1 whose dimension is a multiple of the continuum index. Strict equality Index_lat(D) = N_def for multiple charges, and a clean single-mode continuum extrapolation of chirality to ±1, both require a lattice Dirac operator with better chiral properties (overlap, domain-wall, or spectral-flow definition of the index). The continuum Callan-Harvey construction and the analytic index theorem remain intact; the remaining tasks are purely discretisation improvements.
