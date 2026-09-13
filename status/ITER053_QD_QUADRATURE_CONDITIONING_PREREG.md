# Iter053-QD prospective diagnostic — compact-support quadrature conditioning

Frozen before diagnostic implementation or diagnostic production evidence.

## Gate
`ITER053-QD-COMPACT-SUPPORT-QUADRATURE-CONDITIONING`

## Purpose
Diagnose the numerical/infrastructure failure of Iter053 run `34750610751` without changing, weakening, or reclassifying the frozen Iter053 scientific gate. This is a numerical diagnostic only and cannot produce an Iter053 scientific PASS.

## Frozen hypotheses
1. The Iter053 tensor Gauss-Legendre `n=3/4` rules were scaled to the outer integration box `[-0.32,0.32]^4`, while the perturbation support is only `[-0.24,0.24]^4`.
2. Because the compact bump vanishes identically outside support, the outer-box rule has severe support-node aliasing: `n=3` is expected to retain only the central one-dimensional node, hence `1^4=1` nonzero-support tensor node; `n=4` is expected to retain two one-dimensional nodes, hence `2^4=16` nonzero-support tensor nodes.
3. Since the directional integrand vanishes outside the perturbation support, changing only the quadrature parameterization from the outer box to the support cube is mathematically an integration-domain reduction, not a change of the target action variation.

## Frozen diagnostic panel
Run 8 cheap independent lanes, one for each Iter053 A4+B2+C2 witness seed pair. No H5 bulk assembly is permitted in this diagnostic.

For each lane:
- compute exact Gauss-Legendre abscissae for orders 3, 4, 5, 6 on the outer box and on the support cube;
- count one-dimensional and 4D tensor nodes at which the analytic compact bump is nonzero;
- compute the tensor quadrature of the pure compact bump `B(x)=prod_i (1-(x_i/SUPPORT)^2)^4` on both parameterizations;
- compare with the exact analytic integral `[(256/315)*SUPPORT]^4`, because `int_{-a}^a (1-(x/a)^2)^4 dx = (256/315)a`;
- additionally integrate the cheap direct directional-action density for the lane at epsilon `5e-5` with orders 3/4/5 on both parameterizations. No H5 evaluation and no scientific identity comparison are allowed.

## Frozen outputs
- support-node fractions for every order/domain;
- pure-bump relative quadrature error;
- direct-density outer-box 3->4 change;
- direct-density support-domain 3->4 and 4->5 changes;
- metric signature/inverse controls at sampled direct-density nodes.

## Diagnostic classifier
- `PASS_DIAGNOSTIC_ITER053_OUTER_BOX_QUADRATURE_ALIASING_CONFIRMED` iff: outer-box order-3 nonzero tensor-node count = 1, outer-box order-4 count = 16, and support-domain pure-bump error improves by at least 100x at order 5 relative to outer-box order 4.
- otherwise `DIAGNOSTIC_ITER053_QUADRATURE_ALIASING_NOT_CONFIRMED`.

No result from this diagnostic may alter the historical Iter053 run, fit a coefficient, change `c6`, set `beta=1`, or establish theory correctness. Any replacement scientific gate must be separately preregistered before implementation/production, with its own frozen quadrature design and thresholds.
