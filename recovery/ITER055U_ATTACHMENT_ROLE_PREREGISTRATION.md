# Iter055U preregistration — continuum-to-B3 attachment: candidate structure or readout convention

Date: 2026-09-14
Gate: `ITER055U-CONTINUUM-TO-B3-ATTACHMENT-ROLE`

## Frozen question
Can the missing continuum/test-function -> finite-B3 map of Iter055T be dismissed as an arbitrary external readout/coarse-graining convention, or does the microscopic dynamical role of the finite B3 variables make the attachment a candidate-owned sector-identification object up to ordinary invertible reparameterization?

## Frozen source facts
- G6C/G6E: finite B3 variables are restrictions of the candidate configuration `X_Gamma`, not merely detector outputs.
- Iter006-G7B: `G_v,A_e` and path/loop transports form the coarse observable/configuration algebra and participate in exact blocking.
- Iter055S: arbitrary physical Hilbert-dual test functions are legitimate external one-particle readouts.
- Iter055T: no source-defined attachment from the one-particle/test sector to finite B3 variables exists.

## Frozen obligations
1. Formalize ordinary finite-B3 coordinate equivalence as `C2=M C1` with `M` invertible on the finite target coordinates. Note the invariant consequence `ker C1 = ker C2` and equal rank.
2. Construct at least two bounded admissible coarse readout maps from `H_char` to the same finite-dimensional target with different kernels/nullspaces.
3. Determine whether current QGR contains a theorem that microscopic/boundary dynamics or continuum recovery is independent of replacing one inequivalent attachment by another.
4. Distinguish external measurement/readout freedom from identification of which continuum perturbations correspond to the candidate's microscopic configuration variables.
5. Do not infer uniqueness of a missing attachment; the gate only classifies its role.

## Frozen classifications
- `PASS_SCOPED_ITER055U_ATTACHMENT_IS_CANDIDATE_OWNED_UP_TO_B3_REPARAMETERIZATION__ARBITRARY_READOUT_MAPS_ARE_INEQUIVALENT` if inequivalent bounded maps exist and no source theorem makes their induced microscopic sector identification physically scheme-independent.
- `PASS_SCOPED_ITER055U_ATTACHMENT_IS_PURE_READOUT_SCHEME_WITH_SOURCE_PROVEN_INDEPENDENCE` only if current QGR proves continuum recovery/predictions independent of all admissible attachment choices relevant to the finite B3 variables.
- `BLOCKED_ITER055U_B3_VARIABLE_ROLE_TOO_AMBIGUOUS_TO_CLASSIFY` if the source does not establish whether B3 variables are candidate state or readout.
- `INVALID_PROVENANCE_ITER055U_SOURCE_ROLE_CONFLICT` only if existing authorities contradict one another.

## Interpretation ceiling
A candidate-owned-role PASS does not select a map. It only establishes that a new attachment or a genuine scheme-independence theorem is required before claiming recovery of the continuum one-particle sector from finite B3 dynamics. No dynamics/beta/c6/Weyl3/regulator/unitarity/UV/GR/experiment/theory claim follows.

No GitHub Actions run is preregistered; this is exact Hilbert/linear-algebra plus source-role analysis.
