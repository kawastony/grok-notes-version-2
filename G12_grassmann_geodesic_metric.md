# Grassmann geodesic path length and quantum metric

**Date:** 2026-09-26  
**Setup:** L=10, d=3, residual-gated k=4 soft subspace, boost path s∈{0,0.25,0.40,0.45,0.50,0.55,0.60,0.75,1.0}

## Definitions

Soft modes span a point P(s)∈Gr(k,N). Between two projectors:

| Quantity | Definition |
|----------|------------|
| Principal angles θ_i | cos θ_i = σ_i(V†W) from SVD |
| Tr(PQ) | Σ cos²θ_i |
| Frobenius | \|P−Q\|_F² = 2k − 2 Tr(PQ) |
| **Geodesic distance** | d_geo = √(Σ_i θ_i²) |
| **Quantum metric proxy** | g_ss ≈ (d_geo / Δs)² |

Path length = sum of segment geodesics (not the single chord from endpoint to endpoint).

## Segment results

| step | θ (rad) | d_geo | TrPQ | g_ss ≈ (d_geo/Δs)² |
|------|---------|-------|------|---------------------|
| 0.00→0.25 | 0.25, 0.28, 0.36, **1.57** | 1.65 | 2.74 | 44 |
| 0.25→0.40 | 0.22, 0.26, 0.26, **1.50** | 1.56 | 2.82 | 108 |
| 0.40→0.45 | 0.05, 0.11, 0.13, **1.55** | 1.56 | 2.97 | **976** |
| **0.45→0.50** | **0.06, 0.12, 0.15, 0.20** | **0.28** | **3.92** | **32** |
| 0.50→0.55 | 0.07, 0.11, 0.17, **1.57** | 1.58 | 2.96 | **1001** |
| 0.55→0.60 | 0.09, 0.13, 0.17, **1.46** | 1.48 | 2.96 | 872 |
| 0.60→0.75 | 0.47, 0.80, 1.29, 1.55 | 2.22 | 1.36 | 220 |
| 0.75→1.00 | 0.46, 0.85, 0.96, 1.48 | 2.01 | 1.57 | 65 |

## Path totals

```
Path geodesic length     L_path  = 12.35
Endpoint direct geodesic L_chord =  2.67
Ratio L_path / L_chord           =  4.62
```

The soft subspace path is **far from a single Grassmann geodesic**: it wanders; the chord underestimates motion by ~4.6×.

## Quantum metric reading

- **Minimum g_ss** on the path sits at the **bottleneck** 0.45→0.50 (g_ss≈32), where all principal angles are small and TrPQ≈3.92.
- **Peaks of g_ss** (~1000) sit on **either side** of the bottleneck (0.40→0.45 and 0.50→0.55), where **one** principal angle remains ≈π/2 (one direction flips / leaves the frame) even when the other three angles are small.
- Late path (0.60→1.00): large d_geo, moderate g_ss — sustained subspace drift (matches earlier singular-value collapse).

So the quantum metric density is **not** peaked at the gap minimum itself; the gap minimum is where the plane **stops turning**. The high metric segments are where one soft direction is exchanged.

## Relation to prior diagnostics

| Prior | Grassmann refinement |
|-------|----------------------|
| TrPQ≈3.92 at bottleneck | All θ_i small; d_geo=0.28 |
| TrPQ≈3 with one σ≈0 | Three small θ, one θ≈π/2; d_geo still large |
| B_off peak at bottleneck | Mixing *inside* a nearly fixed plane |
| Late TrPQ collapse | Large integrated geodesic length |

**B_off peak + small d_geo** at 0.45–0.50 means: strong intra-subspace hybridization with little Grassmann motion — the plane is stable while internal levels rearrange.

## Locked claims

1. Soft-subspace path length on Gr(k,N) is L_path≈12.35 vs chord≈2.67 (ratio≈4.6).
2. Bottleneck is a **metric quiet** region (minimal g_ss, minimal d_geo), not a singularity of Grassmann motion.
3. High quantum metric flanks the bottleneck where a single principal angle opens to π/2.
4. Geodesic length is the right additive measure of subspace change; TrPQ alone can look “high” while one direction is already lost.

## Data

`data/G12_grassmann_metric.json`

## Related

- `G12_PT_Heff_Beff.md`
- `G12_4mode_subspace_track.md`
- `G12_PT_flow_and_d5.md`
