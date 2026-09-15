# Pair scaling through L = 8

Tony Kawas / 15 September 2026.

---

## Results

| L | sep | softest \|λ\| | P per core (softest) | IPR | Owner |
|---|-----|--------------|----------------------|-----|-------|
| 5 (single) | — | ∼0.01–0.05 | ∼0.05–0.16 | ∼0.003 | — |
| 6 pair | ∼2–3 | 0.001 | ∼0.05–0.15 | ∼0.002 | shared |
| 7 pair | ∼4 | 0.008 | ∼0.25 | ∼0.018 | shared |
| **8 pair** | **5** | **0.0008** | **∼0.10** | **∼0.004** | **shared** |

L = 8 assembly + eigsh completed in a few seconds after switching to an explicit sparse Hermitian H.

---

## Observations

1. **Spectrum continues to soften** — softest |λ| drops to ∼8×10⁻⁴ at L = 8.  
2. **Hybridization persists** — every low mode has equal weight on both cores (bonding/antibonding).  
3. **Core weight** — non-monotonic in this window (peaks at L = 7 with the chosen ball radius); absolute localization still limited by residual overlap.  
4. **Molecular regime confirmed** through L = 8 with sep = 5.

---

## Interpretation

The data remain consistent with two underlying defect modes that hybridize at finite separation. Full decoupling requires sep ≫ core radius (likely L ≳ 12–16 with sep ≳ 6–8 for the present profile width w ∼ 1.2).

---

## Technical note

Explicit sparse construction of H = ½(γ⁵D + h.c.) + ARPACK shift-invert is fast enough for N = 4096 (L = 8). Larger volumes are now practical.

---

## Compact statement

Through L = 8 the hedgehog–anti-hedgehog pair produces an increasingly soft spectrum with modes that remain equally shared between the two cores. The system is still in the molecular (hybridized) regime. The Callias embedding continues to respond correctly; independent core localization is a matter of further scale separation.
