# 4-mode soft subspace tracking along boost path

**Date:** 2026-09-25  
**Setup:** L=10, d=3, ε=0.05, residual gate 1e−6, s ∈ {0, 0.25, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75, 1.0}

## Method

1. Compute residual-accepted soft multiplet (k=4) at each s.
2. Sequential **max-overlap matching** (Hungarian on |⟨i|j⟩|) between consecutive s.
3. **Projector continuity:** for soft projectors P(s)=VV†,
   \(\|P-Q\|_F^2 = n_P+n_Q-2\mathrm{Tr}(PQ)\).
4. Track per-branch λ and dP after matching; also subspace dS.

## Key result

### Projector stays continuous through the bottleneck

| step | \(\|P-Q\|_F^2\) | Tr(PQ) (max 4) |
|------|------------------|----------------|
| 0.00→0.25 | 2.52 | 2.74 |
| 0.25→0.40 | 2.35 | 2.82 |
| 0.40→0.45 | 2.06 | 2.97 |
| **0.45→0.50** | **0.16** | **3.92** |
| 0.50→0.55 | 2.09 | 2.96 |
| 0.55→0.60 | 2.08 | 2.96 |
| 0.60→0.75 | **5.29** | **1.36** |
| 0.75→1.00 | **4.85** | **1.57** |

At the narrowest gap (**0.45→0.50**), Tr(PQ)≈**3.92/4**: the **soft subspace as a whole barely changes**, even though ordered eigenvalues reorganize.

Late path (0.60→1.00): large projector distance — subspace composition **does** change substantially toward the endpoint.

### Individual mode labels are unreliable

Pairwise max overlaps along the path often include **near-zero** entries (e.g. 0.004, 0.042, 0.045). Mean overlap per step ≈0.69 early, drops to ≈0.44–0.49 late.

Sequential branch tracking therefore **scrambles** identity: a “branch 0” λ string crosses zero and jumps — not a physical adiabatic level, an artifact of forced matching when states mix.

**Implication:** do **not** trust softest-only or single-branch dP through the bottleneck. Trust **subspace** observables (dS, Tr(PQ), Frobenius distance).

## Subspace dS (unchanged diagnostic)

```
s:   0.00   0.25   0.40   0.45   0.50   0.55   0.60   0.75   1.00
dS:  ~0   -0.003  -0.001  -0.003  -0.002  -0.001  -0.003  -0.006  -0.009
```

Endpoint G_subspace from baseline remains ≈ −0.176 (as before).

## Effective-model conclusion

| Model | Verdict |
|-------|--------|
| 2-level avoided crossing | Insufficient (prior note) |
| Ordered softest eigenvalue | Unstable under reordering |
| Overlap-tracked single branches | Unstable when min overlap → 0 |
| **Soft projector P_soft(s) + subspace dS** | **Stable through bottleneck; preferred** |

Minimal honest effective description:

> The residual soft sector is a **4-dimensional subspace** that evolves continuously under one-core boost (especially through the gap minimum). Observable influence is the **subspace-averaged** core-weight imbalance dS(s). Individual instantaneous eigenlabels are gauge-like under multiplet mixing.

A quantitative 4×4 H_eff(s) would require a smooth frame (e.g. parallel transport of the basis inside P_soft); sequential matching alone is not enough when overlaps collapse.

## Locked claims

1. Soft **projector** is continuous at the path bottleneck (Tr(PQ)≈4).
2. Mode **labels** are not — multiplet mixing is real.
3. Subspace dS is the correct propagation diagnostic for this system.
4. Late-path projector drift (0.6→1.0) shows the endpoint deformation is not only a local avoided crossing; the soft sector content shifts.

## Data

`data/G12_4mode_subspace_track.json`

## Related

- `G12_avoided_crossing_fit.md` — 2-level rejected
- `G12_subspace_and_d5_scan.md` — subspace G at d=3,5
- `G12_spectral_flow_scan.md` — quasi-SF path
