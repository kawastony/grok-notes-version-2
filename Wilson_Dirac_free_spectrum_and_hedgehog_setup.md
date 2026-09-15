# Minimal Wilson–Dirac Hamiltonian for 3-D hedgehog + free-spectrum verification

Tony Kawas / 15 September 2026.

---

## Part A — Minimal Wilson–Dirac Hamiltonian (sketch)

### A.1 Free Wilson–Dirac operator (3-D, periodic)

In lattice units \(a=1\):

\[
D_W = m\,\mathbf{1} + \sum_{\mu=1}^{3}\Bigl[\tfrac12\gamma_\mu\bigl(T_\mu-T_\mu^\dagger\bigr) - \tfrac r2\bigl(T_\mu+T_\mu^\dagger-2\bigr)\Bigr]
\]

where \(T_\mu\) is the unit shift operator in direction \(\mu\) and \(r\sim 1\).

Site-level implementation:
- Diagonal: \(m + 3r\)
- Forward hop \(x\to x+\hat\mu\): \(-\frac12(r - \gamma_\mu)\)
- Backward hop \(x\to x-\hat\mu\): \(-\frac12(r + \gamma_\mu)\)

Hermitian operator for spectral flow:
\[
H_W(m) = \gamma_5 D_W(m).
\]

### A.2 Exact free dispersion (periodic lattice)

\[
E(\mathbf k) = \pm\sqrt{\sum_\mu\sin^2 k_\mu + \Bigl(m + r\sum_\mu(1-\cos k_\mu)\Bigr)^2}.
\]

Doublers at the Brillouin-zone corners are lifted by the Wilson term (mass ~ \(m+6r\) in 3-D).

### A.3 Hedgehog mass texture (smooth, asymptotically gapped)

\[
M(\mathbf x) = v\,f(r)\,\begin{pmatrix}\boldsymbol\sigma\cdot\hat{\mathbf n}_{N} & 0\\ 0 & -\boldsymbol\sigma\cdot\hat{\mathbf n}_{N}\end{pmatrix},
\]
with
\[
f(r)=\tanh(r/w),\qquad f(0)=0,\;f(\infty)=1,
\]
and higher-winding map
\[
\hat{\mathbf n}_N = \bigl(\sin\theta\cos(N\phi),\;\sin\theta\sin(N\phi),\;\cos\theta\bigr).
\]

Full operator:
\[
D = D_W^{\rm kinetic+Wilson} + M(\mathbf x).
\]

### A.4 Spectral-flow index

\[
H(s) = \gamma_5\bigl(D_{\rm free} + s\,M_{\rm hedge}\bigr)\quad\text{or}\quad H(m)=\gamma_5\bigl(D_{\rm hedge}+m\bigr).
\]
Net signed zero-crossings = \(\mathrm{Index}_{\rm sf}\). On a healthy operator one expects \(\mathrm{Index}_{\rm sf}=N_{\rm def}\) (local index around one core on a torus pair).

### A.5 Free-spectrum checklist (must pass before any defect)

1. Periodic lattice, no hedgehog.  
2. Numerical eigenvalues of \(H_W\) match the analytic dispersion mode-by-mode.  
3. No extensive zero kernel (\(\#\{|\lambda|<10^{-6}\}=0\) for generic \(m\ne0\)).  
4. Doubler corner \(|E(\pi,\pi,\pi)|\) is O(1) or larger.  
5. Gap above the lowest modes is consistent with the analytic formula.

---

## Part B — Free-spectrum verification (PASSED)

### B.1 Implementation

- Periodic \(L=4\) lattice.  
- Wilson parameter \(r=1\).  
- Bare masses \(m=0.5\), \(1.0\), \(-0.5\).  
- Dense diagonalisation of \(H=\gamma_5 D_W\).  
- Direct comparison with the analytic Wilson dispersion sampled on the discrete Brillouin zone.

### B.2 Results

**m = 0.5**

| Quantity | Numerical | Analytic |
|----------|-----------|----------|
| Lowest \|λ\| (×4) | 0.500000 | 0.500000 |
| Next cluster | 1.802776 | 1.802776 |
| # \|λ\| < 1e-6 | 0 | — |
| Doubler corner (π,π,π) | — | 6.5000 |

**m = 1.0**

| Quantity | Numerical | Analytic |
|----------|-----------|----------|
| Lowest \|λ\| (×4) | 1.000000 | 1.000000 |
| Next cluster | 2.236068 | 2.236068 |
| # \|λ\| < 1e-6 | 0 | — |
| Doubler corner | — | 7.0000 |

**m = −0.5**

| Quantity | Numerical | Analytic |
|----------|-----------|----------|
| Lowest \|λ\| (×4) | 0.500000 | 0.500000 |
| Next cluster | 1.118034 | 1.118034 |
| # \|λ\| < 1e-6 | 0 | — |
| Doubler corner | — | 5.5000 |

### B.3 Conclusion of the free-operator test

- Exact numerical–analytic match.  
- **No extensive zero kernel.**  
- Doublers lifted.  
- Gap correct.  

**The free Wilson–Dirac operator is now healthy.** All previous spectral-flow failures can be attributed to the defective continuum-like / naive kinetic term that produced an unphysical kernel.

---

## Part C — Immediate next steps

1. Re-introduce the smooth hedgehog mass texture on top of this verified Wilson operator.  
2. Run spectral flow (additive mass or strength scan) on L ≥ 7–9.  
3. For periodic lattices use a hedgehog–anti-hedgehog pair and extract the **local** index around one core.  
4. Only then revisit residual chirality and continuum extrapolation.

---

## Compact statement

A minimal Wilson–Dirac Hamiltonian for the 3-D hedgehog test has been written down. Its free periodic spectrum has been verified analytically and numerically: perfect match, no extensive zero kernel, doublers lifted. The free-operator prerequisite is now satisfied. The topological index calculation can be restarted on a healthy discretisation.
