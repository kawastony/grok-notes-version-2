# Amplitude bookkeeping — no double-counting

## Objects that enter a_eff

| Symbol | Value / origin | Role |
|--------|----------------|------|
| κ_0 | 0.394 (earlier TAFA geometric stiffness) | √κ_0 or √(2κ_0) in a_eff |
| Q | √2 (Paper 14 cone-sector matching) | multiplicative geometric factor |
| C_ang | √(κ_0/(sin ψ_1 cos ψ_2)) = 1.4172 with ψ_1=35°, ψ_2=70° | angular packing of cone sector |
| A | free normalization in Paper 24 fits | overall scale |
| R_cone | √6/φ ≈ 1.51387 (activation surface) | micro cone amplitude (not yet in Paper 24 a_eff formula) |
| B | topological stiffness correction | degenerate with A in current fits (untested) |

## Preferred empirical form (Paper 24 winner)

\[
a_{\rm eff}=A\sqrt{2\kappa_0}\,\Bigl(\frac{\Sigma_b}{\Sigma_{\rm ref}}\Bigr)^\gamma
\]

Here Q does **not** appear as a free multiplier: the winning surface-density model absorbs angular/Q content into A√(2κ_0). The radius-law models that *did* carry Q explicitly were disfavored.

## Double-counting risks

1. **Q and C_ang:** both encode cone-angle geometry. Using Q×C_ang×√κ_0 together without a derivation that they are independent overcounts angle information.
2. **R_cone and √(2κ_0):** both are O(1) geometric amplitudes from cone structure. Promoting R_cone as an extra multiplier on top of fitted A√(2κ_0) without a matching relation double-counts the same geometric layer.
3. **B and A:** Paper 24 states B is absorbed into normalization; adding B as free does not improve fit.

## Canonical amplitude rule (working)

**For SPARC / Paper 24 phenomenology:**
\[
a_{\rm eff}=A\,\sqrt{2\kappa_0}\,\Bigl(\frac{\Sigma_b}{\Sigma_{\rm ref}}\Bigr)^{1/7}
\]
with A fitted once; κ_0 fixed; Q fixed at √2 only when a model explicitly requires it (radius-law branch, already disfavored).

**For micro cone / R_cone contact:** treat R_cone as a candidate identification for the same O(1) geometric factor that A√(2κ_0) calibrates — **one** amplitude, two descriptions — until an explicit matching
\[
A\sqrt{2\kappa_0}\;\stackrel{?}{=}\;f(R_{\rm cone},\varphi,\ldots)
\]
is derived. Do not multiply them.

## Status

| Item | Status |
|------|--------|
| κ_0 fixed | yes |
| Q free to fix at √2 | yes (no cost) |
| A fitted | yes |
| R_cone independent extra factor | **no — risk of double-count** |
| B independent | no (degenerate) |
