#!/usr/bin/env python3
"""Residual correlation estimator for hierarchical SPARC midpoint tests.

Usage (synthetic demo):
  python residual_correlation_estimator.py

With prepared table (columns: name, mu_hat, X [, class]):
  python residual_correlation_estimator.py --csv path/to/table.csv
"""
from __future__ import annotations

import argparse
import numpy as np
import pandas as pd
from numpy.linalg import lstsq


def fit_common_intercept(mu_hat: np.ndarray, X: np.ndarray):
    A = np.column_stack([np.ones(len(X)), X])
    coef, _, _, _ = lstsq(A, mu_hat, rcond=None)
    mu_star, S = float(coef[0]), float(coef[1])
    e = mu_hat - (mu_star + S * X)
    return mu_star, S, e


def corr_vs_sep(values: np.ndarray, coord: np.ndarray, n_bins: int = 8, min_pairs: int = 5):
    values = np.asarray(values, float)
    coord = np.asarray(coord, float)
    i, k = np.triu_indices(len(values), k=1)
    d = np.abs(coord[i] - coord[k])
    prod = values[i] * values[k]
    if d.size == 0:
        return np.array([]), np.array([]), np.array([])
    bins = np.linspace(d.min(), d.max() + 1e-15, n_bins + 1)
    centers, cvals, counts = [], [], []
    for b0, b1 in zip(bins[:-1], bins[1:]):
        m = (d >= b0) & (d < b1)
        if int(m.sum()) < min_pairs:
            continue
        centers.append(0.5 * (b0 + b1))
        cvals.append(float(prod[m].mean()))
        counts.append(int(m.sum()))
    return np.asarray(centers), np.asarray(cvals), np.asarray(counts)


def shuffle_pvalue(e: np.ndarray, coord: np.ndarray, n_null: int = 300, seed: int = 0):
    rng = np.random.default_rng(seed)
    e0 = e - e.mean()
    _, cy, _ = corr_vs_sep(e0, coord)
    if len(cy) == 0:
        return np.nan, np.nan
    obs = float(np.max(np.abs(cy)))
    null = []
    for _ in range(n_null):
        es = rng.permutation(e0)
        _, cys, _ = corr_vs_sep(es, coord)
        if len(cys):
            null.append(float(np.max(np.abs(cys))))
    null = np.asarray(null)
    p = float((null >= obs).mean()) if len(null) else np.nan
    return obs, p


def demo(seed: int = 7, n_gal: int = 40):
    rng = np.random.default_rng(seed)
    mu_star, S, tau = 0.10, 0.05, 0.015
    X = rng.uniform(0.7, 1.3, n_gal)
    mu_hat = mu_star + S * X + tau * rng.standard_normal(n_gal)
    order = np.argsort(X)
    mu_hat[order] += 0.02 * np.sin(2 * np.pi * np.linspace(0, 2, n_gal))
    mu_star_h, S_h, e = fit_common_intercept(mu_hat, X)
    obs, p = shuffle_pvalue(e, X)
    return {
        "mu_star_hat": mu_star_h,
        "S_hat": S_h,
        "mean_e": float(e.mean()),
        "std_e": float(e.std()),
        "max_abs_C": obs,
        "shuffle_p": p,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=None, help="CSV with columns mu_hat, X")
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    if args.csv is None:
        out = demo(seed=args.seed)
        print("synthetic demo:", out)
        return
    df = pd.read_csv(args.csv)
    mu_star_h, S_h, e = fit_common_intercept(df["mu_hat"].to_numpy(), df["X"].to_numpy())
    obs, p = shuffle_pvalue(e, df["X"].to_numpy())
    print({"mu_star_hat": mu_star_h, "S_hat": S_h, "mean_e": float(e.mean()), "max_abs_C": obs, "shuffle_p": p})


if __name__ == "__main__":
    main()
