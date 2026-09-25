# Parallel-transported soft frame: H_eff and boost matrix B_eff

**Date:** 2026-09-25  
**Setup:** L=10, d=3, ε=0.05, residual-gated 4-mode soft subspace

## Construction

1. Soft eigenvectors V(s) at each s along the boost path v1=v0(1+sε).
2. **Parallel transport:** Procrustes alignment — SVD of V(s)†V(s+Δs) → unitary R; align next frame so connection is symmetric.
3. **H_eff(s) = V† H V** in the PT frame (nearly diagonal).
4. **Boost generator:** ∂H/∂v1 from core-1 hedgehog mass texture only;  
   ∂H/∂s = (v0 ε) ∂H/∂v1.
5. **B_eff(s) = V† (∂H/∂s) V** — matrix of the deformation inside the soft subspace.

## Parallel-transport SVD (subspace continuity)

Singular values of the overlap map V(s)†V(s+Δs):

| step | singular values | Tr(PQ) |
|------|-----------------|--------|
| 0.00→0.25 | 0.969, 0.962, 0.935, **0.003** | 2.74 |
| 0.25→0.40 | 0.975, 0.967, 0.965, 0.071 | 2.82 |
| 0.40→0.45 | 0.999, 0.994, 0.992, 0.019 | 2.97 |
| **0.45→0.50** | **0.998, 0.993, 0.989, 0.980** | **3.92** |
| 0.50→0.55 | 0.998, 0.994, 0.986, **0.003** | 2.96 |
| 0.55→0.60 | 0.996, 0.991, 0.985, 0.113 | 2.96 |
| **0.60→0.75** | **0.89, 0.70, 0.28, 0.02** | **1.36** |
| 0.75→1.00 | 0.90, 0.66, 0.57, 0.09 | 1.57 |

**Bottleneck:** all four singular values ≈1 → full-rank continuous subspace.  
**Late path:** two singular values collapse → soft sector partially **leaves** the original 4D window (mixing with harder modes / projector drift).

## H_eff and B_eff diagnostics

| s | dS | mean\|B_diag\| | \|B_off\| | \|H_off\| |
|---|-----|-----------------|----------|----------|
| 0.00 | ~0 | 0.0071 | 0.0014 | ~0 |
| 0.25 | −0.0032 | 0.0101 | 0.0056 | 2.4e−3 |
| 0.40 | −0.0008 | 0.0150 | 0.0207 | 5.8e−4 |
| **0.45** | −0.0027 | 0.0166 | **0.0343** | 1.2e−3 |
| **0.50** | −0.0022 | 0.0186 | **0.0360** | 1.4e−3 |
| 0.55 | −0.0009 | 0.0173 | 0.0335 | 1.9e−3 |
| 0.60 | −0.0033 | 0.0193 | 0.0137 | 2.7e−3 |
| 0.75 | −0.0062 | 0.0193 | 0.0191 | 2.3e−3 |
| 1.00 | −0.0088 | 0.0181 | 0.0243 | 2.2e−3 |

- **H_eff** stays nearly diagonal (eigenframe property; small off-diag from residual/PT numerics).
- **B_off peaks at the bottleneck** (s≈0.45–0.55): strongest **intra-subspace mixing** driven by the boost precisely where the gap is narrowest.
- **mean\|B_diag\|** grows from ~0.007 to ~0.018–0.019: diabatic forces on soft weights increase along the path.

## Effective-theory reading

```
P_soft(s)     continuous at bottleneck, drifts late
B_eff(s)      = soft matrix of ∂H/∂s
B_off large   ⇔ multiplet hybridization (not single-level flow)
B_diag        ⇔ Hellmann–Feynman forces on PT diabatic weights
dS(s)         = subspace observable of core imbalance (propagation diagnostic)
```

This is the correct few-level structure:

- Not a 2-level Landau–Zener gap with fixed V.
- A **4D soft subspace** with a **boost operator B_eff(s)** whose off-diagonal part peaks at the compression point and whose diagonal drives weight rearrangement.
- Late-path singular-value collapse means any H_eff truncated to the initial soft window is incomplete for s≳0.6 — the true soft space rotates toward other modes.

## Locked claims

1. Parallel transport confirms full-rank continuity of P_soft through s≈0.45–0.50.
2. Boost matrix B_eff has **maximum off-diagonal** exactly in that window → multiplet mixing is driven by the physical deformation, not by an artifact of ordering.
3. Preferred propagation observable remains **subspace dS**; B_eff supplies the effective force law inside P_soft.
4. For s≳0.6, effective models must allow **subspace drift** (not a fixed 4D truncation).

## Data

`data/G12_PT_Heff_Beff.json`

## Related

- `G12_4mode_subspace_track.md`
- `G12_avoided_crossing_fit.md`
- `G12_subspace_and_d5_scan.md`
