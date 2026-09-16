# Correlation length and the molecular regime

Tony Kawas / 16 September 2026.

---

## 1. What “correlation length” means here

In the Callias / lattice-Dirac setting there is no critical point in the usual sense. The relevant length is the **bulk correlation length** set by the spectral gap of the free (or far-from-defect) operator:

\[
\xi \sim \frac{1}{\Delta_{\rm bulk}}.
\]

Defect zero modes decay as ∼ e^{−r/ξ} away from the core. Two cores separated by distance sep hybridize with amplitude

\[
\Delta\lambda \sim e^{-{\rm sep}/\xi}
\]

(up to power-law prefactors). Independent localization requires **sep ≫ ξ**.

There is no divergent correlation-length *exponent* ν unless one tunes a parameter to a continuum limit or a gap-closing transition. The practical question is the numerical value of ξ relative to available sep.

---

## 2. Bulk gap measurement

Free 8-component Wilson (no hedgehog), m₀ = 0.3, r = 1:

| L | min \|λ\| |
|---|----------|
| 6 | 0.300 |
| 8 | 0.300 |

Bulk gap Δ_bulk = m₀ = 0.3 (exact match to the mass parameter at these volumes). Therefore

\[
\xi_{\rm bulk} \approx \frac{1}{m_0} \approx 3.3 \text{ lattice units}.
\]

Core width w ∼ 1 adds a second scale; the effective mode size is a few times max(w, ξ_bulk).

---

## 3. Soft splitting vs separation (L = 8)

| sep | \|λ₁\| | Δλ |
|-----|-------|-----|
| 2 | 0.0040 | 0.018 |
| 3 | 0.0040 | 0.018 |
| 4 | 0.00043 | 0.0021 |
| 5 | 0.00043 | 0.0021 |
| 6 | 0.0010 | 0.0030 |

Δλ is **non-monotonic**. An exponential fit sep 4 → 6 yields an unphysical negative ξ — torus image interactions and discrete placement dominate over pure two-core tunneling at these sizes.

---

## 4. Why the molecular regime persists

At L ≤ 10 the largest usable separation is sep ∼ 5–6. With ξ ∼ 3.3 that is only

\[
{\rm sep}/\xi \sim 1.5\text{–}2.
\]

Exponential suppression e^{−sep/ξ} ∼ 0.14–0.22 is mild — hybridization remains O(1). To reach e^{−sep/ξ} ≲ 0.01 one needs sep/ξ ≳ 5, i.e. sep ≳ 15–20 lattice units and therefore L ≳ 30–40 for a pair on a torus — far beyond the present memory ceiling.

---

## 5. Correlation-length exponent

A critical exponent ν would appear if one tuned a parameter (e.g. m₀ → 0, or a continuum a → 0 limit) so that ξ diverges:

\[
\xi \sim |m-m_c|^{-\nu}.
\]

In the present fixed-m₀ lattice setup:
- ξ is finite and set by m₀,
- there is no diverging length to extract ν from,
- the only “exponent” question is the power of finite-a or finite-L corrections to the Callias index, which requires a continuum extrapolation at large L.

**Conclusion:** the correlation-length *exponent* is not the operative concept here; the correlation *length value* relative to separation is. That ratio is currently too small for decoupling.

---

## 6. Practical implications

| Goal | Requirement |
|------|-------------|
| Isolated core modes | sep/ξ ≳ 5 ⇒ sep ≳ 15–20 |
| Clean FSS of Δλ ∼ e^{−sep/ξ} | several sep values ≫ ξ |
| Continuum index extrapolation | L large, a → 0 at fixed physical ξ |

None of these are accessible at L ≤ 10. Reducing m₀ would *increase* ξ and make decoupling harder; increasing m₀ shrinks ξ but risks lattice artefacts and a harder bulk gap that may push soft modes up.

---

## Compact statement

The bulk gap fixes ξ ≈ 1/m₀ ≈ 3.3 lattice units. Soft-mode splitting is non-monotonic in separation at L = 8 and cannot be fit to a clean exponential. At available volumes sep/ξ ∼ 1.5–2, so strong hybridization is expected. A correlation-length *exponent* is not relevant until a gap-closing or continuum limit is tuned; the present bottleneck is simply sep ≲ ξ, not a missing critical exponent.
