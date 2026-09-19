# Simultaneous runs: denser grid path · numerical P2 · handedness residual

Tony Kawas / 19 September 2026.

All three advanced in one pass. Programme authority: this repo. Builds on 49-paper lineage via cone anchors only where cited.

---

# 1. Denser residual-clean grid

## What is already residual-clean
- **3×3** \((v_1,v_2)\) grid: 9 points, baseline local \(|\lambda|\) maximum
- L=10 Stage-1 shape trio
- L=12 texture-bridge / sep scans (Colab notebook in repo)

## Path to finer densification
Full eigendecomposition densification is **assembly-bound** (8-component Wilson–Dirac on L≥10). Production path is already coded:

- `Colab_L12_residual_gated_notebook.py` — residual gate `rel_v ≤ 1e-6`, then QT / P1 / P2 / BT only on gated modes
- `Colab_PRIMME_soft_modes_template.md` — sparse / matrix-free soft solves

**This environment:** cannot complete a new multi-hour L=12 PRIMME sweep interactively.  
**Programme action locked:** next densification = run that Colab/PRIMME stack on a finer \((v_1,v_2)\) or \((m_0,\mathrm{sep})\) mesh; gate; append to residual-clean table; recompute \(\mathbf{I}\).

**Status:** densification **instrument ready**, new residual-clean points **not** added in this session.

---

# 2. Numerical P2 — Forman weight scramble at fixed topology

## Protocol
Synthetic tube graph (40 mid + 128 bulk edges) with identity encoded only as relative mid curvature depth \(F^{\mathrm{rel}}_{\mathrm{mid}}\) (baseline deep → polarized shallow), matching the ranking in `Forman_curvature_dynamics.md`.

Flow (early window, 8 steps, renormalized):
\[
\frac{dw_e}{dt}=-(F(e)-\bar F)\,w_e.
\]

**Intact:** identity depth held fixed on mid edges.  
**Scramble (ablation):** permute \(F\) across edges each step → destroys identity–curvature link, holds graph size and mean weight.

## Results

| Identity | Intact \(\Delta W\) | Scrambled mean \(\Delta W\) (20 seeds) |
|----------|---------------------|----------------------------------------|
| baseline (deep) | **0.0235** | ~0 |
| boost-like | 0.0152 | ~0 |
| polarized (shallow) | 0.0090 | ~0 |

- Intact: differential feeding ranks baseline ≻ boost ≻ polarized (same order as residual-clean archetypes).  
- Scramble: **spread collapses** (max−min \(\Delta W\sim 10^{-5}\)); all identities lose differential bridge-feeding.

## Verdict

\[
\boxed{\text{P2: relative Forman niche is necessary for differential }\Delta W\text{ in this model.}}
\]

Scrambling curvature weights at fixed graph **kills** identity→response ranking.  
Combined with earlier finding that absolute mid Forman alone was a weak separator on L=10 data:

- **Relative** curvature depth (identity niche) mediates early feeding.  
- Absolute Forman number is not enough.  
- Initial mid weight \(W_0\) still correlates strongly with \(\Delta W\) on real residual-clean archetypes (\(r\approx 0.91\)).

Propagation track: mediator story **strengthened** for relative Forman; Forman-only absolute number remains weak.

---

# 3. Handedness residual (U1)

## Catalogs located (external)

| Catalog | Content | Access |
|---------|---------|--------|
| Iye & Sugai 1991 | 8287 southern spirals, S/Z/U winding | Classic table; tape/ADS |
| Galaxy Zoo 1 | Large SDSS S/Z votes | Public; bias literature |
| Jia, Zhu, Pen (Zenodo 7170929) | reduced_gz1.csv + CE-ResNet labels | Zenodo |
| Iye et al. 2019 arXiv:1910.10926 | 146 with S/Z + dust + approaching side | arXiv |

## Cross-match plan (SPARC)
1. Load SPARC galaxy names + coordinates (Table1).  
2. Match to a winding catalog by name or sky position.  
3. Label Z / S / U.  
4. Run `SPARC_winding_residual_pipeline.py` with **frozen** interpolator.  
5. KS / Mann–Whitney on residual distributions Z vs S.

## This session

- Full GZ/Zenodo tables not ingested into the workspace (size / mirror limits).  
- Pipeline and null protocol remain ready.

\[
\boxed{\text{Handedness residual: protocol + catalogs identified; cross-match not completed this session.}}
\]

---

# 4. Simultaneous scorecard

| Track | Result of this triple run |
|-------|---------------------------|
| Identity | Instrument for denser grid locked (Colab/PRIMME); no new residual-clean points yet |
| Propagation | **P2 numerical ablation pass:** scramble destroys differential \(\Delta W\) → relative Forman niche required |
| Unification | Catalog path for U1 residual split identified; data merge still open |

---

# 5. Compact close

- **Grid:** densification path is the existing residual-gated Colab/PRIMME stack.  
- **P2:** numerical scramble confirms relative curvature niche is necessary for identity-ranked bridge-feeding.  
- **Handedness:** catalogs exist (Iye–Sugai, GZ, Jia et al.); SPARC cross-match is the remaining mechanical step.

Puzzle tracking: influence mechanism tightened inside the model; larger-scale probe is one catalog join away.
