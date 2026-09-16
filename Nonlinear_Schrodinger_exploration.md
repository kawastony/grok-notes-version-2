# Nonlinear Schrödinger equation — exploration and links to the cone/chirality program

Tony Kawas / 16 September 2026.

---

## 1. Basic structure

The focusing/defocusing nonlinear Schrödinger equation (NLS) in d spatial dimensions:

\[
 i\partial_t\psi = -\tfrac12\Delta\psi + g|\psi|^{2}\psi + V(x)\psi
\]

(or with higher-order nonlinearities, self-steepening, etc.). Conserved quantities: mass (L² norm), energy, momentum. In 1D the cubic NLS is integrable (inverse scattering); in higher D it supports solitary waves, vortices, and collapse regimes.

---

## 2. Topological objects in NLS

### Vortices (2D)
Stationary states of the form
\[
\psi(r,\phi,t)=f(r)e^{im\phi}e^{-i\mu t},\qquad m\in\mathbb Z,
\]
carry integer winding (topological charge) m. The density vanishes at the origin; the phase winds by 2πm. Stability depends on the nonlinearity (cubic, cubic–quintic, LHY correction, etc.).

### Dark / bright solitons (1D)
- Bright: sech-type envelope in focusing media.  
- Dark: density dip with a π phase jump in defocusing media.  
Both are topologically protected in the sense of a nonzero winding or topological charge of the phase.

### Higher-dimensional and chiral variants
- Chirped chiral solitons appear when self-steepening / self-frequency-shift terms break left–right symmetry; chirality is controlled by the sign of the self-steepening coefficient.  
- Vortex rings, hopfions, and skyrmion-like textures arise in multi-component or spinor NLS and in related continuum models (chiral magnets, chiral liquid crystals).

---

## 3. Relation to the Callias / hedgehog program

| Feature | NLS vortices / solitons | Callias hedgehog (our 8-component setup) |
|---------|-------------------------|------------------------------------------|
| Topology | π₁(S¹) winding of phase | π₂(S²) degree of mass-map Φ̂ |
| Zero / soft modes | Core of vortex is a density zero; phase singular | Protected fermionic zero modes at the defect |
| Index | Integer winding m | Index = N_def (Callias) |
| Chirality | Chirped / chiral solitons from higher-order terms | Chiral residual / inflow from defect orientation |
| Scale | Nonlinear continuum field | Lattice Dirac + topological mass texture |

**Conceptual bridge**  
Both systems realise integer topological charges that force soft or zero modes localised on a defect core. In NLS the “charge” is carried by the phase of a complex scalar; in Callias it is carried by the asymptotic map of a matrix-valued mass. The lattice work is the fermionic, index-theoretic counterpart of the bosonic vortex/soliton story.

A possible concrete link for the cone program: the radial profile f(r) of the hedgehog mass is analogous to the vortex core function f(r) of an NLS vortex. The alternative profiles we tested (tanh, exp, sech², compact, sharp) are the same families used for NLS vortex cores. The persistent hybridization at finite separation is the same molecular-regime phenomenon seen when two NLS vortices are brought close together (bonding/antibonding phase patterns).

---

## 4. Chirality across scales (NLS angle)

- **Microscopic / optical:** chirped chiral solitons; optical vortices with intrinsic spin–orbit structure (meronic spin defects at vortex cores).  
- **Mesoscopic:** chiral liquid-crystal solitons, skyrmions, hopfions; defects that are incompatible with uniform chirality are topologically forbidden or force opposite-handedness regions.  
- **Our program:** microscopic cone chirality → transport asymmetry → galactic handedness. NLS supplies a well-studied intermediate scale where chirality and topology already coexist in a nonlinear continuum equation.

---

## 5. What NLS does *not* replace

NLS does not furnish a Callias index or a lattice Dirac zero-mode proof. It is a bosonic, dispersive PDE. The fermionic index theorem, anomaly inflow, and the 8-component embedding remain the correct language for the microscopic cone / SPARC residual program. NLS is useful as:

1. intuition for core profiles and pair hybridization,  
2. a source of exact/ variational core shapes to try on the lattice,  
3. a parallel arena where chirality and topology are already linked at continuum level.

---

## 6. Possible next uses inside the project

- Import a variational NLS vortex core (e.g. the liquid-with-surface-tension ansatz for cubic–quintic vortices) as an alternative f(r) if further profile tests are desired.  
- Treat the two-core hybridization pattern as an NLS-molecule analogue and extract an effective splitting-vs-separation curve (already started in the pair scaling table).  
- Keep NLS as a conceptual parallel for the chirality-unification narrative, not as a replacement for the lattice index calculation.

---

## Compact statement

The nonlinear Schrödinger equation supports topological vortices and chiral solitons whose core structure and pair hybridization closely parallel the soft-mode physics of the Callias hedgehog. It does not replace the fermionic index theorem, but it supplies useful core-profile families, a clear molecular-regime analogy, and an intermediate-scale illustration of chirality meeting topology. The lattice program remains the correct path for a quantitative N_def demonstration.
