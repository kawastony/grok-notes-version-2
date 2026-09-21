# Next walls — instructions

Script: `colab_next_walls.py`

## Wall order

| # | Wall | Method | Colab? |
|---|------|--------|--------|
| 1 | **Planck compressed + DESI ALL** | R, l_A, ω_b prior + official 12×12 BAO | **Yes** |
| 2 | **fσ8 orientation** | Fluid growth vs published points | **Yes** |
| 3 | Full Planck plik | Cobaya + Planck likelihoods | Cluster |
| 4 | Pantheon+ full cov | Large matrix | Heavy Colab |
| 5 | PPF growth | CLASS `use_ppf` | Cluster/local |

## Run Wall 1+2 on Colab
1. New notebook  
2. Copy cells from `colab_next_walls.py`  
3. Report:
   - joint χ² table (phi / lcdm / paste)
   - Δχ² joint vs LCDM
   - fσ8 pulls / chi2_fs8

## Caveats (honest)
- Planck compressed prior is **approximate** (diagonal σ; rd↔r_s(z*) factor). Orientation-grade, not publication-grade.
- fσ8 uses fixed σ₈=0.81 and fluid equations (no PPF). Orientation only.
- Full plik + Pantheon+ + PPF remain the true remaining walls.

## After Wall 1+2
If joint Δχ² stays O(1) or negative → geometry survives compressed CMB+DESI.  
Then escalate to full Planck only if resources allow.
