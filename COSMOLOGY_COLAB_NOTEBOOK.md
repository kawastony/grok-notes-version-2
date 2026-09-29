# TAFA cosmology Colab notebook — ΛCDM vs frozen-φ

**Order (do not reorder):**  
Install → write YAMLs → Stage 0 (DESI) → **save to Drive** → Stage 1 (Planck) → **save** → Stage 2 (Planck+DESI) → **save** → GetDist compare

**Frozen-φ point:**  
`w0 = -0.8090169943749475`, `wa = -0.6180339887498948`

**Rules**
1. Never run GetDist before chain `.txt` files exist.
2. Always save to Drive after each `Sampling complete`.
3. If runtime dies → restore from Drive, continue next unfinished stage.
4. Do not use `--force` unless you intend to delete chains.
5. SPARC analysis is a separate notebook; this is cosmology only.

---

## Cell 0 — mount Drive first

```python
from google.colab import drive
drive.mount("/content/drive")
!mkdir -p "/content/drive/MyDrive/tafa_chains"
print("Drive ready: /content/drive/MyDrive/tafa_chains")
```

---

## Cell 1 — install Cobaya stack

```python
!pip -q install cobaya getdist camb
```

```python
!cobaya-install camb \
  planck_2018_lowl.TT planck_2018_lowl.EE \
  planck_2018_highl_plik.TTTEEE_lite_native \
  planck_2018_lensing.native \
  bao.generic \
  --path /content/packages
```

```python
import os
print("CAMB:", os.path.isdir("/content/packages/code/CAMB"))
print("BAO:", os.path.isdir("/content/packages/data/bao_data"))
os.makedirs("/content/chains", exist_ok=True)
print("chains dir ready")
```

**Do not** symlink over `/content/packages/data/bao_data`.

---

## Cell 2 — write all six YAML configs

