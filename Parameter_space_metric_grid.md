# Parameter-space metric on (v1,v2)

Tony Kawas / 19 September 2026.

L=10, d=3, mode 0. All 9 residual-validated (rel ~ 10⁻¹⁴).

Grid: \(v_1,v_2 \in \{1.7, 2.0, 2.3\}\).

---

## Softest |λ| landscape

| v1\\v2 | 1.7 | 2.0 | 2.3 |
|--------|------|------|------|
| 1.7 | 0.00067 | 0.00093 | 0.00091 |
| 2.0 | 0.00066 | **0.00139** | 0.00027 |
| 2.3 | 0.00032 | **0.00004** | 0.00064 |

Baseline (2,2) is a **local maximum** of |λ| among the 9 points — nearby ± perturbations soften the mode.

---

## L2 density distances (selected)

| pair | d_L2 |
|------|------|
| (2,2) ↔ (2.3,2) | 0.040 |
| (2,2) ↔ (1.7,2) | 0.041 |
| (2,2) ↔ (2,2.3) | 0.039 |
| (2,2) ↔ (2,1.7) | 0.042 |
| (2.3,2) ↔ (1.7,2) | 0.029 |
| (2.3,2) ↔ (2,2.3) | **0.024** |

Boost and weaken along either axis remain ~0.04 from baseline and closer to each other than to baseline.

---

## Approximate metric at (2,2)

Pullback of L2 density distance via centered finite differences (Δv = 0.6):

\[
g_{ab} \approx \sum_x \partial_a\rho\,\partial_b\rho
\]

| component | value |
|-----------|-------|
| \(g_{11}\) (along v1) | 0.00227 |
| \(g_{22}\) (along v2) | 0.00320 |
| \(g_{12}\) | 0.00040 |
| \(g_{11}/g_{22}\) | 0.71 |

One-sided sensitivities (|∂ρ/∂v|²):

| direction | up (+0.3) | down (−0.3) |
|-----------|-----------|-------------|
| v1 | 0.0177 | 0.0190 |
| v2 | 0.0171 | 0.0200 |

Slightly stronger response on the **down** side — consistent with non-reciprocity, but magnitudes are comparable (not a hard threshold at ±15%).

---

## Interpretation

1. **Parameter geometry exists** as a real (discrete) metric on soft-mode densities.  
2. Baseline sits at a soft-eigenvalue **ridge/maximum** in this 3×3 patch.  
3. v1 and v2 directions are **not orthogonal** in density space (\(g_{12}\neq 0\)) and not equally stiff (\(g_{22}>g_{11}\)).  
4. Still **not** spacetime geometry and not Einstein.

---

## Compact statement

A 3×3 residual-validated grid yields a usable parameter-space metric: density L2 distances and a local \(g_{ab}\) at (2,2). Softness peaks at baseline; boost and weaken move into a nearby, mutually closer region of configuration space. Stage-2 parameter geometry is in place.
