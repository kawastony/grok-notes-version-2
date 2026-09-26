# Robust r_p search for non-circular SPARC intercept test

## Problem diagnosed
Naive max |d ln R / d ln r| often locks onto the **outer data edge** when the true crossover lies near or beyond R_max. A candidate local scale ~10–15 kpc makes this common for compact disks.

## Robust rules (implemented in synthetic re-test)
1. **Interior window only:** search in [0.1 R_max, 0.85 R_max] — reject outer 15%.
2. **Require R rise:** max R ≳ 1.05 × min R in the window; else mark invalid / censored.
3. **Prefer positive slope peaks** (R increasing outward); fallback to abs-slope only if needed.
4. **Coverage stratification (design, not proof):**
   - Primary / coverage-safe: R_max above a pre-chosen cut (e.g. 18 kpc) justified as “large enough to capture turnover,” **not** as proof of any specific 12.1 kpc anchor.
   - Coverage-limited: no local r_p claim; censored or secondary analysis only.

## Synthetic re-test outcome
- Edge hits reduced vs first skeleton (no automatic r_p = R_max).
- Intercept recovery still **poor** under this synthetic boost shape (linregress intercept not near planted 0.1).
- Conclusion: robust search is **necessary but not sufficient**. Need better transition definition (curvature, threshold on R, or parametric transition) and hierarchical stats before real SPARC.

## Use of ~12 kpc-class scale
- **Allowed now:** estimator-design constraint and sample stratification (why short disks fail local derivative search).
- **Not allowed yet:** hard-code 12.1 kpc into the cut and then claim the data recovered 12.1 kpc (selection circularity).
- **Later:** after estimator stabilizes, compare recovered μ_* to any independent benchmark (including 1/12.1 kpc if motivated from framework).

## Fallback for short disks
Do **not** adopt an unmotivated global form R(r)=1+S(Σ_b/Σ_ref)^{1/7} μ_* r as official. Prefer: mark censored, or use an agnostic parametric transition family in secondary analyses only.
