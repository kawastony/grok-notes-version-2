# Hardest test: full official Planck + DESI joint at frozen φ

Tony Kawas / 21 September 2026.

## Reality
Full `plik` TTTEEE + lowℓ + DESI is the #1 confidence booster (~70% → ~80% if it passes).
It generally **does not fit** on free Colab (install size + MCMC memory).

## What we ship

| Path | What | Where |
|------|------|-------|
| **C (true wall)** | Cobaya YAML with plik + lowℓ + DESI ALL | Cluster / local with packages |
| **B (done)** | DESI ALL + Planck compressed | Colab — Δχ² ≈ −0.08 |
| **A (optional)** | Attempt cobaya-install on Colab | Often OOM |

Script: `colab_hardest_planck_desi.py` writes:
- `/content/frozen_phi_planck_desi.yaml`
- `/content/lcdm_planck_desi.yaml`

## Cluster commands (Path C)
```bash
git clone https://github.com/CobayaSampler/bao_data.git
export COBAYA_PACKAGES_PATH=./packages
cobaya-install planck_2018_highl_plik.TTTEEE planck_2018_lowl.TT planck_2018_lowl.EE -p ./packages
# edit YAML paths to bao_data mean/cov
cobaya-run frozen_phi_planck_desi.yaml -p ./packages
cobaya-run lcdm_planck_desi.yaml -p ./packages
# compare .minimum chi2
```

Enable PPF in CLASS if available (`use_ppf: true`) for phantom crossing.

## Decision tree on Δ = χ²_φ − χ²_Λ

| Δ | Action |
|---|--------|
| ≤ 0 | Cosmology → green; next RC fixed-R + PPF |
| 0–5 | Competitive; diagnose drivers; still do RC + PPF |
| > 5 | Tension; do not retune (w₀,w_a); galaxy/micro remain independent value |
| Run fails | Keep Wall 1 (Δ≈−0.08) as best orientation; move to cluster |

## Current scoreboard (unchanged until Path C returns)

| Claim | Color |
|-------|-------|
| Identities, DESI BAO, R_cone norm | Green |
| BAO+Planck compressed, growth fluid, dual bridge, micro recipe | Yellow |
| Full Planck joint, PPF, full RC, micro→macro | Red |

## Compact statement
The hardest test is full plik+DESI at frozen φ. YAML is ready for a machine that can install Planck likelihoods. Colab best proxy remains Wall 1 (Δχ²≈−0.08). Decision tree above governs next moves once Path C returns a number.
