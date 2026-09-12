# QGR Iter008 G4 — interacting clock-gravity scale and global quantization audit

Date: 2026-09-12
Status: `PARTIAL_SCOPED_FROZEN_NORMALIZATION_CLOSED / ABSOLUTE_SCALE_STILL_OPEN / Z2_GLOBAL_SECTOR_EXPOSED`

GitHub Actions run `34661941803`: five lanes + aggregate `SUCCESS`.

## G4-1 — frozen normalization matching

The earlier exact QGR result is

`S2_connection = -2 S2_QGR`.

Using the frozen discrete/continuum coordinate convention `D=h partial` and one coordinate four-cell volume `h^4`,

`kappa sum S2_QGR(Dh) -> (kappa/h^2) integral S2_QGR(partial h)`

while

`a_cont integral L_connection^(2) = -2 a_cont integral S2_QGR(partial h)`.

Thus, in this **frozen repository convention**,

`a_cont = - kappa/(2 h^2)`

and the signed conversion factor is

`c_geom=-1/2`.

This number is convention dependent. If the quadratic basis is rescaled by `alpha`, `c_geom` and `g=kappa/hbar` transform inversely. The invariant content is their product, not the separate statement `c_geom=-1/2`.

Classification:
`PASS_SCOPED_FROZEN_QGR_ACTION_CONVENTION_FIXES_SIGNED_C_GEOM_MINUS_ONE_HALF__ONLY_PRODUCT_C_GEOM_G_IS_NORMALIZATION_INVARIANT`.

## G4-2 — common clock-gravity constraint

For a linear deparametrizing constraint

`C=A P_tau + B C_g = 0`,

overall multiplication of the whole constraint is irrelevant, but the ratio

`r=B/A`

survives. Since the intrinsic clock has fixed unit rank increment, rescaling `tau` to absorb `r` would change the already derived clock normalization.

For a quadratic scalar clock

`C=P_tau^2/(2 Z_tau)+C_g=0`,

deparametrization gives a physical generator proportional to `sqrt(Z_tau)`. Thus the relative clock normalization also survives.

Classification:
`BLOCKED_SCOPED_LINEAR_OR_QUADRATIC_CLOCK_GRAVITY_DEPARAMETRIZATION_RETAINS_ONE_RELATIVE_NORMALIZATION_UNLESS_A_NEW_SAME_REALIZATION_RELATION_IS_DERIVED`.

## G4-3 — two global flat-line-bundle sectors

From G3, `Q_{1,3}~RP^3` and `pi_1=Z2`. Flat `U(1)` line bundles are classified by

`Hom(Z2,U(1))={+1,-1}`.

Therefore there are exactly two flat global quantum sectors:

- trivial holonomy `+1`;
- twisted holonomy `-1` around the noncontractible loop.

The current `H_kin=L^2(Q_13,dmu)` construction uses ordinary scalar functions and therefore realizes the trivial sector. The twisted sector is locally identical on contractible patches. Since `Aut(Z2)` is trivial, covariance of configuration-space maps does not remove the two-sector choice.

Classification:
`PARTIAL_SCOPED_Q13_ADMITS_TWO_FLAT_U1_LINE_BUNDLE_QUANTIZATION_SECTORS__CURRENT_SCALAR_L2_CONSTRUCTION_IS_THE_TRIVIAL_SECTOR_AND_NO_EXISTING_QGR_RULE_SELECTS_IT_UNIQUELY`.

This is a discrete global ambiguity, not a quantization of positive real `g`.

## G4-4 — loop/root-of-unity quantization fails

The regular curved QGR branch admits continuously variable small curvature/holonomy. If one imposed

`exp(i g Phi)=1`

for **every** small loop phase `Phi`, continuity near `Phi=0` forces the integer winding to remain zero. Any allowed nonzero small `Phi` would then force `g=0`.

Thus nonzero `g` cannot be quantized by declaring every physical curvature/history loop phase to be a root of unity. A new discrete curvature-flux spectrum would have to be derived first.

Classification:
`FAIL_SCOPED_ROOT_OF_UNITY_OR_LOOP_SINGLE_VALUEDNESS_CANNOT_QUANTIZE_NONZERO_G_WHILE_QGR_CURVATURE_HOLONOMY_VARIES_CONTINUOUSLY`.

## G4-5 — ordinary dynamical rank clock backreacts

For an ordinary scalar clock with fixed nonzero timelike gradient,

`T_mn=Z_tau (d_m tau d_n tau - 1/2 G_mn (d tau)^2)`

is nonzero for every `Z_tau != 0`. In a normalized flat `+---` frame with `d tau=(1,0,0,0)`,

`T_mn=(Z_tau/2) diag(1,1,1,1)`.

The established active QGR seed is the zero-cosmological flat **vacuum** branch. Therefore promoting rank time to ordinary dynamical scalar matter changes the background unless one takes a probe/zero-coupling limit or adds compensating stress-energy data. Neither route fixes the scale prospectively.

Classification:
`FAIL_SCOPED_ORDINARY_DYNAMICAL_RANK_CLOCK_SCALAR_CANNOT_PRESERVE_THE_ESTABLISHED_ZERO_LAMBDA_FLAT_VACUUM_BRANCH_WITH_NONZERO_KINETIC_NORMALIZATION_WITHOUT_NEW_BACKREACTION_OR_COMPENSATION_DATA`.

## Consolidated classification

`PARTIAL_SCOPED_FROZEN_ACTION_MATCHING_CLOSES_C_GEOM_IN_REPOSITORY_CONVENTION_BUT_INTERACTING_CLOCK_CONSTRAINTS_RETAIN_RELATIVE_NORMALIZATION__Q13_HAS_TWO_UNSELECTED_Z2_GLOBAL_SECTORS__NO_ABSOLUTE_SCALE_FIX`.

## Consequence

The continuous scale freedom has not multiplied: the pure-gravity phenomenological sector still contains one continuous microscopic normalization combination after continuum gravity is fixed. However, a **separate discrete global sector choice** has now been exposed in the quantum configuration-space completion.

The next decisive question is whether:

1. the existing local/broadband observables are insensitive to this `Z2` sector;
2. the one remaining continuous coupling leaves parameter-free relative predictions or falsifiable one-parameter relations;
3. the `Z2` sector can be selected or measured by a genuinely global configuration-space loop.

Next gate:
`QGR-ITER008-G5-ONE-PARAMETER-PREDICTIVITY-AND-Z2-SECTOR-OBSERVABILITY-AUDIT`.
