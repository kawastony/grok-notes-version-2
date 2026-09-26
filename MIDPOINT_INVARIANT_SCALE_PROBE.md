# Midpoint-invariant scale probe

**Role:** Discovery / mapping tool — same class of mechanism used microscopically to identify phases and bridge types.  
**Not claimed:** automatic solution of the absolute-scale no-go.

Canonical freeze unchanged: relative structure stronger; absolute scale calibrated or Pathway-1 bridged; pure-geometry μ open.

---

## 1. Abstract structure

Endpoints controlled by a deformation parameter λ:
\[
E_-(\lambda),\quad E_+(\lambda).
\]

Midpoint and half-separation:
\[
M(\lambda)=\frac{E_++E_-}{2},\qquad
\Delta(\lambda)=\frac{E_+-E_-}{2},
\qquad
E_\pm = M \pm \Delta.
\]

**Invariant-midpoint condition:**
\[
M(\lambda)=u_*\quad\text{independent of }\lambda.
\]
Endpoints may separate or approach; the center stays fixed. That is stronger than ordinary averaging — it marks a protected anchor.

Quadratic identity:
\[
\frac{E_+^2+E_-^2}{2}=u_*^2+\Delta^2.
\]

Candidate dynamical law:
\[
\left.\frac{du}{d\xi}\right|_{\xi=\xi_*}
= \alpha\,\frac{E_+^2+E_-^2}{2}
= \alpha\bigl(u_*^2+\Delta^2\bigr).
\]

---

## 2. Dimensional filter (make-or-break)

\([u/d\xi]=U/X\), \([u^2]=U^2\). Matching requires either:
- \(U=1/X\) with α dimensionless, or
- α carrying units \(1/(U X)\).

**Safe cases (α can be dimensionless):**

| u | ξ | [du/dξ] | [u²] |
|---|---|---------|------|
| μ (inverse length) | r (length) | L⁻² | L⁻² |
| ω_c (inverse time) | t (time) | T⁻² | T⁻² |

**Unsafe without smuggling scale:** both u and ξ dimensionless → no new SI units; α would carry the entire scale (fails as scale-solver; may still organize correlations).

---

## 3. Case A — u = μ (pause inverse length)

**Filled ansatz**

| Item | Choice |
|------|--------|
| u | μ (pause / crossover inverse length) |
| [u] | L⁻¹ |
| E₋, E₊ | inner-regime scale, outer-regime scale (or compressive / tensile branch readouts) |
| λ | e.g. Σ_b, boost parameter, or sector separation |
| M(λ)=μ_* | invariant under endpoint deformation |
| ξ | r (galactic / cone radial coordinate) |
| Law | \(\left.d\mu/dr\right|_*=\alpha(\mu_*^2+\Delta^2)\) |
| [α] | dimensionless |

**Success criteria**
- μ_* identified with a stable crossover (not fit freely from SPARC alone).
- Endpoint pair correlates with known regime split (baryonic vs effective, or cone compressive vs tensile).
- Does **not** by itself invent SI units if μ_* is still inserted; can reframe μ as flow of a deeper midpoint field.

**Link to microscopic use:** same pattern as identifying soft-mode phases / bridge types by holding a topological or chirality midpoint fixed while defect endpoints deform.

---

## 4. Case B — u = ω_c (cosmic clock frequency)

**Filled ansatz**

| Item | Choice |
|------|--------|
| u | ω_c |
| [u] | T⁻¹ |
| E₋, E₊ | e.g. early-time / late-time clock rates, or DE/DM sector rates |
| λ | scale factor a, or redshift, or cosmic-time label |
| M=ω_* | invariant midpoint frequency |
| ξ | t |
| Law | \(\left.d\omega_c/dt\right|_*=\alpha(\omega_*^2+\Delta^2)\) |
| [α] | dimensionless |

**Bridge to acceleration (provisional):**
\[
a_{\rm eff}\;\stackrel{?}{\sim}\;\frac{c\,\omega_*}{Q}
\quad\text{or}\quad
\frac{c\,\omega_*}{\varphi}.
\]
Dimensionally consistent (c×T⁻¹ → L/T²). Numerically, if ω_* ~ H_0-class, recovers Pathway-1 order after geometric O(1) factors — **reparameterization of the bridge**, not a pure-geometry derivation.

---

## 5. What this inherits from the microscopic mechanism

Microscopically, midpoint-style invariants helped:
- separate phase types (soft-mode sectors, hedgehog vs anti-hedgehog),
- classify bridges (static G12 response vs topological charge conservation),
- hold topology/chirality fixed while transport endpoints moved.

**Here the same logic is applied at scale level:** hold u_* fixed; let regime endpoints move; read structure from Δ and from du/dξ. That is organizational power. Units still come from the choice that u is inverse length or inverse time.

---

## 6. Pass / fail against the no-go

| Outcome | Meaning |
|---------|--------|
| u dimensionless, ξ dimensionless | Organizes correlations only; **does not** solve absolute scale |
| u=μ or ω_c with physical ξ | Dimensions close; may **reveal** where the scale sits; still needs one input to fix SI size |
| Predicts dimensionless prefactor of Pathway 1 | Useful (bridge cleanup) |
| Predicts μ_* from pure angles alone | Would challenge the no-go — requires explicit construction |

---

## 7. Immediate worksheet (to fill with data / lattice / SPARC)

1. Choose Case A or B.  
2. Name concrete E₋, E₊ from existing observables (lattice soft eigenvalues, Σ_b bins, H(z) proxies, …).  
3. Check whether M(λ) is approximately constant across λ.  
4. Fit α; test residual structure.  
5. Report whether SI scale is generated or only redistributed.

---

## One-line status

**Enabler tool** (as in microscopic phase/bridge identification): midpoint invariance can expose hidden anchors and regime splits. Absolute SI scale still requires at least one dimensionful input unless a future construction derives u_* from pure geometry alone.
