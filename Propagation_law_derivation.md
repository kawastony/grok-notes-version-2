# Propagation law — derivation and status

Tony Kawas / 17 September 2026.

**Status:** candidate effective law grounded in anomaly inflow + texture chirality.  
**Not** a theorem from the lattice Index = N_def program.  
**Not** a completed dynamical TOE.

---

## 1. What must be derived

The missing half of the program is not “identity” (index, soft sector, χ_βn) but **influence**:

> Why does a local change in organization produce a response elsewhere?

A propagation law must specify:

1. A local order parameter (what carries identity/orientation)
2. A conserved or quasi-conserved current (what flows)
3. A response rule (how distant regions feel the flow)
4. Consistency with topology (anomaly matching / inflow)

---

## 2. Continuum backbone: Callan–Harvey inflow

In odd-dimensional bulk with a topological mass/Higgs texture, the **consistent anomaly** on a defect or boundary is cancelled by **inflow** from the bulk.

Schematically (Abelian prototype):

\[
\partial_\mu J^\mu_{\rm edge}
=
\frac{n_R-n_L}{4\pi}\,q^2\,F
\qquad\text{(edge anomaly)}
\]

Bulk Chern–Simons / parity-odd response supplies a current whose flux into the edge cancels the variation:

\[
*J_{\rm bulk} = \sigma_H\,F
\qquad\Rightarrow\qquad
\Delta Q_{\rm edge}
=
\int *J_{\rm bulk}
=
\sigma_H\int F.
\]

**Propagation content already present here:**

- Local chiral imbalance / defect charge is not isolated.
- Continuity forces bulk current to adjust when edge (or defect) content changes.
- The “why elsewhere responds” is **anomaly matching**: gauge/topological invariance of the full system.

Callias zero modes and hedgehog textures sit in this same family: index fixed by asymptotic mass map; local soft modes are the IR carriers of that index.

---

## 3. Lattice-earned order parameter

From the soft-sector diagnostics:

\[
\chi_{\beta n}
=
\big\langle
\psi\,\big|\,
\beta\otimes\big(\tau\cdot\hat n(x)\big)
\,\big|\,
\psi
\big\rangle
\]

- Soft modes: \(\chi_{\beta n}\approx -0.8\) (anti-aligned with mass texture)
- Bulk modes: \(\chi_{\beta n}\approx +0.99\)

Define a **coarse-grained texture chirality density** on scales larger than the core:

\[
\rho_\chi(x)
=
\mathrm{Tr}\,\rho(x)\,\big(\beta\otimes\tau\cdot\hat n(x)\big)
\]

with \(\rho\) the soft-sector projector (or a local density built from soft modes).

This is the best lattice-motivated local order parameter we currently have. It is **not** continuum \(\gamma_5\) chirality; it is **defect-aligned mass-texture orientation**.

---

## 4. Minimal propagation law (candidate)

### 4.1 Continuity + inflow template

Promote inflow to an effective continuum statement for the texture field:

\[
\boxed{
\partial_t\rho_\chi + \nabla\cdot\mathbf J_\chi
=
S_{\rm top}
-
\Gamma_f\,\rho_\chi
}
\]

- \(\mathbf J_\chi\): texture-chiral current (to be specified)
- \(S_{\rm top}\): topological source (anomaly density / winding production rate)
- \(\Gamma_f\): relaxation / flipping rate (UV, finite-volume, Wilson artefacts)

This is the direct analogue of axial continuity with anomaly source and chirality-flipping sink.

### 4.2 Constitutive relation (response rule)

The simplest anomaly-inspired constitutive law (CME-style structure, adapted to texture):

\[
\boxed{
\mathbf J_\chi
=
-D_\chi\nabla\rho_\chi
+
\kappa\,\rho_\chi\,\mathbf B_{\rm eff}
+
\boldsymbol\xi_{\rm cone}
}
\]

| Term | Meaning |
|------|--------|
| \(-D_\chi\nabla\rho_\chi\) | Ordinary diffusion of texture chirality |
| \(\kappa\,\rho_\chi\,\mathbf B_{\rm eff}\) | Anomaly-like induced current along an effective “axial” field |
| \(\boldsymbol\xi_{\rm cone}\) | Framework residual (cone / galactic chiral residual) |

Here:

- \(\kappa\) is the **chiral residual / inflow coefficient** already appearing in the cone program language.
- \(\mathbf B_{\rm eff}\) is an effective field built from the background that couples to texture orientation (Higgs gradient, emergent gauge field from defect lattice, or macroscopic handedness field — model-dependent).

