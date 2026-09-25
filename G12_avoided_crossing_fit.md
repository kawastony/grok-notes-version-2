# Fine grid near s=0.5 and 2-level avoided-crossing fit

**Date:** 2026-09-25  
**Status:** Executed. Honest partial fit.

## Fine path (L=10, d=3, ε=0.05)

| s | min\|λ\| | second\|λ\| | gap12 | subspace dS |
|---|----------|-------------|-------|-------------|
| 0.00 | 0.001471 | 0.002959 | 0.001489 | ~0 |
| 0.25 | 0.001508 | 0.001767 | 0.000259 | −0.00321 |
| 0.40 | 0.000915 | 0.001789 | 0.000874 | −0.00084 |
| **0.45** | **0.000484** | **0.000583** | **0.000099** | −0.00265 |
| **0.50** | **0.000262** | **0.000776** | 0.000514 | −0.00219 |
| 0.55 | 0.000329 | 0.001313 | 0.000984 | −0.00088 |
| 0.60 | 0.000828 | 0.002267 | 0.001438 | −0.00328 |
| 0.75 | 0.000700 | 0.001543 | 0.000843 | −0.00621 |
| 1.00 | 0.000865 | 0.000970 | 0.000105 | −0.00882 |

**Narrowest gap:** near **s≈0.45** (gap12 ≈ 1×10⁻⁴), not exactly 0.50. Soft window minimum slightly before midpoint of the boost.

All points residual-accepted (n_acc=4).

## 2-level avoided-crossing model

Form fitted to (min\|λ\|, second\|λ\|):

```
mid(s)  = mid0 + mid1 · s
half(s) = h0 + h1 · s
λ±(s)   = mid(s) ± sqrt(half(s)² + V²)
```

**Best-fit parameters:**

| param | value |
|-------|-------|
| mid0 | +1.76×10⁻³ |
| mid1 | −1.14×10⁻³ |
| h0 | +5.38×10⁻⁴ |
| h1 | −3.42×10⁻⁴ |
| V | **≈1.2×10⁻⁶** (essentially vanishing) |

**RMSE** on abs eigenvalues ≈ 4.9×10⁻⁴

### Reading

- With **V≈0**, the “avoided crossing” reduces to **almost-crossing diabatic lines** — the model does **not** prefer a sizable hybridization gap.
- Fit tracks the **overall downward trend** of the soft window but **misses the deep min\|λ\| dip** at s=0.45–0.50 (data 2.6×10⁻⁴ vs fit ~8×10⁻⁴).
- **Conclusion:** a pure **2-level** model is **insufficient**. The residual-gated sector has **4 accepted modes**; reordering involves more than one pair. Effective description needs **≥3–4 levels** or a subspace projector flow, not a single Landau–Zener gap.

## dS empirical fit

```
dS(s) ≈ a + b s + c tanh((s−s0)/w)
```

Params ≈ (0.0029, −0.0151, 0.0030, 0.34, 0.10), RMSE ≈ 7.7×10⁻⁴.

Captures the **endpoint trend** (dS → more negative) better than the mid-path wiggles. Useful as a smooth summary, not a derivation.

## What this locks

1. Bottleneck is **real and localized** near s≈0.45–0.50 (finest grid).
2. Subspace dS remains coherent (negative, growing) despite softest-mode drama.
3. **2-level avoided crossing is not the right minimal model** for this multiplet — upgrade path is few-level / projector-based effective theory.

## What this does not lock

- Integer spectral flow
- Continuum 2-level theorem
- L=12 path (not run here; expensive)

## Next theoretical step

Build effective Hamiltonian in the **4-dimensional residual soft subspace** (or at least 3-level) along s, and track the **projector** P_soft(s) rather than ordered eigenvalues alone.

## Data

`data/G12_avoided_crossing_fit.json` (summary); full local scan in artifacts.
