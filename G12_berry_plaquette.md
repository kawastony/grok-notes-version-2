# Berry / Wilczek–Zee plaquette holonomy (L=10, d=3)

**Date:** 2026-09-26  
**Status:** First measurement executed.

## Protocol

Second parameter α = core-2 boost fraction:  
`v1 = v0(1+s ε)`, `v2 = v0(1+α ε)`, ε=0.05.

Tiny plaquette δs=δα=0.05 at three centers:

1. Bottleneck region s₀=0.45, α₀=0  
2. Flank s₀=0.40, α₀=0  
3. Baseline s₀=0, α₀=0  

Holonomy:

```
γ = arg det(U₁₂ U₂₃ U₃₄ U₄₁)
```

with U_ab = polar/SVD unitary of V_a† V_b (Procrustes).

## Results

| Center | γ (rad) | γ (deg) | Edge singular values (min) |
|--------|---------|---------|----------------------------|
| **s₀=0.45 (bottleneck)** | **≈ π** | **≈ 180°** | edges 2→3, 3→4: **σ_min ≈ 0.011, 0.004** |
| s₀=0.40 (flank) | ≈ 0 | ≈ 0 | (stable) |
| s₀=0 (baseline) | ≈ 0 | ≈ 0 | (stable) |

## Interpretation (honest)

### Trustworthy

- **Baseline and flank plaquettes: trivial holonomy (γ≈0).**  
  Within numerical noise, the residual soft subspace acquires **no geometric phase** around a small loop in (s,α) away from the gap-compression region.

### Not trustworthy as pure Berry curvature

- Bottleneck γ≈π coincides with **rank collapse** on two edges of the plaquette (one principal angle ≈π/2).  
  When σ_min→0, the Procrustes unitary on the full 4-plane is ill-conditioned; det can pick up a **sign discontinuity** that is not continuous Berry curvature of a fixed-rank bundle.

So the correct claim is:

> Away from the bottleneck, soft-subspace plaquette holonomy is consistent with **zero** curvature at this resolution.  
> At the bottleneck, the 4-plane is **not a smooth rank-4 bundle** along the α direction on this plaquette — geometry is dominated by subspace turnover, not a clean U(4) Berry phase.

This matches the Grassmann metric story: bottleneck is quiet in *s* for a fixed α, but opening α can exchange one soft direction (high metric / rank drop).

## Next refinements (Colab)

1. **Reduced-rank holonomy** — restrict to the 3 directions with σ>0.5 on every edge; compute arg det on that subbundle.  
2. **Smaller plaquette** — δs=δα=0.02 centered at s₀=0.47.  
3. **Denser L=12 s-path** — validation of Tr(PQ) continuity.  

## Data

`data/G12_berry_plaquette.json`

## Related

- `G12_grassmann_geodesic_metric.md`
- `G12_PT_Heff_Beff.md`
