# QGR Current Research Front

Updated: 2026-09-15
Primary active front: `ITER057F3 / SOURCE-OWNED G3 ORIGIN WEYL3 DEGREE-2 BLOCK WITH FULL-TENSOR NORMALIZATION`
Project phase: `FULL LOCAL MIXED-ORDER WEYL3 LINEARIZATION / OFF-SHELL OPERATOR RECONSTRUCTION`

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

These blockers are not bypassed by the present classical covariant-symbol work. `kappa` is an existing source-family parameter, not a derived microscopic calibration.

## Established covariant/principal structure

### Iter056X

Durable result `7162882d6a22ad567b8cee0a02868922bf7b0e85`:

`PASS_SCOPED_ITER056X_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFIED__C6_SYMBOLIC_UNFIXED`.

`E_W3^{ab} = (1/2) g^{ab} I3 - P^{(a|cde|} R^{b)}_cde - 2 nabla_mu nabla_nu P^{mu(ab)nu}`,

with exact `nabla_a E^{ab}=0`, `g_ab E^{ab}=-I3`, generic off-shell metric differential order four, and the corrected Iter052 `-2D` sign.

### Iter056Y/Z

- Iter056Y `8368407bcf7b379fa2040b88f7a8fc3b3b4e3501`: non-null Weyl3 `k4` quotient rank <=5 on a six-dimensional diffeomorphism quotient; mixed-order analysis is mandatory.
- Iter056Z `d3d167bb1ba7211ca3009d8dc59f2b771e9e6416`: for `k^2!=0`, the Einstein `k2` quotient symbol is rank six and complements all nonzero Weyl3 high-order-null quotient directions.

Neither result is a hyperbolicity theorem.

## Null-cone two-block chain

### Iter057A — immutable SCIENTIFIC_FAIL

Durable result `024a7e1f99366c8598b7a44ae9393009c1eddeab`.
Run `34904311442`; artifact digest `sha256:95fd17b39e49bd05b3bba938bd3dda41690a93b3a4f019a09b715c7ab6f2b182`.

`SCIENTIFIC_FAIL_ITER057A_COMMON_NULL_CONE_KERNEL_HYPOTHESIS_ON_FROZEN_PANEL`.

On 12 exact Weyl backgrounds x 2 null covectors, the common full kernel of Einstein `M2` and Weyl3 `M4` has dimension five = four gauge directions + one non-gauge class, not two non-gauge common classes.

### Iter057B — immutable PARTIAL

`PARTIAL_SCOPED_ITER057B_GENERIC_NONZERO_MULTIPLIER_RANK5_ALL_NONZERO_NOT_CERTIFIED`.

Generic symbolic rank five was established, but its frozen single-monomial-minor all-nonzero certificate was not met.

### Iter057C — maximum PASS

Durable result `15d2f5a4b573b066150bd3609331bf9220c98b83`.
Run `34904958249`; artifact digest `sha256:c49d92b05854b03b28ac0c9fd6c989a9a6166eb893b1384f5107cbb79b8c1317`.

`PASS_SCOPED_ITER057C_TWO_BLOCK_NULL_CONE_PENCIL_RANK5_FOR_ALL_NONZERO_SYMBOLIC_MULTIPLIERS_ON_FROZEN_PANEL`.

After quotienting the exact five-dimensional common kernel, all 252 reduced maximal minors were reconstructed/verified exactly. Their gcd is exactly `lambda` in all 24 cases, proving

`rank(M2 + lambda M4)=5` for every `lambda != 0`

on the frozen **two-block** panel.

## Source-owned lower-degree bridge

### Iter057D

Durable result `e0f305be490a979f9c0dfa626a8e4e4e2f47fb3f`:

`PASS_SCOPED_ITER057D_G3_SOURCE_OWNED_WEYL_ACTIVE_BACKGROUND_JET_SUFFICIENT_FOR_FULL_LOCAL_WEYL3_LINEARIZATION`.

The existing G3/H0 quadratic tidal metric supplies the complete local background jet. In the current principal-curvature convention `I3=-96 kappa^3`; at the origin `Gamma=0`, `nabla C=0`, `nabla P=0`.

### Iter057E

Durable result `02217019d74d40297601a054a272c307893c73ae`:

`PASS_SCOPED_ITER057E_G3_ORIGIN_WEYL3_LINEARIZATION_HAS_ONLY_K4_K2_K0_BLOCKS__K2_CONSTRUCTION_REQUIRED`.

Exact inversion symmetry plus naturality gives

`L_W3(k)=L4(k)+L2(k)+L0`, with `L3=L1=0`.

