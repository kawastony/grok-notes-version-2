# Mediator test: relative Forman vs identity vs Ollivier

Tony Kawas / 19 September 2026.

Real 8-component operator, 8 residual-clean points (transition-densified).

---

## 1. Predictor ranking for ΔW

| Predictor | Spearman ρ vs ΔW | |Pearson| | Role |
|-----------|------------------|----------|------|
| **\(F^{\rm rel}_{\rm mid}\)** | **−0.976** | **0.91** | **Best mediator** |
| gain-sector fraction | +0.850 | 0.81 | Strong |
| \(R_{\rm mid}\) | +0.762 | 0.61 | Good but weaker |
| \(H_{\rm mid}\) | −0.571 | — | Moderate |
| \(|P|\) | +0.05 | ~0 | Weak alone |
| Ollivier mid (sample) | nan | — | **Non-discriminating** |

**\(F^{\rm rel}_{\rm mid}\) wins clearly** over identity variables alone.  
Gain-sector fraction is second. Identity shape still works; relative Forman is the tighter link to feeding.

---

## 2. Mechanism status (text recommendation 2)

> predict ΔW from R_mid alone / from P,H / from F^rel alone / from gain-sector alone

Result: **F^rel alone is the strongest single predictor** on this set.  
That supports the claim that relative curvature is the mediating variable between identity and response.

---

## 3. Ollivier–Ricci cross-check (recommendation 3)

Implementation: lazy random-walk measures (α=0.5), W₁ via linear program on hop-distance costs, mean over a sample of mid-tube edges.

**Outcome:** Ollivier mid mean ≈ **−0.005 constant** across all 8 points — no discrimination.

### Why (honest)
On this dense, nearly regular tube graph with unit hop metric, neighborhood measures are similar and W₁ ≈ graph distance for most mid edges, so κ ≈ 1 − W₁/d collapses to a near-constant.  
This is a **limitation of the discrete metric / implementation on this geometry**, not a refutation of Forman. A density-weighted continuous cost or full Ollivier on a coarsened graph might differ — not done here.

**Conclusion:** Ollivier did **not** corroborate the relative-curvature story under this practical setup. Forman remains the working discrete curvature for the program. Do not claim multi-Ricci agreement.

---

## 4. Text recommendation 1 (denser scan)

Already partially done: 8 points on the imbalance/transition axis.  
F^rel ranks feeding consistently (ρ≈−0.98). Gain-sector tracks slope/ΔW.  
Further densification remains useful but is not required to see the mediator pattern.

---

## 5. Breakthrough proximity (agreed, with caution)

| Criterion | Status |
|-----------|--------|
| Real operator + residual gate | Yes |
| Identity → response | Yes |
| Dynamic slope separation | Yes |
| Relative curvature as mediator | **Yes — strongest predictor** |
| F^rel generalizes beyond 4 archetypes | **Supported on 8 pts** |
| Ollivier cross-check | **Failed to discriminate** |
| Continuum Ricci / gravity | No |

**Safe statement:**

> On residual-validated soft modes of the 8-component Callias/Wilson–Dirac operator, relative mid-tube Forman curvature is the strongest single predictor of early bridge feeding among tested variables, outperforming R_mid and polarization alone. Gain-sector occupancy is a close second. A practical Ollivier–Ricci sample on the same graphs did not discriminate. This tightens the within-model mechanism (identity → relative curvature → feeding) without establishing continuum Ricci or galactic law.

---

## Compact

F^rel wins the mediator test. Ollivier (this implementation) does not help. Mechanism chain is stronger; still micro/meso only.
