# Preregistration — AT vs generalized corrected Frechet first-divergence localization

Date: 2026-09-18

Gate: `CORRECTED_DEGREE8_AT_GENERALIZED_FIRST_DIVERGENCE_LOCALIZATION`

Parent terminal diagnostic: `LOCALIZED_GENERALIZED_CONSTRUCTOR_FORMULA_MISMATCH`, authoritative run `35276104151`, corrected durable record commit `fff23e02ebafc18d3aaa0bfe41217b29a19b43b3`.

## Frozen question

On one identical canonical R10 metric seed, at which first exact construction stage does the corrected generalized degree-eight Frechet/Euler path cease to reproduce the historical Iter057AT degree-six Frechet/Euler path?

This is a causal-localization gate only. It is not a repair and cannot authorize corrected degree-eight source coefficients or Q10.

## Frozen historical AT path

The historical producer at `c4e7ccc05ea1b8f4967379fc370812dfa99cce03` uses:

1. `seed_metric10()`;
2. `geometry8(g)`;
3. `Cup = raise_last(C,gi,8)`;
4. `I3,QF = _fixed_cubic_and_Q(C,Cup,6)`;
5. `PF = _fixed_p_from_frechet(...,QF,8)`;
6. degree-six downstream Euler assembly.

Its authoritative ordered 840-vector SHA256 is

`5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`.

AQ authority `de82fe82c8f3f40854c81d7cb3e0e5d490a153a4` already established exact agreement between the corrected degree-six AQ/X and AO downstream assemblies for the corrected `P_F` object.

## Frozen generalized path

The blocked corrected degree-eight constructor uses the same corrected Frechet functional but raises construction ceilings:

1. geometry through degree ten;
2. `raise_last(...,10)`;
3. `_fixed_cubic_and_Q(...,8)`;
4. `_fixed_p_from_frechet(...,10)`;
5. source through degree eight, later projected to degree six.

Its already-observed degree-six projection SHA256 is

`2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d`.

## Outcome-blind intervention order

Use one exact canonical R10 metric `g`. Before loading the durable AT coefficient target, each lane must construct and freeze these stages in order:

### H0 — historical baseline

`geometry8 / Cup8 / QF6 / PF8 / source6`.

### H1 — geometry/Cup ceiling intervention

On the identical metric, change only the geometry/Cup construction to the generalized `geometry10 / Cup10` path while retaining `QF6 / PF8 / source6`.

### H2 — cubic/QF ceiling intervention

Starting from H1, change only `_fixed_cubic_and_Q` from degree 6 to degree 8 while retaining `PF8 / source6`.

### H3 — Frechet-P ceiling intervention

Starting from H2, change only `_fixed_p_from_frechet` from degree 8 to degree 10 while retaining the degree-six downstream source evaluation.

### H4 — downstream source ceiling intervention

Starting from H3, change only the downstream Euler assembly from degree six to the generalized degree-eight assembly and then project the exact result back to the ordered degree-six 840-vector.

Each lane must freeze exact source-vector hashes at H0-H4 and exact hashes/mismatch counts for relevant lower-degree geometry/Cup, `I3/QF`, and `P_F` objects sufficient to identify the first divergence. No numerical tolerance is permitted.

Only after H0-H4 have been frozen locally may the durable Iter057AT coefficient file be loaded. H0 must then reproduce the AT 840-vector exactly, and H4 must reproduce the parent generalized blocker hash exactly, or the diagnostic is unresolved/invalid rather than reinterpreted.

## Independent lanes

Researcher lane:
- historical/AQ `x_operator` for H0-H3;
- generalized primary degree-eight downstream assembly for H4.

Critic lane:
- independent AO covariant degree-six source assembly for H0-H3;
- generalized AO-style independent degree-eight downstream assembly for H4.

The Critic must not read the Researcher artifact before terminal aggregation.

## Frozen causal classifications

Terminal aggregation may emit only:

- `LOCALIZED_GEOMETRY_CUP_CEILING_MISMATCH` if H0 reproduces AT and the first exact source/intermediate divergence is introduced by H1;
- `LOCALIZED_CUBIC_QF_CEILING_MISMATCH` if H1 remains identical to H0 and the first exact divergence is introduced by H2;
- `LOCALIZED_FRECHET_P_CEILING_MISMATCH` if H2 remains identical to H1 and the first exact divergence is introduced by H3;
- `LOCALIZED_DOWNSTREAM_SOURCE_CEILING_MISMATCH` if H3 remains identical to H2 and the first exact divergence is introduced by H4;
- `NO_MISMATCH_UNDER_SAME_SEED_INTERVENTION` if H0-H4 all remain identical despite the previously observed parent mismatch;
- `UNRESOLVED_AT_GENERALIZED_FIRST_DIVERGENCE` for any other exact pattern, missing control, lane disagreement, or failed parent-hash reproduction.

A localization classification is diagnostic, not a physics PASS and not permission to change any source.

## Frozen controls

- exact equality of the two independently obtained canonical R10 metric seeds before intervention;
- historical AT producer/authority identities pinned;
- parent localization and generalized blocker hashes pinned;
- exact Fraction arithmetic only;
- complete ordered 840-vector comparisons;
- no AT coefficient target read until H0-H4 are frozen;
- no sign, scale, normalization or coefficient fitting;
- `c6 = SYMBOLIC_UNFIXED`;
- corrected-Y authority unchanged;
- Q10 remains LOCKED;
- `theory_established = 0%`.

## Prohibitions

Do not modify Iter057AT, corrected-Y source convention, `c6`, normalization, thresholds, seed coefficients, or equation convention. Do not run corrected Q10. Do not promote a localization result into nonlinear completion, continuum consistency, quantum consistency, UV completion, or theory correctness.
