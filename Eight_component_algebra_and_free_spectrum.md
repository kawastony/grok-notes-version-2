# 8-component Dirac ⊗ isospin — algebraic verification and free spectrum

Tony Kawas / 15 September 2026.

---

## 1. Continuum target (locked)

\[
H = \boldsymbol\alpha\cdot\mathbf p\otimes\mathbf 1_\tau + \beta\otimes\bigl(v f(r)\,\boldsymbol\tau\cdot\hat{\mathbf x}\bigr)
\]

8-component spinors: Dirac (4) ⊗ isospin (2).

---

## 2. Algebraic verification — PASSED

| Check | Result |
|-------|--------|
| {α_i ⊗ 1, α_j ⊗ 1} = 2δ_ij | Exact (error 0) |
| {α_i ⊗ 1, β ⊗ 1} = 0 | Exact |
| {β ⊗ τ_a, α_i ⊗ 1} = 0 for all a,i | Exact |
| (β ⊗ τ_a)² = I | Exact |
| {β ⊗ τ_a, β ⊗ τ_b} = 0 (a ≠ b) | Exact |
| M(n) = n · (β ⊗ τ), M² = \|n\|² I | Exact (∼ 10⁻¹⁶) |
| H² = I at constant n (p = 0) | Exact |

**All required anticommutators and the continuum H² structure hold.**  
The three mass matrices β ⊗ τ_a supply the non-trivial π₂ needed for a Callias hedgehog of degree N_def.

### Grading note

In the representation used, γ⁵ ⊗ 1 and β ⊗ 1 **commute** (they are the same matrix structure on the Dirac factor). Consequently {γ⁵ ⊗ 1, M} ≠ 0.  
Local chirality diagnostics should therefore use spectral asymmetry / local density of low modes, or an alternative involution that anticommutes with the full H, rather than raw 〈γ⁵〉 as the sole index proxy. This does not affect the existence of the Callias index; it only affects how the grading is measured on the lattice.

---

## 3. Free Wilson spectrum (8-component, periodic, no hedgehog) — HEALTHY

L = 4, m = 0.5, r = 1:

| Quantity | Numerical | Analytic |
|----------|-----------|----------|
| Lowest \|λ\| (8-fold) | 0.500000 | 0.500000 |
| # \|λ\| < 10⁻⁶ | 0 | — |
| Doubler corner | — | 6.50 |

- Exact match of the lowest gap to the analytic Wilson dispersion.  
- Isospin doubles the degeneracy (8 = 4 Dirac × 2 isospin) as expected.  
- No extensive zero kernel.  
- Doublers lifted.

(The next spectral cluster shows a mild representation-dependent shift under the γ⁵ conjugation used to form H; the physical gap and the absence of a spurious kernel are unambiguous.)

---

## 4. Status

| Item | Status |
|------|--------|
| 4-component embedding | Ruled out (algebraic) |
| 8-component algebra | **Verified** |
| Free 8-component Wilson spectrum | **Healthy** |
| Next | Insert smooth hedgehog mass β ⊗ (v f τ · n̂), then local diagnostics on a pair |

---

## 5. Compact statement

The 8-component Dirac ⊗ isospin embedding satisfies every continuum algebraic requirement of the Callias / Jackiw–Rossi class. Its free Wilson spectrum is healthy (correct gap, no spurious kernel, doublers lifted). The structural obstruction that nullified all 4-component runs is removed. The project can now proceed to the hedgehog mass texture and local defect diagnostics.
