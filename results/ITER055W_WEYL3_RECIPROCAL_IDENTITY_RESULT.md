# Iter055W terminal result — Weyl3 reciprocal survival/decoupling identity

Date: 2026-09-14
Preregistration: `752a92f8ec7990579c859fd755e21aef28115f63`

## Terminal classification

`PASS_SCOPED_ITER055W_ANSATZ_INDEPENDENT_SURVIVAL_DECOUPLING_INCOMPATIBILITY__C6_RUNNING_NOT_AUTHORIZED`

## 1. Exact reciprocal identity

On the fixed Weyl-active diagnostic scope, use the frozen Iter054I/J formal quantities

`rho(h,k) = A(h) h^4 k^2`,

`k_HD(h) = 1 / (h^2 sqrt(A(h)))`,

with `A(h)>0` and fixed nonzero physical `k`.

Then for every admissible `h`,

`rho(h,k) k_HD(h)^2`

`= [A(h) h^4 k^2] [1/(h^4 A(h))]`

`= k^2`.

Thus

`rho(h,k) = k^2 / k_HD(h)^2`

and

`k_HD(h) = |k| / sqrt(rho(h,k))`.

No pure-power ansatz, differentiability, monotonicity, beta function, or specific regulator running law is used.

## 2. General asymptotic consequences

Let `h_n -> 0` be any sequence for which `A(h_n)>0`.

### Formal HD scale decouples
If

`k_HD(h_n) -> infinity`,

then the exact identity gives

`rho(h_n,k)=k^2/k_HD(h_n)^2 -> 0`.

Therefore the fixed nonzero physical-frequency Weyl3 correction cannot remain finite and nonzero while the formal HD characteristic/root scale is sent to infinity.

### Weyl3 correction survives finitely
If

`rho(h_n,k) -> rho_*`, `0<rho_*<infinity`,

then

`k_HD(h_n) -> |k|/sqrt(rho_*)`,

a finite nonzero value.

### Weyl3 correction diverges
If

`rho(h_n,k) -> infinity`,

then

`k_HD(h_n) -> 0`.

### Formal HD scale has a finite nonzero limit
If

`k_HD(h_n) -> K_*`, `0<K_*<infinity`,

then necessarily

`rho(h_n,k) -> k^2/K_*^2`.

These implications are ansatz-independent within the frozen formal model.

## 3. Relation to Iter054I and Iter054J

Iter054I proved, for regulator-independent finite symbolic `c6` and bounded fixed physical curvature, that on fixed physical bands

`rho -> 0`, `k_HD -> infinity`.

Iter054J then showed that in the diagnostic pure-power family `c6(h)=cbar6 h^-s`, finite nonzero fixed-band survival requires `s=4`, which leaves `k_HD` finite, while `k_HD -> infinity` requires `s<4`, which makes `rho -> 0`.

Iter055W shows that this incompatibility was not an artifact of the pure-power family. It follows directly from the reciprocal structure of the same formal scaling object for an arbitrary positive diagnostic magnitude `A(h)`.

## 4. Weyl-flat sector

For the exact Weyl-flat sector `Cbar=0`, the correction is exactly

`rho=0`.

The nonzero-`A` formula used to define a finite `k_HD` is not applied by division through zero. This sector remains an exact-zero correction control and is not used to infer a physical root.

## 5. Scientific meaning and strict scope

The result is a **necessity theorem inside the Iter054I/J formal reduced/fixed-background scaling model**.

It says that no regulator-dependent choice of the single magnitude entering this formal object can simultaneously accomplish both:

1. a finite nonzero Weyl3 correction at fixed nonzero physical frequency; and
2. decoupling of the formal higher-derivative characteristic/root scale to infinite physical frequency.

This does not establish that `k_HD` is a physical propagating mode, ghost, pole, instability, or observable. That question depends on a physical exact-vs-order-reduced/EFT treatment rule which QGR has not yet supplied.

Likewise, allowing arbitrary `A(h)` in the proof is **not authorization** to assign regulator running to `c6`, to the background curvature, or to a physical coupling. It is a counterfactual mathematical control showing that such running, even if proposed later inside the same formal object, cannot satisfy both desiderata simultaneously.

## Roadmap effect

The pure-power loophole is closed. The remaining Weyl3 model-construction fork is now structural rather than a choice of running exponent:

- if the continuum limit keeps the current regulator-independent `c6` authority, fixed-band Weyl3 corrections vanish while the formal HD scale decouples;
- if a nonzero fixed-band Weyl3 effect is retained within this formal exact higher-derivative object, the corresponding formal HD scale cannot be pushed to infinity by coefficient running alone;
- avoiding this fork requires a different physical treatment/interpretation object, such as a prospectively justified order-reduced/EFT formulation, finite physical refinement stop, or other independently derived dynamics. None is authorized by this result.

## Next highest-information gate

Audit existing QGR authority for a physical **Weyl3 dynamical treatment selector**: exact higher-derivative equations versus perturbative/order-reduced EFT versus a finite physical refinement/cutoff formulation. Determine whether any earlier source actually chooses among these and specifies the regime/error control. If absent, record the selector as a candidate-defining missing object rather than treating the formal `k_HD` root as physical by default.

## Claim ceiling

- `c6` running: not authorized;
- physical exact-vs-order-reduced Weyl3 treatment: not selected;
- physical higher-derivative mode/ghost: not established;
- strong hyperbolicity, quantum unitarity, UV completion, regulator removal, full GR recovery, experiment and theory establishment: not established;
- theory established remains 0%.

No GitHub Actions run was required; the result is exact algebra/asymptotics.
