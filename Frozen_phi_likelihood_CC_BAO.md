# Frozen-φ CPL likelihood test (CC + DESI BAO)

Tony Kawas / 20 September 2026.

**Hypothesis:** The geometric dark-energy point
\[
(w_0,w_a)=(-\varphi/2,\,-1/\varphi)\approx(-0.809017,\,-0.618034)
\]
is consistent with late-time expansion data when only \((H_0,\Omega_m,r_d)\) are profiled.

---

## Dataset (Stage 1)

| Probe | Content | Treatment |
|-------|---------|-----------|
| Cosmic chronometers | 32 H(z) points (Moresco et al. compilation + others) | Uncorrelated χ² (approx.) |
| DESI DR1 BAO | 6 isotropic \(D_V/r_d\) + 4 anisotropic \((D_M,D_H)/r_d\) bins | Diagonal errors (full cov not used) |

**Nuisance / free:** \(H_0\), \(\Omega_m\), \(r_d\).  
**Frozen:** \(w_0\), \(w_a\).  
**Fixed:** flatness, no radiation, no growth sector.

**Caveat:** Diagonal BAO + uncorrelated CC is a **first-pass** likelihood, not the official DESI joint analysis. Results are indicative, not definitive.

---

## Results

### Combined CC + DESI BAO (N ≈ 46 effective points)

| Model | \(w_0\) | \(w_a\) | best \(H_0\) | best \(\Omega_m\) | best \(r_d\) | **χ²** |
|-------|---------|---------|--------------|------------------|---------------|--------|
| **φ-frozen** | −0.809 | −0.618 | 67.68 | 0.306 | 147.5 | **32.57** |
| ΛCDM | −1 | 0 | 69.61 | 0.286 | 147.4 | 33.46 |
| paste (−0.79, −0.152) | −0.79 | −0.152 | 67.47 | 0.272 | 147.2 | 33.03 |

### Δχ² vs ΛCDM

| Model | Δχ² |
|-------|-----|
| **φ-frozen** | **−0.89** |
| paste | −0.43 |
| ΛCDM | 0 |

**φ-frozen is not worse than ΛCDM on this Stage-1 combination; it is slightly better.**

### CC-only sanity

| Model | χ²_CC | H₀ | Ωₘ |
|-------|-------|-----|-----|
| φ | 14.50 | 66.1 | 0.344 |
| ΛCDM | 14.24 | 68.0 | 0.321 |
| paste | 14.63 | 65.8 | 0.315 |

CC alone does not distinguish strongly (as expected with large errors).

---

## Decision (Stage 1 criteria)

| Criterion | Result |
|-----------|--------|
| Acceptable χ² | **Yes** (χ²/N ~ 0.7) |
| Not catastrophically worse than ΛCDM | **Yes** (Δχ² = −0.89) |
| Beats paste point | **Yes** |
| Residuals pathological? | No obvious trend in H(z) or DV/rd plots |

**Stage-1 verdict: viable / interesting.**  
The frozen φ point survives a real distance+expansion test under profiling of \((H_0,\Omega_m,r_d)\). Orientation pass is **not** mere coincidence on this dataset approximation.

---

## What this does *not* claim

- Official DESI+Pantheon+Planck posterior at frozen F  
- Full BAO covariance / SN magnitude likelihood  
- Forced derivation of \((w_0,w_a)\) from TAFA micro physics  
- Growth or galaxy-bridge tests  

---

## Next verification walls

1. Add Pantheon+ (or DESY5) with covariance → Stage 2  
2. Use full DESI BAO covariance matrix  
3. Optional Planck distance prior  
4. Only then: transition-redshift definition test, growth, R-bridge on SPARC  

---

## Compact statement

On a Stage-1 late-time combination (cosmic chronometers + DESI DR1 BAO summaries, diagonal approximation), the frozen geometric CPL point \((w_0,w_a)=(-\varphi/2,-1/\varphi)\) yields χ² = 32.57 after profiling \((H_0,\Omega_m,r_d)\), slightly better than ΛCDM (33.46) and the paste comparison point (33.03). The frozen-φ cosmology is viable under this test. Full covariance + SN is the next required step before strong claims.
