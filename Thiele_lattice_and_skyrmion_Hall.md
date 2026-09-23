# Thiele equation on lattice data + skyrmion Hall effect

Tony Kawas / 23 September 2026.

**Data used:** residual-validated L=10/12 pair and single soft modes (P₁, P₂, BT, χ_βn, Δλ, d).  
**Scope:** Map Thiele collective-coordinate dynamics onto *existing static* observables; identify what Hall physics would mean; state what is not yet measured.

Level I/II/III discipline preserved.

---

# Part 1 — Thiele equation (reminder)

Rigid defect, dissipative medium:

\[
\mathbf G\times\mathbf v + \alpha\,\mathcal D\,\mathbf v = \mathbf F
\]

| Symbol | Meaning |
|--------|--------|
| \(\mathbf v=\dot{\mathbf R}\) | velocity of defect center |
| \(\mathbf G\) | gyrocoupling vector, \(|\mathbf G|\propto N_{\rm def}\) or skyrmion number \(Q\) |
| \(\alpha\mathcal D\) | dissipative drag tensor |
| \(\mathbf F\) | total force (external + pinning + inter-defect) |

In components (planar motion, \(\mathbf G=G\hat{\mathbf z}\)):

\[
G v_y + \alpha D_{xx} v_x = F_x,
\qquad
-G v_x + \alpha D_{yy} v_y = F_y.
\]

Solving for velocity given force yields a **Hall angle**:

\[
\tan\theta_H
=
\frac{v_\perp}{v_\parallel}
=
\frac{G}{\alpha D}
\quad\text{(isotropic }\mathcal D\text{, order of magnitude)}.
\]

Nonzero \(G\) ⇒ drive and velocity are not collinear. That is the skyrmion Hall effect.

---

# Part 2 — Mapping Thiele symbols onto lattice objects

The lattice program has **no measured velocities**. Everything below is an **identification dictionary** for quasi-static and future dynamical tests.

| Thiele object | Lattice / continuum proxy | Available now? |
|---------------|---------------------------|----------------|
| Defect center \(\mathbf R\) | Core position (hedgehog center); for pairs, two centers \(\mathbf R_1,\mathbf R_2\) | Yes (geometry) |
| Topological charge entering \(G\) | \(N_{\rm def}=\pm 1\) per hedgehog; pair total 0 | Yes (by construction) |
| Soft identity | \(\chi_{\beta n}\approx-0.81\) (soft) vs \(+0.99\) (bulk) | Yes (residual-gated) |
| Molecular binding | \(P_1\approx P_2\), BT peak at intermediate \(d\) | Yes (L=10/12) |
| Hybridization scale | Soft splitting \(\Delta\lambda\sim 10^{-3}\)–\(10^{-4}\) | Yes |
| Inter-defect force \(\mathbf F_{\rm inter}\) | Derivative of effective pair potential vs \(d\); encoded in how soft eigenvalues and BT depend on \(d\) | Qualitative only |
| Dissipation \(\alpha\mathcal D\) | Inverse response timescale; related to \(\Gamma_f\), Wilson artefacts, hybridization rate | Not measured |
| Velocity \(\mathbf v\) | \(d\mathbf R/dt\) under adiabatic drive of mass texture | **Not measured** |
| Hall angle \(\theta_H\) | Angle between drive and displacement of weight / center | **Not measured** |

**Level-I content:** existence of \(G\propto N_{\rm def}\) and of a soft sector that carries it.  
**Level-II content:** any specific formula linking \(\Delta\lambda\) or BT to \(\alpha D\) or to \(|F_{\rm inter}|\).

---

# Part 3 — What static lattice data already constrain

## 3.1 Single defect

- Soft modes exist for H and AH with \(|\mathrm{QT}|\approx 0.84\), modest \(P_{\rm core}\).
- H ↔ AH spectral match ⇒ opposite topological charge, same energetics (as expected).
- Thiele reading: a single defect has nonzero \(G\) (sign of charge) and a drag channel; no partner force.

## 3.2 Pair (molecular regime)

From L=10/12 residual-validated scans:

