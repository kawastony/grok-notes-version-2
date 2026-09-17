# Random Instanton Liquid Model (RILM)

Tony Kawas / 17 September 2026.

**Scope:** Definition, parameters, computational method, successes/failures vs interacting ensembles; relation to the lattice soft-sector program.

---

## 1. What RILM is

The **Random Instanton Liquid Model** is the simplest working ensemble realization of the instanton liquid:

| Ingredient | RILM choice |
|------------|-------------|
| Instanton size | Fixed (or narrowly distributed), typically \(\rho_0 \simeq 0.35\,\mathrm{fm}\) |
| Density | Fixed \(n_0 \simeq 1\,\mathrm{fm}^{-4}\) (I and A equal) |
| Positions | **Random** in Euclidean volume |
| Color orientations | **Random** |
| Classical I–A interactions | **Ignored** in the ensemble measure |
| Fermion determinant in measure | **Ignored** (quenched-style ensemble); quarks enter only when computing propagators |

Parameters go back to Shuryak (1982); large-scale correlator calculations: Shuryak–Verbaarschot and Schäfer–Shuryak–Verbaarschot (1990s).

RILM = “put random topological lumps of fixed size and density, then solve quark propagation in that background.”

---

## 2. How calculations are done

1. Generate a multi-instanton gauge field (sum/ratio ansatz of many I and A).
2. Build the Dirac operator in that background (often zero-mode zone + non-zero mode corrections).
3. Compute quark propagators.
4. Contract into mesonic and baryonic **point-to-point correlators**.
5. Average over the random ensemble.

The ’t Hooft interaction is effectively kept to all orders through the zero-mode structure of the propagator, while quark loops in the measure are not (quenched character of the ensemble).

---

## 3. Successes

| Channel / quantity | RILM performance |
|--------------------|------------------|
| \(\pi\), many light mesons | Strong attraction; correlators often close to phenomenology/lattice |
| Nucleon (octet) | Deeply bound; good agreement with early lattice point-to-point data |
| \(\Delta\) (decuplet) | Weaker binding; qualitative N–\(\Delta\) pattern |
| Dozens of correlators | Often good out to ~1–1.5 fm |
| Vacuum scales | Built to match condensate/gluon scales via \(n,\rho\) |

Surprising historical result: a model **without confinement** still bound the main light hadrons in correlators well enough that free multi-quark continuum pollution was hard to see in practice.

---

## 4. Failures and why interacting liquids exist

| Problem channel | What goes wrong in pure RILM |
|-----------------|------------------------------|
| **\(\eta'\)** | Correlator drops too fast, can go negative — no topological screening |
| **Isovector scalar (\(\delta\))** | Same class of failure |
| Topological susceptibility | Random ensemble lacks I–A correlation → wrong screening |

**Cure:** **Interacting Instanton Liquid Model (IILM)** — put classical + fermion-induced interactions into the ensemble measure so I–A molecules and topological charge screening appear. Then \(\eta'\) and related channels improve.

So:

- RILM ≈ excellent for many “non-topologically delicate” channels  
- RILM ≈ insufficient where topology and U(1)_A matter most  
- IILM / molecular ensembles restore those

---

## 5. RILM vs IILM (short)

| Feature | RILM | IILM |
|---------|------|------|
| Positions/orientations | Random | Correlated by interactions |
| Measure | Flat (fixed n, ρ) | Weighted by bosonic ± fermion forces |
| Molecules | Only accidental overlaps | Built in |
| \(\eta'\) / screening | Poor | Improved |
| Most light correlators | Already good | Refined |

---

## 6. Relation to the hedgehog soft-sector program

| RILM | This lattice system |
|------|---------------------|
| Many random topological lumps | One (or few) fixed hedgehog pairs |
| Ensemble-averaged quark correlators | Spectrum of one Hamiltonian |
| Dilute liquid by construction | **Molecular** pair at L≤10 |
| Quenched random measure | No gauge ensemble at all — mass texture only |

**Shared idea:** topological backgrounds generate soft Dirac structure and chiral physics.  
**Not RILM:** your code does not sample random multi-instanton ensembles or compute hadron correlators.

Milestone 3 discipline:

- Do **not** fit RILM \((n,\rho)\) from soft \(\lambda\) or χ_βn.  
- Molecular soft sector is closer in spirit to **one I–A molecule** than to a random liquid.  
- A multi-pair density scan would be a weak analogue of “varying liquid density,” still a different operator.

---

## 7. Status table

| Statement | Status |
|-----------|--------|
| RILM is the standard minimal instanton ensemble for correlators | Established |
| Works well for π, N, many channels | Established |
| Fails η′, topological screening without interactions | Established |
| Lattice soft pair = RILM | **No** |
| Soft molecular regime ~ one molecule, not random liquid | **Analogy** |
| Extract RILM parameters from L≤10 | **Drop** |

---

## 8. Compact statement

RILM is a fixed-density, fixed-size, randomly placed/oriented instanton–antiinstanton ensemble used to compute quark propagators and hadron correlators. It succeeds in many light channels and fails where topological correlations (η′, screening) matter — which motivates interacting and molecular ensembles. The Wilson–Dirac hedgehog program shares topology-driven soft modes but is not an RILM simulation; at L≤10 it sits in a molecular, not random-liquid, regime.
