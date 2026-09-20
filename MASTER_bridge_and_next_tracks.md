# Master bridge note + Track A/B status

Tony Kawas / 20 September 2026.

**Override rule:** Notes microscopic geometry supersedes paper micro-geometry on conflict (especially origins of R and 11/72).

---

## PART I — Explicit bridge map (Track B4)

One document, same notation, all scales.

### Primitives (accepted spine)

| Symbol | Value / meaning | Origin |
|--------|-----------------|--------|
| \(\varphi\) | \((1+\sqrt5)/2\) | Simple interpolator at \(x=g_N/a_T=1\): \(\nu=\tfrac12+\sqrt{5/4}=\varphi\) |
| \((\varphi')^2\) | 6 | Activation surface definition |
| \(\sqrt6\) | \(\approx2.44949\) | From \((\varphi')^2=6\) |
| \(\Delta y\) | \(\approx0.2445\,f/\Lambda^2\) | 5D integration (notes) |

### Exact identities (arithmetic once primitives accepted)

\[
\boxed{R_{\rm cone}=\frac{\sqrt6}{\varphi}\approx1.513867916}
\]
\[
\boxed{w_0=-\frac{\varphi}{2},\quad w_a=-\frac1{\varphi}}
\]
\[
\boxed{z_{\rm cross}=\frac1{\sqrt5}\approx0.447213595}\quad(w=-1)
\]
\[
(11/72)_{\rm cone}:=\frac{\Delta y}{\varphi}\approx0.15111\quad(\text{accounting, }\sim1\%\text{ vs }11/72)
\]

### What is exact vs empirical vs open

| Item | Class |
|------|-------|
| \(R_{\rm cone}=\sqrt6/\varphi\) | **Exact** (given primitives) |
| \((w_0,w_a)=(-\varphi/2,-1/\varphi)\) | **Exact** φ-lock (geometric DE path) |
| \(z_{\rm cross}=1/\sqrt5\) | **Exact** |
| \((11/72)_{\rm cone}=\Delta y/\varphi\) | **Accounting** (Δy numerical) |
| Stage 1–2 cosmology survival | **Empirical** (approx pipeline) |
| SPARC BTFR mean residual → ~0 with \(R\times a_0\) | **Empirical** |
| Callias Index\((D)=N_{\rm def}\) continuum | **Open** |
| κ in chiral term | **Open** |
| Full RC law from micro | **Open** |
| Official Cobaya joint posterior | **Open** (external) |
| PPF growth likelihood | **Open** (external) |

### Bridge diagram

```
Cone primitives (φ, (φ')²=6, Δy)
        │
        ├──► R_cone = √6/φ  ──► BTFR normalization (SPARC tested)
        │
        ├──► (w0,wa)=(-φ/2,-1/φ) ──► frozen DE (Stage 1–2 tested)
        │         └──► z_cross=1/√5
        │
        └──► (11/72)_cone = Δy/φ  (accounting; retires 10D dictionary)

Micro lattice (hedgehog, Index, H, inflow)
        │
        └──► orientation / identity  (not yet mapped to R or w0,wa)
```

**Honest statement:** Same geometric family organizes DE and the galactic normalization. The **derivation** micro → both macro laws is not a closed theorem. Cosmology and BTFR give empirical viability at both ends.

---

## PART II — Paper vs notes overrides (Track B5)

| Quantity | Old paper language | Notes override |
|----------|-------------------|----------------|
| Origin of R ≈ 1.5156 | 10D dictionary / warped-volume Jacobian | **\(R_{\rm cone}=\sqrt6/\varphi\)** |
| Origin of 11/72 | 10D quantized asymptotic slope | **\((11/72)_{\rm cone}=\Delta y/\varphi\)** |
| All other TAFA geometry, floors, SPARC protocols | Unchanged | Unchanged |

**Action:** Anywhere papers still treat R or 11/72 as independent UV inputs from a 10D dictionary, replace with cone accounting. Do not rewrite entire papers; correct the bookkeeping origin.

---

## PART III — Fixed-R_cone residual campaign (Track A3, BTFR level)

Sample: SPARC Q=1, i>30°, Vf>0, N=83, Υ*=0.5.
Deep-regime: \(V^4=G a_{\rm eff} M_{\rm bar}\).

| Scale | mean residual | rms |
|-------|---------------|-----|
| pure a₀ | −0.161 dex | 0.247 |
| **R_cone × a₀** | **+0.019 dex** | 0.247 |

**New detail (velocity split):**
- Low-V half: mean residual +0.095 dex
- High-V half: mean residual −0.056 dex
- corr(log V, residual_R) = **−0.40**

**Interpretation:** R_cone removes the **global** mean offset. A residual velocity trend remains (~0.15 dex across the sample). Pure intercept shift is not the whole story; slope ≈3.6 (free fit) vs assumed 4 contributes. Full galaxy-by-galaxy RC residuals require SPARC rotmod files (not loaded here).

**Verdict:** Bridge viable as normalization; **not** yet proven as a complete galactic law.

---

## PART IV — What this environment cannot run (Track A1, A2)

### Official cosmology joint (highest external priority)
Requires Cobaya + CLASS + DESI joint BAO covariance + Planck likelihood.

**Ready recipe (for local/Colab/cluster):**
```python
# Pseudocode — install cobaya, classy, desi bao likelihoods
info = {
  "theory": {"classy": {"path": "..."}},
  "likelihood": {
    "bao.desi_2024_bao_all": None,   # or desi_dr1 files from CobayaSampler/bao_data
    "planck_2018_highl_plik.TTTEEE": None,
    "planck_2018_lowl.TT": None,
    "planck_2018_lowl.EE": None,
    # + sn.pantheonplus if available
  },
  "params": {
    "w0": {"value": -0.8090169944, "prior": None},  # FROZEN
    "wa": {"value": -0.6180339887, "prior": None},  # FROZEN
    "H0": {"prior": {"min": 50, "max": 90}},
    "omega_b": {"prior": {...}},
    "omega_cdm": {"prior": {...}},
    # standard nuisances
  },
  "sampler": {"mcmc": {"Rminus1_stop": 0.01}}
}
```
Compare χ² at frozen F vs ΛCDM and vs free CPL. Report Δχ²(F−Λ) and posterior of free params only.

### PPF + growth
CLASS with `use_ppf = yes` (or equivalent) for CPL across w=−1; then fσ₈ likelihood (e.g. RSD compilations). Linear-fluid result already shows ≲2.5% difference from ΛCDM; PPF is the proper crossing treatment.

### Micro Index closure (Track B6)
Sharp deliverable: residual-gated spectral-flow or soft-mode count vs N_def on L≥12, multiple charges, continuum extrapolation. Lattice evidence exists; continuum theorem does not.

---

## PART V — Priority order if resources limited

| Rank | Item | Where |
|------|------|-------|
| 1 | Official Cobaya joint at frozen F | External pipeline |
| 2 | SPARC RC residuals with R fixed | Needs rotmod; BTFR level done here |
| 3 | PPF growth + fσ₈ | External (CLASS) |
| 4 | Master bridge (this note) | **Done** |
| 5 | Overrides documented | **Done** |
| 6 | Lattice Index robust | Colab/cluster numerics |

---

## Compact status

- **Bridge note:** written; exact vs empirical vs open listed.
- **Overrides:** cone accounting supersedes 10D dictionary for R and 11/72.
- **SPARC:** R_cone kills mean BTFR offset; velocity-dependent residual remains (corr −0.4).
- **Official cosmology + PPF:** recipes only; not executable in this sandbox.
- **Micro:** Index≈N_def remains the sharp closure target.
