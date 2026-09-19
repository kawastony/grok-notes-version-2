# Triple track: identity · propagation · scale-up

Tony Kawas / 19 September 2026.

**Programme authority:** this repository (microscopic cone / lattice / chirality).  
`notes-by-grok` is an independent research path. This work borrows mainly the microscopic anchors
\[
R_{\mathrm{cone}}=\frac{\sqrt6}{\varphi}\approx 1.51387,
\qquad
(11/72)_{\mathrm{cone}}:=\frac{\Delta y}{\varphi}\approx 0.1511,
\]
and builds its own larger-scale programme from cone + lattice structure — not from that path’s freeze list.

---

# A. Identity (raise toward ~90%)

## A.1 Operational definition

On residual-clean soft support of the 8-component pair defect, define
\[
\mathbf{I}
=
\bigl(
R_{\mathrm{mid}},\;
c,\;
|D_1|,\;
A-1,\;
\chi_{\beta n},\;
\mathrm{IPR},\;
w_{\mathrm{core}}
\bigr).
\]

**Identity claim (within model):** residual-clean soft states form a measurable cluster in \(\mathbf{I}\)-space, separated from bulk modes by a residual-clean gap.

## A.2 What is already derived / observed

| Fact | Status |
|------|--------|
| 8-component Callias-type embedding | Confirmed |
| Soft sector exists for pair defects | Confirmed |
| Molecular hybridization at moderate sep | Confirmed |
| Mid-peak / mid-dip under boost / weaken | Residual-clean |
| Bulk gap \(\Delta_{\mathrm{bulk}}=m_0\) | Measured (e.g. \(m_0=0.3\Rightarrow\xi_{\mathrm{bulk}}\approx 1/m_0\)) |

## A.3 Derivations still open (identity)

1. **Index = \(N_{\mathrm{def}}\)** in continuum limit of the lattice Dirac operator (Callias / JR route).  
2. **Stability of \(\mathbf{I}\)** under residual-clean enlargements (L, sep, \(m_0\)).  
3. **Decoupling criterion:** sep \(\gg\) core radius \(\Rightarrow\) independent opposite local charges (not yet at L=6–8).

## A.4 Immediate tests

- Denser residual-clean \((v_1,v_2)\) or \((m_0,\mathrm{sep})\) grid.  
- Report silhouette / gap of soft cluster in \(\mathbf{I}\).  
- Record whether opposite-core localization appears as sep increases.

---

# B. Propagation (raise toward ~85%)

## B.1 Continuity + constitutive skeleton

Texture chirality density \(\rho_\chi\) (lattice-facing identification with soft \(\chi_{\beta n}\) structure):
\[
\partial_t\rho_\chi+\nabla\cdot\mathbf{J}_\chi
=
S_{\mathrm{top}}-\Gamma_f\rho_\chi,
\]
\[
\mathbf{J}_\chi
=
-D_\chi\nabla\rho_\chi
+\kappa\rho_\chi\mathbf{B}_{\mathrm{eff}}
+\boldsymbol\xi_{\mathrm{cone}}.
\]

- Continuity / inflow structure: standard anomaly matching (Callan–Harvey family).  
- Drift term: **ansatz** (CME-shaped).  
- \(\kappa=R_{\mathrm{cone}}/c\): dimensional match from cone surface data (borrowed microscopic value).

## B.2 Lattice-facing predictions (falsifiable inside the model)

| ID | Prediction |
|----|------------|
| P1 | Soft anti-alignment (\(\chi_{\beta n}<0\)) flips sign of early bridge-feeding relative to bulk-aligned texture under the same discrete \(\mathbf{B}_{\mathrm{eff}}\) proxy |
| P2 | Relative Forman curvature mediates \(\mathbf{I}\to\Delta W_{\mathrm{mid}}\): scrambling curvature weights at fixed \(\mathbf{I}\) collapses rank prediction |
| P3 | Increasing sep at fixed identity class increases hybridization time / effective \(D_\chi\) monotonically in the molecular regime |

## B.3 Derivation status

| Piece | Derived? |
|-------|----------|
| Anomaly continuity template | Yes (QFT standard) |
| Soft sector as IR carrier of index | Lattice-supported |
| \(\mathbf{J}\propto\rho_\chi\mathbf{B}_{\mathrm{eff}}\) | Ansatz |
| Forman as discrete curvature mediator | Empirical in-model |
| Full continuum limit of \(\mathbf{J}\) from lattice | **Open** |

## B.4 Immediate tests

- Mediator ablation (P2) on existing residual-clean archetypes.  
- Sign flip test (P1) if both alignment classes exist in the grid.  
- Sep scan (P3) as L allows.

---

# C. Scale-up / unification (raise from ~38% by derivation routes, not slogans)

This section explores **how larger scales can become possible** from objects already in this programme. Nothing here claims a finished galactic TOE.

## C.1 Available microscopic anchors

\[
R_{\mathrm{cone}}=\frac{\sqrt6}{\varphi},\qquad
\kappa=\frac{R_{\mathrm{cone}}}{c},\qquad
\xi_{\mathrm{bulk}}\sim\frac{1}{m_0}\ \text{(lattice units)},\qquad
w_{\mathrm{core}}\sim O(1)\ \text{sites}.
\]

