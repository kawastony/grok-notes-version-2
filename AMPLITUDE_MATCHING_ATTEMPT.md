# Amplitude matching attempt: R_cone, Q, κ₀, a_eff

## Fixed geometric numbers

| Symbol | Value |
|--------|-------|
| φ | 1.618034 |
| R_cone = √6/φ | 1.513868 |
| κ₀ | 0.394 |
| √(2κ₀) | 0.887694 |
| Q = √2 | 1.414214 |
| C_ang = √(κ₀/(sin35° cos70°)) | 1.417185 ≈ Q |
| a_eff(median Σ_b) | ≃ 1.41×10^{-10} m s^{-2} |

Note: C_ang / Q ≈ 1.002 — angular packing and Q are essentially the same O(1) factor.

---

## Preferred Paper 24 form at Σ_b = Σ_ref

\[
a_{\rm eff}=A\sqrt{2\kappa_0}
\quad\Rightarrow\quad
A = \frac{a_{\rm eff}}{\sqrt{2\kappa_0}}\approx 1.588\times 10^{-10}\ {\rm m\,s^{-2}}
\]
(if the power term is 1 at reference).

---

## Candidate identifications (dimensionless geometry × 10^{-10} m s^{-2})

| Candidate for a_eff(median) | Value | Ratio to 1.41×10^{-10} |
|-----------------------------|-------|-------------------------|
| Q × 10^{-10} | 1.414×10^{-10} | **0.997** |
| C_ang × 10^{-10} | 1.417×10^{-10} | **0.995** |
| R_cone × 10^{-10} | 1.514×10^{-10} | 0.931 |
| φ × 10^{-10} | 1.618×10^{-10} | 0.871 |
| √(2κ₀) × 10^{-10} | 0.888×10^{-10} | 1.588 |

**Best numerical contact:**
\[
a_{\rm eff}(\Sigma_{\rm med}) \approx Q\times 10^{-10}\ {\rm m\,s^{-2}}
\]
to ~0.3%. Same with C_ang.

---

## Matching propositions (ranked)

### P1 — Q sets the median scale (strongest numerics)
\[
a_{\rm eff}(\Sigma_{\rm med}) = Q\,a_\ast,\qquad a_\ast = 10^{-10}\ {\rm m\,s^{-2}}
\]
Then A = Q a_*/√(2κ₀) ≈ 1.59×10^{-10}, and R_cone is **not** an extra multiplier.

**Caveat:** a_* = 10^{-10} is a convenient SI unit, not derived from the cone action. Numerically excellent; theoretically a unit choice.

### P2 — R_cone as the same O(1) factor
\[
R_{\rm cone} \stackrel{?}{\sim} Q\quad\text{or}\quad R_{\rm cone}/Q \approx 1.07
\]
Within ~7%. Could absorb into Σ_ref choice or weak γ correction. Treat as **one** geometric amplitude family {Q, C_ang, R_cone}, not a product.

### P3 — Fail condition
If a model writes
\[
a_{\rm eff}\propto R_{\rm cone}\times Q\times\sqrt{2\kappa_0}\times\cdots
\]
without deriving independence, it double-counts. **Rejected** by bookkeeping rule.

---

## Working amplitude law (post-attempt)

\[
\boxed{
a_{\rm eff}=A\sqrt{2\kappa_0}\,\Bigl(\frac{\Sigma_b}{\Sigma_{\rm ref}}\Bigr)^{1/7}
\quad\text{with }A\text{ fixed by }a_{\rm eff}(\Sigma_{\rm med})\approx Q\times 10^{-10}
}
\]

R_cone remains the micro-cone expression for the same O(1) geometric content as Q/C_ang — **identified**, not multiplied.

---

## Status

| Claim | Status |
|-------|--------|
| Q×10^{-10} ≈ a_eff(median) | Numerical match ~0.3% |
| C_ang ≈ Q | Numerical identity |
| R_cone ≈ Q (within 7%) | Same family |
| a_* = 10^{-10} derived | **Not derived** — unit |
| Product R_cone×Q×√(2κ₀) | **Forbidden** (double-count) |
