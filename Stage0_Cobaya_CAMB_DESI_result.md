# Stage 0 Cobaya CAMB + DESI ALL — result

Tony Kawas / 21 September 2026.

## Setup
- Theory: CAMB (`DarkEnergyPPF` for φ)
- Likelihood: `bao.generic` with official  
  `desi_2024_gaussian_bao_ALL_GCcomb` mean + full cov
- Frozen: \(w_0=-\varphi/2\), \(w_a=-1/\varphi\)
- LCDM: no w/wa (standard Λ)
- Sampler: MCMC, converged (LCDM 1080 steps, φ 720 steps)

## Results

| Model | χ² (bao.generic) | H0 | ombh2 | omch2 |
|-------|------------------|-----|-------|-------|
| **φ-frozen** | **11.79** | 69.04 | 0.0243 | 0.1259 |
| ΛCDM | 12.74 | 70.03 | 0.0239 | 0.1197 |

**Δχ²(φ − ΛCDM) = −0.95**

## Cross-check vs pure-Python

| Method | χ²_φ | χ²_Λ | Δχ² |
|--------|------|------|-----|
| Pure-Python profile | 11.78 | 12.74 | **−0.96** |
| **Cobaya CAMB MCMC** | 11.79 | 12.74 | **−0.95** |

Agreement at the 0.01 level. Official DESI ALL BAO preference for frozen φ is **confirmed** with a Boltzmann code (CAMB), not only a background integrator.

## Status
- Stage 0 **pass**
- Sampler + BAO likelihood path proven
- Next optional: Stage 1 CLASS DESI-only; then Planck only if desired
- Wall 1 compressed Planck joint remains Δχ² ≈ −0.08 (orientation)

## Compact statement
Cobaya CAMB DESI-only: Δχ²(φ−Λ) = −0.95, matching pure-Python −0.96. Frozen geometric DE survives official DESI ALL covariance under a real Einstein–Boltzmann pipeline.
