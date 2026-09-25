# Subspace G12 and d=5 boost scan

**Date:** 2026-09-25  
**Status:** Executed. Continuation of quasi-spectral-flow work.

## Motivation

Softest-mode `dP` is unstable under multiplet reordering (especially near s≈0.5). Track:

1. **Softest-mode G12** — previous diagnostic
2. **Subspace-averaged density** — mean density over all residual-accepted modes → (S1, S2, dS)
3. **Sum of per-mode dP** — Σ dP over accepted modes

Repeat continuous boost at **d=3** and **d=5** (L=10, ε=0.05, s∈{0,0.25,0.5,0.75,1}).

## Endpoint results

| Geometry | G_softest | G_subspace_avg | G_sum_dP |
|----------|-----------|----------------|----------|
| **d=3** | **−0.09045** | **−0.1764** | **−0.7057** |
| **d=5** | **+0.07722** | **+0.0938** | **+0.3751** |

All residual-accepted (n_acc=4 at every s). Baseline dS ≈ 0 at both separations.

## Path structure

### d=3 (tight molecular)

| s | min \|λ\| | softest dP | subspace dS |
|---|----------|------------|-------------|
| 0.00 | 0.00147 | ~0 | ~0 |
| 0.25 | 0.00151 | −0.00089 | −0.00321 |
| 0.50 | **0.00026** | +0.00473 | −0.00219 |
| 0.75 | 0.00070 | −0.00819 | −0.00621 |
| 1.00 | 0.00087 | −0.00452 | −0.00882 |

- Soft window **compresses** at s=0.5
- Softest dP **sign-flips** through the bottleneck; subspace dS stays **negative** and grows in magnitude toward the endpoint
- Subspace observable is **more stable** than softest-only dP

### d=5 (looser pair)

| s | min \|λ\| | softest dP | subspace dS |
|---|----------|------------|-------------|
| 0.00 | 0.00041 | ~0 | ~0 |
| 0.25 | 0.00141 | −0.00017 | +0.00131 |
| 0.50 | 0.00011 | +0.00238 | +0.00449 |
| 0.75 | 0.00068 | +0.00594 | +0.01046 |
| 1.00 | 0.00025 | +0.00386 | +0.00469 |

- Endpoint G_softest matches earlier single-shot d=5 boost (+0.077)
- **Sign of G is opposite to d=3** (geometry-dependent direction of weight flow for softest mode and subspace)
- Soft window also compresses (very small min \|λ\| at s=0.5)

## Interpretation

1. **Subspace averaging helps.** At d=3, softest dP is non-monotonic with a sign flip; subspace dS is smoother and monotonic in sign toward the endpoint. Prefer subspace (or sum) diagnostics when claiming pathwise influence.

2. **Geometry dependence is real.** d=3 and d=5 both show pathwise reorganization and nonzero endpoint G, but **opposite overall sign**. Influence exists in both molecular windows; the *direction* of soft-weight flow depends on separation / multiplet structure — not a universal “always toward boosted core” for the softest label alone.

3. **Still not integer spectral flow.** No zero crossing counted; open path only.

## Locked claims (updated)

- Continuous one-core boost → structured soft multiplet rearrangement (d=3 and d=5).
- Endpoint G_softest consistent with prior static tests at both separations.
- Subspace-averaged dS is a stabler path observable than softest-only dP under reordering.
- Sign of G depends on geometry (d=3 vs d=5).

## Not claimed

- Integer SF index
- Continuum effective 2-level Hamiltonian fit (next optional step)
- L=12 path scan (resource-heavy; optional)

## Data

Full tables: local `artifacts/G12_subspace_and_d5_scan.json`

## Related

- `G12_spectral_flow_scan.md`
- `G12_spectral_flow_link.md`
- `L10_static_response_test.md`
