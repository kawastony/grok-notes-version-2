# Phase A: m₀ scan at fixed L=10, sep=6

Tony Kawas / 16 September 2026.

---

## Setup

- L = 10, sep = 6, w = 1.0, v = 3.0 (best Phase 2 geometry)
- m₀ ∈ {0.20, 0.25, 0.30, 0.40, 0.50, 0.60}
- Expected: increasing m₀ raises sep/ξ ≈ 6m₀ and should reduce hybridization if ξ ∼ 1/m₀ controls overlap

---

## Results

| m₀ | sep/ξ | \|λ₁\| | Δλ | F₂ (R=2) | F₄ (R=2) | F₂ (R=2.5) | F₄ (R=2.5) | IPR₁ | soft |
|----|-------|-------|-----|----------|----------|------------|------------|------|------|
| 0.20 | 1.20 | 0.00045 | 0.00134 | 0.026 | 0.029 | **0.053** | 0.043 | 0.0015 | Y |
| 0.25 | 1.50 | 0.00054 | 0.00105 | 0.000 | 0.013 | 0.000 | 0.017 | 0.0014 | Y |
| 0.30 | 1.80 | 0.00053 | 0.00052 | 0.020 | 0.017 | 0.036 | 0.023 | 0.0009 | Y |
| 0.40 | 2.40 | 0.00006 | 0.00017 | 0.000 | 0.003 | 0.000 | 0.010 | 0.0012 | Y |
| 0.50 | 3.00 | 0.00124 | 0.00272 | 0.013 | 0.020 | 0.015 | 0.024 | 0.0010 | Y |
| 0.60 | 3.60 | 0.00017 | 0.00046 | 0.001 | 0.006 | 0.004 | 0.011 | 0.0011 | Y |

Soft sector present at all m₀ (no collapse of the topological window).

---

## Trend assessment

**No systematic improvement with m₀.**

- F₂ and F₄ fluctuate between ∼0 and ∼0.05; highest F at *lowest* m₀ (0.20, R=2.5).
- IPR stays O(10⁻³) with no rising trend.
- Soft eigenvalues remain O(10⁻³–10⁻⁴); splitting does not tighten into a clean weakly-coupled pair pattern.

Increasing sep/ξ from ∼1.2 to ∼3.6 at fixed L=10 does **not** produce measurably less hybridization under the 2D/4D rotation diagnostics.

---

## Interpretation

1. **Simple ξ ∼ 1/m₀ is insufficient** at these volumes. Either:
   - the actual mode tails are not controlled by the free bulk gap alone (core structure, Wilson artefacts, or torus images dominate), or
   - sep/ξ must reach ≳ 5 before a clear exponential decoupling appears, and the present window is still too small to see the trend.

2. **Soft sector is robust** across the full m₀ range — the topological mechanism survives bulk-mass changes.

3. **Null result is informative**: hybridization at L≤10 is not primarily cured by raising the bulk gap. Geometric scale separation (larger absolute sep and L) remains the bottleneck.

---

## Compact statement

Phase A (6-point m₀ scan at L=10, sep=6) finds no systematic rise in post-rotation ownership F or IPR as sep/ξ increases from 1.2 to 3.6. The soft sector remains present. The simple bulk-gap lever does not resolve hybridization within the accessible window; larger absolute separation is still required.
