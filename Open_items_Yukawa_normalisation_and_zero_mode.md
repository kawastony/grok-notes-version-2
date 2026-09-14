# Open items: Yukawa normalisation, continuum zero-mode profile, global cancellation

Tony Kawas / 15 September 2026.  
First concrete work on the three open points left by the Callan-Harvey investigation.

---

## 1. Minimal Yukawa coupling (new but minimal)

The notes contain no prior fermion content. We therefore introduce the unique lowest-order coupling of a Dirac fermion to the existing radial mode:

\[
\mathcal{L}_{\mathrm{Yukawa}}
=
-g\,\chi\,\bar{\psi}\psi
\]
(or the chiral version \(-g\chi\,\bar{\psi}i\gamma^5\psi\) if the representation demands it).  
The coupling constant \(g\) has dimensions of mass (or inverse length) once \(\chi\) is taken dimensionless, or is dimensionless if \(\chi\) carries mass dimension.  
We keep \(g\) explicit for the moment and fix it by anomaly matching.

No other new fields or scales are introduced.

---

## 2. Fixing the numerical factor (anomaly matching)

### 2.1 Standard anomaly of the zero-modes

A single left-handed Weyl fermion in 3+1 dimensions has the consistent axial anomaly
\[
\partial_\mu j_5^\mu
=
\frac{e^2}{16\pi^2}\,\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=
\frac{e^2}{2\pi^2}\,\mathbf{E}\cdot\mathbf{B}
\]
(with the conventional factor for one Weyl species; the precise 2\(\pi\) counting depends on whether one uses the consistent or covariant form).  
For \(N_{\mathrm{def}}\) zero-modes of the same chirality the anomaly is multiplied by \(N_{\mathrm{def}}\).

(The factor-of-two distinction between consistent and covariant anomalies is the classic Callan-Harvey point; the bulk inflow supplies the covariant form, while the world-volume theory sees the consistent form. A local counter-term on the defect converts one into the other.)

### 2.2 Divergence of the geometric inflow current

From the earlier derivation
\[
\partial_\mu J^\mu_{\mathrm{inflow}}
=
\frac{\kappa}{4\pi}\,N_{\mathrm{def}}\,(\mathbf{E}\cdot\mathbf{B})\Big|_{\mathrm{defect}}
\]
(up to the conventional placement of \(2\pi\) factors inside the definition of the topological density of \(\chi\)).

### 2.3 Matching condition

Require that the geometric inflow exactly cancel the zero-mode anomaly:
\[
\frac{\kappa}{4\pi}\,N_{\mathrm{def}}
=
N_{\mathrm{def}}\times(\text{standard anomaly coefficient per zero-mode}).
\]
This fixes the overall normalisation of the continuum field \(\chi\) (or equivalently the product \(g\times(\text{jump of }\chi)\)) relative to the canonical axial anomaly.  
Because \(\kappa=R_{\mathrm{cone}}/c\) is already locked, the matching determines the dimensionless combination
\[
\frac{g\,\Delta\chi}{(\text{canonical scale})}
\]
once and for all.  
No new free parameter survives; the Yukawa strength is fixed by the same surface data that produce \(R_{\mathrm{cone}}\).

(The explicit numerical value of the combination depends on the chosen units of \(\chi\) and on whether one matches the consistent or the covariant form; the important statement is that a unique matching exists and is fixed by geometry.)

---

## 3. Continuum zero-mode profile

### 3.1 Domain-wall (activation surface)

Let \(\chi(z)\) interpolate from \(\chi_-\) to \(\chi_+\) with opposite signs.  
The zero-mode equation reduces to the Jackiw–Rebbi ODE
\[
\bigl(-i\gamma^3\partial_z - g\chi(z)\bigr)\psi(z)=0.
\]
The normalisable solution of definite chirality is
\[
\psi(z)
=
\mathcal{N}\,
\exp\Bigl(-g\int_0^z\chi(z')\,\mathrm{d}z'\Bigr)
\times
(\text{constant chiral spinor}).
\]
Normalisation:
\[
\int_{-\infty}^{\infty}|\psi(z)|^2\,\mathrm{d}z=1
\]
fixes \(\mathcal{N}\).  
The profile is exponentially localised on the wall with width set by \(1/(g|\Delta\chi|)\).

### 3.2 Hedgehog (degree-\(N_{\mathrm{def}}\) core)

In the spherically symmetric hedgehog background the Dirac operator admits \(|N_{\mathrm{def}}|\) normalisable zero-modes.  
For the elementary degree-1 case the radial profile of the zero-mode is again of the form
\[
\mathcal{F}(r)
\propto
\exp\Bigl(-g\int_0^r\chi(\sigma)\,\mathrm{d}\sigma\Bigr),
\]
multiplied by the appropriate angular spinor that saturates the index.  
(The explicit angular form is the standard Jackiw–Rossi spinor; it need not be re-derived here.)

Both profiles are completely determined once \(g\) and the background \(\chi\) are known.  
They supply the “bump function” that smooths the defect source in the modern treatment of anomaly inflow.

---

## 4. Global cancellation

Consider a large closed region of the network that contains many defects.  
The total topological charge inside the region is
\[
N_{\mathrm{tot}}=\sum_i N_{\mathrm{def}}^{(i)}.
\]
By the index theorem the net number of chiral zero-modes is likewise \(N_{\mathrm{tot}}\).  
The total inflow into the region is proportional to \(N_{\mathrm{tot}}\).  

If the region is topologically trivial (or if the network is compact without boundary), the only consistent possibility is
\[
N_{\mathrm{tot}}=0.
\]
Defects must therefore appear in pairs of opposite topological charge, or the net charge must be cancelled by boundary modes.  
This is the geometric analogue of anomaly cancellation by equal numbers of left- and right-handed species, or by the requirement that the total instanton number on a closed manifold vanishes.

In the residual-network (galactic) limit the same statement becomes: the net residual chiral torque averaged over a large volume vanishes unless a net topological charge is present.  That is a sharp, testable selection rule for the SPARC winding-sense split: a statistically significant global handedness would require a net \(N_{\mathrm{tot}}\neq0\) on cosmological scales, which is already constrained by the absence of a large cosmic birefringence or related parity-odd observables.

---

## 5. Status after this note

| Open item | Status after this note |
|---|---|
| Precise numerical factor (Yukawa / anomaly matching) | Fixed in principle by matching; explicit numerical value awaits only a choice of units for \(\chi\) |
| Continuum zero-mode wave-function | Written (Jackiw–Rebbi / Jackiw–Rossi profiles) |
| Global cancellation | Stated: net \(N_{\mathrm{tot}}=0\) on closed regions; selection rule for residual torque |
| Discrete lattice zero-mode | Still open (next discrete step) |

---

## 6. Recommended immediate follow-up

1. Choose a definite normalisation convention for \(\chi\) (e.g. the jump across the activation surface equals 1, or equals the value already used in Model D for static charge).  
2. Insert that convention into the matching condition and write the final numerical prefactor in the inflow current.  
3. On the lattice side, discretise the hedgehog profile on a small cubic or tetrahedral patch of the cone network and solve the resulting finite-dimensional Dirac eigenvalue problem to confirm a near-zero mode of the expected chirality.

All three open items are now under active reduction; none requires a new free parameter beyond those already locked by the activation surface.
