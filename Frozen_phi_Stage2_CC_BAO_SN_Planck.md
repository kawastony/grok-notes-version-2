# Frozen-φ Stage 2: CC + BAO (correlated) + Pantheon+ + Planck prior

Tony Kawas / 20 September 2026.

**Frozen:** \((w_0,w_a)=(-\varphi/2,\,-1/\varphi)\).  
**Free:** \(H_0,\Omega_m,r_d,M\) (SN magnitude offset).

---

## Datasets

| Probe | Implementation |
|-------|----------------|
| Cosmic chronometers | 32 H(z) points, uncorrelated |
| DESI DR1 BAO | \(D_V/r_d\) + anisotropic \((D_M,D_H)/r_d\) with published \(r_{\rm off}\) |
| Pantheon+ | 1590 Hubble-flow SNe (z>0.01), **STATONLY** covariance (full SYS not loaded) |
| Planck 2018 | Approximate distance prior \((R,\ell_A)\) with rough 2×2 cov |

**Caveats (important):**
1. SN uses STATONLY cov, not STAT+SYS — systematics underrepresented.  
2. Planck prior is compressed/approximate (not full Planck likelihood).  
3. BAO uses published bin correlations, not the full official DESI joint matrix.  
Results are **stronger than Stage 1** but still **not official joint posteriors**.

---

## Stage 2A — CC + BAO + Pantheon+ STAT

| Model | χ² | H₀ | Ωₘ | r_d | M |
|-------|-----|-----|-----|------|------|
| **φ-frozen** | **1516.7** | 68.0 | 0.304 | 147.0 | −19.40 |
| ΛCDM | 1524.4 | 68.0 | 0.327 | 147.0 | −19.42 |
| paste (−0.79,−0.152) | 1516.7 | 67.9 | 0.264 | 147.1 | −19.40 |

**Δχ² vs ΛCDM:** φ = **−7.7**, paste = −7.6

---

## Stage 2B — CC + BAO + SN + Planck distance prior

| Model | χ² | H₀ | Ωₘ | r_d | M |
|-------|-----|-----|-----|------|------|
| **φ-frozen** | **1517.9** | 66.0 | 0.306 | 151.2 | −19.46 |
| ΛCDM | 1530.5 | 66.0 | 0.310 | 153.0 | −19.48 |
| paste | 1554.7 | 63.2 | 0.324 | 152.7 | −19.54 |

**Δχ² vs ΛCDM:** φ = **−12.6**, paste = **+24.2**

With the Planck prior, paste degrades sharply; φ remains preferred over ΛCDM on this approximate combination.

---

## Decision

| Criterion | Stage 2A | Stage 2B |
|-----------|----------|----------|
| Acceptable χ² | Yes | Yes |
| Not worse than ΛCDM | **Better (Δχ²=−7.7)** | **Better (Δχ²=−12.6)** |
| Beats paste | Tied (2A) / **clearly** (2B) | **Yes** |

**Stage-2 verdict (with caveats):** The frozen φ point remains viable and is preferred over ΛCDM on these approximate late-time+prior combinations. The result is consistent in direction with the Stage-1 CC+BAO test and with the DESI free-CPL orientation pass.

---

## What is still required for a definitive claim

1. Pantheon+ **STAT+SYS** full covariance  
2. Official DESI BAO joint covariance (all tracers)  
3. Proper Planck likelihood or validated distance-prior covariance for CPL  
4. Independent pipeline cross-check (Cobaya/MontePython)

Until then: **promising Stage-2 indication**, not a published cosmology constraint.

---

## Compact statement

On Stage-2 combinations (CC + DESI BAO with bin correlations + Pantheon+ STAT cov ± approximate Planck prior), the frozen geometric CPL point \((-\varphi/2,\,-1/\varphi)\) yields lower χ² than ΛCDM (Δχ² ≈ −8 to −13) after profiling background/nuisance parameters. The paste comparison point fails under the Planck prior. Full systematic covariances remain the verification wall before strong claims.
