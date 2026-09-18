# L=12 pair bridge “dynamics” (static geometry)

Tony Kawas / 18 September 2026.

**Data:** Residual-validated L=12 pair scan (16/16 accepted, max rel_v ~ 6.5×10⁻¹⁰).  
**Scope:** How bridge observables change with separation and softness.  
**Not in scope:** Time evolution, currents, signal transfer, or transport laws.

---

## 1. What “bridge dynamics” can mean here

| Meaning | Status |
|---------|--------|
| BT, Bρ vs separation *d* | **Done** (static scan) |
| Softness (\|λ\|) vs bridge weight | **Done** (correlations) |
| Preferred *d* for texture-bound corridor | **Done** |
| Response to core perturbation | **Not done** |
| Phase / current along corridor | **Not done** |
| Time-dependent transfer | **Not done** |

This note is **static bridge geometry and spectral correlation only**.

---

## 2. Bridge vs separation (from your Colab table)

### Softest / most molecular modes highlighted

| d | mode | \|λ\| | P1 | P2 | Bρ | BT | class |
|---|------|--------|------|------|------|------|--------|
| 1 | 0 | 0.0026 | 0.0015 | 0.0015 | 0.0010 | **3e-8** | defect_like |
| 1 | 1 | 0.0038 | 0.0028 | 0.0030 | 0.0018 | **1e-7** | defect_like |
| 3 | 0 | 0.00042 | 0.046 | 0.037 | 0.064 | **1.2e-4** | **strict molecular** |
| 3 | 2 | 0.00109 | 0.067 | 0.057 | 0.096 | **2.8e-4** | **strict molecular** |
| 3 | 3 | 0.00139 | 0.032 | 0.023 | 0.037 | 4.3e-5 | shared |
| 5 | 0 | 0.00106 | 0.028 | 0.028 | 0.079 | **1.7e-4** | **strict molecular** |
| 5 | 3 | 0.00273 | 0.022 | 0.021 | 0.063 | **1.0e-4** | **strict molecular** |
| 6 | 0 | 0.00007 | 0.010 | 0.010 | 0.018 | 6e-6 | defect_like |
| 6 | 3 | 0.00053 | 0.029 | 0.029 | 0.035 | 2.6e-5 | shared |

### Pattern

1. **d=1 (merged):** almost no bridge (BT ~ 10⁻⁸). Cores overlap; corridor is undefined.
2. **d=3:** **BT peak** (~1–3×10⁻⁴) + largest Bρ; strict molecular modes.
3. **d=5:** still strong BT (~1–2×10⁻⁴); molecular survives.
4. **d=6 (max on torus):** Bρ remains, BT drops; sharing persists (P1=P2) but strict BT threshold often fails.

**Preferred window for texture-weighted corridor: intermediate d (3–5), same qualitative window as L=10.**

---

## 3. Softness ↔ bridge (static correlation)

From the accepted modes:

- Softest multiplet at **d=6** has small BT (modes live delocalized, not corridor-dominated).
- Softest **molecular** modes (d=3 m0, d=5 m0) combine **low \|λ\|** with **measurable BT**.
- Defect_like modes at d=1 are **harder** and almost bridgeless.

Qualitative rule of thumb (not a fit):

> Intermediate separation → soft + shared + texture-lit bridge.  
> Too close → hard, no bridge.  
> Too far (on this volume) → soft but bridge weight thins.

That is **structural “dynamics” of the bridge with *d***, not time dynamics.

---

## 4. Relation to single-defect control

| | Single L=12 | Pair L=12 (molecular d) |
|--|-------------|-------------------------|
| \|QT\| | ~0.84 | ~0.75–0.85 |
| Bridge | none | BT up to ~3×10⁻⁴ |
| Spatial | one core | two cores + corridor |

Bridge weight is a **pair-only** observable. Dynamics questions that need a corridor only make sense for the pair.

---

## 5. What would count as true bridge dynamics (future)

Ordered by difficulty:

1. **Static response:** rescale one core mass slightly → measure ΔP1, ΔP2, ΔBT (does weight slide along the corridor?).
2. **Phase structure:** arg of soft spinor along the tube (standing-wave vs gradient).
3. **Current proxy:** if a conserved U(1) exists, lattice current between planes perpendicular to the pair axis.
4. **Time-dependent:** real-time or adiabatic drive of one core — far beyond current spectral program.

None of (1)–(4) are claimed from the present scan.

---

## 6. Defensible statements

**Allowed**

- At residual-validated L=12, the texture-weighted bridge BT peaks at intermediate separation (d≈3–5).
- Strict texture-bound molecular modes coincide with that window.
- Bridge is pair-specific; singles have no corridor.
- Softness and bridge weight are related only in a structural, d-dependent way.

**Not allowed**

- Signal propagates along the bridge.
- BT is a current or transfer rate.
- Bridge dynamics explain gravity / DM / DE.

---

## 7. Compact statement

L=12 residual-validated soft pairs show a **static bridge geometry** that strengthens at intermediate separation and tracks texture-bound molecular identity. That opens structured propagation questions; it does not demonstrate dynamical transfer.
