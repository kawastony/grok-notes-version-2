# Scar boundary-layer physics

## What “scar” means here

Not a paper-25 spelled-out field theory of a scar. Operational content from geometry + the ν₀ shift:

1. Ideal defect sector: Δψ = 35° = 7π/36 from N_wind = 72/7 (full azimuth / sector).
2. Mixed BC placed at 35° (Neumann, baryonic) and 70° (Dirichlet, sovereign) — outer edge = 2×35°.
3. Pure spherical Legendre mixed-BC root on exact [35°,70°]: ν₀ = 2.3713.
4. Paper 25 quotes ν₀ ≈ 2.31 → equivalent to shifting the outer edge to ≈70.82° (Δψ_eff ≈ 35.82°) or an effective boundary-layer width δθ ≈ 0.82°.

That δθ is the **scar / boundary-layer** correction: a thin angular region where ideal cone BC fail and tiling/image charges or mixed-boundary transition live.

---

## Geometric origins of a ~1° layer

| Mechanism | Scale |
|-----------|--------|
| Winding unit | 360°/N_wind = 35° exactly |
| Image reduction (n_eff: ⌊N_wind⌋−2) | removes 2 units → 70° outer scale |
| Fractional residual of N_wind | N_wind−10 = 0.286 → 0.286×35° ≈ 10° (coarse) |
| Fine scar to match ν=2.31 | δθ ≈ 0.82° ≈ 2.3% of 35° |

The 0.82° layer is **phenomenological** relative to the pure spherical problem: it is the angle shift that moves ν from 2.3713 → 2.31. It is not yet derived from a stress-energy boundary layer or lattice cutoff.

---

## Physics content (working picture)

```text
Ideal cone sector (35°) + mixed BC
        → pure Legendre ν₀ = 2.3713
        → boundary layer / scar δθ ~ O(1°)
        → effective ν₀ ≈ 2.31 (Paper 25)
        → Δ_μ in γ formula
```

Possible microscopic readings (none closed):

- **Tiling scar:** frustration of 72/7 on a discrete angular graph leaves a residual defect angle.
- **BC transition layer:** Neumann→Dirichlet cannot jump discontinuously; a finite angular skin depth softens the outer wall.
- **Image-charge offset:** the −2 unit reduction in n_eff is a discrete image count; continuous version shifts the Dirichlet wall slightly.

---

## Effect on γ

Scar is the difference between pure-sphere γ≈0.161 and Paper-25 γ≈0.156 — both inside SPARC ±0.060. Scar is **sub-dominant** to bootstrap error; it matters for theory bookkeeping, not for data exclusion.

---

## Status

| Claim | Status |
|-------|--------|
| δθ≈0.82° maps ν 2.3713→2.31 | Verified numerically |
| Scar = tiling frustration from 72/7 | Motivated, not derived |
| Dynamical boundary-layer equation | Open |
