# Quantitative molecular regime scan

Tony Kawas / 17 September 2026.

**Operator:** 8-component Wilson–Dirac + hedgehog/antihedgehog, m₀=0.3, v=2, w=1, r=1.  
**Core ball:** radius 2.  
**Data:** `/home/workdir/artifacts/molecular_scan_L6_8_10.json` (pair + single controls).

---

## 1. Pair scan — soft splitting and support

### L = 6

| d | soft \|λ\| (4) | Δλ | P₁ | P₂ | \|P₁−P₂\| | IPR₀ |
|---|---------------|------|------|------|----------|------|
| 1 | 0.0005, 0.0039, … | 0.0035 | 0.020 | 0.024 | 0.004 | 0.031 |
| 2 | 0.0010, 0.0033, … | 0.0023 | 0.126 | 0.178 | 0.052 | 0.009 |
| 3 | 0.0057, 0.0080, … | 0.0023 | 0.118 | 0.118 | 0.000 | 0.010 |

### L = 8

| d | soft \|λ\| | Δλ | P₁ | P₂ | \|P₁−P₂\| | IPR₀ |
|---|------------|------|------|------|----------|------|
| 1 | 0.0014, 0.0023, … | 0.0009 | 0.007 | 0.009 | 0.002 | 0.014 |
| 2 | 0.0005, 0.0048, … | 0.0043 | 0.077 | 0.078 | 0.001 | 0.005 |
| 3 | 0.0001, 0.0024, … | 0.0023 | 0.080 | 0.098 | 0.018 | 0.003 |
| 4 | 0.0004, 0.0016, … | 0.0012 | 0.095 | 0.095 | 0.000 | 0.004 |

### L = 10

| d | soft \|λ\| | Δλ | P₁ | P₂ | \|P₁−P₂\| | IPR₀ |
|---|------------|------|------|------|----------|------|
| 1 | 0.0036, 0.0046, … | 0.0009 | 0.029 | 0.032 | 0.003 | 0.003 |
| 2 | 0.0008, 0.0039, … | 0.0031 | 0.073 | 0.036 | 0.037 | 0.002 |
| 3 | 0.0014, 0.0015, … | 0.0001 | 0.042 | 0.029 | 0.013 | 0.002 |
| 4 | 0.0005, 0.0011, … | 0.0007 | 0.030 | 0.023 | 0.007 | 0.002 |
| 5 | 0.0004, 0.0008, … | 0.0004 | 0.009 | 0.009 | 0.000 | 0.003 |

**Universal:** \|P₁−P₂\| is small for most points; soft modes share both centers when weight is measurable. At large d, core fractions drop (delocalized on the torus).

---

## 2. Single-defect control

| L | type | lowest \|λ\| | P_core | IPR |
|---|------|-------------|--------|-----|
| 6 | H / AH | 0.0065 | 0.101 | 0.006 |
| 8 | H / AH | 0.0015 | 0.056 | 0.003 |
| 10 | H / AH | 0.0005 | 0.012 | 0.001 |

- H and AH spectra **identical** (as expected by symmetry of the setup).
- Single defect already produces soft modes (Callias-like), with modest core weight decreasing with L.
- Pair softest \|λ\| is often **smaller** than single-defect softest at same L (hybridization / level repulsion structure), not a simple copy of two singles.

---

## 3. Operational regime labels (empirical)

Proposed cuts (refine later):

- **Molecular:** soft pair present, \|P₁−P₂\| < 0.05, and both P₁,P₂ > 0.02 **or** (if both small) balanced delocalized with Δλ < 0.005
- **Hybridizing:** shared support but \|P₁−P₂\| moderate or Δλ larger
- **Close / merged:** d=1 — soft modes exist but core weights tiny (texture nearly canceling on scale of core radius)

At L≤10, **no clear isolated regime** (one mode on one core only): volume too small / ξ too large. Molecular and hybridizing dominate the scanned window.

---

## 4. Main conclusions

1. **Balanced two-center support** (P₁≈P₂) is robust across L and most d.  
2. **Soft sector exists for both pair and single defect**; pair is not two independent copies.  
3. **Isolated single-core ownership is not reached** at L≤10 — consistent with Milestone 1 molecular claim.  
4. Δλ stays O(10⁻³)–O(10⁻⁴); no simple exponential dissociation curve yet (need larger L / larger d/ξ).

---

## 5. Next

- Optional: denser d grid or L=12 only with residual-validated soft modes.  
- Optional: regime diagram figure from this table.  
- Multi-pair density only after one-pair map is settled.

---

## 6. Compact statement

A separation scan at L=6,8,10 shows soft modes with stably balanced core ownership (P₁≈P₂) and O(10⁻³) splittings. Single-defect controls confirm soft modes without a partner, but the pair soft sector is not a disjoint union of two singles. The molecular regime is an internal property of this operator at these volumes; the isolated-core limit is not yet visible.
