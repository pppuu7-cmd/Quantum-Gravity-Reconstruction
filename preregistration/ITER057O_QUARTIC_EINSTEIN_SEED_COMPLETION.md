# Iter057O preregistration — quartic c6^0 Einstein-seed completion

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057O-QUARTIC-EINSTEIN-SEED-COMPLETION`
Parent authority: Iter057N terminal scientific FAIL `32c6f1b077d72a616f52dc41bbef8a39ba0cf1af`.

## Question

Can the exact source-owned G3/H0 metric be completed by an unrestricted quartic **zeroth-order** metric jet so that the corrected seed satisfies the vacuum Einstein equation through coordinate degree two while preserving the frozen origin metric, connection and curvature?

This is a `c6^0` seed-construction gate. It is not an `O(c6)` Weyl3 correction and may not use or tune `c6`.

## Frozen expansion

Let

`g_seed = g_G3 + r^(4) + O(|x|^6)`

with `r^(4)_ab` an unrestricted symmetric quartic polynomial. Use trace-reversed quartic coefficients

`rbar_ab = (1/24) R4_ab,cdef x^c x^d x^e x^f`,

where `(ab)` is symmetric and `(cdef)` is completely symmetric.

Because `r^(4)` starts at coordinate degree four,

`r^(4)(0)=0`, `partial r^(4)(0)=0`, `partial^2 r^(4)(0)=0`.

Therefore the corrected seed has exactly the same origin metric, connection and Riemann/Weyl tensor as G3/H0.

At coordinate degree two, all interactions between the G3 quadratic perturbation and `r^(4)` are degree four or higher. Hence the effect of `r^(4)` on the degree-two Einstein tensor is exactly the flat-principal linearized Einstein map. This statement must be independently checked by direct substitution into the corrected full metric.

## Frozen target

Use the exact Iter057N residual `G_ab^(2)[g_G3]` from `32c6f1b...` and require

`DG_flat_ab[r^(4)] = - G_ab^(2)[g_G3]`.

No matter, cosmological constant, additional operator, fitted coefficient or modified quadratic source is allowed.

## Frozen obligations

A. **Consume the exact Iter057N target.** Use the full 15-coefficient quadratic Einstein residual and its exact degree-one Bianchi identity, not a restricted subset.

B. **Full quartic generality.** Parameterize all 350 trace-reversed quartic coefficients: 10 symmetric tensor components times 35 symmetric rank-four derivative multi-indices. No conformal, diagonal, static-component, spherical or plane-wave ansatz is allowed.

C. **Gauge control.** Impose the flat de Donder condition on `rbar` through cubic order. Verify that the pre-existing G3 quadratic perturbation already satisfies the corresponding linearized de Donder condition through degree one, so the combined seed is gauge-controlled through the frozen orders.

D. **Exact solve and compatibility.** Assemble the full exact gauge+Einstein coefficient system. Account for the complete Bianchi left-nullspace before deciding consistency. Numerical rank/tolerance may not decide exact solvability.

E. **Origin-data preservation.** Verify exactly that the quartic correction and its first two derivatives vanish at the origin, so `g`, `Gamma`, `Riemann` and the electric Weyl eigenvalues there are unchanged.

F. **Independent full-metric control.** Substitute one exact unrestricted solution into the corrected metric `g_G3+r^(4)` and recompute the nonlinear Einstein tensor directly. All coordinate-degree-two coefficients must vanish exactly. Reduced/linearized self-consistency alone is insufficient.

G. **Weyl3 source reset lock.** Do not infer that `E_W3[g_seed](0)` equals the old G3/H0 value. Record explicitly that the quartic seed changes fourth metric derivatives and therefore requires a fresh exact Weyl3 Euler evaluation before any successor `O(c6)` correction is consumed.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057O_QUARTIC_EINSTEIN_SEED_COMPLETES_G3_THROUGH_QUADRATIC_ORDER__WEYL3_SOURCE_MUST_BE_RECOMPUTED`

iff an exact unrestricted quartic correction exists and obligations A-G pass identically.

Scientific FAIL:

`SCIENTIFIC_FAIL_SCOPED_ITER057O_G3_CURVATURE_PRESERVING_QUARTIC_EINSTEIN_SEED_COMPLETION_INCOMPATIBLE`

only if the full exact coefficient system is inconsistent after gauge freedom and Bianchi identities are accounted for.

BLOCKED:

`BLOCKED_ITER057O_EXACT_QUARTIC_SEED_SYSTEM_NOT_REALIZED`

if the exact system or full-metric control cannot be completed without changing the frozen problem.

INVALID:

`INVALID_ITER057O_RESTRICTION_CONVENTION_OR_EXACTNESS_CONTROL`

if general solvability is inferred from a restricted ansatz, numerical zero/rank is used, `c6` is introduced/fixed, the G3 quadratic source is modified, or the full-metric control fails.

## Scope ceiling

Even a PASS establishes only a curvature-preserving local Einstein-seed completion through coordinate degree two. It does not establish a full Ricci-flat neighborhood, convergence, global boundary conditions, or a solution of Einstein+Weyl3.

A PASS necessarily invalidates automatic reuse of the old G3/H0 `E_W3` source jet: the successor must recompute Weyl3 on the corrected seed before reconstructing the `O(c6)` correction.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`; no experiment, hyperbolicity, ghost, stability, unitarity, regulator-removal or UV-completion claim is authorized.