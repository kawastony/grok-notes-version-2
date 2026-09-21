# Official DESI ALL BAO (full covariance) — frozen-φ result

Tony Kawas / 21 September 2026.

Data: `CobayaSampler/bao_data`  
`desi_2024_gaussian_bao_ALL_GCcomb_mean.txt` + `..._cov.txt`  
12 points (DV/DM/DH over rs), full 12×12 covariance, including Lyα at z=2.33.

Method: pure-Python profile likelihood over (H₀, Ωₘ, r_d); (w₀, w_a) frozen.

---

## Results

| Model | χ² | H₀ | Ωₘ | r_d |
|-------|-----|-----|-----|------|
| **φ-frozen** | **11.782** | 67.51 | 0.316 | 146.77 |
| ΛCDM | 12.741 | 69.10 | 0.294 | 147.52 |
| paste (−0.79, −0.152) | 13.842 | 66.91 | 0.302 | 145.99 |

**Δχ²(φ − ΛCDM) = −0.958**  
**Δχ²(paste − ΛCDM) = +1.101**

---

## Interpretation

- Frozen φ is **mildly preferred** over ΛCDM on the official DESI ALL Gaussian BAO covariance.
- Paste is disfavored relative to both.
- Consistent in *direction* and *magnitude* with the earlier summary-cov Stage-1/Colab result (Δχ² ≈ −0.6 to −0.9).
- This is **not** a full DESI+Planck joint posterior; it is the official multi-tracer BAO block only.
- Background parameters shift mildly (H₀ lower, Ωₘ higher under φ) as expected for a CPL that is phantom early and quintessence late.

---

## Relation to previous tests

| Test | Δχ²(φ − Λ) |
|------|-----------|
| Stage-1 summary BAO+CC | ≈ −0.9 |
| Colab summary BAO+CC | −0.64 |
| **Official DESI ALL full cov** | **−0.96** |

No tension introduced by upgrading to the official joint covariance.

---

## What remains external

- Full Planck likelihood (plik + lowℓ)
- PPF growth / fσ₈
- Joint DESI+Planck+SN posterior at frozen F

---

## Compact statement

On official DESI DR1 ALL Gaussian BAO (12 points, full cov): frozen φ χ² = 11.78 vs ΛCDM 12.74 → **Δχ² = −0.96**. Official-cov survival confirmed at the BAO level; joint CMB remains the next wall.
