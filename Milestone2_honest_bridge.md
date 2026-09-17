# Milestone 2 — Honest bridge (L ≤ 10)

Tony Kawas / 17 September 2026.

**Purpose:** First defensible translation layer from locked lattice facts to coarse-grained interpretation.  
**Not:** full unification, Bessel identity, FDM profile, exact D_χ/κ theorem, or L≥12 physics.

---

## A. Trusted input (Milestone 1)

- Soft sector exists at L=8,10 (ARPACK + PRIMME).
- Molecular regime; plain γ₅ fails; χ_βn organizes soft vs bulk.
- Only L≤10 used below.

---

## B. Soft eigenvalues and splitting

Parameters: m₀=0.3, v=2, w=1.

| L | sep | soft \|λ\| | splitting \|λ₁\|−\|λ₀\| |
|---|-----|-----------|-------------------------|
| 8 | 5 | 0.000435, 0.001639, 0.001911, 0.003215 | **0.00120** |
| 10 | 6 | 0.000779, 0.001496, 0.002199, 0.002636 | **0.00072** |

**Direct observation:** Soft cluster remains near zero; pairwise splitting is O(10⁻³). At larger L (still molecular), splitting is smaller in this comparison — consistent with weaker hybridization as volume/separation grows, but **not** yet asymptotic isolation.

---

## C. Mass-texture density and core weights

For each soft mode ψ, define site density dens(x)=∑_s |ψ_s(x)|² and local texture density contributing to

\[
\chi = \sum_x \psi(x)^\dagger \big[\beta\otimes(\tau\cdot\hat n(x))\big]\psi(x).
\]

Core balls: radius 2 lattice units about each defect center. P₁, P₂ = integrated dens in each ball; P_rest = 1−P₁−P₂ (bridge + bulk).

### L = 8, sep = 5

| mode | χ | P₁ | P₂ | P_rest | IPR |
|------|------|------|------|--------|------|
| 0 | −0.822 | 0.095 | 0.095 | 0.811 | 0.0039 |
| 1 | −0.797 | 0.092 | 0.092 | 0.816 | 0.0051 |
| 2 | −0.817 | 0.106 | 0.106 | 0.788 | 0.0043 |
| 3 | −0.797 | 0.092 | 0.092 | 0.816 | 0.0056 |

### L = 10, sep = 6

| mode | χ | P₁ | P₂ | P_rest | IPR |
|------|------|------|------|--------|------|
| 0 | −0.814 | 0.032 | 0.032 | 0.936 | 0.0018 |
| 1 | −0.800 | 0.029 | 0.029 | 0.942 | 0.0019 |
| 2 | −0.807 | 0.018 | 0.018 | 0.965 | 0.0015 |
| 3 | −0.812 | 0.048 | 0.048 | 0.904 | 0.0019 |

**Direct observations:**

1. **χ stable:** mean χ ≈ **−0.808** at both L (soft anti-alignment holds spatially in aggregate).
2. **Perfect core balance:** P₁ = P₂ for every soft mode → equal ownership of both defects (molecular, not single-core).
3. **Most weight outside core balls:** P_rest ≫ P₁+P₂, especially at L=10 → delocalized / bridge-heavy soft density at these volumes.
4. **IPR small** and decreases with L → more spread out, consistent with molecular delocalization on a larger torus.

---

## D. Observable facts vs effective estimates

### Direct observables (Layer 1 + this note)

- Soft \|λ\| and splitting values above
- χ ≈ −0.81 for soft modes
- P₁ = P₂; P_rest dominant
- IPR trends

### Effective estimates (interpretive, not theorems)

| Quantity | Estimate | Caveat |
|----------|----------|--------|
| Hybridization scale | Δλ ~ 10⁻³ (L=8) → ~7×10⁻⁴ (L=10) | Static spectrum only; not a measured decay rate |
| Core localization fraction | ~9–11% per core (L=8); ~2–5% per core (L=10) | Core radius = 2 is a convention |
| Diffusion-like length | Soft weight fills O(L) | No time-dependent diffusion experiment |
| κ / D_χ | **Not fixed** | Need response or driven setups |

These estimates can **inform** an effective continuity picture (Milestone-scale transport language) but do **not** calibrate the propagation law.

---

## E. Honest bridge claim

> The trusted L≤10 soft sector supports a **spatially balanced, delocalized, mass-texture-organized** density: soft modes share both defect cores equally, carry stable χ_βn ≈ −0.8, and put most probability outside tight core balls. Eigenvalue splitting provides a numerical hybridization scale O(10⁻³). This is a legitimate microscopic bridge to coarse-grained “molecular texture” language. It does **not** establish conical spectral identity, FDM soliton profiles, or exact hydrodynamic coefficients.

---

## F. Explicit limits

- No L≥12 claims
- No Bessel b₃/b₁ identification
- No FDM r_c mapping
- No theorem-level D_χ, κ
- No galactic/cosmological closure

---

## G. Milestone 2 status

**DONE** as an honest first span.

Next (Milestone 3): dictionary decision — derive or drop conical spectral-ratio claims for this operator.
