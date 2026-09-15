# Analysis of residual chirality mixing

Tony Kawas / 15 September 2026.

---

## 1. Goal

Isolate and rank the sources of the few-percent residual 〈γ⁵〉 observed in the angular-hedgehog zero-mode.

---

## 2. Controlled numerical isolation (L = 5 and 7)

| Setup                        | L=5 〈γ⁵〉 | L=7 〈γ⁵〉 | lowest \|λ\|     | Interpretation |
|------------------------------|----------|----------|------------------|----------------|
| Open + full angular (baseline) | −0.026 | −0.015 | ∼ 10⁻¹⁶         | Reference      |
| Periodic + full angular      | +0.036   | +0.014   | ∼ 10⁻¹⁶         | Boundary effect comparable, not dominant |
| Open + **smoothed** angular  | **−0.004** | **+0.002** | ∼ 10⁻¹⁶     | **Dominant source removed** |
| Open + radial-only (control) | +0.020   | +0.001   | 0.01–0.03        | No protected zero-mode |

---

## 3. Ranking of sources

### Leading source: angular discretisation of σ · r̂ at the origin

- When the unit vector r̂ is replaced by a smoothed version  
  \[
  \hat{\mathbf{r}}_{\mathrm{eff}} = \mathbf{r}/\sqrt{r^2+(0.5a)^2}
  \]
  the residual chirality collapses by a factor of ∼5–10 (from ∼0.02 to ∼0.003).  
- On the lattice the origin and the nearest-neighbour shell have no continuum direction; any discrete assignment of r̂ introduces a local O(a) defect in the mass matrix that mixes the two chiralities.  
- This is the dominant lattice artefact.

### Sub-leading source: open (or periodic) boundaries

- Switching from open to periodic boundaries changes the sign of 〈γ⁵〉 but leaves its magnitude essentially unchanged.  
- Boundaries contribute an O( few percent ) mixing that does not vanish with the present volumes; it is expected to fall as the mode becomes more core-localised relative to the box size (L a ≫ w).

### Negligible in the present window: pure kinetic discretisation error

- The central-difference operator is O(a²).  
- Because the eigenvalue remains an exact zero under refinement, the kinetic error does not lift the mode; any chirality mixing it induces is smaller than the angular artefact already isolated.

### Control confirmation

- Removing the angular texture entirely (radial-only mass) destroys the protected zero eigenvalue (\|λ\| jumps to 10⁻²).  
- Thus the angular hedgehog is both the origin of the topological zero-mode and the origin of the leading chirality-mixing artefact.

---

## 4. Continuum-limit implication

The residual mixing is an ultraviolet lattice artefact localised on the scale of a single lattice spacing at the core.  
Consequently it must vanish in the continuum limit once the angular texture is resolved by many points inside the core radius w:
\[
\langle\gamma^5\rangle_{\mathrm{lat}} - \langle\gamma^5\rangle_{\mathrm{cont}} \;\sim\; O\bigl(a/w\bigr)\quad\text{or}\quad O\bigl((a/w)^2\bigr).
\]
A sequence with fixed physical core width w and a → 0 (i.e. more lattice points inside the core) is the cleanest way to extrapolate 〈γ⁵〉 → ±1.

---

## 5. Practical remedies (in order of simplicity)

1. **Smoothed angular definition** (already shown to work) — reduces residual to the per-mille level at current spacings.  
2. **Finer resolution of the core** — increase the number of sites inside r ≲ w while keeping the same continuum profile.  
3. **Larger volume** — suppress the residual boundary contribution.  
4. Optional: hedgehog–anti-hedgehog pair on a periodic lattice (net topology zero) to eliminate boundary chirality mixing entirely.

---

## 6. Status inside the Callan-Harvey program

| Quantity                        | Continuum expectation | Lattice status after isolation |
|---------------------------------|-----------------------|--------------------------------|
| Zero eigenvalue                 | Exactly zero          | Exactly zero (protected)       |
| Core localisation               | Exponential / power   | Stable ∼ 70 % in core shells   |
| Chirality 〈γ⁵〉                  | ±1                    | Residual O(10⁻²) dominated by angular discretisation at origin; removable by smoothing or continuum extrapolation |

The residual chirality mixing is fully understood: it is a short-distance lattice artefact arising from the discrete sampling of σ · r̂ at the hedgehog core. It does not obstruct the continuum Callan-Harvey construction or the index theorem.

---

## 7. Compact statement

The few-percent residual 〈γ⁵〉 is caused primarily by the ill-defined lattice direction r̂ at the origin. Smoothing the angular texture on the scale of one lattice spacing reduces the mixing by an order of magnitude. Boundaries contribute a comparable but non-dominant piece. Both artefacts vanish in the continuum limit at fixed physical core size. The topological zero-mode itself remains exact and core-localised throughout.
