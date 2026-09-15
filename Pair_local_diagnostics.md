# Hedgehog–anti-hedgehog pair — local diagnostics

Tony Kawas / 15 September 2026.

---

## Setup

- 8-component Wilson + Callias mass texture β ⊗ (v f τ · n̂).  
- Periodic lattice with one hedgehog (+1) and one anti-hedgehog (−1).  
- L = 6 (sep ∼ 2–3) and L = 7 (sep ∼ 4).  
- Diagnostics: lowest eigenvalues, local density in balls around each core (D1), IPR (D4), mode-to-core assignment.

---

## Results

### L = 6 (cores nearly adjacent)

| Mode | \|λ\| | P(+core) | P(−core) |
|------|-------|----------|----------|
| 0 | 0.0012 | 0.048 | 0.048 |
| 1 | 0.0042 | 0.094 | 0.094 |
| 2 | 0.0079 | 0.147 | 0.147 |

Extremely soft spectrum. Weight shared equally (hybridization of overlapping cores).

### L = 7 (sep ∼ 4)

| Mode | \|λ\| | P(+core) | P(−core) | IPR |
|------|-------|----------|----------|-----|
| 0 | 0.0079 | 0.246 | 0.246 | 0.018 |
| 1 | 0.0122 | 0.252 | 0.252 | 0.020 |
| 2 | 0.0143 | 0.087 | 0.087 | 0.002 |

Soft modes persist. Core weight rises to ∼25 % for the softest pair (better than L = 5 single-defect ∼5–16 %). IPR of the lowest two modes is higher, consistent with increased localization. Weight remains equal on both cores → bonding/antibonding combinations of two underlying defect modes.

---

## Interpretation

1. **Spectral response** — near-zero eigenvalues continue to appear and are even softer with a pair, consistent with two topological defects.

2. **Equal core weight** — on these volumes the two cores still communicate. The low modes are hybridized (even/odd combinations) rather than independently localised on one core. This is the expected intermediate regime when separation is only a few lattice spacings.

3. **Trend with volume** — core weight and IPR improve from L = 5 → 7. The system is moving in the right direction; full resolution of opposite local signatures requires larger separation (larger L).

4. **What would clinch it** — on a lattice with core separation ≫ core radius, one expects two near-zero modes (or multiplets) with P concentrated on opposite cores and opposite local asymmetry, global sum ∼ 0.

---

## Status

| Item | Status |
|------|--------|
| 8-component Callias embedding | Confirmed (algebra + soft spectrum) |
| Pair geometry | Implemented |
| Near-zero modes | Present, soft |
| Independent core localization | Not yet (hybridization on L ≤ 7) |
| Next | Larger L (sep ≫ w) or accept bonding/antibonding as evidence of two underlying core modes |

---

## Compact statement

A periodic hedgehog–anti-hedgehog pair on L = 6–7 produces a soft near-zero spectrum and higher core weight than the single-defect runs. Modes remain equally shared between the two cores (hybridization). The topological embedding continues to respond correctly; clean, independently localised opposite-core signatures require greater scale separation.
