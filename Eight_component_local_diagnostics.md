# 8-component hedgehog — first local diagnostics

Tony Kawas / 15 September 2026.

---

## Setup

- 8-component Wilson (verified free spectrum) + mass texture β ⊗ (v f(r) τ · n̂) with N_def = 1, v = 1.8, w = 1.4.  
- L = 5, open and periodic.  
- Diagnostics D1 (local density in ball R ≤ 1.5), D4 (IPR), core vs boundary weight.

---

## Results

### Open L = 5

| Mode | \|λ\| | P_ball (R≤1.5) | IPR |
|------|-------|----------------|-----|
| 0–2 | 0.0105 | 0.056 | ∼0.003 |
| 3–4 | 0.0127 | 0.047 | ∼0.003 |
| 5–7 | 0.0298 | 0.015 | ∼0.005 |

Near-zero eigenvalues appear (\( |\lambda| \sim 10^{-2} \)).  
Local density inside the core ball remains low (∼5 %); most weight sits on the outer/boundary region.

### Periodic L = 5

| Mode | \|λ\| | P_ball | IPR |
|------|-------|--------|-----|
| 0–1 | 0.056 | 0.160 | ∼0.003 |
| 2–4 | 0.066 | 0.038 | ∼0.003 |

Softest eigenvalues ∼0.05–0.06. Core weight still modest (∼16 % for the lowest pair).

---

## Interpretation

1. **Near-zero modes now exist** — a qualitative change from all 4-component runs (where the gap stayed O(1)–O(4)). The 8-component Callias embedding is producing a soft spectrum, as required for an index-carrying defect.

2. **Localization is still weak** — on L = 5 the core, asymptotic region and boundary are not separated. Modes hybridize with the boundary (open) or feel the global topological obstruction (periodic single hedgehog). IPR values are consistent with delocalised or boundary-spread states rather than tightly core-bound Jackiw–Rossi modes.

3. **Expected on this volume** — exact continuum zero modes require a hierarchy core radius ≪ box size and, on the torus, a compensating anti-hedgehog. Neither is present at L = 5.

---

## Status

| Item | Status |
|------|--------|
| 8-component algebra | Verified |
| Free spectrum | Healthy |
| Hedgehog mass inserted | Done |
| Near-zero eigenvalues | **Appear** |
| Core localization (D1) | Weak on L = 5 |
| Next | Larger L and/or hedgehog–anti-hedgehog pair; re-run D1–D4 |

---

## Compact statement

The 8-component Callias embedding produces near-zero eigenvalues that were absent in the 4-component theory. Local density and IPR on L = 5 show that these modes are not yet core-localised — consistent with insufficient volume and the absence of a compensating anti-defect on the torus. The structural fix is working; scale separation and a pair geometry are the remaining practical requirements.
