# D5 canonical-lattice cache performance audit

Date: 2026-09-14

Status: outcome-independent implementation/performance analysis. **Not a scientific gate and not authorization to modify any active frozen run.**

## Target

The current `code/qgr_iter051c_d2n_near_null.py` evaluates the double-divergence term through nested five-point first derivatives:

`direct_D5 -> derivative5(first_div5) -> first_div5 -> derivative5(p_actual)`.

The active Iter053T productions must remain untouched. This note identifies an exact-stencil optimization for later prospectively frozen gates.

## Current evaluation count

For one `direct_D5(metric,x,h)`:

1. `R0 = first_div5(metric,x,h)` evaluates one center `P0` plus four axes x four nonzero five-point offsets = `1+16=17` expensive P/Weyl evaluations.
2. The outer derivative runs over four axes and four offsets (`+2,+1,-1,-2`), so it evaluates `first_div5` at `16` more centers.
3. Each of those 16 centers again evaluates one `P0` and 16 inner `p_actual` samples.

Thus `direct_D5` requests

`17 centers * (1 center P + 16 inner P samples) = 289`

P/Weyl evaluations before considering the separate `P` already computed by `assemble_minus5` at the original point. `assemble_minus5` therefore requests about **290** P evaluations per H5 evaluation, with extensive duplication.

## Exact unique stencil lattice

Represent every sample point as

`x + h n`, `n in Z^4`.

The nested five-point stencil needs only points with at most two nonzero integer components.

### Same-axis combinations

When outer and inner derivative axes coincide, the summed offset lies in `-4,...,+4`. Across four coordinate axes this gives

- the origin: 1 point;
- nonzero one-axis offsets `+/-1,...,+/-4`: `4 axes * 8 = 32` points.

Total same-axis/center set: **33**.

### Distinct-axis combinations

Choose an unordered pair of axes: `C(4,2)=6`.
For each pair, each nonzero component independently takes one of `{-2,-1,+1,+2}`, giving `4*4=16` points per pair.

Total two-axis set:

`6*16 = 96`.

Therefore the complete canonical nested-stencil P-sample set contains exactly

`33 + 96 = 129`

unique lattice points.

The separate `assemble_minus5` P at `x` is already the origin in this set.

## Exact reuse opportunity

A future implementation can evaluate and cache the projected `P_actual` object once for each canonical integer lattice offset, then have both inner and outer stencil algebra read from this immutable cache.

Expensive P/Weyl evaluations can therefore drop from about

`290 -> 129`

per H5 evaluation, an ideal call-count reduction factor

`290/129 ≈ 2.248`.

This does not yet count possible reuse of geometry/connection data at the 17 outer centers, so additional safe optimization may exist.

## Why the current long jobs are expensive

One GJ3 side has `3^4=81` quadrature nodes. A C covariance lane evaluates both base and transformed sides, hence 162 H5 evaluations at a fixed hstep/order.

At the current call structure this is approximately

`162 * 290 = 46,980`

expensive P/Weyl requests for one C GJ3 lane, before other geometry/control work.

The six-lane hstep companion therefore exposes a raw scale of roughly

`6 * 46,980 = 281,880`

P/Weyl requests.

This explains why node-level Actions sharding plus exact lattice caching are complementary rather than redundant optimizations.

## Numerical-identity firewall

Although the algebraic stencil is identical, a cache refactor can alter floating-point operation paths if coordinates that are mathematically the same are constructed by different addition orders. Therefore future scientific adoption must not assume bitwise identity.

Before using the cache in an authoritative gate, prospectively freeze a non-scientific equivalence control that:

1. constructs cache keys from canonical integer lattice offsets, not rounded arbitrary coordinates;
2. evaluates coordinates in one frozen canonical expression `x + h*n`;
3. compares historical and cached `direct_D5` on frozen representative metric/point/h panels;
4. scores H/D tensors with a machine-roundoff-scale tolerance frozen before execution;
5. retains a deliberately corrupted offset/cache negative control;
6. verifies signature/inverse controls at all required lattice points;
7. rejects mixed code/input identities.

Only after this equivalence control may a later scientific preregistration choose the cached implementation prospectively.

## Interaction with deterministic GitHub sharding

The cache is local to one quadrature node. It composes cleanly with `analysis/POST_ITER053_PARALLEL_FULL_REPLACEMENT_ARCHITECTURE.md`:

- outer parallelism: independent quadrature-node shards across GitHub runners;
- inner optimization: 129-point canonical D5 lattice cache inside each H5 node;
- deterministic reducer: reconstruct the unchanged scientific integral in canonical node order.

Neither optimization changes seeds, quadrature orders, hsteps, thresholds, object identity or the scientific lane graph when prospectively adopted.

## Claim ceiling

No active result is accelerated or modified by this note. No Iter053T classification follows. No physical QGR claim follows. This is a future reproducibility/performance optimization only.