# Phase B: secondary geometry m₀ check

Tony Kawas / 16 September 2026.

---

## Setup

- L = 10, sep = 6
- Secondary geometry: **w = 0.8, v = 2.0** (narrower core from Phase 2 ranking)
- m₀ = 0.30 and 0.50

Purpose: confirm that Phase A’s null trend (no F improvement with rising sep/ξ) is not unique to w=1, v=3.

---

## Results

| m₀ | sep/ξ | \|λ₁\| | Δλ | F₂ (R=2) | F₄ (R=2) | F₂ (R=2.5) | F₄ (R=2.5) | IPR |
|----|-------|-------|-----|----------|----------|------------|------------|-----|
| 0.30 | 1.80 | 0.00039 | 0.00016 | 0.008 | 0.009 | 0.015 | 0.017 | 0.0010 |
| 0.50 | 3.00 | 0.00033 | 0.00049 | 0.000 | 0.015 | 0.000 | 0.036 | 0.0014 |

Soft sector present in both runs.

---

## Comparison with Phase A (same m₀)

| Geometry | m₀=0.30 F₂/F₄ (R=2.5) | m₀=0.50 F₂/F₄ (R=2.5) |
|----------|------------------------|------------------------|
| w=1.0, v=3.0 (Phase A) | 0.036 / 0.023 | 0.015 / 0.024 |
| w=0.8, v=2.0 (Phase B) | 0.015 / 0.017 | 0.000 / 0.036 |

No systematic rise with m₀ on either geometry. F remains O(0.01–0.04).

---

## Conclusion

Phase B confirms Phase A: increasing the nominal bulk gap does not produce cleaner core ownership at L=10 on a second (narrower-core) geometry. The null result is robust against this geometry change.

Combined with Phase 1–2 and Phase A, the ruled-out shortcuts are:

1. Width / amplitude tuning  
2. 2D / 4D soft-subspace rotation  
3. Raising bulk gap (m₀) at fixed L and sep  

The accessible window remains a structural molecular regime. Further progress requires larger absolute separation or a different effective description, not more small-box parameter scans.
