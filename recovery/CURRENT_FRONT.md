# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `Iter054K / general-scaling continuum-survival no-go`
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

## Iter054J — TERMINAL SCOPED PASS / C6 RUNNING NOT AUTHORIZED

Gate: `ITER054J-WEYL3-CONTINUUM-SURVIVAL-SCALING-TRILEMMA`.

- preregistration `4f1dd6d3cdbf39c795d65c097daf6805a9e9d41a`
- implementation `b03d3f6353047ac288d7a7284ff9f24a4dc9e564`
- production head `911dd5ff97a603baec067e741f6ad3adb94ab23e`
- authoritative run `34830453709`
- aggregate job `103932441006`
- summary artifact `10341724457`
- digest `sha256:9ca9cd86e6e4a55cf1e1106a63a0dba0846bb653b68f9ae47b1db4c545d12d93`
- classification **`PASS_SCOPED_ITER054J_POWERLAW_CONTINUUM_SURVIVAL_TRILEMMA__C6_RUNNING_NOT_AUTHORIZED`**

Raw lane provenance:

- A0 `103932315646` / artifact `10341687873` / `sha256:5e8eab3b87782b5a0f8e1b464ea50d7ffc6b1563f78cf65db8b8f7ae353c2edb`
- A1 `103932315212` / artifact `10342425509` / `sha256:6db9e0ad2592996fac7796bd84a5f91d783ebf1bc5a5ef53eb0bc65a6daf418d`
- B0 `103932315398` / artifact `10341178674` / `sha256:7ff2ea4284c12cfb336163ba8736a36281fc6f29821b7f28dfa087ab70e31a01`
- B1 `103932315417` / artifact `10341493127` / `sha256:18ef4950512e50067129ea5dc7f1c5f24f479e43813e89631b861f9e62a9b99c`

Frozen result for the diagnostic family `c6(h)=cbar6 h^(-s)`:

- `rho ~ h^(4-s)`;
- `k_HD ~ h^(s/2-2)`;
- `s<4`: correction vanishes and branch decouples to infinity;
- `s=4`: correction can remain finite/nonzero but branch remains finite;
- `s>4`: correction diverges and branch moves to zero;
- no single pure power law simultaneously preserves a finite nonzero fixed-band correction and sends the singular branch to infinite physical frequency.

This does not authorize regulator running of `c6` or any physical dynamical treatment.

Durable note: `results/ITER054J_TERMINAL_RESULT.md`.

## Iter054K — next highest-information gate

Iter054J used a pure-power diagnostic family. The frozen definitions themselves suggest a stronger statement that should be tested prospectively without assuming any power law.

Freeze

`rho(h,k) = |c6(h) Cbar| h^4 k^2`,

`k_HD(h) = 1/(h^2 sqrt(|c6(h) Cbar|))`,

for positive nonzero `|c6(h) Cbar|` and fixed nonzero physical `k`.

Algebraically these imply the exact identity

`rho(h,k) = (k / k_HD(h))^2`.

Prospectively test:

1. exact symbolic identity with no power-law assumption;
2. arbitrary positive sequence/function controls for `|c6(h) Cbar|`;
3. if `k_HD -> infinity` at fixed nonzero `k`, then `rho -> 0`;
4. if `rho -> rho0` with `0 < rho0 < infinity`, then `k_HD -> |k|/sqrt(rho0)`, finite;
5. if `rho -> infinity`, then `k_HD -> 0`;
6. therefore no arbitrary regulator dependence in this frozen proxy normalization can simultaneously preserve a finite nonzero fixed-band Weyl3 correction and send the singular branch to infinite physical frequency.

A PASS may establish only this **general fixed-band compatibility no-go**. It must not establish a physical running law for `c6`, renormalization, a cutoff, UV completion, ghost/unitarity, strong hyperbolicity, or correctness of QGR.