| \(d\) | Regime | Thiele reading |
|-------|--------|----------------|
| 1 | Merged / defect_like, BT\(\sim 10^{-8}\) | Cores not independent; collective coordinate is one “bound” object; \(G_{\rm tot}\approx 0\) |
| 3–5 | Strict molecular, BT peak | Two centers with strong \(F_{\rm inter}\); soft multiplet = shared zero-mode structure of the molecule |
| 6 (L=12 max) | Shared but BT thins | \(F_{\rm inter}\) weakening; still not isolated on this volume |

**Balanced \(P_1\approx P_2\)** ⇒ the soft weight does not prefer one core. In Thiele language, the molecular ground state is a **bound pair** with total topological charge 0, so net gyrocoupling of the *molecule as a whole* vanishes, while each core retains opposite \(G\).

That is important for Hall physics (Part 5).

## 3.3 Soft splitting as a scale

\(\Delta\lambda\) is an energy (frequency) scale for hybridization. A crude mobility estimate (Level II only):

\[
\tau_{\rm hyb}\sim \frac{1}{\Delta\lambda}
\quad\Rightarrow\quad
\text{drag scale }\sim \alpha D \sim \frac{\text{inertia}}{\tau_{\rm hyb}}
\]

No calibrated inertia exists yet. So \(\Delta\lambda\) constrains a *timescale*, not a numerical Hall angle.

---

# Part 4 — Applying Thiele in the quasi-static limit (what you can do now)

At zero velocity, Thiele collapses to force balance:

\[
\mathbf F_{\rm tot}(\mathbf R)=0.
\]

A small static perturbation (boost mass on core 1 by \(\delta v_1\)) shifts the equilibrium:

\[
\delta\mathbf R \sim (\text{stiffness})^{-1}\delta\mathbf F.
\]

On the lattice, the measurable proxies are not geometric \(\delta\mathbf R\) (centers are fixed by the texture ansatz) but **soft weight sliding**:

\[
G_{12}
=
\frac{\partial(P_2-P_1)}{\partial(\delta v_1)}
\bigg|_{\rm soft},
\qquad
G_{\rm BT}
=
\frac{\partial\,\mathrm{BT}}{\partial(\delta v_1)}.
\]

**Thiele interpretation of \(G_{12}\):**

- Nonzero \(G_{12}\) ⇒ inter-defect force network transmits the boost from core 1 to core 2 (influence).
- Sign of \(G_{12}\) correlated with \(\chi_{\beta n}\) and pair axis ⇒ parity-odd structure consistent with gyro/texture coupling.
- If cores were independent, \(G_{12}\approx 0\).

This is the **static Thiele test** already flagged as the killer experiment. It does not measure \(\theta_H\); it measures whether the force sector of Thiele is active between cores.

---

# Part 5 — Skyrmion Hall effect in this setting

## 5.1 Standard skyrmion Hall effect

A driven skyrmion with topological charge \(Q\neq 0\) acquires a velocity component perpendicular to the drive:

\[
\theta_H=\arctan\frac{G}{\alpha D}\neq 0.
\]

Experimentally: current-driven skyrmions deflect; the sign of deflection tracks the sign of \(Q\).

## 5.2 What Hall would mean for hedgehog pairs

| Object | Net \(G\) | Expected Hall |
|--------|----------|---------------|
| Single H or AH | \(\propto \pm 1\) | Nonzero \(\theta_H\) under drive; opposite for H vs AH |
| Bound H–AH molecule | \(\approx 0\) | **No net Hall** of the molecule CM; possible *internal* relative Hall (cores push opposite ways) |
| Dissociated pair (large sep) | each \(\pm 1\) | Each core deflects oppositely under the same drive |

**Molecular regime (your data):** net topological charge of the soft multiplet is consistent with a charge-neutral molecule. So the **center of mass** of the pair should show little or no Hall deflection. What *can* appear is:

- opposite transverse response of the two cores,
- or sliding of soft weight along a direction not collinear with the pair axis if an effective drive has a transverse component.

That is a sharper prediction than “Hall exists somewhere.”

