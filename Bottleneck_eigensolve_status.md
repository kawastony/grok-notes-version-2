# Soft-mode eigensolve bottleneck — status

Tony Kawas / 17 September 2026.

---

## Goal

Extract soft modes at L ≥ 12 without OOM, to test spatial decoupling and mass-texture χ at larger separation.

---

## Attempts

### 1. Explicit sparse + shift-invert at L=12
- **Result: OOM (exit 137)** — same as earlier ceiling
- Assembly + ARPACK workspace still exceeds available memory

### 2. Matrix-free apply_H
- **Works** through L=14 (matvec ~few ms, Hermitian to 1e-16)
- Alone does not extract soft modes (need solver)

### 3. Matrix-free H² extremal (SA / LOBPCG)
- **Does not converge** without preconditioner / shift-invert
- Concept validated only with **sparse** K = H@H + sigma=0

### 4. Polynomial filter (I − H²/b²)^d + Rayleigh–Ritz
- Spectral radius estimated by power iteration
- **Partial:** brings some Ritz values into soft range, but does **not** match known soft spectrum accurately

| L | sparse soft \|λ\| | filter deg=100 (lowest 4) |
|---|------------------|---------------------------|
| 8 | 0.0004, 0.0016, 0.0019, 0.0032 | 0.009, 0.013, 0.014, 0.027 |
| 10 | 0.0008, 0.0015, 0.0022, 0.0026 | 0.0004, 0.012, 0.019, 0.023 |

Filter moves the subspace toward soft eigenvalues but is not precise enough for physics (ownership, χ_βn) without further tuning (degree, Jackson kernel, block filters, etc.).

---

## Current ceiling (honest)

| Capability | Status |
|------------|--------|
| Soft modes L ≤ 10 | **Reliable** (sparse shift-invert) |
| Soft modes L = 12 | **Not available** in this environment |
| Matrix-free matvec L ≤ 14 | OK |
| Mass-texture χ diagnostic | Done at L = 8, 10 |
| Spatial decoupling test at larger sep | Blocked on soft-mode extraction |

---

## What would fix it

1. **More memory** — sparse L=12 may fit on a larger machine
2. **Proper Chebyshev / Jackson filter** with known spectrum bounds and higher degree, or filtered Davidson
3. **Preconditioned MINRES** for iterative shift-invert on matrix-free H
4. **External library** (SLEPc, PRIMME, ARPACK with better reverse communication)

None of these is a small local patch in the present sandbox.

---

## Recommendation

- Treat **L ≤ 10** as the validated physics window for this campaign
- Keep matrix-free infrastructure for future larger runs
- Center the write-up on:
  - robust soft sector
  - molecular hybridization at accessible L
  - mass-texture organization (χ_βn ≈ −0.8 soft vs +1 bulk)
  - ruled-out shortcuts (width, m₀, 2D/4D rotation)

The diagnostic breakthrough (defect-aligned mass operator) does **not** require L=12. The bottleneck is real for geometric decoupling tests only.

---

## Compact statement

Sparse L=12 still OOMs. Simple matrix-free polynomial filtering partially softens the spectrum but does not recover accurate soft eigenvalues. Soft-mode physics remains reliable at L ≤ 10; larger-L decoupling tests stay blocked without more memory or a production-grade filtered eigensolver.
