# Geometry vs intensity (L=10, d=3 static response)

Tony Kawas / 19 September 2026.

**Question:** When one core is boosted and both cores/bridge respond, does the pair **elongate** or **load more at similar (or tighter) geometry**?

**Answer:** Primarily **densification + modest contraction**, not axial elongation.

Residuals ~10⁻¹⁴. Mode 0 only for the comparison.

---

## Observables

| Symbol | Meaning |
|--------|--------|
| span | RMS axial second moment of full density |
| width | RMS transverse second moment |
| z_cent | density centroid along pair axis (vs midpoint) |
| load | P1+P2+Bρ |
| Wpair | weight in pair tube |
| span_pair / width_pair | RMS of tube-restricted density |

---

## Mode 0 numbers

| Tag | \|λ\| | load | span | width | z_cent | Wpair | BT |
|-----|--------|------|------|-------|--------|-------|------|
| baseline | 0.00139 | 0.134 | 3.37 | 3.88 | +0.99 | 0.170 | 1.76e-4 |
| boost_c1 +15% | 0.00004 | **0.214** | **2.94** | **3.52** | +0.32 | 0.248 | 1.99e-4 |
| boost_c2 +15% | 0.00027 | **0.191** | **3.08** | **3.64** | +0.37 | 0.256 | 1.88e-4 |
| boost_c1 +30% | 0.00089 | 0.123 | 3.08 | 3.83 | +0.26 | 0.210 | 0.76e-4 |
| boost_c2 +30% | 0.00083 | 0.112 | 2.74 | 3.63 | +0.21 | 0.268 | 0.64e-4 |

### Δ vs baseline (+15%)

| | Δload | Δspan | Δwidth | Δz_cent |
|--|--------|--------|---------|---------|
| boost_c1 | **+0.080** | **−0.43** | **−0.35** | −0.67 |
| boost_c2 | **+0.057** | **−0.29** | **−0.24** | −0.62 |

---

## Case classification

| Hypothesis | Expected | Observed (+15%) |
|------------|----------|-----------------|
| Cone elongation | span ↑ | **span ↓** |
| Corridor widening | width ↑ | **width ↓** |
| Densification at fixed size | load ↑, span ~ const | load ↑, span actually **shrinks** |
| Directed slide to boosted core | centroid toward that core | centroid **toward midpoint** |

**Best description:** Case 2/3 hybrid — **more loaded and slightly more compact**, not elongated. Mild boost pulls the object toward a tighter, more pair-centered support.

+30% is non-monotonic (load and BT fall) — different regime; do not use it for the elongation question.

---

## Limits of the check

- span1090 = 9 on all runs (density is torus-wide); 10–90% span is saturated and uninformative.
- peak_sep diagnostic failed (coarse local-max search).
- L=10 only; Prest still large.
- “Mode 0” can change character under strong boost.

---

## Compact statement

The collective static response is **not cone elongation**. A +15% one-core boost increases pair-region load and slightly **decreases** axial and transverse RMS size, with the centroid moving toward the pair midpoint. Intensity/compactification, not stretching.
