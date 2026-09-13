# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051 / G51C-D2`
Project phase: `MODEL_CONSTRUCTION / WEYL3 VARIATIONAL SIGN + HELD-OUT VALIDATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **85%**; diagnostics do not earn completion credit before a replacement full-EOM gate.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Historical G51C remains terminal FAIL
Authoritative run `34741060700`, aggregate job `103680844833`, summary artifact `10311749167`, digest `sha256:1b4a324a05666a2ff0c67bdb922e87efc600d70d481ab380bb4532baf43c8c99`.

Frozen terminal classification: **`SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`**. Controls valid; 18/18 artifacts present; A=4/4 PASS, B exact-G48 reduced EL=0/6, C=4/4, D=4/4. Worst B relative residual `1.9999998126753908` while derivative convergence remained good. Historical frozen assembly was `A + I + 2 sqrt(-g) D` and is not retuned or rewritten.

Durable result: `results/ITER051C_FULL_WEYL3_EOM_ASSEMBLY_FAIL.md`.

## G51C-D1 — terminal term localization
Prospective preregistration `6eae32508dacccf0a2be6a947bfa84707a5aa9c4`; implementation `a4f412632ffbbdb1989ec8049fc7e363133d03ae`; aggregate `39437929740a8105e63c7cf291147fda247ad4aa`; workflow `32e91be9d5ee619b1752a16c629097c23b301372`; production head `a705020e9f0b5779c39ddf62174bd000db84a735`.

Run `34741524418`; aggregate job `103682017568`; summary artifact `10313265535`; digest `sha256:38dcc34cf1502bef249ad315461e35a0ac3ad4ad02df3f58e1a3826d52829412`.

Terminal diagnostic classification: **`DIAGNOSTIC_LOCALIZED_G51C_COEFFICIENT_PATTERN`**.

Six frozen Bianchi-I witnesses gave full-rank term decomposition. Diagnostic best-fit coefficients multiplying `(A,I,J)` were
`(0.9999999910360834, 0.9999999923600963, -1.9999999868098797)`.
Global fitted residual `1.642818965188329e-07`; historical `+2J` residual `2.042500869567214`; direct sign-flipped `-2J` residual `5.359533167345127e-06`; leave-one-out coefficient spread `7.345974766392648e-05`.

This is localization only, not replacement authority. Durable result: `results/ITER051C_D1_ASSEMBLY_TERM_LOCALIZATION.md`.

## Active G51C-D2 — independent sign derivation and held-out validation
D2 was prospectively preregistered **before implementation/production** at commit `72d42c480c23723b1d185d73816e8c3db5cf809a`.

The Palatini/index-symmetry derivation frozen there gives the candidate
`H_D2 = A + I - 2 sqrt(-g) D`
under the existing project definition `D^{mn}=nabla_b nabla_a P^{a m b n}`. No D2 coefficient fitting is allowed.

Implementation commit `fb5d87918ab91c2a318465f9f638bf029a512084`; aggregate `054f169a68dd0eef545f9b110b8ed2557f29571c`; workflow `c2d1063d1ffdf6f3a9d3d6d05ddcb97b5602580d`; production head `a18d7d054d3612f9ccfbe235b509c51c7890f3ff`.

Authoritative run: **`34741924103`**.

Frozen 20-lane matrix:
- A: 8 disjoint Bianchi-I exact reduced-EL witnesses not used in D1;
- B: 4 new spherical polynomial profiles tested against the independent exact generic Iter049 radial-gauge-unfixed Euler–Lagrange authority;
- C: 4 fresh generic 4D Lorentz-frame covariance/symmetry witnesses;
- D: 4 fresh conformally-flat FLRW null controls.

The historical `A+I+2D` assembly is retained as a negative control in A/B. A terminal D2 PASS will **only** authorize a separately preregistered `G51C-R1` replacement full-EOM gate; it will not itself establish full EOM.

## Next-gate lock
Consume raw lane logs/artifacts and the frozen D2 aggregate before making a scientific classification. If D2 is terminal PASS, preregister G51C-R1 before implementation and use a panel that is not merely the D1/D2 fitting/validation set. If D2 fails, preserve the failure and localize the failed stream without changing frozen thresholds.

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
