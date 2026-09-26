# Bridge build: SPARC / R_cone / Σ_b^{1/7}

**Date:** 2026-09-26  
**Priority:** Highest near-term empirical bridge (not GR derivation).

## Locked primitives (do not retune)

| Symbol | Value | Origin |
|--------|-------|--------|
| φ | (1+√5)/2 ≈ 1.618034 | simple interpolator at x=1 |
| R_cone | √6 / φ ≈ 1.51387 | activation surface (φ')²=6 |
| a_T | 8.25×10^{-11} m s^{-2} | calibrated disk floor |
| interpolator | g = ½ g_N + √[(½ g_N)² + g_N a_T] | locked package |
| Υ_disk, Υ_bul | 0.5, 0.7 | SPARC 3.6 µm convention |

## Bridge components

### A. R_cone normalization (BTFR / global offset)

Reported effect: multiplying the geometric scale by R_cone shifts SPARC mean velocity residuals from ≈ −0.161 dex (pure a_0) toward ≈ +0.019 dex.

**Operational definition to lock:**

```text
V_model → R_cone-scaled or a_eff scaled by R_cone in the deep-MOND / transition sector
```

Do not refit a_T. Apply R_cone as a fixed amplitude from cone geometry.

### B. Surface-density response Σ_b^{1/7}

Reported law: a_eff ∝ Σ_b^{1/7} with MAE ≈ 0.0586 dex on 135 SPARC galaxies; bootstrap exponent ≈ 0.144 ± 0.060 vs theory 1/7 ≈ 0.1429 (≈ 0.02σ).

**Status:** empirical scaling consistent with 1/7; RG/derivation of exponent is Paper 25 territory — cite, do not invent a new free power.

### C. Forced Prediction B (already closed)

At g_N = a_T:

```text
g_obs / a_T = φ ≈ 1.618
```

Exact for simple interpolator. Stack SPARC near g_bar ≈ a_T; expect median ≈ φ, not 2 (standard MOND μ).

### D. Optional Prediction A (cosmology-linked a_T)

```text
a_T ≟ R_cone · (3 Ω_Λ / 8π) c H_0
```

~1% match at Planck-like H_0; larger tension at H_0 ~ 73. Motivated, not uniquely forced from action variation.

## Build steps (do now)

1. **Freeze protocol** — Υ, a_T, interpolator fixed; no post-hoc retuning.
2. **R_cone residual test** — recompute global BTFR / velocity residual mean with and without R_cone factor; report dex shift.
3. **Prediction B stack** — select SPARC points with g_N within a narrow band of a_T; measure median g_obs/a_T.
4. **Σ_b^{1/7} audit** — if Paper 24/25 tables exist, reproduce MAE and residual correlations vs R_d, M_b.
5. **Document only** — do not claim lattice dS → g_eff(r) theorem.

## Explicitly not this bridge

- Forman → Ricci / Einstein equation
- Soft-subspace G_subspace as galactic force law
- Single-field phantom without PPF/multi-field

## Success criteria

| Check | Pass if |
|-------|--------|
| R_cone residual | mean offset moves toward zero without retuning a_T |
| Prediction B | median g_obs/a_T ≈ φ near transition |
| Σ_b^{1/7} | MAE ~0.06 dex; no strong residual vs size/mass |
| Constitution | no GR claim from lattice geometry |

## One-line program

Build the galaxy bridge from locked cone numbers (R_cone, φ, a_T, simple interpolator) against SPARC observables; keep cosmology and GR as separate, lower-priority tracks.
