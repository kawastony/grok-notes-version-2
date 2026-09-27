# Callias index theorem — details

Complements `Callias_index_theorem_exploration.md`.

---

## 1. Operator class

On odd-dimensional ℝⁿ (n=3 in the lattice program):
\[
L = \mathcal{Q} + \Phi,
\qquad
\mathcal{Q} = \sum_{j=1}^{n} \gamma_j \partial_j
\]
with Φ Hermitian, matrix-valued, and **invertible at infinity**:
\[
|\Phi(x)| \ge c > 0 \quad \text{for } |x| > R.
\]
Derivatives of Φ decay so that L is Fredholm on L².

---

## 2. Index formula (structure)

\[
\mathrm{Index}(L) = \dim\ker L - \dim\ker L^*
= \text{topological degree of } U\big|_{S^{n-1}_\infty},
\]
where
\[
U(x) = \mathrm{sgn}(\Phi(x)) = \Phi(x)/|\Phi(x)|
\]
on a large sphere. Explicit integral forms exist (Callias; Gesztesy–Waurick; Anghel): Chern character of the positive eigenbundle of U evaluated on S^{∞}.

**Structural fact:** only the **asymptotic class** of Φ enters the index. Smooth deformations of the core that preserve invertibility at infinity and the asymptotic winding leave Index(L) unchanged.

---

## 3. Hedgehog case (n=3)

\[
\Phi(\mathbf{r}) = v\, f(r)\, \hat{\mathbf{n}}(\theta,\phi)\cdot\boldsymbol{\tau},
\quad f(r)\to 1\ (r\to\infty).
\]
If the map S² → S² given by n̂ has degree N_def:
\[
\mathrm{Index}(L) = N_{\rm def}
\]
(up to convention of sign). Unit hedgehog → one protected zero mode (or definite chiral imbalance). Hedgehog + antihedgehog → total index 0, with a soft hybridized pair when separation is not ≫ correlation length.

---

## 4. What Callias does *not* say

- It does not fix the **energy** of soft modes away from exact zero (lattice, finite volume, Wilson terms shift them).
- It does not by itself produce SI scales (μ_*, a_eff, ρ_Λ).
- It does not identify the asymptotic sphere with a cosmological horizon unless that identification is added as a separate physical assumption.

---

## 5. Link to spectral motion and protection

Along a path that preserves asymptotic winding and invertibility:
\[
\frac{d}{ds}\mathrm{Index}(L(s))=0,
\]
while individual eigenvalues λ_a(s) may move (spectral motion). That is the continuum backbone of “activity without identity change” in the micro→galactic scale-transfer example.
