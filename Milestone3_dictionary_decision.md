# Milestone 3 — Dictionary decision

Tony Kawas / 17 September 2026.

**Purpose:** Audit every major proposed paper↔lattice correspondence. Assign **Derived**, **Hypothesis**, or **Drop**.  
**Primary target:** conical Bessel spectral ratios vs lattice soft eigenvalues.

---

## Method (four tests per claim)

1. **Same operator?** (or systematic reduction exists)
2. **Same boundary / topology setting?**
3. **Same observable object?**
4. **Numerics support or contradict?**

Verdicts:

- **Derived** — mapping justified by argument and/or matching data; safe in core bridge.
- **Hypothesis** — coherent but unproved; may appear as conjecture only.
- **Drop** — remove from core bridge; do not present as established correspondence.

---

## Claim-by-claim audit

### 1. Soft sector exists; molecular at L≤10; χ_βn organizes soft vs bulk

| Test | Result |
|------|--------|
| Operator | Same (this lattice system) |
| BC | Same |
| Observable | Direct |
| Numerics | Support |

**Verdict: Derived** (Milestone 1–2).

---

### 2. Plain γ₅ fails as soft-sector organizer

**Verdict: Derived.**

---

### 3. Mass-texture operator β⊗(τ·n̂) is the correct soft diagnostic

**Verdict: Derived** (stable χ≈−0.8 soft vs ≈+1 bulk).

---

### 4. Hybridization scale ~ O(10⁻³) from soft splitting at L=8,10

**Verdict: Derived** as a measured spectral splitting.  
**Hypothesis only** if rephrased as “the transport diffusion constant D_χ.”

---

### 5. Spatial structure: P₁=P₂, P_rest dominant

**Verdict: Derived** (Milestone 2).

---

### 6. Conical Bessel roots (b₁, b₃) ↔ lattice soft eigenvalue ratios

| Test | Result |
|------|--------|
| Same operator? | **No.** Cone mode equation (geometric deficit / reduced radial) ≠ 3D Wilson–Dirac + hedgehog mass on T³ |
| Same BC? | **No.** Cone boundary ≠ periodic torus pair |
| Same observable? | **No.** Bessel zeros of order ν=\|m\|/β vs near-zero eigenvalues of H |
| Numerics? | **Contradict.** b₃/b₁≈2.28; lattice soft ratios are O(1) within a near-zero cluster, not that cone tower |

**Verdict: Drop** from core bridge.

May remain as a **separate paper-side spectral fact** about the geometric cone. It is **not** a dictionary entry for this lattice soft sector.

---

### 7. Liouville half-density weight → preconditioner for full 3D matrix-free H

| Test | Result |
|------|--------|
| Same operator? | Only after **radial reduction** of a single-defect continuum problem |
| Full 3D pair on torus? | No systematic reduction used in current code |
| Numerics? | Not demonstrated as fix for L=12 PRIMME |

**Verdict: Drop** as a direct claim on the present 3D solver.  
**Hypothesis** only for a future reduced radial code path.

---

### 8. Soft spectrum forms n_eff=8 multiplet

| Test | Result |
|------|--------|
| Embedding dimension | 8-component (true by construction) |
| Soft degeneracy | **Not observed** — ~2–4 near-zero modes, not 8-fold soft multiplet |

**Verdict: Drop** as a soft-spectrum claim.  
(Keep only: “Dirac⊗isospin embedding is 8-dimensional.”)

---

### 9. Instanton action S_inst ∝ 1/sinψ from current lattice runs

| Test | Result |
|------|--------|
| Setup varies ψ? | **No** — fixed flat torus, fixed hedgehog |
| Measures S_inst? | **No** |

**Verdict: Drop** for this code base. Requires a dedicated β-scan setup.

---

### 10. Lattice soft density = fuzzy DM soliton core r_c(x)

| Test | Result |
|------|--------|
| Same theory? | **No** without an explicit map |
| Numerics? | Soft density is molecular on T³, not a 1 kpc FDM profile |

**Verdict: Drop.**

---

### 11. Propagation law (continuity + κ ρ B_eff) as established dynamics

| Test | Result |
|------|--------|
| Continuity/inflow template | Standard anomaly structure |
| Identification ρ_χ ↔ texture density | Motivated by lattice |
| Constitutive κ term | **Ansatz** |
| Calibrated D_χ, κ | **Not done** |

**Verdict: Hypothesis** (architecture-level). Allowed as candidate law; not Derived.

---

### 12. Cone constants (e.g. 11/72, R) appear as lattice soft-sector invariants

| Test | Result |
|------|--------|
| Measured in soft spectrum? | **No** |
| Same geometric origin? | Unproven dictionary |

**Verdict: Hypothesis** at program-architecture level only. **Drop** as lattice-measured invariants.

---

## Summary table

| Claim | Verdict |
|-------|---------|
| Soft sector + molecular regime L≤10 | **Derived** |
| γ₅ fails; χ_βn organizes soft/bulk | **Derived** |
| P₁=P₂, P_rest dominant; splitting O(10⁻³) | **Derived** |
| Propagation law as calibrated dynamics | **Hypothesis** |
| Cone constants as lattice invariants | **Hypothesis** (architecture only) |
| Liouville weight fixes full 3D H | **Drop** (direct); Hypothesis (radial only) |
| Bessel b₃/b₁ ↔ soft λ ratios | **Drop** |
| Soft n_eff=8 multiplet | **Drop** |
| Instanton S∝1/sinψ from current runs | **Drop** |
| Soft density = FDM soliton | **Drop** |

---

## Bessel decision (explicit)

> **Drop.** The conical Bessel root ratio is not a dictionary entry for the Wilson–Dirac hedgehog soft spectrum. Different operators, different boundary conditions, different observables; low-L numerics do not match. Keep Bessel roots inside the geometric-cone paper series; do not use them to validate or reject lattice soft modes.

---

## What the core bridge retains

After the audit, the **core lattice↔effective bridge** is only:

1. Robust soft sector (L≤10)
2. Molecular spatial structure
3. Mass-texture chirality organization (χ_βn)
4. Hybridization scale from spectral splitting (estimate-grade for transport language)
5. Candidate anomaly-style propagation law (**hypothesis**)

Everything else is either paper-side only or future work with a new setup.

---

## Milestone 3 status

**DONE.**  
Dictionary cleaned. Unification architecture remains; false identifications removed.
