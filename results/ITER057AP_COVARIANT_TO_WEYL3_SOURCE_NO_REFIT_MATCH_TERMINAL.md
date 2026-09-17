# Iter057AP terminal result — covariant AO to finite-local Weyl3 source no-refit match

Date: 2026-09-17
Gate: `ITER057AP-COVARIANT-TO-WEYL3-SOURCE-NO-REFIT-MATCH`
Preregistration: `6de62a559381a7c86e01c58a62ea7d8c91606884`

## Terminal classification

**`SCIENTIFIC_FAIL_ITER057AP_COVARIANT_AO_RESTRICTION_DISAGREES_WITH_TERMINAL_WEYL3_SOURCE_AFTER_FROZEN_CONVENTION_MAP`**

## Chronology and target firewall

The independent AO-restricted constructor was repaired only for target-blind implementation/control defects before any terminal Iter057U/X source coefficients were loaded. In particular, the final trace-Ward control repair was documented at `92eb386bffe25d8781b1e62a1426703970bb7a73`; the corrected target-blind constructor completed successfully in run `35178004277`, job `105063887646`, artifact `10478944256`, digest `sha256:34abcef317269db57f8909ca45f0e8b54179ceece6c449f781f57e3aa1718428`.

Its complete 2100-slot payload was frozen before target loading at commit `fe0ba26567155622780a29d3969de1e125cbf2d3`, with complete payload SHA256 `9fb92dce4d8a0153be4eb0044460c17fe120bbfe83a66e860a284a3d7acbc61b` and scientific summary SHA256 `b504e20c600aea0c193d96d5a0545a642eabe893e677529dcff8b04dfd74dbb0`.

The constructor exact controls all passed: independent algebraic-Riemann Frechet reconstruction of `P=dI3/dR`, `P.R=3 I3`, exact nonzero Frechet direction replay, source symmetry through degree six, corrected d=4 trace Ward identity, Noether divergence through degree five, complete 2100-slot basis, `I3(0)/kappa^3=96`, no floating tolerance, and `c6` symbolic/unfixed.

Only after that freeze did the separate comparator open terminal Iter057U/X source authorities.

## Exact comparator outcome

Comparator implementation: `235af31e68400d652f2f25bb1e41083c0221c1cf`.
Workflow head: `c3ca83b737035ae176f5d67db45d0f8e9b482d87`.
Run/job: `35178418055 / 105065138539`.
Artifact: `10479562543`, digest `sha256:e92ce7907f8a25bb9624ff4da413f30f254586d82380c0a7fb501d759ca7c53f`.
Complete comparator payload SHA256: `ecc72565f71e358386bcce1b4729fa7f9b6371b6a8b9d0a7e98b31abeb7662d8`.
Scientific summary SHA256: `f8c410bf8ba7c79e8e7c0627c9975aebc00ede2ac88c71219400347a97fdbc44`.
Durable authority: `9622fcc6a7dcfd6c77a67a6e8d3049ea197a7b3a`.

All comparator controls passed exactly. Of the complete 2100 frozen slots, exactly 230 differ, equal to the entire nonzero support of the historical U/X source:

- degree 0: 4 mismatches;
- degree 1: 0;
- degree 2: 22;
- degree 3: 0;
- degree 4: 64;
- degree 5: 0;
- degree 6: 140.

The degree 0/2/4 AO coefficients are exact global sign opposites of the terminal Iter057U lower source coefficients. However the degree-six coefficients are **not** related to the terminal Iter057X authority by one global sign: the exact coefficient ratios are nonconstant. Therefore the full 2100-slot disagreement cannot be removed by a single convention-sign reinterpretation, and no post-hoc sign or scale was applied.

## Scientific meaning

This is a genuine scoped source-level inconsistency under the prospectively frozen AP convention map. It does not invalidate the independently certified Iter057AO covariant directional-variation identity by itself, nor does it retroactively rewrite terminal Iter057U/X. Instead it proves that the independently constructed AO Euler/Taylor restriction and the historical finite-local Weyl3 source authority are not the same exact degree-six source object under the frozen map.

The highest-information unresolved question is now **which construction carries the degree-six defect and why**. Because lower degrees 0/2/4 show a clean exact sign relation while degree six does not, the next gate should independently adjudicate the degree-six source using direct first-variation probes on the immutable Iter057W seed, chosen before inspecting the corresponding historical coefficient targets. It must not repair AP by changing its sign map post hoc.

## Claim ceiling

This is an exact finite-local classical source-level FAIL of the AP bridge only. It is not a global/all-orders no-go theorem, does not establish instability, hyperbolicity failure, quantum inconsistency, unitarity failure, UV behavior, or experiment. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.
