# Stage-1 shape geometry (L=10, d=3, mode 0)

Tony Kawas / 19 September 2026.

Residual-validated soft modes. Geometry of support only — **not** spacetime metric, not Einstein.

---

## Definitions

Normalized density \(\rho(x)=|v|^2/\sum|v|^2\).

**Shape tensor** around density COM (min-image relative to pair midpoint):
\[
M_{ij}=\sum_x \rho(x)\,(x_i-\bar x_i)(x_j-\bar x_j).
\]
Eigenvalues \(\lambda_1\ge\lambda_2\ge\lambda_3\); anisotropy \(=\lambda_1/\lambda_3\).

**Axial quadratic fit** near midpoint (\(|z|\le 1.5\)):
\[
\rho_{\rm ax}(z)\approx a+bz+c z^2.
\]
\(c<0\): local peak at mid; \(c>0\): local dip/hollow.

---

## Results

| case | \|λ\| | aniso \(\lambda_1/\lambda_3\) | major\|cos∠z\| | quad \(c\) | \(K_{\rm mid}\) | \(D_1\) |
|------|--------|------------------------------|---------------|-----------|----------------|--------|
| baseline | 0.00139 | 1.56 | 1.00 | **−0.0074** | +0.20 | −0.18 |
| +15% | 0.00004 | 1.47 | 1.00 | **−0.0104** | −0.04 | +0.03 |
| −15% | 0.00093 | **1.86** | 1.00 | **+0.0043** | −0.16 | +0.29 |

Eigenvalues (descending):

| case | \(\lambda_1\) | \(\lambda_2\) | \(\lambda_3\) |
|------|-------------|-------------|-------------|
| base | 11.33 | 7.34 | 7.26 |
| +15% | 8.64 | 6.23 | 5.89 |
| −15% | 10.36 | 5.80 | 5.57 |

Major axis is **exactly along the pair axis** (align = 1) in all three states — the object is always elongated along the defect–defect line.

COM shifts toward the midpoint under both ±15% (z-component: +0.99 → +0.32 / +0.11).

---

## Reading

### Boost (+15%)
- All eigenvalues shrink → more compact support (matches earlier densification).
- Anisotropy slightly **down** (1.56 → 1.47) → a bit rounder in the transverse plane relative to length.
- quad \(c\) more negative → **sharper mid peak** (bridge filling in the axial profile).
- \(D_1\to 0\): balanced.

### Weaken (−15%)
- Anisotropy **up** (1.56 → 1.86) → more elongated / one-sided stretch.
- quad \(c\) **positive** → **local dip at mid** (bridge hollow).
- \(D_1=+0.29\): polarized.

### Geometric identity contrast

| | Boost | Weaken |
|--|-------|--------|
| Support size | shrinks | mixed/shrinks less |
| Axial mid shape | peak (\(c<0\)) | dip (\(c>0\)) |
| Anisotropy | down | up |
| Tilt | balanced | polarized |

Same compactification story as before, now with a **tensor** and a **local curvature coefficient**.

---

## What this is / is not

**Is:** discrete geometry of the soft-mode support; Stage-1 of the geometric roadmap.

**Is not:** continuum Riemannian metric; not Callias asymptotics; not cone \(R_{\rm cone}\); not Einstein.

---

## Compact statement

Shape tensor and axial quadratic fit confirm: +15% yields a more compact, mid-peaked, balanced object elongated along the pair axis; −15% yields a more anisotropic, mid-dipped, polarized object. Stage-1 geometry is residual-clean and sharpens identity without spacetime claims.
