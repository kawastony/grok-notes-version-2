# Fix: Cobaya bao.generic install error → pure-Python official DESI χ²

## What broke
```
ComponentNotInstalledError: run cobaya-install bao.generic
TypeError: expected str, bytes or os.PathLike object, not NoneType
```
`bao.generic` is an InstallableLikelihood; on Colab it still demands packages_path even when `measurements_file` / `cov_file` are set. `cobaya-install` also needs `-p /path`.

## Fix
**Do not use Cobaya for this step.**  
Script: `colab_desi_official_chi2.py` (artifacts / copy cells to Colab).

- Loads official  
  `desi_2024_gaussian_bao_ALL_GCcomb_mean.txt`  
  `desi_2024_gaussian_bao_ALL_GCcomb_cov.txt`  
- 12 points: DV/DM/DH over rs at DESI effective redshifts including Lyα  
- Full 12×12 covariance  
- Minimizes χ² over (H0, Om, rd) with **frozen** (w0, wa)
- Same for ΛCDM and paste → Δχ²

## Colab steps
1. New notebook  
2. Paste cells from `colab_desi_official_chi2.py` in order  
3. Run — no cobaya, no classy required  
4. Report the printed χ² table and Δχ²

## Why this is still the official-cov test
Same data vector and covariance Cobaya would use for DESI ALL Gaussian BAO. Only the sampler differs (L-BFGS profile vs MCMC). For a frozen point, profiling (H0, Om, rd) is the correct comparison.

## After it works
Optional later: proper Cobaya with  
`cobaya-install bao.generic -p /content/cobaya_packages`  
and packages_path in YAML — not required for the Δχ² number.
