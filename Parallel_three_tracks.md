# Three tracks in parallel

Tony Kawas / 21 September 2026.

Stage 0 CAMB DESI is **done** (Δχ² = −0.95). Run these three independently.

---

## Track A — Stage 1 CLASS + DESI only

**Script:** `colab_stage1_classy_desi.py`

```
!python -m cobaya.run /content/stage1_lcdm_desi_classy.yaml -f
!python -m cobaya.run /content/stage1_phi_desi_classy.yaml -f
```

- Phi: `Omega_Lambda: 0`, `use_ppf: yes`, frozen w0_fld/wa_fld
- LCDM: no w parameters
- Expect Δχ² ≈ −0.95 if CLASS agrees with CAMB
- If CLASS crashes on phi → keep Stage 0 CAMB as BAO authority

---

## Track B — Stage 2 CAMB + DESI + Planck

**Script:** `colab_stage2_camb_planck_desi.py`

```
export COBAYA_PACKAGES_PATH=/content/packages
python -m cobaya.install planck_2018_highl_plik.TTTEEE planck_2018_lowl.TT planck_2018_lowl.EE -p /content/packages
# then uncomment Planck in YAML and run
```

- **Risk:** free Colab often OOM on Planck install
- If install fails: Wall 1 compressed (Δχ² ≈ −0.08) remains best CMB proxy
- Prefer CAMB over CLASS for Stage 2 (Stage 0 already proved CAMB stable)

---

## Track C — Galaxy fixed-R_cone

**Script:** `colab_galaxy_Rcone_RC_path.py`

| Level | Content | Status |
|-------|---------|--------|
| 1 | SPARC Table1 BTFR, R fixed | **Done** (mean res +0.019 dex) |
| 2 | Full rotmod V(R) residuals | Needs SPARC mass-model files |
| 3 | Report mean/rms, no free R | After Level 2 |

Level 1 already shows R_cone removes global offset; free slope ≈ 3.56 explains residual V-trend.

---

## Report back template

```
Track A: chi2_phi=... chi2_lcdm=... Delta=...
Track B: installed? yes/no; if yes Delta=...
Track C: Level1 confirmed; rotmod available? yes/no
```

## Priority if only one finishes
1. Track A (quick confirmation)
2. Track C Level1 already banked
3. Track B only if Planck packages install cleanly
