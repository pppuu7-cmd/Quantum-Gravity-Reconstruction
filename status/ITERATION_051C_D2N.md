# Iter051C-D2N — near-null spherical numerical-conditioning diagnostic

Date: 2026-09-13
Gate: `ITER051C-D2N-NEAR-NULL-SPHERICAL-CONDITIONING`

## Prospective authority
This diagnostic is preregistered after terminal D2 and before D2N implementation/production. It may diagnose numerical conditioning only. It can never retroactively change the terminal D2 classification `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, relax any D2 threshold, or establish the full covariant Weyl^3 EOM.

Historical facts frozen as inputs:
- D2 run `34741924103` passed 19/20 with all controls valid.
- sole failed lane B3 had exact `E_S=-3.994998616073071e-07`, central-stencil prediction `-3.916615060048186e-07`, absolute discrepancy about `7.84e-09`, relative residual `0.019620421321179977`, and final-step change `3.27e-06`.
- the independently derived candidate remains `H=A+I-2 sqrt(-g)D`; no coefficient fitting is allowed.

## Question
Is the sole D2 B3 mismatch consistent with cancellation/truncation in the nested second-derivative numerical operator, rather than a stable failure of the `-2D` tensor assembly, when the same covariant quantity is recomputed using an independently implemented fourth-order five-point coordinate derivative stencil and tested across a fixed spherical neighborhood around the near-null witness?

## Frozen numerical methods
### Existing method M3
The existing production method uses nested 3-point central derivatives through `qgr_iter051c_full_eom.py`, evaluated at `h=[1e-3,5e-4,2.5e-4]`.

### Independent method M5
Implement a new five-point first derivative

`f'(x) = [-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)]/(12h)`

both for the coordinate derivative of actual Weyl^3 `P` entering the first covariant divergence and for the outer coordinate derivative entering `D^{mn}=∇_b∇_a P^{a m b n}`. Connection terms are recomputed from the same metric at each evaluation and are not fitted. M5 uses `h=[2e-3,1e-3,5e-4]`.

No Richardson coefficient or physics coefficient is fitted from production data.

## Frozen 8-lane panel
Use the D2 B3 spherical polynomial profile
- `F=2+r/8+r^2/12`,
- `N=1+r/5`,
- `S=3/2+r+r^3/50`,

at radii:
- A0 `r=1.00`
- A1 `r=1.10`
- A2 `r=1.15`
- A3 `r=1.20` — exact replay of failed D2 B3
- A4 `r=1.25`
- A5 `r=1.30`.

Two ordinary-condition controls reuse D2 spherical profiles but at their frozen radii:
- B0: D2 B0 profile at `r=5/4`;
- B1: D2 B1 profile at `r=4/3`.

The exact target for each lane is independently evaluated from the generic exact Iter049 radial-gauge-unfixed generalized Euler–Lagrange authority; it is not obtained from M3 or M5.

## Frozen controls and outputs
Each lane must report:
- exact `(E_F,E_N,E_S)`;
- M3 finest prediction and component absolute/relative errors;
- M5 predictions at all three frozen steps;
- M5 finest component absolute/relative errors;
- M5 final-step vector change;
- M5/M3 angular absolute-error ratio;
- metric signature and inverse residual;
- historical `A+I+2D` vector residual as a negative control.

Controls valid iff Lorentz signature holds across all stencil points, inverse residual `<=2e-11`, and exact target vector norm `>1e-10`.

## Frozen diagnostic criteria
### A3 replay criterion
For the exact B3 replay (`r=1.20`) diagnostic PASS requires all:
- M5 angular sign equals exact angular sign;
- M5 angular absolute error `<=2e-9`;
- M5 angular absolute error `<=0.35 *` the M3 angular absolute error recomputed in the same run;
- M5 vector relative residual `<=5e-5`;
- M5 final-step vector change `<=5e-5`;
- historical `+2D` vector residual `>=1e-2`.

### Neighborhood/control lanes
For all other 7 lanes PASS requires:
- M5 vector relative residual `<=1e-4`;
- M5 final-step vector change `<=5e-5`;
- maximum M5 component absolute error `<=2e-7`;
- historical `+2D` vector residual `>=1e-2`.

A lane with an exact component whose magnitude is very small is judged by these preregistered absolute/vector criteria; this is a new numerical-conditioning diagnostic and does not alter D2's componentwise relative criterion.

## Aggregate classes
All 8 unique artifacts + valid controls + 8/8 lane PASS:
`PASS_DIAGNOSTIC_D2N_NEAR_NULL_ERROR_COLLAPSES_UNDER_INDEPENDENT_FIVE_POINT_STENCIL`

Valid scientific mismatch:
`DIAGNOSTIC_FAIL_D2N_NEAR_NULL_MISMATCH_PERSISTS`

Missing/invalid controls or implementation failure:
`ITER051C_D2N_CONTROL_OR_IMPLEMENTATION_INVALID`

## Interpretation lock
Even full D2N PASS means only that the sole D2 near-null discrepancy collapses under an independently frozen higher-order numerical operator across the sampled spherical neighborhood. D2 remains historical FAIL. A full D2N PASS may authorize a **new, separately preregistered replacement held-out validation gate on fresh profiles**; it does not authorize G51C-R1 directly and does not establish full EOM.

`c6` remains symbolic/unfixed, `beta=1` remains unauthorized, theory established remains `0%`, and no claim of experimental confirmation, global theorem, absolute energy positivity or quantum unitarity is permitted.
