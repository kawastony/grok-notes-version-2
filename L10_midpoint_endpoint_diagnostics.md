# Midpoint / endpoint diagnostics (L=10, d=3)

Tony Kawas / 19 September 2026.

**Finite-difference language:** tilt (slope), sharedness, packed intensity, midpoint curvature.

\[
D_1=\frac{P_2-P_1}{P_1+P_2},\quad
S=\frac{B_\rho}{P_1+P_2},\quad
C_s=\frac{B_\rho}{(\mathrm{span})(\mathrm{width})},\quad
K=\frac{2M-(P_1+P_2)}{P_1+P_2+2M}
\]

\(M\) = density in a thin slab about the geometric midpoint (tube-restricted).

Plots: `diag_bars.png`, `axial_profiles.png`, `midplane_slices.png` in artifacts / local run.

---

## Table (mode 0)

| case | \|λ\| | D1 (tilt) | S | Cs | M | K | E | span | width |
|------|--------|-----------|------|--------|------|--------|------|------|-------|
| baseline | 0.00139 | **−0.18** | **0.88** | 0.0048 | 0.054 | **+0.20** | 0.53 | 3.37 | 3.88 |
| +15% | 0.00004 | **+0.03** | 0.61 | **0.0078** | **0.062** | −0.04 | 0.62 | 2.94 | 3.52 |
| −15% | 0.00093 | **+0.29** | 0.69 | 0.0060 | **0.035** | **−0.16** | 0.59 | 3.22 | 3.39 |

\(E=(P_1+P_2)/(P_1+P_2+B_\rho)\) = end fraction.

---

## Reading

### Boost (+15%)
- **D1 → 0**: balanced (slope analogue vanishes)
- **Cs ↑**: more bridge weight per unit geometry (densified sharing)
- **S ↓**: because endpoints rose *more* than Brho (pair region fills, ratio shifts)
- **K → ~0**: midpoint no longer excess relative to ends
- **M ↑ slightly**: absolute midpoint still rises

**Collective compactification:** more balanced, denser packing, midpoint holds absolute support.

### Weaken (−15%)
- **|D1| ↑**: polarized (AH-heavy)
- **M ↓**: midpoint loses absolute support
- **K more negative**: end-heavy relative to middle
- still span/width down, Cs modest

**Polarized compactification:** tilted, midpoint relatively hollowed.

---

## Finite-difference analogy

| Calculus | Pair observable |
|----------|-----------------|
| symmetric slope at center | D1 (tilt) |
| midpoint vs ends (curvature-like) | K or D2 |

Useful organizing language; not a theorem that the mode is \(f(x)=x^2\).

---

## Compact statement

Boost: tilt collapses, packed bridge intensity rises, midpoint holds.  
Weaken: tilt grows, midpoint support falls, curvature K more end-heavy.  
Same compactification, different midpoint/endpoint structure.
