# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `Iter054J / continuum-survival scaling trilemma`
Project phase: `MODEL_CONSTRUCTION / WEYL3 DYNAMICAL TREATMENT CONSTRUCTION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; no regulator-dependent scaling is authorized.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- Complete mixed-order evolution reduction: **not established**.
- Physical exact-vs-order-reduced Weyl3 treatment selector: **absent**.
- Quantum amplitude/measure transition: **not authorized**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID/BLOCKED results are immutable.

## Iter054I — TERMINAL SCOPED PASS / FINITE-H PHYSICAL TREATMENT NOT AUTHORIZED

Gate: `ITER054I-WEYL3-REGULATOR-LIMIT-ASYMPTOTIC-SEPARATION`.

- preregistration `691d35e4250393593a2d99eac6c4b78b51ce833d`
- implementation `d8949b44229bf18c43ab62750253a96f4993ad3f`
- production head `c4c89a8dc5dc14acb337eb49aad3af3aad5fff64`
- authoritative run `34825507474`
- aggregate job `103916655515`
- summary artifact `10339582352`
- digest `sha256:5a357796951d3ab001a4fde2d2728ed64badedaa807585f6e8623aacb12f0da7`
- classification **`PASS_SCOPED_ITER054I_FIXED_BAND_REGULATOR_LIMIT_WEYL3_ASYMPTOTIC_DECOUPLING__FINITE_H_PHYSICAL_TREATMENT_NOT_AUTHORIZED`**

Raw lane provenance:

- A0 `103916603388` / artifact `10340356605` / `sha256:e5ebe6556b9a63a26cdf142bb8eb53766215eab599d58c4f7ed3b1efb8851e50`
- A1 `103916603310` / artifact `10340630363` / `sha256:b77e6a9a5833a3fbabe2717605f2cdc5a9f40e0b187851eb21e07d325421e68e`
- B0 `103916603456` / artifact `10339762671` / `sha256:fbf20eab3a6ac7f0dc65b7f2f9e71504e8a34ff54876867504e878bde6b8f369`
- B1 `103916603452` / artifact `10340156993` / `sha256:52397f198ceee8e7036adf8bd8da8edf6867ac6a61355b2c7d204d91e4fd958e`

Frozen result:

`rho = |c6*Cbar| h^4 k^2`,

`k_HD = 1/(h^2 sqrt(|c6*Cbar|))` for nonzero finite `|c6*Cbar|`.

For every fixed compact physical-frequency/curvature set with `c6` held h-independent,

`sup rho -> 0`, while `k_HD -> infinity` as `h -> 0`.

For nonuniform `k ~ h^-p`, `rho ~ h^(4-2p)`: it vanishes for `p<2`, is finite nonzero at `p=2`, and diverges for `p>2`.

This is an asymptotic regulator-limit statement only. It does not authorize finite-h physical order reduction, a physical cutoff, a refinement-stop scale, or a regulator-dependent `c6`.

Durable note: `results/ITER054I_TERMINAL_RESULT.md`.

## Iter054J — next highest-information gate

Iter054I exposes a sharp continuum-survival question. Do not choose a regulator-dependent coefficient post hoc. Prospectively test the algebraic necessity first.

Use the frozen one-parameter power-law control family

`c6(h) = cbar6 * h^(-s)`

only as a **diagnostic scaling family**, not as a physical assignment.

Then on fixed nonzero finite physical `k` and `Cbar`, derive

`rho ~ h^(4-s)`,

`k_HD ~ h^(s/2-2)`.

Freeze the following outcomes before outputs:

1. `s < 4`: Weyl3 correction vanishes and the higher-derivative branch decouples to infinite physical frequency;
2. `s = 4`: Weyl3 correction can remain finite/nonzero, but the higher-derivative branch remains at finite physical frequency;
3. `s > 4`: Weyl3 correction diverges and the branch moves toward lower physical frequency;
4. no single pure power-law scaling can simultaneously keep a finite nonzero fixed-band Weyl3 correction and push the singular branch to infinite physical frequency;
5. `c6(h)` remains unauthorized physically; this is a necessity/compatibility audit only;
6. preserve `c6` symbolic, `beta=1` unauthorized, theory established 0%, quantum transition closed, and no ghost/hyperbolicity claim.

A PASS may establish only the **power-law continuum-survival trilemma** in the frozen proxy normalization. It must not establish a physical running coupling, renormalization law, microscopic cutoff, UV completion, or correctness of QGR.
