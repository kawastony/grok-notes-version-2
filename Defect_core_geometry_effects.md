# Defect core geometry effects

Tony Kawas / 16 September 2026.

---

## Setup

L = 8, w = 1.0, v = 2.0, 8-component Wilson + Callias mass. Geometry parameters varied systematically.

---

## 1. Separation scan (periodic pair along z)

| sep | softest \|λ\| |
|-----|--------------|
| 2 | 0.0040 |
| 3 | 0.0040 |
| **4** | **0.00043** |
| **5** | **0.00043** |
| 6 | 0.0010 |

Softest window around sep = 4–5. Closer pairs (sep ≤ 3) harden; larger sep = 6 slightly harder again (finite-volume / image effects on the torus).

---

## 2. Placement orientation (sep = 4)

| Axis | softest \|λ\| | P_A / P_B (mode 0) |
|------|--------------|-------------------|
| z | 0.00043 | 0.095 / 0.095 |
| x | 0.00043 | 0.095 / 0.095 |
| y | 0.00043 | 0.095 / 0.095 |
| body diagonal | 0.00027 | 0.076 / 0.076 |

Orientation of the pair axis is essentially irrelevant; modes remain equally shared. Body-diagonal placement is slightly softer but still fully hybridized.

---

## 3. Relative topological sign

| Configuration | softest \|λ\| |
|---------------|--------------|
| Opposite (+1, −1) | **0.00043** |
| Same-sign (+1, +1) | 0.00145 |

Opposite-charge pair is significantly softer — consistent with a topologically compensated pair supporting a soft sector, while same-sign pairs sit higher.

---

## 4. Single defect vs pair (periodic)

| Geometry | softest \|λ\| |
|----------|--------------|
| Single +1 | 0.00154 |
| Pair +/− | **0.00043** |

The compensated pair is softer than a single defect on the same volume (torus obstruction for a single nonzero topological charge is expected to push modes up).

---

## 5. Open boundary, single defect

| Geometry | softest \|λ\| |
|----------|--------------|
| Open BC, single +1 | 0.00126 |

Still soft (comparable to periodic single). Open BC removes the torus obstruction but does not by itself produce a dramatically isolated zero mode at L = 8.

---

## Interpretation

1. **Separation** is the dominant geometric knob within L = 8: an intermediate window (sep ≈ 4–5) minimizes the softest eigenvalue.  
2. **Pair axis orientation** does not break the hybridization.  
3. **Opposite topological charges** are required for the softest sector — same-sign pairs are harder.  
4. **Compensated pair** is softer than a single defect on the torus, as expected from index considerations.  
5. None of these geometry changes at L = 8 recover independent core localization; they modulate the soft spectrum but leave modes shared.

---

## Compact statement

Defect-core geometry (separation, placement, relative sign, single vs pair, open vs periodic) modulates the soft spectrum in the expected directions: opposite-charge pairs at intermediate separation are softest. Hybridization and equal core weight persist across all tested geometries at L = 8. Scale separation remains the bottleneck for independent core localization.
