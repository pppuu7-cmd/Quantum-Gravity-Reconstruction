# QGR Iter035 G35 — distant torsion branch invariant verification

Date: 2026-09-12
Status: `SCIENTIFIC_PASS_SCOPED_DISTINCT_EXTENDABLE_BRANCH_COUNTEREXAMPLE`

## Reproducibility

Authoritative GitHub Actions run: `34706686021`.

- head: `faec0f17c49c43d97984b16cf048dc4a52a8f247`
- 24 preregistered verification lanes + aggregate, workflow completed `SUCCESS`
- aggregate job: `103588230856`
- aggregate artifact: `10301772238`
- aggregate digest: `sha256:d41b2ecb33301b4bdcb6e63fa006133656611481919455921551239a4e13ee53`

## Frozen gate result

- expected lanes: **24**
- found lanes: **24**
- residual-qualified origin candidates: **22**
- reference controls valid: **YES**
- verified distinct extendable finite branch patches: **8**
- verified `(lane, scale_index, start_scale)` tuples:
  - `(0, 3, 6.0)`
  - `(1, 2, 3.0)`
  - `(1, 3, 6.0)`
  - `(2, 2, 3.0)`
  - `(2, 3, 6.0)`
  - `(3, 1, 1.5)`
  - `(4, 2, 3.0)`
  - `(5, 3, 6.0)`

Each promoted branch satisfied the preregistered independent residual, metric compatibility,
central invariant transport separation, four-neighbor extension, and plaquette-holonomy invariant
separation criteria.

## Scientific interpretation

Within the exact finite nonlinear torsion realization tested by G35, the old single-branch assumption
is numerically false on the verified finite patch: at least one, and in fact eight frozen starts,
produce distinct extendable branch patches with different invariant holonomy data from the reference.

This is a **scoped finite-patch numerical counterexample to uniqueness in the tested realization**.
It is not a global branch-count/nonuniqueness theorem, not a proof of infinite/tower persistence,
and not a phenomenological prediction.

## Claim locks

- global torsion nonuniqueness theorem established = **NO**;
- global compactness/finiteness established = **NO**;
- tower-wide uniform torsion-Jacobian gap established = **NO**;
- solver nonconvergence is not proof of no root;
- absolute normalization `beta` remains underived;
- `c6` remains unfixed;
- theory established = **0%**;
- KMQGB `NEW_REQUIRED` remains unauthorized unless benchmark authority changes.

## Next gate

Freeze branch-persistence testing on a larger neighboring-cell patch across multiple background
amplitudes and a controlled shrinking-cell/refinement proxy before making any broader branch claim.
