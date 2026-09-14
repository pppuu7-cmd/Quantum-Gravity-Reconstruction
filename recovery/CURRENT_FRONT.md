# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `Iter054I / regulator-limit asymptotic Weyl3 separation`
Project phase: `MODEL_CONSTRUCTION / WEYL3 DYNAMICAL TREATMENT CONSTRUCTION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- Complete mixed-order evolution reduction: **not established**.
- Physical exact-vs-order-reduced Weyl3 treatment selector: **absent**.
- Quantum amplitude/measure transition: **not authorized**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID/BLOCKED results are immutable.

## Iter054H — TERMINAL SCOPED PASS / PHYSICAL TREATMENT NOT AUTHORIZED

Gate: `ITER054H-WEYL3-REFINEMENT-DOMAIN-CONDITIONAL-ORDER-REDUCTION`.

- preregistration `3d10369e862b4bb559e6eecfadfb6d0377ddc183`
- implementation `0295f245cb07d5ad25c5982a4e6b26b8a1aab8d4`
- production head `8b39156c3a26d1effae5c726cc536554bdf1c43d`
- authoritative run `34820024699`
- aggregate job `103899290026`
- summary artifact `10337404013`
- digest `sha256:71bf6a33820187368a1f074d5c2f74c21cd86c42bfa377d513f889898c1c83c4`
- classification **`PASS_SCOPED_ITER054H_CONDITIONAL_REFINEMENT_BAND_SEPARATION__PHYSICAL_ORDER_REDUCED_TREATMENT_NOT_AUTHORIZED`**

Raw lane provenance:

- A0 `103899244850` / artifact `10338320251` / `sha256:b8ed8716cfca8f4270399a95fefb68b11a5a9dd799077408b3e8f98208c61982`
- A1 `103899244868` / artifact `10337937032` / `sha256:6d8cf66991182b64965dd9f0a8a5ddf0066607f042fafd30fb46059b0d151511`
- B0 `103899244803` / artifact `10338310241` / `sha256:4b45b74e9ed41cc859ee225bc03856f7b75e112005470b4f450942222c5aaa64`
- B1 `103899244652` / artifact `10337617979` / `sha256:e7790f7a2f565a9f24defa0b7a7bfd3df1a83ada251c527f4fccfe7780770eed`

Frozen algebra establishes

`rho = chi q^2`, `q_HD = chi^(-1/2)`,

with

`chi q_max^2 < 1  <=>  chi < 1/q_max^2  <=>  q_HD > q_max`.

All prospectively frozen small-chi positive controls and chi>=1 negative controls behave as required.

### Promotion boundary

The source audit closes only one of five promotion obligations:

- `h4_hierarchy_authority = true`
- `chi_bound_authority = false`
- `physical_resolved_band_authority = false`
- `microscopic_state_mapping = false`
- `remainder_operator_tower_control = false`

Therefore the result is a conditional mathematical bridge, not a finite-h physical order-reduced theory.

Durable note: `results/ITER054H_TERMINAL_RESULT.md`.

## Iter054I — next highest-information gate

Iter007 already established that current QGR does not derive a nonzero physical refinement stop scale. Therefore do **not** invent a physical `q_max` or identify `h` with a fundamental length.

The next useful question is the regulator-limit asymptotic one. Freeze before outputs:

1. treat `h -> 0` as a removable regulator limit;
2. keep `c6` symbolic and h-independent;
3. keep physical background curvature `|Cbar|` bounded independently of h;
4. on each fixed compact physical-frequency band `|k| <= K`, derive the exact h-scaling of
   `rho = |c6 Cbar| h^4 k^2`;
5. derive the physical singular-branch scale
   `k_HD = q_HD/h = 1/(h^2 sqrt(|c6 Cbar|))` when the frozen channel normalization is unity;
6. verify that fixed-band `rho -> 0` and `k_HD -> infinity` as `h -> 0` for nonzero finite `|c6 Cbar|`;
7. include nonuniform controls `k ~ h^-p`, especially the threshold `p=2`, to demonstrate exactly where compact-band asymptotics cease to be uniform;
8. preserve the Weyl-flat `Cbar=0` case separately rather than dividing by zero;
9. do not promote this asymptotic statement to finite-h physical order reduction, a physical cutoff, hyperbolicity, ghost or unitarity claims.

A PASS would establish only **asymptotic continuum decoupling on fixed compact physical-frequency/curvature sets**. It would be consistent with the existing Iter007 result that finite-history/Weyl3 corrections vanish if h is purely a removed regulator.

Only a separately derived physical-discreteness/microscopic-amplitude/remainder principle could later convert the finite-h conditional domain into a physical treatment selector.
