# QGR Current Research Front

Updated: 2026-09-15
Primary active front: `ITER057F / SOURCE-OWNED G3 ORIGIN WEYL3 DEGREE-2 BLOCK EXTRACTION`
Project phase: `FULL LOCAL MIXED-ORDER WEYL3 LINEARIZATION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- No experimental confirmation.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; running/fitting not authorized.
- Existing QGR authority contains no physical Weyl3 treatment selector.
- Strong hyperbolicity of the exact full higher-derivative theory is not established.
- Global interacting measure/regulator removal remains blocked.
- Finite/refinement, local-symbol and symmetry-reduced certificates are not global theorems.
- Classical consistency is not quantum consistency/unitarity.
- KMQGB `NEW_REQUIRED` is not authorized.

## Persistent microscopic bridge blockers

- Iter056V remains `BLOCKED_OBJECT_DEFINITION_ITER056V_ABSOLUTE_MICRO_TO_TIDAL_AMPLITUDE_MAP_REMAINS_UNFIXED`.
- Iter056W remains `BLOCKED_OBJECT_DEFINITION_ITER056W_BALANCED_PAIR_TENSOR_HAS_NO_SOURCE_OWNED_PARENT_CHILD_REFINEMENT_RULE`.

These blockers are not bypassed by the current classical covariant-symbol work. `kappa` is an existing source-family parameter, not a derived microscopic calibration.

## Iter056X — terminal covariant variation PASS

Durable result: `7162882d6a22ad567b8cee0a02868922bf7b0e85`.

Classification:

`PASS_SCOPED_ITER056X_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFIED__C6_SYMBOLIC_UNFIXED`.

For covariant metric variation `delta g_ab=h_ab`, the explicit bulk response is

`E_W3^{ab} = (1/2) g^{ab} I3 - P^{(a|cde|} R^{b)}_cde - 2 nabla_mu nabla_nu P^{mu(ab)nu}`,

with the Iter052-authoritative boundary-current/sign convention. Exact controls include

- `nabla_a E_W3^{ab}=0`;
- `g_ab E_W3^{ab}=-I3`;
- generic off-shell metric differential order four, not six;
- conformally-flat null and constant-rescaling controls.

## Iter056Y/Z — exact mixed-order structure off the null cone

### Iter056Y

Durable result: `8368407bcf7b379fa2040b88f7a8fc3b3b4e3501`.

`PASS_SCOPED_ITER056Y_WEYL3_K4_SYMBOL_RANK_BOUND_FORCES_MIXED_ORDER_PHYSICAL_QUOTIENT_ANALYSIS`.

For every non-null covector, the pure Weyl3 `k4` symbol descends to the six-dimensional local diffeomorphism quotient but has rank at most five. At least one non-gauge quotient direction is necessarily high-order-null.

### Iter056Z

Durable result: `d3d167bb1ba7211ca3009d8dc59f2b771e9e6416`.

`PASS_SCOPED_ITER056Z_EINSTEIN_K2_SYMBOL_COMPLEMENTS_WEYL3_K4_QUOTIENT_KERNEL_FOR_NONNULL_COVECTORS`.

For `k^2 != 0`, de Donder gives an exact quotient cross-section and the Einstein `k2` symbol is rank six there. Hence every nonzero Weyl3 high-order quotient-kernel direction is controlled by the Einstein lower-order block away from the null cone.

Neither result is a hyperbolicity theorem.

## Iter057A/B/C — exact null-cone two-block chain

### Iter057A — immutable SCIENTIFIC_FAIL

Durable result: `024a7e1f99366c8598b7a44ae9393009c1eddeab`.
Authoritative run `34904311442`, job `104177299559`, artifact `10372565865`, digest `sha256:95fd17b39e49bd05b3bba938bd3dda41690a93b3a4f019a09b715c7ab6f2b182`.

Classification:

`SCIENTIFIC_FAIL_ITER057A_COMMON_NULL_CONE_KERNEL_HYPOTHESIS_ON_FROZEN_PANEL`.

Across 12 exact rational Weyl backgrounds x 2 exact null covectors, both `M2_Einstein` and `M4_Weyl3` have rank four/nullity six, but their full common kernel has dimension five = four gauge directions + only one non-gauge class. The hypothesis that both GR non-gauge null classes are also Weyl3-null is false on the frozen panel.

### Iter057B — immutable PARTIAL

Classification:

`PARTIAL_SCOPED_ITER057B_GENERIC_NONZERO_MULTIPLIER_RANK5_ALL_NONZERO_NOT_CERTIFIED`.

The symbolic two-block pencil `M2+lambda M4` has generic rank five in all 24 cases, but the preregistered single-monomial-minor certificate was not obtained. This result is not rewritten after the later stronger gate.

### Iter057C — terminal maximum PASS

Durable result: `15d2f5a4b573b066150bd3609331bf9220c98b83`.
Authoritative run `34904958249`, job `104179352990`, artifact `10371802534`, digest `sha256:c49d92b05854b03b28ac0c9fd6c989a9a6166eb893b1384f5107cbb79b8c1317`.

Classification:

`PASS_SCOPED_ITER057C_TWO_BLOCK_NULL_CONE_PENCIL_RANK5_FOR_ALL_NONZERO_SYMBOLIC_MULTIPLIERS_ON_FROZEN_PANEL`.

After quotienting the exact five-dimensional common kernel, all 252 reduced maximal minors were reconstructed/verified exactly. In all 24 cases their polynomial gcd is exactly `lambda`. Therefore

`rank(M2 + lambda M4)=5` for every `lambda != 0`

on the frozen **two-block** panel.

This is not yet the full characteristic operator because lower-degree Weyl3 blocks were absent.

## Iter057D/E — source-owned lower-degree bridge

### Iter057D

Durable result: `e0f305be490a979f9c0dfa626a8e4e4e2f47fb3f`.

`PASS_SCOPED_ITER057D_G3_SOURCE_OWNED_WEYL_ACTIVE_BACKGROUND_JET_SUFFICIENT_FOR_FULL_LOCAL_WEYL3_LINEARIZATION`.

The existing G3/H0 quadratic tidal metric supplies the complete local background jet at the origin. In the current principal-curvature convention the source is Weyl-active with exact `I3=-96 kappa^3`. The source is inversion-even, so `Gamma(0)=0`, `nabla C(0)=0`, `nabla P(0)=0`; higher required coefficient derivatives are uniquely determined by the same analytic metric. The cubic-sign convention was adversarially corrected before terminalization.

### Iter057E

Durable result: `02217019d74d40297601a054a272c307893c73ae`.

`PASS_SCOPED_ITER057E_G3_ORIGIN_WEYL3_LINEARIZATION_HAS_ONLY_K4_K2_K0_BLOCKS__K2_CONSTRUCTION_REQUIRED`.

Exact inversion symmetry plus naturality implies

`L_W3(k)=L4(k)+L2(k)+L0`,

with `L3=L1=0` at the G3 origin. `L4` is the existing Iter054C Weyl3 principal block. The missing object is now sharply localized to the source-faithful `L2_Weyl3` block.

## Active gate — Iter057F

Gate:

`ITER057F-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-EXTRACTION`.

Prospective preregistration: `8df569f7414a9d634b72e54264b529245b356288`.
Implementation: `15b77a71280aa755601a7c5fd20253ed723650a0`.
Production head/workflow: `e7c74847184e826ed3331c107b2a9ad54b2dab90`.
Authoritative run currently active: `34905773224`.

Frozen source:

- G3/H0 origin, `kappa=0.08`;
- exact convention translation to `(-,+,+,+)` for reuse of the corrected Iter051C/Iter054C machinery;
- null covector `k=(1,1,0,0)`;
- ten independent symmetric-metric basis lanes.

Each lane linearizes the **full corrected** Weyl3 Euler evaluator (`A+I-2 sqrt(-g)D5`) under a cosine plane-wave perturbation and extracts

`R(s)=L0+s^2 L2+s^4 L4`

from frozen frequencies `s=0,1,2`, with held-out `s=3/2`.

Critical preregistered controls include:

- perturbation-amplitude and five-point-stencil convergence;
- held-out frequency prediction;
- direct no-fit comparison of extracted `L4` against the exact Iter054C Hessian column;
- aggregate `L4` symmetry/exact-Q control;
- four pure-gauge `L2` null controls.

Maximum PASS:

`PASS_SCOPED_ITER057F_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_K4_CONTROL`.

Any convention/extraction/control failure is `INVALID_ITER057F_FULL_EOM_EXTRACTION_OR_CONVENTION_CONTROL`; no empirical rescaling/sign repair is allowed after output.

## Next-dependency lock

Do not infer a full characteristic cone from Iter057C alone. First consume Iter057F and establish or invalidate the source-faithful `L2_Weyl3` block. Only after a valid `L2` extraction may the full local mixed-degree pencil

`M2_Einstein + c6 L2_Weyl3 + c6 L4_Weyl3`

be prospectively audited on/near the null cone.

Green CI alone can never establish scientific PASS.
