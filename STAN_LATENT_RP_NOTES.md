# Stan latent-r_p starter — notes

File: `STAN_LATENT_RP_STARTER.stan`

## Syntax highlights vs PyMC
| Piece | Stan |
|-------|------|
| Truncated positive | `real<lower=0> mu_star;` + `~ normal(...) T[0, ];` or half-normal style |
| inv_logit | `inv_logit((x-1)/w)` = logistic F |
| Hierarchy | `mu_i ~ normal(mu_star + S * X, tau_mu);` |
| Soft prior switch | `use_soft_prior` data flag; default free |
| Benchmark | `generated quantities` holds 1/12.1 for comparison only |

## Guardrails baked in
- `use_soft_prior=0` by default → free μ_*.
- 12.1 kpc only in generated quantities for **post-fit** comparison, not as forced truth.
- Same simple logistic + one X_i as PyMC starter.

## Run sketch (CmdStanPy / PyStan / CmdStanR)
1. Prepare arrays: gal, r, R_obs, R_err, X.
2. Set `use_soft_prior=0` for primary inference.
3. Sample; report posterior of `mu_star`, `S`, `tau_mu`.
4. Optionally compare `mu_star` posterior to `1/12.1`.
5. LOO vs null models (S=0; free per-galaxy intercept — requires model variants).

## Upgrades (mirror PyMC list)
- Baseline B_i near 1.
- Class offsets.
- X_i from Σ_b(r_p,i) via interpolation (harder in pure Stan).
- Alternative F: arctan coded as `(atan((x-1)/w)/pi() + 0.5)`.
