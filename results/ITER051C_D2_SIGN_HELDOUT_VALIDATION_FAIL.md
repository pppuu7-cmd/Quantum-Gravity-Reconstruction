# Iter051C-D2 — independent variational sign and held-out validation

Date: 2026-09-13
Gate: `ITER051C-D2-VARIATIONAL-SIGN-AND-HELDOUT-VALIDATION`

## Terminal authority
This gate was prospectively frozen before implementation and production. It does not alter the historical G51C full-assembly failure or the D1 diagnostic.

- preregistration commit: `72d42c480c23723b1d185d73816e8c3db5cf809a`
- implementation commit: `fb5d87918ab91c2a318465f9f638bf029a512084`
- aggregate commit: `054f169a68dd0eef545f9b110b8ed2557f29571c`
- workflow commit: `c2d1063d1ffdf6f3a9d3d6d05ddcb97b5602580d`
- production head: `a18d7d054d3612f9ccfbe235b509c51c7890f3ff`
- authoritative run: `34741924103`
- aggregate job: `103683219373`
- summary artifact: `10312601307`
- summary digest: `sha256:dcdef4dff571b1ba3350a2e6acec7478e1aec1b6847d5fc7765c17d82b931c78`

## Frozen candidate
The independently preregistered Palatini/index-symmetry derivation tested

`H_D2 = A + I - 2 sqrt(-g) D`,

with no production fitting and `c6` symbolic/unfixed. The historical `A + I + 2 sqrt(-g)D` formula was retained as a negative control.

## Terminal classification
**`SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`**.

All 20 expected lane artifacts were present and all controls were valid. Final count: **19/20 PASS, 1/20 FAIL**.

Stream counts:
- A — 8 held-out Bianchi-I exact reduced-EL witnesses: **8/8 PASS**;
- B — 4 independent spherical exact reduced-EL witnesses: **3/4 PASS**;
- C — 4 fresh generic 4D covariance/symmetry witnesses: **4/4 PASS**;
- D — 4 fresh conformally-flat null controls: **4/4 PASS**.

Aggregate worst values:
- A corrected max residual: `3.2810328446797246e-06` versus frozen max `5e-4`;
- A final-step change: `8.053555275688545e-06` versus `2e-4`;
- A historical `+2D` minimum residual: `1.9062857265170805`;
- B corrected max residual: `0.019620421321179977` versus frozen max `1e-3`;
- B final-step change: `3.269672623339041e-06` versus `4e-4`;
- B historical `+2D` minimum residual: `1.3627838958724205`;
- C covariance residual: `6.129475301102737e-08` versus `1e-3`;
- C step change: `2.791436525656051e-07` versus `2e-3`;
- C symmetry residual: `3.1700357616681885e-10` versus `3e-7`;
- D `||H||`: `6.420867488461474e-39`, `|I3|=1.5190223422119525e-46`, `||P||=3.1712037800575055e-47`.

## Sole failed witness — spherical B3
B3 had valid controls and excellent derivative-step convergence, but failed the prospectively frozen componentwise relative criterion because its exact angular reduced coefficient is nearly zero.

Exact target:
`[-0.005833265028423915, 0.01035139955710527, -3.994998616073071e-07]`.

Corrected prediction:
`[-0.0058332750503464975, 0.01035140003504168, -3.916615060048186e-07]`.

Component relative residuals:
`[1.7180610370872388e-06, 4.617118530643133e-08, 0.019620421321179977]`.

The third-component absolute discrepancy is only about `7.84e-09`, but because the exact target magnitude is only about `3.995e-07`, the relative residual is `1.962%`, above the frozen `1e-3` limit. The final-step change remained `3.27e-06`, far inside its threshold. The historical `+2D` negative control remained grossly inconsistent (`1.8803596058345882`).

For comparison, independent spherical B0 passed with max residual `3.700183647889059e-07` and B1 passed with `4.529162077566821e-08`, while their historical `+2D` controls were order unity.

## Interpretation
D2 is a genuine terminal FAIL because its frozen 20/20 requirement was not met, and that result must not be softened post hoc. At the same time, the evidence strongly supports localization of the remaining issue to a numerically ill-conditioned near-null spherical component rather than to a generic failure of the `-2D` sign: 19/20 independent lanes pass, including all Bianchi-I, generic 4D covariance and conformally-flat controls, and three spherical profiles.

The scientifically authorized next step is therefore a separately preregistered numerical-conditioning diagnostic using an independent higher-order derivative stencil and a panel spanning both ordinary and near-null spherical reduced coefficients. It may diagnose the B3 discrepancy but may not retroactively change D2's FAIL or relax D2 thresholds.

No replacement full-EOM gate is authorized yet.

## Claim locks
- historical G51C remains `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`;
- D2 remains `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`;
- `c6` remains symbolic/unfixed;
- `beta=1` remains unauthorized;
- full covariant six-derivative EOM remain unestablished;
- theory established remains `0%`;
- no experimental confirmation, global theorem, absolute-energy-positivity proof or quantum-unitarity proof follows from this finite diagnostic panel.
