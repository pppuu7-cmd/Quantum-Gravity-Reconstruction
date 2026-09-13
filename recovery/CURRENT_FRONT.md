# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051 / G51C-D1`
Project phase: `MODEL_CONSTRUCTION / WEYL3 FULL-EOM ASSEMBLY DIAGNOSIS`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **85%**; the failed final assembly earns no new completion credit.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Closed prerequisites
Historical G51A remains `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION`; independent G51A-R1 is `PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE` (12/12), run `34729269493`, artifact `10308907565`, digest `sha256:24b077748f70585ffa4bf24c4e88f814de06db13e66dd4e899da062707217cab`.

Historical G51B0 remains `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`; independent G51B0-R1 is `PASS_REPLACEMENT_G51B0_COVARIANT_DOUBLE_DIVERGENCE_CERTIFICATE` (8/8), run `34734247977`, aggregate job `103662730311`, artifact `10310119784`, digest `sha256:a211e21b2190d4c7acd2f58bb75da43ab59d36af03762d42dd9f5c1afa78b7`.

G51B1 is terminal `PASS_SCOPED_WEYL3_P_INSERTION_CERTIFICATE` (8/8), run `34736761744`, aggregate job `103669479104`, artifact `10311710726`, digest `sha256:6ea83543ff58b2ac42bd02e166fed3534f37f09459e6cd55616ac1c4090fd3f0`.

G51B2 initial frozen run `34736978191` remains `SCIENTIFIC_FAIL_G51B2_WEYL3_P_CONNECTION_RESPONSE`; the separately authorized numerical reprojection retry `34737103399` is terminal `PASS_SCOPED_WEYL3_P_CONNECTION_RESPONSE_CERTIFICATE` (4/4), aggregate job `103670518127`, artifact `10312171778`, digest `sha256:f076eb8a61bd2e0cc6d648533737aca349e28c14c3cb39f1f465e857442bf568`.

## Iter051C — terminal frozen assembly failure
Prospective preregistration: `4bdb68cfd50ea7b521372bf633c1b1b43d848625`.
Implementation: `d19aecadfc316c2ec08d75fb5dd188bff245444f`.
Aggregate: `bf4f5a2aeb376efa2e5af4f1e529bebe7864b937`.
Workflow: `77df1829163213a6e6b2a9e6c0464adea223e1ec`.
Authoritative production head: `a69562cb0552abc283dfef1ffff941809578ffd8`.
Run: `34741060700`.
Aggregate job: `103680844833`.
Summary artifact: `10311749167`.
Digest: `sha256:1b4a324a05666a2ff0c67bdb922e87efc600d70d481ab380bb4532baf43c8c99`.

Frozen terminal classification: **`SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`**.
All 18/18 artifacts were present and controls valid. A=4/4 PASS, B=0/6 PASS, C=4/4 PASS, D=4/4 PASS. The prospectively decisive exact G48 reduced-Euler–Lagrange Stream B failed all six lanes, with worst exact reduced residual `1.9999998126753908` versus frozen maximum `3e-4`; B numerical final-step change remained good (`2.3681555754359778e-05 <= 2e-4`). Therefore this is an assembly/scientific mismatch, not an infrastructure or loose-convergence failure.

Durable negative result: `results/ITER051C_FULL_WEYL3_EOM_ASSEMBLY_SCIENTIFIC_FAIL.md`.

## Active frontier — G51C-D1 term localization
The next authorized work is a separately preregistered diagnostic decomposition of the exact reduced response into the already independently computed pieces:
- `A`: algebraic metric-density derivative at fixed all-lower Riemann;
- `I = sqrt(-g) sym(P.R)`;
- `J = sqrt(-g) D`: covariant double-divergence contribution before the frozen factor 2.

The diagnostic may measure component contributions and identify which convention is inconsistent, but it may **not** rewrite the historical G51C result or promote a formula chosen merely because it fits the failed B data. A replacement full-EOM assembly is authorized only after an independent variational derivation fixes the sign/index/coefficient convention and that replacement is prospectively preregistered on new held-out controls.

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
