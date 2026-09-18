# Matched ±15% boost vs weaken + path question

Tony Kawas / 19 September 2026.

L=10, d=3, mode 0, residual ~10⁻¹⁴. Perturb **core 1** only.

---

## 1. Matched magnitudes

| State | v1 | load | span | width | P1 | P2 | pol=(P1−P2)/(P1+P2) |
|-------|-----|------|------|-------|------|------|------|
| base | 2.0 | 0.134 | 3.37 | 3.88 | 0.042 | 0.029 | **+0.18** |
| **+15%** | 2.3 | **0.214** | **2.94** | **3.52** | 0.065 | 0.068 | **−0.03** |
| **−15%** | 1.7 | 0.161 | 3.22 | 3.39 | 0.034 | 0.061 | **−0.29** |

### Δ vs base

| | Δload | Δspan | Δwidth | Δpol |
|--|--------|--------|---------|------|
| +15% | **+0.080** | **−0.43** | −0.35 | −0.21 (→ balanced) |
| −15% | +0.027 | −0.15 | **−0.49** | **−0.47** (→ AH-heavy) |

**Equal-size up/down do not give equal-size effects.**  
Boost: larger load gain, larger span shrink, **less** polarized.  
Weaken: smaller load change, strong width shrink, **more** polarized.

---

## 2. “Compact without spin” vs “shrink and spin”

Interpreting **spin** as **polarization** (weight imbalance), not literal rotation:

| Action | Compactify? | Polarize (“spin”)? |
|--------|-------------|---------------------|
| +15% one pole | **Yes** (span↓ width↓ load↑) | **No** — pol → ~0 (more balanced) |
| −15% one pole | **Yes** (span↓ width↓) | **Yes** — pol → −0.29 (AH gains) |

So your contrast is **directionally right**:
- energy **up** → collective compactification, **less** polarized  
- energy **down** → still compactifies, **more** polarized  

Not “spin” in a dynamical sense — **reweighting**.

---

## 3. Tube narrowing vs pole lengths — same size?

Pole length proxy = axial RMS of density **inside each core ball**.

| | rel Δspan (tube) | rel Δwidth | rel Δpole1 | rel Δpole2 |
|--|------------------|------------|------------|------------|
| +15% | **−13%** | −9% | **+52%** | **+36%** |
| −15% | −4% | **−13%** | +30% | −14% |

**Not the same.** Global tube span/width shrink while core-local “pole” RMS often **grows**.  
The object becomes more concentrated in the pair region (global span down) while support inside the core balls can spread a bit. Do not equate “tube length” with “pole length.”

---

## 4. Sequential energy phases (one cone vs separate cones)

**Static spectral observables depend only on the final \((v_1,v_2)\).**  
History does not matter:

- base → +15% → −15% ends at the same state as base → −15%  
- UU / DD / UD / DU cannot be distinguished by these eigenmode diagnostics

So with **this** method you **cannot** test “huge single cone vs separately created cones” via energy-up/down sequencing. That would need:

- true time-dependent dynamics, or  
- a hysteretic / nonlinear order parameter that remembers path, or  
- something other than the static soft mode of a fixed texture

`up15_then_dn15` in the data is **identical** to `dn15` — as required by static H.

---

## Compact statements

1. Matched ±15%: both compactify; boost is collective, weaken is polarized.  
2. Effects are **not** symmetric in magnitude.  
3. Tube size and pole-ball size do **not** scale together.  
4. Static path sequences **cannot** decide one-cone vs multi-cone assembly.
