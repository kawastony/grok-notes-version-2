# One-sided weakening test (L=10, d=3)

Tony Kawas / 19 September 2026.

**Hypothesis:** If +15% boost compactifies and loads the pair, a mild one-sided *cut* should expand it (span↑, width↑, load↓).

**Result:** **Not confirmed.** Weakening is **not** the inverse of boosting.

Residuals ~10⁻¹⁴. Mode 0.

---

## Numbers

| Tag | v1 | v2 | \|λ\| | P1 | P2 | load | span | width | z_cent | BT |
|-----|----|----|--------|------|------|------|------|-------|--------|------|
| baseline | 2.00 | 2.00 | 0.00139 | 0.042 | 0.029 | 0.134 | 3.37 | 3.88 | +0.99 | 1.76e-4 |
| cut_c1 −7.5% | 1.85 | 2.00 | 0.00106 | 0.032 | 0.045 | 0.134 | 3.33 | 3.59 | +0.76 | 0.98e-4 |
| cut_c1 −15% | 1.70 | 2.00 | 0.00093 | 0.034 | 0.061 | 0.161 | 3.22 | 3.39 | +0.11 | 1.66e-4 |
| cut_c2 −7.5% | 2.00 | 1.85 | 0.00011 | 0.028 | 0.041 | 0.111 | 3.21 | 3.45 | +0.48 | 0.74e-4 |
| cut_c2 −15% | 2.00 | 1.70 | 0.00066 | 0.029 | 0.061 | 0.142 | 3.04 | 3.65 | +0.60 | 0.86e-4 |

### Δ vs baseline

| Tag | Δload | Δspan | Δwidth | Δz_cent |
|-----|--------|--------|---------|---------|
| cut_c1 −7.5% | ~0 | −0.03 | **−0.29** | −0.23 |
| cut_c1 −15% | +0.027 | **−0.15** | **−0.49** | −0.88 |
| cut_c2 −7.5% | **−0.023** | **−0.15** | **−0.43** | −0.51 |
| cut_c2 −15% | +0.007 | **−0.33** | **−0.23** | −0.40 |

---

## Verdict

| Expected if reversible | Observed |
|------------------------|----------|
| load ↓ | mixed (only cut_c2 −7.5% clearly down) |
| span ↑ | **span ↓ in all four** |
| width ↑ | **width ↓ in all four** |
| stay molecular, expand | no expansion |

Also: P2 **rises** in every cut (weight toward the AH core), P1 falls. That is **asymmetric redistribution**, not a symmetric tube expansion.

---

## Classification

- **Not** smooth inverse / cone expansion.  
- **Not** a clean breakup into a single defect either (both cores still have weight).  
- Best label: **nonlinear / non-reciprocal response** — weakening does not undo compactification; the pair stays compact or tightens further, with weight shifting toward core 2.

This matches the earlier warning: ±15% is already near a non-monotonic regime.

---

## Compact statement

A mild one-sided *decrease* of either core at L=10, d=3 does **not** expand the molecular object. Axial span and transverse width shrink or stay smaller; load does not systematically fall. The boost→compactify map is **not reversible** under weakening. Elongation-on-reduction remains unsupported.
