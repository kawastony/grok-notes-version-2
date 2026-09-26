# Latent-r_p hierarchical model (next SPARC protocol)

Replaces fragile per-galaxy max-slope point estimates with a population model where each galaxy has a **latent** transition scale.

---

## Why

Local derivative search fails when coverage is short, residuals noisy, transition broad, or the edge dominates. Hierarchical latent inference treats short disks as **weakly informative / censored** rather than forcing r_p = R_max.

---

## Core structure

**Profile (galaxy i, radius j):**
\[
\mathcal R_i(r)=1+A_i\,F\!\left(\frac{r}{r_{p,i}},w_i\right),
\qquad
\mathcal R_{ij}^{\rm obs}\sim\mathcal N\bigl(\mathcal R_i(r_{ij}),\sigma_{ij}^2+\sigma_{\rm int}^2\bigr).
\]

**Monotone F family (start simple):**
\[
F(x,w)=\frac{1}{1+e^{-(x-1)/w}}
\quad\text{(logistic)},
\]
or arctan / smooth broken-power alternatives for robustness checks.

**Population for inverse-radius:**
\[
\mu_i\equiv\frac{1}{r_{p,i}},
\qquad
\mu_i\sim\mathcal N(\mu_*+S X_i,\,\tau_\mu^2).
\]

**X_i (first pass):** one characteristic Σ_b per galaxy (central / effective / mean inner).  
**Later:** X_i=(Σ_b(r_{p,i})/Σ_ref)^{1/7} with interpolation (harder, more aligned).

Optional: S_i ~ N(S_0, τ_S²) for galaxy-varying dressing.

---

## Hypotheses to compare

| Model | Structure |
|-------|-----------|
| H1 universal intercept + dressing | μ_i ~ N(μ_* + S X_i, τ_μ²) |
| Null no dressing | μ_i ~ N(μ_*, τ_μ²) |
| Null free intercepts | effectively per-galaxy μ_{*,i} |
| Null free exponent | X_i = (Σ_b/Σ_ref)^p with p free |

Success: H1 preferred; τ_μ small; μ_* stable across HSB/LSB/dwarf class splits.

---

## Role of ~12.1 kpc

- **Not** built into the likelihood as a hard cut that then “recovers” itself.
- **Allowed:** external benchmark — fit μ_* freely, then compare posterior to 1/(12.1 kpc) if that value is independently motivated.
- **Allowed:** soft prior only if pre-registered and sensitivity-checked against flat prior.

---

## Implementation path

1. Stage 1: common μ_*, S, τ_μ; logistic F; one X_i per galaxy; PyMC/Stan/NumPyro.
2. Stage 2: keep short-coverage galaxies (posterior on r_{p,i} becomes one-sided).
3. Stage 3: class offsets δ_class; test consistency with zero.

**Minimal first model only** — no full complexity up front.

---

## Status

Methodological upgrade over point-estimate pipeline. Not yet run on real SPARC (no catalog in this environment). Ready for implementation when prepared tables exist.
