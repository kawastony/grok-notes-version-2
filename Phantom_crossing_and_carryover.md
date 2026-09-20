# Phantom crossing implications + galaxy carryover map

Tony Kawas / 20 September 2026.

---

## 1. Phantom crossing of the frozen-φ CPL point

### Arithmetic (exact)
\[
w(z)=w_0+w_a\frac{z}{1+z},\quad
w_0=-\varphi/2,\quad w_a=-1/\varphi
\]
\[
w=-1 \quad\Longleftrightarrow\quad z_c=\frac{1}{\sqrt5}\approx0.447214
\]

| z | w(z) | q(z) (Ωₘ=0.30) | phase |
|---|------|----------------|-------|
| 0 | −0.809 | −0.35 | quintessence-like (w>−1) |
| 0.447 | **−1** | −0.19 | **crossing** |
| 0.78 | −1.08 | ≈0 | acceleration onset (q=0) |
| ∞ | −1.427 | — | phantom-like early |

Direction of crossing (early→late):
**phantom (w<−1) → quintessence (w>−1)**.

This matches the direction preferred by DESI free-CPL analyses (early phantom → late quintessence).

---

## 2. Physical implications

### A. Background: safe
- f_DE(z=1089) ∼ 10⁻³, Ω_DE(z_*) ∼ 10⁻¹² → negligible early DE; CMB distance priors not spoiled by early DE density.
- Acceleration onset z_t(q=0)≈0.78 at Ωₘ∼0.30 is in the usual observational band.

### B. Perturbations: the real risk
Single-field quintessence **cannot** cross w=−1 smoothly without pathology.
Standard issues when w crosses −1:
- gradient instability / wrong-sign spatial kinetic term (for w<−1 regions)
- possible ghost modes
- adiabatic sound speed issues near the divide

**How the literature handles it:**
1. **Parametrized post-Friedmann (PPF)** — Hu & Sawicki style: phenomenological matching across the divide; used in many DESI/Planck CPL analyses.
2. **Quintom** (two fields) — one quintessence + one phantom; can cross stably with c_s²=1 for each field.
3. **Dissipative / interacting DE** — effective crossing without true phantom kinetic term.
4. **Effective fluid + PPF** — treat CPL as background only; freeze DE perturbations or use PPF when |w+1| small.

**Implication for TAFA / frozen-φ:**
- As a **background geometry prediction**, the crossing is fine and DESI-aligned.
- As a **fundamental single-field micro model**, it is **not yet justified** — needs either:
  - an explicit multi-field / quintom realization from the cone/chirality structure, or
  - an effective-fluid + PPF treatment with a clear statement that micro derivation is incomplete.

This is the **next genuine theoretical wall**, distinct from data walls.

### C. Observational sharpness
z_c=1/√5 is a **falsifiable timing prediction**:
- Independent of Ωₘ (unlike z_t).
- Can be tested with reconstruction of w(z) once DESI DR2/DR3 + SN precision improves.
- If reconstructed crossing is far from ∼0.45, the geometric lock is strained.

---

## 3. Confidence scores (agree with assessment)

| Sector | Score | Rationale |
|--------|-------|-----------|
| Identity | **74%** | Survives Stage 1–2D; clear lead vs paste |
| Propagation | **68%** | Signal persists through systematics |
| Unification | **43%** | Cosmology pillar stronger; micro↔galaxy bridge still incomplete |

---

## 4. Carryover to the galaxy paper

### What *does* strengthen

| Claim type | Carryover strength |
|------------|--------------------|
| Shared geometric constants (φ, R_cone≈√6/φ) | **Moderate–strong** if mapping is explicit |
| Shared activation / pause structure | **Moderate** (architectural) |
| Framework credibility as a whole | **Strong** |
| Motivation to test galaxy bridge carefully | **Strong** |

### What does *not* automatically strengthen

| Claim type | Carryover |
|------------|-----------|
| SPARC residual handedness / S–Z asymmetry | **None** (separate empirical test) |
| Chirality-labeled galaxy subsets | **None** |
| Local residual null tests already performed | **None** — nulls remain nulls |
| BTFR amplitude via R without explicit derivation + SPARC test | **Weak** until bridge is run |

### Fair paper wording

> The success of the frozen-φ cosmology tests strengthens the credibility of the shared geometric framework underlying both the cosmology and galaxy analyses. This carryover is architectural rather than automatic: it does not by itself validate galaxy-handedness or local residual claims, which remain separate empirical tests. The strongest carryover occurs only where explicit cross-scale bridge quantities—such as R or r_p—are derived and independently confirmed.

---

## 5. Next failure points (ordered)

1. **Official-grade late-time pipeline** (full DESI joint cov + STAT+SYS already partly done; remaining: Lyα BAO, identical nuisance handling).
2. **Proper CMB anchoring** (validated distance prior or full Planck likelihood for CPL).
3. **Perturbation / growth sector** — can the model survive P(k), fσ₈, lensing without pathological growth? Requires PPF or micro completion.
4. **Explicit galaxy bridge test** (R on SPARC / BTFR) — independent of cosmology success.

---

## Compact statement

The frozen-φ point crosses the phantom divide at the exact geometric redshift z_c=1/√5≈0.447 (early phantom → late quintessence), consistent with the direction preferred by DESI free-CPL fits. Background expansion and early-DE density are safe; perturbation stability is not yet secured and requires either a multi-field realization or a PPF effective treatment. Cosmology success strengthens framework credibility and shared-constant motivation but does not automatically validate galaxy-handedness or local residual claims.
