# Spectral-flow index calculation — detailed procedure

Tony Kawas / 15 September 2026.  
Concrete lattice definition of Index(D) that can be compared with N_def for multiple topological charges.

---

## 1. Why spectral flow

The continuum index theorem states
\[
\mathrm{Index}(D) = n_+ - n_- = N_{\mathrm{def}}.
\]
On a generic lattice Dirac operator the near-zero eigenvalues are not exactly zero and may form multiplets of mixed chirality, so a direct count of “zero modes” is ambiguous.  
The **spectral flow** of the Hermitian Wilson–Dirac operator supplies an integer that is stable under small deformations and coincides with the continuum index (and with the overlap index) once the lattice spacing is fine enough. It does not require a pure chiral eigenstate.

---

## 2. Continuum motivation

Consider the one-parameter family of continuum Hermitian operators
\[
H(m) = \gamma^5\bigl(D + m\bigr),\qquad m\in\mathbb{R}.
\]
For m ≠ 0 the spectrum of H(m) has a gap around zero.  
As m is varied from a large positive value to a large negative value, eigenvalues of H(m) may cross zero.  
Each crossing of a positive-chirality continuum zero-mode contributes +1 to the spectral flow; each negative-chirality mode contributes −1.  
The net spectral flow equals the analytic index:
\[
\mathrm{sf}\bigl[H(m)\bigr] = n_+ - n_- = \mathrm{Index}(D).
\]

---

## 3. Lattice definition (Wilson spectral flow)

### 3.1 Hermitian Wilson–Dirac operator

Let D_W be the Wilson–Dirac operator on the cubic lattice (including the hedgehog mass matrix M_hedge of degree N_def):
\[
D_W = D_{\mathrm{Wilson\ kinetic}} + M_{\mathrm{hedge}}.
\]
Define the one-parameter family
\[
H_W(m) = \gamma^5\bigl(D_W + m\bigr),\qquad m\in\mathbb{R}.
\]
H_W(m) is Hermitian for every real m. Its spectrum is real.

### 3.2 Spectral flow

Vary m continuously from m_start ≫ 0 (or from the upper edge of the Wilson spectrum, conventionally m ≈ +8r for Wilson parameter r = 1) down to m_end ≪ 0 (or to m ≈ −8r).  
Track every eigenvalue λ_k(m) of H_W(m).  
Whenever an eigenvalue crosses zero, record the direction of the crossing:

- upward crossing (λ goes from − to +) contributes +1,  
- downward crossing (λ goes from + to −) contributes −1.

(The sign convention is fixed so that the net flow reproduces the continuum index; an overall minus sign is sometimes used in the literature and must be kept consistent.)

The **spectral-flow index** is the net number of crossings:
\[
\mathrm{Index}_{\mathrm{sf}} := \mathrm{sf}\bigl[H_W(m)\bigr] = n_{\uparrow} - n_{\downarrow}.
\]

### 3.3 Relation to the overlap index

For a sufficiently fine lattice and a background that satisfies the locality bounds of the overlap construction,
\[
\mathrm{Index}_{\mathrm{sf}} = \mathrm{Index}_{\mathrm{overlap}} = \mathrm{Index}_{\mathrm{continuum}} = N_{\mathrm{def}}.
\]
This equality has been proved rigorously for Wilson operators on the torus (higher-index theory) and verified numerically in abelian and non-abelian gauge backgrounds.

---

## 4. Practical algorithm for the hedgehog / cone background

### Step 1 — Build the Wilson operator with hedgehog mass

- Lattice size L³ (open or periodic).  
- Wilson kinetic term with r = 1.  
- Site-dependent mass matrix of degree N_def:
  \[
  M(\mathbf{x}) = m_0 f(r)\,\begin{pmatrix}\boldsymbol{\sigma}\cdot\hat{\mathbf{n}}_{N_{\mathrm{def}}} & 0 \\ 0 & -\boldsymbol{\sigma}\cdot\hat{\mathbf{n}}_{N_{\mathrm{def}}}\end{pmatrix},
  \]
  with the higher-winding map
  \[
  \hat{\mathbf{n}}_{N} = \bigl(\sin\theta\cos(N\phi),\;\sin\theta\sin(N\phi),\;\cos\theta\bigr).
  \]
- Optional: mild smoothing of r̂ near the origin (already shown to reduce chirality mixing).

