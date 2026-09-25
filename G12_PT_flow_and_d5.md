# Projector-flow proxy and d=5 PT comparison

**Date:** 2026-09-25  
**Status:** Executed.

## 1. Flow proxy: close B_eff → dS

Hellmann–Feynman identity in the soft subspace:

\[
\frac{d}{ds}\mathrm{Tr}(P H)=\mathrm{Tr}\big(P\,\partial_s H\big)=\mathrm{Tr}(B_{\rm eff}).
\]

Empirical closure for the propagation observable:

\[
dS(s)\approx a\int_0^s \mathrm{Tr}(B_{\rm eff}(s'))\,ds' + b
\]

| Geometry | a | b | RMSE |
|----------|---|---|------|
| **d=3** | **−0.407** | ~0 | **0.00233** |
| **d=5** | **+0.148** | ~0 | **0.00228** |

- Sign of **a** matches sign of endpoint **G / dS** (negative at d=3, positive at d=5).
- RMSE ~0.002 on |dS| values up to ~0.01 → rough but **directional** closure: integrated boost trace predicts subspace imbalance trend.
- Not a full double-commutator projector PDE; it is the simplest integrated force law consistent with Tr(B_eff).

**Claim:** Propagation diagnostic dS is linearly correlated with the time-integrated soft boost trace, with geometry-dependent coupling a.

---

## 2. PT + B_eff at d=5 (geometry dependence)

### Continuity (Tr PQ)

| step | d=3 TrPQ | d=5 TrPQ |
|------|----------|----------|
| 0.00→0.25 | 2.74 | **0.15** (discontinuous jump) |
| 0.25→0.40 | 2.82 | 2.79 |
| 0.40→0.45 | 2.97 | 2.96 |
| **0.45→0.50** | **3.92** | **3.94** |
| 0.50→0.55 | 2.96 | **3.94** |
| 0.55→0.60 | 2.96 | **3.95** |
| 0.60→0.75 | 1.36 | 2.62 |
| 0.75→1.00 | 1.57 | 0.98 |

- Both geometries: **full-rank continuous soft subspace through s≈0.45–0.55**.
- d=5: first step 0→0.25 has **collapsed** singular values (TrPQ=0.15) — soft multiplet **re-forms** under even a mild boost; after that it is stable until late path.
- Late-path drift exists at both separations.

### B_off peak

| Geometry | max \|B_off\| | at s |
|----------|----------------|------|
| **d=3** | **0.036** | **0.50** (bottleneck) |
| **d=5** | **0.032** | **0.25** (early) |

- d=3: mixing peak coincides with gap compression (as before).
- d=5: largest off-diagonal boost matrix at **early** s, not at min\|λ\| (min\|λ\| still ~0.50).
- Mixing structure is **geometry-dependent**, not universal in s.

### Endpoint dS

| Geometry | dS(s=1) |
|----------|--------|
| d=3 | −0.00882 |
| d=5 | +0.00469 |

Matches prior subspace G signs.

---

## Combined reading

```
B_eff(s)  --Tr-->  integrated force  --a(d)-->  dS(s)
                geometry enters mainly as sign/magnitude of a
                and as location of B_off peak
```

| Result | Status |
|--------|--------|
| dS tracks ∫Tr(B_eff) with fit a(d) | **Shown** (RMSE~0.002) |
| Sign(a) = sign(endpoint dS) | **Shown** |
| Bottleneck continuity at both d | **Shown** |
| B_off peak location depends on d | **Shown** |
| Full double-commutator Ṗ integration | Not done (proxy only) |

---

## Data

`data/G12_PT_flow_and_d5.json`

## Related

- `G12_PT_Heff_Beff.md`
- `G12_subspace_and_d5_scan.md`
- `G12_4mode_subspace_track.md`
