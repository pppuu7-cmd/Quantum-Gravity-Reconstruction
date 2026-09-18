# COVARIANT_WEYL3_A7_FIRST_IBP_FI_JET_CAUSAL_AUDIT — implementation binding

Date: 2026-09-19
Status: **FROZEN BEFORE IMPLEMENTATION / BEFORE FI-JET RESULT INSPECTION**

Parent preregistration: `ae2024bd8179f84c7b9ef3b2412d6cad088f5748`
Parent terminal localization: `6ccfededab41dbe01b071916a5aa746491273276`
Frozen witness: `OFFSHELL_A / d=7`

## Purpose

This record fixes the operational meaning of the preregistered five chain-rule source classes before either Fi first-jet lane is implemented or compared.

The scientific comparator remains exactly the preregistered lexicographic scan over `(i,j)`, with source-class comparison only after the first differing first-jet slot is identified.

## Common exact controls

At the frozen normal-coordinate point:
- `g_ab = eta_ab`;
- all first background metric jets vanish;
- `Gamma(0)=0`;
- therefore first jets of the inverse metric also vanish.

Consequently, in both lanes and for every `d_j Fi`:
- `METRIC_JET = 0`;
- `INVERSE_METRIC_JET = 0`.

These are exact controls, not fitted outcomes.

## Researcher operational decomposition

The Researcher remains on `qgr_covariant_weyl3_researcher` and must not import Critic science code.

Generalize its existing exact dual-number build only by separating:
- the scalar-test coefficient key `K=(i,)`, selecting `Fi`;
- the spatial first-jet direction `j`, selecting `d_j Fi`.

The full Researcher first jet is obtained from the unchanged direct metric variation with the complete all-lowered Riemann construction.

Freeze the source classes as follows.

### PERTURBATION_JET

Re-evaluate the same `Fi` first jet with all spatial derivatives of the frozen background metric jets suppressed in the auxiliary first-jet dual channel, while retaining the frozen perturbation first/second jets.

The resulting exact derivative is `PERTURBATION_JET`.

This changes only the auxiliary derivative channel used for source attribution; the point value, frozen metric jets, perturbation jets, and full scientific first jet are unchanged.

### CONNECTION_JET

Re-evaluate the full background first-jet derivative with the explicit quadratic-connection term

`g_ef (Gamma^e_ca Gamma^f_db - Gamma^e_da Gamma^f_cb)`

removed only from the auxiliary source-attribution copy of the all-lowered Riemann expression.

Because `Gamma(0)=0`, this operation leaves every pointwise `Fi` value unchanged. Its difference from the full first jet isolates the derivative of the pointwise-vanishing quadratic-connection contribution:

`CONNECTION_JET = FULL_FIRST_JET - NO_GAMMA_GAMMA_FIRST_JET`.

No target value from the Critic is used.

### CURVATURE_WEYL_JET

With the exact normal-coordinate metric/inverse classes zero, define prospectively:

`CURVATURE_WEYL_JET = NO_GAMMA_GAMMA_FIRST_JET - PERTURBATION_JET`.

This is the remaining exact background curvature/Weyl coefficient-jet contribution after the explicit connection source has been removed.

### Reconstruction

For every ordered `(i,j)`:

`d_j Fi = METRIC_JET + INVERSE_METRIC_JET + CURVATURE_WEYL_JET + CONNECTION_JET + PERTURBATION_JET`

must hold exactly.

## Critic operational decomposition

The Critic remains on `qgr_covariant_weyl3_critic` and must not import Researcher science code.

Use its independently constructed polynomial coefficient

`Fi = K^{abcd} S_i(h)_{abcd}`,

where `K=sqrt(-g) P` and `S_i(h)` is the exact coefficient of `d_i phi` in the Critic's frozen normal-coordinate Palatini principal expression.

For each `(i,j)`:

- `PERTURBATION_JET = K(0) * d_j S_i(h)(0)`;
- `CURVATURE_WEYL_JET = d_j Fi - PERTURBATION_JET`;
- `CONNECTION_JET = 0`, because the frozen Critic `Fi` polynomial contains no explicit connection-dependent first-derivative coefficient;
- `METRIC_JET = 0`;
- `INVERSE_METRIC_JET = 0`.

The Critic decomposition is descriptive of the already frozen Critic lineage. It does not add a missing connection term and is not a repair.

Its five classes must reconstruct every Critic `d_j Fi` exactly.

## Comparison order

After target-blind serialization and hashing:

1. confirm all four pointwise `Fi` controls;
2. scan first jets lexicographically:
   `(0,0),(0,1),(0,2),(0,3),(1,0),...,(3,3)`;
3. freeze the first exact nonzero difference;
4. at that one slot compare source classes only in the preregistered order:
   - metric jet;
   - inverse-metric jet;
   - curvature/Weyl jet;
   - connection jet;
   - perturbation jet.

No source class may be redefined after the first-jet result is visible.

## Parent transfer reconstruction

Each lane must additionally reconstruct the already terminal parent scalar first-IBP transfer exactly as

`-sum_i d_i Fi`.

Failure is provenance/execution evidence, not a scientific mismatch.

## Hard locks

Exact rational arithmetic only. No tolerance, sign fit, scale fit, normalization fit, c6 fit, witness replacement, coordinate replacement, index remapping, Weyl-convention change, symmetry reduction, source-class movement, or formula repair.

`c6 = SYMBOLIC_UNFIXED`.
Corrected Q10 remains LOCKED.
`theory_established = 0%`.
