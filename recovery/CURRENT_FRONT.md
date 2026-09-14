# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER055L / SOURCE SELECTION OF A COVARIANT SMEARING-REFINEMENT KERNEL FAMILY`
Project phase: `MODEL_CONSTRUCTION / QUANTUM SECTOR BRIDGE PROFILE SELECTION BEFORE DYNAMICS`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / physical Weyl3 treatment selector: **absent**.
- Global interacting measure/regulator removal: **not established**.
- No full quantum unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

## Terminal chain relevant to the current bridge

- Iter055I: `PASS_SCOPED_NONUNIQUENESS...NEW_CANDIDATE_DYNAMICS_RULE_REQUIRED`.
- Iter055J: `BLOCKED_OBJECT_DEFINITION_ITER055J_ONE_PARTICLE_TO_BOUNDARY_OVERLAP_MAP_NOT_SOURCE_DEFINED`.
- Iter055K prereg `f49fc045fa0387634638d7eedd67b75c150a9d64`, result `107f041cd8b9f22f7de6571494cc6dc9bafe4fbd`:
  `FAIL_SCOPED_ITER055K_RAW_L2_BOUNDARY_POINT_RESTRICTION_NOT_BOUNDED__SMEARING_OR_REGULARITY_REQUIRED`.
- Iter055L prereg `c6d1150c66e09db8f52ff6c49407f87ab787507c`, result `b74f69a4fb5808ab1ae039003791ea0dee7d7d57`:
  `PASS_SCOPED_ITER055L_SMEARING_CLASS_MINIMAL_DOMAIN_PRESERVING_BRIDGE__PROFILE_SELECTION_STILL_NEW_INPUT`.

## Iter055L scientific result

On the established physical one-particle Hilbert `H_char`, any finite family of physical kernels `phi_j in H_char` defines bounded observables `B_j[a]=<phi_j,a>` on the entire existing domain. The class is finite-frame covariant when states and kernels transform together, descends through the physical quotient, and exposes exact linear kernel relations required by refinement.

A stronger trace/Sobolev repair can be mathematically viable only by replacing or shrinking the established `L2` domain or adding regularity/scale/representative structure. It therefore is not the minimal domain-preserving bridge under the frozen criterion.

This is only a class selection. Current authority has not yet fixed concrete kernels, their physical scale/shape, metric-versus-connection relation, B3 mapping or refinement law.

## Current highest-information gate

Audit whether existing QGR source structure already selects a concrete covariant smearing/refinement kernel family. Fixed candidate sources to examine include:

1. B3/B4 finite-cell geometry and boundary-variable restriction maps;
2. G6F/G6H one-particle wavepacket/readout envelope definitions;
3. physical measure/disintegration structure;
4. compact-support/local perturbation machinery already used elsewhere in QGR;
5. local observable/preparation definitions that may distinguish candidate-owned kernels from externally specified detector/input profiles.

A source-defined kernel must be more than a convenient bump/Gaussian/finite-element profile. It must specify its transformation law, normalization, physical scale/support and refinement relation without post-hoc tuning.

If no current source selects such a family, record the kernel/profile/refinement choice as explicit new candidate-defining bridge input before any interacting dynamics axiom is tested.

## Operational note

Scheduled-task UI/finalization failures are operational incidents only. Keep short-orchestrator mode and avoid fake GitHub Actions load for source-level theorem/audit gates.
