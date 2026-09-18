# L=10 texture-bridge analysis (residual-validated)

Tony Kawas / 18 September 2026.

**Status:** Soft modes residual-converged (rel_v ~ 10⁻¹³). Bridge diagnostics run only on trusted eigenvectors.

**Settings:** CORE_R=2, BRIDGE_R=1.5, pair along z, m₀=0.3, v=2, w=1.

---

## Observables

| Symbol | Meaning |
|--------|--------|
| QT | global texture charge ∑ χ_T |
| t₁, t₂ | core-normalized texture alignment |
| ST=1 | both cores anti-aligned (t₁<0, t₂<0) |
| Bρ | plain density in bridge tube |
| BT | texture-weighted bridge ∑ ρ max(0,−χ_T) in tube |
| A, A_T | raw vs texture-weighted anisotropy |

---

## Results (modes 0–1)

| d | n | \|λ\| | P₁ | P₂ | Prest | QT | t₁ | t₂ | ST | Bρ | BT | A | A_T | class |
|---|---|------|------|------|-------|------|------|------|----|------|------|------|------|--------|
| 1 | 0 | 0.0036 | 0.029 | 0.032 | 0.94 | −0.65 | −0.47 | −0.60 | 1 | 0.020 | ~0 | 0.81 | 1.52 | shared anti-aligned |
| 1 | 1 | 0.0046 | 0.019 | 0.022 | 0.96 | −0.70 | −0.38 | −0.54 | 1 | 0.013 | ~0 | 0.92 | 1.76 | shared anti-aligned |
| 2 | 0 | 0.0008 | 0.073 | 0.036 | 0.89 | −0.65 | −0.69 | −0.42 | 1 | 0.052 | 1.2e-4 | 0.55 | 0.68 | **texture-bound molecular** |
| 2 | 1 | 0.0039 | 0.007 | 0.007 | 0.99 | −0.84 | −0.48 | −0.53 | 1 | 0.007 | ~0 | 1.02 | 1.01 | anti-aligned weak share |
| 3 | 0 | 0.0014 | 0.042 | 0.029 | 0.93 | −0.83 | −0.88 | −0.74 | 1 | 0.063 | **1.8e-4** | 0.82 | 1.04 | **texture-bound molecular** |
| 3 | 1 | 0.0015 | 0.031 | 0.028 | 0.94 | −0.80 | −0.82 | −0.86 | 1 | 0.049 | 8e-5 | 0.66 | 0.84 | shared anti-aligned |
| 4 | 0 | 0.0005 | 0.030 | 0.023 | 0.95 | −0.80 | −0.86 | −0.88 | 1 | 0.045 | 6e-5 | 0.85 | 1.46 | shared anti-aligned |
| 4 | 1 | 0.0011 | 0.034 | 0.031 | 0.94 | −0.83 | −0.83 | −0.87 | 1 | 0.055 | 9e-5 | 0.85 | 1.43 | shared anti-aligned |
| 5 | 0 | 0.0004 | 0.009 | 0.009 | 0.98 | −0.86 | −0.88 | −0.88 | 1 | 0.033 | 5e-5 | 0.21 | 0.07 | anti-aligned weak share |
| 5 | 1 | 0.0008 | 0.030 | 0.030 | 0.94 | −0.86 | −0.87 | −0.87 | 1 | 0.057 | 7e-5 | 0.29 | 0.10 | shared anti-aligned |

---

## Main findings

1. **Texture anti-alignment is universal at L=10**  
   ST=1 for every soft mode (both cores t₁,t₂ < 0). QT ≈ −0.65 to −0.86.

2. **Spatial sharing is real but core weights are modest**  
   P₁,P₂ typically 2–7%; Prest dominates (molecular delocalization on the torus).

3. **Texture-weighted bridge BT is small but nonzero**  
   Peak ~1.8×10⁻⁴ at d=3 mode 0. Most modes have BT ~ 10⁻⁵–10⁻⁴.  
   Plain bridge Bρ is larger (few %). Soft weight sits more in the bulk/rest than in a tight texture-lit corridor.

4. **A_T vs A**  
   At intermediate d, A_T is often **larger** than A (texture weight prefers more elongated support).  
   At d=5, both A and A_T drop (more isotropic / transverse).

5. **“Texture-bound molecular” label**  
   Strict (shared + anti-aligned + BT>10⁻⁴) hits at **d=2 mode0** and **d=3 mode0**.  
   Broader “shared anti-aligned” covers most of the scan.

---

## What this secures

At residual-validated L=10:

> Soft modes are texture-anti-aligned on **both** cores, spatially shared (not single-core), and carry a weak but measurable texture-weighted bridge contribution at intermediate separation.

That is a **validated numerical structure**, not a solver artifact.

---

## What this does not claim

- L=12 continuation  
- Asymptotic isolation  
- Gravity / elongation cycle  
- Transport current from BT  

---

## Compact statement

On residual-converged L=10 soft modes, texture anti-alignment is robust on both defect cores; the pair is molecular (shared, delocalized); a weak texture-weighted bridge appears at intermediate d. L=10 is the trusted platform for these diagnostics.
