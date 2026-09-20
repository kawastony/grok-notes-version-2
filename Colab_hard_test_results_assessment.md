# Colab hard-test results assessment

Tony Kawas / 20 September 2026.

User-run Colab output (reproduced below for the record).

---

## Test A — CC + DESI BAO (summary cov)

| Model | χ² | H₀ | Ωₘ | r_d |
|-------|-----|-----|-----|------|
| **φ-frozen** | **31.28** | 67.84 | 0.302 | 147.52 |
| ΛCDM | 31.92 | 69.85 | 0.281 | 147.46 |
| paste | 32.00 | 67.58 | 0.269 | 147.22 |

**Δχ²(φ − ΛCDM) = −0.64**  
**Δχ²(paste − ΛCDM) = +0.08**

Consistent with Stage-1 (earlier Δχ² ≈ −0.9). Frozen φ remains **mildly preferred**; paste is neutral/slightly worse. Not an official joint posterior.

---

## Test B — Linear growth (fluid ODE, Ωₘ=0.30)

| z | f_ΛCDM | f_φ | ratio |
|---|--------|-----|-------|
| 0.00 | 0.513 | 0.511 | 0.997 |
| 0.38 | 0.705 | 0.687 | **0.975** |
| 0.51 | 0.753 | 0.737 | 0.979 |
| 0.61 | 0.784 | 0.770 | 0.983 |
| 1.00 | 0.869 | 0.866 | 0.996 |

Maximum difference **~2.5%** near z≈0.38 (close to phantom crossing). Compatible with current fσ₈ precision if σ₈ is fixed today. **PPF still required** for a proper Boltzmann treatment.

---

## Test C — SPARC Q=1 BTFR residuals (N=83)

| Scale | mean residual | rms |
|-------|---------------|-----|
| pure a₀ | **−0.161 dex** | 0.247 |
| R_cone × a₀ | **+0.019 dex** | 0.247 |

corr(log V, res_R) = **−0.403**

**Plot reading:**  
Orange points (R_cone) sit closer to zero on average than blue (a₀), especially at mid–high V. A downward slope with log V remains — pure intercept shift does not erase a residual velocity trend (free BTFR slope ≈3.6 vs assumed 4 contributes).

**Verdict:** R_cone **works as a normalization** (mean offset removed). It is **not** a complete velocity-independent galactic law on this sample.

---

## Cumulative consistency check

| Probe | This Colab | Earlier notes | Agreement |
|-------|------------|---------------|-----------|
| CC+BAO Δχ²(φ−Λ) | −0.64 | ≈ −0.9 | Yes |
| Growth max |Δf|/f | ~2.5% | ~2.5% | Yes |
| SPARC mean res_R | +0.019 | +0.019 | Exact match |
| corr(logV, res) | −0.40 | −0.40 | Exact match |

No numerical surprise; Colab reproduced the sandbox results.

---

## What this does / does not establish

**Establishes**
- Frozen φ survives the same late-time summary test on an independent run.
- Linear growth stays close to ΛCDM.
- R_cone removes the global BTFR mean offset on SPARC Q=1.

**Does not establish**
- Official DESI+Planck joint posterior
- PPF-stable growth / lensing
- Galaxy-by-galaxy RC law (only BTFR intercept + residual trend)
- Micro → macro derivation theorem

---

## Next (still external)
1. Cobaya + bao_data full DESI cov + Planck at frozen F  
2. CLASS/CAMB with `use_ppf` + fσ₈  
3. SPARC rotmod RC residuals with R fixed  

---

## Compact statement

Colab confirms: φ χ² = 31.28 vs ΛCDM 31.92 (Δχ²=−0.64); growth within 2.5% of ΛCDM; SPARC mean residual shifts from −0.16 to +0.02 dex under R_cone, with a remaining corr(log V, residual)=−0.40. Results match prior notes. Official joint cosmology and PPF remain the verification walls.
