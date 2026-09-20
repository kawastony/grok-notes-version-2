# Chiral density form details + Callias index theorem

Tony Kawas / 20 September 2026.

Connects the notes’ helical density, Callan–Harvey inflow, and the Callias index theorem to the lattice hedgehog program. TAFA floors and R_cone / geo_φ remain untouched.

---

## 1. Chiral density form — details from the notes

### Ingredients already present
- Transverse elongation \(\boldsymbol{\varepsilon}\) (network deformation)
- Radial mode \(\chi\) (Model D charge; domain-wall-like profile across the cone/defect)
- Local cone axis \(\hat{\mathbf{c}}\)
- Right-handed polarization triad:
  \[
  \mathbf{e}^{(1)}\times\mathbf{e}^{(2)}=\hat{\mathbf{k}},\quad
  \mathbf{e}^{(\pm)}=\tfrac1{\sqrt2}(\mathbf{e}^{(1)}\pm i\mathbf{e}^{(2)})
  \]
- Hedgehog topological density:
  \[
  \rho_{\rm top}=\frac1{4\pi}\varepsilon_{ijk}\,\mathbf{n}\cdot(\partial_j\mathbf{n}\times\partial_k\mathbf{n}),\quad
  \mathbf{n}=\boldsymbol{\varepsilon}/|\boldsymbol{\varepsilon}|
  \]

### Minimal helical density
\[
\boxed{
\mathcal{H}
:=
\chi\,\bigl(\hat{\mathbf{c}}\cdot(\boldsymbol{\varepsilon}\times\partial_t\boldsymbol{\varepsilon})\bigr)
}
\]

**Why this form**
| Property | Role |
|----------|------|
| Linear in \(\chi\) | Uses the radial mode already required for charge |
| Quadratic in \(\boldsymbol{\varepsilon}\) | Built from transverse network |
| Parity-odd | Changes sign under spatial inversion → true chirality |
| Projects onto \(\hat{\mathbf{c}}\) | Selects helicity along the defect |
| Unique (up to factor) | Minimal scalar with those symmetries |

### Action term
\[
S_{\rm chiral}
=
\frac{\kappa}{2}
\int\mathrm{d}t\,\mathrm{d}^3x\;
\chi\,\bigl(\hat{\mathbf{c}}\cdot(\boldsymbol{\varepsilon}\times\partial_t\boldsymbol{\varepsilon})\bigr).
\]
\(\kappa\) has dimensions of inverse velocity; **not yet fixed from first principles** in the notes.

### Continuum rewrite
With transverse potential \(\mathbf{A}\sim\boldsymbol{\varepsilon}_T\):
\[
\mathcal{H}\;\sim\;
\chi\,\hat{\mathbf{c}}\cdot(\mathbf{A}\times\partial_t\mathbf{A})
\]
or the static helicity density \(\mathbf{A}\cdot(\nabla\times\mathbf{A})\) projected on \(\hat{\mathbf{c}}\).

---

## 2. Callan–Harvey inflow (notes identification)

Classic Goldstone–Wilczek / Callan–Harvey current (3+1D):
\[
J^\mu_{\rm GW}
=
\frac{1}{8\pi^2}\,
\varepsilon^{\mu\nu\rho\sigma}
(\partial_\nu\phi)\,F_{\rho\sigma}.
\]
Divergence concentrates on the defect and cancels the anomaly of bound chiral zero-modes.

**Notes map**
\[
\phi\;\longleftrightarrow\;\chi,\qquad
F_{\rho\sigma}=\partial_\rho A_\sigma-\partial_\sigma A_\rho,\quad
\mathbf{A}=\boldsymbol{\varepsilon}_T.
\]
Inflow current in cone variables:
\[
\boxed{
J^\mu_{\rm inflow}
=
\frac{\kappa}{4\pi}\,
\varepsilon^{\mu\nu\rho\sigma}
(\partial_\nu\chi)\,(\partial_\rho A_\sigma)
}
\]
(static defect → spatial current along \(\hat{\mathbf{c}}\)).

This is the **anomaly-inflow** interpretation of the same chiral structure: bulk current cancels defect zero-mode anomaly.

---

## 3. Callias index theorem — standard statement

