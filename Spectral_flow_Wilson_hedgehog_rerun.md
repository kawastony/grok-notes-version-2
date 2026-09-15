# Spectral flow rerun on verified Wilson–Dirac + smooth hedgehog

Tony Kawas / 15 September 2026.

---

## 1. Setup

- Free Wilson–Dirac operator previously verified (exact match to analytic dispersion, no extensive kernel, doublers lifted).
- Smooth hedgehog mass texture of degree N_def = 1:
  \[
  M(\mathbf x)=v\,f(r)\,(\boldsymbol\sigma\cdot\hat{\mathbf n}),\qquad f=\tanh(r/w).
  \]
- Hermitian operator \(H=\gamma_5(D_W+M)\) (or strength flow / additive mass flow).
- Lattices: L = 5 and L = 7, open and periodic.
- Parameters explored: v = 1.2–2.5, mass scan m ∈ [−4, 4], strength s ∈ [0, 2].

---

## 2. Results

| Lattice | BC | Scan | Index_sf | min \|λ\| over scan | Crossings |
|---------|-----|------|----------|---------------------|-----------|
| L=5 | periodic | strength s | 0 | O(6) | none |
| L=5 | open | strength s | 0 | O(6) | none |
| L=7 | periodic | strength s | 0 | O(6) | none |
| L=7 | open | strength s | 0 | O(6) | none |
| L=5 | periodic | additive m, v=1.5 | 0 | ∼4.5 | none |
| L=5 | open | additive m, v=2.5 | 0 | ∼4.4 | none |

In every run the spectrum of H remained gapped and predominantly negative; no eigenvalue crossed zero.

---

## 3. What is working

- Free Wilson operator is healthy (verified analytically and numerically).
- Code infrastructure for spectral flow (tracking, signed crossings) functions correctly.
- Adding the hedgehog shifts the spectrum in a smooth, reproducible way.

---

## 4. Why Index_sf is still zero

1. **Global topology on the torus**  
   A single hedgehog on a periodic lattice is topologically obstructed. The global index is required to vanish. Index_sf = 0 on periodic single-hedgehog runs is therefore the expected global answer, not a failure. A non-trivial test requires a hedgehog–anti-hedgehog pair and a *local* index measurement around one core.

2. **Wilson mass scale vs hedgehog strength**  
   Even with v = 2.5 the gap of H stays O(4–6). The physical window where continuum-like zero crossings would appear has not yet been reached; the Wilson term still dominates the low-lying spectrum of H = γ₅D.

3. **Mass-matrix embedding and γ₅ structure**  
   The block form used for M may not be the precise continuum Jackiw–Rossi operator that guarantees exact zero modes of D (and therefore zero eigenvalues of H at the critical mass). A different Dirac-structure embedding may be required before crossings appear.

4. **Volume**  
   L = 5–7 remains modest for simultaneous resolution of core, asymptotic gap, and (on the torus) a well-separated pair.

---

## 5. Revised next steps (ordered)

1. **Hedgehog–anti-hedgehog pair on a periodic lattice**  
   Place charges +1 and −1 well separated. Compute local spectral asymmetry / local density of near-zero modes of H inside a sub-volume around one core. That local integer is the quantity that should equal N_def.

2. **Tune the bare mass into the critical Wilson window**  
   Scan m more finely in the region where the free Wilson operator has its smallest eigenvalues, with a stronger asymptotic hedgehog gap v.

3. **Continuum Jackiw–Rossi mass matrix**  
   Replace the present block embedding by the exact continuum Dirac structure that produces analytic zero modes, then discretise.

4. **Larger volume** once the pair geometry is in place.

---

## 6. Status relative to the Callan-Harvey program

| Item | Status |
|------|--------|
| Free Wilson spectrum | Verified healthy |
| Smooth hedgehog texture | Implemented |
| Global Index_sf on single hedgehog (periodic) | 0 (expected) |
| Local Index_sf = N_def | Not yet demonstrated |
| Continuum analytic index & inflow | Intact |

The free-operator obstacle is removed. The remaining obstacle is to measure the *local* index of a topologically consistent configuration (pair on the torus, or single hedgehog on a large open volume with controlled boundaries).

---

## 7. Compact statement

Spectral flow was re-run on the verified Wilson–Dirac operator plus a smooth hedgehog. No zero crossings were observed; Index_sf remained 0. On periodic lattices this is the expected global answer for a single hedgehog. The next decisive calculation is a hedgehog–anti-hedgehog pair with a local spectral-flow measurement around one core.
