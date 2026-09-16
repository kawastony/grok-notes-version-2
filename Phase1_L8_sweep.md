# Phase 1: L=8 coarse sweep with 2-mode rotation

Tony Kawas / 16 September 2026.

---

## Setup

- L = 8, sep ≈ 5, R = 2.0 diagnostic ball
- 8-component Wilson + Callias pair
- w ∈ {0.8, 1.0, 1.2, 1.4, 1.6}, v ∈ {2.0, 3.0} → 10 runs
- Post-processing: optimal rotation of the two softest modes to maximize core-ownership difference

---

## Results summary

| Rank | w | v | \|λ₁\| | Δλ | ΔP_rot (sum) | F | S | Note |
|------|---|---|-------|-----|--------------|---|---|------|
| 1 | 1.6 | 2.0 | 0.00082 | 0.00064 | 0.019 | 0.019 | 0.288 | weak ownership gain |
| 2 | 0.8 | 2.0 | 0.00111 | 0.00419 | 0.026 | 0.026 | 0.247 | largest ΔP_rot |
| 3 | 1.2 | 2.0 | 0.00018 | 0.00123 | 0.000 | 0.000 | 0.210 | fully shared |
| 4 | 1.0 | 2.0 | 0.00043 | 0.00207 | 0.005 | 0.005 | 0.195 | |
| 5 | 1.4 | 2.0 | 0.00080 | 0.00080 | 0.000 | 0.000 | 0.190 | |
| 6 | 0.8 | 3.0 | 0.00040 | 0.00016 | 0.014 | 0.014 | 0.143 | soft, weak split |
| 7 | 1.2 | 3.0 | 0.00001 | 0.00043 | 0.000 | 0.000 | 0.134 | |
| 8 | 1.0 | 3.0 | 0.00028 | 0.00058 | 0.030 | 0.030 | 0.133 | best F among soft |
| 9 | 1.4 | 3.0 | 0.00119 | 0.00057 | 0.002 | 0.002 | 0.103 | |
| 10 | 1.6 | 3.0 | 0.00007 | 0.00023 | 0.002 | 0.002 | 0.086 | |

Raw eigenmodes: **shared in every run** (P_A = P_B to numerical precision).

After optimal 2-mode rotation: maximum ownership difference ΔP_rot remains **O(0.01–0.03)** — not enough to claim independent core localization. Best F is 0.030 (w=1.0, v=3.0).

---

## Interpretation

1. Soft near-zero sector is robust across the (w, v) window.  
2. 2-mode rotation does **not** recover strong single-core ownership at L=8, sep=5.  
3. The soft subspace is hybridized more thoroughly than a simple bonding/antibonding pair of tightly localized core modes; residual overlap dominates.  
4. Lower v (=2) tends to give higher score (more core weight in the diagnostic ball); higher v softens eigenvalues further but does not unlock ownership.

---

## Best 4 candidates for Phase 2 (L=10)

By score and/or rotation F:

1. w=1.6, v=2.0  
2. w=0.8, v=2.0  
3. w=1.0, v=3.0   (best F)  
4. w=0.8, v=3.0   (very soft, modest ΔP_rot)

---

## Compact statement

Phase 1 (10 runs at L=8) finds a robust soft sector but no strong post-rotation core ownership. Maximum ΔP after optimal 2-mode mixing is ~0.03. The molecular regime is not resolved by width/amplitude tuning alone at this volume and separation. Proceed to Phase 2 (L=10) with the top candidates, or accept that L≤10 is insufficient for decoupling.
