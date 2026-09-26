# μ — derivation or no-go

**Purpose:** Pin the choke point in \(a_{\rm eff}=\Lambda_*^2\mu\).  
**Rule:** No new amplitude formulas. No DE branch. Define, test, pass/fail.

---

## 1. Exact operational definition (from Papers 24–25)

### 1.1 Framework role

Paper 25 asymptotic relation:
\[
v_\infty \approx \bigl(\Lambda_*^2\, G\, M\, \mu\bigr)^{1/4}
\quad\Longleftrightarrow\quad
a_{\rm eff} = \Lambda_*^2\,\mu.
\]

So **μ** is the factor that, together with the tension-like scale Λ_*, produces the absolute acceleration in the BTFR.

### 1.2 Pause / crossover scale

Paper 25:
\[
r_p = \frac{1}{\mu}
\]
interpreted as a **pause or crossover scale** between compressive and tensile regimes on the cone sector.

**Operational reading:**
- μ has dimensions of **inverse length** (or inverse time / c, depending on convention).
- r_p is the radial (or angular×radius) location where the cone response changes regime.
- In galactic language, r_p is a characteristic transition radius; in pure geometry, it is the inverse of a junction eigenvalue or mass gap.

### 1.3 What μ is *not*

- Not γ (structure exponent).
- Not Q, κ₀, R_cone (O(1) geometric factors in the amplitude family).
- Not A (the fitted normalization in Paper 24).
- Not ν₀ (that is Δ_μ of the transmission operator, dimensionless spectral weight).

ν₀ and μ are different objects: ν₀ enters γ; μ enters the absolute product Λ_*^2 μ.

---

## 2. Units

| Convention | [μ] | [Λ_*] | [Λ_*^2 μ] |
|------------|-----|-------|-----------|
| SI, a_eff in m s^{-2} | s^{-1} or m^{-1}×c | depends | m s^{-2} |
| Natural (ħ=c=1) | mass | mass^{1/2} or as defined | mass² |
| Geometric only | 1/length | — | needs second scale |

**Point:** Geometry alone (angles, Q, ν₀, R_cone dimensionless or pure numbers) **cannot** produce an SI acceleration without one dimensionful input (Λ_*, μ, H_0, ρ_Λ, or compactification scale).

---

## 3. Candidate origins in cone / junction geometry

### C1 — Inverse junction length
\[
\mu \stackrel{?}{=} \frac{\nu_0}{R_{\rm junc}}
\]
where R_junc is a physical radius of the cone junction (galactic or micro).

- **Pros:** Uses verified ν₀; inverse-length units automatic.
- **Cons:** R_junc is not fixed by angles alone; choosing it as 12.1 kpc (or similar) reimports observation.

### C2 — Pause as Legendre / regime boundary
μ marks the compressive↔tensile switch at fixed angles (35°/70°).

- **Pros:** Tied to same sector as ν₀.
- **Cons:** Angles are dimensionless; still need a metric scale to convert to 1/length.

### C3 — Soft-mode / defect mass gap
\[
\mu \stackrel{?}{=} m_{\rm soft}\ \text{or}\ \frac{m_0}{L_{\rm soft}}
\]
from Wilson–Dirac / hedgehog lattice sector.

- **Pros:** Concrete lattice observable (eigenvalue gap).
- **Cons:** Lattice units must be matched to SI; continuum limit of that match is open.

### C4 — Domain-wall thickness
\[
\mu \stackrel{?}{=} 1/\delta
\]
with δ the 5D wall thickness or warp skin.

- **Pros:** Standard in warped constructions.
- **Cons:** δ usually set by UV/compactification scale — another name for an external scale.

---

## 4. Candidate origins in parent action

### A1 — Coefficient in L_def after reduction
μ as mass parameter for X or Y in
\[
\mathcal{L}_{\rm def}=\tfrac12(\partial X)^2+\tfrac12(\partial Y)^2+\cdots+\tfrac12 m^2 X^2
\]
with m∼μ.

- Requires parent action → L_def reduction with a computable mass.

### A2 — Junction tension vs pause product
Λ_* from wall tension (∫ e^{2A} or cone-junction Euclidean action); μ from IR gap; product checked against 1.41×10^{-10} m s^{-2}.

- Paper 13 has toy Euclidean S_cone for a light modulus, not a fixed μ for galaxies.

### A3 — No pure-action μ (no-go branch)
If every definition of μ requires an external length (kpc, H_0^{-1}, compactification radius), then **absolute scale cannot be closed inside pure cone geometry** and must take **one** dimensionful input (e.g. ρ_Λ via Pathway 1, or r_p from data).

---

## 5. Can μ be derived without SPARC?

| Route | SPARC-free? | Status |
|-------|-------------|--------|
| Angles + ν₀ only | Dimensionless only | **No SI μ** |
| ν₀ / R_junc with R_junc from cosmology (H_0, ρ_Λ) | Yes, but external scale | Bridge, not pure action |
| Lattice m_soft with lattice spacing fixed by theory | Only if spacing derived | Open |
| 5D δ from warp parameters only | Only if all warp scales derived | Open |
| Fit r_p from rotation curves | **No** — SPARC input | Calibration |

**Working conclusion:**  
Under the **current** written framework, μ is **not** derived as an SI number from geometry alone. A SPARC-free μ requires either (i) an external cosmological length/density or (ii) a completed UV/lattice matching that does not yet exist in the papers.

---

## 6. Pass / fail criteria

### PASS (derivation)
1. Write μ = explicit functional of cone action parameters (no SPARC, no hand kpc).
2. Units: inverse length or inverse time, consistent with a_eff=Λ_*^2 μ.
3. Product Λ_*^2 μ predicts a_eff(median) to within ~10% of 1.41×10^{-10} m s^{-2} **or** predicts a clean cosmological bridge (e.g. 1/Q √(Gρ_Λ)c) with fixed geometric prefactor.
4. No retuning of Q, κ₀, γ to save the product.

### FAIL (no-go on pure geometry)
1. Every candidate μ still contains one free length.
2. Setting that length from SPARC is the only way to hit 1.41×10^{-10}.
3. Then the honest boundary is:

> **Absolute galactic acceleration requires one external dimensionful input; relative structure dependence (γ, Q, Σ_b law) does not.**

### Conditional PASS (bridge)
μ (or Λ_*^2 μ) identified with a cosmological combination involving ρ_Λ or H_0 and **only** locked geometric factors (Q, R_cone, …). Pathway 1 is this class:
\[
a_{\rm eff}\stackrel{?}{=}\frac{1}{Q}\sqrt{G\rho_\Lambda}\,c.
\]
Allowed as a **candidate normalization principle**, not as pure-action closure.

---

## 7. Immediate decision matrix

| Choice | Action |
|--------|--------|
| Pursue pure μ from junction | Need explicit R_junc or mass gap from action — not available now → **blocked** |
| Accept one external scale | Formalize Pathway 1 (or H_0-bridge) as candidate; keep μ as r_p^{-1} structural |
| Declare no-go | Freeze: absolute A calibrated; relative law tested; μ not SI-derived from cone alone |

**Recommended freeze until new action content exists:**

\[
\boxed{
\mu\ \text{is the pause/crossover inverse scale in }a_{\rm eff}=\Lambda_*^2\mu;
\text{ SI value not derived from geometry alone; absolute amplitude calibrated or bridged.}
}
\]

---

## 8. One-sentence result

**μ is defined as the pause factor in a_eff=Λ_*^2 μ (inverse length); it is not yet derived in SI units from cone geometry without an external scale — that is a no-go on pure geometry, not a failure of the relative Σ_b / operator spine.**
