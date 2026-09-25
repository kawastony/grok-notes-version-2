# L=12 dense path + rank-safe Berry plaquettes

**Date:** 2026-09-26  
**Status:** Executed on Colab.

## 1. L=12 denser s-path (d=3)

s ∈ {0, 0.15, 0.30, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75, 1.0}

### Soft spectrum & dS

| s | min\|λ\| scale | dS |
|---|---------------|-----|
| 0.00 | ~1e−4 | ~0 |
| 0.15 | ~1e−3 | +1.3e−4 |
| 0.30–0.45 | ~5e−4–1e−3 | ~±1e−4 |
| 0.50 | ~2e−3 | −3.1e−4 |
| 0.60 | ~7e−4 | +1.6e−3 |
| 0.75 | ~5e−4 | −1.9e−3 |
| 1.00 | ~5e−4 | −2.2e−3 |

```
G_subspace = −0.0448   (same as coarse L=12 path)
path geodesic length ≈ 15.74
```

### Projector continuity (dense)

| step | TrPQ | d_geo |
|------|------|-------|
| 0.00→0.15 | 2.54 | 1.33 |
| 0.15→0.30 | 1.66 | 2.20 |
| 0.30→0.40 | 1.50 | 2.13 |
| **0.40→0.45** | **3.78** | **0.47** |
| 0.45→0.50 | 2.85 | 1.58 (one θ≈π/2) |
| 0.50→0.55 | 2.67 | 1.42 |
| 0.55→0.60 | 2.81 | 1.57 |
| 0.60→0.75 | 0.93 | 2.35 |
| 0.75→1.00 | 0.28 | 2.69 |

**Finding:** Denser sampling reveals a **local continuity window** at 0.40→0.45 (TrPQ=3.78, geo=0.47), analogous to L=10 bottleneck quiet region — but it is **narrower** and not sustained through 0.45→0.50 (one angle opens). Late-path turnover remains strong.

**G sign and magnitude unchanged** vs coarse L=12 → volume result is robust to s-sampling.

---

## 2. Rank-safe Berry plaquettes (L=10)

| Center | δs=δα | γ | rank_safe |
|--------|-------|---|-----------|
| s₀=0.45 | 0.02 | **0.00** | **True** |
| s₀=0.47 | 0.02 | **0.00** | **True** |
| s₀=0.30 | 0.05 | **0.00** | **True** |

(Earlier large plaquette at s₀=0.45 with δ=0.05 gave γ≈π but **rank-unsafe** edges — discarded.)

### Locked Berry claim

> Where the soft 4-plane remains rank-stable around a small loop in (s, α=core-2 boost), the Wilczek–Zee / U(k) holonomy is **consistent with zero** at this resolution.

Nonzero geometric phase is **not** required by current data. Metric response (g_ss, d_geo) and propagation (dS, G) stand without an antisymmetric curvature layer at the scales probed.

---

## Combined status of the soft-sector program

| Layer | Status |
|-------|--------|
| Topology / identity (shell, Q flat in s) | **Stable** |
| Soft multiplet residual-gated | **L=10 and L=12** |
| Propagation G_subspace sign | **Negative at L=10 and L=12** |
| Grassmann metric / path length | **Measured; bottleneck metric-quiet** |
| Berry holonomy (rank-safe) | **Trivial (γ≈0)** |
| L=12 continuity | **Local window only; late drift** |

## Data

User Colab: `L12_dense_path.json`; Berry rank-safe runs as logged.

## Related

- `G12_berry_plaquette.md` (first, rank-unsafe π)
- `G12_L12_residual_gated_path.md`
- `G12_grassmann_geodesic_metric.md`
