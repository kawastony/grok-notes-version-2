# SPARC empirical freeze (authoritative)

**Date:** 2026-09-29
**Estimator:** threshold-crossing r_p on R = g_obs/g_bar
**Sample:** CDS Table1 Q≤2 + Rotmod; N=111 with interior r_p; coverage R_max > 1.2 r_p
**Lattice / Callias:** not used

---

## Catalog quality

| Quantity | Value |
|----------|-------|
| Q≤2 matched | 163 |
| Threshold r_p OK | 111 |
| r_p / R_max median | 0.46 |
| r_p / R_max range | 0.22 – 0.79 |
| Σ_ref (SB_disk median) | 319.76 |
| corr(μ̂, X) | −0.36 |

---

## M0 vs M1 (Gaussian NLL)

| Model | μ_* | S | τ | NLL |
|-------|-----|---|---|-----|
| M0 | 0.208 | — | 0.246 | 1.25 |
| M1 | 0.591 | **−0.345** | 0.230 | −6.42 |
| **ΔNLL(M0−M1)** | | | | **+7.66** |

M1 preferred. Higher X (SB_disk proxy) ↔ larger r_p (smaller μ̂).

Earlier N=78 subsample (same estimator family) gave consistent S≈−0.53 with hierarchical Bayes HDI excluding 0. N=111 is the larger clean sample after corrected Table1 parse.

---

## Post-M1 residual correlation (C_ee vs X)

| Test | max\|C\| | shuffle p (2000) |
|------|---------|------------------|
| All bins | 0.0027 | **0.80** |
| Drop last bin | 0.0024 | **0.74** |

**Residuals after M1 are consistent with white noise** in X.

Earlier marginal p~0.05 on a smaller/subsample was **not** confirmed on the authoritative N=111 catalog; that signal was sparse-bin sensitive and does not survive.

---

## Locked statements

1. Threshold r_p yields interior transitions for N=111.
2. Linear μ = μ_* + S X is preferred over constant μ_* (ΔNLL≈8).
3. S < 0 is stable under this estimator.
4. Post-M1 residuals in X are **white** (shuffle p ≈ 0.8).
5. **M2 structured C_μ is not required** by residual tests.
6. **Lattice / Callias / soft modes are not justified** as residual drivers on raw SPARC with this μ̂.

---

## Next (data order)

1. Optional: hierarchical LOO M0 vs M1 on N=111 (confirm elpd gap).
2. Optional: galaxy-level BTFR residual analysis without r_p.
3. Cosmology: stage0/1/2 LCDM vs frozen-φ chains can be compared independently.
4. Micro / lattice only if a *new* residual observable shows non-white structure on raw SPARC.
