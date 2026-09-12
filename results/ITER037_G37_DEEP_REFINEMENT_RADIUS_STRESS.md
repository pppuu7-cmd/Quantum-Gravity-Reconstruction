# QGR Iter037 G37 — deeper shrinking-cell and radius-growth supporting stress

Date: 2026-09-12
Status: `SCIENTIFIC_PASS_SCOPED_SAME_BRANCH_SURVIVES_DEEPER_REFINEMENT_AND_RADIUS4_PATH_CONSISTENCY`

## Reproducibility

Authoritative GitHub Actions run: `34708971979`.

- head: `cfe59ac5ab31325cd7978f761a9a5264a24f63b8`
- frozen matrix: **36 lanes** + aggregate
- aggregate job: `103594387725`
- aggregate artifact: `10302384093`
- aggregate artifact digest: `sha256:ebde6d1d48870bb983bef368c78ce7984bb5738cd3cb9959059c34b5c64c25c2`

## Frozen aggregate result

- expected lanes: **36**
- found unique lanes: **36**
- reference-control-valid lanes: **36**
- promoted lanes: **36**
- deep-refinement sequence pass seed slots: **[0,1,2,3,4,5]**
- radius-4 sequence pass seed slots: **[0,1,2,3,4,5]**
- joint sequence pass seed slots: **[0,1,2,3,4,5]**
- minimum reference origin Jacobian singular value: `0.3700315206600654`
- minimum candidate origin Jacobian singular value: `1.6287333043387907e-05`
- minimum deep edge-fingerprint distance: `2.9498457030344065`
- minimum resolved deep holonomy distance: `0.0050396273717341344`
- maximum multi-parent transport disagreement in radius-growth test: `3.187584583331305e-13`

## Scientific interpretation

All six G36 jointly persistent distant finite-cell roots survive the frozen supporting stress down to
`h=0.08` under the local shrinking-cell proxy and extend through the positive-orthant `R=4` patch
(70 cells) with exceptionally small multi-parent/path disagreement under the preregistered numerical
criterion.

This is strong evidence that the G35/G36 finite algebraic multiplicity is not merely a one-cell,
one-background, or simple path-choice numerical artifact.

However, this gate does **not** decide physical same-realization admissibility. The older prospective
G10B criterion requires the physical connection to be the identity/refinement-connected branch with
the correct `L=I+h omega+O(h^2)` behavior and fixed-physical-path fine-product blocking. That audit is
recorded separately in G37C and has authority over any physical multiple-branch interpretation.

## Claim locks

- finite algebraic branch persistence = **PASS_SCOPED**;
- physical additional same-realization connection branches = **NOT ESTABLISHED BY THIS GATE**;
- `h` here is a shrinking-cell proxy, not the full projective refinement map;
- `R<=4` is a finite patch, not a global compactness theorem;
- parent-path agreement is numerical consistency, not an analytic cocycle theorem;
- solver nonconvergence is not proof of absence;
- theory established = **0%**;
- `beta`, `c6`, and KMQGB `NEW_REQUIRED` remain unauthorized without independent authority.