```python
import os

W0 = -0.8090169943749475
WA = -0.6180339887498948
PACK = "/content/packages"
OUT = "/content/chains"
os.makedirs(OUT, exist_ok=True)

CAMB_LCDM = """
theory:
  camb:
    extra_args:
      lens_potential_accuracy: 1
      num_massive_neutrinos: 1
      nnu: 3.044
"""

LIK_PLANCK = """
likelihood:
  planck_2018_lowl.TT: null
  planck_2018_lowl.EE: null
  planck_2018_highl_plik.TTTEEE_lite_native: null
  planck_2018_lensing.native: null
"""

LIK_DESI = """
likelihood:
  bao.generic:
    measurements_file: data/bao_data/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
    cov_file: data/bao_data/desi_2024_gaussian_bao_ALL_GCcomb_cov.txt
"""

LIK_PLANCK_DESI = """
likelihood:
  planck_2018_lowl.TT: null
  planck_2018_lowl.EE: null
  planck_2018_highl_plik.TTTEEE_lite_native: null
  planck_2018_lensing.native: null
  bao.generic:
    measurements_file: data/bao_data/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
    cov_file: data/bao_data/desi_2024_gaussian_bao_ALL_GCcomb_cov.txt
"""

SAMPLER = """
sampler:
  mcmc:
    Rminus1_stop: 0.05
    Rminus1_cl_stop: 0.2
    learn_proposal_Rminus1_max: 30
    max_tries: 10000
    burn_in: 20
"""

def write(name, body):
    path = f"/content/{name}.yaml"
    with open(path, "w") as f:
        f.write(body)
    print("Wrote", path)

def params_block(with_aplanck=False, with_w=False):
    lines = [
        "params:",
        "  logA:",
        "    prior: {min: 2.5, max: 3.5}",
        "    ref: {dist: norm, loc: 3.05, scale: 0.001}",
        "    proposal: 0.001",
        r"    latex: \ln(10^{10} A_\mathrm{s})",
        "    drop: true",
        "  As:",
        '    value: "lambda logA: 1e-10*np.exp(logA)"',
        r"    latex: A_\mathrm{s}",
        "  ns:",
        "    prior: {min: 0.8, max: 1.2}",
        "    ref: {dist: norm, loc: 0.965, scale: 0.004}",
        "    proposal: 0.002",
        r"    latex: n_\mathrm{s}",
        "  theta_MC_100:",
        "    prior: {min: 0.5, max: 10}",
        "    ref: {dist: norm, loc: 1.041, scale: 0.0004}",
        "    proposal: 0.0002",
        r"    latex: 100\theta_\mathrm{MC}",
        "    drop: true",
        "    renames: theta",
        "  cosmomc_theta:",
        '    value: "lambda theta_MC_100: 1.e-2*theta_MC_100"',
        "    derived: false",
        "  ombh2:",
        "    prior: {min: 0.005, max: 0.1}",
        "    ref: {dist: norm, loc: 0.0224, scale: 0.0001}",
        "    proposal: 0.0001",
        r"    latex: \Omega_\mathrm{b} h^2",
        "  omch2:",
        "    prior: {min: 0.001, max: 0.99}",
        "    ref: {dist: norm, loc: 0.12, scale: 0.001}",
        "    proposal: 0.0005",
        r"    latex: \Omega_\mathrm{c} h^2",
        "  tau:",
        "    prior: {min: 0.01, max: 0.8}",
        "    ref: {dist: norm, loc: 0.055, scale: 0.006}",
        "    proposal: 0.003",
        r"    latex: \tau_\mathrm{reio}",
    ]
    if with_aplanck:
        lines += [
            "  A_planck:",
            "    prior: {min: 0.9, max: 1.1}",
            "    ref: {dist: norm, loc: 1.0, scale: 0.002}",
            "    proposal: 0.0005",
            r"    latex: A_\mathrm{planck}",
        ]
    if with_w:
        lines += [
            f"  w:",
            f"    value: {W0}",
            f"  wa:",
            f"    value: {WA}",
        ]
    lines += [
        "  H0:",
        r"    latex: H_0",
        "  omegam:",
        r"    latex: \Omega_\mathrm{m}",
        "  sigma8:",
        r"    latex: \sigma_8",
    ]
    return "\n".join(lines) + "\n"

CAMB_PHI = """
theory:
  camb:
    extra_args:
      lens_potential_accuracy: 1
      num_massive_neutrinos: 1
      nnu: 3.044
      dark_energy_model: ppf
"""

write("stage0_lcdm_desi", f"""
output: {OUT}/stage0_lcdm_desi
packages_path: {PACK}
{CAMB_LCDM}
{params_block(with_aplanck=False, with_w=False)}
{LIK_DESI}
{SAMPLER}
""")

write("stage0_phi_desi", f"""
output: {OUT}/stage0_phi_desi
packages_path: {PACK}
{CAMB_PHI}
{params_block(with_aplanck=False, with_w=True)}
{LIK_DESI}
{SAMPLER}
""")

write("stage1_lcdm_planck", f"""
output: {OUT}/stage1_lcdm_planck
packages_path: {PACK}
{CAMB_LCDM}
{params_block(with_aplanck=True, with_w=False)}
{LIK_PLANCK}
{SAMPLER}
""")

write("stage1_phi_planck", f"""
output: {OUT}/stage1_phi_planck
packages_path: {PACK}
{CAMB_PHI}
{params_block(with_aplanck=True, with_w=True)}
{LIK_PLANCK}
{SAMPLER}
""")

write("stage2_lcdm_planck_desi", f"""
output: {OUT}/stage2_lcdm_planck_desi
packages_path: {PACK}
{CAMB_LCDM}
{params_block(with_aplanck=True, with_w=False)}
{LIK_PLANCK_DESI}
{SAMPLER}
""")

write("stage2_phi_planck_desi", f"""
output: {OUT}/stage2_phi_planck_desi
packages_path: {PACK}
{CAMB_PHI}
{params_block(with_aplanck=True, with_w=True)}
{LIK_PLANCK_DESI}
{SAMPLER}
""")

print("Frozen-φ: w0 =", W0, " wa =", WA)
!ls -la /content/stage*.yaml
```

If BAO path fails:

```python
!ls /content/packages/data/bao_data/*.txt | head
```

---

## Cell 3 — save chains to Drive (run after EVERY stage)

```python
def save_chains_to_drive():
    from google.colab import drive
    import os, shutil
    drive.mount("/content/drive", force_remount=False)
    dest = "/content/drive/MyDrive/tafa_chains"
    os.makedirs(dest, exist_ok=True)
    src = "/content/chains"
    n = 0
    for fn in os.listdir(src):
        s = os.path.join(src, fn)
        d = os.path.join(dest, fn)
        if os.path.isfile(s):
            shutil.copy2(s, d)
            n += 1
    print(f"Copied {n} files → {dest}")
    !ls "{dest}" | head -30

save_chains_to_drive()
```

---

## Cell 4 — Stage 0a: ΛCDM DESI

