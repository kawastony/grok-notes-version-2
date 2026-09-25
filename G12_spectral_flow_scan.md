# G12 quasi-spectral-flow scan

**Date:** 2026-09-25  
**Status:** Executed (sandbox). Residual-gated soft sector.

## Setup

- L=10, d=3 molecular pair, k=4 soft modes
- 8-component Wilson–Dirac + hedgehog mass texture
- Cores: c1=(5,5,4), c2=(5,5,7)
- Baseline: v1=v2=2.0; boost path: v1 = v0·(1 + s·ε), ε=0.05, s ∈ {0, 0.25, 0.5, 0.75, 1.0}
- Residual gate: rel ≤ 1e−6; core radius = 2

## Results (softest residual-accepted mode)

| s | v1 | |λ| softest | dP = P2−P1 |
|---|-----|------------|-------------|
| 0.00 | 2.000 | 0.001471 | ~0 (noise) |
| 0.25 | 2.025 | 0.001508 | −0.000886 |
| 0.50 | 2.050 | 0.000262 | +0.004731 |
| 0.75 | 2.075 | 0.000700 | −0.008192 |
| 1.00 | 2.100 | 0.000865 | −0.004523 |

**Endpoint G12** (baseline → s=1):

```
G12_end = (dP(s=1) − dP(s=0)) / ε ≈ −0.09045
```

Matches the earlier single-shot +5% boost measurement.

**Segment G12** (local finite differences along path):

```
[−0.071, +0.449, −1.034, +0.294]
```

Non-monotonic: multiplet reordering / avoided-crossing structure, not a single smooth adiabatic level.

## Spectral behaviour

- Soft multiplet **rearranges** under continuous boost (ordering of |λ| changes; at s=0.5 the soft window compresses strongly).
- **No zero crossing** forced in this open path (all |λ| remain > 0).
- Soft weight **does** reorganize: endpoint dP ≠ 0 with same sign structure as static G12.

## Interpretation vs true spectral flow

| Claim | Status |
|-------|--------|
| Soft spectrum depends on core coupling | **Shown** |
| Soft weight responds along continuous path | **Shown** |
| Endpoint G12 consistent with static test | **Shown** (−0.09045) |
| Integer spectral-flow index | **Not measured** (open path; torus SF obstructed historically) |
| G12 = SF | **False** — G12 is linear weight response; SF counts crossings |

**Safe statement:**

> The residual-gated molecular soft sector is parametrically tied to defect strength. Continuous one-core boost produces a quasi-spectral-flow diagram in which eigenvalues move and soft weight slides. Endpoint susceptibility matches the static G12 test. This is the kinematic prerequisite for spectral flow, not a measured SF integer.

## Data file

See `data/G12_spectral_flow_scan.json` for full mode tables (all accepted modes at each s).

## Related notes

- `L10_static_response_test.md` — original G12
- `Propagation_law_annotated_levels.md` — Level I continuity
- `Quantum_foundations_contact.md` — SF ↔ G12 foundations link
- `Framework_laws_derived_vs_guiding.md` — law taxonomy
