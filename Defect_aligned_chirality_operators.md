# Defect-aligned chirality operators

Tony Kawas / 17 September 2026.

---

## Motivation

Plain γ₅ expectation values do **not** distinguish the soft sector (soft |χ| ≲ 0.3, bulk χ ≈ +0.99). Continuum Callias / Jackiw–Rebbi zero modes are organized by the **mass texture**, not only by γ₅. Natural next operators are defect-aligned.

---

## Candidate operators (8-component embedding)

| # | Operator | Structure |
|---|----------|-----------|
| 1 | Γ₅ | γ₅ = β ⊗ I |
| 2 | τ_z | I₄ ⊗ τ_z (pair axis) |
| 3 | γ₅ τ_z | (β ⊗ I)(I ⊗ τ_z) |
| 4 | **β ⊗ (τ · n̂(x))** | local mass direction (same matrices as hedgehog mass) |
| 5 | I ⊗ (τ · n̂(x)) | local isospin along n̂ |

Here n̂(x) is the unit vector of the **net** signed hedgehog field of the pair.

Continuum intuition: Callias zero modes live where the position-dependent mass vanishes or flips; their spinor structure is locked to the asymptotic Higgs map. The local mass matrix β ⊗ (τ · n̂) is the lattice avatar of that texture.

---

## Numerical results

### L = 8, sep = 5, m₀ = 0.3, v = 2, w = 1

| mode | χ(γ₅) | χ(τ_z) | χ(γ₅τ_z) | **χ(β⊗τ·n̂)** | χ(I⊗τ·n̂) |
|------|-------|--------|----------|--------------|----------|
| soft 0 | −0.32 | −0.61 | +0.23 | **−0.82** | +0.35 |
| soft 1 | +0.01 | −0.31 | −0.35 | **−0.80** | −0.06 |
| soft 2 | −0.07 | −0.10 | −0.36 | **−0.82** | +0.04 |
| soft 3 | +0.03 | −0.36 | −0.30 | **−0.80** | −0.10 |
| bulk 0 | +0.99 | +0.99 | +0.98 | **+0.99** | +1.00 |
| bulk 1 | +0.99 | +0.99 | +0.98 | **+0.99** | +1.00 |
| bulk 2 | +0.99 | −0.99 | −0.98 | **+0.98** | +1.00 |
| bulk 3 | +0.99 | −0.99 | −0.98 | **+0.98** | +1.00 |

### L = 10, sep = 6, m₀ = 0.3, v = 2, w = 1

| sector | χ(γ₅) | **χ(β⊗τ·n̂)** |
|--------|-------|--------------|
| soft (4 modes) | −0.24 … −0.04 | **−0.81 … −0.80** |
| bulk (4 modes) | +0.99 | **+0.99** |

---

## Interpretation

**Local mass-aligned operator β ⊗ (τ · n̂(x)) cleanly separates soft from bulk:**

- Soft: χ ≈ **−0.80 to −0.82** (stable across L = 8, 10)
- Bulk: χ ≈ **+0.98 to +0.99**

Soft modes are polarized **against** the local mass texture; bulk modes lock **with** it. That matches continuum intuition: near-zero modes concentrate where mass is small or opposite in structure, while high modes follow the mass grading.

Other operators:
- γ₅: soft less polarized than bulk (previous null)
- τ_z: soft moderately negative; bulk ±1 (pair-axis isospin, less distinctive)
- γ₅τ_z / I⊗τ·n̂: no comparable soft-vs-bulk contrast

---

## Conceptual status

| Claim | Support |
|-------|--------|
| Soft sector is spectrally special | Yes (robust near-zero modes) |
| Soft sector is γ₅-chiral vs bulk | No |
| Soft sector is **mass-texture aligned** (anti-aligned) vs bulk | **Yes** |
| Clean ±1 Γ_sub under γ₅ | No |
| Localization / ownership | Still hybridized |

Revised framing:

> The soft sector is a **mass-texture-organized molecular subspace**: modes are robustly anti-aligned with the local hedgehog mass direction (χ_βn ≈ −0.8), while bulk modes are locked to it (χ_βn ≈ +1). Spatial ownership remains shared at accessible L.

This is closer to Callias/Jackiw–Rebbi physics than plain γ₅ expectations.

---

## Caveats

1. β ⊗ (τ · n̂) is **not** a global involution with Γ² = I everywhere in a simple constant sense (n̂ varies); χ is a weighted expectation, not a sharp ±1 quantum number.
2. Pair geometry makes n̂ a compromise field (opposite cores); single-defect runs would be cleaner for asymptotic chirality.
3. Wilson artefacts still mix continuum chiralities; χ_βn ≈ −0.8 is strong but not exact −1.

---

## Next steps (optional)

- Single-defect open BC: asymptotic n̂ and continuum-like χ
- Γ_sub built from a projected/constant version of β⊗τ·n̂
- Local chiral density maps of soft modes vs cores
- Stability of χ_βn under m₀, v, w scans

---

## Compact statement

Defect-aligned operator β ⊗ (τ · n̂(x)) yields χ ≈ −0.8 on soft modes and χ ≈ +1 on bulk modes at L = 8 and 10. Plain γ₅ does not. The soft sector is organized by the mass texture (anti-alignment) more than by γ₅ grading. Spatial hybridization persists; the robust invariant at accessible volume is texture alignment, not core ownership.
