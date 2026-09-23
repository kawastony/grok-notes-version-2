# Topological defect dynamics and anomaly cancellation mechanisms

Tony Kawas / 23 September 2026.

Builds on `Propagation_law_annotated_levels.md`. Level I/II/III discipline preserved.

---

# Part 1 — Topological defect dynamics

## 1.1 What “dynamics of a defect” means

A topological defect has:

1. **Identity** — charge \(N_{\rm def}\) (or winding) stable under continuous deformation.
2. **Collective coordinates** — position \(\mathbf R(t)\), orientation, possible internal moduli.
3. **Equation of motion** for those coordinates, obtained by projecting the underlying field equation onto the translational (or rotational) zero mode of the defect.

The soft modes you measure on the lattice are the IR carriers of that identity. Defect *dynamics* is how \(\mathbf R(t)\) and the soft sector respond when the background or the other defects change.

---

## 1.2 Universal structure of the equation of motion

For a rigid defect in a dissipative medium, the projected dynamics takes a Thiele-like form (skyrmions, domain walls, and point defects share this skeleton):

\[
\mathbf G\times\mathbf v + \alpha\,\mathcal D\,\mathbf v = \mathbf F_{\rm ext}+\mathbf F_{\rm pin}+\mathbf F_{\rm inter}
\]

| Symbol | Meaning |
|--------|--------|
| \(\mathbf v=\dot{\mathbf R}\) | defect velocity |
| \(\mathbf G\) | gyrocoupling (topological; \(\propto N_{\rm def}\) or skyrmion number \(Q\)) |
| \(\alpha\mathcal D\) | dissipative drag tensor |
| \(\mathbf F_{\rm ext}\) | external drive |
| \(\mathbf F_{\rm pin}\) | pinning by impurities / lattice discreteness |
| \(\mathbf F_{\rm inter}\) | forces from other defects |

**Topological content:** the gyro term \(\mathbf G\times\mathbf v\) is parity-odd and proportional to the topological charge. It produces Hall-like transverse motion (skyrmion Hall effect) and suppresses ordinary diffusion of isolated defects.

**Connection to your lattice:** molecular H–AH pairs at finite separation are the discrete analogue of two defects with opposite charge interacting through the soft multiplet and the bridge. Soft splitting \(\Delta\lambda\) and BT are static diagnostics of that interaction; a time-dependent boost of one core is the first dynamical probe.

---

## 1.3 Classes of defect motion relevant to the program

| Class | Continuum picture | Lattice / cone analogue |
|-------|-------------------|-------------------------|
| Translation of a single hedgehog | Callias/Jackiw–Rossi soliton moving in a slowly varying background | Single-defect soft mode following a moving mass center |
| Pair binding / unbinding | H–AH molecule; molecular vs isolated regime | Your sep scan: intermediate \(d\) = molecular; large \(d\) = thinning bridge |
| Spectral flow under adiabatic drive | Eigenvalue branches cross zero as texture interpolates | Index_sf diagnostics (torus obstruction already noted) |
| Driven motion under effective current | Thiele with spin-transfer / spin-orbit–like drive | Level-II term \(\kappa\rho_\chi\mathbf B_{\rm eff}\) as drive on texture |
| Pinning and depinning | Defect trapped by core potential or lattice scale | Wilson core + finite \(L\); residual gate must stay passed |

---

## 1.4 Coarse-grained dynamics ↔ propagation law

Defect equations of motion are **particle-like**. The Level-I continuity equation is **field-like**:

\[
\partial_t\rho_\chi+\nabla\cdot\mathbf J_\chi=S_{\rm top}-\Gamma_f\rho_\chi.
\]

They match when:

- \(\rho_\chi\) is concentrated near defect cores (and on bridges in the molecular regime),
- \(\mathbf J_\chi\) includes the current carried by moving cores plus the anomaly-driven bulk current,
- \(S_{\rm top}\) accounts for creation/annihilation (pair production) allowed only in opposite-charge pairs.

So:

- **Thiele-type EOM** = dynamics of the *centers* (identity locations).
- **Propagation law** = dynamics of the *texture density and its current* (influence).

Both are needed. Lattice static response (\(G_{12}\)) is the bridge between them at zero frequency.

---

## 1.5 What lattice can already say about dynamics

