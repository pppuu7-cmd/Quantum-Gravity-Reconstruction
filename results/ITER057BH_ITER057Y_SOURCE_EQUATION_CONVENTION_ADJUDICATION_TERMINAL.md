# Iter057BH terminal result — Iter057Y source/equation convention adjudication

Date: 2026-09-17
Gate: `ITER057BH_ITER057Y_SOURCE_EQUATION_CONVENTION_ADJUDICATION`
Preregistration: `4317e8d2dce74178ecddab100374455c933959c4`
Static implementation: `657c65495eafb438574e78bdb0599dba075a4c82`
Exact implementation: `a2b46f9f8d97d775638cc7a2383007229811da1d`
Production head: `deceffde435e81f8009e7d38887c4bcbe6a0943e`
Workflow: `.github/workflows/qgr-iter057bh-y-source-convention.yml`
Actions run: `35255309628` (`completed/success`)

Artifacts:
- static `10512309191`, digest `sha256:7a935eff265bcd4d70a35c07e928751a5afcba6db14ad868b299d57ed64000ed`;
- exact `10512805176`, digest `sha256:11285d039a33d0484b4cc713747f064a0f676a1b09927196e0a33148a24f8572`;
- terminal `10511939920`, digest `sha256:8727ae931b118033a4d69b0fe9c4b95d0fdf586da6180664ac02918cd8bab37c`.

## Frozen classification

`BLOCKED_ITER057BH_Y_SOURCE_CONVENTION_UNRESOLVED`

Terminal payload SHA256: `b6dcca603fba2f156ae15cad6fc59156a3022769eff2283b4eb1fc19e8cdff02`.

## Terminal execution facts

The frozen terminal classifier correctly refused to infer a sign because the exact convention payload was absent.

The static lane completed and established all frozen Iter057Y/AT/AQ semantic controls except one X-sign extractor predicate. It recognized:

- Iter057AQ `x_operator` returns `Edown`;
- Iter057AT primary uses AQ `x_operator(P_F)`;
- Iter057AT independent uses AO `Edown`;
- historical Iter057Y loads the X CSV values into `source`;
- historical Iter057Y residual convention is `DG - source = 0` and its affine RHS is the negative of the current residual;
- no corrected-Y outcome was loaded.

Its only blocking semantic predicate was `x_serialized_source_is_unary_negative_edown=false`. Post-terminal inspection localizes this to the extractor assuming one AST `Subscript` layer for `neg(Edown[a][b])`; Python AST represents the two-dimensional access with nested `Subscript` nodes. This does not reclassify BH.

The exact lane freshly executed the pinned Iter057AQ production computation successfully: `fresh-aq-exitcode.txt = 0`. The subsequent comparison script exited `1` before any 840-slot relation was classified because its CSV metadata parser attempted `split('=',1)` on every `# ` comment line. Historical `data/ITER057X_CANONICAL_SOURCE_DEGREE6.csv` contains a descriptive line `# ITER057X canonical authority` with no equals sign. The resulting exception was `ValueError: not enough values to unpack (expected 2, got 1)`. No exact sign verdict was promoted from the incomplete lane.

Thus BH is preserved as BLOCKED due representation-level extraction failures. No corrected Iter057Y solve, rank, solvability test or Q8 response was executed.

## Diagnostic ceiling

A non-authoritative check against the immutable older Iter057AQ artifact is consistent with `MAP_MINUS` at sampled coefficients, but this is not BH authority and does not authorize corrected-Y replay.

A new prospectively preregistered repair gate may change only:

1. static recognition of nested-subscripting whose root object is `Edown`;
2. exact CSV metadata parsing so descriptive comment lines without `=` are ignored while key-value metadata remains exact.

All convention criteria, both preauthorized sign outcomes, exact 840-slot comparison requirements and corrected-Y outcome firewall must remain unchanged.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
