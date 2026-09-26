# SPARC bootstrap constraints (Paper 24)

## Reported bootstrap

- Method: 500 resamples
- Result: γ = 0.144 ± 0.060 (1σ)
- Best-fit point estimate: γ_fit = 0.1463
- Theory 1/7 ≈ 0.1429: **0.02σ** from bootstrap mean

## What the error bar allows

| γ | Allowed at 1σ? | Comment |
|---|----------------|---------|
| 1/7 ≈ 0.1429 | Yes | Near center |
| 0.156 (ν₀=2.31 chain) | Yes | ~0.2σ from mean |
| 0.161 (ν₀=2.371 pure) | Yes | ~0.3σ |
| 1/6 ≈ 0.1667 | Yes | Still inside |
| 1/8 = 0.125 | Yes | Inside |
| 1/5 = 0.20 | Marginal | ~0.9σ |
| 1/2 (deep MOND-like Σ^{1/2}) | **No** | ~6σ out |
| 0 (no Σ dependence) | **No** | ~2.4σ out if taken as point |

**Constraint strength:** data require a **shallow positive** Σ_b exponent; they do **not** uniquely select 1/7 among {1/8, 1/7, 1/6}.

## Other constraints from Paper 24

| Observable | Constraint |
|------------|------------|
| MAE full sample | 0.05859 dex (preferred model) |
| Blind MAE fixed-1/7 | 0.0794 dex; no penalty vs free γ |
| Residual vs R_d, M_b | consistent with 0 for Σ_b model |
| μ∝1/R_d | excluded (ΔAIC=83.25) |
| Q=√2 fixed | no MAE cost |
| a_eff at median Σ_b | ≃ 1.41×10^{-10} m s^{-2} |

## Bootstrap vs theory chains

Theory γ from ν₀/(8 Δ_X) lands at 0.156–0.161. Distance from bootstrap mean 0.144 is 0.2–0.3σ — **compatible**, not a precision confirmation. Tightening bootstrap (larger N or lower systematics) is what would pressure scar vs pure ν₀.

## Status

Empirical envelope is wide on γ; decisive on “shallow Σ_b, not 1/R_d.” Theory targets sit comfortably inside the envelope.
