# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter039`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / ABSOLUTE SOURCE AND PHASE IDENTIFIABILITY`
Active roadmap stage: `principal refinement closure -> absolute source/phase identifiability -> minimal calibration authority -> Weyl-active matching -> higher-derivative coefficient status`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter038 completion: **100%**
- Iter039 completion: **PRODUCTION ACTIVE**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Projective refinement-limit action mechanism: **PASS_SCOPED on the frozen principal smooth compact realization after G38**
- Principal identity/refinement-connected connection: **PASS_SCOPED / G10B physical branch rule**
- Principal compact-domain small-h uniform regularity: **PASS_SCOPED (G38)**
- Actual principal fixed-path/loop fine-to-coarse blocking: **PASS_SCOPED (G38)**
- Finite nonlinear torsion equation multiplicity: **VERIFIED_SCOPED (G35–G37)**
- Additional physical connection branches from strongest distant roots: **NOT SUPPORTED UNDER FROZEN G10B (G37C)**
- Physical multiple-branch measure/selection from G35–G37 roots: **NOT AUTHORIZED**
- Absolute source normalization `beta`: **UNDER IDENTIFIABILITY AUDIT (G39)**
- Physical Weyl-active same-realization finite absolute phase target: **NOT DERIVED**
- `c6` fixed: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Iter038 terminal — principal refinement regularity and actual blocking
Authoritative run `34709394158`, head `ae8f365ea1ad9e92cdeaed8fefa81a9f05e152d9`, aggregate job `103595441181`, artifact `10303065332`, digest `sha256:26bf51ad50a90cc42b8ee92ba997a237df25aa82dc0ffedeb538170d9997a432`.

Frozen outcome:
- exact certificate **1/1 PASS**;
- finite-range gap bridge **8/8 PASS**;
- fixed-physical-path blocking **8/8 PASS**;
- elementary loop/groupoid blocking **12/12 PASS**;
- total **29/29 PASS**.

Exact common scaled-residual h=0 torsion Jacobian:
- exact rank **24**;
- exact determinant **11664**;
- numerical minimum singular value `0.3742889790499052`.

Finite bridge/blocking diagnostics:
- minimum finite-bridge Jacobian singular value `0.3117043266205393`;
- maximum finite-bridge condition number `18.83979439212241`;
- maximum final path contraction ratio `0.5053863019927789`;
- maximum final loop contraction ratio `0.5080076341318422`.

Classification: `PASS_SCOPED_PRINCIPAL_COMPACT_REFINEMENT_REGULARITY_AND_FINE_TO_COARSE_BLOCKING`.

Scientific authority: after scaling `z=h w`, the exact common h=0 derivative is invertible. Analyticity plus compactness of frozen `K=[0,1]^4` therefore supplies a uniform sufficiently-small-h principal identity-connected IFT branch and positive local Jacobian gap on this smooth compact realization. The independent numerical B/C/D streams bridge the finite range and verify actual physical-path/loop fine blocking. Thus the G32 regularity assumption is no longer unsupported within this scoped principal realization.

Record: `results/ITER038_PRINCIPAL_REFINEMENT_REGULARITY_AND_BLOCKING.md`.

## Why the front changed
G38 removes the immediate reason to spend more compute on principal regularity grids for the same smooth compact realization. Existing G27–G32 authority now leaves a narrower unresolved problem: the absolute source/action-phase scale. G27 gives `J(n)=beta*n` but one free scalar; G28 gives exact beta-quotiented predictions; G29/G30 localize missing Weyl-active absolute phase authority; G31 shows stationarity does not fix overall quantum phase normalization. G38 adds regular refinement authority but introduces no new absolute source datum.

## Active gate — Iter039
`QGR-ITER039-ABSOLUTE-SOURCE-PHASE-IDENTIFIABILITY-AFTER-REFINEMENT-CLOSURE`.

Preregistered before production in `status/ITERATION_039.md`.
Production workflow: `qgr-iter039-absolute-scale-identifiability`.
Production run: `34709657749`, launch head `15cedcd3507f0223dc50827a2f72e3d0762ec901`.

Five audit classes x six frozen lanes = **30**:
1. exact homogeneous source-law null direction;
2. negative-authority audit that G38 principal refinement/blocking has zero beta authority;
3. exact current absolute-parameter authority rank over `(u=beta^2,c6)`;
4. minimal calibration-rank theorem using hypothetical target rows only as identifiability controls;
5. beta-sign authority: phase is even in beta while a signed absolute source/endpoint datum is odd.

Full PASS classification is `PASS_SCOPED_INTERNAL_ABSOLUTE_SCALE_NONIDENTIFIABILITY_AND_MINIMAL_CALIBRATION_RANK_DERIVED`.

If G39 passes, beta must stop being treated as a number that more internal numerical search can discover under the same authority. It remains an explicit matching/calibration parameter unless an independent microscopic normalization principle is derived. `c6` remains unfixed until an independent genuine Weyl-active absolute phase/matching equation exists. Hypothetical controls are not physical data.

## Strongest positive result
Principal projective refinement regularity and actual fine-to-coarse blocking are now closed at scoped authority for the frozen smooth compact realization, with an exact nonzero determinant rather than numerical extrapolation alone.

## Strongest blocker
`ABSOLUTE_SOURCE_ACTION_PHASE_NORMALIZATION_AND_WEYL_ACTIVE_MATCHING_AUTHORITY`.

## Claim locks
- theory established `0%`;
- G38 authority is scoped to the frozen smooth compact principal realization, not arbitrary global field space;
- G35–G37 distant algebraic roots do not authorize physical branch weights under current G10B evidence;
- no physical branch weights/measures from those roots;
- hypothetical calibration rows are not physical QGR data;
- `beta=1` unauthorized;
- absolute quantum phase normalization remains unfixed pending G39 authority classification;
- `c6` unfixed;
- no physical Weyl-active absolute finite-phase target yet;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` authorization.
