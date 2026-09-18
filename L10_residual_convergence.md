# L=10 residual convergence analysis

Tony Kawas / 18 September 2026.

**Operator:** 8-component Wilson–Dirac + hedgehog pair, m₀=0.3, v=2, w=1, r=1.  
**Solver:** scipy.sparse.linalg.eigsh, sigma=0, which='LM', tol=1e-8.  
**Residual:** \(\mathrm{rel\_v}=\|Hv-\lambda v\|/\|v\|\).

**Pass criterion:** rel_v ≲ 10⁻⁸ (engineering); target ≲ 10⁻¹⁰.

---

## Pair scan residuals

| d | mode | \|λ\| | rel_v | status |
|---|------|--------|---------|--------|
| 1 | 0–3 | 0.0036–0.012 | 1e-14 – 5e-13 | **OK** |
| 2 | 0–3 | 0.0008–0.0063 | 4e-14 – 2e-10 | **OK** |
| 3 | 0–3 | 0.0014–0.0040 | ~6e-14 | **OK** |
| 4 | 0–3 | 0.0005–0.0024 | 7e-14 – 1e-10 | **OK** |
| 5 | 0–3 | 0.0004–0.0033 | ~1e-13 | **OK** |

**Max rel_v over all pair soft modes: ~2×10⁻¹⁰** (well below 10⁻⁸).

---

## Single-defect control

| mode | \|λ\| | rel_v |
|------|--------|---------|
| 0 | 5.0e-4 | 7e-14 |
| 1 | 1.2e-3 | 1e-13 |
| 2 | 1.2e-3 | 9e-14 |
| 3 | 2.1e-3 | 8e-13 |

Also **OK**.

---

## Tol sensitivity (d=5)

| eigsh tol | max rel_v | \|λ\| stable? |
|-----------|-----------|---------------|
| 1e-4 | 2.5e-9 | yes |
| 1e-6 | 1.6e-9 | yes |
| 1e-8 | 1.6e-13 | yes |
| 1e-10 | 2.0e-13 | yes |

Eigenvalues stable across tols; residual improves as tol tightens. Default tol=1e-8 is more than enough.

---

## Conclusion

**L=10 soft modes are residual-converged.**  
All pair and single-defect soft eigenvectors satisfy rel_v ≪ 10⁻⁸ (typically 10⁻¹⁴–10⁻¹⁰).

This **locks** L=10 as a trusted volume for:

- molecular regime claims
- texture chirality / bridge diagnostics
- anisotropy A
- any Colab-style texture-bound analysis at L=10

**L=12 remains unvalidated** until similar residual checks pass there.

---

## Compact statement

Sparse ARPACK soft modes at L=10 for the Wilson–Dirac hedgehog pair are fully residual-converged (rel_v ~ 10⁻¹³). Layer-1 and Milestone-2 results at L=10 rest on verified eigenvectors.
