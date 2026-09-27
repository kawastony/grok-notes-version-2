# Spectral flow diagnostics — operational checklist

**Purpose:** Practical tests that spectral motion is real and index is conserved on the lattice paths used for G12 / scale-transfer.

---

## 1. What to track along path s

| Diagnostic | Quantity | Pass |
|------------|----------|------|
| Soft spectrum | Sorted \|λ_a\| for a=1…k | Remain soft vs bulk; continuous in s |
| Zero crossings | Signed crossings of λ=0 (or window) | Net crossings = 0 if topology fixed |
| Index proxy | n(|λ|<λ_cut) or spectral asymmetry | Constant along s |
| Core charges | Q_1(s), Q_2(s) | Flat within numerical tolerance |
| Weight slide | P_1(s), P_2(s), G12 | Can move; reports activity |
| Subspace metric | Tr(P_s P_{s+ds}), geodesic length | Smooth; no rank collapse |
| Localization | IPR, core fraction | Soft modes stay core/tube-localized |
| Residual | \|Hψ−λψ\|/\|ψ\| | Below acceptance gate |

---

## 2. Spectral-flow algorithm (minimal)

1. Build H(s) on a discrete path (boost, v_coup, separation).
2. Compute k lowest eigenpairs (ARPACK/PRIMME/matrix-free as available).
3. Match modes across s by overlap max |⟨ψ_a(s)|ψ_b(s+ds)⟩| (avoid label swaps at avoided crossings).
4. Record λ_a(s), P_core, Q, residuals.
5. Report: max |ΔQ|, net zero-crossings, max G12, path geodesic in soft subspace.

---

## 3. Failure signatures

| Symptom | Likely cause |
|---------|----------------|
| Index jumps | Topology change, pair creation, or mode lost below cut |
| Q drifts smoothly | Measurement bias / incomplete sphere integral, not true topology change |
| Soft mode delocalizes to boundary | Finite-volume edge mode contamination |
| Residuals spike | Solver not converged; tighten tol / increase maxiter |
| Rank collapse in soft projector | Gap closing; path hits singular background |

---

## 4. Link to coarse-graining

Diagnostics supply the inputs of COARSE_GRAINING_MICRO_TO_MESO.md:
- A_c from |∂_s λ| and |∂_s w|
- L_c from Index/Q stability
- ξ_corr from tube width / separation where weight is shared

If diagnostics fail, the upward map is not trusted.

---

## 5. Status

Operational layer on top of SOFT_MODE_SPECTRAL_MOTION and TOPOLOGICAL_INDEX_CONSERVATION. Ready to drive lattice path reports.
