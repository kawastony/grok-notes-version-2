#!/usr/bin/env python3
"""
SPARC residual pipeline with winding-sense (Z/S) split.

Status: skeleton ready for data.  
Requires:
  1. SPARC Table1 + mass-model files (official SPARC release).
  2. External winding-sense table: galaxy name → 'Z', 'S', or 'U' (unknown).

Locked simple interpolator:
    g_obs = 0.5 * g_N + sqrt( (0.5 * g_N)**2 + g_N * a_T )
with a_T = 8.25e-11 m s^-2 (locked product).

Usage:
  python SPARC_winding_residual_pipeline.py \
      --sparc-table1 Table1.mrt \
      --mass-models MassModels/ \
      --winding winding_labels.csv \
      --out residual_split_report.txt

Output:
  - residual distributions split by winding sense
  - median / mean residual per bin
  - Mann-Whitney or KS statistic between Z and S bins
  - list of galaxies with unknown winding
"""

import argparse
import numpy as np
from pathlib import Path
import warnings

# Locked constants from the spine
A_T = 8.25e-11          # m s^-2
KAPPA = np.sqrt(6) / ((1 + np.sqrt(5))/2) / 2.99792458e8   # R_cone / c  (placeholder numerical)

def simple_interpolator(g_N, a_T=A_T):
    """Locked simple interpolator (exact at transition = golden ratio)."""
    g_N = np.asarray(g_N, dtype=float)
    return 0.5 * g_N + np.sqrt((0.5 * g_N)**2 + g_N * a_T)

def load_winding_labels(path):
    """Expect CSV: name,winding  where winding in {'Z','S','U'}."""
    labels = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            name, wind = [x.strip() for x in line.split(',')[:2]]
            labels[name.upper()] = wind.upper()
    return labels

def compute_residuals_for_galaxy(v_obs, v_bar, distances):
    """
    Placeholder: convert velocities to accelerations (g = V^2 / R),
    apply interpolator, return residual array.
    Real implementation must use the official SPARC mass-model columns.
    """
    # g_obs ≈ V_obs**2 / R , g_N ≈ V_bar**2 / R   (cgs or SI consistent)
    # This is schematic only.
    g_obs = (v_obs**2) / distances
    g_N   = (v_bar**2) / distances
    g_pred = simple_interpolator(g_N)
    residual = g_obs - g_pred
    return residual

def main():
    parser = argparse.ArgumentParser(description="SPARC residual split by winding sense")
    parser.add_argument("--sparc-table1", required=True, help="SPARC Table1.mrt or equivalent")
    parser.add_argument("--mass-models", required=True, help="Directory of per-galaxy mass models")
    parser.add_argument("--winding", required=True, help="CSV name,winding (Z/S/U)")
    parser.add_argument("--out", default="residual_split_report.txt")
    args = parser.parse_args()

    winding = load_winding_labels(args.winding)

    # --- Placeholder data loading ---
    # In a full run one would parse Table1 and the rotmod / mass-model files.
    # Here we only demonstrate the split logic.
    print("Pipeline skeleton loaded.")
    print("Locked a_T =", A_T)
    print("Number of winding labels supplied:", len(winding))
    print("Z :", sum(1 for v in winding.values() if v == 'Z'))
    print("S :", sum(1 for v in winding.values() if v == 'S'))
    print("U :", sum(1 for v in winding.values() if v == 'U'))
    print()
    print("To complete the test:")
    print("1. Parse official SPARC mass models.")
    print("2. Compute g_obs, g_N per radial point.")
    print("3. Form residual = g_obs - simple_interpolator(g_N).")
    print("4. Aggregate residual statistic per galaxy (median or mean).")
    print("5. Split the per-galaxy residual list by winding['Z'] vs winding['S'].")
    print("6. Run Mann-Whitney U or KS test between the two lists.")
    print("7. Report effect size and p-value.")
    print()
    print("Output file would contain the two residual distributions and the test statistic.")
    print("This skeleton is ready; only the SPARC parser + cross-match table are missing.")

if __name__ == "__main__":
    main()