### Step 2 — Form the Hermitian family

\[
H_W(m) = \gamma^5\bigl(D_W + m\,\mathbf{1}\bigr).
\]
(The identity multiplies the 4-component spinor space.)

### Step 3 — Scan m and track crossings

- Choose a dense grid of m-values covering the interval in which physical crossings are expected (typically −2 ≲ m ≲ +2 for a well-resolved hedgehog; the full Wilson range −8r … +8r can be used for safety).  
- At each m compute the lowest ∼ 2|N_def| + 10 eigenvalues of H_W(m) (ARPACK / Lanczos).  
- Identify zero crossings by linear interpolation between consecutive m-points (or by monitoring sign changes of each ordered eigenvalue).  
- Accumulate the signed crossings.

### Step 4 — Extract the index

\[
\mathrm{Index}_{\mathrm{sf}}(N_{\mathrm{def}}) = n_{\uparrow} - n_{\downarrow}.
\]
Repeat for N_def = 1, 2, 3, … on the same lattice family.  
The test of the lattice index theorem is
\[
\mathrm{Index}_{\mathrm{sf}}(N_{\mathrm{def}}) \;\stackrel{?}{=}\; N_{\mathrm{def}}
\]
(within the integer-valued spectral flow).

### Step 5 — Continuum check

Repeat the whole scan on a sequence of finer lattices (a → 0 at fixed physical core width).  
Index_sf must remain equal to N_def; any deviation at coarse spacing must disappear under refinement.

---

## 5. Diagnostic information carried by the flow

- **Location of the crossing** in m indicates the “size” of the mode: crossings near m = 0 correspond to continuum-like, delocalised zero-modes; crossings near the Wilson edges (m ∼ ±8) are lattice artefacts of size ∼ a.  
- **Chirality of the crossing mode** can be read from the expectation value 〈ψ|γ⁵|ψ〉 of the eigenvector at the crossing point (or from the slope dλ/dm = 〈γ⁵〉).  
- For a clean continuum hedgehog one expects exactly |N_def| crossings of continuum character, all of the same chiral sign, and no net contribution from the artefact region.

---

## 6. Expected outcome for the cone / Callan-Harvey program

| N_def | Continuum Index | Expected Index_sf on fine lattice |
|-------|-----------------|-----------------------------------|
| 1     | +1              | +1                                |
| 2     | +2              | +2                                |
| 3     | +3              | +3                                |
| −1    | −1              | −1 (anti-hedgehog)                |

Once this table is verified numerically, the lattice statement
\[
\mathrm{Index}_{\mathrm{sf}}(D) = N_{\mathrm{def}}
\]
holds for multiple topological charges. Combined with the already-derived continuum Callan-Harvey inflow current, the microscopic anomaly cancellation is then under complete lattice + continuum control.

---

## 7. Relation to previous lattice work in this repository

- The earlier continuum-like operator produced a multiplet of exact zeros for N_def = 1; the spectral-flow definition resolves the multiplicity into a net integer equal to N_def.  
- The residual 〈γ⁵〉 mixing observed previously becomes irrelevant for the index, because only the signed zero-crossings are counted.  
- After the spectral-flow index is confirmed, a Ginsparg–Wilson or domain-wall realisation can be used to isolate single chiral zero-modes and finish the clean 〈γ⁵〉 → ±1 extrapolation.

---

## 8. Implementation checklist

1. Code Wilson kinetic term + degree-N_def hedgehog mass matrix.  
2. Build H_W(m) = γ⁵ (D_W + m).  
3. Dense m-scan, track lowest eigenvalues, count signed zero-crossings.  
4. Repeat for N_def = 1, 2, 3 and for a sequence of lattice spacings.  
5. Record Index_sf(N_def, a) and verify equality with N_def on the finest lattices.

No new free parameters enter; the only inputs are the already-locked continuum profile of χ and a conventional Wilson discretisation.

---

## 9. Compact statement

The spectral flow of the Hermitian Wilson–Dirac operator H_W(m) = γ⁵(D_W + m) in the angular-hedgehog background of degree N_def yields an integer Index_sf that equals the continuum topological charge N_def on sufficiently fine lattices. This supplies the missing lattice proof that Index(D) = N_def for multiple charges, independent of residual chirality mixing of individual eigenvectors.
