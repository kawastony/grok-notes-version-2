# Non-circular SPARC intercept protocol — skeleton test

## What was run
Synthetic pipeline implementing Estimator B (max |d ln R / d ln r| of residual ratio R = g_obs/g_b):
- 20 synthetic galaxies with planted μ_* = 0.1 and Σ_b^{1/7} dressing
- Code path matches the pasted skeleton (Savitzky–Golay smooth, residual-inflection r_p, μ̂=1/r_p, X=(Σ_b/Σ_ref)^{1/7}, linregress)

## Result of synthetic run
- valid fraction = 1.0 (all galaxies returned a finite r_p)
- **Problem:** for several galaxies r_p hit the **outer data edge** (r=20), so μ̂ is biased low
- linregress then recovers a **spurious negative intercept** (−0.47 vs true 0.10) despite high |r|

**Lesson:** max-slope of R alone is not robust when the transition is weak or near the edge. The protocol is **executable** but needs stronger transition definition before real SPARC use.

## Required upgrades before real data
1. Restrict search window (e.g. exclude outer 20% of radial range).
2. Compare max-slope vs max-curvature vs threshold crossing of R.
3. Require R to actually rise (g_obs > g_b) before accepting r_p.
4. Hierarchical / mixed-effects model instead of plain linregress.
5. Unit-consistent SPARC table (r, V_obs, V_gas, V_disk, V_bulge, Σ_b).

## Status
Skeleton **runs**. Synthetic recovery **fails** under naive max-slope — protocol not yet science-ready. Non-circular design remains the right target.

Synthetic output saved locally as `synthetic_midpoint_results.csv` (artifacts).
