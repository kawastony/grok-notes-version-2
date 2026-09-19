# Ricci flow dynamics — investigation

Tony Kawas / 19 September 2026.

**Scope:** What Ricci flow is, discrete analogues, and what is realistic for the lattice pair program.  
**Not claimed:** continuum GR, Einstein equations, or spacetime evolution of the cone.

---

## 1. Continuum Ricci flow

Hamilton’s Ricci flow on a Riemannian metric \(g\):
\[
\frac{\partial g_{ij}}{\partial t} = -2\,\mathrm{Ric}_{ij}(g).
\]

- Positive Ricci regions contract; negative expand (roughly).
- Used by Perelman to prove the Poincaré conjecture (with surgery).
- Requires a smooth manifold and a true Ricci tensor from a metric connection.

**We do not have that** for soft-mode densities. Shape tensor \(M_{ij}\) and Forman curvature on a density graph are **not** continuum Ricci of a spacetime metric.

---

## 2. Discrete Ricci flow (what is available)

Two standard graph discretizations:

| Notion | Idea | Cost |
|--------|------|------|
| **Forman–Ricci** | Combinatorial Bochner-type formula on edges | Cheap, local |
| **Ollivier–Ricci** | Optimal transport between neighborhood measures | Expensive |

**Forman flow** (common update):
\[
\frac{d}{dt} w_e = -F(e)\, w_e
\]
or normalized
\[
\frac{d}{dt} w_e = -\bigl(F(e)-\bar F\bigr) w_e.
\]

Intuition: edges with more positive curvature tighten; more negative loosen — used in network science for community detection and change detection (Weber–Jost–Saucan and others).

This is **graph geometry dynamics**, not continuum Ricci flow of GR.

---

## 3. Link to our Stage-2 work

We already compute static Forman curvature on the pair-tube density graph:

| case | mean mid \(F\) |
|------|----------------|
| baseline | −9.28 |
| +15% | −8.71 |
| −15% | −8.72 |

All negative (dense local lattice neighborhoods). Relative differences exist; absolute scale is not universal.

**Ricci flow dynamics** would mean: evolve edge weights under Forman flow and track whether mid-bridge edges strengthen or thin — a discrete “bridge health” evolution, still not spacetime.

---

## 4. Numerical probe (baseline tube graph)

Normalized Forman flow, \(\Delta t=0.05\), fixed vertex weights from soft-mode density:

| step | mean \(F\) | mid \(F\) | \(W_{\rm mid}/W_{\rm tot}\) |
|------|-----------|----------|---------------------------|
| 0 | −8.44 | −9.28 | 0.40 |
| 4 | −8.90 | −10.01 | **0.50** |
| 8 | −11.17 | −12.71 | **0.58** |
| 10 | −18.1 | −17.7 | 0.41 |
| 12+ | blows up | — | collapses |

**Early transient:** mid-tube weight fraction **rises** (bridge gains relative weight under normalized flow).  
**Later:** instability / collapse — discrete Forman flow on this dense, uniformly negative-curvature lattice graph is **numerically fragile** without extra regularization (clipping, adaptive step, different normalization).

Unnormalized flow (\(dw = -F w\,dt\)) grows total weight because \(F<0\) everywhere — expected and not informative.

---

## 5. What this means for identity / propagation / unification

| Theme | Ricci flow relevance |
|-------|----------------------|
| **Identity** | Limited. Static Forman already weak as a boost/weaken separator; flow adds dynamics of edge weights, not a new identity invariant. |
| **Propagation** | Suggestive as a *model* of bridge evolution, but it evolves **graph weights**, not the Dirac soft mode or a continuity equation for \(\rho_\chi\). |
| **Unification** | Methodological only: same discrete-geometry language. Does not unify with cone \(R_{\rm cone}\) or Callias asymptotics. |

---

## 6. Realistic path (if pursued)

1. **Stabilize** discrete Forman flow (smaller \(\Delta t\), weight clips, volume renormalization).  
2. Compare flow trajectories of baseline vs +15% vs −15% initial graphs — do mid-bridge weights diverge differently?  
3. Do **not** identify flow limits with continuum Ricci solitons or Einstein metrics.  
4. Optional: Ollivier flow on a coarse-grained bridge graph (costly).  
5. True propagation still needs dynamics of the fermion/mode or a constitutive current law — not only edge-weight flow.

---

## 7. Compact statement

Ricci flow in the continuum is metric evolution driven by Ricci curvature. On our pair-tube graph, a **discrete Forman flow** is the honest analogue: it can transiently shift weight toward mid-bridge edges but is unstable on this uniformly negative-curvature lattice without regularization. It is a legitimate Stage-2 *dynamics* experiment on network geometry, not a derivation of GR or a replacement for soft-mode identity diagnostics. Einstein language remains out of scope.