**This constitutive piece is the ansatz.** Continuity + anomaly source is continuum-standard; the identification of \(\rho_\chi\) with lattice texture chirality and of \(\kappa\) with the cone residual is the program-specific step.

### 4.3 Propagation of influence

Linearize about a background \(\bar\rho_\chi\):

\[
\partial_t\delta\rho_\chi
=
D_\chi\nabla^2\delta\rho_\chi
-
\kappa\,\nabla\cdot\big(\bar\rho_\chi\,\delta\mathbf B_{\rm eff}+\delta\rho_\chi\,\mathbf B_{\rm eff}\big)
-
\Gamma_f\delta\rho_\chi
+
\delta S_{\rm top}.
\]

A localized change \(\delta\rho_\chi(x_0)\) sources:

1. Diffusive spreading (ordinary)
2. Ballistic / anomaly-driven current along \(\mathbf B_{\rm eff}\) (parity-odd)
3. Possible wave-like modes if \(\mathbf B_{\rm eff}\) is dynamical (chiral magnetic wave analogues)

**That is the propagation law in differential form:** local texture change → divergence of \(\mathbf J_\chi\) → remote \(\rho_\chi\) adjustment, constrained by topology via \(S_{\rm top}\).

---

## 5. Matching to the scale chain

| Scale | Carrier of \(\rho_\chi\) | Propagation mechanism |
|-------|------------------------|------------------------|
| Micro (lattice) | Soft-sector texture alignment | Overlap / hybridization; inflow to cores |
| Mesoscopic | Defect gas / skyrmion-like textures | Anomaly-induced currents between defects |
| Macro (galactic) | Handedness / residual torque language | \(\kappa\)-coupled residual in effective dynamics |
| Cosmic | Large-scale parity-odd flow | Same constitutive structure, coarse-grained |

The **same continuity + constitutive template** is proposed at each level; only the realization of \(\mathbf B_{\rm eff}\) and the magnitude of \(\kappa, D_\chi, \Gamma_f\) change.

This is how “chirality as organizing principle across scales” becomes a **law-shaped** statement rather than a pure narrative.

---

## 6. What is derived vs assumed

| Piece | Status |
|-------|--------|
| Anomaly continuity / inflow structure | Standard QFT (Callan–Harvey, ABJ) |
| Soft sector robust; texture χ soft ≠ bulk | **Lattice result** |
| \(\rho_\chi\) identified with \(\beta\otimes(\tau\cdot\hat n)\) density | Motivated identification |
| Constitutive \(\mathbf J_\chi\supset\kappa\rho_\chi\mathbf B_{\rm eff}\) | **Ansatz** (CME-shaped) |
| \(\kappa\) = cone residual coefficient | Program identification |
| Cross-scale universality of the template | **Hypothesis** |
| Full nonlinear dynamics of \(\mathbf B_{\rm eff}\) | Open |

---

## 7. Minimal testable consequences

1. **Parity-odd residual transport** correlated with measured soft-sector \(\chi_{\beta n}\) imbalance.
2. **Diffusion + drift** of texture chirality: changing defect separation or \(m_0\) should change effective \(D_\chi\) and hybridization timescale.
3. **Sign structure:** soft anti-alignment (\(\chi_{\beta n}<0\)) implies opposite current direction relative to bulk-aligned matter under the same \(\mathbf B_{\rm eff}\).
4. **Galactic / SPARC-style:** if \(\boldsymbol\xi_{\rm cone}\) is nonzero, handedness-sensitive residuals should improve under a chiral extension — the observational test already flagged in the program notes.

---

## 8. Compact statement

The candidate propagation law is anomaly continuity for a texture-chirality density plus a CME-shaped constitutive current:

\[
\partial_t\rho_\chi+\nabla\cdot\mathbf J_\chi=S_{\rm top}-\Gamma_f\rho_\chi,
\qquad
\mathbf J_\chi=-D_\chi\nabla\rho_\chi+\kappa\rho_\chi\mathbf B_{\rm eff}+\boldsymbol\xi_{\rm cone}.
\]

Local changes in organization propagate because topology enforces inflow/outflow of the associated current; distant regions adjust to keep the full system anomaly-matched. Identity (index, soft sector, \(\chi_{\beta n}\)) is the lattice-earned half; influence (this continuity + constitutive law) is the continuum-effective completion still to be calibrated and tested.
