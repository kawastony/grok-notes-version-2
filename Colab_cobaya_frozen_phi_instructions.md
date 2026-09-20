# Colab Cobaya frozen-φ instructions

Script: use local `colab_cobaya_frozen_phi.py` or copy cells below logic from GitHub artifacts discussion.

## Goal
Freeze \((w_0,w_a)=(-\varphi/2,-1/\varphi)\) and profile background params against **official DESI BAO mean+cov** from [CobayaSampler/bao_data](https://github.com/CobayaSampler/bao_data). Compare χ² to ΛCDM on the same likelihood.

## Cells (order)
0. Runtime note (High-RAM if available)
1. `pip install cobaya getdist classy` (or camb fallback)
2. `git clone` bao_data
3. Set frozen W0, WA; auto-detect ALL mean/cov files
4. Write `frozen_phi_desi.yaml`
5. `cobaya-run frozen_phi_desi.yaml -f`
6. Write + run `lcdm_desi.yaml` control
7. Read `.minimum` files → Δχ²
8. Fallback: scipy χ² if Cobaya param names break
9. Report checklist

## Frozen values (exact)
```
w0 = -0.8090169944
wa = -0.6180339887
```

## Expected issues on Colab
| Issue | Fix |
|-------|-----|
| classy build fails | install camb; change theory block |
| `w0_fld` unknown | check `cobaya-doc classy` for fluid DE names (sometimes `w0_fld`/`wa_fld` under Omega_fld) |
| cov size / quantity labels | open mean file; map DV_over_rs etc. |
| OOM with Planck | **skip Planck on free Colab**; DESI-only is still the official-cov upgrade |
| PPF | enable only if CLASS build supports `use_ppf` |

## Report back
1. chi2_phi, chi2_lcdm, Δχ²  
2. best-fit H0, ω_cdm  
3. any traceback  

DESI-only official cov is the highest-value Colab-reachable step toward the joint posterior wall.