| Observable | Static meaning | Dynamical upgrade |
|------------|----------------|-------------------|
| \(\chi_{\beta n}\approx-0.81\) | Soft identity | Orientation that couples to drive |
| \(P_1\approx P_2\), BT peak at intermediate \(d\) | Molecular binding | Channel for sliding weight under \(\delta v_1\) |
| Soft splitting \(\Delta\lambda\) | Hybridization scale | Inverse timescale for pair response |
| ST = 1 | Both cores anti-aligned | Sign structure of \(G_{12}\) |

None of these is a measured velocity yet. The first dynamical (or quasi-static) experiment remains: boost one core → measure \(\Delta(P_2-P_1)\) and \(\Delta\mathrm{BT}\).

---

# Part 2 — Anomaly cancellation mechanisms

Anomaly cancellation is why Level I exists. Different mechanisms cancel the same type of obstruction in different settings.

## 2.1 Why cancellation is required

A chiral theory with an anomalous global or gauge symmetry is inconsistent as a standalone quantum theory: the path integral is not invariant under the symmetry, unitarity/gauge invariance fails, or the effective action is not well-defined.

**Cancellation** means the total variation vanishes:

\[
\delta_\varepsilon W_{\rm total}=0.
\]

That can happen by:

1. **Spectrum cancellation** (fermion content cancels the anomaly polynomial),
2. **Inflow** from a higher-dimensional bulk,
3. **Green–Schwarz** coupling to a higher-form field,
4. **Local counterterms** that convert consistent ↔ covariant form (but do not remove a genuine anomaly by themselves).

---

## 2.2 Mechanism catalogue

### A. Callan–Harvey inflow (primary for this program)

- **Setting:** Defect (wall, string, hedgehog) hosts chiral zero modes; bulk is higher-dimensional or ambient space with a topological density.
- **How cancellation works:** Bulk Chern–Simons / Goldstone–Wilczek current has divergence supported only on the defect, equal and opposite to the edge anomaly.
- **Formula (cone variables, already locked):**

  \[
  J^\mu_{\rm inflow}
  =
  \frac{\kappa}{4\pi}\,
  \varepsilon^{\mu\nu\rho\sigma}(\partial_\nu\chi)(\partial_\rho A_\sigma),
  \qquad
  \kappa=\frac{R_{\rm cone}}{c}.
  \]

- **Level:** **I** — structure derived; coefficient from surface data.

### B. Jackiw–Rossi / Callias index matching

- **Setting:** Dirac operator in a hedgehog (or odd-D) background.
- **How cancellation works:** Index theorem fixes the net number of zero modes; spectral flow under adiabatic change of texture moves charge between bulk and core so that the total index is conserved.
- **Lattice avatar:** Wilson–Dirac + hedgehog; soft multiplet; attempted spectral-flow index (torus obstruction already diagnosed).
- **Level:** **I** for the index statement; continuum limit of soft chirality still open.

### C. Consistent vs covariant anomaly + Bardeen–Zumino polynomials

- **Consistent anomaly:** Comes from variation of an effective action; obeys Wess–Zumino consistency; may not be gauge-covariant.
- **Covariant anomaly:** Gauge-covariant form of the divergence; preferred for local conservation statements.
- **Relation:** They differ by a local Bardeen–Zumino current. Adding BZ polynomials converts one into the other; it does **not** cancel a nonzero anomaly polynomial by itself.
- **Use here:** When writing Level-I continuity, one works with the form appropriate to the current that couples to bulk inflow (covariant language is natural for \(\partial_\mu J^\mu\)).

### D. Green–Schwarz mechanism

- **Setting:** Typically string / higher-form theories; anomaly polynomial factorizes; a 2-form (or higher) field couples so that its gauge variation cancels the residual anomaly.
- **How cancellation works:** Classical variation of the GS term cancels the one-loop anomaly.
- **Use here:** Not the primary micro mechanism for the hedgehog lattice. Relevant only if a higher-form / residual network field is later elevated to play a GS role at galactic scale — currently **not claimed**.

### E. Spectrum cancellation (representation theory)

- **Setting:** Standard Model, chiral gauge theories.
- **How cancellation works:** Trace identities on fermion charges make the total anomaly coefficient vanish.
- **Use here:** Not how the defect system cancels its edge anomaly; the defect system uses **inflow**, not a second chiral species with opposite index in the same dimension.

