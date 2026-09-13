# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051 / post-G51C-D2 replacement validation authorization`
Project phase: `MODEL_CONSTRUCTION / WEYL3 FRESH HELD-OUT REPLACEMENT VALIDATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **87%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false**.

## Historical G51C — terminal FAIL
Run `34741060700`, aggregate job `103680844833`, artifact `10311749167`, digest `sha256:1b4a324a05666a2ff0c67bdb922e87efc600d70d481ab380bb4532baf43c8c99`.
Classification: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`. Frozen `A+I+2D` assembly: 12/18 PASS, exact reduced-EL Stream B 0/6. Never rewritten.

## G51C-D2 — historical terminal FAIL preserved
Run `34741924103`; aggregate job `103683219373`; artifact `10312601307`; digest `sha256:dcdef4dff571b1ba3350a2e6acec7478e1aec1b6847d5fc7765c17d82b931c78`.
Classification: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS. Sole fail: spherical B3 near-null angular component. Frozen D2 criteria remain unchanged.

## D2N — terminal numerical-conditioning diagnostic PASS
Prereg `b3fc227d6521b92fc6f5131f99b3812080bf4ee8`; implementation `0fbfbdcb552e170f9a228bf555057b63065d19d6`; aggregate `c294074743955d66b0e14a3fd9a56430c09428a2`; workflow `9ae51dd4e0bcc9db769ef782e16e16987d4be60c`; head `c6efa69559a0222242e6c79a617c09c3d4e42adc`.
Run `34742201899`; aggregate job `103684234240`; artifact `10312526872`; digest `sha256:5809e09fb4365a745399f9db5fd1630b85d9cb280f23dca1d4a03337774b55a4`.
Classification: `PASS_DIAGNOSTIC_D2N_NEAR_NULL_ERROR_COLLAPSES_UNDER_INDEPENDENT_FIVE_POINT_STENCIL`, 8/8 PASS.
B3 angular absolute error collapsed from `7.838355602488458e-09` (nested M3) to `1.743008620663677e-11` (independent nested M5), ratio `0.002223691688739307`; M5 vector residual `2.5056495286480338e-09`.

## D2Z — terminal exact diagnostic
Prereg `645a972a2280e645cf9f5c86d456c7f2ad333b49`; implementation `8edd979ece4b972ad49337f28b22a0ccc4066688`; workflow `4dfa87805bd8d09dd7615ac67614a7835bbfc95b`; head `6558221ff4de5d688ab6da57aed81bdf358d6b80`.
Run `34742259726`; job `103683830040`; artifact `10312697366`; digest `sha256:326e868eafc082965602eb9a6b57e792b4fcb45661c5546d117269ae3ed8cf5b`.
Classification: `DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_CONFIRMED`.
At `r=6/5`, exact `E_S=-3.9949986160730709e-07`; nearest positive exact numerator root `1.199993503822622846...`, distance `6.496177377135481e-06`; derivative at root nonzero and conditioning proxy `1.8472151595166072e5`.

## Active authorization
The historical D2 FAIL remains terminal. D2N+D2Z jointly authorize exactly one next scientific gate: a **fresh prospectively preregistered spherical replacement held-out validation** using the independent five-point covariant derivative. It must use fresh radii/profile points not used for threshold tuning, preserve `-2D` without fitting, retain a historical `+2D` negative control, and explicitly separate ordinary-scale from near-null component criteria preregistered before production.

A replacement PASS may authorize a new full-EOM replacement gate. It may not rewrite G51C or D2 historical failures.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- full covariant six-derivative EOM not established;
- finite panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
