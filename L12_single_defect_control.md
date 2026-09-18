# L=12 single-defect control

Tony Kawas / 18 September 2026.

**Status:** Pair scan at L=12 is residual-validated (16/16 accepted). Single-defect control should use the **same** residual gate and texture observables.

This environment OOMs on L=12; run the cells below on **Colab High-RAM** (same session that produced the pair results is ideal).

---

## Scientific questions

1. Does a single H/AH at L=12 still show **QT ≈ −0.8** (defect-local texture identity)?
2. Is softest single \|λ\| smaller or larger than softest pair modes?
3. Is **pair identity** still distinguished by **P1≈P2 + multiplet + BT**, not by QT alone?

From L=10 we expect:
- Single QT ≈ −0.84, Pcore small (~0.01)
- Pair QT similar, but shared two-center support

---

## Colab cells (paste after the pair notebook is loaded)

```python
# ===== L=12 single-defect control =====
# Requires: algebra, hedgehog, build_sparse_H, relative_residual,
#           solve_soft_modes, gate_modes, in_ball, CFG, BASE_DIR, MASS_B, etc.

def run_single_L12(cfg, charges=(+1, -1), k=4):
    rows = []
    for ch in charges:
        label = "H" if ch > 0 else "AH"
        print(f"\n=== L={cfg.L} single {label} ===")
        c = (cfg.L//2, cfg.L//2, cfg.L//2)
        defects = [(int(ch), *c)]
        H = build_sparse_H(cfg.L, defects, cfg.m0, cfg.v_coup, cfg.w, cfg.r_wilson)
        print(f"nnz={H.nnz}")
        evals, evecs = solve_soft_modes(H, k, cfg.eig_tol, cfg.eig_maxiter)
        records = gate_modes(H, evals, evecs, cfg.rel_residual_gate)
        for j, (lam, rr, ok) in enumerate(records):
            print(f"  mode{j}: λ={lam:+.6e} rel_v={rr:.3e} accepted={ok}")
            row = {
                "L": cfg.L, "config": f"single_{label}", "d": None,
                "mode": j, "lambda": lam, "abs_lambda": abs(lam),
                "rel_residual": rr, "accepted": ok,
            }
            if ok:
                pr = evecs[:, j].reshape((cfg.L, cfg.L, cfg.L, 8))
                dens = np.sum(np.abs(pr)**2, axis=3)
                dens /= dens.sum() + 1e-30
                chiT = np.zeros_like(dens)
                for x, y, z in product(range(cfg.L), repeat=3):
                    loc = pr[x, y, z]
                    f, hx, hy, hz = hedgehog(x, y, z, *c, cfg.L, cfg.w)
                    nn = np.sqrt(hx*hx + hy*hy + hz*hz + 1e-30)
                    M = (hx/nn)*MASS_B[0] + (hy/nn)*MASS_B[1] + (hz/nn)*MASS_B[2]
                    chiT[x, y, z] = float(np.vdot(loc, M @ loc).real)
                Pcore = Xcore = 0.0
                for x, y, z in product(range(cfg.L), repeat=3):
                    if in_ball(x, y, z, c, cfg.L, cfg.core_radius):
                        Pcore += dens[x, y, z]
                        Xcore += chiT[x, y, z]
                row.update({
                    "Pcore": Pcore,
                    "t_core": Xcore / (Pcore + 1e-12),
                    "QT": float(np.sum(chiT)),
                    "IPR": float(np.sum(dens**2)),
                    "class": "single_defect",
                })
            rows.append(row)
        del H, evecs
    df = pd.DataFrame(rows)
    path = f"{BASE_DIR}/tables/L{cfg.L}_single_scan.csv"
    df.to_csv(path, index=False)
    print("Saved", path)
    return df

df_single = run_single_L12(CFG)
print(df_single[df_single["accepted"]==True][
    ["config","mode","abs_lambda","rel_residual","QT","Pcore","t_core","IPR"]
].to_string(index=False))
```

---

## Comparison table to fill after Colab run

| Quantity | L=10 single | L=10 pair d=3 | L=12 pair (done) | L=12 single (todo) |
|----------|-------------|---------------|------------------|---------------------|
| Softest \|λ\| | 0.00050 | 0.00139 | 0.00007 (d=6) | ? |
| QT | −0.84 | −0.83 | −0.73…−0.85 | ? |
| Core share | P~0.01 | P1≈P2~0.03–0.04 | P1≈P2 when molecular | Pcore only |
| ST / t | t<0 | ST=1 | ST=1 always | t_core ? |
| BT | n/a | ~1e-4 | up to ~3e-4 | n/a |

**Expected if no mistake:** H and AH nearly identical; QT strongly negative; Pcore modest; softest single comparable order to pair soft modes.

---

## Identity conclusion template (after single results)

If QT(single) ≈ QT(pair) and t_core < 0:
> Texture anti-alignment is **defect-local** at L=12, as at L=10.

If pair still shows P1≈P2 + BT peak while single has only one core:
> **Pair identity** remains spatial (sharing + bridge), not QT alone.

---

## Compact statement

L=12 pair soft modes are residual-validated. Single-defect control at L=12 is the next identity check; run on Colab with the residual gate. Sandbox cannot host N=13824 solves.
