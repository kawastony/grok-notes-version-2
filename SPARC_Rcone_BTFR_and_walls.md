# Priority c → b → a: SPARC R_cone, PPF growth, official joint

Tony Kawas / 20 September 2026.

---

## (c) SPARC BTFR with fixed R_cone — DONE

### Sample
- SPARC Table 1 (Lelli+2016), N=175 parsed
- Cuts: **Q=1, i>30°, V_f>0** → **N=83**
- Υ_*=0.5 at 3.6 μm; M_bar = Υ_* L_[3.6] + 1.33 M_HI

### Free BTFR fit
\[
\log_{10} M_{\rm bar} = 2.51 + 3.60\,\log_{10} V_f
\]
(slope consistent with literature ~3.5–3.9 depending on estimator)

### Deep-regime (slope-4) acceleration scale
Using \(V^4 = G\,a_{\rm eff}\,M_{\rm bar}\):

| Model | a_eff [(km/s)²/kpc] | mean residual (dex) | rms (dex) |
|-------|---------------------|---------------------|-----------|
| pure a₀ (=3600) | 3600 | **−0.161** | 0.247 |
| **R_cone × a₀** | **5450** | **+0.019** | 0.247 |
| best-fit a_eff | 5208 | ~0 | 0.247 |

\[
R_{\rm cone}=\sqrt6/\varphi \approx 1.51387
\]
\[
a_{\rm best}/a_0 \approx 1.45 \quad\text{(data preferred)}
\]
\[
R_{\rm cone}\text{ vs data preferred: relative difference }\sim 4\%
\]

**Key result:** Inserting R_cone shifts the mean residual from −0.16 dex to **+0.019 dex** (essentially zero mean offset). Scatter is unchanged (as expected for a pure normalization shift). Data prefer a factor ~1.45; R_cone predicts 1.51 — **agreement at the ~4% level** on the normalization, with R_cone slightly high relative to this Υ_*=0.5 choice.

### Caveats
- Υ_* choice moves the intercept; Υ_*=0.5 is standard but not unique.
- Slope is not exactly 4 (free fit ~3.6); deep-regime assumption is approximate for the full sample.
- This is a **normalization test**, not a full RC fit galaxy-by-galaxy.
- Alternate bridge form \(v_\infty^4=G R m_1^2 M_{\rm bar}\) needs explicit m₁ definition to be distinguished from a₀ rescaling.

**Verdict for (c):** R_cone is **empirically viable** as a BTFR normalization on SPARC Q=1. It largely removes the mean offset left by pure a₀. Not a precision confirmation of the micro derivation, but the bridge is no longer purely theoretical.

---

## (b) PPF growth — STATUS

### Already computed (linear GR fluid)
f_φ / f_ΛCDM within **≲2.5%** across z=0–1.4 at fixed Ω_m and σ₈ today.

### PPF layer
Hu–Sawicki PPF matches DE perturbations across |1+w| small, removing the formal singularity at phantom crossing. Background H(z) unchanged; growth correction is localized near z_c≈0.45 and is expected to be small for CPL parameters of this magnitude.

**Not run:** full CLASS/CAMB + PPF + fσ₈ likelihood.  
**Expectation:** no large shift relative to the linear-fluid result already in hand.  
**Remaining risk:** gradient instability if a single-field micro completion is forced without PPF/quintom.

**Verdict for (b):** Growth wall partially addressed; formal PPF Boltzmann run still required for closure.

---

## (a) Official joint posterior — STATUS

Stage-2 approximate pipeline (CC + DESI summaries + Pantheon+ STAT+SYS + approx Planck prior) already shows frozen φ preferred (Δχ²≈−3 to −4). Full DESI joint covariance + validated Planck likelihood in Cobaya/CLASS is **not executed in this environment**.

**Verdict for (a):** Indication only; official joint is the remaining data wall.

---

## Priority scoreboard

| Priority | Item | Result |
|----------|------|--------|
| **c** | SPARC BTFR + R_cone | **Mean residual → ~0; R vs data ~4%** |
| **b** | PPF growth | Linear OK (~2%); PPF Boltzmann pending |
| **a** | Official joint | Stage-2 favorable; Cobaya pending |

---

## Compact statement

On SPARC Q=1 (N=83, Υ_*=0.5), fixing the deep-regime scale to R_cone×a₀ reduces the mean BTFR residual from −0.16 dex to +0.019 dex. The data-preferred scale factor is ~1.45 versus R_cone=1.51 (~4% high). The galaxy bridge is empirically viable at the normalization level. Growth remains compatible with ΛCDM at the few-percent level under a linear fluid treatment; official joint cosmology and full PPF Boltzmann runs are the remaining external walls.
