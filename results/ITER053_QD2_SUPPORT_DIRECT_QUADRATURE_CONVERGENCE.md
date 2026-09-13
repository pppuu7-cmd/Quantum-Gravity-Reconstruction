# Iter053-QD2 — support-domain direct-action quadrature convergence

Gate: `ITER053-QD2-SUPPORT-DIRECT-QUADRATURE-CONVERGENCE`

Authority:
- preregistration: `5b85e850f4ad38d8b3dcc07958c6a3f664a4f5f7`
- implementation: `48bee611c8482817d447af61a76ccb43af165b47`
- aggregate: `71c81f38a4db6b80357c1a8dbd5b1dd781e3aec2`
- workflow: `c8a9121954d71dae391603c9fa5685db180aba4d`
- production head: `ddf266c2b7e33bac6a8942fb099e60a76ac78aac`
- run: `34770521310`
- aggregate job: `103759533568`
- summary artifact: `10322290890`
- digest: `sha256:bc30c712c33fca891656cede20e5de73f8c0404da99e25257a961d82a02b160a`

Classification: **`PASS_DIAGNOSTIC_ITER053_SUPPORT_DIRECT_QUADRATURE_CONVERGED_BY_GL8`**.

All eight A4+B2+C2 diagnostic lanes were found, control-valid and converged under the prospectively frozen support-domain GL5/6/7/8 direct-action test.

Aggregate metrics:
- worst generic GL6->GL7 relative change: `1.8944968469868708e-4`;
- worst generic GL7->GL8 relative change: `8.031564672079293e-8`;
- worst null |GL8|: `9.672771482817587e-18`;
- worst null |GL8-GL7|: `1.4382301600313946e-17`.

Representative A0 direct integral converged from `9.05658569677377e-6` (GL5) to `9.066728302213213e-6` (GL6), `9.066614167698799e-6` (GL7), and `9.06661370654654e-6` (GL8), with GL7->GL8 relative change `5.086267593945806e-8`.

Interpretation lock: this is a direct-action numerical convergence diagnostic only. No H5 bulk integral is certified, Iter053 is not scientifically reclassified, and no coefficient/sign fitting is authorized. A weighted H5 bulk pilot was separately prospectively preregistered before any replacement scientific gate. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains 0%.
