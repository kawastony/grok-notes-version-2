# Staged cosmology test program — Tier 1 results

Tony Kawas / 20 September 2026.

**Principle:** pre-registered, frozen predictions vs standard datasets. No post-hoc retuning.

**Scope honesty:** Full χ² with DESI BAO covariances + Pantheon+ likelihood requires data vectors not loaded here. What is run: **orientation tests**, **kinematic predictions** (H(z), q(z), z_t), **bridge constants from cone notes**, and clear pass/fail against published DESI DR2 free-CPL centers.

---

## Frozen candidate points

| Label | w₀ | wₐ | Source |
|-------|-----|-----|--------|
| **geo_phi** | −φ/2 ≈ **−0.809017** | −1/φ ≈ **−0.618034** | Geometric DE (φ-locked); matches RSIT librarian arithmetic |
| paste_773 | −0.773 | −0.152 | Example values from test-design paste |
| paste_790 | −0.790 | −0.152 | Example values from test-design paste |
| LCDM | −1 | 0 | Reference |

**Important:** The lattice/micro repo (`grok-notes-version-2`) does **not** contain a forced derivation of (w₀, wₐ) from the Callias/Forman program. The geo_phi point is the cleanest frozen geometric candidate for orientation. Paste values are illustrative only until TAFA papers lock a forced pair.

DESI DR2 free-CPL centers (DESI Collaboration 2025, arXiv:2503.14738):

| Dataset combo | (w₀, wₐ) |
|---------------|----------|
| DESI+CMB+Pantheon+ | (−0.838 ± 0.055, −0.62⁺⁰·²²₋₀·₁₉) |
| DESI+CMB+Union3 | (−0.667 ± 0.088, −1.09⁺⁰·³¹₋₀·₂₇) |
| DESI+CMB+DESY5 | (−0.752 ± 0.057, −0.86⁺⁰·²³₋₀·₂₀) |

---

## Test 1 — Expansion history / w(z) orientation

### Euclidean distance in (w₀, wₐ) plane to DESI free-CPL centers

| Frozen | dist → Pantheon+ | dist → Union3 | dist → DESY5 |
|--------|------------------|---------------|--------------|
| **geo_phi** | **0.029** | 0.493 | 0.249 |
| paste_773 | 0.472 | 0.944 | 0.708 |
| paste_790 | 0.470 | 0.946 | 0.709 |
| LCDM | 0.641 | 1.140 | 0.895 |

### 1σ box vs DESI+CMB+Pantheon+

| Frozen | w₀ in 1σ? | wₐ in 1σ? |
|--------|-----------|-----------|
| **geo_phi** | **Yes** | **Yes** |
| paste_773 | No | No |
| paste_790 | Yes | No |

### Decision (orientation only)

- **geo_phi:** lies inside the DESI+CMB+Pantheon+ 1σ region and is the closest frozen point among candidates (d ≈ 0.03).  
- **paste_773 / paste_790:** far from all three DESI centers; fail orientation unless a different dataset/definition is pre-registered.  
- **Not a full χ² pass:** joint MCMC at fixed F has not been run (verification wall, not theory hole).

**Primary flagship result of this session:** geometric φ-locked DE is **compatible in orientation** with DESI DR2 + CMB + Pantheon+ free-CPL preference (w₀ > −1, wₐ < 0 quadrant).

---

## Test 2 — Transition redshift

Definition frozen here: **acceleration onset** where deceleration parameter q(z) = 0.

| Model | z_t (q=0), Ωₘ=0.31 | z_cross (w=−1) |
|-------|---------------------|----------------|
| geo_phi | **0.75** | **0.447** (=1/√5) |
| paste_773 | 0.65 | none (no phantom crossing) |
| paste_790 | 0.65 | none |
| LCDM | 0.645 | — |

Sensitivity (geo_phi): z_t ∈ [0.66, 0.84] for Ωₘ ∈ [0.28, 0.34].

### vs paste claim z_t ≈ 0.35

The paste’s “pause” z ≈ 0.35 is **not** the same as q(z)=0.  
- q=0 acceleration onset is ~0.65–0.75 for these models.  
- Phantom-crossing for geo_phi is at **0.447**.  
- A “pause” defined by H r_p = 1 needs the theory’s exact r_p,cosmo and is **not computed** without that map.

