# Iter054L preregistration — quantum amplitude/measure closure authority audit

Date: 2026-09-14
Gate: `ITER054L-QUANTUM-AMPLITUDE-MEASURE-CLOSURE-AUTHORITY`

## Motivation

Iter054K closed the arbitrary-regulator-scaling escape route inside the frozen Weyl3 proxy normalization. QGR still has no authorized physical exact-vs-order-reduced Weyl3 selector. The QGR constitution/roadmap independently requires a controlled quantum dynamics or amplitude/measure with normalization and regulator-removal rules. The next highest-information step is therefore a fail-closed source-authority audit, not another symmetry reduction or scaling panel.

## Frozen source classes

A0 governance/design source class: `README.md`, `docs/CONSTITUTION.md`, `docs/ROADMAP.md`, `docs/KMQGB_HANDOFF.md`.

A1 candidate-development source class: text/JSON files under `iterations/`, `analysis/`, and `status/`, excluding `results/`, `recovery/`, `prereg/`, `preregistration/`, generated artifacts and workflows.

B0 parameter-identity source class: same candidate-development set, looking specifically for explicit microscopic-to-IR identity reaching `c6` without an assumed `c6(h)` running law, and for a normalized observable defined on both sides.

B1 authority/anti-overclaim controls: canonical locks from `recovery/state.json` must remain false where currently false.

## Frozen minimum closure tuple

The audit asks whether current source authority explicitly defines all five objects:

1. microscopic amplitude or measure object;
2. normalization rule fixing relative/absolute weights without setting `beta=1` by convention;
3. regulator-removal / distributional-extension / renormalization rule attached to that amplitude/measure;
4. microscopic-to-IR parameter identity reaching the Weyl3 coefficient `c6` without postulating regulator-dependent `c6`;
5. at least one normalized observable computable on both microscopic and IR sides with the same parameter identity.

Keyword hits are discovery evidence only. They do not by themselves authorize any object. The aggregate may return `SOURCE_AUTHORITY_PRESENT_FOR_REVIEW_ITER054L` only if all five categories have at least one non-governance candidate-development witness; otherwise it returns `REQUIRES_SOURCE_AUTHORITY_REVIEW_ITER054L` with missing categories. A later manual/raw-source review is mandatory before any physical promotion.

## Frozen interpretation locks

This gate cannot establish QGR correctness, quantum unitarity, a physical measure, `beta=1`, a numerical/fixed `c6`, regulator running of `c6`, a physical cutoff, UV completion, experimental confirmation, strong hyperbolicity, or KMQGB `NEW_REQUIRED`.

Missing authority is `REQUIRES_SOURCE_AUTHORITY_REVIEW` / potentially `BLOCKED` after review, never scientific disproof of the existence of a consistent quantum measure.