**Setting (Callias 1978).**  
Odd-dimensional open Euclidean space (physically relevant: static 3D).  
Dirac operator perturbed by a Hermitian mass/potential \(\Phi\) that is asymptotically homogeneous of degree 0 and invertible at infinity:
\[
L = -i\boldsymbol{\alpha}\cdot\nabla + \beta\Phi.
\]
\(L\) is Fredholm. The index is determined by the topology of the **unitarized mass at infinity**:
\[
\mathrm{Index}(L)
=
\text{(Chern character of the positive eigenspace bundle of }\Phi\text{ on the sphere at infinity)}.
\]
For an SU(2) hedgehog mass \(\Phi=\boldsymbol{\tau}\cdot\hat{\mathbf{r}}\,f(r)\) with \(f(\infty)>0\):
\[
\mathrm{Index}(L) = \pm 1
\]
(one chiral zero mode bound to the monopole/hedgehog).

**Physical content**
- Domain wall / monopole mass profile → chiral zero modes localized on the defect.
- Index = topological charge of the mass map \(S^2_\infty\to S^2\) (degree of the hedgehog).
- Lattice analogue: Wilson–Dirac + hedgehog mass texture; soft modes ≈ continuum zero modes when residual-gated.

**Relation to APS**  
Callias is the open-space / odd-dimensional relative of Atiyah–Patodi–Singer. On a domain wall, APS boundary conditions encode the same zero-mode counting.

---

## 4. How the three pieces fit the cone program

```
Hedgehog / cone defect
        │
        ├─ topological density ρ_top  →  integer N_def (degree)
        │
        ├─ radial profile χ          →  Callias mass Φ ~ χ · (τ·n̂)
        │                                 Index(D) = N_def  (target theorem)
        │
        └─ helical density H         →  chiral orientation of the defect
              │
              └─ Callan–Harvey inflow J_inflow
                    cancels anomaly of the Callias zero modes
```

| Layer | Object | Role |
|-------|--------|------|
| Topology | \(N_{\rm def}\), \(\rho_{\rm top}\) | Integer charge of the defect |
| Index | Callias Index\((D)\) | Counts chiral zero modes = \(N_{\rm def}\) |
| Orientation | \(\mathcal H\), \(S_{\rm chiral}\) | Selects which handedness the modes carry |
| Anomaly | \(J_{\rm inflow}\) | Bulk current that cancels mode anomaly |

**Lattice status (this repo)**  
Residual-gated soft modes on Wilson–Dirac + hedgehog at L=8–12 are consistent with Index ≈ N_def for single defects; continuum analytic proof is still open. Chirality diagnostics (QT, D1, etc.) probe orientation, not yet a measured index theorem.

---

## 5. What is derived vs open

| Item | Status |
|------|--------|
| Form of \(\mathcal H\) | **Derived** (minimal symmetry construction) |
| Form of \(S_{\rm chiral}\) | **Derived** (up to κ) |
| Inflow current map \(\chi\leftrightarrow\phi\) | **Identified** with Callan–Harvey |
| Callias Index\((D)=N_{\rm def}\) continuum theorem for cone mass | **Target**, not proved |
| Lattice soft-mode count ≈ N_def | **Numerical evidence** (residual-gated) |
| Value of κ from first principles | **Open** |
| Link of κ or Index to geo_φ / R_cone | **Not derived** |

---

## 6. Practical next calculations (if pursued)

1. **Spectral-flow index** on the lattice hedgehog: vary a continuous mass deformation and count eigenvalue crossings through zero → direct numerical Index.
2. **Localize** soft modes on the hedgehog core; measure chirality (overlap with \(\gamma_5\) or texture QT) as a function of N_def.
3. **Match κ**: require that the divergence of \(J_{\rm inflow}\) equals the anomaly polynomial of one Callias zero mode per unit N_def.
4. **Continuum limit**: extrapolate lattice Index vs L and residual gate to recover Callias.

---

## Compact statement

The chiral density \(\mathcal H=\chi\,\hat c\cdot(\boldsymbol\varepsilon\times\partial_t\boldsymbol\varepsilon)\) is the minimal parity-odd helical density built from cone variables already in the notes. Its associated inflow current is the Callan–Harvey current with \(\phi\leftrightarrow\chi\). The Callias index theorem says that a Dirac operator with hedgehog mass has Index = topological degree of the mass map at infinity — exactly the integer N_def the lattice program aims to recover. Orientation (chirality) selects the sign; inflow cancels the anomaly. Form-level derivation is in hand; continuum Index theorem and κ remain open.
