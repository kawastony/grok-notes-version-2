# Effective source–geometry ansatz (locked)

Tony Kawas / 19 September 2026.

**Status:** Locked as a discrete/effective research ansatz.  
**Not:** Einstein’s equation, GR, or continuum Ricci dynamics.

---

## 1. Analogy map

### Source-like \(\mathcal T\)

| symbol | meaning |
|--------|--------|
| \(R_{\rm mid}\) | midpoint density / mean end density |
| \(c\) | axial quadratic coefficient (\(<0\) peak, \(>0\) dip) |
| \(|D_1|\) | polarization |
| \(A=\lambda_1/\lambda_3\) | shape anisotropy |

\[
\mathcal T = (R_{\rm mid},\, c,\, |D_1|,\, A).
\]

### Geometry-like \(\mathcal G\)

| symbol | meaning |
|--------|--------|
| \(F_{\rm mid}\) | mean mid-edge Forman curvature |
| \(\Delta W_{\rm mid}\) | early bridge-feeding under stabilized Forman flow |
| \(g_{ab}\) | local parameter-space metric |

Primary dynamic discriminator: \(\Delta W_{\rm mid}\).

---

## 2. Working ansatz (scalar form)

\[
\Delta W_{\rm mid}
\approx
a_0
+ a_1 R_{\rm mid}
+ a_2 (-c)
- a_3 |D_1|
- a_4 (A-1).
\]

Expected signs:
- \(a_1>0\): midpoint richness → more bridge feeding
- \(a_2>0\): sharper peak (more negative \(c\)) → more feeding
- \(a_3>0\): polarization → less feeding
- \(a_4\): excess anisotropy may reduce shared support

---

## 3. Three-case table (L=10, d=3, residual-validated)

| case | \(R_{\rm mid}\) | \(c\) | \(|D_1|\) | \(A\) | \(F_{\rm mid}\) | \(\Delta W_{\rm mid}\) |
|------|----------------|------|----------|------|----------------|----------------------|
| baseline | **1.30** | −0.007 | 0.18 | 1.56 | −9.28 | **+0.113** |
| +15% | 1.21 | **−0.010** | **0.03** | **1.47** | −8.71 | +0.048 |
| −15% | **0.90** | **+0.004** | **0.29** | **1.86** | −8.72 | **≈ 0** |

### Rank coherence

| quantity | rank (favorable → unfavorable) |
|----------|--------------------------------|
| \(\Delta W_{\rm mid}\) | base > +15% > −15% |
| \(R_{\rm mid}\) | base > +15% > −15% | **matches** |
| \(c\) (peaked first) | +15% > base > −15% | partial |
| \(|D_1|\) (low first) | +15% > base > −15% | partial |

**\(R_{\rm mid}\) alone matches \(\Delta W_{\rm mid}\) rank exactly.**  
Equal-weight \(T_{\rm eff}=R_{\rm mid}-c-|D_1|-(A-1)\) ranks +15% above base (because +15% is more balanced and more peaked), so coefficients are not all equal — \(R_{\rm mid}\) appears to dominate early bridge feeding in this sample.

With 3 points this is **coherence**, not a fitted law.

---

## 4. Are Einstein’s equations useful here?

**No — not as equations to solve or identify.**

| Einstein structure | Our setting |
|--------------------|-------------|
| \(G_{\mu\nu}=8\pi T_{\mu\nu}\) | No spacetime metric, no Einstein tensor |
| Continuum Ricci from Levi-Civita | Forman is combinatorial graph curvature |
| Stress-energy from matter fields | Source vector is mode-shape diagnostics |
| Differential Bianchi identities | Not applicable |

What **is** useful is the **architectural idea**:

> load organization (source-like) predicts geometric response (geometry-like).

That is an effective correspondence ansatz, not GR. Claiming Einstein’s equations themselves would be false.

---

## 5. Locked claim (safe wording)

> We introduce a discrete/effective source–geometry ansatz in which midpoint load, anisotropy, polarization, and center hollowing act as source-like variables, while graph curvature, bridge-feeding under stabilized Forman flow, and local parameter-space stiffness act as geometry-like variables. The goal is not to reproduce Einstein gravity, but to test whether internal load organization predicts emergent geometric response in a systematic way.

---

## 6. Next test (when expanding)

Denser \((v_1,v_2)\) grid → multivariate regression of \(\Delta W_{\rm mid}\) on \((R_{\rm mid},c,|D_1|,A)\).  
Until then: rank coherence + sign checks only.

---

## Compact statement

Ansatz locked. \(R_{\rm mid}\) tracks \(\Delta W_{\rm mid}\) rank on the three residual-validated states; polarization and hollowing align directionally. Einstein’s equations are **not** useful as equations here — only the source→geometry architectural analogy is.
