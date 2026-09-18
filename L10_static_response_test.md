# Static response test (L=10, d=3)

Tony Kawas / 19 September 2026.

**Protocol:** Residual-validated pair at L=10, d=3. Boost one core coupling \(v\) while holding the other at 2.0. Recompute two softest modes. Residuals ~10⁻¹³–10⁻¹⁴.

**Question:** Does weight slide along the corridor toward the boosted core?

---

## Mode 0 results

| Tag | v1 | v2 | \|λ\| | P1 | P2 | P1−P2 | BT | Bρ |
|-----|----|----|--------|------|------|--------|--------|------|
| baseline | 2.0 | 2.0 | 0.00139 | 0.042 | 0.029 | +0.013 | 1.76e-4 | 0.063 |
| boost_c1 | 2.3 | 2.0 | 0.00004 | 0.065 | 0.068 | −0.004 | 1.99e-4 | 0.081 |
| boost_c1_strong | 2.6 | 2.0 | 0.00089 | 0.035 | 0.038 | −0.004 | 0.76e-4 | 0.050 |
| boost_c2 | 2.0 | 2.3 | 0.00027 | 0.068 | 0.048 | +0.020 | 1.88e-4 | 0.076 |
| boost_c2_strong | 2.0 | 2.6 | 0.00083 | 0.043 | 0.026 | +0.017 | 0.64e-4 | 0.044 |

### Δ vs baseline (mode 0)

| Tag | Δλ | ΔP1 | ΔP2 | ΔBT | ΔBρ |
|-----|------|------|------|------|------|
| boost_c1 (+15%) | −0.00135 | +0.023 | +0.039 | +2.3e-5 | +0.018 |
| boost_c1 (+30%) | −0.00050 | −0.008 | +0.009 | −1.0e-4 | −0.013 |
| boost_c2 (+15%) | −0.00112 | +0.026 | +0.019 | +1.3e-5 | +0.013 |
| boost_c2 (+30%) | −0.00056 | +0.001 | −0.004 | −1.1e-4 | −0.019 |

---

## Interpretation

### What happened (mild +15% boost)

- Softest \|λ\| **drops sharply** (pair gets softer).
- **Both** P1 and P2 **increase** (more weight on the pair, less Prest).
- BT and Bρ **rise modestly**.
- Weight does **not** simply pile onto the boosted core only.

Boosting core 1 even **increases P2 more than P1**. Boosting core 2 increases **both**, with P1 still larger.

### Strong +30% boost

- Response is **non-monotonic**: BT and Bρ **fall** below baseline.
- P shifts mixed; possible mode-character change.
- Treat as a different regime, not a linear continuation of +15%.

### Answer to the dynamics question

**No clean sliding-transfer law** at this volume:

> Boosting one core does not move support from the other core along the bridge in a directed way.

What *is* seen:

> A mild one-sided texture boost **softens** the pair and **increases shared + bridge weight** together — a **collective** response of the molecular object, not a one-way transfer.

That still supports pair identity (the object responds as a whole). It does **not** demonstrate propagation along the rope.

---

## Caveats

- Comparing “mode 0” across perturbations can mix characters if levels reorder.
- L=10, d=3 only; L=12 response not run here.
- Finite torus; Prest still dominates (~0.87–0.93).

---

## Compact statement

Static response at residual-validated L=10, d=3: a +15% boost of either core softens the ground mode and raises both core weights and bridge density together. There is no simple directed slide of weight onto the boosted core. The pair responds as a shared molecular object. This is structural response, not a transport demonstration.
