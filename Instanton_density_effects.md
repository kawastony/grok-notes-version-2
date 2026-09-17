# Instanton density effects — investigation

Tony Kawas / 17 September 2026.

**Scope:** Standard physics of instanton density and how it relates (or does not) to the Wilson–Dirac hedgehog soft sector. Respects Milestone 3: no false dictionary with cone Bessel roots or FDM solitons.

---

## 1. What “instanton density” means

In QCD / Yang–Mills, the **instanton density** \(n(\rho)\) (or integrated \(n_{I+A}\)) is the number of instantons + antiinstantons per unit four-volume in a given size bin \(\rho\).

Canonical dilute-liquid numbers (order of magnitude):

- average size \(\bar\rho \sim 0.3\text{–}0.35\,\mathrm{fm}\)
- inter-instanton distance \(\bar R \sim 0.8\text{–}1\,\mathrm{fm}\)
- density \(n_{I+A} \sim 1\,\mathrm{fm}^{-4}\)

Semiclassical one-instanton density (schematic):

\[
n(\rho)\,d\rho
\propto
\frac{d\rho}{\rho^5}
\left(\frac{8\pi^2}{g^2(\rho)}\right)^{2N_c}
e^{-8\pi^2/g^2(\rho)}
\times
(\text{fermion zero-mode factors}).
\]

Large instantons are suppressed by interactions, screening, and higher-order effects beyond the pure semiclassical formula.

---

## 2. Physical effects of instanton density

| Effect | Mechanism |
|--------|-----------|
| **Chiral condensate** | Quarks hop between I and A zero modes → dynamical mass; \(\langle\bar qq\rangle\) tied to density (vacuum: often \(\propto\sqrt{n}\); dense matter: sometimes \(\propto n\)) |
| **Topological susceptibility** \(\chi_{\rm top}\) | Fluctuations of topological charge; dilute gas: \(\chi_{\rm top}\sim n\) (Poisson); full QCD: screening, \(\chi\to0\) in chiral limit |
| **η′ mass** | Witten–Veneziano: links \(m_{\eta'}^2\) to topological susceptibility |
| **’t Hooft vertices** | Zero modes → effective multi-fermion interactions violating U(1)_A |
| **High T / high μ** | Density exponentially suppressed → chiral restoration mechanisms |
| **Monopole–instanton link** | Lattice: monopole–antimonopole pairs can create instanton number; zero modes of overlap Dirac track topology |

**Density is not a free knob alone:** size distribution, interactions, and fermion determinant all matter.

---

## 3. Zero modes: instantons vs Callias / hedgehog

| Object | Setting | Index / zero modes |
|--------|---------|---------------------|
| BPST instanton | 4D Euclidean YM | Atiyah–Singer: \(n_L-n_R=Q\) |
| Caloron | S¹×R³ | Constituent monopoles; zero mode can hop with BC |
| Callias / hedgehog | 3D Dirac + Higgs/mass texture | Callias index from asymptotic map |
| **Our lattice** | Wilson–Dirac + hedgehog pair on T³ | Soft near-zero cluster; molecular |

**Shared idea:** topology → protected fermionic soft modes.  
**Not the same object:** 4D instanton density is not the number of our 3D hedgehog pairs, and our soft \(\lambda\) are not BPST zero modes.

Milestone 3 already **Dropped** identifying lattice soft spectrum with unrelated geometric-cone towers. Same discipline applies here: analogy ≠ dictionary.

---

## 4. Density effects relevant to *this* program

### 4.1 What could matter conceptually

1. **Diluteness vs molecular regime**  
   Instanton liquid: dilute when \(\bar R\gg\bar\rho\).  
   Our pair: “dilute” when sep \(\gg\xi\) (localization length).  
   At L≤10 we are in the **molecular** (overlapping) regime — the analogue of a dense or correlated instanton molecule, not a dilute gas.

2. **Zero-mode zone / chirality**  
   Instanton: fixed handedness zero mode.  
   Our soft modes: organized by **mass-texture** anti-alignment (\(\chi_{\beta n}\approx-0.8\)), not plain \(\gamma_5\).  
   Density of defects would change hybridization and effective \(\rho_\chi\), not automatically reproduce instanton liquid formulas.

3. **Anomaly inflow / topological source**  
   In the candidate propagation law, \(S_{\rm top}\) plays the role of a topological source. Instanton density in 4D is one realization of topological activity; our \(S_{\rm top}\) on the lattice would be tied to defect winding / texture changes — **Hypothesis**, not Derived.

### 4.2 What this lattice does *not* measure

- Instanton size distribution \(n(\rho)\)
- Topological susceptibility of 4D YM
- \(S_{\rm inst}\propto 1/\sin\psi\) (Milestone 3: **Drop** for current setup)
- Chiral condensate of continuum QCD

Measuring those requires 4D gauge configurations (or a dedicated reduced model), not the present 3D Wilson–Dirac hedgehog Hamiltonian alone.

---

## 5. If one wanted density effects *on this operator*

A controlled extension (future work, not Layer 1):

1. Vary **number of hedgehog pairs** (1, 2, …) on larger volumes.  
2. Track soft multiplicity, hybridization, mean \(\chi_{\beta n}\), and IPR vs defect density \(n_{\rm def}=N_{\rm pairs}/L^3\).  
3. Ask whether soft-sector observables scale like a dilute gas, a molecular liquid, or saturate.

That would be a **defect-density** study on this operator — useful and honest — not an instanton-liquid simulation.

---

## 6. Status relative to milestones

| Statement | Status |
|-----------|--------|
| Instanton density drives chiral and topological effects in QCD | Standard physics |
| Topology ↔ soft fermionic modes (general) | Shared principle |
| Our soft sector = BPST zero modes | **No** |
| Our pair density = instanton density | **No** |
| Molecular regime ≈ correlated I–A molecules (analogy) | **Hypothesis** / pedagogical |
| Propagation-law \(S_{\rm top}\) ← instanton density | **Hypothesis** only |
| Measure \(n(\rho)\) with current code | **Drop** |

---

## 7. Compact statement

Instanton density is a central nonperturbative parameter in 4D QCD: it feeds the chiral condensate, topological susceptibility, and ’t Hooft interactions, and is suppressed at high T/μ. Fermionic zero modes bind topology to chirality. Our lattice program shares the **topology → soft modes** principle via Callias/hedgehog physics, but operates a different operator in a molecular regime at L≤10. Instanton-density formulas should not be imported as dictionary entries. A future **defect-density scan** on this Hamiltonian is the honest way to study density effects inside the present framework.