Lattice spacing \(a\) is **not fixed** by the Dirac operator alone; scale-up requires a map
\[
a\;\longrightarrow\;\text{physical length}.
\]

## C.2 Route 1 — Correlation-length matching (exploratory)

Suppose the soft-mode support size in physical units is set by
\[
\ell_{\mathrm{soft}}
=
a\cdot\max(w_{\mathrm{core}},\xi_{\mathrm{bulk}},R_{\mathrm{mid}}^{\mathrm{(lat)}}).
\]

**Question (not yet answered):** is there a natural choice of \(a\) such that \(\ell_{\mathrm{soft}}\) sits at a galactic core scale (\(\sim 0.1\)–\(1\,\mathrm{kpc}\)) without hand-tuning beyond cone data?

Dimensional sketch only:
- If one identifies a UV cutoff with a hadronic / geometric scale, \(\ell_{\mathrm{soft}}\) is microscopic — **no** automatic kpc.  
- If one treats the network as already coarse-grained (residual network), \(a\) is a meso-scale and kpc is not absurd — but that **assumes** the scale one wanted to derive.

**Status:** route open; not a derivation until \(a\) is fixed by a continuum limit or a matching condition forced by the cone action.

## C.3 Route 2 — Acceleration / stiffness from \(\kappa\) (exploratory)

Chiral / gyroscopic coefficient has units of inverse speed:
\[
\kappa=\frac{R_{\mathrm{cone}}}{c}.
\]
An effective residual acceleration or stiffness would need an extra scale, e.g.
\[
a_{\mathrm{eff}}
\sim
\kappa\cdot(\text{velocity scale})^2
\quad\text{or}\quad
\kappa\cdot c\cdot H,
\]
etc. None of these is forced yet.

**Honest barrier:** \(\kappa\) alone does not select MOND-like \(a_T\sim 10^{-10}\,\mathrm{m\,s^{-2}}\). One would need a dynamical equation that converts helical density into a radial acceleration law, then a vacuum or deep-MOND limit.

**Status:** architectural possibility only; **no derivation of \(a_T\)** from this programme at present.

## C.4 Route 3 — Same constitutive template at residual-network scale (best near-term unification)

Promote lattice fields by geometric analogy (already written in residual chiral notes):
\[
\boldsymbol\varepsilon\to\boldsymbol\Sigma_{\mathrm{res}},\qquad
\hat{\mathbf{c}}\to\hat{\mathbf{n}},\qquad
\kappa\ \text{unchanged}.
\]

This is **template unification** (U1):
- same continuity law,  
- same drift structure,  
- coefficients inherited from cone micro data.

It becomes scientific when it yields a **falsifiable residual prediction** (e.g. handedness-split residuals in rotation-curve or weak-lensing parity-odd stats). Until data confrontation, it is a structured hypothesis, not a completed scale-up.

## C.5 Route 4 — Continuum limit first (required for honest U2)

Pre-register continuum targets the lattice must approach:

1. Index \(\to N_{\mathrm{def}}\).  
2. Soft gap / localization length scaling.  
3. Sign of \(\Delta W\) / current under \(\chi_{\beta n}\) flip.  
4. Recovery of a local effective action containing \(\mathcal{L}_{\mathrm{chiral}}\).

Only after (1)–(4) is it legitimate to speak of an emergent continuum field theory that could couple to gravity or galactic dynamics.

## C.6 What would count as real progress on unification

| Milestone | Moves unification |
|-----------|-------------------|
| Continuum index theorem matched on lattice | U2 start |
| Effective action with fixed \(\kappa\) from cone | U2 |
| Template residual prediction tested (even null) | U1 empirical |
| Acceleration law derived from that action without target | U3 (high bar) |

---

# D. Simultaneous work package (this programme)

| Priority | Action | Track |
|----------|--------|-------|
| 1 | Residual-clean denser grid; freeze \(\mathbf{I}\) | Identity |
| 2 | Mediator ablation P2; sign test P1 | Propagation |
| 3 | Write continuum target list; push sep decoupling | Identity + U2 roadmap |
| 4 | Residual-network template: one concrete observable design (handedness residual) | Unification U1 |
| 5 | Dimensional analysis note: list **all** extra assumptions needed to reach kpc or \(a_T\) | Unification honesty |

---

# E. Compact statements

**Identity.** Soft residual-clean states are operationally \(\mathbf{I}\); index and decoupling remain open derivations.

**Propagation.** Continuity is standard; constitutive drift is ansatz; Forman mediation is in-model and falsifiable.

**Scale-up.** Borrowed \(R_{\mathrm{cone}}\) and \(\kappa\) do **not** by themselves yield galactic accelerations or kpc cores. Viable near-term path is template promotion to residual networks plus continuum limit; derivation of macro acceleration laws is not yet achieved.

**Independence.** This programme does not treat `notes-by-grok` as constitution; it only reuses cone microscopic numbers where cited and builds scale-up on its own lattice + chirality + residual logic.
