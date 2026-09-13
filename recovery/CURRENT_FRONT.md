# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051 / five-point full-EOM replacement authorization`
Project phase: `MODEL_CONSTRUCTION / WEYL3 FULL-EOM REPLACEMENT`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **90%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false**.

## Historical terminal failures retained
- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, frozen historical `A+I+2D`, 12/18 PASS. Never rewritten.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS. Sole fail was the near-null spherical B3 angular component. Never rewritten.

## Conditioning diagnostics
- D2N run `34742201899`, artifact `10312526872`, digest `sha256:5809e09fb4365a745399f9db5fd1630b85d9cb280f23dca1d4a03337774b55a4`: independent five-point stencil collapses the B3 near-null numerical error.
- D2Z run `34742259726`, artifact `10312697366`, digest `sha256:326e868eafc082965602eb9a6b57e792b4fcb45661c5546d117269ae3ed8cf5b`: exact simple near-zero conditioning confirmed.

## D2R — terminal scoped replacement PASS
Prereg `2597fb51bc087a4332d5974db38e0641bfacccba`; head `a5f1021f8596f8e00a4a39f0d366eb276de3b397`; run `34744139101`; aggregate job `103689280172`; artifact `10312909946`; digest `sha256:714f66fb514d9046e82a8ede2e4350bf3586989060469dbcdcc415ba22f830c0`.

Classification: `PASS_SCOPED_G51C_D2R_FRESH_SPHERICAL_REPLACEMENT_VALIDATION`.

Frozen aggregate consumed all 12 raw lane artifacts: 12/12 expected, 12/12 valid, 12/12 PASS, 0 parse errors. Worst absolute component error `1.5270905373565569e-09`; worst final-step change `6.047761854580956e-09`; worst vector relative residual `7.3382674860456824e-09`; minimum historical `+2D` residual `1.4228139519895726`.

Interpretation lock: this is a fresh finite spherical-panel validation of the independently implemented five-point covariant derivative with the `-2D` sign. It is not a full 4D covariant Weyl^3 EOM certificate and does not alter historical G51C/D2 failures.

Durable result commit: `c12b9af1a4c930ed6ae703ca53d7e83d712b3a94`.

## Active authorization
D2R terminal PASS authorizes a **separately prospectively preregistered full-EOM replacement gate** using the independently validated five-point derivative and the `-2D` sign, with no coefficient fitting or threshold retuning. The replacement must include mutually independent generic/non-null, anisotropic variational, conformally-flat null, and covariance controls; finite panels remain scoped evidence only.

Only a terminal artifact from that new gate may change the full-covariant-EOM status. A PASS would still be a finite computational certificate, not a global theorem.

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