### F. Defect-network / higher-form formulation

- **Setting:** Modern view of ’t Hooft anomalies via topological defect webs.
- **How cancellation works:** Rearrangement of defect lines/surfaces encodes the anomaly; consistency of the web is equivalent to anomaly freedom (or inflow from a bulk).
- **Use here:** Conceptual support for “change one defect → rest of network must adjust” without writing a continuum current — same physics as Level I in defect language.

---

## 2.3 What cancels what in *this* framework

| Anomalous object | Cancelling object | Mechanism |
|------------------|-------------------|-----------|
| Edge / zero-mode anomaly on hedgehog or wall | Bulk inflow current \(J_{\rm inflow}\) | Callan–Harvey |
| Change of local soft charge under texture motion | Spectral flow / soft multiplet rearrangement | Callias / lattice spectral flow |
| Effective continuum \(\partial_\mu J^\mu_\chi\) imbalance | \(S_{\rm top}\) and bulk \(\mathbf J_\chi\) | Level-I continuity |
| Residual macroscopic chiral density | Coarse-grained descendant of same inflow | Program identification (\(\boldsymbol\xi_{\rm cone}\)) |

Nothing in this list cancels anomalies by adding opposite-chirality continuum fermions in the same dimension. The cancellation is **inflow + index**, not SM-style spectrum cancellation.

---

## 2.4 Failure modes (when cancellation fails)

| Failure | Symptom | Relevance |
|---------|---------|-----------|
| Open boundary without bulk | Edge anomaly uncanceled | Lattice torus partially obstructs global index; local diagnostics still work |
| Wrong coefficient \(\kappa\) | Residual gauge/topological variation | Why \(\kappa\) is locked to \(R_{\rm cone}/c\) |
| Ignoring consistent vs covariant distinction | Wrong Ward identity for local current | Prefer covariant form for continuity equation |
| Treating GS as automatic at micro scale | Overclaim | GS not used in current lattice/cone claims |

---

# Part 3 — Joint picture: dynamics + cancellation

```
Topological charge N_def
        │
        ▼
Soft modes (identity)  ←→  Index / Callias
        │
        ▼
Edge anomaly on defect
        │
        ▼
Bulk inflow current (Callan–Harvey)     ←── anomaly cancellation
        │
        ▼
Level-I continuity for ρ_χ
        │
        ├── Thiele-like motion of defect centers (dynamics of identity locations)
        └── Level-II constitutive J_χ (dynamics of influence)
```

- **Cancellation** guarantees that the system can exist as a consistent quantum/continuum theory.
- **Dynamics** says how the defect centers and the texture density move once the system exists.
- **Propagation law** is the field-level expression of that dynamics under the constraint of cancellation.

---

# Part 4 — Status relative to the program

| Item | Level | Status |
|------|-------|--------|
| Inflow cancellation structure | I | Derived (Callan–Harvey + locked \(\kappa\)) |
| Index ↔ soft sector | I | Derived on lattice for local diagnostics; global spectral flow obstructed on torus |
| Thiele-like EOM for defect centers | II | Standard continuum template; not yet fitted to lattice |
| Constitutive \(\mathbf J_\chi\) | II | Minimal symmetry-allowed ansatz |
| One-core response \(G_{12}\) | Test | Not yet run at L=12 (static first step toward dynamics) |
| Green–Schwarz at micro scale | — | Not claimed |
| Agency / vision-path-boundary | III | Interpretation only |

---

# Part 5 — Compact statements

**Defect dynamics:**  
Topological defects move under a gyroscopic + dissipative + force balance (Thiele-type). The gyro term is proportional to topological charge. Soft modes and bridges are the lattice window on that motion; quasi-static response is the first measurable step.

**Anomaly cancellation:**  
The operative mechanism for this framework is **Callan–Harvey inflow** (plus Callias/Jackiw–Rossi index matching), not Green–Schwarz or SM spectrum cancellation. Inflow forces bulk current when defect content changes — that is the microscopic reason Level-I propagation exists.

**Together:**  
Cancellation makes the theory consistent; dynamics says how identity centers and texture currents evolve under that consistency constraint.
