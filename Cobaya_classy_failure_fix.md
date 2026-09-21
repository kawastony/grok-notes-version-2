# Cobaya CLASS failure fix

## Error
```
Could not find random point giving finite posterior after 100000 tries
[classy] Serious error setting parameters or computing results
```
Both **phi and LCDM** failed → wiring/setup problem, not unphysical frozen-φ.

## Likely causes
1. CLASS fluid DE not configured (`Omega_Lambda` still on; no `use_ppf`)
2. LCDM YAML still passed `w0_fld`/`wa_fld` (wrong)
3. Planck likelihoods not installed → all points non-finite
4. Phantom crossing without PPF aborts CLASS
5. `bao.generic` install path issues on Colab

## Fix strategy (staged)

| Stage | Content | Goal |
|-------|---------|------|
| **0a** | CAMB + LCDM + DESI only | Prove sampler + BAO likelihood work |
| **0b** | CAMB + PPF + frozen φ + DESI only | Prove CPL runs |
| **1** | CLASS + correct fluid flags + DESI only | CLASS path |
| **2** | Add Planck only after 0/1 succeed | True joint |

Script: `colab_cobaya_fixed_yaml.py` writes:
- `stage0_lcdm_desi_camb.yaml`
- `stage0_phi_desi_camb.yaml`
- `stage1_phi_desi_classy.yaml`
- `stage1_lcdm_desi_classy.yaml`

## Key YAML rules
- **LCDM:** no `w`/`wa`/`w0_fld`/`wa_fld` at all
- **CAMB CPL:** `dark_energy_model: DarkEnergyPPF`, params `w`, `wa`
- **CLASS CPL:** `Omega_Lambda: 0`, `w0_fld`, `wa_fld`, `use_ppf: yes`
- **Priors:** tighten H0 60–80, omch2 0.10–0.14 for stage 0
- **Planck:** add only after DESI-only chains produce finite χ²

## If bao.generic still fails install
Keep pure-Python official DESI result (already in hand):
- χ²_φ = 11.78, χ²_Λ = 12.74, Δχ² = −0.96
- Wall 1 joint compressed: Δχ² ≈ −0.08

## Compact statement
Both models crashing means CLASS/YAML setup, not geometry failure. Stage CAMB DESI-only first; enable PPF for φ; never put w0/wa on LCDM; add Planck last.
