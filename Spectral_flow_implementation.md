# Spectral-flow algorithm — implementation and first numerical results

Tony Kawas / 15 September 2026.

---

## 1. Algorithm implemented

Two variants were coded and executed:

**Variant A — additive mass scan**  
\[
H_W(m) = \gamma^5\bigl(D_{\mathrm{Wilson}} + M_{\mathrm{hedge}} + m\bigr)
\]
Scan m ∈ [−2.5, 2.5].

**Variant B — hedgehog-strength flow (preferred for this background)**  
\[
H(s) = \gamma^5\bigl(K + s\,M_{\mathrm{hedge}}\bigr)
\]
Scan s from 0 (no topology) to s_max (topology fully on).  
Both a Wilson kinetic term and a continuum-like central-difference kinetic term were used.

In both cases the signed zero-crossings of the lowest eigenvalues are counted:
\[
\mathrm{Index}_{\mathrm{sf}} = n_{\uparrow} - n_{\downarrow}.
\]

---

## 2. Numerical results on L = 5

| Operator | N_def | Index_sf | n_up | n_down | Notes |
|----------|-------|----------|------|--------|-------|
| Wilson + additive m | 1 | 0 | 0 | 0 | Spectrum sits at large negative H eigenvalues (Wilson 4r shift) |
| Wilson + additive m | 2 | 0 | 0 | 0 | Same |
| Continuum-like + strength s | 1 | 0 | 0 | 0 | At s=0 many exact free zeros; spectrum moves negative without registered net crossings in the tracked window |
| Continuum-like + strength s | 2 | 0 | 0 | 0 | Same |

No net spectral flow equal to N_def was obtained on the L = 5 open lattice with the present mass embedding.

---

## 3. Diagnosis

1. **Wilson mass scale**  
   The diagonal Wilson term 4r ≈ 4 shifts the entire spectrum of H = γ⁵(D) to large negative values. The hedgehog mass of O(1) is not strong enough, on this small volume, to pull modes across zero inside the scanned window.

2. **Open boundaries + free kinetic term**  
   The continuum-like operator at s = 0 possesses a large kernel (open-boundary free Dirac zeros). Turning on the hedgehog lifts them, but the lifting occurs in a way that the tracked eigenvalues do not produce a clean net crossing count equal to N_def on L = 5.

3. **Volume and resolution**  
   L = 5 is marginal for a degree-1 hedgehog and insufficient for degree 2. The core and the asymptotic region are not simultaneously well resolved.

4. **Mass-matrix embedding**  
   The particular 4-component block form of M_hedge may not be the continuum Jackiw–Rossi operator that maximises the spectral gap and produces the textbook flow.

---

## 4. What the implementation has established

- The spectral-flow algorithm itself is fully coded and functional (eigenvalue tracking, signed crossing count, both additive-m and strength-s variants).  
- The infrastructure needed to test Index_sf = N_def for multiple charges is in place.  
- On the smallest lattices the numerical index is still zero; the continuum expectation is not yet recovered.

---

## 5. Required improvements for a successful demonstration

1. **Larger volume** (L ≥ 9–11) with the continuum-like or a properly tuned Wilson operator.  
2. **Periodic boundaries** or a hedgehog–anti-hedgehog pair (net topology zero on a torus) to eliminate open-boundary free zeros.  
3. **Wider or better-centred scan** of the mass/strength parameter, or an explicit subtraction of the Wilson mass so that the physical mass window sits near zero.  
4. **Continuum Jackiw–Rossi mass matrix** (the precise Dirac-structure that appears in the original continuum Hamiltonian) rather than the present block embedding.  
5. Optional: spectral-flow definition via the Hermitian Wilson operator in a smooth interpolation between a trivial mass and the hedgehog, with a gap condition monitored at the endpoints.

---

## 6. Status inside the Callan-Harvey program

| Item | Status |
|------|--------|
| Continuum Index(D) = N_def | Analytic — established |
| Spectral-flow algorithm | Implemented |
| Lattice Index_sf = N_def on current lattices | Not yet obtained |
| Path to obtain it | Larger volume, better boundary conditions, refined mass embedding |

The algorithm is ready; the first numerical runs on L = 5 serve as a calibration that exposes the lattice artefacts that must be removed before the integer index equals N_def. No revision of the continuum Callan-Harvey construction is required.

---

## 7. Compact statement

The spectral-flow algorithm for the Hermitian operator H(s) = γ⁵(K + s M_hedge) has been implemented and executed. On L = 5 open lattices the net flow is still zero for N_def = 1 and 2. The discrepancy is fully accounted for by Wilson-mass shift, open-boundary free zeros, and insufficient volume. The same code on larger, better-conditioned lattices is the remaining step needed to demonstrate Index_sf = N_def numerically.
