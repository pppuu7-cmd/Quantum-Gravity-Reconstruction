# COVARIANT_WEYL3_A7_LOWER_ORDER_COVARIANTIZATION_IBP_LOCALIZATION — implementation decomposition binding

Status: **PROSPECTIVE / FROZEN BEFORE LOWER-ORDER PRODUCTION**
Date: 2026-09-18
Parent preregistration: `a8c7bd1bd5280f18aa50955b4cd847b707c178ab`
Parent A7 terminal authority: `feba733ef0e7d1423be4e38ad5c9c9c8b623a5ea`
Frozen witness: `OFFSHELL_A / d=7`

## Purpose

This binding fixes how the preregistered lower-order classes are operationalized before any lower-order production result exists. It does not alter the preregistered class names, parent discrepancy, witness, sign, normalization, or terminal taxonomy.

The terminal comparator must first inspect the ordered pre-IBP/IBP ledger and stop at the earliest exact disagreement. The additive class vectors are then used as an exact accounting identity for each lane and for the frozen parent discrepancy.

## Researcher lane

The Researcher remains on the frozen direct metric directional-variation lineage and imports only `qgr_covariant_weyl3_researcher` plus the neutral panel generator.

For the scalar-test representation

`delta L[h phi] = F0 phi + sum_i Fi d_i phi + sum_{i<=j} Fij d_i d_j phi`,

freeze:

1. `F0`;
2. ordered `Fi`, `i=0,1,2,3`;
3. ordered ten `Fij` slots `00,01,02,03,11,12,13,22,23,33`;
4. `-sum_i d_i Fi`;
5. `+sum_{i<=j} d_i d_j Fij`;
6. the already frozen volume contribution;
7. the exact final direct bulk.

Researcher additive classes are frozen as:

- `CONNECTION_VARIATION = 0`;
- `COVARIANTIZATION_GAMMA_TIMES_DH = 0`;
- `COVARIANTIZATION_DGAMMA_TIMES_H = 0`;
- `COVARIANTIZATION_GAMMA_GAMMA_TIMES_H = 0`;
- `IBP_FIRST_TRANSFER = -sum_i d_i Fi`;
- `IBP_SECOND_TRANSFER = +sum_{i<=j} d_i d_j Fij`;
- `ALGEBRAIC_CURVATURE_VARIATION = F0 - VOLUME_CONTROL`;
- `VOLUME_CONTROL = frozen direct volume contribution`;
- `PRINCIPAL_CONTROL = 0` as an additive scalar, with the ten frozen principal slots carried separately as a vector control.

Their exact scalar sum must equal the frozen Researcher parent bulk.

## Critic lane: independent P/Palatini reconstruction

The Critic imports only `qgr_covariant_weyl3_critic` plus the neutral panel generator. It must not import the Researcher implementation or read Researcher lower-order values before serialization.

Let

`K^{abcd}(x) = sqrt(-g(x)) P^{abcd}(x)`.

Using the Critic's own exact degree-2 Taylor polynomials for `g`, `P`, and the frozen perturbation jets, independently reconstruct the normal-coordinate scalar-test coefficients from

`K^{abcd} delta R_abcd`

with

`delta R_abcd|x0 = 1/2( d_c d_b H_ad + d_d d_a H_bc - d_c d_a H_bd - d_d d_b H_ac )`,

`H_ab = h_ab phi`.

This yields independent polynomial coefficients `F0_P`, `Fi_P`, `Fij_P`.

Separately compute the exact fixed-R metric variation of `sqrt(-g) I3` with a fresh dual-number metric perturbation `g_ab -> g_ab + eps h_ab`, holding the all-lowered point Riemann tensor fixed. This gives the independent algebraic metric contribution, including the volume term.

Define Critic reconstructed scalar-test coefficients:

- `F0 = fixed_R_metric_density_variation + F0_P`;
- `Fi = Fi_P`;
- `Fij = Fij_P`.

Then freeze the ordinary-density partial-IBP reconstruction:

