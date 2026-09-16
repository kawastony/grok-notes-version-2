# Wilsonian effective actions — exploration for the Callias / cone program

Tony Kawas / 16 September 2026.

---

## 1. What a Wilsonian effective action is

Start from a UV theory with cutoff Λ (e.g. lattice spacing a ∼ 1/Λ). Integrate out modes with momenta above a sliding scale μ < Λ. The result is a **Wilsonian effective action** S_μ[φ] for the remaining soft fields:

\[
e^{-S_\mu[\varphi]} = \int_{k>\mu}\mathcal{D}\phi\; e^{-S_\Lambda[\phi]}.
\]

Couplings in S_μ run with μ (RG flow). At low energy only relevant and marginal operators matter; irrelevant operators are suppressed by powers of μ/Λ.

The continuum limit is the limit Λ → ∞ (or a → 0) with physical scales held fixed, so that the Wilsonian action approaches a continuum EFT.

---

## 2. Lattice Dirac theory as a Wilsonian UV completion

The 8-component Wilson–Dirac operator with hedgehog mass is a concrete UV theory at cutoff ∼ 1/a:

- Wilson term: irrelevant (dimension-5) regulator that lifts doublers.
- Bare mass m₀ and hedgehog amplitude v: relevant deformations.
- Core profile f(r) and width w: UV detail of the defect insertion.

After integrating out hard modes one expects a continuum Dirac operator coupled to a smooth mass texture Φ(x), plus higher-dimension corrections O(a). The Callias index and anomaly inflow are properties of that continuum (or near-continuum) effective description, not of the particular lattice regulator.

---

## 3. Defect effective actions

A topological defect can be viewed as a lower-dimensional theory coupled to the bulk. Integrating out bulk modes yields a **defect effective action** on the world-volume (or, for a pointlike hedgehog, effective couplings at the core and asymptotic boundary conditions).

For the Callias hedgehog:

- UV: lattice mass map with winding N_def.
- IR effective description: continuum Dirac fermion in a background Φ̂ with deg(Φ̂) = N_def, plus possible localized counterterms at the core.
- Protected data: index, zero-mode chirality, inflow current — insensitive to irrelevant core counterterms.

This is the same logic as defect RG in CFTs: relevant defect deformations change the defect phase; topological invariants and anomalies constrain the flow.

---

## 4. Chiral residual as an IR effective term

In the microscopic-cone program the chiral residual is an effective contribution to large-scale dynamics (e.g. galactic residual network) descending from microscopic orientation / winding. In Wilsonian language:

\[
S_{\rm eff} \supset S_{\rm standard} + \kappa\,\mathcal{O}_{\rm chiral}[{\rm orientation},\,N_{\rm def},\ldots].
\]

Here κ is a low-energy coefficient fixed by matching to the UV (cone geometry, R_cone, anomaly inflow). Whether O_chiral is relevant, marginal, or irrelevant at galactic scales determines whether the residual survives or is washed out — a standard EFT question.

The lattice Callias calculation is the UV matching step for the fermionic / topological part of that coefficient: it aims to show that a nonzero N_def produces a protected soft sector and an inflow structure that can source a nonzero κ.

---

## 5. Matching table

| Wilsonian notion | Program counterpart |
|------------------|---------------------|
| UV cutoff Λ ∼ 1/a | Lattice spacing |
| Relevant mass deformation | m₀, hedgehog amplitude v |
| Irrelevant operators | Wilson term, core profile shape |
| Defect effective action | Continuum Callias problem with winding N_def |
| IR observable after matching | Soft modes, index, chiral residual κ |
| Continuum limit | a → 0, sep/ξ fixed ≫ 1, artefacts → Callias zeros |

---

## 6. What the lattice results already illustrate

- Soft sector robust under changes of f(r), w, v → those are UV/irrelevant details; the winding is the effective defect datum.
- Hybridization controlled by sep/ξ → IR physics of the Wilsonian theory at finite volume.
- Failure to decouple at L ≤ 10 → the Wilsonian IR cutoff (box size) is still too small compared with ξ; not a failure of the UV defect definition.

---

## 7. What a full Wilsonian analysis would add

1. Explicit matching of lattice near-zero modes onto continuum Callias zero modes as a → 0.  
2. Operator product / effective Lagrangian for the residual chiral term coupled to continuum gravity or galactic dynamics.  
3. Power-counting for κ: relevance at galactic scales, natural size from anomaly matching.  
4. Systematic improvement of the lattice action (remove O(a) artefacts) as a better UV starting point for the same IR physics.

None of these replace the need for larger geometric separation on the lattice; they organize what the continuum theory should look like once that separation is achieved.

---

## Compact statement

Wilsonian effective actions frame the lattice hedgehog as a UV defect insertion whose relevant/topological content (winding, soft modes, inflow) survives integration of hard modes, while core profile and Wilson artefacts are irrelevant. The chiral residual is an IR effective operator whose coefficient is matched to that UV topology. The present lattice window is still an intermediate-scale Wilsonian theory with sep ∼ ξ; the continuum Callias EFT is the target after the IR cutoff is removed.
