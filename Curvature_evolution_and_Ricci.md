# Curvature evolution and Ricci curvature landscape

Tony Kawas / 19 September 2026.

Real 8-component Wilson–Dirac + hedgehog operator. Early Forman-flow window.

---

## A. Curvature evolution (numerical)

### Relative mid curvature controls feeding

\[
F^{\rm rel}_{\rm mid} = F_{\rm mid} - \bar F
\]

| Identity | \(F^{\rm rel}(0)\) | frac mid edges in gain sector | \(\Delta W_8\) |
|----------|-------------------|-------------------------------|---------------|
| B (2,2) | **−0.84** | **0.66** | **+0.088** |
| B (2.3,2) | −0.55 | 0.65 | +0.034 |
| T (1.85,2) | −0.55 | 0.52 | +0.033 |
| P (1.7,2) | **−0.33** | **0.46** | **+0.001** |

**Correlation** \((F^{\rm rel}(0),\,\Delta W_8) = -0.997\) on these four archetypes:  
more negative relative mid curvature ↔ larger early bridge feeding.

### Evolution pattern

- Absolute \(F_{\rm mid}\) becomes more negative under flow for all classes (early window).
- Relative depth \(F^{\rm rel}\) **deepens** for strong feeders (B: −0.84 → −1.05) and stays shallow for P.
- Fraction of mid edges in the gain sector (\(F < \bar F\)) starts highest for B and lowest for P.

So curvature evolution is **self-reinforcing for feeders**: deep relative well → weight flows mid → relative well can deepen further in the early window. Polarized states lack that feedback.

---

## B. Ricci curvature landscape (what exists)

| Notion | Definition idea | Cost | Role in this project |
|--------|-----------------|------|----------------------|
| **Continuum Ricci** | Trace of sectional curvature; enters Einstein equations | Smooth metric required | **Not available** — no spacetime metric here |
| **Forman–Ricci** | Combinatorial Bochner-type on edges | Cheap, local | **What we use** — drives the flow |
| **Ollivier–Ricci** | 1 − W₁(μ_u,μ_v)/d(u,v) optimal transport | Expensive | Optional future check; correlated with Forman in many networks |
| **Lin–Lu–Yau** | Limit form of Ollivier | Medium | Not used |

### Continuum Ricci flow (reference only)
\[
\partial_t g_{ij} = -2\,\mathrm{Ric}_{ij}.
\]
Positive Ricci regions shrink; used by Hamilton/Perelman for geometrization.  
**We do not have** a continuum metric or Ricci tensor on soft-mode support.

### Discrete Forman flow (what we run)
\[
\frac{dw_e}{dt} = -\bigl(F(e)-\bar F\bigr) w_e.
\]
Same *architectural* idea (curvature drives metric/weight change), different mathematical object.

### Why absolute Forman was weak, relative Forman is strong

Static absolute \(F_{\rm mid}\) barely separated B vs P (all ~ −8.7 to −9.3).  
**Relative** \(F^{\rm rel}_{\rm mid}\) and the **fraction of mid edges in the gain sector** separate cleanly and predict \(\Delta W\) almost perfectly on the archetype set.

---

## C. Unified micro picture

```
soft-mode density ρ
    → shape identity (R_mid, H_mid, P, A)
    → density-weighted tube graph
    → Forman F(e) and F^rel_mid
    → early Forman flow
    → slope / ΔW_mid  (mesoscopic response)
```

One flow law; identity sets relative curvature position; relative curvature sets early trajectory.

---

## D. What not to claim

- Forman ≠ continuum Ricci  
- Graph flow ≠ Einstein gravity  
- No derivation of a_T / galactic law from F^rel  
- Ollivier not yet computed on this operator (optional consistency check only)

---

## Compact statement

Curvature evolution under Forman flow is organized by relative mid-tube curvature: feeders start with a deep relative well and a high fraction of mid edges in the gain sector; polarized/hollowed states start shallow and nearly stall. Absolute Forman levels look similar across classes; relative Forman and gain-sector fraction are the dynamical discriminants. Continuum Ricci remains a separate mathematical object — not instantiated by this lattice program.
