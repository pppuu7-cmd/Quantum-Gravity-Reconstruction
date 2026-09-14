# Iter056Z preregistration — mixed-order Einstein/Weyl3 quotient-complement certificate

Date: 2026-09-15
Gate: `ITER056Z-MIXED-ORDER-EINSTEIN-WEYL3-QUOTIENT-COMPLEMENT-CERTIFICATE`

## Motivation

Iter056Y proved that for every non-null covector the pure Weyl3 degree-four metric principal symbol descends to a six-dimensional diffeomorphism quotient but has rank at most five there. Hence at least one non-gauge quotient direction is invisible to the `k4` block.

The next exact structural question is whether the ordinary Einstein degree-two principal symbol is necessarily nondegenerate on the same non-null quotient, so that every nonzero Weyl3 high-order-null quotient direction is controlled by the lower-order Einstein block.

## Frozen question

For `k^2 != 0`, construct a canonical six-dimensional representative of the symmetric-metric perturbation quotient by infinitesimal diffeomorphisms using the de Donder functional

`F_b(h)=k^a h_ab - (1/2) k_b h`,

and determine whether the Einstein `k2` principal symbol is an isomorphism on this slice. Then combine the result with Iter056Y without introducing a treatment prescription or a numerical value/sign of `c6`.

## Frozen obligations

A. **Unique quotient slice.** For the pure-gauge direction `G_k(xi)_ab=k_a xi_b+k_b xi_a`, derive the exact transformation law of `F_b` and prove/refute that `F=0` gives a unique representative of every gauge orbit for `k^2 != 0`.

B. **Einstein principal symbol.** Derive the linearized Einstein tensor principal symbol from the same local Riemann convention used by the Weyl3 principal-map chain. Do not import a scalar proxy.

C. **Restriction to the slice.** Reduce the Einstein symbol on `F=0` to its trace-reversal form and prove/refute its rank on the six-dimensional slice for `k^2 != 0`.

D. **Kernel complement.** Combine only after A-C with the Iter056Y exact fact `dim ker sigma4_bar >= 1`. PASS requires proving that every nonzero element of the Weyl3 quotient kernel is acted on nontrivially by the Einstein `k2` symbol.

E. **Conformally-flat control.** Check the special case `Cbar=0`, where the Weyl3 `k4` block vanishes and all quotient directions must reduce to the Einstein second-order principal structure.

F. **PDE interpretation ceiling.** State only the exact mixed-order consequence. Do not infer full-system characteristic roots, strong hyperbolicity, a physical ghost, stability, energy positivity, or a preferred exact/order-reduced treatment.

G. Keep `c6` symbolic/unfixed and preserve all canonical claim locks.

## Frozen classifications

Maximum PASS:

`PASS_SCOPED_ITER056Z_EINSTEIN_K2_SYMBOL_COMPLEMENTS_WEYL3_K4_QUOTIENT_KERNEL_FOR_NONNULL_COVECTORS`.

Scientific FAIL:

`SCIENTIFIC_FAIL_ITER056Z_EINSTEIN_SYMBOL_DOES_NOT_COMPLEMENT_WEYL3_K4_KERNEL`.

INVALID:

`INVALID_ITER056Z_GAUGE_SLICE_OR_PRINCIPAL_CONVENTION_INCOMPLETE`.

## Claim locks

No characteristic/hyperbolicity theorem; no physical mode/ghost count; no exact-vs-order-reduced treatment selection; no fixed/running `c6`; no `beta=1`; no quantum unitarity/UV/full-QG claim. `theory established=0%`.