# QGR Current Research Front

Updated: 2026-09-15
Primary active front: `ITER057N / G3 ZERO-ORDER EINSTEIN SEED NEIGHBORHOOD AUDIT`
Project phase: `ONSHELL BACKGROUND SEED CONSISTENCY PROGRAMME`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- No experimental confirmation.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; running/fitting not authorized.
- No physical Weyl3 treatment selector, strong hyperbolicity, ghost/stability, quantum unitarity, regulator removal or UV completion is established.
- Finite local Taylor/symbol certificates are not open-neighborhood/global theorems.

## Newly consumed authority

### Iter057J coefficient correction

Iter057J remains terminal scientific FAIL for the **conformal continuation candidate only**. The historical result commit is preserved, but its witness coefficient has been superseded by exact audit `dd3d2ec07b3dbb3828331afd2502667a5e3ffbc8`:

`A_E K_0011 = -8 kappa^4`,

and at `kappa=2/25`,

`A_E K_0011 = -128/390625 != 0`.

The scoped scientific FAIL is unchanged.

### Iter057M terminal PASS

Preregistration: `9760ca0324dce13cf141a9f93b6ff69ea4c75605`.
Exact derivation: `443d52b759232addf580cb70d7f6b5fedcce9519`.
Terminal result: `f947efac35e5093ec536ee9da52e86de23325d72`.
Classification:

`PASS_SCOPED_ITER057M_GENERAL_QAB_QUARTIC_JET_EXTENDS_THROUGH_SECOND_EVEN_SOURCE_ORDER__OPEN_NEIGHBORHOOD_NOT_ESTABLISHED`.

Consumed exact production evidence includes:

- source-component equivalence Actions run `34954206549`, artifact `10390318470`, digest `sha256:ab331b2093e7d26e1d5f609f08e81c70739bb79d88a9a210a73ffc5b8155cd92`;
- Q4/unreduced-control Actions run `34954412091`, artifact `10390657547`, digest `sha256:78aca057d3fd2ef4db1d7e746e188c625a02eda14c41c902fcee642bf886208c`;
- exact matrix `180 x 350`, rank `164`, homogeneous Q4 nullity `186`;
- all 16 canonical Noether compatibility contractions exactly zero;
- one exact particular Q4 with 32 nonzero normalized coefficients;
- de Donder vector identically zero through cubic coordinate order;
- all ten unreduced `DG_ab-S_ab` components identically zero through quadratic coordinate order.

Iter057M remains a finite local Taylor certificate only.

Historical Iter057K remains terminal technical BLOCKED; its old exact-lineage replay is still useful only as an additional independent cross-check. Two of its four diagonal replay lanes have already independently confirmed the corrected source-component sign.

## Active Iter057N gate

Preregistration: `ebaead95ba38dc4521b57477c54bf7d4f1b11c83`.
Gate: `ITER057N-G3-ZERO-ORDER-EINSTEIN-SEED-NEIGHBORHOOD-AUDIT`.
Implementation: `842d50cc3e5b471d4a2565321b0c86d570b7ad52`.
Workflow head: `c38a7c3c8f88cfcdef8cfe9ab38340acf37992cc`.
Actions run: `34954958651`.
Terminal classification: none yet.

## Why this gate precedes Q6

The first-order expansion

`g = g0 + c6 q + O(c6^2)`

can describe an open-neighborhood solution only if the fixed seed `g0` already satisfies its own `c6^0` Einstein equation to the same local order. Iter057L/M solve the `O(c6)` coefficient equation; they cannot cancel an `O(c6^0)` seed residual without introducing forbidden inverse powers of `c6`.

The G3/H0 source is exactly Ricci-flat at the frozen origin, but its exact metric is only a weak-static tidal construction. Nonlinear inverse/connection terms may generate an Einstein residual at quadratic coordinate order.

Iter057N therefore computes exact `R_ab`, `R` and `G_ab` through degree two, preserves the origin controls, checks contracted Bianchi/trace identities, and includes a direct full-rational component factorization as an independent exact cross-check.

## Consequence boundary

If all exact quadratic Einstein coefficients vanish, the fixed seed survives this finite-order check and higher seed orders remain open.

If any exact coefficient is nonzero, the preregistered outcome is a scoped scientific FAIL of the **fixed G3 seed as the c6^0 neighborhood background**. This does not invalidate G3 as a local operator probe or invalidate Iter057L/M finite-jet algebra.

The correct successor in that case is a separate `c6^0` Einstein-seed completion. A quartic seed correction can preserve the origin metric/connection/curvature while modifying the degree-two Einstein residual. Because such a quartic correction also changes fourth metric derivatives, the Weyl3 Euler source must then be recomputed on the corrected seed; the old G3 `E_W3` jet may not be carried over automatically.

## Next bounded step

Consume Actions run `34954958651` strictly under preregistration `ebaead95...`.

Do not:

- absorb a `c6^0` Einstein residual into the `O(c6)` correction;
- fit or fix `c6`;
- add matter/cosmological/additional operators to rescue the frozen gate;
- infer an open-neighborhood solution from the existing finite local Q2/Q4 certificates;
- reuse the old Weyl3 source unchanged after any future quartic Einstein-seed completion without recomputing its fourth-derivative-dependent Euler tensor.
