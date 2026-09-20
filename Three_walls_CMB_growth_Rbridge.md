# Three walls in parallel: CMB, growth, galaxy bridge

Tony Kawas / 20 September 2026.

---

## Wall 1 — Official DESI joint + full CMB anchoring

### Done so far
- Stage 2 used DESI DR1 summary BAO with published bin correlations + Pantheon+ STAT+SYS + **approximate** Planck (R, ℓ_A) prior.
- Frozen φ remained preferred (Δχ² ≈ −3 to −4 vs ΛCDM).

### Not yet done (requires external pipeline)
| Item | Status |
|------|--------|
| Full DESI joint BAO covariance (all tracers + Lyα) | **Not loaded** — needs DESI VAC / Cobaya bao_data |
| Full Planck likelihood (or validated CPL distance-prior cov from Chen+2019 exact matrix) | **Not run** |
| Identical nuisance handling across models | Partial |

**Verdict:** Background indication is robust under our approximations; **official joint posterior remains a verification wall**, not a theory hole. Must be run in Cobaya/CLASS or equivalent before any published claim.

---

## Wall 2 — Growth / perturbations

### Linear growth ODE (GR + effective fluid, no PPF)
Integrated
\[
\frac{d^2 D}{da^2}+\left(\frac{3}{a}+\frac{d\ln H}{da}\right)\frac{dD}{da}-\frac{3}{2}\frac{\Omega_m(a)}{a^2}D=0
\]
for frozen φ vs ΛCDM at Ω_m=0.30.

| z | f_ΛCDM | f_φ | f_φ/f_Λ |
|---|--------|-----|---------|
| 0.00 | 0.513 | 0.511 | 0.997 |
| 0.38 | 0.705 | 0.687 | 0.975 |
| 0.61 | 0.784 | 0.770 | 0.983 |
| 1.00 | 0.869 | 0.866 | 0.996 |

**Result:** Linear growth rate differs by **≲ 2.5%** from ΛCDM across the observed range when σ₈ is fixed today. fσ₈(z=0) ≈ 0.414 (φ) vs 0.415 (ΛCDM) for σ₈=0.81 — well within current fσ₈ error bars.

### Caveats (critical)
1. This assumes **GR + smooth effective fluid** (no extra DE clustering).
2. Phantom crossing is **not** handled with PPF or quintom — the ODE is formal across w=−1.
3. Full test requires: Boltzmann code + PPF (or micro completion) + fσ₈ likelihood + weak lensing.

**Verdict:** At pure linear GR-fluid level, growth is **compatible** with ΛCDM to ~2%. This is **encouraging but not a pass** of the perturbation wall. Instability risk at the crossing remains open.

---

## Wall 3 — Galaxy bridge R_cone

### Prediction
\[
R_{\rm cone}=\frac{\sqrt6}{\varphi}\approx1.51387
\]
Historical quoted value ≈ 1.5156 → fractional difference **0.11%** (bookkeeping, not tension).

### Bridge form (from notes)
\[
v_\infty^4 = G\,R\,m_1^2\,M_{\rm bar}
\]
or equivalently a rescaling of the deep-regime acceleration scale:
\[
a_{\rm eff}=R\,a_0 \quad(\text{if written as }V^4=G a_{\rm eff} M_{\rm bar}).
\]
With a₀≈1.2×10⁻¹⁰ m s⁻² → R a₀ ≈ 1.82×10⁻¹⁰ m s⁻².

### Status
| Item | Status |
|------|--------|
| Geometric value locked | **Yes** |
| Explicit SPARC/BTFR fit with this R | **Not yet run in this session** |
| Empirical BTFR slope (SPARC literature) | ~3.5–4 (depends on Υ*, estimator) |

**Verdict:** Prediction is **ready and sharp**. Confirmation requires a controlled SPARC Q=1 BTFR residual test with R fixed (not refit). Cosmology success does **not** substitute for that test.

---

## Combined status board

| Wall | Result this pass | Still required |
|------|------------------|----------------|
| 1. Official SN+BAO+CMB | Approximate Stage 2 holds | Cobaya/CLASS joint |
| 2. Growth | Linear f within ~2% of ΛCDM | PPF + fσ₈ likelihood |
| 3. R galaxy bridge | R_cone locked; formula clear | SPARC residual fit |

---

## Compact statement

1. **CMB/DESI:** Official joint pipeline not yet run; Stage-2 approximate results remain favorable to frozen φ.  
2. **Growth:** Linear GR-fluid growth for frozen φ differs from ΛCDM by ≲2.5% in f(z); compatible with current fσ₈ precision, but phantom-crossing stability is unresolved.  
3. **Galaxy bridge:** R_cone=√6/φ≈1.51387 is locked and differs by 0.11% from the historical 1.5156; SPARC confirmation is the outstanding empirical step.

All three walls advanced; none is fully closed. Highest-impact next actions: (a) Cobaya joint posterior at frozen F, (b) PPF growth run, (c) SPARC BTFR with fixed R_cone.
