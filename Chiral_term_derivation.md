# Mathematical Derivation of the Chiral Term for the Microscopic Cone

Tony Kawas / 14 September 2026.  
Builds on cone defect topology, hedgehog, polarization basis, radial mode χ, and the earlier chi-flow intuition (one handedness facilitates energy flow / relaxation; opposite impedes / tension).

All TAFA geometry, floors, R_cone = √6/φ and (11/72)_cone = Δy/φ remain untouched. Only an orientation (handedness) is added to the existing defect.

---

## 1. Geometric ingredients already present

- Vector elongation ε (transverse outside cores).
- Radial (longitudinal) mode χ used for static charge (Model D).
- Local cone axis or defect normal ĉ (unit vector along the preferred radial or screw direction of the vacancy/interstitial).
- Polarization triad already constructed as a **right-handed** frame:

\[
\mathbf{e}^{(1)}\times\mathbf{e}^{(2)}=\hat{\mathbf{k}},\qquad
\mathbf{e}^{(\pm)}=\frac1{\sqrt2}\bigl(\mathbf{e}^{(1)}\pm i\mathbf{e}^{(2)}\bigr).
\]

The existence of a preferred orientation on the triad is the seed of chirality.

- Topological density of the hedgehog:

\[
\rho_{\mathrm{top}}=\frac1{4\pi}\varepsilon_{ijk}\,\mathbf{n}\cdot(\partial_j\mathbf{n}\times\partial_k\mathbf{n}),\qquad
\mathbf{n}=\boldsymbol{\varepsilon}/|\boldsymbol{\varepsilon}|.
\]

The cross product already carries a handedness; the integer N_def can be signed once an orientation of the map is chosen.

---

## 2. Minimal chiral density from the triad and the radial mode

Define the local **helical density** relative to the cone axis ĉ:

\[
\mathcal{H}
:=
\chi\,\bigl(\hat{\mathbf{c}}\cdot(\boldsymbol{\varepsilon}\times\partial_t\boldsymbol{\varepsilon})\bigr).
\]

This is the unique scalar (up to overall factor) that is

- linear in the radial mode χ already required for charge,
- quadratic in the transverse elongation,
- parity-odd (changes sign under spatial inversion),
- time-odd in a way that selects a preferred sense of rotation about ĉ.

(The cross product ε × ∂t ε is the continuum analogue of angular momentum density of the deformation; projecting onto ĉ extracts the helicity along the defect.)

---

## 3. Chiral contribution to the action

Add the local term to the existing network action:

\[
S_{\mathrm{chiral}}
=
\frac{\kappa}{2}
\int\mathrm{d}t\,\mathrm{d}^3x\;
\chi\,\bigl(\hat{\mathbf{c}}\cdot(\boldsymbol{\varepsilon}\times\partial_t\boldsymbol{\varepsilon})\bigr).
\]

The coefficient κ has dimensions of inverse velocity (or inverse speed of the network) and will be fixed by the same surface data that produce R_cone (no new free parameter).

Variation with respect to ε yields an additional force density on the transverse modes:

\[
\mathbf{f}_{\mathrm{chiral}}
=
\kappa\,\chi\,(\hat{\mathbf{c}}\times\partial_t\boldsymbol{\varepsilon})
+
\text{(total-derivative terms that integrate to boundary contributions)}.
\]

The term linear in ∂t ε acts as a **gyroscopic** (velocity-dependent) force whose sign is controlled by the product κ χ ĉ.  One sign lowers the effective inertia of one circular polarization; the opposite sign raises it.

---

## 4. Effect on circular polarizations (explicit)

Decompose a plane-wave packet propagating along k̂ into the circular basis already derived:

\[
\boldsymbol{\varepsilon}
=
\mathrm{Re}\Bigl\{
\bigl(a_+\mathbf{e}^{(+)}+a_-\mathbf{e}^{(-)}\bigr)
e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}
\Bigr\}.
\]

Substitute into the chiral density. After time-averaging one obtains

\[
\langle\mathcal{H}\rangle
\propto
\chi\,(\hat{\mathbf{c}}\cdot\hat{\mathbf{k}})\,\bigl(|a_+|^2-|a_-|^2\bigr).
\]

Thus the chiral term splits the two helicities:

\[
\omega_\pm
=
c\lvert\mathbf{k}\rvert
\pm
\frac{\kappa\chi}{2\mu}\,(\hat{\mathbf{c}}\cdot\hat{\mathbf{k}})\,\lvert\mathbf{k}\rvert
+
O(\kappa^2).
\]

(μ is the inertia density of the network action.)  
One circular polarization propagates faster (lower effective resistance → “relax / energy flows more easily”); the opposite polarization is slowed (higher resistance → “tense”).  This is the precise continuum translation of the earlier chi-flow intuition.

---

## 5. Fixing the coefficient from existing surface data

On the activation surface one already has the locked relations

\[
A''=-2,\qquad(\phi')^2=6,\qquad R_{\mathrm{cone}}=\sqrt6/\varphi.
\]

The same surface supplies a preferred orientation (the outward normal of the wall can be identified with ĉ).  Dimensional matching of the gyroscopic term to the Einstein-scalar surface stress gives

\[
\kappa
=
\frac{R_{\mathrm{cone}}}{c}
=
\frac{\sqrt6}{\varphi\,c}.
\]

(The factor R_cone converts the geometric warp into a velocity scale; c is the already-emergent network speed.)  No new constant is introduced.

Consequently the frequency split is completely determined:

\[
\frac{\Delta\omega}{\omega}
=
\frac{\kappa\chi}{2\mu c}
(\hat{\mathbf{c}}\cdot\hat{\mathbf{k}})
=
\frac{R_{\mathrm{cone}}\,\chi}{2\mu c^2}
(\hat{\mathbf{c}}\cdot\hat{\mathbf{k}}).
\]

---

## 6. Topological protection of the sign

Because the hedgehog map carries an integer degree N_def, the overall sign of χ (or of the orientation of ĉ relative to the map) cannot be flipped by continuous deformation without passing through a core singularity.  Thus the preferred handedness is topologically stable once a given defect is formed — exactly as the integer charge is stable.

---

## 7. Summary of the chiral term

**Action density**
\[
\mathcal{L}_{\mathrm{chiral}}
=
\frac{\kappa}{2}\,
\chi\,\bigl(\hat{\mathbf{c}}\cdot(\boldsymbol{\varepsilon}\times\partial_t\boldsymbol{\varepsilon})\bigr),
\qquad
\kappa=\frac{\sqrt6}{\varphi\,c}=\frac{R_{\mathrm{cone}}}{c}.
\]

**Observable consequence**  
Circular polarizations of the transverse elongation wave acquire opposite group-velocity shifts proportional to χ (ĉ · k̂).  One sense of helicity is facilitated (energy flows more freely → relaxation analogue); the opposite sense is impeded (tension analogue).

**Status relative to prior notes**  
- Uses only objects already present (χ, ε, polarization triad, R_cone, activation surface).  
- Introduces no free parameter.  
- Leaves all previous TAFA results, 11/72 and R accounting, and Maxwell exterior theory unchanged.  
- Supplies the microscopic geometric origin of the directional chi-flow effect described in earlier papers.

---

## 8. Next natural checks

1. Insert the term into the lattice discretization and verify the helicity-dependent dispersion on a finite cone network.  
2. Couple the same chiral density to the topological current and examine possible chiral-magnetic-like effects on moving defects.  
3. Confirm that the surface value of κ remains stable under the same 5-D integration that produced Δy.
