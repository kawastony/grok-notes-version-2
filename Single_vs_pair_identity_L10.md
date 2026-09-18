# Single vs pair identity (L=10, residual-validated)

Tony Kawas / 18 September 2026.

---

## Results

| Config | mode | \|λ\| | QT | core weight(s) | IPR |
|--------|------|--------|------|----------------|-----|
| Single H | 0 | 0.00050 | **−0.840** | P=0.012 | 0.0014 |
| Single H | 1 | 0.00120 | −0.802 | P=0.018 | 0.0013 |
| Single AH | 0 | 0.00050 | **−0.840** | P=0.012 | 0.0014 |
| Single AH | 1 | 0.00120 | −0.802 | P=0.018 | 0.0013 |
| Pair d=3 | 0 | 0.00139 | **−0.828** | P1=0.042, P2=0.029 | 0.0024 |
| Pair d=3 | 1 | 0.00148 | −0.795 | P1=0.031, P2=0.028 | 0.0019 |

All rel_v ~ 10⁻¹⁴.

---

## Identity conclusions

1. **Single H and AH are identical** in spectrum and QT (expected by construction).
2. **Texture anti-alignment is not pair-specific** — singles also have QT ≈ −0.8.  
   Identity marker QT is a **defect-texture** property, not only a molecular one.
3. **Pair identity is spatial + spectral**, not QT alone:  
   - shared two-center support (P1≈P2)  
   - soft cluster of two modes near each other  
   - (from prior scan) weak BT bridge  
4. Pair softest \|λ\| is **larger** than single softest (0.0014 vs 0.0005) at this d — hybridization / finite-volume coupling, not a deeper zero.

### Identity hierarchy

| Level | Marker |
|-------|--------|
| Defect-level | QT < 0 (texture anti-alignment) |
| Pair-level | P1≈P2 + soft multiplet + optional BT |

---

## Track status after this step

| Track | Progress |
|-------|----------|
| Identity | Single vs pair distinguished; QT common; sharing is the pair signature |
| Propagation | Unchanged (bridge geometry only) |
| Unification | Still scaffolding |

---

## L=12 note

Sandbox OOM (exit 137) on L=12 sparse H build/solve.  
**L=12 residual tests belong on Colab / larger RAM**, with the same residual gate (rel_v ≲ 10⁻⁶ before any physics).  
Do not interpret L=12 modes without that gate.
