# L=12 residual-gated boost path (d=3)

**Date:** 2026-09-26  
**Status:** Executed on Colab. Residual-gated success.

## Setup

- L=12, d=3, cores (6,6,5)/(6,6,8), N=13824
- v1=v0(1+sε), ε=0.05, s∈{0,0.25,0.5,0.75,1}
- eigsh shift-invert, residual gate (rels reported as 0 within print precision)
- subspace dS, Procrustes Tr(PQ)

## Soft spectrum

| s | \|λ\| (soft multiplet) | dS |
|---|----------------------|-----|
| 0.00 | 0.00012, 0.00049, 0.00384, 0.00433 | ~0 |
| 0.25 | 0.00010, 0.00021, 0.00112, 0.00141 | −4.9e−5 |
| 0.50 | 0.00202, 0.00262, 0.00323, 0.00359 | −3.1e−4 |
| 0.75 | 0.00047, 0.00148, 0.00205, 0.00280 | −1.9e−3 |
| 1.00 | 0.00048, 0.00069, 0.00079, 0.00162 | −2.2e−3 |

Soft window is in the **10⁻⁴–10⁻³** range (not mid-spectrum). Residuals acceptable.

## Endpoint G

```
G_subspace = (dS(1) − dS(0)) / ε ≈ −0.0448
```

| Quantity | L=10 d=3 | L=12 d=3 |
|----------|----------|----------|
| G_subspace | **−0.176** | **−0.045** |
| sign | negative | **negative (same)** |
| \|G\| | larger | smaller |

**Sign of propagation response survives volume increase.** Magnitude is reduced (finite-size / multiplet structure dependence).

## Projector continuity Tr(PQ)

| step | TrPQ | max S |
|------|------|-------|
| 0.00→0.25 | 0.50 | 0.57 |
| 0.25→0.50 | 0.52 | 0.60 |
| 0.50→0.75 | 1.24 | 0.87 |
| 0.75→1.00 | 0.28 | 0.38 |

Weaker than L=10 bottleneck (TrPQ≈3.92). At L=12 with this path sampling, the soft subspace **turns over** between steps more strongly — continuous path still shows monotonic dS trend, but individual projector frames are less stable.

## Locked claims

1. L=12 residual-gated soft multiplet **resolved** (Colab).
2. Subspace dS remains **negative** along the boost path; endpoint G **same sign** as L=10 d=3.
3. \|G\| is **volume-dependent** (smaller at L=12 in this setup).
4. Tr(PQ) continuity is **weaker** than L=10 — do not claim full-rank bottleneck continuity at L=12 without finer s-grid / larger k.

## Data

User Colab: `L12_d3_path.json`

## Related

- `G12_subspace_and_d5_scan.md` (L=10 baseline)
- `G12_L12_volume_check.md` (prior failed sandbox attempt)
