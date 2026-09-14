# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER055O / CELL-RELATIVE SCALE-COVARIANT SMEARING FAMILY AND BOUNDARY CAUSAL TYPE`
Project phase: `MODEL_CONSTRUCTION / QUANTUM SECTOR BRIDGE INTERNAL REFINEMENT SCALE`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Global interacting measure/regulator removal: **not established**.
- Physical Weyl3 treatment selector / strong hyperbolicity theorem: **absent**.
- No full quantum unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

## Relevant bridge chain

- Iter055K: raw one-particle `L2 ->` pointwise B3 restriction is unbounded.
- Iter055L: bounded physical Hilbert-dual smearing is the minimal full-domain-preserving bridge class.
- Iter055M: no concrete smearing/refinement kernel is source-selected.
- Iter055N: no nonzero universal fixed scalar `L2` kernel exists without relational data.
- Iter055O prereg `d85444875d4dc9f93d8cdcb6e08144318d4c86f6`, result `4d8563b9cbb4db844bc18a223e0f0b6a52031c34`:
  `PASS_SCOPED_PARTIAL_ITER055O_BOUNDARY_DIRECTION_ANCHOR_EXISTS__PHYSICAL_SMEARING_SCALE_UNFIXED`.

## Iter055O scientific result

The shared B3 is an embedded incidence subcomplex with an exact restriction map. Its three-dimensional tangent subspace determines a one-dimensional conormal line. The physical metric maps this to a covariant normal line, and on a regular non-null face a unit normal can be formed up to ordinary coorientation/sign. Thus no new observer direction is needed for the boundary anchor.

The physical radial scale is not fixed. G7A proves the exact normalization degeneracy `a_cont = c_geom*kappa/h^2`, with `h -> lambda h`, `kappa -> lambda^2 kappa`. Existing authority does not identify `h` absolutely or set it to a Planck length.

## Current highest-information gate

Test whether absolute calibration is actually required for the **internal sector bridge**. A microscopic cell scale parameter `h` already exists in the refinement construction even though its physical value is unidentified. Prospectively ask whether one can define a covariant normalized family `phi_(h,n)` whose profile depends only on dimensionless combinations such as `h (n.k)` and whose refinement law is induced by `h -> h/r`, so that channel/intertwining tests can be formulated dimensionlessly before external scale calibration.

The gate must separate boundary causal type:

- for a spacelike B3 with future-timelike unit normal `n`, `n.k>0` on the future null cone and can serve as a covariant energy variable;
- for a timelike B3 with spacelike normal, `n.k` has angular zero sets and may not by itself control ultraviolet momentum in all null directions;
- null B3 remains outside the normalized Iter055O scope.

Do not choose a concrete radial shape after seeing results. First determine whether the source data `(h,n)` are mathematically sufficient to define a nonempty square-integrable covariant **class** with norm-preserving refinement scaling, and whether this works for all allowed non-null boundary causal types or only the spacelike-B3 subdomain.

Absolute phenomenological calibration of `h` remains a separate G7A blocker even if an internal dimensionless bridge class exists.

## Operational note

Scheduled-task UI/finalization failures are operational incidents only. Keep short-orchestrator mode; exact analytic gates need no fake CI load.