**Decision:**  
- If transition ≡ q=0 → geo_phi predicts ~0.75 (Om-dependent), consistent with usual reconstructed range ~0.6–0.8.  
- If transition ≡ paste 0.35 → **not supported** by q=0 definition; requires separate frozen definition and data metric.

---

## Test 3 — Growth / P(k) suppression

**Not executed.** Requires:
- frozen k_field / m_B3 → Jeans scale map,
- DESI full-shape or Lyα likelihood,
- baryonic-systematics control.

Status: **pre-registration only**. Do not claim pass/fail.

---

## Test 4 — Energy budget

With flat CPL, (Ωₘ₀, Ω_DE₀) are **inputs**, not outputs of (w₀, wₐ).  
True theory prediction of Ωₘ₀ from first principles is **not available** in the lattice notes.

**Decision:** cannot pass/fail without a forced Ωₘ₀ derivation. Using Planck/DESI Ωₘ as external prior is allowed for H(z) plots but is not a theory test of the budget.

---

## Test 5 — Galaxy–cosmology bridge

### 5A. R normalization (from cone notes — locked)

| Quantity | Value |
|----------|-------|
| R_cone = √6 / φ | **1.51387** |
| Historical target R | 1.5156 |
| Relative offset | **−0.11%** |

This is the cone-accounting identity already in `FINDINGS_cone_11_72_R.md`. It supports SPARC/BTFR amplitude bookkeeping. Full BTFR χ² not re-run in this session.

### 5B. r_p transition radius

Requires frozen cosmology→galaxy map. **Not executed** without that chain.

### Chirality / S/Z

Explicitly **out of scope** for this cosmology-first program (per test design).

---

## Master decision table

| Test | Prediction used | Dataset / metric | Result |
|------|-----------------|------------------|--------|
| 1. w(z) orientation | geo_phi (−0.809, −0.618) | DESI DR2 free-CPL centers | **Pass orientation** (inside P+ 1σ; d=0.029) |
| 1b. paste w(z) | (−0.77/−0.79, −0.152) | same | **Fail orientation** |
| 2. z_t (q=0) | geo_phi → ~0.75 | literature range ~0.6–0.8 | **Compatible** (definition-dependent) |
| 2b. z_t = 0.35 | paste pause | — | **Not supported** by q=0 |
| 3. P(k) | — | — | **Not run** |
| 4. Energy budget | — | — | **Not run** (no forced Ωₘ) |
| 5A. R_cone | √6/φ | historical R | **Pass** (0.11% offset) |
| 5B. r_p bridge | — | — | **Not run** |

---

## What would lock a real breakthrough

1. **Forced derivation** of (w₀, wₐ) from TAFA/cone spine (not only geometric φ analogy).  
2. Joint χ² at frozen F against DESI BAO + SN + CMB (public data vectors).  
3. Frozen definition of “transition” matching an observable.  
4. Forced Ωₘ₀ or H₀ from the same spine.  
5. Only then: cosmology→R or r_p bridge on SPARC with frozen coefficient.

Until (1)–(2), the strongest honest claim is:

> The geometric φ-locked CPL point (w₀, wₐ) = (−φ/2, −1/φ) lies inside the DESI DR2 + CMB + Pantheon+ 1σ free-CPL region and is far closer to that posterior than ΛCDM or the paste example points. Full likelihood at the frozen point remains a verification task.

---

## Relation to micro program

Lattice Forman / identity-propagation work does **not** yet supply w₀, wₐ, or Ωₘ. Scale-up remains architectural. Cosmology tests above use continuum/geometric bookkeeping, not soft-mode numerics.

---

## Compact statement

Tier-1 orientation: geometric DE (w₀, wₐ) = (−φ/2, −1/φ) passes DESI+CMB+Pantheon+ 1σ orientation; paste example points do not. Transition redshift depends on definition (q=0 ≈ 0.75 vs claimed pause 0.35). R_cone passes historical match. Growth, energy-budget prediction, and r_p bridge not yet executable without further forced inputs. Full χ² is the next verification wall.
