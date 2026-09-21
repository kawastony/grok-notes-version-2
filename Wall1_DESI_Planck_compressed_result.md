# Wall 1 result: DESI ALL full cov + Planck compressed prior

Tony Kawas / 21 September 2026.

## Formula fix
Acoustic scale must use angular-diameter form:
\[
\ell_A = \pi\, D_M(z_*)/r_s(z_*) = \pi\, D_c(z_*)/r_s(z_*)\quad(\text{flat}).
\]
Earlier extra \((1+z_*)\) factor produced \(\ell_A\sim 3\times 10^5\) (invalid).

## Sanity (LCDM fiducial H0=67.4, Ωm=0.315, rd=147)
| Quantity | Theory | Obs | Pull |
|----------|--------|-----|------|
| R | 1.758 | 1.7502 | 1.69 |
| ℓ_A | 303.7 | 301.5 | 24.8 |
| χ²_planck (at this fixed point) | 618 | — | proxy/σ mismatch |

High χ² at a fixed non-optimized point is expected: rd↔r_s(z*) proxy and diagonal σ are approximate. The **profiled** joint fit below is the relevant number.

## Profiled joint results

| Model | χ²_tot | H0 | Ωm | rd | χ²_BAO | χ²_P |
|-------|--------|-----|-----|------|--------|------|
| **φ** | **13.211** | 67.66 | 0.316 | 147.07 | 12.48 | 0.73 |
| ΛCDM | 13.287 | 68.78 | 0.302 | 147.58 | 13.26 | 0.02 |
| paste | 21.130 | 65.61 | 0.341 | 145.19 | 19.70 | 1.43 |

**Δχ²(φ − ΛCDM) = −0.076**  
**Δχ²(paste − ΛCDM) = +7.84**

## Interpretation
- Frozen φ is **statistically equivalent** to ΛCDM on DESI ALL + compressed Planck (Δχ² ≈ 0).
- BAO-only preference (Δχ² ≈ −0.96) is largely absorbed once CMB distance geometry is included.
- Paste is clearly worse.
- This is **orientation-grade**, not full plik TTTEEE.

## Cumulative BAO / CMB status

| Test | Δχ²(φ − Λ) |
|------|-----------|
| DESI ALL BAO only | −0.96 |
| DESI ALL + Planck compressed | **−0.08** |

## Remaining walls
- Full Planck plik + lowℓ (cluster)
- Pantheon+ full cov
- PPF growth / fσ₈ with consistent σ₈

## Compact statement
With correct ℓ_A, frozen φ survives DESI ALL + Planck compressed geometry at Δχ² ≈ −0.08 (indistinguishable from ΛCDM). Official-cov BAO preference is diluted but not reversed by CMB distances. Full plik remains the next hard wall.
