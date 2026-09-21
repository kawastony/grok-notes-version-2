# Stage 1 CLASS DESI result + Stage 2 Planck status

Tony Kawas / 21 September 2026.

## Stage 1 — CLASS + official DESI ALL (converged)

| Model | min χ² | H0 | ω_b | ω_cdm |
|-------|--------|-----|------|--------|
| **φ** | **11.778** | 66.80 | 0.0214 | 0.1195 |
| ΛCDM | 12.738 | 67.94 | 0.0211 | 0.1145 |

**Δχ²(φ − ΛCDM) = −0.960**

### Triple confirmation of DESI ALL preference

| Method | Δχ² |
|--------|-----|
| Pure-Python profile | −0.96 |
| Cobaya CAMB MCMC (Stage 0) | −0.95 |
| **Cobaya CLASS MCMC (Stage 1)** | **−0.96** |

Frozen φ is robust on official DESI ALL under two Boltzmann codes.

---

## Stage 2 — CAMB + DESI + full Planck (in progress)

**Good news**
- Planck plik TTTEEE loaded (clipy test: −1172.47 matched)
- lowℓ TT/EE present
- LCDM chain is sampling (5000+ accepted steps in log)

**Issues**
- `blockedproposer: covmat is not positive-definite` (repeated)
- R−1 still high (~5–34) — not yet converged
- Many plik nuisance parameters → slow learning of proposal covariance

**Advice**
1. Let LCDM continue if Colab session holds (hours more may be needed for R−1 < 0.1).
2. If covmat errors persist: restart with `learn_every: 100` or provide a seed covmat from a short DESI-only run; or freeze most plik nuisances at defaults for a faster orientation run.
3. Only start φ Stage 2 after LCDM produces a usable chain / .covmat.
4. For a **fast joint orientation** without full MCMC: profile (H0, ωb, ωc) with pure-Python DESI + compressed Planck (already done: Δχ² ≈ −0.08).

---

## Scoreboard update

| Claim | Status |
|-------|--------|
| Official DESI ALL (3 methods) | **Green** Δχ² ≈ −0.96 |
| CAMB + CLASS agreement | **Green** |
| BAO + Planck compressed | Yellow Δχ² ≈ −0.08 |
| Full plik + DESI MCMC | **In progress** (LCDM sampling) |
| SPARC Level 2 RC | Blocked (site refused from Colab) |
| PPF growth likelihood | Still external |

## Compact statement
Stage 1 CLASS confirms Δχ²(φ−Λ) = −0.96 on DESI ALL. Stage 2 full Planck has loaded successfully and is sampling LCDM; proposal covmat is unstable and convergence is not yet reached. DESI result is locked; joint Planck MCMC is the remaining live cosmology wall.
