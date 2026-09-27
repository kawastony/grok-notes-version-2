# Wilson fermion artifacts — investigation

**Context:** Lattice Dirac / Wilson–Dirac operators used for soft modes and index. Artifacts can fake or spoil spectral motion and chirality.

---

## 1. Wilson term (reminder)

Wilson operator adds a Laplacian-like term ~ r_W a □ to lift doublers:
\[
D_W = \gamma_\mu\nabla_\mu + \frac{r_W a}{2}\Delta + m.
\]
Doublers acquire O(1/a) masses; physical mode remains light if m is tuned.

---

## 2. Artifact classes relevant to TAFA

| Artifact | Effect on soft modes / index |
|----------|------------------------------|
| **Explicit chirality breaking** | {D_W, γ_5} ≠ 0; residual chiral mixing; soft eigenvectors not exact chiral eigenstates |
| **Additive mass renormalization** | m_crit ≠ 0; bare mass must be tuned; mistuning shifts soft λ |
| **O(a) discretization errors** | Soft λ and localization distorted; continuum extrapolation required |
| **Doubler contamination** | If r_W too small or a large, near-doubler states can enter soft window |
| **Exceptional configurations** | Near-zero modes from topology + mistuning → solver instability |
| **Open boundary / edge modes** | Extra soft eigenvalues unrelated to bulk defects |

---

## 3. Impact on TAFA diagnostics

- **Index:** Wilson index theorems hold in modified form (e.g. via Ginsparg–Wilson if overlap used; for plain Wilson, use spectral flow of Hermitian operator or carefully defined topological charge). Plain Wilson can mis-count if mass is not in the correct window.
- **Spectral motion:** Physical soft motion can be mixed with lattice-spacing drift; always compare ≥2 spacings or L values.
- **Chirality / χ_βn:** Residual breaking from Wilson term is a known mixing source (prior chirality-mixing notes).
- **G12:** Weight slide is still meaningful if modes are bulk-localized and residuals are tight; edge contamination can fake G12.

---

## 4. Mitigations

1. Tune bare mass near κ_c (or use known critical hopping).
2. Monitor chirality residual ⟨ψ|γ_5|ψ⟩ for soft modes.
3. Refine a or increase L; demand soft λ and Q stable.
4. Prefer domain-wall / overlap if resources allow (better chiral symmetry).
5. Reject paths where soft IPR indicates boundary localization.
6. Report r_W and a explicitly in every lattice table.

---

## 5. Relation to non-propagation claim

Non-propagation assumes **physical** index lock and **physical** spectral motion. Wilson artifacts can:
- fake index jumps (bad lock),
- fake soft motion (bad activity scalar A_c),
- inject white-ish residual noise after coarse-graining.

So Wilson control is part of the evidential chain for the micro→meso map, not a side issue.

---

## 6. Status

Artifact list and mitigations for the lattice program. Does not change the schematic coarse-graining law; it constrains when lattice outputs may be fed into that law.
