# Lattice zero-mode on a hedgehog patch of the cone network

Tony Kawas / 15 September 2026.  
Concrete discrete calculation that closes the last open item of the Callan-Harvey sector.

---

## 1. Goal

Construct a finite-dimensional lattice Dirac operator on a small cubic neighbourhood of a degree-1 hedgehog, insert the continuum radial profile of χ as a position-dependent mass, and verify the existence of a near-zero eigenvalue of definite chirality whose wave-function is localised on the core.

Success criterion: the lowest eigenvalue satisfies |λ| ≪ gap of the rest of the spectrum, and the corresponding eigenvector has the expected chirality and radial fall-off.

---

## 2. Lattice geometry

- Grid: cubic lattice of size L³ with L odd (so a unique centre site), open or Dirichlet boundaries far from the core.  
  Practical starting values: L = 7, 9 or 11.
- Lattice spacing a = 1 (units in which the core radius is a few lattice units).
- Centre of the hedgehog placed at the origin site.

The cone network itself is not yet discretised; we only need a local patch that supports the topological defect. The continuum identification A ≡ ε_T is not required for the pure zero-mode problem.

---

## 3. Continuum hedgehog profile on the lattice

Define the radial distance from the centre site
\[
r_i = a\sqrt{n_x^2+n_y^2+n_z^2}.
\]
A simple smooth profile that realises topological degree 1 is
\[
\chi(r) = \chi_\infty\,\tanh\bigl((r-r_0)/w\bigr)
\]
or the classic exponential form
\[
\chi(r) = \chi_\infty\bigl(1-e^{-r/w}\bigr),
\]
with χ(0) = 0 (or π) and χ → χ_∞ far away.  
The width w is chosen a few lattice spacings (w ∼ 1.5–2.5 a) so that the core is resolved but still localised inside the patch.

The angular part of the hedgehog is carried by the Dirac matrices; the scalar profile χ(r) supplies the radial mass that binds the zero-mode.

---

## 4. Lattice Dirac operator (Wilson form)

The free Wilson–Dirac operator on a cubic lattice reads
\[
D_{\rm W}(x,y)
=
\frac{1}{2}\sum_\mu\Bigl[(r-\gamma_\mu)\,U_\mu(x)\,\delta_{y,x+\hat\mu}
+(r+\gamma_\mu)\,U_\mu^\dagger(y)\,\delta_{y,x-\hat\mu}\Bigr]
+(m+4r)\delta_{xy},
\]
where r is the Wilson parameter (usually r = 1) and U_μ are the link variables.  
For the pure zero-mode problem we may set all links to the identity (no background gauge field) and absorb the continuum mass into a site-dependent term:
\[
D(x,y)
=
D_{\rm W}^{\rm free}(x,y)
+
g\,\chi(r_x)\,\delta_{xy}.
\]
The full operator is a sparse complex matrix of size (4 L³) × (4 L³) (4 spinor components).

Chirality operator: γ⁵ = diag(+1,+1,−1,−1) in the Dirac basis.  
The would-be zero-mode should be an approximate eigenvector of both D and γ⁵.

---

## 5. Numerical procedure

1. Build the sparse matrix D for chosen L, w, g χ_∞.  
2. Compute the eigenvalues of smallest absolute value (ARPACK / Lanczos / dense SVD for tiny L).  
3. For the lowest mode ψ₀ extract:  
   - |λ₀|,  
   - the chiral expectation 〈ψ₀|γ⁵|ψ₀〉,  
   - the radial density ρ(r) = ∑_{sites at r} |ψ₀|².  
4. Verify:  
   - |λ₀| is parametrically smaller than the bulk gap ∼ O(1),  
   - 〈γ⁵〉 ≈ ±1,  
   - ρ(r) peaks at the origin and falls exponentially.

A successful run on L = 9 already demonstrates the continuum index theorem at finite lattice spacing.

---

## 6. Minimal Python skeleton (numpy / scipy)

```python
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigs

# Parameters
L = 9
a = 1.0
w = 2.0
gchi = 1.5          # g * χ_∞
r_wilson = 1.0

def idx(x,y,z,s):
    """Flatten (x,y,z,spin) -> 0 .. 4L^3-1"""
    return s + 4*((z%L) + L*((y%L) + L*(x%L)))

# gamma matrices (Dirac basis)
gamma = [None]*5
# ... standard 4x4 Dirac matrices ...

N = 4 * L**3
D = lil_matrix((N, N), dtype=complex)

# Wilson kinetic + site-dependent mass
for x in range(L):
    for y in range(L):
        for z in range(L):
            r = a * np.sqrt((x-L//2)**2 + (y-L//2)**2 + (z-L//2)**2)
            mass = gchi * np.tanh((r - 0.5)/w)   # or 1-exp(-r/w)
            for s in range(4):
                i = idx(x,y,z,s)
                D[i,i] += (mass + 4*r_wilson)
                # hopping terms for mu = 1,2,3
                # ... standard Wilson hoppings ...

# Extract lowest eigenvalues
evals, evecs = eigs(D.tocsr(), k=6, sigma=0.0, which='LM')
print(np.sort(np.abs(evals)))
```

(The hopping implementation is standard and omitted for brevity; any textbook Wilson kernel works.)

---

## 7. Expected output and interpretation

On a sufficiently fine patch one finds a single eigenvalue |
λ₀| ∼ O(e^{-L/w}) or smaller, separated by a gap of order the bulk mass g χ_∞.  
The corresponding eigenvector is localised on the core and is an approximate eigenstate of γ⁵.  
That is the lattice avatar of the continuum Jackiw–Rossi zero-mode.

Increasing L or decreasing a improves the continuum limit; the index remains stable under moderate changes of w and g χ_∞, confirming topological protection.

---

## 8. Relation to the continuum results already obtained

- The lattice zero-mode realises the index Index(D) = 1 calculated earlier for a degree-1 hedgehog.  
- Its radial profile converges to the continuum exponential derived from the Yukawa equation.  
- Once the mode is obtained, the local vector current it carries can be measured directly on the lattice and compared with the continuum Callan-Harvey inflow expression.  
- Global cancellation on a larger lattice that contains both a hedgehog and an anti-hedgehog follows automatically: the two near-zero modes have opposite chirality and the net index vanishes.

---

## 9. Status

The calculation is fully specified and ready for numerical execution.  
No new free parameter is required; the only inputs are the already-locked continuum profile of χ and a conventional lattice discretisation.  
A successful run closes the last open item of the Callan-Harvey sector at the discrete level.

---

## 10. Next action

Implement the skeleton above (or an equivalent staggered / overlap operator) on L = 7–11, report the lowest eigenvalues and the chiral density of the zero-mode, and deposit the numerical notebook or script in the same repository.
