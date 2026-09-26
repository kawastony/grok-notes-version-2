# Midpoint stability, DE/DM endpoints, holographic contact (Case A + B progress)

Freeze unchanged. Tool status: discovery/mapping, not SI-scale derivation from pure geometry.

---

## 1. Stability conditions for the midpoint

### 1.1 Raw quadratic flow (both cases)
\[
\frac{du}{d\xi}=\alpha\bigl(u_*^2+\Delta^2\bigr).
\]
- If α>0 and u>0: drives |u| upward — **unstable** as a fixed point for u itself.
- If α<0: drives toward smaller |u| — monotonic collapse, not a stable finite attractor at u_*.

So the raw law does **not** make u_* a stable fixed point of u.

### 1.2 Fixed-point form (preferred)
Write u = u_* + δu and impose relaxation to the midpoint:
\[
\frac{d\,\delta u}{d\xi}=-\gamma\,\delta u+\beta\,\Delta(\xi)^2,
\qquad \gamma>0.
\]

**Linear stability:** homogeneous part δu ∝ e^{-γξ} → attracts to δu=0 when Δ=0.  
**Driven response:** nonzero Δ sources a steady shift
\[
\delta u_{\infty}=\frac{\beta}{\gamma}\Delta^2
\]
(if Δ slowly varying). Midpoint remains the organizing center; endpoints only dress it.

**Stability condition summary**
| Condition | Role |
|-----------|------|
| γ>0 | Attractive midpoint |
| β finite | Controlled deformation |
| Δ bounded | No runaway branch split |
| α-only quadratic without −γδu | **Not** stable at finite u_* |

---

## 2. Case A progress — μ with Σ_b-driven Δ

\[
\mu(r)=\mu_*+\delta\mu(r),\qquad
\frac{d\delta\mu}{dr}=-\gamma\,\delta\mu+\beta\,\Delta(r)^2.
\]

**Explicit Δ model (first test):**
\[
\Delta(r)^2=\Delta_0^2\left(\frac{\Sigma_b(r)}{\Sigma_{\rm ref}}\right)^p.
\]

- p~0 → pure constant split.  
- p in 1/7-class → density-driven deformation compatible with shallow response.  
- Empirical question: do diverse Σ_b profiles share a common μ_* once Δ(Σ_b) is factored out?

**Does not** derive SI μ_*; organizes radial/environment variation around an anchor.

---

## 3. Case B progress — explicit DE/DM endpoint derivation

### 3.1 Identification
\[
E_-=\omega_{\rm DM},\qquad E_+=\omega_{\rm DE},\qquad
\omega_*=\frac{\omega_{\rm DE}+\omega_{\rm DM}}{2},\qquad
\Delta=\frac{\omega_{\rm DE}-\omega_{\rm DM}}{2}.
\]

### 3.2 Bridge closure (structural, not pure-geometry)
Set the midpoint clock to the cosmological density scale:
\[
\omega_*=\sqrt{G\rho_\Lambda}.
\]
Numerically: ω_* ≈ 6.56×10^{-19} s^{-1} (H₀=70, Ω_Λ=0.7). Then
\[
a_{\rm eff}=\frac{c\,\omega_*}{Q}=\frac{c}{Q}\sqrt{G\rho_\Lambda}\approx 1.39\times 10^{-10}\ {\rm m\,s^{-2}},
\]
i.e. **Pathway 1 recovered** as the projection of the midpoint clock.

### 3.3 Stability for ω
\[
\frac{d\,\delta\omega}{dt}=-\gamma\,\delta\omega+\beta\,\Delta(t)^2,\quad\gamma>0.
\]
Late-time cosmology with small Δ → ω→ω_*. Epoch-dependent Δ (e.g. matter–DE transition) sources transient shifts without destroying the attractor.

### 3.4 What is still inserted
ω_*=√(Gρ_Λ) is the one dimensionful input. Case B explains *where it sits* (midpoint clock) and *how sectors split around it*; it does not derive ρ_Λ from cone angles.

---

## 4. Holographic entropy bounds — contact only

| Bound | Schematic |
|-------|-----------|
| Bekenstein | S ≤ 2π E R / (ℏ c) |
| Covariant (Bousso) | Entropy on light-sheets ≤ Area/(4ℓ_Pl²) |
| Causal / Hubble | Variants using H^{-1} as IR cutoff |

**Acceleration-scale contact:** c H₀ = c²/L_H ≈ 6.8×10^{-10} m s^{-2} (same order as √(Gρ)c scales). Holographic dark-energy constructions often set ρ_DE ~ M_Pl² H² or ~ M_Pl² L^{-2} with L an IR cutoff — another route to one dimensionful cosmological input.

**TAFA posture:** Bounds reinforce that IR cosmological scales can source acceleration-class numbers. They are **not** used here as a derivation of μ or of Pathway 1. No claim that cone geometry saturates a Bousso bound to fix a_eff.

---

## 5. Simultaneous status

| Item | Status |
|------|--------|
| Midpoint stability | Requires −γ δu + β Δ² form; raw α(u²+Δ²) not a finite attractor |
| Case A | μ_* anchor + Δ(Σ_b)^p deformation; empirical share-μ_* test defined |
| Case B | DE/DM endpoints; ω_*=√(Gρ_Λ) ⇒ Pathway 1; stability as above |
| Holographic bounds | Order-of-magnitude contact; not a TAFA theorem |
| No-go | Intact — one dimensionful input still required |
