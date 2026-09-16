# Finite-size scaling analysis of the soft sector

Tony Kawas / 16 September 2026.

---

## 1. Purpose

Assess how the soft eigenvalues, core weight, and IPR of the hedgehog–antihedgehog pair scale with volume, and what that implies for the continuum / isolated-defect limit.

---

## 2. Consistent series (this work)

Fixed: w = 1.0, v = 2.0, sep ≈ L/2, R = 2.0 diagnostic ball, 8-component Wilson + Callias pair, periodic BC.

| L | sep | \|λ₁\| | \|λ₂\| | Δλ | P_core (mode 0) | IPR |
|---|-----|-------|-------|-----|-----------------|-----|
| 6 | 3 | 0.00831 | 0.00880 | 0.00049 | 0.258 | 0.0062 |
| 7 | 4 | 0.00636 | 0.00971 | 0.00335 | 0.072 | 0.0040 |
| 8 | 5 | 0.00043 | 0.00164 | 0.00207 | 0.095 | 0.0026 |
| 10 | 6 | 0.00078 | 0.00150 | 0.00072 | 0.032 | 0.0009 |

Plus earlier Phase 1/2 data at varied (w, v): soft sector always present; post-rotation ownership ΔP ≲ 0.03.

---

## 3. Crude power-law checks

\(|\lambda_1|\cdot L\), \(|\lambda_1|\cdot L^2\), \(|\lambda_1|\cdot L^3\) are **not** approximately constant. L = 8 is anomalously soft relative to L = 6, 7, 10. A single power law does not describe the series.

Possible reasons:
- Separation is discrete and jumps with L; the physical sep/w ratio is not held fixed smoothly.
- Finite-volume image interactions of the pair on the torus are non-monotonic in L.
- Residual Wilson / mass-scale artefacts that do not scale out cleanly at these small L.

---

## 4. Expected continuum scaling (theory)

For an isolated Callias defect in infinite volume one expects exact zero modes (up to exponentially small corrections from the continuum edge of the bulk gap). On a finite torus with a compensated pair:

\[
|\lambda_{\rm soft}| \sim e^{-{\rm sep}/\xi} \quad \text{or} \quad \sim (\xi/{\rm sep})^p e^{-{\rm sep}/\xi}
\]

for some correlation length ξ set by the bulk gap and core width — **exponential** decoupling with separation, not a pure power of L.

IPR of a fully localized core mode should approach a constant set by the core volume (∼ w³), independent of L once sep ≫ w. Shared molecular modes have IPR that falls as the support spreads over both cores and possibly the bulk.

P_core in a fixed physical ball should rise toward O(1) for an isolated mode and stay ∼1/2 per core for a hybridized pair.

---

## 5. What the data show

| Observable | Trend L = 6 → 10 | Consistent with isolated cores? |
|------------|------------------|----------------------------------|
| Soft \|λ\| | Remains O(10⁻³–10⁻⁴); non-monotonic | Soft sector yes; not yet exp-small |
| Δλ | O(10⁻³) | Hybridization splitting still large |
| P_core | Decreases | Opposite of isolated-core expectation |
| IPR | Decreases | Modes become more volume-spread |
| Post-rotation ΔP | ≲ 0.03 | No single-core ownership |

**Conclusion:** within the accessible window the system remains in the **molecular regime**. Softness is robust; localization and decoupling are not improving with L at fixed sep ∼ L/2.

---

## 6. Proper finite-size scaling protocol (for larger resources)

To claim continuum / isolated-defect scaling one needs:

1. **Fixed physical separation** in units of core width: sep / w = constant ≫ 1 (e.g. 8, 10, 12), while L → ∞.  
2. **Or** fixed sep / L with L large enough that sep ≫ w and bulk gap is resolved.  
3. Track:
   - \(|\lambda_1|(L)\), \(|\lambda_2|(L)\), Δλ(L)
   - IPR(L), P_core(L) in a ball of fixed physical radius
   - post-rotation ownership ΔP(L)
4. Fit Δλ ∼ e^{−sep/ξ} or power-law corrections; demand ΔP → O(1) and IPR → core-volume constant.

Until that protocol is feasible (L ≳ 12–16), finite-size scaling remains incomplete.

---

## 7. Compact statement

A consistent L = 6–10 series with sep ≈ L/2 shows a robust soft sector but non-monotonic eigenvalues, falling P_core and IPR, and no post-rotation core ownership. The data are compatible with a molecular (hybridized) regime and do not yet exhibit the exponential decoupling expected for isolated Callias cores. Proper finite-size scaling requires larger L at fixed sep/w ≫ 1, which exceeds the current memory ceiling.
