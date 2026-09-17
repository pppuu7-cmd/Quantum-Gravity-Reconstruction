# Iter057AS — terminal source basis cardinality audit

Date: 2026-09-17
Gate: `ITER057AS_SOURCE_BASIS_CARDINALITY_AUDIT`
Preregistration: `6c08691e0a00e6176531c1d07c01f50fc4758ab8`
Implementation: `dec284303f705e3cee4b41bdfde918032c9186ad`
Production head: `e86f1476b574dfd414ac0b69c664bd6518a9c2fc`
Actions run: `35192308567`
Terminal artifact: `10483644731` (`iter057as-source-basis-cardinality-audit`)
Artifact digest: `sha256:a96eb0ff445c027eb769250ad1b651f6203cfcc380d7b821e6fd9d4568c1b57b`
Scientific payload SHA256: `cb5f692055ca708d4630090dfc3e2894fdde17671d219679246bb25fa91085ea`
Workflow conclusion: `success`

## Terminal classification

`PASS_SCOPED_ITER057AS_AR_CARDINALITY_INCONSISTENCY_ESTABLISHED`

## Frozen exact evidence

The target-blind audit satisfies the prospectively frozen Iter057AS criteria. Independent explicit enumeration and closed-form stars-and-bars agree:

- four variables and ten symmetric tensor pairs;
- homogeneous degree-six monomials: `84`;
- homogeneous degree-six symmetric-source slots: `10 * 84 = 840`;
- cumulative degree-zero-through-six monomials: `210`;
- cumulative degree-zero-through-six symmetric-source slots: `10 * 210 = 2100`.

The source-interface controls also pass: Iter057AR serializes over the ten `PAIRS` and `alphas(6)`, while the inherited Iter057W `alphas(n)` is the exact homogeneous four-tuple set with exponent sum equal to `n`. Historical target coefficients were not loaded; no tolerance or fit was used; `c6` stayed symbolic/unfixed.

Therefore under the inherited representation, `840` is the homogeneous degree-six slice while `2100` is the cumulative degree-0-through-6 tensor-source space. The frozen Iter057AR phrases “degree-six vector” and “2100-slot basis” denote different cardinality objects and are internally inconsistent.

## Authority / firewall

Iter057AR remains terminal BLOCKED and is not retroactively repaired or promoted. No 840-to-2100 embedding is authorized. No historical target/coefficient comparison is consumed here.

A later prospectively preregistered corrected-source gate may explicitly choose a scientifically defined object (e.g. the 840-slot homogeneous degree-six slice or the 2100-slot cumulative through-degree-six vector), but it is a NEW gate/object and must not be called an Iter057AR reproduction.

Theory established remains `0%`; `beta=1` unauthorized; `c6` symbolic/unfixed; finite certificate != theorem; classical != quantum; diagnostic != closure.
