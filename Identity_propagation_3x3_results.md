# Real-operator 3×3 identity-propagation results

Tony Kawas / 19 September 2026.

**Operator:** 8-component Wilson–Dirac + isospin hedgehog, L=10, d=3.  
**Grid:** \(v_1,v_2\in\{1.7,2.0,2.3\}\).  
**Gate:** all 9 points passed with \(r_{\rm rel}\sim 10^{-14}\).

---

## Master table

| v1 | v2 | R_mid | H_mid (c) | A | P (signed) | ΔW_mid | F_mid | class |
|----|-----|-------|-----------|---|------------|--------|-------|-------|
| 1.7 | 1.7 | 1.21 | −0.008 | 1.61 | −0.05 | +0.053 | −8.80 | B |
| 1.7 | 2.0 | **0.90** | **+0.004** | 1.86 | **+0.29** | **−0.001** | −8.72 | **P** |
| 1.7 | 2.3 | 1.59 | −0.017 | 1.55 | −0.16 | +0.061 | −9.08 | T |
| 2.0 | 1.7 | 1.01 | −0.000 | 1.45 | **+0.36** | +0.050 | −8.81 | P |
| 2.0 | 2.0 | 1.30 | −0.007 | 1.56 | −0.18 | **+0.113** | −9.28 | T |
| 2.0 | 2.3 | 1.26 | −0.012 | 1.51 | −0.17 | +0.029 | −8.71 | T |
| 2.3 | 1.7 | 1.30 | −0.012 | 1.35 | +0.07 | +0.027 | −8.71 | B |
| 2.3 | 2.0 | 1.21 | −0.010 | 1.47 | +0.03 | +0.048 | −8.71 | B |
| 2.3 | 2.3 | 1.06 | −0.003 | 1.34 | +0.11 | +0.029 | −8.70 | T |

Class rule (first pass): B if \(R_{\rm mid}>1.15\) and \(|P|<0.15\); P if \(|P|>0.20\) or \(H_{\rm mid}>0\); else T.

---

## Propagation tests

### Spearman rank (n=9)

| predictor | ρ vs ΔW_mid | p |
|-----------|-------------|---|
| R_mid | **+0.48** | 0.19 |
| H_mid | −0.17 | 0.67 |
| \(|P|\) | −0.02 | 0.97 |
| A | +0.20 | 0.61 |

Direction of R_mid is right; not statistically significant at n=9.

### Class → mean ΔW_mid

| class | n | mean ΔW_mid | mean R_mid |
|-------|---|-------------|------------|
| B | 3 | +0.043 | 1.24 |
| T | 4 | +0.058 | 1.30 |
| P | 2 | **+0.024** | **0.96** |

Polarized class has weaker bridge gain and lower R_mid. Transitional includes the baseline (strongest ΔW), so class thresholds need refinement (baseline |P|=0.18 sits on the B/T boundary).

### Constitutive fit

\[
\Delta W_{\rm mid} = c_0 + c_1 R_{\rm mid} + c_2 H_{\rm mid} + c_3 |P|
\]

| coef | value |
|------|-------|
| c0 | −0.20 |
| c1 (R_mid) | **+0.25** |
| c2 (H_mid) | +6.0 |
| c3 (|P|) | −0.05 |
| MAE | 0.019 |
| LOO-MAE | **0.041** |

c1 positive as expected. LOO error is ~2× in-sample — honest for n=9; do not overclaim fit quality.

---

## Decision against protocol criteria

| Criterion | Result |
|-----------|--------|
| Residual gating | **Pass** (9/9 at ~1e−14) |
| R_mid varies nontrivially | **Yes** (0.90–1.59) |
| ΔW_mid varies nontrivially | **Yes** (−0.001–+0.113) |
| Higher R_mid tracks larger ΔW | **Weakly** (ρ=+0.48) |
| Identity classes cleanly separate response | **Partial** (P weaker; B/T mixed) |
| Signed P adds value | **Mixed** (extreme P points weak ΔW; mild P in baseline still strong ΔW) |
| LOO reasonable | **Marginal** (0.04 on ΔW scale ~0.05) |

**Minimum success: yes. Strong success: not yet.**

---

## Safe claim

> On a residual-validated 3×3 grid of the full 8-component Callias/Wilson–Dirac operator, microscopic midpoint richness varies together with mesoscopic bridge-feeding under early Forman flow (Spearman ρ≈+0.5). Polarized/hollowed states show weaker bridge gain. Class separation is partial; leave-one-out error remains appreciable at n=9. This is identity→response coherence within the model — not a galactic or Einstein result.

---

## What not to claim

- Derivation of a_T / z_act
- Chirality unifies all scales
- Graph flow is gravity
- Strong statistical confirmation (n=9)

---

## Compact statement

Real-operator 3×3 completed. All points residual-clean. R_mid tracks ΔW_mid directionally; polarized class is weaker. Minimum success for identity propagation; refine class thresholds and expand grid before strong claims.
