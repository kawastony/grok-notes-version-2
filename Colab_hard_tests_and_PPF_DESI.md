# Colab hard tests + PPF crossing treatments + DESI covariance

Tony Kawas / 20 September 2026.

Colab script path (local artifacts): `colab_hard_tests_frozen_phi.py`  
Also mirrored below as cell list.

---

## PART I — Colab hard tests (for you to run)

Copy cells from `colab_hard_tests_frozen_phi.py` into Colab.

| Cell | Test | What you get |
|------|------|--------------|
| 0 | Installs | numpy/scipy/matplotlib |
| 1 | Frozen constants | w0, wa, R_cone, helpers |
| 2 | **Test A** CC+DESI BAO χ² | Δχ² frozen vs ΛCDM vs paste |
| 3 | **Test B** linear growth | f(z) ratio (fluid; not PPF) |
| 4 | **Test C** SPARC R_cone residuals | mean residual, velocity trend |
| 5 | Cobaya YAML skeleton | paste to file when cobaya+classy ready |

**Frozen numbers (do not retune):**
```
w0 = -phi/2 ≈ -0.8090169944
wa = -1/phi ≈ -0.6180339887
R_cone = sqrt(6)/phi ≈ 1.513867916
```

**What Colab can do well:** A, B (fluid), C.  
**What needs cluster/Cobaya:** full DESI joint cov + Planck likelihood + CLASS PPF.

---

## PART II — PPF crossing treatments (investigation)

### Why PPF is needed
Single scalar field cannot cross w=−1 without ghost/gradient instability.  
Frozen-φ CPL **does** cross at z_c=1/√5 (early phantom → late quintessence).

### Hu–Sawicki / Fang–Hu–Lewis PPF
Parameterized Post-Friedmann closes the metric perturbation equations **without** requiring a fundamental scalar that crosses.

Core object: auxiliary variable Γ related to DE rest-frame density contrast:
\[
\Gamma \propto -\frac{a^2}{k^2}\delta\rho_{\rm DE}^{\rm rest}
\]
Evolution (schematic, conformal time):
\[
\Gamma' = \mathcal{H}\left[
\frac{S}{1+c_\Gamma^2 k^2/\mathcal{H}^2}-\Gamma\left(1+\frac{c_\Gamma^2 k^2}{\mathcal{H}^2}\right)^{-1}
\right]
\]
with source S built from total matter velocity. Typical closure: c_Γ ≈ 0.4 c_s, f_ζ=0.

**Properties:**
- Conserves energy–momentum
- Exact on super-horizon and deep sub-horizon relative to the DE Jeans scale
- Well-controlled approximation across the crossing

### Implementations
| Code | How |
|------|-----|
| **CAMB** | Public PPF module (Fang/Hu): https://background.uchicago.edu/ppf/ — supports w0–wa and arbitrary w(a) file |
| **CLASS** | PPF formalism (Tram notes); flag `use_ppf = yes` in fluid dark energy when built with PPF support |
| **Cobaya** | Theory: classy or camb with PPF-enabled extra_args; freeze w0_fld, wa_fld |

### Practical recommendation for frozen-φ
1. Background: ordinary CPL H(z) (no issue).
2. Perturbations: **always** enable PPF when running Boltzmann for growth/lensing/ISW.
3. Compare: fluid ODE (already done, ≲2.5% vs ΛCDM) vs CLASS+PPF fσ₈ — difference should be small if PPF works as designed.

**Risk if PPF omitted:** formal singularities or wrong-sign sound speed near w=−1 can crash the integrator or give spurious growth.

---

## PART III — DESI covariance matrices (investigation)

### Official public sources

| Product | Location |
|---------|----------|
| **Cobaya-ready BAO likelihoods** | https://github.com/CobayaSampler/bao_data |
| DESI DR1 Gaussian BAO | `desi_2024_gaussian_bao_*_mean.txt` + `*_cov.txt` per tracer |
| DESI DR1 ALL combined | `desi_2024_gaussian_bao_ALL_GCcomb_mean.txt` + cov |
| DESI DR2 | `desi_bao_dr2/` folder in same repo |
| Full-shape + BAO clustering | https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering (h5 covariances, large) |
| Cosmology chains | https://data.desi.lbl.gov/public/dr1/vac/dr1/bao-cosmo-params |

### Format (Cobaya `bao.generic` / desi_2024_*)
- **mean file:** columns z, value, quantity type (DV_over_rs, DM_over_rs, Hz_rs, …)
- **cov file:** square matrix, same row order as mean file
- Optional `rs_fid` if distances stored in units of a fiducial sound horizon

### Tracer structure (DR1 summary)
| Tracer | z_eff (approx) | Observables |
|--------|----------------|-------------|
| BGS | 0.30 | DV/rd |
| LRG1–3 | 0.51, 0.71, 0.93 | DM/rd, DH/rd (correlated) |
| ELG | 1.32 | DM/rd, DH/rd |
| QSO | 1.49 | DV/rd |
| Lyα | ~2.3 | DM/rd, DH/rd |

Published **r_off** between DM and DH per bin (~ −0.4) is what Stage-2 used; full joint matrix includes cross-tracer and Lyα blocks.

### What Stage-2 approximated vs official
| Item | Stage-2 (this repo) | Official |
|------|---------------------|----------|
| Diagonal + r_off per anisotropic bin | Yes | Subset |
| Full joint multi-tracer + Lyα cov | **No** | bao_data `ALL` + Lyα files |
| Planck full likelihood | Approx (R,ℓ_A) | plik TTTEEE + lowℓ |

**Action for Colab/Cobaya:** clone `CobayaSampler/bao_data`, point likelihood at `desi_2024_gaussian_bao_ALL_GCcomb_*.txt` (or DR2 equivalents), freeze w0/wa, free H0/ωb/ωcdm/nuisances.

---

## PART IV — While you run Colab

Suggested order on Colab:
1. Cells 0–2 → confirm Stage-1-style χ² still favors φ
2. Cell 3 → growth ratios
3. Cell 4 → SPARC residuals (needs network for CDS download)
4. If GPU/time: install cobaya+classy, run YAML with bao_data DESI files only first (no Planck), then add Planck

Report back:
- χ² table (phi / lcdm / paste)
- SPARC mean res_R and corr(logV, res)
- Any Cobaya Δχ²(F−Λ) if you get that far

---

## Compact statement

Hard tests are drafted in `colab_hard_tests_frozen_phi.py` (A: CC+BAO χ², B: fluid growth, C: SPARC R_cone, D: Cobaya skeleton). PPF (Hu–Sawicki / Fang–Hu–Lewis) is the correct crossing treatment for frozen-φ; enable in CLASS/CAMB. DESI covariances are public via CobayaSampler/bao_data (`desi_2024_*` mean+cov); Stage-2 used only diagonal+r_off — official joint is the upgrade path.
