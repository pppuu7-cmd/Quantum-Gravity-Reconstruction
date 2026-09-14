# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER055W / PHYSICAL WEYL3 DYNAMICAL-TREATMENT SELECTOR AUTHORITY`
Project phase: `MODEL_CONSTRUCTION / WEYL3 PHYSICAL DYNAMICS DEFINITION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; regulator running is not authorized.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Physical exact-vs-order-reduced Weyl3 treatment selector: **absent pending current audit**.
- Strong hyperbolicity / physical ghost / quantum unitarity claims: **not established**.
- Global interacting measure/regulator removal: **not established**.
- Micro-to-continuum reconstruction `R_h`: **not source-defined** by Iter055V.

## Terminal Iter055W

Preregistration `752a92f8ec7990579c859fd755e21aef28115f63`; result `8573681d9bddf2e6561950c7afd4439d512fffdb`.

`PASS_SCOPED_ITER055W_ANSATZ_INDEPENDENT_SURVIVAL_DECOUPLING_INCOMPATIBILITY__C6_RUNNING_NOT_AUTHORIZED`.

Inside the same formal Iter054I/J fixed-background scaling object,

`rho(h,k)=A(h) h^4 k^2`,

`k_HD(h)=1/[h^2 sqrt(A(h))]`

imply the exact identity

`rho(h,k) k_HD(h)^2 = k^2`

for every positive diagnostic `A(h)` and fixed nonzero physical `k`.

Therefore, without any power-law ansatz:

- `k_HD -> infinity` forces `rho -> 0`;
- `rho -> rho_*` finite nonzero forces `k_HD -> |k|/sqrt(rho_*)`, finite nonzero;
- `rho -> infinity` forces `k_HD -> 0`.

This closes the pure-power loophole of Iter054J. It does **not** authorize running `c6` or identify `k_HD` as a physical ghost/mode.

## Current highest-information gate

Audit whether existing QGR authority already selects the physical treatment of the Weyl3 higher-derivative term. Freeze three mutually distinct treatment classes before reading decisive sources:

1. **EXACT_HD** — vary/use the full six-derivative action as exact finite-h/continuum equations, retaining the full formal principal polynomial and any additional roots;
2. **ORDER_REDUCED_EFT** — treat Weyl3 perturbatively in a controlled small parameter, use lower-order equations to remove higher time derivatives/order-reduce, and interpret only the EFT-valid branch with a specified error/regime;
3. **FINITE_PHYSICAL_REFINEMENT** — retain a nonzero physical refinement/UV stop scale so the finite-h correction is part of the physical theory rather than a removable regulator.

A valid source selector must specify more than a diagnostic computation. It must state which treatment is physical, the domain/regime and what happens to formal extra roots. A numerical principal-symbol audit or continuum scaling theorem that explicitly withholds physical interpretation does not count as a selector.

If no selector exists, record it as a candidate-defining missing object. Do not choose the branch that best rescues Weyl3 after seeing Iter055W.

## Parallel orthogonal blocker retained

The quantum/emergence line remains blocked at Iter055V:

`X_Gamma -> [MISSING micro-to-continuum R_h] -> continuum characteristic sector`.

No finite-element/interpolation rescue is authorized.

## Operational note

Short-orchestrator mode remains active. This source-authority audit requires no fake GitHub Actions load.
