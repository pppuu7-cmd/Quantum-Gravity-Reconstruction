# Iter053U conditional prospective preregistration — full corrected source-faithful compact-support Weyl3 action variation

Date frozen: 2026-09-14

Status: **PROSPECTIVELY FROZEN BUT NOT AUTHORIZED FOR EXECUTION**.

This contract is frozen while both Iter053T scientific productions are still non-terminal and before any substantive GJ3/nodewise terminal evidence from them is consumed. It is a conditional successor only. It may be implemented/executed **only** if the two independent Iter053T gates terminally satisfy the exact execution lock below. Otherwise it remains an unused preregistration and a different question requires a new preregistration.

## Gate

`ITER053U-CORRECTED-SOURCE-FAITHFUL-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`

## Execution authorization lock

Execution is authorized only if repository authority contains both terminal classifications, independently obtained under their already frozen contracts:

1. primary Iter053T:
   `ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED`;
2. nodewise companion Iter053T-GJ:
   `ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED`.

No raw-lane pooling or majority vote is allowed. A FAIL/INVALID/nonterminal result in either gate does not authorize Iter053U. This preregistration itself cannot reclassify Iter053R, Iter053T or Iter053T-GJ.

## Dependency and historical boundary

Historical Iter053R remains permanently

`SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`.

Its failure was localized retrospectively and analytically to the transformed weighted C wrapper path, where the Gauss-Jacobi measure supplied one compact-support factor `B(u)` while wrapper-depth extraction supplied a second `B(u)`, producing an effective transformed weight `B(u)^2` rather than the base-path `B(u)`.

Iter053S separately confirmed pointwise H5 tensor-density covariance on its frozen finite panel. Iter053T/Iter053T-GJ are the prospective diagnostics of the corrected source-faithful pushforward. Even if they pass, they do not themselves establish the complete A4+B2+C2 action-variation certificate; this full fresh replacement is required.

## Scientific question

For the same prospectively frozen genuinely four-dimensional A4+B2+C2 scientific panel and the same numerical/scientific thresholds as Iter053R, does

`d/dε ∫ sqrt(-g(ε)) W3[g(ε)] d4x |_(ε=0)`

agree with

`∫ H5^{ab} h_ab d4x`,

where

`H5 = A + I - 2 sqrt(-g) D5`,

when the compact support is represented by one exact Gauss-Jacobi support factor and every transformed covariance lane uses a source-parameter-faithful transformation of only the **unfactored polynomial tensor**?

## Frozen scientific lane identities

Freshly recompute all eight scientific lanes with `fail-fast:false`:

- A0,A1,A2,A3: four generic compact-support genuinely-4D lanes;
- B0,B1: two conformally-flat/null lanes;
- C0,C1: two determinant-one linear-coordinate covariance lanes.

No historical A/B/C raw result is pooled into Iter053U. Every terminal verdict consumes only fresh Iter053U artifacts generated from the Iter053U production identity.

## Frozen physical/numerical inputs

Reuse exactly the Iter053R scientific inputs and conventions:

- all A/B/C metric seeds and perturbation seeds from Iter053R;
- support radius `a=0.24`;
- compact bump `B(u)=prod_i(1-(u_i/a)^2)^4`;
- direct support-domain Gauss-Legendre orders `GL7` and `GL8`;
- symmetric direct epsilon ladder `(2e-4,1e-4,5e-5)`;
- H5 coordinate/double-divergence derivative step `5e-4`;
- weighted H5 tensor Gauss-Jacobi `alpha=beta=4`;
- coarse weighted order `GJ2=2^4=16` nodes;
- fine weighted order `GJ3=3^4=81` nodes;
- determinant-one C shears inherited unchanged from Iter052/Iter053R;
- H5 sign/coefficient `A + I - 2 sqrt(-g) D5`;
- historical wrong-sign control `A + I + 2 sqrt(-g) D5`.

No seed, support radius, epsilon, H5 step, quadrature order, shear, sign, coefficient or scientific threshold may be changed after Iter053U implementation/trigger begins.

## Single allowed scientific implementation correction

The base A/B/C weighted paths remain mathematically unchanged.

For a C transformed frame under `x=L y`, use the original source parameter `u=x`, evaluate transformed geometry at

`y=L^-1 u`,

and transform only the unfactored polynomial tensor

`p_y(u)=L^T p_x(u) L`.

The Gauss-Jacobi rule supplies the compact-support factor exactly once. The transformed weighted reducer must therefore contract `H_y(L^-1 u)` with `L^T p_x(u)L`, not with a tensor obtained by passing the full `CompactPerturbation` through an additional `.base` wrapper level.

The transformed **direct** compact-support action path remains the full transformed compact perturbation used by Iter053R. It is not replaced by the reduced polynomial path.

No other scientific code-path correction is authorized by this preregistration.

## Freshness / regression firewall

- A and B scientific formulas are unchanged from Iter053R.
- C base formulas are unchanged from Iter053R.
- C direct transformed action path, support map, collar control and metric/perturbation transformation algebra are unchanged from Iter053R.
- only the transformed **weighted polynomial-source extraction** is corrected.

Unexpected required changes outside that location are implementation/object-definition evidence and require `INVALID` or a new preregistration, not silent repair.

## Frozen validity controls

A lane is INVALID rather than scientific FAIL if any required condition fails:

- Lorentzian signature at any required node/epsilon point;
- maximum metric inverse residual `>3e-11`;
- any scored output non-finite;
- compact-support boundary/collar construction residual `>1e-13`;
- for C lanes, `|det L-1| >2e-12`;
- for C lanes, transformed metric or full perturbation algebra residual `>3e-11` on the frozen transformation-control probes;
- required fresh artifacts/nodes missing, duplicated or carrying mixed gate/code/input identity.

