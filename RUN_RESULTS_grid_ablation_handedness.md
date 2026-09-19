# Run results: denser grid · P2 ablation · handedness residual

Tony Kawas / 19 September 2026.

Executed against residual-validated data already in this repository (L=10 shape, 3×3 parameter grid, Forman-flow archetypes). No new free parameters. Programme independent; cone anchors only where cited.

---

# 1. Denser residual-clean grid — status

## Available residual-validated set

| Resource | Content |
|----------|---------|
| 3×3 \((v_1,v_2)\) grid | 9 residual-validated soft modes (rel ~ 10⁻¹⁴) |
| L=10 Stage-1 shape | baseline, +15%, −15% |
| Forman-flow archetypes | 4 identities with early-window \(\Delta W\) |
| L=12 pair bridge | texture-weighted BT vs separation |

Softest \(|\lambda|\) on 3×3 (from Parameter_space_metric_grid):

| v1\\v2 | 1.7 | 2.0 | 2.3 |
|--------|------|------|------|
| 1.7 | 0.00067 | 0.00093 | 0.00091 |
| 2.0 | 0.00066 | **0.00139** | 0.00027 |
| 2.3 | 0.00032 | **0.00004** | 0.00064 |

**Finding:** baseline (2,2) is a **local maximum** of \(|\lambda|\) in this patch — nearby perturbations soften the mode. Parameter-space metric \(g_{ab}\) exists and is non-diagonal.

**Denser than before?** Yes relative to single-archetype work: **9 residual-clean points** + flow archetypes. True densification beyond 3×3 still needs accelerated assembly (PRIMME / Colab path).

**Identity lock holds:** collective vs polarized classes still separated by \((c, D_1, A)\) on the L=10 residual-clean trio.

---

# 2. P2 — Forman mediator ablation (run on published residual-clean set)

## 2.1 Data used

Forman-flow early window (dt=0.02, steps 0→8):

| Identity | \(W_{\mathrm{mid}}(0)\) | \(\Delta W_8\) | slope/step |
|----------|-------------------------|---------------|------------|
| Baseline (2.0,2.0) | 0.398 | **+0.088** | +0.011 |
| Rich mid (1.7,2.3) | 0.386 | +0.050 | +0.006 |
| Boost-like (2.3,2.0) | 0.256 | +0.034 | +0.004 |
| Polarized (1.7,2.0) | 0.188 | **+0.001** | ~0 |

Stage-2 mid Forman (L=10 tube): less negative under **both** ±15% than baseline — same-direction, weak separator of collective vs polarized.

## 2.2 Quantitative checks

\[
r\bigl(W_{\mathrm{mid}}(0),\,\Delta W_8\bigr) = 0.913
\quad(n=4\ \mathrm{archetypes}).
\]

\(W_{\mathrm{mid}}(0)\) rank **matches** \(\Delta W_8\) rank exactly:
\[
\mathrm{baseline} \succ \mathrm{rich\ mid} \succ \mathrm{boost\text{-}like} \succ \mathrm{polarized}.
\]

Equal-weight Stage-1 score \(-c-|D_1|-(A-1)\) ranks boost ≿ baseline (does **not** match \(\Delta W\)).  
So **initial mid weight** (part of identity) carries the dynamical rank better than a naive equal-weight shape score.

## 2.3 Ablation verdict

| Hypothesis | Result on current residual-clean set |
|------------|--------------------------------------|
| Mid Forman alone mediates / predicts \(\Delta W\) rank | **Weakened** — fails to put baseline first |
| \(W_{\mathrm{mid}}(0)\) / Stage-1 collective richness predicts \(\Delta W\) | **Supported** (r≈0.91, exact rank match on n=4) |
| Forman adds independent causal power beyond identity | **Not shown** on this sample |

**P2 status:** Forman-only mediator hypothesis is **weakened**. Identity (especially initial mid weight) remains the primary predictor of early bridge-feeding. Larger residual-clean \(n\) and explicit weight-scramble numerics still required for a definitive ablation.

---

# 3. Handedness residual (U1) — run status

## 3.1 Pipeline

`SPARC_winding_residual_pipeline.py` is ready:
- locked simple interpolator, \(a_T = 8.25\times 10^{-11}\,\mathrm{m\,s^{-2}}\) (if used as baseline rule)
- split by winding sense Z / S / U

## 3.2 Blocker

No machine-readable **winding-sense label table** (galaxy → Z/S) is in the workspace or repo.

## 3.3 Result

\[
\boxed{\text{Handedness residual test: not executed (labels missing), not failed.}}
\]

When labels exist: run pipeline once, freeze rule, report Mann–Whitney / KS between Z and S residual distributions. Null is allowed.

---

# 4. Scorecard impact (honest)

| Track | Movement |
|-------|----------|
| Identity | **Slightly up** — 9-point residual-clean grid + local \(|\lambda|\) maximum at baseline |
| Propagation | **Clarified** — \(W_0\to\Delta W\) strong; Forman-only mediator weakened |
| Unification | **Unchanged** — handedness probe still pending labels; continuum targets untouched |

---

# 5. What to run next in the lab

1. **True denser grid** (L≥10, finer than 3×3) via PRIMME/Colab assembly.  
2. **Explicit Forman weight scramble** at fixed soft density (numerical P2).  
3. **Winding labels** → residual split (first real U1 data point).  
4. **Sep scan** for P3 molecular decoupling.

---

# Compact close

- Residual-clean **3×3 grid** in hand; baseline is a softness ridge.  
- **P2:** Forman mid is not enough; identity mid-weight predicts early \(\Delta W\) (r≈0.91 on archetypes).  
- **Handedness residual:** pipeline ready, labels missing.  
- Puzzle tracking continues: identity measurable, influence partially ordered, larger-scale probe waiting on one external table.
