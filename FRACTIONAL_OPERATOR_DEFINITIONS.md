# Fractional operator definitions vs Legendre O_μ

## Two definitions of O_μ

### A. Geometric (primary)

\[
\mathcal{O}_μ:\ \text{junction transmission mode},\quad
\Delta_μ = ν_0
\]
with ν₀ the Legendre mixed-BC root (2.3713 pure / 2.31 scar-adjusted).

This is a **spectral** definition on S² restricted to the sector — not an abstract fractional power.

### B. Scaffold fractional (Paper 24)

\[
\mathcal{O}_μ \sim (-\nabla^2)^{-α} X,\qquad
\frac{\Delta_μ}{\Delta_X}=\frac{3}{7}
\]
chosen so that with X∼Σ_b^{1/3} one gets μ∼Σ_b^{1/7}.

## Reconciliation

- Fractional form is a **1D kinematic surrogate** that encodes the same dimension shift in a translation-invariant medium.
- Physical operator on the cone junction is the **Legendre mode** with Δ_μ=ν₀.
- They agree on numbers only if α is fixed by
  \[
  \Delta_X - 2α = ν_0
  \quad\Rightarrow\quad
  α = \frac{\Delta_X - ν_0}{2}.
  \]
  With Δ_X≈1.846 and ν₀≈2.37 this would make α **negative** (O_μ more relevant than X), which is consistent with a boundary/response operator reading a bulk mismatch, but it shows the fractional picture is not a bulk Riesz potential of positive order in the usual sense.

## Preferred language going forward

1. **Define** O_μ as the Legendre junction operator (Δ_μ=ν₀).  
2. **Use** γ=ν₀/(n_eff Δ_X) as the scaling formula.  
3. **Reserve** (−∇²)^{-α} for heuristic continuum limits only; do not treat it as the derivation of γ.

## Fractional calculus — short glossary for this program

| Object | Meaning here |
|--------|----------------|
| (−∇²)^{-α} | Formal Riesz potential; scaffold only |
| Δ_μ/Δ_X=3/7 | Scaffold ratio for cubic sourcing → 1/7 |
| ν₀ | Actual spectral dimension of the junction mode |
| α from Δ_X−2α=ν₀ | Not required once ν₀ is primary |

**Status:** Fractional definitions explored and demoted to surrogate; Legendre O_μ is the operational definition.