If deterministic sharding is used, its reducer must additionally reject missing/duplicate canonical node IDs and mixed implementation/input hashes. Shard topology is infrastructure only; the exact canonical node set and scientific sum are fixed by the quadrature definitions above.

## Frozen scientific thresholds — Generic A lanes

All A0-A3 must satisfy exactly the Iter053R thresholds:

- `|direct_GL8| >=1e-10`;
- direct epsilon final-step relative change `<=5e-4`;
- direct GL7->GL8 relative change `<=5e-4`;
- weighted H5 GJ2->GJ3 relative change `<=2e-3`;
- fine `direct_GL8` vs `bulk_GJ3` relative residual `<=3e-3`;
- coarse-to-fine identity-residual absolute change `<=3e-3`.

## Frozen scientific thresholds — Null B lanes

Both B0,B1 must satisfy exactly the Iter053R thresholds:

- integrated `|direct_GL8| <=5e-8`;
- integrated `|bulk_GJ3| <=5e-8`;
- sampled `|W3| <=2e-10`;
- sampled `||P|| <=3e-9`;
- sampled `||H5|| <=3e-7`.

## Frozen scientific thresholds — Covariance C lanes

For each C0,C1:

1. base and corrected transformed frames independently satisfy the applicable generic A thresholds above;
2. direct integrated covariance relative residual `<=2e-3`;
3. corrected weighted-H5 bulk covariance relative residual `<=2e-3`.

The corrected transformed GJ2/GJ3 values must be computed fresh inside Iter053U. Iter053T results are authorization/provenance only and are not substituted for these values.

## Frozen negative controls

### Historical H5 sign control

On every generic A lane evaluate

`H5_wrong = A + I + 2 sqrt(-g) D5`.

Requirements copied from Iter053R:

- wrong-sign integrated residual is larger than correct-sign residual on every A lane;
- at least one A lane has wrong-sign residual `>=1e-2`.

### C transformed-source object control

For each C lane retain a non-scientific diagnostic/negative-control evaluation of the historical double-weight wrapper path. It must not enter the corrected physical integral. Its purpose is only to verify that Iter053U is not accidentally executing the historical object again.

The classifier must reject an implementation in which the corrected transformed weighted extraction is object-identical to the legacy full-CompactPerturbation wrapper path.

No magnitude threshold from historical Iter053R or Iter053T may be added post hoc to this control.

## Parallel execution contract

Execution may use GitHub Actions sharding to reduce wall-clock cost, but parallelism is not a scientific parameter.

Before launch, the trigger/implementation must freeze:

- canonical lexicographic node IDs for every GL/GJ tensor rule;
- deterministic shard assignment;
- code/input identity stored in every shard artifact;
- deterministic reducer that verifies complete unique node coverage and reconstructs additive sums in canonical node order using `math.fsum` or an equivalently frozen stable sum.

Changing runner/shard count for infrastructure reasons is permitted only before substantive launch, or as an exact infrastructure-only retry that preserves the same canonical nodes, code/input identity and reduction rule. Successful scientific outputs from incompatible implementations/contracts may not be pooled.

Outcome-independent architecture reference:
`analysis/POST_ITER053_PARALLEL_FULL_REPLACEMENT_ARCHITECTURE.md`.

The optional D5 canonical-lattice cache is **not authorized by this preregistration unless** a separate prospectively frozen implementation-equivalence control has already terminally validated it before Iter053U implementation is frozen. Without that control, use the historical H5/D5 implementation.

## Frozen terminal classifications

After all eight fresh scientific lanes and required controls are terminal, only:

- `PASS_SCOPED_ITER053U_CORRECTED_SOURCE_FAITHFUL_WEYL3_COMPACT_SUPPORT_ACTION_VARIATION_CERTIFICATE`;
- `SCIENTIFIC_FAIL_ITER053U_CORRECTED_SOURCE_FAITHFUL_WEYL3_COMPACT_SUPPORT_ACTION_VARIATION`;
- `ITER053U_IMPLEMENTATION_OR_CONTROL_INVALID`;
- `ITER053U_NUMERICAL_OR_INFRASTRUCTURE_FAIL`

are permitted.

A green workflow alone is not a scientific PASS.

## PASS semantics

PASS requires:

- all 8/8 fresh lanes present and valid;
- A4 all PASS;
- B2 all PASS;
- C2 all PASS under the corrected source-faithful weighted object;
- all frozen validity and negative controls satisfied;
- no raw-lane pooling from Iter053R/T/T-GJ;
- aggregate provenance complete.

## FAIL / INVALID semantics

- A valid lane violating a frozen scientific predicate contributes scientific FAIL.
- A failed validity/object/provenance/control condition yields INVALID, not scientific FAIL.
- Missing/incomplete infrastructure before valid substantive coverage yields numerical/infrastructure failure according to the frozen aggregate implementation.
- Thresholds are never weakened after evidence.

## Interpretation ceiling

Even a full Iter053U PASS is only a finite genuinely-4D compact-support computational certificate for the frozen panel. It does not rewrite Iter053R. It is not a global functional-analytic theorem, not a physical higher-derivative stability theorem, not quantum amplitude/measure closure, not quantum unitarity, not full GR recovery and not experimental confirmation.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; `theory established=0%`.

A PASS may close the currently targeted finite computational functional-variation bridge strongly enough to authorize the **next object-definition layer**, but the repository must still resolve `MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY` before interpreting the raw quartic corrected principal symbol as a physical ghost/mode spectrum.
