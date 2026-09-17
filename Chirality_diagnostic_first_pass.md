# Chirality diagnostic — first pass

Tony Kawas / 17 September 2026.

---

## Setup

- Candidate Γ = γ₅ = β ⊗ I (same matrix used to form Hermitian H = γ₅ D)
- Verified: Γ† = Γ, Γ² = I, diag = (+1,+1,+1,+1,−1,−1,−1,−1)
- Soft modes: eigsh(H, sigma=0), lowest 4 by |λ|
- Bulk comparison: largest-|λ| modes
- Γ_sub = U† Γ U on soft 4D subspace; eigenvalues of Γ_sub
- Relative anticommutator: ‖{H,Γ}‖_sub / ‖H‖_sub in soft space
- Local core chiral weights at R=2

---

## Results

### L=8, sep=5, m₀=0.3, v=2, w=1

| quantity | value |
|----------|-------|
| soft \|λ\| | 0.00043, 0.00164, 0.00191, 0.00322 |
| χ_soft | −0.32, +0.01, −0.07, +0.03 |
| χ_bulk (large \|λ\|) | **+0.99, +0.99, +0.99, +0.99** |
| Γ_sub eigenvalues | −0.32, −0.14, +0.03, +0.08 |
| ‖{H,Γ}‖/‖H‖ soft | 0.11 |
| core A/B ownership | equal (hybridized) |

### L=10, sep=6, m₀=0.3, v=2, w=1

| quantity | value |
|----------|-------|
| soft \|λ\| | 0.00078, 0.00150, 0.00220, 0.00264 |
| χ_soft | −0.24, −0.04, −0.21, −0.17 |
| χ_bulk | **+0.99** |
| Γ_sub eigenvalues | −0.27, −0.18, −0.18, −0.04 |
| ‖{H,Γ}‖/‖H‖ soft | 0.36 |

### L=10, sep=6, m₀=0.5, v=3, w=1

| quantity | value |
|----------|-------|
| soft \|λ\| | 0.00124, 0.00147, 0.00167, 0.00181 |
| χ_soft | −0.33, −0.11, −0.12, −0.03 |
| χ_bulk | **+0.99** |
| Γ_sub eigenvalues | −0.34, −0.11, −0.11, −0.03 |
| ‖{H,Γ}‖/‖H‖ soft | 0.31 |

---

## Interpretation

**Opposite of the naive hope.**

1. **Bulk modes are strongly Γ-polarized** (χ ≈ +0.99). Soft modes are **more mixed** (|χ| ≲ 0.3).
2. **Γ_sub eigenvalues are not near ±1** — no clean chiral splitting of the soft subspace under this Γ.
3. **Core chiral weights are symmetric** on the two defects — consistent with spatial hybridization; no opposite-chirality core assignment.
4. Soft-subspace anticommutator is O(0.1–0.4) of ‖H‖_sub — not tiny; Wilson + hedgehog mass break continuum anticommutation appreciably even in the soft sector.

### Why bulk χ ≈ +1 is expected

At large |λ|, Wilson and kinetic structure align modes with the γ₅ grading used to define H. Soft modes sit where the position-dependent hedgehog mass mixes the two γ₅ sectors, so |χ| is reduced. That is a standard Wilson-fermion pattern, not evidence that chirality “organizes” the soft sector more than the bulk under this particular Γ.

### What this does *not* kill

- Continuum Callias still predicts chiral zero modes; lattice Wilson only approximates them.
- A **different** Γ (e.g. involving isospin τ aligned with the hedgehog, or a continuum-limit improved chirality) might still show soft-sector structure.
- The soft sector remains spectrally special; it is just not γ₅-polarized under the Hermitianizing matrix.

### What it does constrain

The simplest “γ₅ expectation value organizes soft modes better than bulk” diagnostic **fails**. Soft modes are less γ₅-polarized than bulk, and Γ_sub is not approximately ±I on a split basis.

---

## Progress status

| Item | Status |
|------|--------|
| Matrix-free apply_H | Done (L≤14) |
| H² sparse validation | Done |
| H² matrix-free SA/LOBPCG | Does not converge without preconditioner |
| Chirality first pass (Γ=γ₅) | **Done — soft less polarized than bulk** |
| Alternative Γ / isospin chirality | Open |
| Chiral-molecule write-up | Needs revised claim |

---

## Compact statement

With Γ = γ₅ (the Hermitianizing matrix), soft modes have |χ| ≲ 0.3 while bulk modes have χ ≈ +0.99. Γ_sub on the soft 4D space does not yield eigenvalues near ±1. Spatial core chiral weights remain symmetric. The soft sector is spectrally robust but **not** more γ₅-chiral than the bulk under this diagnostic. Next options: try a defect-aligned or isospin-weighted chirality operator, or treat continuum chirality as asymptotic only.
