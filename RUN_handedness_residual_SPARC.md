# Handedness residual run — SPARC × winding labels

Tony Kawas / 19 September 2026.

U1 scale probe executed. Frozen baseline rule only. No retune.

---

## Data

| Source | Role |
|--------|------|
| SPARC MassModels (Lelli+2016) | \(V_{\mathrm{obs}}, V_{\mathrm{gas}}, V_{\mathrm{disk}}, V_{\mathrm{bul}}\) |
| VizieR SPARC Table1 | RA, Dec |
| Jia–Zhu–Pen reduced GZ1 / DESI CE-ResNet | S/Z probabilities |

**Match:** sky separation \(\le 0.05^\circ\).  
**Sense rule:** prefer DESI CE-ResNet if \(p_{\mathrm{cw}}+p_{\mathrm{acw}}>0.05\); else GZ votes.  
Label **Z** if \(p_{\mathrm{cw}}>p_{\mathrm{acw}}+0.1\); **S** if opposite; else U.

## Sample

| Sense | Galaxies with RC residual |
|-------|---------------------------|
| Z | 11 |
| S | 11 |
| U (excluded) | 153 |

Nearby SPARC ∩ SDSS/DESI chirality catalogs is **sparse** (as expected).

## Frozen rule

\[
\Upsilon_{\mathrm{disk}}=0.5,\quad \Upsilon_{\mathrm{bul}}=0.7,\quad
a_T=8.25\times 10^{-11}\,\mathrm{m\,s^{-2}},\quad
\text{simple interpolator}.
\]

Per-galaxy residual: \(V_{\mathrm{obs}}-V_{\mathrm{model}}\).

## Results

| Sense | Median MAE (km/s) | Mean MAE | Median mean residual |
|-------|-------------------|----------|----------------------|
| S | 14.32 | 21.34 | (mixed signs) |
| Z | 14.85 | 14.85 | (mixed signs) |

**Mann–Whitney (two-sided)**

| Quantity | U | p |
|----------|---|---|
| MAE Z vs S | 51 | **0.56** |
| Mean residual Z vs S | 65 | **0.79** |

## Verdict

\[
\boxed{\text{Null result on }n=22\text{ matched SPARC galaxies under freeze.}}
\]

No significant S/Z residual split. This does **not** falsify lattice identity or relative Forman mediation; it means the residual-network chiral template is **not detected** in this small cross-match.

## Limitations

- Small \(n\) (SPARC is local; GZ/DESI chirality is mostly higher-\(z\))
- Name/coord match only; no visual re-inspection of winding
- Baseline rule is the simple interpolator, not a full residual-network force law

## Next for U1

1. Expand labels via Iye–Sugai southern catalog + manual SPARC overlap  
2. Or use larger RC samples (e.g. SPARC-like) that sit inside GZ footprint  
3. Pre-register effect size before claiming a detection

## Programme impact

| Track | Effect |
|-------|--------|
| Identity | Unchanged |
| Propagation | Unchanged |
| Unification U1 | **Probe executed — null on current match** |

Honest scale tracking: the first residual handedness test is done; the puzzle piece did not light up on this sample.
