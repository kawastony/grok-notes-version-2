// Latent-r_p hierarchical SPARC starter (Stan)
// Intentional simple: logistic transition, one X per galaxy, free mu_star
// Units must be consistent. Soft 12.1 kpc prior optional and OFF by default.

data {
  int<lower=1> N_obs;                 // stacked residual points
  int<lower=1> N_gal;                 // galaxies
  array[N_obs] int<lower=1, upper=N_gal> gal;  // galaxy index per obs
  vector<lower=0>[N_obs] r;           // radii
  vector[N_obs] R_obs;                // residual ratio g_obs/g_b
  vector<lower=0>[N_obs] R_err;       // errors on R
  vector[N_gal] X;                    // (Sigma_b/Sigma_ref)^(1/7) per galaxy
  int<lower=0, upper=1> use_soft_prior; // 0 = free mu_star; 1 = soft prior
  real mu_star_mean;                  // e.g. 1/12.1 if used
  real<lower=0> mu_star_sd;
}

parameters {
  real<lower=0> mu_star;
  real S;
  real<lower=0> tau_mu;
  vector<lower=1e-6>[N_gal] mu_i;     // latent 1/r_p
  vector<lower=0>[N_gal] A;
  vector<lower=0>[N_gal] w;
  real<lower=0> sigma_int;
}

transformed parameters {
  vector<lower=0>[N_gal] r_p = inv(mu_i);
}

model {
  // Hyperpriors — free by default (anti-circularity)
  if (use_soft_prior == 1) {
    mu_star ~ normal(mu_star_mean, mu_star_sd) T[0, ];
  } else {
    mu_star ~ normal(0, 1) T[0, ];   // weak half-ish via truncation
  }
  S ~ normal(0, 1);
  tau_mu ~ normal(0, 0.5) T[0, ];
  sigma_int ~ normal(0, 0.2) T[0, ];

  // Population model
  mu_i ~ normal(mu_star + S * X, tau_mu);

  // Profile parameters
  A ~ normal(0, 5) T[0, ];
  w ~ normal(0, 1) T[0, ];

  // Observation model: logistic transition
  {
    vector[N_obs] x;
    vector[N_obs] F;
    vector[N_obs] R_model;
    vector[N_obs] sigma_tot;
    for (n in 1:N_obs) {
      x[n] = r[n] / r_p[gal[n]];
      F[n] = inv_logit( (x[n] - 1) / w[gal[n]] );  // 1/(1+exp(-(x-1)/w))
      // inv_logit(z) = 1/(1+exp(-z)); z=(x-1)/w => F = 1/(1+exp(-(x-1)/w))
      R_model[n] = 1 + A[gal[n]] * F[n];
      sigma_tot[n] = sqrt(square(R_err[n]) + square(sigma_int));
    }
    R_obs ~ normal(R_model, sigma_tot);
  }
}

generated quantities {
  real mu_star_benchmark_12p1 = 1.0 / 12.1; // for post-hoc comparison only
}