```python
!cobaya-run /content/stage0_lcdm_desi.yaml -p /content/packages
```

When you see `Sampling complete` → **run Cell 3**.

```python
import glob
print("stage0_lcdm files:", len(glob.glob("/content/chains/stage0_lcdm_desi*")))
```

---

## Cell 5 — Stage 0b: φ DESI

```python
!cobaya-run /content/stage0_phi_desi.yaml -p /content/packages
```

→ **run Cell 3**.

```python
import glob
print("stage0_phi files:", len(glob.glob("/content/chains/stage0_phi_desi*")))
```

---

## Cell 6 — Stage 1a: ΛCDM Planck

```python
!cobaya-run /content/stage1_lcdm_planck.yaml -p /content/packages
```

→ **run Cell 3**.

---

## Cell 7 — Stage 1b: φ Planck

```python
!cobaya-run /content/stage1_phi_planck.yaml -p /content/packages
```

→ **run Cell 3**.

---

## Cell 8 — Stage 2a: ΛCDM Planck+DESI

```python
!cobaya-run /content/stage2_lcdm_planck_desi.yaml -p /content/packages
```

→ **run Cell 3**.

---

## Cell 9 — Stage 2b: φ Planck+DESI

```python
!cobaya-run /content/stage2_phi_planck_desi.yaml -p /content/packages
```

→ **run Cell 3**.

---

## Cell 10 — restore from Drive (if runtime died)

```python
from google.colab import drive
import os, shutil, glob
drive.mount("/content/drive")
os.makedirs("/content/chains", exist_ok=True)
src = "/content/drive/MyDrive/tafa_chains"
for fn in os.listdir(src):
    shutil.copy2(os.path.join(src, fn), os.path.join("/content/chains", fn))
print("Restored", len(glob.glob("/content/chains/*")), "files")
!ls /content/chains | head
```

---

## Cell 11 — GetDist comparison

```python
import glob
from getdist import loadMCSamples
import getdist.plots as plots

CHAINS = "/content/chains"

def load(prefix, ignore=0.3):
    files = glob.glob(f"{CHAINS}/{prefix}*")
    print(prefix, "→", len(files), "files")
    if not files:
        raise FileNotFoundError(f"No chains for {prefix}. Restore from Drive or re-run MCMC.")
    return loadMCSamples(f"{CHAINS}/{prefix}", settings={"ignore_rows": ignore})

pairs = [
    ("stage0_lcdm_desi", "stage0_phi_desi", "DESI-only"),
    ("stage1_lcdm_planck", "stage1_phi_planck", "Planck-only"),
    ("stage2_lcdm_planck_desi", "stage2_phi_planck_desi", "Planck+DESI"),
]

for lcdm_p, phi_p, label in pairs:
    try:
        s_l = load(lcdm_p)
        s_p = load(phi_p)
        print(f"\n=== {label} ===")
        for name, s in [("ΛCDM", s_l), ("φ", s_p)]:
            print(f"  {name}:")
            for p in ["H0", "omegam", "sigma8", "ns", "ombh2", "omch2"]:
                if p in s.paramNames.list():
                    print(f"    {s.getInlineLatex(p, limit=1)}")
        g = plots.get_subplot_plotter()
        g.triangle_plot(
            [s_l, s_p],
            [p for p in ["H0", "omegam", "sigma8"] if p in s_l.paramNames.list()],
            legend_labels=["ΛCDM", "φ"],
        )
    except Exception as e:
        print(label, "SKIP:", e)
```

---

## Checklist

| Step | Action | Saved to Drive? |
|------|--------|-----------------|
| 0 | Mount Drive | — |
| 1 | Install Cobaya/CAMB/Planck/BAO | — |
| 2 | Write 6 YAMLs | — |
| 4 | stage0_lcdm_desi until Sampling complete | ☐ Cell 3 |
| 5 | stage0_phi_desi | ☐ Cell 3 |
| 6 | stage1_lcdm_planck | ☐ Cell 3 |
| 7 | stage1_phi_planck | ☐ Cell 3 |
| 8 | stage2_lcdm_planck_desi | ☐ Cell 3 |
| 9 | stage2_phi_planck_desi | ☐ Cell 3 |
| 11 | GetDist compare | — |

---

## Related notes in this repo

- `SPARC_M1_RESIDUAL_FREEZE.md` — SPARC threshold r_p M1 preferred; post-M1 residuals white; lattice parked
- `SPARC_THRESHOLD_M1_EMPIRICAL.md` — earlier empirical freeze
