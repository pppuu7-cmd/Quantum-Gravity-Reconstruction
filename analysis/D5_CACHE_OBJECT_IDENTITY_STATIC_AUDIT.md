# D5 cache object-identity static audit

Date: 2026-09-14

Status: non-scientific code audit supporting the separate D5 cache equivalence matrix. It does not assign that matrix's terminal classification.

## Historical object

`qgr_iter051c_d2n_near_null.py` defines:

- `p_actual(metric,x) = c.P_actual(metric,x)`;
- `derivative5` with coefficients `(-1,8,-8,1)/(12h)` at offsets `(+2,+1,-1,-2)`;
- `first_div5`: center `geometry`, center projected P, four coordinate derivatives of P, then `b0.first_cov(P0,dP,G)` and contraction `aambn->mbn`;
- `direct_D5`: center `geometry`, center first divergence, four outer five-point derivatives of `first_div5`, then the same three Christoffel/connection additions;
- `assemble_minus5`: same center P, algebraic A, lowering insertion I, historical D5, and final `A+I-2 sqrt(-g) D`.

`qgr_iter051c_full_eom.py::P_actual` is exactly

`geometry(metric,x)`
`-> w3.complex_step_gradient(R,g,gi)`
`-> w3.project_algebraic_riemann(...)`.

## Candidate cached object

`qgr_d5_canonical_cache_equivalence.py` computes, for each canonical lattice offset:

`geometry(metric,x+h*n)`
`-> w3.complex_step_gradient(R,g,gi)`
`-> w3.project_algebraic_riemann(...)`.

Thus each cached P entry is the same mathematical/numerical P object as historical `c.P_actual`, evaluated at a canonically constructed coordinate.

`first_div_cached` uses the identical five-point coefficients and the same `b0.first_cov(P0,dP,G)` contraction.

`reduce_cache` uses the identical outer five-point coefficients and the same center connection terms:

`G[m,b,r] R0[r,b,n] + G[b,b,r] R0[m,r,n] + G[n,b,r] R0[m,b,r]`.

It then computes center A and I from the same functions and forms the same final sign:

`H=A+I-2 sqrt(-g) D`.

## Only intended difference

The historical nested implementation recomputes P at duplicated coordinates reached through different outer/inner stencil paths. The candidate implementation stores each unique canonical lattice point once and reuses it.

No derivative coefficient, tensor contraction, connection term, H5 sign, metric seed, coordinate step, curvature construction or P projection is changed.

## Floating-coordinate caveat

Historical mixed-axis coordinates may be assembled as sequential additions, whereas the cache canonicalizes a point as `x+h*n`. These are mathematically identical but need not be bitwise identical in binary floating point. This is precisely why the prospective matrix froze `1e-9` D/H equivalence tolerances rather than requiring bitwise equality.

## Audit verdict

`STATIC_OBJECT_IDENTITY_COMPATIBLE_WITH_EQUIVALENCE_TEST`

This is not the terminal cache classification. The cache may be used in a future scientific gate only if the separate 16-lane aggregate terminally classifies `D5_CANONICAL_CACHE_EQUIVALENCE_PASS` before that gate's final implementation freeze.