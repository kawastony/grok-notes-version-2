# Alternative core profile functions — L = 10, sep = 6

Tony Kawas / 16 September 2026.

---

## Profiles tested

| Name | f(r) |
|------|------|
| tanh | tanh(r/w) |
| exp | 1 − exp(−r/w) |
| sech_sq | tanh²(r/w) |
| compact | smoothstep to 1 at r = 2.5w, then flat |
| sharp | linear ramp 0.5w → 1.5w, then 1 |

Common parameters: L = 10, sep = 6, w = 1.0, v = 1.5, R = 2.0 diagnostic ball.

---

## Results

| Profile | softest \|λ\| | Δλ | Owner | P per core (softest) | IPR (softest) |
|---------|--------------|-----|-------|----------------------|---------------|
| tanh | 6×10⁻⁵ | 0.00022 | shared | 0.025 | 0.0014 |
| exp | 0.00095 | 0.0024 | shared | 0.023 | 0.0022 |
| sech_sq | 1×10⁻⁵ | 0.00085 | shared | 0.041 | 0.0010 |
| compact | 0.00193 | 0.00003 | shared | 0.031 | 0.0008 |
| sharp | 5×10⁻⁵ | 0.00037 | shared | 0.034 | 0.0007 |

---

## Observations

1. **Soft near-zero sector is robust** across all five profiles.  
2. **No profile produces preferred-core ownership** at this volume/separation.  
3. tanh and sech_sq give the softest eigenvalues; compact is the hardest (still O(10⁻³)).  
4. IPR remains O(10⁻³) for all — modes are not tightly core-bound.  
5. Changing the radial shape alone does not exit the molecular regime at L = 10, sep = 6.

---

## Conclusion

The hybridization is driven by **geometric overlap** (separation vs mode extent), not by the detailed shape of f(r). Alternative core functions do not substitute for larger absolute separation.

The 8-component Callias embedding continues to produce a soft sector for every reasonable profile tested.

---

## Compact statement

Five core profiles (tanh, exp, sech², compact smoothstep, sharp ramp) were compared at L = 10, sep = 6. All keep a soft near-zero spectrum and fully shared mode weight. Profile shape is not the bottleneck; scale separation is.
