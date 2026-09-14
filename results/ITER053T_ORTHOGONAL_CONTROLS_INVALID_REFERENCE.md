# Iter053T non-authoritative orthogonal controls — terminal INVALID reference control

Date: 2026-09-14

Run: `34792340429`
Head: `702ac27ae2820318f42f100b966714e838953d90`
Scientific authority: **none**
Evidence pooling with either Iter053T scientific gate: **forbidden**

## Frozen classification

`ORTHOGONAL_CONTROLS_INVALID`

The four independent frozen controls produced:

- STENCIL: job success;
- WRAPPER: job success;
- TENSOR: job success;
- WEIGHT: job failure against the frozen reference-digit tolerance;
- aggregate: failure by construction because not all four controls passed.

The WEIGHT calculation itself returned

- `GJ2_extra_weight_suppression = 0.2176291357901487`;
- `GJ3_extra_weight_suppression = 0.3063851989352829`;
- `GJ2_to_GJ3_relative_drift = 0.28968782909086266`.

The frozen contract had copied earlier approximate references

- `0.3063851988551639`;
- `0.2896878290952537`;

with an absolute tolerance `5e-13`. The observed reference discrepancies were therefore about `8.01e-11` and `4.39e-12`, respectively. This is a reference-constant precision defect in this non-authoritative control contract; it is not a failure of either active Iter053T scientific object.

The original run remains terminal INVALID and will not be rewritten. A distinct R1 control-only retry may be preregistered using exact rational reference values derived before the retry.

## Artifact provenance

- wrapper artifact `10328663093`, digest `sha256:9fb816c1c4c215b55b7be9a1a5b91e7dfebd316a464710dade5b8ad3216c11f1`;
- weight artifact `10328308999`, digest `sha256:2fe168db97ce7aa3fdd1203537052eeef2ceeed02a95392696f90e4eac95408c`;
- tensor artifact `10328008036`, digest `sha256:1a7aea517622e559610a5c8934f2be275c54dd443e2af0973956446d8dbe676b`;
- stencil artifact `10327683616`, digest `sha256:04de499ce30755331beb4e4105aaac3650955a7b009324d31b4b395761e5b2b5`;
- aggregate artifact `10328192778`, digest `sha256:23e0d986fcfa6fc2a679e9d090b22a08ed3e8147d46d72f976604d4bd4fb57ac`.

## Claim ceiling

No scientific Iter053T classification follows. Historical Iter053R remains scientific FAIL. `theory established=0%`; `c6` remains symbolic/unfixed; `beta=1` remains unauthorized.