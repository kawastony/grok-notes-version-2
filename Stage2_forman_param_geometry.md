# Stage-2: graph curvature + parameter-space distances

Tony Kawas / 19 September 2026.

L=10, d=3, mode 0. Residual-validated. Discrete / effective geometry only.

---

## A. Forman–Ricci on the pair tube

**Construction**
- Nodes: lattice sites inside the pair tube (half-length + core radius, transverse radius BRIDGE+1).
- Vertex weight \(w_i = \rho_i\).
- Edge weight \(w_e = \sqrt{\rho_i\rho_j}\) for nearest-neighbor edges inside the tube.
- Forman curvature on edge \(e=ij\):
\[
F(e)=w_i+w_j-\sum_{e'\sim i,\,e'\ne e}\frac{w_e}{\sqrt{w_e w_{e'}}}-\sum_{e'\sim j,\,e'\ne e}\frac{w_e}{\sqrt{w_e w_{e'}}}.
\]

**Results** (168 nodes, 403 edges in all three states)

| case | mean \(F\) (all) | mean \(F\) (mid edges) | frac neg (mid) |
|------|------------------|------------------------|----------------|
| baseline | −8.44 | **−9.28** | 1.00 |
| +15% | −8.16 | **−8.71** | 1.00 |
| −15% | −8.39 | −8.72 | 1.00 |

All edges have negative Forman on this weighted lattice graph (common for dense local neighborhoods). **Relative** mid-region Forman is less negative under both ±15% than baseline, with +15% slightly less negative overall.

**Interpretation (disciplined)**
- Absolute Forman scale is not universal; compare **differences** across states.
- Mid-tube Forman moves in the same direction for boost and weaken (less negative than baseline).
- This does **not** yet cleanly separate collective vs polarized identity the way \(D_1\) and quad \(c\) do.
- Graph curvature is a usable Stage-2 observable; it is **not** continuum Ricci or Einstein curvature.

---

## B. Parameter-space density distances

States as points in the space of normalized densities \(\rho(x)\).

**\(L^2\) distance**
\[
d_{L2}(\rho,\rho')=\sqrt{\sum_x(\rho_x-\rho'_x)^2}.
\]

| pair | \(d_{L2}\) | Hellinger |
|------|-----------|----------|
| base ↔ +15% | 0.040 | 0.359 |
| base ↔ −15% | 0.041 | 0.372 |
| +15% ↔ −15% | **0.029** | **0.270** |

Boost and weaken are each ~0.04 from baseline and **closer to each other** (~0.029) than to baseline. Both perturbations move the density into a nearby region of configuration space; they are not opposite rays from the baseline point.

That matches the earlier finding that ±15% both compactify (not inverse operations).

---

## C. Relation to Stage 1

| Layer | Best separator of boost vs weaken |
|-------|-----------------------------------|
| Stage 1 shape (\(D_1\), quad \(c\), anisotropy) | **Strong** |
| Stage 2 Forman mid | Weak / same-direction |
| Stage 2 param distance | Shows non-opposition of ± paths |

Identity contrast remains sharpest at Stage 1. Stage 2 adds network and parameter geometry without replacing those diagnostics.

---

## Compact statement

Forman curvature on the pair tube is uniformly negative; mid-tube Forman is less negative under both ±15% than baseline. Parameter-space \(L^2\) distances show boost and weaken as nearby states, not opposite displacements from baseline — consistent with non-reciprocal compactification. Stage-2 geometry is in place; Einstein language remains out of scope.