- `IBP_FIRST_TRANSFER = -sum_i d_i Fi`;
- `IBP_SECOND_TRANSFER = +sum_{i<=j} d_i d_j Fij`;
- `PARTIAL_IBP_BULK = F0 + IBP_FIRST_TRANSFER + IBP_SECOND_TRANSFER`.

No Researcher target enters this construction.

## Critic covariantization accounting

The Critic's already frozen parent Euler contraction is computed independently from

`E^ab = -P^{a c d e} g^{bf} R_{f c d e} + 2 nabla_c nabla_d P^{a c d b} + 1/2 g^{ab} I3`.

Define the exact internally computed covariantization gap

`GAP = EULER_PARENT - PARTIAL_IBP_BULK`.

This is not fitted to the Researcher or to the frozen parent difference; it compares two independently evaluated Critic-lineage representations before any cross-lane read.

At the frozen normal-coordinate point `Gamma(0)=0`, the explicit derivative-of-Gamma component of the Critic double divergence is frozen directly from the Critic Taylor polynomial:

`DGAMMA = 2 h_ab sum_{c,d,r} [ (d_c Gamma^a_{dr}) P^{r c d b} + (d_c Gamma^c_{dr}) P^{a r d b} + (d_c Gamma^d_{dr}) P^{a c r b} + (d_c Gamma^b_{dr}) P^{a c d r} ]`.

The additive Critic classes are frozen as:

- `COVARIANTIZATION_DGAMMA_TIMES_H = DGAMMA`;
- `COVARIANTIZATION_GAMMA_TIMES_DH = 0` at the frozen normal-coordinate point;
- `COVARIANTIZATION_GAMMA_GAMMA_TIMES_H = 0` at the frozen normal-coordinate point;
- `CONNECTION_VARIATION = GAP - DGAMMA` (the remaining exact connection/index covariantization operator difference after removing the explicitly frozen dGamma term; it is not defined from the Researcher-parent discrepancy);
- `IBP_FIRST_TRANSFER` and `IBP_SECOND_TRANSFER` as reconstructed above;
- `ALGEBRAIC_CURVATURE_VARIATION = F0 - VOLUME_CONTROL`;
- `VOLUME_CONTROL = independently recomputed fixed-R density volume contribution`;
- `PRINCIPAL_CONTROL = 0` as an additive scalar, with the ten `Fij(0)` slots carried separately as vector controls.

Their exact scalar sum must equal the Critic parent Euler contraction.

## Ordered first-divergence comparator

After both target-blind payloads are serialized and hashed, compare in this immutable order:

1. `LOWER_ORDER_CURVATURE_VARIATION_BEFORE_IBP`: compare `F0 - volume`;
2. `FIRST_DERIVATIVE_PERTURBATION_COEFFICIENTS`: compare ordered `Fi` values;
3. `FIRST_DERIVATIVE_IBP_TRANSFER`: compare the exact first-transfer scalar;
4. `SECOND_DERIVATIVE_LOWER_ORDER_IBP`: compare the exact second-transfer scalar, with the ten principal `Fij(0)` slots remaining a separately required exact-match control;
5. `COVARIANTIZATION_CONNECTION`: compare the four frozen connection/covariantization classes;
6. `ALGEBRAIC_EULER_TERM`: only if stages 1-5 have no exact difference but the full parent discrepancy remains.

The comparator records the first stage and smallest ordered tensor/vector slot with nonzero exact difference and stops causal interpretation there, while still verifying total reconstruction identities.

## Interpretation of frozen terminal taxonomy

For the preregistered `LOWER_ORDER_LOCALIZED_EXACT` classification, "class-by-class" means that both lanes provide the same frozen class keys/semantics and the terminal comparator accounts for the exact difference vector class-by-class; numerical equality is required only for classes upstream of the first localized divergence. The exact sum of class differences must equal the frozen parent discrepancy.

No new terminal classification is introduced by this binding.

## Locks

Exact Fraction arithmetic only. No tolerance, sign fit, scale fit, c6 fit, normalization change, witness change, panel broadening, index remapping, symmetry reduction, or post-result regrouping. `c6=SYMBOLIC_UNFIXED`; corrected Q10 remains LOCKED; `theory_established=0%`.
