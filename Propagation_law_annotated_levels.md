# Propagation law — annotated levels + symmetry table + anomaly inflow

Tony Kawas / 23 September 2026.

**Purpose:** Strengthen the effective-theory program by (1) strict separation of derived / ansatz / interpretation, (2) symmetry classification of the constitutive current, (3) a sharper survey of anomaly-inflow mechanisms that justify the continuity spine.

---

# Part A — Three-level annotation

## Level I — Derived (keep in core claims)

These pieces follow from topology + anomaly matching + lattice diagnostics without new free functions.

| Statement | Basis |
|-----------|--------|
| Defects carry integer (or ℤ) topological charge \(N_{\rm def}\) | Homotopy of the mass/Higgs map; lattice hedgehog |
| Soft sector exists and is organized by defect-aligned texture operator \(\beta\otimes(\tau\cdot\hat n)\) | Residual-gated L≤12 numerics: \(\chi_{\beta n}\approx -0.81\) soft vs \(+0.99\) bulk |
| Local anomaly on defect-bound modes must be cancelled for consistency of the full system | Standard QFT (’t Hooft anomaly / Callan–Harvey) |
| Bulk supplies an inflow current whose divergence is supported on the defect | Callan–Harvey / Goldstone–Wilczek structure |
| Effective continuity for a coarse-grained texture density | Anomaly continuity promoted to continuum: \(\partial_t\rho_\chi+\nabla\cdot\mathbf J_\chi=S_{\rm top}-\Gamma_f\rho_\chi\) |
| Coefficient \(\kappa\) fixed by existing surface data | \(\kappa=R_{\rm cone}/c=\sqrt6/(\varphi\,c)\) — no new parameter |
| Local change of \(\rho_\chi\) cannot be isolated: continuity + topology force remote adjustment | Direct consequence of Level-I continuity |

**Level-I law (structure only):**

\[
\partial_t\rho_\chi + \nabla\cdot\mathbf J_\chi = S_{\rm top} - \Gamma_f\rho_\chi
\]

with \(S_{\rm top}\) the anomaly/topological source density and \(\Gamma_f\) a UV/finite-volume sink. The *existence* of \(\mathbf J_\chi\) is derived; its detailed constitutive form is Level II.

---

## Level II — Effective ansatz (mark as model, not theorem)

These pieces are motivated and minimal, but **not uniquely forced** until a symmetry classification or matching calculation selects them.

| Piece | Status | What would promote it to Level I |
|-------|--------|----------------------------------|
| Identification \(\rho_\chi=\mathrm{Tr}\,\rho_{\rm soft}[\beta\otimes(\tau\cdot\hat n)]\) | Motivated by lattice; continuum limit not extrapolated | \(\chi_{\beta n}(L)\to\chi_\infty\) under refinement |
| \(\mathbf J_\chi=-D_\chi\nabla\rho_\chi+\kappa\rho_\chi\mathbf B_{\rm eff}+\boldsymbol\xi_{\rm cone}\) | Minimal CME-shaped constitutive law | Symmetry table + matching or lattice response |
| Scalar diffusivity \(D_\chi>0\) | Standard dissipative term | Extract from hybridization timescale vs sep |
| Effective axial field \(\mathbf B_{\rm eff}\) | Placeholder until defined | Micro definition (see Part C) |
| Residual \(\boldsymbol\xi_{\rm cone}\) | Program-specific macroscopic piece | SPARC / handedness residual test |
| Linear response, no memory kernel | Simplest Markovian closure | Data requiring retardation → upgrade |

**Level-II constitutive law (ansatz):**

\[
\mathbf J_\chi
=
-D_\chi\nabla\rho_\chi
+\kappa\,\rho_\chi\,\mathbf B_{\rm eff}
+\boldsymbol\xi_{\rm cone}
\]

---

## Level III — Interpretation (philosophy of state selection; not predictive physics)

| Claim | Role |
|-------|------|
| Mountain / valley split | Valley = propagation given a defect pattern (determinative). Mountain = which pattern/orientation is instantiated (selection). |
| Choice / agency | Capacity to select or stabilize a topologically allowed sector or orientation — **not** a term inside \(\mathbf J_\chi\). |
| Puzzle analogy | Pieces = identity content; rebalancing = Level-I continuity; choosing which piece to move = Level III. |
| *Sisyphus*-style loop | Narrative image of identity + influence coupled; **not** a physical time-travel mechanism. |

Level III must not be used as a substitute for Level-I derivation or Level-II calibration.

---

# Part B — Symmetry table for \(\mathbf J_\chi\)

Aim: show that the Level-II form is the **minimal local, first-order, parity-odd-compatible** constitutive basis, and list what was omitted.

### Transformation rules (effective 3+1 continuum)

