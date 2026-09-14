# Iter053T orthogonal controls R1 — terminal non-authoritative PASS

Date: 2026-09-14

Gate: `ITER053T-ORTHOGONAL-CONTROLS-R1-NONAUTHORITATIVE`

Run: `34792534325`
Production head: `02861faee2e7d08d764195928b139bcc452e2d01`
Aggregate job: `103819407020`

## Terminal classification

`ORTHOGONAL_CONTROLS_R1_PASS`

This is a **non-authoritative control result**. It cannot classify, reclassify, replace, or pool evidence with either active scientific Iter053T gate.

All four prospectively frozen independent controls completed and passed:

- `stencil`: PASS;
- `weight`: PASS against exact rational GJ references;
- `wrapper`: PASS;
- `tensor`: PASS;
- aggregate: complete, all controls pass.

The aggregate emitted exactly:

`{"classification":"ORTHOGONAL_CONTROLS_R1_PASS","complete":true,"all_controls_pass":true,"modes_found":["stencil","tensor","weight","wrapper"]}`.

## Provenance

Raw artifacts consumed by the aggregate:

- stencil: artifact `10328875020`, digest `sha256:8096a5bd545113ef03529dc62caf667f060be3a6b02deaad6ee3a40c4d3997cc`;
- tensor: artifact `10328678371`, digest `sha256:ac6fe22ef74c6301ee78bd9c105c7046f0a62f65885a9c7a5cd8e27cd951ec1e`;
- wrapper: artifact `10328508809`, digest `sha256:55821a11e0240ea3da8b36bfaf018680a30712794b350cd9a3cd49a4fe446aa8`;
- weight: artifact `10327763608`, digest `sha256:9a0bfa1304ffc102499de91c676ddafa23c20b022378a0bbeb940f36036b504f`.

Aggregate summary artifact:

- artifact `10327693945`;
- digest `sha256:12ea26f978112f9219105743000a1f9b3e40a513bfeaacb3f4d4f553d1cdb5b3`.

## Historical preservation

The original orthogonal-control run `34792340429` remains permanently `ORTHOGONAL_CONTROLS_INVALID` because its frozen WEIGHT reference digits were insufficiently precise for its own `5e-13` reference tolerance. R1 was separately frozen before retry with exact rational reference values. The original result is not rewritten.

## Scientific use allowed

R1 supports only the following control facts:

1. the five-point first-derivative stencil moment structure used by the audited code matches the frozen fourth-order formula;
2. the independent Gauss-Jacobi extra-support-weight fingerprint agrees with exact rational reference values;
3. the transformed wrapper depth used by the historical legacy path has the frozen compact-perturbation factorization behavior;
4. the source-faithful tensor contraction rule satisfies the exact determinant-one algebraic contraction identity and a wrong-congruence negative control is non-vacuous.

These are implementation/algebra controls. The active scientific productions must still reach their own frozen terminal aggregates.

## Claim ceiling

No compact-support functional-variation closure follows. No full replacement gate is authorized by R1 alone. Historical Iter053R remains scientific FAIL. `theory established=0%`; `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no quantum, unitarity, UV, GR-recovery or experimental claim follows.