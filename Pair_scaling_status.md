# Pair scaling status and next geometric push

Tony Kawas / 15 September 2026.

---

## Current evidence chain

| Stage | Observation |
|-------|-------------|
| 4-component | No topological class, persistent O(1) gap |
| 8-component single defect | Soft modes appear |
| 8-component pair L=6–7 | Even softer modes, higher core weight, equal weight on both cores (bonding/antibonding) |

Interpretation: **molecular regime** — each core hosts a would-be soft mode; finite separation hybridizes them into even/odd combinations. This is the expected intermediate before isolated-defect resolution.

---

## Quantitative trend (pair)

| L | sep | softest \|λ\| | P per core (softest) | IPR (softest) |
|---|-----|--------------|----------------------|---------------|
| 6 | ∼2–3 | 0.001 | ∼0.05–0.15 | ∼0.002 |
| 7 | ∼4 | 0.008 | ∼0.25 | ∼0.018 |

Core weight and IPR rise with L/separation. Modes remain shared (hybridized).

---

## L = 8 attempt

Sparse build + shift-invert for N = 8×8³ = 4096 was started. Matrix construction in pure Python over all sites is the bottleneck and exceeded the interactive timeout. The geometry (sep = 5) is in place in the code; a production run needs either a compiled/kernel-accelerated assembly or a longer batch job.

---

## What the data already support

- Algebraic Callias embedding: confirmed.  
- Spectral response to the defect: confirmed.  
- Pair soft sector with hybridization pattern: confirmed.  
- Fully decoupled, opposite local charges: **not yet** (requires sep ≫ core radius).

---

## Recommended next technical moves

1. **Accelerate matrix assembly** (Numba / Cython / precomputed neighbour lists) so L = 8–12 becomes routine.  
2. **Run the existing pair code at L = 8–10** with sep ≥ 5–6 and record:  
   - mode splitting Δλ,  
   - per-core weights,  
   - IPR,  
   - any emergence of preferred-core assignment.  
3. **Expected trend if the interpretation is correct**  
   - Δλ decreases with sep,  
   - per-core localization increases,  
   - modes become more independently centered,  
   - opposite local asymmetry begins to appear.

---

## Compact statement

The project is in the molecular regime of a topologically correct defect pair: soft hybridized modes, improving core weight with volume, no clean single-core split yet. That is consistent and positive. The remaining task is geometric scaling (larger L and separation), limited at present by pure-Python matrix assembly cost rather than by theory.
