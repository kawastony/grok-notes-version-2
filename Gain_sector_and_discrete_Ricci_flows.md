# Gain-sector dynamics and discrete Ricci flows

Tony Kawas / 19 September 2026.

Real 8-component operator. Early window only.

---

## 1. Gain-sector dynamics (normalized Forman)

**Gain sector** = mid-tube edges with \(F(e) < \bar F\) (more negative than mean → weight increases under norm Forman).

| Identity | frac_gain(0) | frac_gain(8) | Frel(0) | ΔW_8 |
|----------|--------------|--------------|---------|------|
| **B (2,2)** | **0.66** | 0.59 | **−0.84** | **+0.088** |
| T (1.85,2) | 0.52 | 0.49 | −0.55 | +0.033 |
| **P (1.7,2)** | **0.46** | **0.39** | **−0.33** | **+0.001** |

### Reading

- B starts with ~2/3 of mid edges in the gain sector; P under half.
- Under flow, frac_gain **slowly declines** for all (reweighting shifts the mean), but B keeps a higher floor longer.
- Weight in mid∩gain (W_gain_mid) tracks the same ordering as ΔW.
- Gain-sector occupancy is both a **static predictor** and a **dynamical intermediate**: high initial occupancy → strong early feeding.

---

## 2. Three discrete flow rules (same graph, same F)

| Rule | Update | ΔW_8 (B) | ΔW_8 (P) |
|------|--------|----------|----------|
| **Normalized Forman** (default) | \(dw = -dt(F-\bar F)w\), renorm | **+0.088** | **+0.001** |
| Absolute Forman | \(dw = -dt\, F\, w\), renorm | +0.074 | +0.002 |
| Gain-only | only edges already in gain sector update | +0.064 | **−0.003** |

### Observations

1. **Ordering B ≫ P is stable across all three rules** — not an artifact of mean-subtraction alone.
2. Absolute Forman (no mean subtract) still feeds B and stalls P; slightly weaker ΔW for B.
3. Gain-only is stricter: P goes slightly negative (mid weight leaks), while B still feeds.  
   That underscores: **without enough edges already in the gain sector, the bridge cannot self-reinforce.**

---

## 3. Discrete Ricci-flow landscape

| Flow family | Driver | Status here |
|-------------|--------|-------------|
| **Normalized Forman** | \(F-\bar F\) | **Primary** — stable early window, clean B/P split |
| Absolute Forman | raw \(F\) | Qualitative same split; less controlled |
| Gain-only threshold | \((F-\bar F)_-\) only | Emphasizes sector occupancy; P cannot feed |
| Ollivier-driven | \(\kappa_{\rm Oll}\) | Not usable yet — sample κ non-discriminating on this graph |
| Combinatorial Ricci (Chow–Luo type) | circle-pack / length from curvature | Not implemented; needs different discrete structure |
| Continuum Ricci | \(\partial_t g = -2\mathrm{Ric}\) | No continuum metric |

**Working definition for the program:** normalized Forman on the density-weighted soft-mode tube is the discrete Ricci-like flow that carries the identity→response mechanism.

---

## 4. Unified picture

```
identity
  → relative Forman depth F^rel
  → gain-sector fraction (static)
  → discrete flow (norm Forman / variants)
  → gain-sector weight evolution
  → ΔW / slope (response)
```

Gain-sector dynamics are the **time-resolved face** of the mediator: not only “how deep is the well” but “what fraction of the bridge sits in the well, and does that fraction sustain feeding under the flow.”

---

## 5. Scope

- Early window (≲10 steps) only  
- Graph discrete curvature, not continuum Ricci  
- No Einstein / a_T claim  
- Ollivier flow not supported by current κ sample

---

## Compact statement

Gain-sector occupancy starts high for balanced states and low for polarized/hollowed ones; under normalized Forman flow the B/P feeding split is robust across absolute and gain-only variants. Discrete Ricci-like dynamics in this program are Forman-driven; Ollivier-driven and continuum Ricci remain outside the present validated pipeline.
