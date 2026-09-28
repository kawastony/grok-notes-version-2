# SPARC empirical freeze: threshold r_p + M0/M1 + residuals

**Estimator:** threshold-crossing r_p on R(r)=g_obs/g_bar; Q≤2; coverage R_max > 1.2 r_p.
**N = 78.** Lattice / Callias not used.

---

## r_p quality

| Quantity | Value |
|----------|-------|
| r_p / R_max mean | 0.463 |
| median | 0.464 |
| range | 0.234 – 0.781 |
| Outer 20% fraction | low (threshold design) |
| Bound-hit logistic (for comparison) | only 17/52 interior — rejected |

---

## M0 vs M1 (Gaussian NLL on mu_hat_thr)

| Model | μ_* | S | τ | NLL |
|-------|-----|---|---|-----|
| M0 | 0.2236 | — | 0.3061 | 17.85 |
| M1 | 0.8079 | −0.5374 | 0.2783 | 9.92 |
| **ΔNLL(M0−M1)** | | | | **+7.93** |

Bootstrap S (2000 resamples): 16/50/84% = **[−0.702, −0.528, −0.387]** — HDI excludes 0.

---

## Hierarchical Bayes M1 (PyMC)

| Parameter | mean | sd | 94% HDI |
|-----------|------|-----|---------|
| mu_star | 0.801 | 0.146 | [0.53, 1.07] |
| S | −0.532 | 0.131 | [−0.78, −0.29] |
| tau | 0.283 | 0.024 | [0.24, 0.33] |

r_hat ≈ 1.0; ESS bulk ≳ 1200. Matches frequentist MLE.

**Note:** One paste block also quoted logistic N=50 M0/M1 (S≈−1.38). That estimator is bound-dominated and **not** part of this freeze. Authoritative sample is threshold N=78.

---

## Residual correlation after M1

| Coordinate | max\|C\| | shuffle p (2000–5000) | Notes |
|------------|---------|------------------------|-------|
| X | 0.036 | **~0.047** | Driven largely by widest bin (dX≈1.05, n_pairs=12) |
| log10(SB_disk) | 0.013 | ~0.23 | Consistent with white |

Interpretation: **marginal** residual structure in X after linear M1; **not** significant vs SB_disk. Treat M2 as exploratory, not required.

---

## Locked empirical statements (this estimator only)

1. Threshold r_p yields interior transitions for N=78.
2. M1 preferred over M0 (ΔNLL≈8; Bayesian HDI on S excludes 0).
3. S < 0: higher X (SB_disk proxy) ↔ larger r_p (smaller μ̂).
4. Post-M1 residuals vs X: borderline non-white (p~0.05); sensitive to sparse outer bins.
5. Lattice / Callias not used; not justified as residual drivers yet.

---

## Next (data order)

1. Build analysis table from official SPARC Table1 + Rotmod (Q≤2).
2. Hierarchical M0/M1/M4 on threshold or latent-r_p μ̂.
3. Residual C_ee / C_μ + shuffle; optional M2 if structure robust to binning.
4. Lattice features only if residual non-whiteness survives on raw SPARC.
