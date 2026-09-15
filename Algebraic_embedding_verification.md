# Algebraic verification of the continuum embedding

Tony Kawas / 15 September 2026.

Result of the highest-priority Part I check: explicit matrix algebra, anticommutators, H² structure, grading, and unitary-equivalence to a known index-carrying class.

---

## 1. Continuum requirements (reminder)

A 3-D Callias / Jackiw–Rossi hedgehog requires:

- Kinetic matrices α_i with {α_i, α_j} = 2δ_ij, α_i† = α_i  
- Mass matrices that anticommute with every α_i  
- At least three independent such mass matrices (so that a map S² → S² of degree N_def exists)  
- M(n)² = |n|² 1  
- A grading operator that organises chiral zero modes  
- Asymptotic gap and point-like defect

---

## 2. Kinetic sector (healthy)

With the standard 4-component choice
\[
\alpha_i = \begin{pmatrix}0&\sigma_i\\\sigma_i&0\end{pmatrix},\qquad
\beta = \begin{pmatrix}I&0\\0&-I\end{pmatrix},
\]
one has
\[
\alpha_i^2 = I,\qquad\{\alpha_i,\alpha_j\}=0\ (i\ne j),\qquad\{\alpha_i,\beta\}=0.
\]
The free kinetic algebra is correct.

---

## 3. Present lattice mass embedding — fails

The 4-component block used so far,
\[
M_{\rm block}(\hat n) = \begin{pmatrix}\boldsymbol\sigma\cdot\hat n&0\\0&-\boldsymbol\sigma\cdot\hat n\end{pmatrix},
\]
satisfies
\[
M_{\rm block}^2 = I
\]
but **does not anticommute with all kinetic matrices**:
\[
\{M_{\rm block},\alpha_1\}\ne0,\qquad\{M_{\rm block},\alpha_2\}\ne0
\]
(when \(\hat n=\hat z\); only the third anticommutator vanishes). Consequently the continuum identity
\[
H^2 = -\nabla^2 + |M|^2 + \text{(gradient/spin terms)}
\]
is not realised. Cross terms survive and the operator is not of Callias type.

Moreover
\[
\{\gamma^5, M_{\rm block}\}\ne0,
\]
so the grading used on the lattice does not make the mass term odd in the sense required for a chiral index.

---

## 4. Dimensional obstruction in 4 components

The vector space of Hermitian 4×4 matrices that anticommute with α_x, α_y and α_z is **one-dimensional**; it is spanned by β.  
A hedgehog needs a non-trivial map from S² into the sphere of normalised mass matrices, which requires **at least three** independent anticommuting mass matrices.  
Therefore **no 4-component embedding can realise a continuum 3-D Callias hedgehog**.

This is the algebraic reason the spectral flow never produced protected crossings: the defect was geometrically hedgehog-like but topologically trivial for the fermions.

---

## 5. Required continuum structure (8-component)

Promote the spinor to
\[
\text{Dirac (4)}\otimes\text{isospin (2)} \quad\Rightarrow\quad 8\text{-component}.
\]

\[
H = \boldsymbol\alpha\cdot\mathbf p\otimes\mathbf 1_\tau + \beta\otimes\bigl(v f(r)\,\boldsymbol\tau\cdot\hat{\mathbf x}\bigr).
\]

- Kinetic matrices: α_i ⊗ 1  (still anticommute among themselves and with β ⊗ 1).  
- Mass matrices: β ⊗ τ_a  (three independent matrices that anticommute with every kinetic matrix and with each other in the appropriate sense).  
- Asymptotic map: ordinary isospin hedgehog of degree N_def.  
- Grading: γ⁵ ⊗ 1 (or the appropriate 8-component involution).  
- Index = N_def by the Callias theorem.

This is the standard continuum representative that carries the index.

---

## 6. Lattice implication

All previous lattice runs used a 4-component mass texture that is **not** in the Callias / Jackiw–Rossi class.  
The free Wilson operator was healthy; the topological class of the defect was not.

**Concrete next implementation step**

1. Enlarge the Hilbert space to 8 components per site (Dirac ⊗ isospin).  
2. Keep the verified Wilson kinetic term acting as α_i ⊗ 1.  
3. Insert the mass texture β ⊗ (v f(r) τ · n̂_N).  
4. Re-run the local diagnostic suite (D1–D4) on a hedgehog–anti-hedgehog pair.

Only after that embedding is in place can a non-zero local index be expected.

---

## 7. Status of the falsifiable programme

| Question | Answer |
|----------|--------|
| Is the free operator healthy? | Yes |
| Does the present 4-component block realise Callias/JR? | **No** |
| What is required? | 8-component Dirac ⊗ isospin mass texture |
| Observable | Local diagnostics on a pair (still correct) |

The programme failed cleanly on the embedding question, exactly as designed. The fix is now unambiguous.

---

## Compact statement

Algebraic verification shows that the 4-component block mass matrix does not anticommute with the kinetic Dirac matrices and cannot support a non-trivial π₂ of mass matrices. A continuum 3-D Callias hedgehog requires an 8-component (Dirac ⊗ isospin) structure of the form β ⊗ (τ · n̂). All previous null spectral-flow results are explained by this mismatch. The next step is to implement the 8-component embedding and repeat the local diagnostics.
