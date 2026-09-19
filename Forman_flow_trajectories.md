# Stabilized discrete Forman flow trajectories

Tony Kawas / 19 September 2026.

L=10, d=3 pair tube. Initial edge weights from soft-mode density (baseline / +15% / −15%).  
Flow: normalized Forman, \(\Delta t=0.02\), weight clips, total-weight renormalization.

**This is graph edge-weight dynamics — not continuum Ricci flow or GR.**

---

## Protocol

\[
w_e \leftarrow \mathrm{clip}\bigl(w_e - \Delta t\,(F(e)-\bar F)\,w_e\bigr),\quad
\text{then renormalize }\sum w = W_0.
\]

Vertex weights fixed from initial soft-mode density. Mid edges = edges near geometric pair midpoint.

---

## Early trajectory (steps 0 → 10) — the usable window

| case | mid \(F\) (0) | mid \(F\) (10) | Δ mid \(F\) | \(W_{\rm mid}/W\) (0) | (10) | Δ \(W_{\rm mid}\) |
|------|---------------|----------------|-------------|----------------------|------|-------------------|
| baseline | −9.28 | −10.11 | −0.83 | **0.40** | **0.51** | **+0.11** |
| +15% | −8.71 | −9.47 | −0.76 | 0.26 | 0.30 | **+0.05** |
| −15% | −8.72 | −9.42 | −0.70 | 0.19 | 0.19 | **≈ 0** |

### Reading

- **Baseline:** mid-bridge weight fraction rises strongly under flow.  
- **+15% (boost):** starts more mid-peaked in Stage 1; mid weight still rises, but less.  
- **−15% (weaken):** starts mid-dipped / polarized; mid weight fraction **does not rise** — stays flat.

So the flow **amplifies the Stage-1 identity contrast**: collective/mid-healthy states feed the bridge under flow; polarized/hollow states do not.

---

## Late steps (15–25)

All three eventually drift: mid \(F\) becomes more negative and weight redistributes unstably. Discrete Forman flow on this dense all-negative lattice remains fragile beyond ~15 steps even with clips and renormalization. **Only the early window is trustworthy.**

---

## Relation to identity / propagation

| Theme | Finding |
|-------|--------|
| **Identity** | Flow trajectories **do** separate boost vs weaken in early \(W_{\rm mid}\) growth — consistent with Stage-1 shape, not a replacement for it. |
| **Propagation** | Still only edge-weight dynamics on a static density graph. No fermion current, no time-dependent Dirac mode. |
| **Unification** | Methodological only. |

---

## Compact statement

Stabilized Forman flow in the early window shows baseline and boost **feeding the mid-bridge**, while weaken does not. That matches Stage-1 mid-peak vs mid-dip identity. Late flow is numerically unstable. Discrete Ricci-type dynamics is a usable network-geometry probe, not continuum GR.