## 5.3 Texture chirality and Hall sign

Soft modes have \(\chi_{\beta n}<0\) (anti-aligned). In anomalous transport language, the sign of the chiral/Hall response tracks the sign of the texture density that couples to \(\mathbf B_{\rm eff}\). Level-II expectation:

\[
\mathrm{sign}(\theta_H)\;\text{or}\;\mathrm{sign}(G_{12})
\quad\text{correlates with}\quad
\mathrm{sign}(\chi_{\beta n})\times\mathrm{sign}(N_{\rm def}).
\]

Your residual-gated data already fix \(\mathrm{sign}(\chi_{\beta n})\) for soft modes. A Hall or static-response measurement would test whether that sign controls the transverse/sliding response.

## 5.4 What is *not* claimed

- No lattice velocity has been measured ⇒ no numerical \(\theta_H\).
- BT is **not** a Hall angle and **not** a current.
- Molecular BT peak is geometry of binding, not proof of gyroscopic motion.

---

# Part 6 — Concrete application recipe (static → quasi-Hall)

### Step A — Force sector (doable on Colab with current operator)

1. Fix L=10 or L=12, molecular \(d\) (e.g. 3 or 5).
2. Residual-gate soft multiplet (same gate as before).
3. Boost core-1 coupling: \(v_1\to v_1(1+\varepsilon)\), \(\varepsilon\sim 0.02\)–\(0.05\).
4. Recompute \(P_1,P_2,\mathrm{BT},\chi\).
5. Report

   \[
   G_{12}(\varepsilon)=\frac{(P_2-P_1)_\varepsilon-(P_2-P_1)_0}{\varepsilon},\qquad
   G_{\rm BT}(\varepsilon)=\frac{\mathrm{BT}_\varepsilon-\mathrm{BT}_0}{\varepsilon}.
   \]

6. Repeat with opposite boost and with roles of core 1/2 swapped (check linearity and reciprocity).

**Thiele reading:** nonzero \(G_{12}\) = active inter-defect force transmission.

### Step B — Hall-sector (future, needs drive + displacement)

1. Define a drive (e.g. slow adiabatic motion of both mass centers along \(\hat{\mathbf x}\), or an effective \(\mathbf B_{\rm eff}\) along the pair axis).
2. Track either geometric centers (if texture is allowed to move) or the first moment of soft density.
3. Measure transverse component of that moment’s drift ⇒ estimate \(\theta_H\).
4. Compare H vs AH (opposite sign) and molecule vs single (molecule CM ≈ 0).

Step B is beyond the present spectral pipeline.

---

# Part 7 — Skyrmion Hall effect: summary for the program

| Claim | Status |
|-------|--------|
| Single hedgehog has topological charge ⇒ nonzero gyrocoupling in Thiele | Level I (by construction) |
| Soft sector carries defect-aligned chirality \(\chi_{\beta n}\approx-0.81\) | Level I (lattice) |
| Bound H–AH molecule has net \(G\approx 0\) ⇒ weak CM Hall | Level I expectation |
| Internal / relative Hall or weight sliding can still occur | Level II expectation |
| Numerical Hall angle from lattice | **Not available** |
| BT or Δλ equal to \(\theta_H\) | **False** |

---

# Part 8 — Compact statements

**Thiele on lattice data:**  
Static residual-validated observables map onto Thiele’s *force and topology* sector (centers, \(N_{\rm def}\), molecular binding, soft chirality). They do not yet map onto velocity or Hall angle. The quasi-static susceptibility \(G_{12}\) is the correct first application of Thiele force balance to existing data.

**Skyrmion Hall effect:**  
Expected for single defects (sign tracks \(N_{\rm def}\)); suppressed for the center of mass of a charge-neutral molecular pair; possible as *relative* core response or soft-weight sliding. Confirming any of that requires a drive plus a transverse observable — not inferable from BT or Δλ alone.

**Next measurement:** Step A (one-core boost → \(G_{12}\), \(G_{\rm BT}\)) on residual-gated L=10/12 molecular pairs.
