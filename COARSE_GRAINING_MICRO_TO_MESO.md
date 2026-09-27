# Coarse-graining map: soft-mode activity → mesoscopic δμ

**Status:** Schematic bridge law. Encodes activity + topological lock → structured variance around fixed μ_*. Does not derive SI μ_*.

Aligned with external review: spectral motion / index lock is the right micro split; coarse-graining is the next formal layer.

---

## 1. Microscopic inputs (per defect-pair / bridge cell c)

- Soft eigenvalues λ_a^{(c)}(s)
- Core weights w_{a,i}^{(c)}(s) = ∫_{core i} |ψ_a|²
- Pair separation Δ^{(c)}
- Topological data Q_i^{(c)}, Index ℐ^{(c)}

**Activity scalar**
\[
A_c(s)=\sum_{a\in\mathrm{soft}}\alpha_a|\partial_s\lambda_a^{(c)}|
+\sum_{a,i}\beta_{ai}|\partial_s w_{a,i}^{(c)}|.
\]

**Lock indicator**
\[
L_c=\mathbf{1}\![\mathcal{I}^{(c)}=\mathcal{I}_0,\; Q_i^{(c)}=Q_{i,0}]
\]
(or a smooth proxy ≈1 when index/charges preserved).

---

## 2. Local bridge contribution

\[
\delta\mu_c = K(\Delta^{(c)},\lambda^{(c)},w^{(c)})\,L_c.
\]

Minimal linear form:
\[
\delta\mu_c
=
\kappa_\Delta f(\Delta^{(c)})
+
\kappa_\lambda \sum_a g(\lambda_a^{(c)})
+
\kappa_w \sum_{a,i} h(w_{a,i}^{(c)}-\bar w_{a,i}).
\]

Zero-mean normalization (identity locked):
\[
\langle\delta\mu_c\rangle_c = 0
\quad\text{(or absorbed into }\mu_*\text{)}.
\]

Topology as selection rule:
\[
\delta\mu_c = L_c\cdot\widetilde{\delta\mu}_c
\quad\Rightarrow\quad
L_c\approx 1:\ \text{variance allowed, drift suppressed.}
\]
If L_c fails → possible midpoint drift / topology change (falsifier).

---

## 3. Coarse-grain to mesoscopic field

Patch R:
\[
\delta\mu_R = \frac{1}{|R|}\sum_{c\in R} W_c\,\delta\mu_c
\]
or continuum:
\[
\delta\mu(x)=\int d^dy\,\mathcal{K}(x-y)\,\delta\mu_{\mathrm{micro}}(y).
\]

\[
\mu(x)=\mu_*+\delta\mu(x).
\]

Weights W_c / kernel 𝒦 encode defect density, bridge connectivity, optional environmental weighting.

---

## 4. Non-propagation

\[
\langle\delta\mu\rangle=0,\qquad \langle\dot\mu\rangle\approx 0
\]
if:
1. ∂_s ℐ^{(c)}=0, ∂_s Q_i^{(c)}=0
2. positive/negative exchange cancels in the first moment
3. activity enters second and higher moments only

Result:
\[
\mu_*\ \text{fixed},\qquad \mathrm{Var}(\delta\mu)>0.
\]

---

## 5. Residual statistics (observable target)

\[
\mathrm{Var}(\delta\mu)
\sim
\frac{1}{|R|^2}\sum_{c,c'}W_c W_{c'}\langle\delta\mu_c\delta\mu_{c'}\rangle
\ \propto\ \langle A_c^2\rangle\,\xi_{\mathrm{corr}}^d.
\]

Two-point:
\[
C_\mu(r)=\langle\delta\mu(x)\delta\mu(x+r)\rangle.
\]
- Short-range bridges: C_μ(r) ~ C_0 e^{-r/ξ_μ}
- Tube / network-like: C_μ(r) ~ C_0 r^{-η} e^{-r/ξ_μ}

Hierarchical SPARC target: not only scatter amplitude, but **correlation structure** of residuals after de-dressing.

---

## 6. Effective closure

\[
\dot{\delta\mu}=-\gamma\,\delta\mu+\sigma\,\zeta_{\mathrm{struct}}(t,x),
\]
with ⟨ζ_struct⟩=0 and
\[
\langle\zeta_{\mathrm{struct}}(x)\zeta_{\mathrm{struct}}(x')\rangle\sim C_\mu(|x-x'|).
\]
Structured noise from micro spectral motion — not white noise.

---

## 7. Specialized to G12 + Δ (first reduction)

\[
A_c \supset |\partial_s(P_1-P_2)| + |\partial_s\Delta|
\]
(G12 weight slide + separation motion).

\[
\delta\mu_c \approx L_c\bigl(\kappa_\Delta f(\Delta)+\kappa_G G_{12}^{\mathrm{loc}}\bigr),
\qquad
\langle\delta\mu_c\rangle=0.
\]

Predicts residual correlation length tied to typical defect separation / soft-tube width.

---

## 8. What this does / does not

| Does | Does not |
|------|----------|
| Encode micro activity explicitly | Derive SI value of μ_* |
| Preserve topological lock | Fully specify f,g,h |
| Explain variance without mean drift | Prove the kernel 𝒦 |
| Give testable C_μ(r) | Remove one-input boundary |

---

## One-line summary

\[
\text{spectral motion}+\text{topological lock}
\ \xrightarrow{\text{coarse-grain}}\
\text{structured mesoscopic variance around fixed }\mu_*.
\]
