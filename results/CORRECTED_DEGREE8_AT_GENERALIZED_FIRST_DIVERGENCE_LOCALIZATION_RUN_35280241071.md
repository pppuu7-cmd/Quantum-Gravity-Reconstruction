# Terminal result — corrected degree8 AT/generalized first divergence

Date: 2026-09-18

Gate: `CORRECTED_DEGREE8_AT_GENERALIZED_FIRST_DIVERGENCE_LOCALIZATION`

Preregistration: `aa2c0784f3b9cd0397c1eb10c000e0e555602a35`.

Authoritative production run: `35280241071`; head `bbbd32a0f75a75ee9687e8f3b41e45c67a7df32f`.

Jobs: Researcher `105400232564`; Critic `105400232296`; terminal `105405399669`.

Artifacts/digests:
- Researcher `10522733730`, `sha256:897f3389453ef6e349f46a9e9cc3ddf78be42394de75c15c134f60014c07fe10`;
- Critic `10522843278`, `sha256:dd6057b31eee7e6c764cb72cf1fa077e10cd2a51a7949f077989fa1bbb47d5ad`;
- terminal `10523185726`, `sha256:ad8d71e1266061fa329b5131a68fba38ce8a15dfcf6c4cd0274a47428e03c6b5`.

Terminal payload SHA256: `3560a470b4ef6c641a6c202d99917ab05a5d7c2971ef2c2beba8fc511d8e247b`.

## Frozen terminal classification

`LOCALIZED_CUBIC_QF_CEILING_MISMATCH`

This is a causal diagnostic, not a physics PASS.

Both independent lanes agree exactly:
- H0 historical baseline = `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`;
- H1 raised geometry/Cup = same AT hash;
- H2 raised cubic/QF ceiling 6→8 = `2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d`;
- H3 raised Frechet-P ceiling = same generalized hash;
- H4 raised downstream source ceiling = same generalized hash.

Frozen equalities: `H1_eq_H0=true`, `H2_eq_H1=false`, `H3_eq_H2=true`, `H4_eq_H3=true`.

Geometry/Cup controls remain exact across H0/H1. The first intermediate change occurs at H2: `P1_equals_P2_through8=false`, with 2824 exact coefficient mismatches; H3 introduces zero further mismatches through degree eight. H0 reproduces the durable Iter057AT ordered 840-vector exactly and H4 reproduces the pinned generalized blocker hash exactly. All lane controls passed; AT was loaded only after pretarget stage freeze.

## Scientific interpretation and locks

The discrepancy is localized to raising the cubic/QF construction ceiling from 6 to 8 on the same seed. This does not by itself decide which degree budget is mathematically correct for the homogeneous degree-six Euler source. A separate prospective degree-budget/causal-adjudication gate is required, specifically because the Euler source contains a double covariant divergence of P and higher P jet coefficients may descend by two coordinate degrees.

Iter057AT and corrected Iter057Y are not reclassified by this diagnostic. Corrected degree-eight coefficients and corrected Q10 remain unauthorized/LOCKED. `c6 = SYMBOLIC_UNFIXED`; `beta=1` unauthorized; `theory_established=0%`; no experimental confirmation, global theorem, quantum unitarity, regulator-removal, UV-completion, or KMQGB `NEW_REQUIRED` claim is authorized.