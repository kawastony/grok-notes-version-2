# Amplitude prediction from action / cone scales

**Goal:** replace the unit choice a_*=10^{-10} m s^{-2} by a derived scale so that
\[
a_{\rm eff}(\Sigma_{\rm med})\approx Q\,a_*
\]
becomes a prediction.

---

## 1. Framework asymptotic (Paper 25)

\[
v_\infty \approx \bigl(\Lambda_*^2\, G\, M\, \mu\bigr)^{1/4}
\]

Equivalent BTFR form:
\[
V^4 = G M\, a_{\rm eff}\quad\text{with}\quad a_{\rm eff}=\Lambda_*^2\,\mu.
\]

So the absolute acceleration is the product of two framework parameters:
- Λ_* — geometric/tension scale
- μ — pause / crossover scale (r_p = 1/μ)

**Status (Paper 25):** framework-level; “precise numerical values not all fixed by base geometry alone.” Micro-derivation of μ open.

---

## 2. Candidate derived a_* (cosmology–geometry bridges)

Using H_0=70 km/s/Mpc, Ω_Λ=0.7, standard constants:

| Candidate | Formula | Value (m s^{-2}) | vs a_eff(med)=1.41e-10 |
|-----------|---------|------------------|-------------------------|
| c H_0 | c H_0 | 6.80×10^{-10} | 0.21× |
| Q c H_0 | √2 c H_0 | 9.62×10^{-10} | 0.15× |
| √(G ρ_Λ) c | √(G ρ_Λ) c | **1.97×10^{-10}** | **0.72×** |
| G ρ_Λ R_H | G ρ_Λ (c/H_0) | 5.68×10^{-11} | 2.5× |
| R_cone G ρ_Λ R_H | R_cone×G ρ_Λ R_H | 8.60×10^{-11} | 1.6× |
| Q × 10^{-10} | unit×Q | 1.41×10^{-10} | **1.00×** |
| R_cone × a_0 | R_cone×1.2e-10 | 1.82×10^{-10} | 0.77× |

**Closest natural bridge without a hand unit:** √(G ρ_Λ) c ≈ 1.97×10^{-10} (~30% high vs 1.41×10^{-10}).

With R_cone:
\[
R_{\rm cone}\sqrt{G\rho_\Lambda}\,c \approx 2.98\times 10^{-10}
\]
(too high). With a fitted O(1):
\[
a_{\rm eff}\stackrel{?}{=}\frac{Q}{\varphi}\sqrt{G\rho_\Lambda}\,c
\approx 1.22\times 10^{-10}
\]
(~13% low). These are **coincidence-level bridges**, not action variations.

---

## 3. Attempted action-level chain

Desired:
\[
\text{TAFA action}
\;\to\;
(\Lambda_*,\mu)
\;\to\;
a_{\rm eff}=\Lambda_*^2\mu
\;\to\;
A\sqrt{2\kappa_0}=a_{\rm eff}(\Sigma_{\rm ref}).
\]

| Step | Status |
|------|--------|
| v_∞=(Λ_*^2 G M μ)^{1/4} written | Yes (Paper 25) |
| Λ_* from cone tension / junction action | Toy instanton in Paper 13; not fixed to SPARC |
| μ from pause / r_p=1/μ | Structural; micro open |
| Λ_*^2 μ = Q×10^{-10} | **Not derived** |
| Parent action → numbers | **Open** |

Paper 13 constructs a Euclidean cone-junction action for a light modulus (S_cone~60–70) — hierarchy for eV-scale fields, not the absolute galactic a_eff.

---

## 4. SPARC cone action scales (inventory)

| Scale | Role | Fixed by |
|-------|------|----------|
| κ_0=0.394 | geometric stiffness | earlier TAFA geometry |
| Q=√2 | cone-sector matching | Paper 14 |
| C_ang≈1.417 | angular packing | κ_0, ψ_1, ψ_2 |
| Σ_ref (log10=8.667) | pivot surface density | Paper 24 convention |
| A | overall normalization | fit / matching |
| γ | structure response | data + operator chain |
| a_eff(med)≃1.41×10^{-10} | absolute scale | data readout |
| Λ_*, μ | asymptotic product | framework; open |
| R_cone=√6/φ | micro cone amplitude | activation surface |

**What SPARC fixes:** A (or a_eff at median) and γ.  
**What cone geometry fixes without SPARC:** Q, κ_0, C_ang, R_cone, angles, ν_0.  
**What is still free / open:** absolute product Λ_*^2 μ.

---

## 5. Honest prediction status

**Cannot yet claim:** a_*=10^{-10} is derived from the action.

**Can claim:**
1. Relative amplitude: a_eff(Σ)/a_eff(Σ_ref)=(Σ/Σ_ref)^γ with γ from operator chain (compatible with data).
2. Angular/Q factor: fixed geometrically; Q×(hand unit) matches median a_eff numerically.
3. Cosmological coincidence: √(G ρ_Λ) c is within ~30% of a_eff(med) — same order as MOND’s a_0~cH_0 coincidence; not a derivation.

**Working law (unchanged):**
\[
a_{\rm eff}=A\sqrt{2\kappa_0}\Bigl(\frac{\Sigma_b}{\Sigma_{\rm ref}}\Bigr)^{1/7},
\qquad
A\ \text{set by}\ a_{\rm eff}(\Sigma_{\rm med})\approx 1.41\times 10^{-10}.
\]
Identify {Q, C_ang, R_cone} as one geometric family for the O(1) factor inside A, without multiplying them.

---

## 6. What would close the absolute scale

One of:
1. Derive μ and Λ_* from the cone action (junction tension + pause condition) with no SPARC input, then check Λ_*^2 μ ≈ 1.41×10^{-10}.
2. Derive a_eff = α √(G ρ_Λ) c with α fixed by Q, φ, or R_cone only, then test α against SPARC median.
3. Show the hand unit 10^{-10} equals a specified combination of c, H_0, G, ρ_Λ and geometric factors uniquely.

Until then, absolute amplitude remains **calibrated**, relative structure dependence is **tested**.