| Object | P (parity) | T (time reversal) | Charge / texture sign |
|--------|------------|-------------------|------------------------|
| \(\rho_\chi\) | odd (pseudo-scalar density) | even | flips with \(N_{\rm def}\) orientation |
| \(\nabla\rho_\chi\) | odd × vector → axial vector | even | — |
| \(\mathbf J_\chi\) | vector (current) | odd | — |
| \(\mathbf B_{\rm eff}\) | axial vector (like B) | odd | — |
| \(\kappa\) | scalar, P-even, T-even | — | locked positive from \(R_{\rm cone}/c\) |
| \(D_\chi\) | scalar, P-even, T-even | — | >0 dissipative |

### Allowed lowest-order local terms

| Term | P | T | In Level-II law? | Reason |
|------|---|---|------------------|--------|
| \(-D_\chi\nabla\rho_\chi\) | ✓ vector | ✓ odd | **Yes** | Standard diffusion; entropy-producing |
| \(\kappa\rho_\chi\mathbf B_{\rm eff}\) | ✓ (pseudo × axial → vector) | ✓ odd | **Yes** | Anomaly / CME-type structure |
| \(\sigma\,\mathbf E_{\rm eff}\) | ✓ | ✓ | Optional | Ohmic-like; omit until needed |
| \(\lambda\nabla\times\mathbf B_{\rm eff}\) | ✓ | ? | Optional | Higher structure; omit at leading order |
| \(\alpha\partial_t\nabla\rho_\chi\) | ✓ | even (wrong T) | **No** | Breaks T of current unless compensated |
| Memory kernel \(\int K(t-t')\nabla\rho_\chi\) | ✓ | depends | **No** | Non-Markovian upgrade if data demand |
| \(c\,\rho_\chi\nabla\rho_\chi\) | ✓ | ✓ | **No** | Nonlinear; higher order in amplitude |
| Pure \(\boldsymbol\xi_{\rm cone}\) (background residual) | model-dependent | model-dependent | **Yes (program)** | Macroscopic chiral residual; not forced by micro symmetry alone |

### Conclusion of the table

- At leading order, local, linear, P/T-compatible transport of a pseudo-scalar texture density, the basis is essentially:

  \[
  \mathbf J_\chi \supset -D\nabla\rho_\chi + \kappa\rho_\chi\mathbf B_{\rm eff}
  \]

- \(\boldsymbol\xi_{\rm cone}\) is an **extra program term** (Level II, framework-specific), not required by the universal symmetry classification.
- Uniqueness is **not** claimed: other terms are allowed but higher-order, dissipative-redundant, or postponed until data require them.

This is the correct strength of claim: **minimal symmetry-allowed ansatz**, not **the unique EFT**.

---

# Part C — Anomaly inflow mechanisms (survey)

## C1. Classic Callan–Harvey (domain wall / string)

- **Setup:** Real scalar (or phase) interpolates across a codimension-1 wall or winds on a codimension-2 string; chiral zero modes bound to the defect.
- **Anomaly:** Lower-dimensional chiral fermions produce \(\partial_\mu J^\mu_{\rm edge}=\mathcal A[F]\).
- **Inflow:** Bulk Chern–Simons / Goldstone–Wilczek current

  \[
  J^\mu_{\rm GW}\propto\varepsilon^{\mu\nu\rho\sigma}(\partial_\nu\phi)F_{\rho\sigma}
  \]

  has divergence supported only on the defect, cancelling \(\mathcal A\).
- **Use here:** Map \(\phi\leftrightarrow\chi\), \(A\leftrightarrow\boldsymbol\varepsilon_T\); recover the locked-\(\kappa\) inflow already written in the cone notes.

## C2. Jackiw–Rossi / Callias (hedgehog in odd dimensions)

- **Setup:** Dirac fermion coupled to a hedgehog Higgs/mass texture in 3D (or Callias index in odd-D).
- **Index:** \(\mathrm{Index}(D)=N_{\rm def}\) (under suitable asymptotics).
- **Inflow content:** Zero modes are the IR carriers of the index; changing the texture (or separating hedgehog–antihedgehog) changes the soft spectrum and forces spectral flow / charge rearrangement — the lattice analogue of inflow.
- **Use here:** Lattice Wilson–Dirac + hedgehog is the discrete avatar. Soft \(\chi_{\beta n}\) is the order-parameter diagnostic of that sector.

## C3. Consistent vs covariant anomaly and descent

- **Consistent anomaly:** Variation of an effective action (e.g. Chern–Simons); satisfies Wess–Zumino consistency.
- **Covariant anomaly:** Gauge-covariant form preferred for local current conservation statements.
- **Descent equations:** Relate bulk topological density → boundary anomaly polynomial.
- **Use here:** Level-I continuity is the effective statement that the *full* (bulk+defect) system is non-anomalous; the split into edge anomaly + bulk inflow is the descent in continuum language.

## C4. Anomalous hydrodynamics / chiral magnetic effect (CME)

- **Setup:** Relativistic fluid with anomalous global symmetries.
- **Constitutive current:** \(\mathbf J\supset\kappa\mu\mathbf B\) (and related vortical terms).
- **Use here:** Supplies the *shape* of the Level-II term \(\kappa\rho_\chi\mathbf B_{\rm eff}\). In the framework, \(\rho_\chi\) plays a role analogous to a chiral chemical-potential density, and \(\mathbf B_{\rm eff}\) to an emergent axial field. This is an analogy for constitutive structure, **not** a claim that the defect network is a quark-gluon plasma.

## C5. Defect networks and higher-form constraints

- Modern view: anomalies of continuous symmetries can be detected from topological defect webs; inflow is the bulk dual of defect rearrangement.
- **Use here:** Changing one defect (or its orientation) is a local rearrangement; the rest of the network must adjust to preserve global consistency — the same logic as Level-I propagation, now phrased in defect-network language.

## C6. What inflow does *not* by itself give

| Claim | Inflow alone? |
|-------|----------------|
| Continuity structure | **Yes** |
| Existence of a bulk current into the defect | **Yes** |
| Exact value of \(D_\chi\) | **No** |
| Unique form of all constitutive terms | **No** |
| Identification of \(\mathbf B_{\rm eff}\) with a specific lattice field | **No** |
| Agency / mountain selection | **No** (Level III) |

Inflow is the **spine** of Level I. Constitutive detail is Level II. Choice is Level III.

---

# Part D — Pinning \(\mathbf B_{\rm eff}\) (concrete options)

Until one is chosen and tested, \(\mathbf B_{\rm eff}\) remains the main Level-II vulnerability.

| Candidate definition | How to extract | Pros | Cons |
|---------------------|----------------|------|------|
| Soft-mode texture gradient \(\nabla\times\mathbf n_{\rm soft}\) or dual of \(\rho_\chi\) gradient | From lattice soft eigenvectors | Local, lattice-native | Noisy at small L |
| Pair-axis field (unit vector from core1→core2, weighted by BT) | Geometry of residual-validated pairs | Simple, already in code | Only defined for pairs |
| Emergent magnetic field from network connection \(A=\boldsymbol\varepsilon_T\) | Continuum limit of elongation | Matches Callan–Harvey \(B=\nabla\times A\) | Requires continuum map |
| Dual of topological density \(*\rho_{\rm top}\) | From \(\mathbf n\cdot(\partial\mathbf n\times\partial\mathbf n)\) | Directly topological | May vanish in molecular regime |

**Recommended first lock:** pair-axis / bridge-aligned field for the static response test (one core boosted → measure sliding of weight along the pair axis). That uses only objects already computed at L=10/12.

---

# Part E — One observable response (for the killer test)

Define a static susceptibility (lattice-realizable):

\[
G_{12}
=
\frac{\partial(P_2-P_1)}{\partial(\delta v_1)}
\bigg|_{\rm soft\ multiplet}
\]

where \(\delta v_1\) is a small boost of the mass coupling on core 1 only.

**Level-I expectation:** \(G_{12}\neq 0\) (influence exists).  
**Level-II expectation:** sign of sliding correlated with \(\chi_{\beta n}\) and pair-axis orientation; magnitude sensitive to sep and \(\kappa\)-scale.  
**Null / alternative:** pure independent cores → \(G_{12}\approx 0\) at fixed residual gate.

This is the discriminating check already flagged in the program.

---

# Part F — Compact status box

\[
\boxed{
\begin{array}{ll}
\textbf{Level I (derived)} &
\partial_t\rho_\chi+\nabla\cdot\mathbf J_\chi=S_{\rm top}-\Gamma_f\rho_\chi
\\
\textbf{Level II (ansatz)} &
\mathbf J_\chi=-D_\chi\nabla\rho_\chi+\kappa\rho_\chi\mathbf B_{\rm eff}+\boldsymbol\xi_{\rm cone}
\\
\textbf{Level III (interpretation)} &
\text{mountain = sector selection;\ valley = determinative propagation}
\end{array}
}
\]

Anomaly inflow (Callan–Harvey, Callias/Jackiw–Rossi, anomalous hydro constitutive shape) justifies Level I and motivates Level II. It does not by itself fix \(D_\chi\) or \(\mathbf B_{\rm eff}\). Choice remains Level III.

**Next physical step:** static one-core response → \(G_{12}\), with \(\mathbf B_{\rm eff}\) taken along the pair axis.
