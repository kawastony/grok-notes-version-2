# Forman curvature dynamics under flow

Tony Kawas / 19 September 2026.

Real 8-component operator. Early window only (steps ≲ 10).

---

## 1. Flow rule (reminder)

Normalized discrete Forman flow on edge weights:
\[
\frac{dw_e}{dt} = -\bigl(F(e)-\bar F\bigr)\, w_e.
\]

**Sign structure:**
- If \(F(e) < \bar F\) (edge more negative than average) → \((F-\bar F)<0\) → \(dw>0\) → **weight increases**
- If \(F(e) > \bar F\) (less negative) → weight decreases

Define relative mid curvature:
\[
F^{\rm rel}_{\rm mid} := F_{\rm mid} - \bar F.
\]
When \(F^{\rm rel}_{\rm mid}<0\) (mid more negative than global mean), mid edges **gain** weight under the flow.

---

## 2. Curvature trajectories by identity

| Identity | \(F_{\rm mid}(0)\) | \(F^{\rm rel}_{\rm mid}(0)\) | \(\Delta W_8\) |
|----------|-------------------|------------------------------|---------------|
| **B baseline** (2,2) | −9.28 | **−0.84** (most negative rel) | **+0.088** |
| B boost (2.3,2) | −8.71 | −0.55 | +0.034 |
| T (1.85,2) | −9.19 | −0.55 | +0.033 |
| **P stall** (1.7,2) | −8.72 | **−0.33** (least negative rel) | **+0.001** |

All states have mid more negative than the tube mean (\(F^{\rm rel}<0\)), so mid is in the “gain” sector for all.  
**How much more negative** ranks with feeding rate: baseline deepest relative well → fastest gain; polarized shallowest → near stall.

Under flow, \(|F_{\rm mid}|\) grows (becomes more negative) for all classes in the early window; the **relative** depth \(F^{\rm rel}_{\rm mid}\) is what organizes differential weight uptake.

---

## 3. Mechanism (corrected)

Same Forman flow law everywhere.

| Initial identity | \(F^{\rm rel}_{\rm mid}\) | Early dynamics |
|------------------|--------------------------|----------------|
| Balanced / rich mid | Deeply negative | Mid edges strongly preferred → fast \(W_{\rm mid}\) growth |
| Transitional | Moderately negative | Moderate feeding |
| Polarized / hollowed | Shallowly negative | Weak preference → stall |

Identity places the bridge at different depths in the curvature landscape; the flow then amplifies or neglects the mid region accordingly.

---

## 4. Relation to the assessment text

The pasted text is right that identity predicts **trajectory**, not only static ΔW.

Curvature dynamics add the mechanism layer:

> the same reweighting rule acts on all states; different identities set different \(F^{\rm rel}_{\rm mid}\); that relative curvature controls early bridge-feeding rate.

Static Forman alone (absolute \(F_{\rm mid}\)) was a weak separator.  
**Relative** Forman plus early slope is the dynamical link.

---

## 5. Scope

- Graph curvature evolution on the soft-mode density tube  
- Not continuum Ricci flow  
- Not Einstein / galactic law  
- Early window only

---

## Compact statement

Under normalized Forman flow, mid-tube edges are more negative than the tube mean in all tested identities, so they sit in the weight-gain sector. Baseline has the deepest relative curvature well and feeds fastest; polarized/hollowed has the shallowest and nearly stalls. Identity sets relative curvature position; the same flow law produces different early trajectories.
