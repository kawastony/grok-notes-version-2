# Parallel progress while Cobaya is pending

Tony Kawas / 20 September 2026.

---

## 1. Geometric identity board (locked arithmetic)

| Symbol | Value |
|--------|-------|
| φ | 1.618033988750 |
| R_cone = √6/φ | **1.513867916134** |
| w₀ = −φ/2 | **−0.809016994375** |
| w_a = −1/φ | **−0.618033988750** |
| z_cross = 1/√5 | **0.447213595500** |
| w₀ + w_a | −1.427050983125 |
| w_a / w₀ | 2/φ² ≈ 0.763932 |

These are exact once the primitives (φ from interpolator, (φ')²=6 on activation surface) are accepted.

---

## 2. SPARC velocity residual — diagnosed

**Question:** Is the corr(log V, residual) ≈ −0.40 a failure of R_cone?

**Answer: No — it is a slope effect.**

| Fit | Slope | Intercept | rms residual |
|-----|-------|-----------|--------------|
| Free | **3.561** | 2.579 | 0.226 |
| Forced slope 4 + best intercept | 4 | 1.649 | higher |
| Forced slope 4 + **R_cone** | 4 | 1.630 | — |

Difference: data slope-4 intercept vs R_cone intercept = **0.019 dex** = exactly the mean residual reported under R_cone.

**Interpretation:**
- R_cone correctly sets the **slope-4 normalization** (to 0.02 dex).
- The sample prefers slope ≈ 3.56 (standard SPARC result), so residuals vs a slope-4 law **must** trend with V.
- That trend is **not** evidence against R_cone; it is evidence that the deep-regime V⁴ law is an approximation for the full sample.

**Implication for the dual claim:** R_cone remains a viable geometric normalization. Claiming a pure V⁴ law for all SPARC galaxies was always too strong; literature slopes are 3.5–3.9 depending on estimator and Υ*.

---

## 3. Lattice Index spectral-flow recipe (ready)

Sharp micro closure target:

```
H(λ) = Wilson-Dirac + λ × hedgehog_mass,  λ: 0 → 1
Track lowest eigenvalues vs λ
Index := number of zero crossings (spectral flow)
Compare to N_def = winding of n̂
Residual-gate soft modes at λ=1 (r_rel ≤ 1e-6)
Test N_def = ±1, ±2 on L = 8, 10, 12
```

This is the cleanest numerical path to Index ≈ N_def without requiring a continuum analytic proof first.

---

## 4. Status board (updated)

| Item | Status |
|------|--------|
| Geometric identities (R_cone, w₀, w_a, z_c) | **Locked** |
| Stage 1–2 / Colab CC+BAO | φ mildly preferred |
| SPARC R_cone normalization | **Works** (0.02 dex); V-trend = slope≠4 |
| Cobaya official DESI cov | **Pending on your Colab** |
| PPF growth | Recipe ready; needs CLASS |
| Lattice Index spectral flow | **Recipe ready** |
| Micro → (w₀,w_a) theorem | Still open |
| Paper override (10D → cone) | Documented |

---

## 5. What to do when Cobaya returns

1. Record Δχ²(φ − Λ) on official DESI ALL cov  
2. If Δχ² ≲ 0 → official-cov survival  
3. If Δχ² ≫ 0 → tension; diagnose which tracer/z drives it  
4. Either way: next is PPF growth or spectral-flow Index Colab  

---

## Compact statement

While Cobaya runs: (1) identity board locked; (2) SPARC V-trend diagnosed as slope≈3.56 vs V⁴ assumption — R_cone normalization still good to 0.02 dex; (3) spectral-flow Index recipe written for micro closure. No blockers created; dual geometric claim intact pending official DESI Δχ².
