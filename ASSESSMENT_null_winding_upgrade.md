# Assessment of the null-upgrade memo + paper-safe rewrite

Tony Kawas / 19 September 2026.

## Verdict on the pasted assessment

**Agree.** The upgrade memo is a useful methodological recovery plan that overstates how completely it explains away the first null.

| Claim in upgrade memo | This assessment |
|-----------------------|-----------------|
| N=22 is underpowered for a subtle effect | **Keep** |
| 2D S/Z can dilute a 3D spin coupling | **Keep** |
| Pre-register, enlarge sample, better residuals | **Keep** |
| Null was **guaranteed** regardless of a real signal | **Trim** — too strong |
| Exact power table (9%, 18%, …) | **Illustrative only** |
| “Not a contradiction of the field theory” | **Rewrite** — little discriminating power ≠ insulation |
| Pause radius 12.1 kpc / compressive-tensile template | **Not used here** — theory-loaded post-null redesign |

Paper-safe core claim:

> The N=22 SPARC × 2D-winding null is not strong evidence against a chiral scale-up idea, because the test was likely underpowered and used a potentially lossy proxy (sky-projected S/Z) for 3D spin. It is also not evidence *for* the idea. A more informative follow-up increases sample size, uses 3D-disambiguated spins where possible, pre-registers the metric, and tests normalized radial residuals — without embedding extra theory knobs after the null.

---

## Pre-registration (written before splits below)

**Rule (frozen):** Υ_disk=0.5, Υ_bul=0.7, a_T=8.25e-11 m s−2, simple interpolator. No retune.

**Primary metric:** per-galaxy mean signed residual (V_obs−V_model)/max(V_obs,1).

**Secondary:** MAE (km/s); inner vs outer third of radial profile (same normalized residual).

**Splits:**
1. Iye 2019 Table-2-class catalog (S/Z + approaching + dark side) ∩ SPARC by normalized name — 3D-informed subsample.
2. Expanded 2D GZ/DESI match (sep ≤0.08°, Δp≥0.1) — larger, still lossy.
3. Combined: Iye overrides GZ when both exist.

**H0:** no difference between S and Z on primary metric (two-sided Mann–Whitney).

**Not used:** 12.1 kpc pause radius, compressive/tensile phase template, one-sided tests chosen after looking.

**Decision rule:** p<0.05 on pre-registered primary = detection candidate. Otherwise null. Small n still means low power; a second null is not a proof of zero effect, and not a confirmation of the theory.

---

## Runs

### A. Iye 2019 3D-informed ∩ SPARC

Catalog: figure8 of Iye+2019 (150 galaxies with S/Z, dark side, approaching side).
Overlap by name: **18 SPARC galaxies** (Z=8, S=10).

| Metric | p (Z vs S) | Δmedian (Z−S) |
|--------|------------|----------------|
| MAE | 0.63 | −0.72 km/s |
| mean normalized residual | 0.76 | −0.010 |
| inner third nrm | 0.46 | +0.004 |
| outer third nrm | 0.97 | −0.020 |

**Result: null.** 3D labels did not produce a detection. n=18 remains small.

### B. Expanded 2D GZ/DESI match

Labeled SPARC: **41** (Z=23, S=18) vs original 22.

| Metric | p | Δmedian (Z−S) |
|--------|---|----------------|
| MAE | 0.095 | −3.62 km/s |
| mean nrm | 0.52 | −0.064 |
| inner nrm | 0.84 | −0.059 |
| outer nrm | 0.12 | −0.081 |

**Result: null** (MAE closest, still p>0.05). Directionally Z slightly lower MAE; not claimed.

### C. Combined (Iye overrides GZ)

**n=56** (Z=29, S=27), of which 18 Iye-3D.

| Metric | p | Δmedian (Z−S) |
|--------|---|----------------|
| MAE | 0.16 | −2.76 km/s |
| mean nrm | 0.44 | −0.046 |
| inner nrm | 0.84 | −0.068 |
| outer nrm | 0.071 | −0.080 |

**Result: null.** Outer-profile p=0.071 is the nearest miss — **not** a detection, not to be promoted after looking.

---

## How to read these nulls (paper-safe)

1. The first N=22 test was likely underpowered; that is fair.
2. A stronger design (3D catalog overlap + ~2.5× 2D sample + normalized/radial metrics) **still returns null**.
3. That still does **not** prove the chiral template is false (Iye overlap is only 18; SPARC∩GZ is still a biased local/high-z mix).
4. It **does** mean: with the observables we can actually build today, no S/Z residual split is seen. The theory is not insulated, and the null is not “guaranteed away.”

## What we did *not* do

- Did not retune a_T or Υ after seeing p-values.
- Did not insert r_p=12.1 kpc.
- Did not treat p=0.07 outer residual as a hint to chase.

## Next that would actually add power

- Iye–Sugai 8287 southern spins ∩ any RC sample with baryonic decompositions (not SPARC-only).
- Independent 3D (dust + approaching) for more than 18 SPARC galaxies.
- Pre-register effect size δ and stop if still null at that n.
