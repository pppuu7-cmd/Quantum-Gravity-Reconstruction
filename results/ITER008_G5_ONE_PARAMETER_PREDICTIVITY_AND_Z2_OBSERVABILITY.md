# QGR Iter008 G5 — one-parameter predictivity and Z2 observability

Date: 2026-09-12
Status: `PASS_SCOPED_ONE_CONTINUOUS_LOCAL_PARAMETER / PARAMETER_FREE_RELATIVE_PREDICTIONS / Z2_LOCALLY_INVISIBLE_GLOBALLY_DISTINGUISHABLE`

GitHub Actions run `34662193575`: five lanes + aggregate `SUCCESS`.

## One continuous local microscopic parameter

After continuum gravitational normalization and a specified preparation/readout are fixed, define the normalization-invariant positive microscopic scale combination

`Gamma = h^2/ell_Q^2 = c_geom g`,

with `ell_Q^2=hbar/a_cont`.

In the frozen QGR convention `|c_geom|=1/2`, but separate values of `c_geom` and `g` depend on action normalization convention. `Gamma` is the appropriate local phenomenological parameter.

The leading specified-preparation history loss has the structure

`Delta_prep = C_prep Gamma^2 (ell_Q^2 R_eff)^2 + ...`.

No additional free phenomenological history/noise coefficient is introduced by the derived leading channel.

Classification:
`PASS_SCOPED_LOCAL_BROADBAND_PHENOMENOLOGY_REDUCES_TO_ONE_CONTINUOUS_MICROSCOPIC_SCALE_PARAMETER_AFTER_CONTINUUM_GRAVITY_AND_PREPARATION_ARE_FIXED`.

## Parameter-free relative prediction

For the two exact G6F normalized packet profiles,

`A0(gamma_L)=2/(1+gamma_L)`,

`A1(gamma_L)=4(2+gamma_L)/(3(1+gamma_L)^2)`.

Writing `gamma_L=1+epsilon`,

`1-A0 = epsilon/2 + O(epsilon^2)`,

`1-A1 = 2 epsilon/3 + O(epsilon^2)`.

Therefore the common microscopic scale cancels and

`(1-A1)/(1-A0) -> 4/3`.

This is exactly consistent with the previous fine-refinement numerical ratio `1.333333315328487`.

Classification:
`PASS_SCOPED_PARAMETER_FREE_RELATIVE_PACKET_PREDICTION_SURVIVES_THE_UNFIXED_MICROSCOPIC_SCALE__LEADING_M1_TO_M0_LOSS_RATIO_EQUALS_FOUR_THIRDS`.

This is a prediction for this specified comparison, not a universal coefficient across arbitrary experimental preparations.

## Direct falsifiability / conditional bound

Any future upper bound

`Delta_prep <= delta_max`

with known positive `C_prep` and nonzero `X=ell_Q^2 R_eff` implies

`Gamma <= sqrt(delta_max/C_prep)/|X|`.

In the frozen `|c_geom|=1/2` convention this corresponds algebraically to `|g|<=2 Gamma`.

Thus leaving `Gamma` free does not make the theory unfalsifiable. One absolute measurement estimates/bounds the single parameter, while additional specified preparations/readouts supply correlated tests and scale-free ratios.

Classification:
`PASS_SCOPED_UNFIXED_MICROSCOPIC_NORMALIZATION_IS_DIRECTLY_BOUNDABLE_BY_ANY_FUTURE_ABSOLUTE_BROADBAND_LIMIT_WITHOUT_SETTING_G_BY_CONVENTION`.

## Local invisibility of the Z2 sector

The symmetric seed

`E=C^-1=-I+J/3`

has eigenvalues

`+1/3,-1,-1,-1`.

By the symmetric-matrix eigenvalue perturbation bound, every perturbation `H` with operator norm

`||H||_2 < 1/3`

keeps signature `(1,3)`. This open norm ball around `E` is convex and contractible.

The two flat `Z2` line-bundle sectors are therefore locally isomorphic on this ball and every contained loop has trivial flat holonomy. Since the refinement-connected construction has `G(h)->E` as `h->0`, the leading local `O(h^4)` broadband asymptotic is insensitive to the global sector.

Classification:
`PASS_SCOPED_LEADING_LOCAL_REFINEMENT_AND_BROADBAND_OBSERVABLES_ARE_Z2_SECTOR_INSENSITIVE_ON_A_CONTRACTIBLE_LORENTZIAN_NEIGHBORHOOD_OF_THE_SEED`.

This result is local/asymptotic and does not declare arbitrary strong-curvature global paths sector-insensitive.

## Explicit global Z2 discriminator

Let

`v(s)=(cos(pi s), sin(pi s),0,0)`, `s in [0,1]`,

and

`G(s)=2 v(s)v(s)^T-I`.

Every `G(s)` has signature `(1,3)`, and

`G(1)=G(0)`.

However the lift of its positive eigenspace line to the `S^3` double cover runs

`v(0)=e0 -> v(1)=-e0`.

Thus this loop is the nontrivial generator of `pi_1(Q_13)=Z2`. The flat quantum holonomy is

- `+1` in the trivial sector;
- `-1` in the twisted sector.

Classification:
`PASS_SCOPED_EXPLICIT_NONCONTRACTIBLE_Q13_LOOP_DISTINGUISHES_THE_TWO_FLAT_QUANTUM_SECTORS_BY_A_GLOBAL_SIGN_HOLONOMY`.

A globally coherent configuration-space interference process winding such a loop could distinguish sectors. The existing local broadband comparator does not.

## Consolidated classification

`PASS_SCOPED_QGR_LOCAL_BROADBAND_SECTOR_IS_ONE_CONTINUOUS_PARAMETER_FALSIFIABLE_AND_HAS_PARAMETER_FREE_RELATIVE_PREDICTIONS__Z2_GLOBAL_SECTOR_IS_LOCALLY_INVISIBLE_BUT_GLOBALLY_DISTINGUISHABLE`.

## Iter008 conclusion

The physical-scale search **does not derive the numerical value of Gamma internally**. Instead it establishes a stricter and more useful boundary:

1. the local model-side phenomenology has one continuous microscopic parameter after continuum gravity is fixed;
2. that parameter is directly boundable/estimable by an absolute measurement;
3. scale-free relative predictions remain available, including the exact `4/3` packet ratio in the specified comparison;
4. the separate global `Z2` sector does not contaminate the leading local refinement observable;
5. the two global sectors are nevertheless physically distinguishable in principle by a noncontractible configuration-space loop.

The next unresolved foundational problem is no longer scale bookkeeping. It is the existence and radiative/refinement stability of the **interacting quantum completion** beyond the already constructed state/BRST/history layer.

Recommended next stage:
`ITER009_INTERACTING_QUANTUM_MEASURE_RADIATIVE_STABILITY_AND_GLOBAL_SECTOR_COMPLETION`.
