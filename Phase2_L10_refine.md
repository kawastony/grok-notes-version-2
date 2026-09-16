# Phase 2: L=10 refine with 2D and 4D localization search

Tony Kawas / 16 September 2026.

---

## Setup

- L = 10, sep ≈ 6
- Four candidates from Phase 1
- 2-mode optimal rotation + random SO(4) search in the soft 4D subspace
- Diagnostic R = 2.0 and R = 2.5

---

## Results

| w | v | \|λ₁\| | F₂ (R=2) | F₄ (R=2) | F₂ (R=2.5) | F₄ (R=2.5) |
|---|---|-------|----------|----------|------------|------------|
| 1.6 | 2.0 | 7×10⁻⁵ | 0.000 | 0.009 | 0.000 | 0.016 |
| 0.8 | 2.0 | 0.00039 | 0.009 | 0.010 | 0.019 | 0.018 |
| **1.0** | **3.0** | 0.00053 | **0.016** | **0.017** | **0.028** | **0.033** |
| 0.8 | 3.0 | 0.00080 | 0.001 | 0.004 | 0.007 | 0.012 |

Raw modes remain equally shared in every case.

Best post-mixing ownership difference is still **O(0.03)** (w=1.0, v=3.0, R=2.5, 4D search).

---

## Interpretation

1. Soft sector survives at L=10 for all four candidates.  
2. Neither 2D nor random 4D mixing recovers strong single-core ownership.  
3. Expanding the soft subspace from 2 to 4 modes does not unlock localization at this volume/separation.  
4. The hybridization is structural: the near-zero sector is not well approximated by “left-core mode + right-core mode” at L≤10.

---

## Conclusion of the low-cost campaign

| Stage | Result |
|-------|--------|
| Phase 1 (L=8, 10 runs) | Soft sector robust; max ΔP_rot ~0.03 |
| Phase 2 (L=10, 4 candidates + 4D) | Soft sector robust; max F ~0.03 |

**Width/amplitude tuning + multi-mode rotation does not resolve independent core localization within the accessible volume.** The remaining issue is geometric scale separation (larger L and/or larger sep), not a post-processing oversight.

---

## Compact statement

Phase 2 confirms Phase 1: at L≤10 the soft near-zero sector is robust, but 2D and 4D rotations of the soft subspace do not yield independently core-localized modes. The pair remains strongly hybridized. Decoupling requires larger absolute separation than this environment can currently provide.
