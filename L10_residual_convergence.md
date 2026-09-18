# L=10 residual convergence analysis

Tony Kawas / 18 September 2026.

**Operator:** 8-component Wilson–Dirac + hedgehog pair, m₀=0.3, v=2, w=1.  
**Solver:** sparse ARPACK `eigsh(..., sigma=0, which='LM', tol=1e-8)`.  
**Residual:** \(\mathrm{rel\_res}=\|H\psi-\lambda\psi\|/\|H\psi\|\).

---

## Pair scan (d = 1…5)

| d | n | \|λ\| | abs_res | rel_res | pass (<10⁻³) |
|---|---|--------|---------|---------|--------------|
| 1 | 0–3 | 0.0036–0.012 | ~10⁻¹⁴ | ~10⁻¹² | YES |
| 2 | 0–3 | 0.0008–0.006 | 10⁻¹⁴–10⁻¹⁰ | 10⁻¹¹–10⁻⁸ | YES |
| 3 | 0–3 | 0.0014–0.004 | ~10⁻¹⁴ | ~10⁻¹¹ | YES |
| 4 | 0–3 | 0.0005–0.002 | 10⁻¹⁴–10⁻¹⁰ | 10⁻¹⁰–10⁻⁸ | YES |
| 5 | 0–3 | 0.0004–0.003 | ~10⁻¹³ | ~10⁻¹⁰ | YES |

**Summary:** min rel = 1.3×10⁻¹², median ≈ 5×10⁻¹¹, max = 5×10⁻⁸.  
**100%** of soft modes pass rel < 10⁻³; **100%** pass < 10⁻⁶; **85%** pass < 10⁻⁸.

---

## Single-defect control

H and AH: all four modes rel_res ~ 10⁻¹¹–10⁻¹⁰ — equally well converged.

---

## Verdict

| Claim | Status |
|-------|--------|
| L=10 soft modes are true approximate eigenpairs | **Validated** |
| Diagnostics (P₁,P₂, χ_T, A, Δλ) at L=10 rest on converged vectors | **Safe** |
| L=12 (prior Colab PRIMME) | Still unvalidated — do not mix |

**Layer 1 / Milestone 2 numerics at L=10 are residual-clean under sparse ARPACK.**