## Exact normalization correction discovered before authoritative L2 production

The full unrestricted tensor scalar used by Iter051B1/Iter056X and the six-dimensional independent-bivector scalar used by Iter054C differ by the exact representation factor

**`I3_full = 8 tr(W^3)`.**

Durable analytic bridge: `725c1e180641e05bc5701ccbb193bd34168e8dd2`.

Consequences:

- full-EOM fourth-order bilinear target is `L4_full = 8 Q_Iter054C`;
- full-EOM trace-Ward degree-two target is `T_full = 8 T_bivector`.

This factor is exact antisymmetric-pair index counting, not an empirical fit. Rank/nullspace results of Iter054C/Iter057A-C are unchanged by the nonzero scale factor.

## Historical Iter057F / F2 / G controls

### Iter057F

Prereg `8df569f7414a9d634b72e54264b529245b356288`, run `34905773224`.

Its frozen direct control `L4=Q_Iter054C` is incorrectly normalized. Basis lane 8 also exposed an ill-posed relative-to-zero column control. Historical Iter057F remains INVALID under its own immutable contract; its raw measurements may be diagnostic only.

### Iter057G

Original pre-output trace target was invalidated by `57f4a2a478b3bf909a4091b089cd84bc04701c15` before consuming any L2 trace outputs. Correct full target is

`T_full = (-48,96,0,0,-48,0,0,-144,0,144)/625`

in basis order `(00,01,02,03,11,12,13,22,23,33)`.

### Iter057F2

Preproduction control invalidation: `00462929e746331767bdf3445ad3c6e9e10ee46c`.

Its cache-equivalence job is still useful implementation evidence: the memoized five-point evaluator reproduced original `assemble_minus5` exactly (`relative=0`, `max_abs=0`; artifact `10373670286`). But F2 scientific controls inherited both old normalization errors and cannot establish PASS.

## Active Iter057F3 — authoritative corrected extraction

Preregistration: `bf64df5b213ca9977d2709c7b7fea8cab96ad688`.
Implementation: `4d5e72b0a50ffe54a85df012de219e840580cbdb`.
Production head/workflow: `9b1a6779d4e2893e59a83a86ef543080afa1db5a`.
Run: `34907701856`.

Scientific panel is unchanged from Iter057F:

- G3/H0 origin, `kappa=0.08`;
- null `k=(1,1,0,0)`;
- ten symmetric metric basis lanes;
- frequencies `0,1,2`, held-out `3/2`;
- epsilon `2e-4,1e-4`;
- five-point D5 stencil `1e-3,5e-4`;
- full corrected Euler evaluator `A+I-2 sqrt(-g)D5`;
- extracted `R(s)=L0+s^2L2+s^4L4`.

Corrected frozen controls now use:

- exact no-fit `8Q` for all nonzero `L4` columns;
- global-scale absolute control for the unique exact-zero Q column 8;
- exact no-fit full-tensor trace target `8T`;
- no invalid isolated subprincipal gauge-null predicate.

Maximum PASS:

`PASS_SCOPED_ITER057F3_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_FULL_TENSOR_NORMALIZATION`.

## Iter057H — on-shell interpretation lock

Durable result `dc8aa5f3f111df1c668e0a25c05313d762305fd8`:

`PASS_SCOPED_ITER057H_G3_H0_IS_OFFSHELL_FOR_NONZERO_C6_EINSTEIN_WEYL3_TRUNCATION__ONSHELL_BACKGROUND_REQUIRED_FOR_PHYSICAL_CHARACTERISTICS`.

At the G3/H0 origin, `G_ab=0` but `g_ab E_W3^{ab}=-I3=96 kappa^3`, so for nonzero `c6,kappa` the trace of the exact two-operator `Einstein+c6 Weyl3` field equation cannot vanish.

Therefore G3/H0 is authorized for **off-shell operator reconstruction**, but no local pencil on it may be promoted to physical characteristic/mode/hyperbolicity structure of the exact equations without a separately authorized on-shell or perturbatively corrected background.

## Next-dependency lock

1. Consume fresh Iter057F3 production under the exact full-tensor normalization.
2. If F3 passes, preserve the extracted `L2_Weyl3` as a scoped off-shell operator certificate and analyze its algebraic structure.
3. Do **not** promote a G3 mixed pencil to physical characteristics. Before physical hyperbolicity/mode claims, construct or source-authorize an on-shell Weyl-active background (or controlled perturbative background correction) for the selected classical truncation.
4. Keep `c6` symbolic/unfixed and all microscopic/quantum claim locks intact.

Green CI alone is never scientific PASS.
