# Iter057Y terminal result — unrestricted on-shell O(c6) Q2/Q4/Q6/Q8 response

Date: 2026-09-16
Gate: `ITER057Y-ONSHELL-FIRST-ORDER-Q2-Q4-Q6-Q8-RESPONSE`
Preregistration: `e372123b622bd1bb94e641b82097687a29416f65`
Implementation: `98c82292885cec9a38fa400a5e08b1272104f8b8`
Frozen pre-production payload digest: `55dda1ea44f912389bec6e3619b7b7c458853da8`
Canonical Q8 data: `adae8b521958573e74bcbe02678cbfd3a9599687`
Parent response: Iter057V terminal `0d98273f8a1ec6071692571518f4faec1af8fa7b`
Parent background: Iter057W terminal `90b4a8d0512bffa70c488111a71e78690368c009`
Parent source: Iter057X terminal `4ab5592cfc6ef5fb69d3a96fa4433ef22d51af8b`

## Terminal classification

**`PASS_SCOPED_ITER057Y_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_Q8_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_SIXTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN`**

This is exactly the prospectively frozen maximum scoped PASS.

## Reproducibility

The frozen problem was evaluated with exact rational polynomial arithmetic in two implementation layouts: a standalone sparse-Fraction evaluator and the repository-native implementation above. The repository-native implementation was then executed again as a separate process. All executions produced the same ordered 180-coefficient Q8 particular solution and the same scientific controls/ranks.

The canonical scientific payload contains the classification, all frozen controls, exact structural invariants, actual curved residual counts, the complete ordered Q8 coefficient list, and reduced/unreduced replay results. Its canonical sorted compact JSON is exactly 17,737 UTF-8 bytes with

`sha256:2454262caad6a1c298b5de445f7dc4e103ab6a1b3d34d6db881b40cbd32a6062`.

The complete repository-native result JSON hash is

`sha256:de39ea547cbf92c530f30be29e2ec5b904f6d19fe64a12f2ebd3a6b9aed6120f`.

Prospective supplemental GitHub Actions reproductions were launched as Ubuntu run `35039234603` and Windows run `35039244062`. At terminalization both were still queued behind existing repository workloads. They were not used to choose or alter the PASS classification and remain supplemental cross-platform checks.

## Fresh curved residual

The fixed terminal Iter057V `Q2+Q4+Q6` response was replayed on the terminal Iter057W decic background against the terminal Iter057U/Iter057X source. Lower established equations remain exact:

- covariant de Donder through degree 5: zero;
- field equation through degree 4: zero.

The newly computed target layer is nontrivial before Q8 is added:

- degree-7 gauge residual: **79** nonzero normalized slots;
- degree-6 field/source residual: **140** nonzero normalized slots.

Thus the Q8 solve is not a vacuous extension and no historical affine right-hand side was reused.

## Exact unrestricted Q8 complex

The frozen pure degree-eight trace-reversed response contains

`10*C(11,3)=1650`

unknown normalized coefficients. The exact affine complex contains

- 480 degree-7 de Donder rows;
- 840 degree-6 field rows;
- 1320 rows total;
- 5280 nonzero principal-matrix entries.

Exact arithmetic gives

`shape(M)=(1320,1650)`,

`rank(M)=1096`,

`rank([M|r])=1096`,

`left-nullity(M)=224`,

`nullity(M)=554`.

The complete canonical Bianchi family has exact rank 224 and annihilates the principal matrix exactly. All **224/224** affine compatibility contractions with the freshly computed curved residual vanish exactly.

## Exact Q8 solution and independent replay

Setting the 554 homogeneous directions to zero only to select a deterministic particular solution gives **180 nonzero normalized Q8 coefficients**. All homogeneous directions remain mathematically unfixed; the canonical particular solution does not remove that freedom.

The complete ordered coefficient authority, including both the exact coefficient value and `Q8/kappa^6`, is frozen in `data/ITER057Y_CANONICAL_Q8_RESPONSE.json`.

Every affine row vanishes exactly after Q8 is inserted. Pure degree eight preserves all already-fixed Q2/Q4/Q6 coefficients and derivatives through order seven.

Independent full-response checks give

- covariant de Donder through degree 7: exact zero;
- reduced `DG_g[qhat]-Shat` through degree 6: exact zero in all 10 independent components;
- unreduced covariant linearized Ricci/scalar/Einstein `DG_g[qhat]-Shat` through degree 6: exact zero in all 10 independent components.

No floating-point rank, tolerance, finite difference, restricted ansatz, lower-response refit, seed mutation, or historical source substitution is used.

## Consequence

A finite local first-order `O(c6)` response is now explicitly source-matched through coordinate degree six on the canonical decic Einstein seed. The next source coefficient at coordinate degree eight is not yet source-owned: because the Weyl-cubic Euler tensor contains two derivatives of a curvature-quadratic object, that layer can depend on a metric twelve-jet. Therefore the next scientifically admissible gate is the unrestricted pure degree-twelve zeroth-order Einstein-seed completion through Einstein coordinate degree ten.

## Scope ceiling

This PASS establishes only one further finite local Taylor response layer. It does not establish an all-orders or convergent Einstein+Weyl3 solution, an open-neighborhood/global/asymptotic solution, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experimental confirmation, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory established remains `0%`.
