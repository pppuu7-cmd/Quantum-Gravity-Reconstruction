# Iter054I Terminal Result — Weyl3 Regulator-Limit Asymptotic Separation

Date: 2026-09-14
Gate: `ITER054I-WEYL3-REGULATOR-LIMIT-ASYMPTOTIC-SEPARATION`
Status: **TERMINAL SCOPED PASS / FINITE-H PHYSICAL TREATMENT NOT AUTHORIZED**

## Authoritative provenance

- preregistration commit: `691d35e4250393593a2d99eac6c4b78b51ce833d`
- implementation commit: `d8949b44229bf18c43ab62750253a96f4993ad3f`
- production head: `c4c89a8dc5dc14acb337eb49aad3af3aad5fff64`
- authoritative run: `34825507474`
- aggregate job: `103916655515`
- summary artifact: `10339582352`
- summary digest: `sha256:5a357796951d3ab001a4fde2d2728ed64badedaa807585f6e8623aacb12f0da7`

Lane provenance:

- A0 job `103916603388`, artifact `10340356605`, digest `sha256:e5ebe6556b9a63a26cdf142bb8eb53766215eab599d58c4f7ed3b1efb8851e50`
- A1 job `103916603310`, artifact `10340630363`, digest `sha256:b77e6a9a5833a3fbabe2717605f2cdc5a9f40e0b187851eb21e07d325421e68e`
- B0 job `103916603456`, artifact `10339762671`, digest `sha256:fbf20eab3a6ac7f0dc65b7f2f9e71504e8a34ff54876867504e878bde6b8f369`
- B1 job `103916603452`, artifact `10340156993`, digest `sha256:52397f198ceee8e7036adf8bd8da8edf6867ac6a61355b2c7d204d91e4fd958e`

## Frozen aggregate classification

`PASS_SCOPED_ITER054I_FIXED_BAND_REGULATOR_LIMIT_WEYL3_ASYMPTOTIC_DECOUPLING__FINITE_H_PHYSICAL_TREATMENT_NOT_AUTHORIZED`

All four frozen lanes are valid and pass.

## Scientific result

With `c6` held symbolic and independent of the removable regulator `h`, and with physical curvature bounded independently of `h`, the frozen identities are

`rho = |c6*Cbar| h^4 k^2`,

and, for nonzero finite `|c6*Cbar|`,

`k_HD = 1/(h^2 sqrt(|c6*Cbar|))`.

Therefore on every fixed compact physical-frequency band `|k| <= K`,

`sup rho <= |c6| Cmax K^2 h^4 -> 0`,

while

`k_HD/K -> infinity` as `h -> 0`.

The Weyl-flat sector `Cbar=0` is handled separately as an exact-zero correction sector.

The rational convergence panel passes all prospectively frozen cases.

## Nonuniformity boundary

For the frozen control family `k ~ h^-p`,

`rho ~ h^(4-2p)`.

The lane verifies:

- `p=0,1,3/2`: correction vanishes;
- `p=2`: correction approaches a finite nonzero constant;
- `p=5/2`: correction diverges.

Thus the continuum-decoupling statement is uniform only on fixed compact physical-frequency sets; the threshold nonuniform scaling is exactly `k ~ h^-2`.

## Interpretation locks

This result does **not** authorize:

- finite-h physical order reduction;
- a physical cutoff or refinement stop scale;
- fixing `c6` or assigning regulator dependence to it;
- setting `beta=1`;
- physical higher-derivative mode counting;
- ghost, residue, stability, unitarity or UV-completion claims;
- strong hyperbolicity/well-posedness;
- quantum amplitude/measure transition;
- experimental confirmation or theory establishment.

Theory established remains **0%**.

## Next highest-information route

Iter054I creates a sharp model-construction fork. Under the currently frozen authority (`c6` fixed with respect to a removable `h`), the finite-history Weyl3 correction disappears on every fixed physical-frequency/curvature band in the continuum limit. A nonzero continuum Weyl3 effect would therefore require an independently justified regulator-dependent coefficient/renormalization or a separately derived nonzero physical discreteness/refinement-stop scale. Neither is authorized by this result.

The next useful gate should prospectively audit the **continuum-survival scaling obligation** without choosing it post hoc: derive the general threshold for `c6(h)` required to keep the Weyl3 correction finite/nonzero on fixed physical bands, and separately audit whether any pre-existing QGR source supplies such a scaling/renormalization authority. This gate must remain an authority/necessity audit, not permission to assign a scaling to `c6`.
