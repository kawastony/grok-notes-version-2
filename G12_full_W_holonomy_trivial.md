# Full U(k) plaquette holonomy W ≈ I

**Date:** 2026-09-26  
**Status:** Rank-safe plaquettes; full matrix inspected.

## Results

| s₀ | δs=δα | max \|φ_i\| (rad) | \|W−I\| | Tr(W) | rank_safe |
|----|-------|------------------|--------|-------|-----------|
| 0.45 | 0.02 | 4.0e−4 | 5.7e−4 | ≈4 | True |
| 0.47 | 0.02 | 5.3e−4 | 7.7e−4 | ≈4 | True |
| 0.30 | 0.05 | 6.1e−4 | 8.6e−4 | ≈4 | True |
| 0.00 | 0.05 | 9.1e−4 | 1.3e−3 | ≈4 | True |

arg det W ∼ 10⁻¹² (numerical zero).

## Claim

Full soft-multiplet holonomy on these deformation plaquettes is **trivial**:

```
W ≈ I ∈ U(k)
```

No hidden SU(k) twist. Deformation-space Berry / Wilczek–Zee curvature is consistent with **flat** at this resolution.

Abelian density f_{sα} = argdet(W)/A is consistent with zero (do not amplify \|W−I\|/A as a signal).

## Implications

- U(k) structure of the soft frame remains (PT, B_eff, metric).
- Antisymmetric geometric phase in (s, α=core-2 boost) is not required by data.
- Propagation (dS, G) and Grassmann metric stand without deformation-space curvature.

## Related

- G12_berry_plaquette.md
- G12_L12_dense_and_Berry_ranksafe.md
- G12_grassmann_geodesic_metric.md
