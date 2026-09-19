# Sharpened classes, transition densification, early slope

Tony Kawas / 19 September 2026.

Real 8-component Wilson–Dirac + hedgehog, L=10. Residual ~1e−14 throughout.

---

## 1. Sharpened class thresholds

| Class | Rule |
|-------|------|
| **P** (polarized/stalled) | \(|P|>0.22\) **or** (\(H_{\rm mid}>0\) and \(R_{\rm mid}<1.05\)) |
| **B** (balanced/feeder) | \(R_{\rm mid}\ge 1.15\) and \(|P|\le 0.20\) and \(H_{\rm mid}\le 0\) |
| **T** (transitional) | otherwise |

**Baseline (2.0,2.0) is now class B** (was T under old thresholds).

---

## 2. Densified transition scan (8 points)

Focus: imbalance axis \(v_1\) at \(v_2=2\), plus cross arms.

| v1 | v2 | R_mid | H_mid | P | ΔW_8 | **slope** | class |
|----|-----|-------|-------|---|------|-----------|-------|
| 2.00 | 2.00 | 1.30 | −0.007 | −0.18 | +0.088 | **+0.0110** | **B** |
| 2.15 | 2.00 | 1.54 | −0.017 | +0.09 | +0.046 | +0.0058 | B |
| 2.30 | 2.00 | 1.21 | −0.010 | +0.03 | +0.034 | +0.0043 | B |
| 2.00 | 2.30 | 1.26 | −0.012 | −0.17 | +0.020 | +0.0026 | B |
| 1.85 | 2.00 | 1.09 | −0.003 | +0.17 | +0.033 | +0.0041 | T |
| 2.00 | 1.70 | 1.01 | −0.000 | **+0.36** | +0.036 | +0.0045 | **P** |
| 1.55 | 2.00 | 0.99 | +0.000 | +0.04 | +0.004 | **+0.0005** | **P** |
| 1.70 | 2.00 | **0.90** | **+0.004** | **+0.29** | **+0.001** | **+0.0002** | **P** |

---

## 3. Class → response (sharpened)

| class | n | mean ΔW | mean **slope** |
|-------|---|---------|----------------|
| **B** | 4 | +0.047 | **+0.0059** |
| T | 1 | +0.033 | +0.0041 |
| **P** | 3 | +0.014 | **+0.0017** |

Clean ordering: B > T > P in both ΔW and slope.

---

## 4. Rank correlations (this densified set)

| pair | Spearman ρ |
|------|------------|
| R_mid vs slope | **+0.76** |
| R_mid vs ΔW | (same direction) |

Stronger than the original 3×3 ρ≈+0.48 — densification near the transition clarifies the trend.

---

## 5. Transition picture along v1 (v2=2)

As \(v_1\) drops from 2.3 → 1.55:
- R_mid falls
- polarization / hollowing appears near 1.7
- **slope collapses from ~0.006 to ~0**

The stalled regime is localized near the hollowed/polarized corner, not a gradual global fade.

---

## 6. Simultaneous deliverable summary

| Task | Status |
|------|--------|
| 1. Sharpen class thresholds | **Done** — baseline is B |
| 2. Denser scan near transition | **Done** — 8 residual-clean points |
| 3. Report early slope with ΔW | **Done** — slope is primary dynamical observable |

---

## Safe claim (updated)

> On the residual-validated 8-component operator, sharpened identity classes order cleanly by early Forman-flow slope: balanced feeders (B) reinforce the bridge fastest, transitional states intermediate, polarized/hollowed states nearly stall. Along the imbalance axis the feeding rate collapses near the hollowed corner. Identity controls both initial bridge condition and early-time trajectory.

Still within-model; not gravity / a_T / cosmology.
