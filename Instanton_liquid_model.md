# Instanton liquid model (ILM) — examination

Tony Kawas / 17 September 2026.

**Scope:** Standard ILM / RILM / interacting liquid; parameters; successes; limits; relation to molecular phase and to the lattice soft-sector program.

---

## 1. Core idea

The **instanton liquid model** (Shuryak and others) describes the QCD vacuum at low resolution as a liquid of instantons and antiinstantons:

- Finite density of topological lumps
- Average size small compared with inter-instanton distance → **dilute** liquid
- Quarks hop between localized zero modes → **chiral symmetry breaking** (Banks–Casher)
- Effective ’t Hooft multi-fermion interactions → light hadron structure

It is a **semiclassical ensemble model**, not full QCD (no confinement by itself).

---

## 2. Canonical parameters

| Parameter | Typical value |
|-----------|----------------|
| Mean size \(\bar\rho\) | \(\sim 1/3\,\mathrm{fm}\) (\(\sim 0.3\text{–}0.35\,\mathrm{fm}\)) |
| Mean density \(n\) | \(\sim 1\,\mathrm{fm}^{-4}\) |
| Mean separation \(\bar R\) | \(\sim 0.8\text{–}1\,\mathrm{fm}\) |
| Packing fraction \(n\bar\rho^4\) | \(\ll 1\) (diluteness) |

These values are chosen to match gluon condensate, topological susceptibility, and quark condensate order of magnitude, then used to predict correlators.

Variants:

- **RILM** — random positions and orientations
- **IILM / interacting liquid** — includes classical + fermion-induced interactions
- **Molecular / dense** ensembles — explicit I–A molecules, especially near \(T_c\)

---

## 3. Mechanism of chiral symmetry breaking

1. Each (anti)instanton binds a chiral zero mode of the Dirac operator.
2. At finite density, zero modes overlap and **delocalize** (band formation).
3. Spectral density \(\rho(\lambda=0)\neq 0\) → Banks–Casher:
   \[
   \langle\bar qq\rangle = -\pi\rho(0).
   \]
4. Quarks acquire a momentum-dependent dynamical mass from the instanton medium.

---

## 4. Successes

| Domain | ILM performance |
|--------|-----------------|
| Vacuum condensates | Order-of-magnitude match with phenomenology |
| Pseudoscalar channels (\(\pi\), \(K\)) | Strong attraction; reasonable correlators |
| \(\eta'\) / U(1)_A | Topological susceptibility / screening |
| Many meson and baryon correlators | Often good up to ~1–1.5 fm in RILM studies |
| Spin-dependent forces | Nucleon vs Δ pattern qualitatively |
| Finite \(T\) | Molecular rearrangement as chiral-transition scenario |

Historically outperformed pure QCD sum-rule estimates in many channels when correlators were computed numerically in multi-instanton backgrounds.

---

## 5. Limitations

| Limitation | Consequence |
|------------|-------------|
| **No confinement** | In principle unphysical multi-quark cuts; often not visible in practice in main correlators |
| Semiclassical / filtered topology | Not a complete UV-complete vacuum |
| Parameter dependence | \(\bar\rho\), \(n\) fixed phenomenologically or by variational/saddle arguments |
| Lattice comparison | Instanton-only backgrounds can miss confining physics; spectroscopy sometimes too light without extra fluctuations |
| Diluteness assumption | Breaks down if large instantons or strong overlap dominate |

ILM is a **powerful effective vacuum model**, not a substitute for full lattice QCD.

---

## 6. Liquid vs molecules (link to previous notes)

- **Random liquid (low \(T\)):** disordered I and A → dense near-zero Dirac modes → condensate.
- **Molecular phase (near/above \(T_c\)):** correlated I–A pairs → hybridized quasi-zeros → condensate drops.

Same interaction physics examined in the molecule notes: orientation-dependent attraction, streamline, fermion determinant.

---

## 7. Relation to the Wilson–Dirac hedgehog program

| ILM concept | This lattice system |
|-------------|---------------------|
| Topological lump + zero mode | Hedgehog texture + soft modes |
| Overlap / hopping | Hybridization, molecular P₁=P₂ |
| Dilute liquid | **Not** realized at L≤10 (molecular pair) |
| Ensemble average over many I,A | Single pair (or few) on T³ |
| ’t Hooft vertex phenomenology | Outside current scope |

**Shared principle:** topology organizes soft Dirac modes and can drive chiral physics.  
**Not shared:** ILM parameter set, hadron correlators, or 4D gauge ensemble.  
**Milestone 3:** do not treat soft \(\lambda\) ratios or χ_βn as measurements of ILM \(\bar\rho\), \(n\).

A future **multi-defect density scan** on this operator would be the analogue of “varying liquid density” — still a different theory.

---

## 8. Status table

| Statement | Status |
|-----------|--------|
| ILM with \(\bar\rho\sim1/3\,\mathrm{fm}\), \(n\sim1\,\mathrm{fm}^{-4}\) is a standard QCD vacuum model | Established phenomenology |
| Explains ChSB via zero-mode delocalization | Standard |
| Molecular rearrangement near \(T_c\) | Standard scenario in ILM literature |
| Lattice soft sector is an ILM simulation | **No** |
| Molecular soft pair “like” one I–A molecule | **Analogy** |
| Extract ILM parameters from L≤10 runs | **Drop** |

---

## 9. Compact statement

The instanton liquid model is a dilute ensemble of topological lumps that generates chiral symmetry breaking through overlapping fermionic zero modes and organizes much of light-hadron correlator phenomenology, with a molecular rearrangement scenario near the chiral transition. It shares the topology↔soft-mode principle with the Callias/hedgehog lattice program. The present L≤10 soft sector is a single molecular defect pair, not an ILM ensemble, and should not be used to fit ILM parameters.
