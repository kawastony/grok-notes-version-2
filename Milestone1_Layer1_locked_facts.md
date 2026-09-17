# Milestone 1 — Layer 1 locked facts (L ≤ 10 only)

Tony Kawas / 17 September 2026.

**Purpose:** Freeze what is nonperturbatively established before any bridge or dictionary claims.

**Scope:** Wilson–Dirac operator with 8-component Dirac⊗isospin embedding and hedgehog–antihedgehog mass texture on a 3-torus. Soft modes extracted by sparse ARPACK (L≤10) and matrix-free PRIMME (L=8,10 on Colab).

**Out of scope for Layer 1:** L≥12, cone–Bessel spectral ratios, instanton sinψ scaling, FDM soliton profiles, calibrated D_χ/κ as theorems, full cross-scale unification.

---

## 1. Operator and embedding

- Hermitian Wilson–Dirac Hamiltonian H = γ₅ D_W with Wilson parameter r = 1.
- Mass texture: position-dependent β ⊗ (τ · n̂) hedgehog / antihedgehog pair.
- 4-component embedding fails algebraically ({M, α_i} ≠ 0). **8-component embedding succeeds** and is the working operator.
- Free spectrum matches analytic Wilson dispersion (verified).

---

## 2. Soft sector exists and is robust

Near-zero modes appear for the defect pair across parameter scans.

| L | sep | typical soft \|λ\| (m₀=0.3, v=2, w=1) |
|---|-----|--------------------------------------|
| 8 | 5 | ~0.0004, 0.0016, 0.0019, 0.0032 |
| 10 | 6 | ~0.0008, 0.0015, 0.0022, 0.0026 |

- Soft modes persist under changes of core width, m₀, and profile shape (within tested ranges).
- They are **not** removed by continuous deformation of UV details that preserve the pair topology.
- Matrix-free PRIMME at L=8 and L=10 recovers the same soft spectrum as sparse ARPACK (\|λ\| agreement to ~10⁻⁹ at L=8; match at L=10).

**Locked claim:** A robust soft sector exists for this operator at L≤10.

---

## 3. Spatial structure: molecular regime

At accessible volumes and separations:

- Soft modes are **hybridized** across both cores (shared ownership).
- Core weights / IPR do not show clean single-core localization.
- Finite-size molecular regime (sep/ξ not large enough for asymptotic isolation).

**Locked claim:** Soft sector is spatially molecular at L≤10, not two isolated Callias cores.

This is a finite-volume fact, not a failure of topology.

---

## 4. Chirality diagnostics

### 4.1 Plain γ₅ fails as soft-sector organizer

| Sector | ⟨γ₅⟩ |
|--------|--------|
| Soft | \|χ\| ≲ 0.3 |
| Bulk | χ ≈ +0.99 |

Soft modes are **less** γ₅-polarized than bulk. Plain γ₅ does not single out the soft sector.

### 4.2 Defect-aligned mass-texture operator succeeds

Operator: β ⊗ (τ · n̂(x)) with n̂ from the net signed hedgehog field.

| Sector | χ_βn (L=8) | χ_βn (L=10) |
|--------|------------|-------------|
| Soft | ≈ −0.80 to −0.82 | ≈ −0.80 to −0.81 |
| Bulk | ≈ +0.98 to +0.99 | ≈ +0.99 |

**Locked claim:** Soft modes are stably **anti-aligned** with the local mass texture; bulk modes are **aligned**. The soft sector is mass-texture-organized, not γ₅-organized.

---

## 5. Ruled-out shortcuts (Layer 1)

Within the tested window, the following do **not** by themselves produce isolated zero modes or kill hybridization:

- Narrower cores alone
- Alternative smooth core profiles alone
- Moderate m₀ scans alone
- 2-mode / 4D rotation diagnostics alone

Hybridization is the expected molecular outcome at these sep/ξ ratios.

---

## 6. Solver status (engineering, not physics)

| Capability | Status |
|------------|--------|
| Sparse ARPACK soft modes L≤10 | Reliable |
| Matrix-free matvec L≤14 | Works |
| Matrix-free PRIMME soft modes L=8,10 | Validated (Colab) |
| L=12 soft modes | **Not converged** (rel residual ≫ 1 or max-iter) |

Layer 1 physics uses **only** L≤10.

---

## 7. What Layer 1 does *not* claim

- Index(D) = N_def as a fully proven lattice theorem for multiple charges on the torus (spectral flow obstructed; local diagnostics used instead).
- Continuum Callias zero-mode isolation at these volumes.
- Equality of lattice soft spectrum with conical Bessel roots (b₁, b₃).
- Propagation law coefficients D_χ, κ as measured constants.
- Any galactic, cosmological, or FDM soliton identification.

---

## 8. Compact Layer 1 statement

> For the 8-component Wilson–Dirac hedgehog–antihedgehog system at L≤10: a robust soft sector exists; it is spatially molecular; it is organized by anti-alignment with the defect mass texture (χ_βn ≈ −0.8) rather than by plain γ₅; bulk modes are texture-aligned (χ_βn ≈ +1). These facts are nonperturbative and solver-validated (ARPACK and PRIMME). Larger-L isolation, cross-theory spectral dictionaries, and transport calibration lie outside Layer 1.

---

## 9. Milestone 1 status

**LOCKED.**  
Further work may add L≥12 only after residual-validated soft modes. Bridges and dictionaries build on this document, not the reverse.
