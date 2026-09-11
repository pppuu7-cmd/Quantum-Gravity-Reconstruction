# QGR Iter006-G2C — symmetric-seed physical Hilbert quotient and unitary history transports

Date: 2026-09-11
Status: `PASS_SCOPED_SEED_PHYSICAL_HILBERT_AND_S4_UNITARY_TRANSPORT`

## Objective

Construct a positive physical state-space on the already derived symmetric `B4` seed without introducing a preferred 10-component gauge-fixing projector, and test whether the 24 symmetry histories can act isometrically while preserving the two QGR-L1 physical modes.

## Physical quotient at a fundamental cover

Let `H(k)` be the selected QGR-L1 quadratic Hessian and `R(k)` the four-parameter derivative gauge map.

At every elementary incidence-null cover covector `e_i`, previous exact results give

- `rank H(e_i)=4` in the ten-component covariant field space;
- therefore `dim ker H(e_i)=6`;
- `rank R(e_i)=4`;
- the Noether identity gives `im R(e_i) subset ker H(e_i)`.

Hence the physical on-shell fiber is canonically the quotient

`P_i = ker H(e_i) / im R(e_i)`

with

`dim P_i = 6-4 = 2`.

No gauge complement is selected.

## Positive seed norm

The ten component labels of `Sym^2(W4)` carry the standard positive Euclidean inner product. The quotient by the gauge subspace carries the associated positive quotient norm (equivalently the norm of the minimal-norm representative).

This norm is used only for the finite symmetric seed. It is **not** asserted to be the final continuum Lorentz-covariant one-particle norm.

## Four-cover one-cell physical space

Define

`H_seed = direct_sum_{i=0}^3 P_i`.

Therefore

`dim H_seed = 4*2 = 8`.

This is the smallest seed mode space that simultaneously retains all four relational cover directions and the independently derived two physical QGR-L1 polarizations on each cover.

## S4 transport

Every `pi in S4` acts by permutation matrices on

- the four relational directions;
- the ten symmetric field components;
- the cover covectors `e_i -> e_{pi(i)}`.

Because the QGR-L1 Hessian was selected inside the exact `S4`-invariant family,

`T_pi ker H(e_i) = ker H(e_pi(i))`.

The derivative gauge map is equivariant as well,

`T_pi im R(e_i) = im R(e_pi(i))`.

The field permutation matrices are orthogonal for the positive seed inner product. Therefore they induce well-defined unitary maps

`U_pi : P_i -> P_pi(i)`

and hence a unitary representation on `H_seed`.

This is crucially different from declaring `S4` to be gauge: the two physical polarization modes are transported, not removed.

## 24-history isometry on the symmetric seed

The 24 maximal `B4` orderings are indexed by `pi in S4`. On the seed physical space define

`V |psi> = (1/sqrt(24)) sum_pi |pi> tensor U_pi |psi>`.

Because every `U_pi` is unitary,

`V^dagger V = (1/24) sum_pi U_pi^dagger U_pi = I`.

Thus the history-register refinement isometry is exact on the symmetric seed **without** a system projector `P_sys`.

If the internal history label is operationally discarded, the corresponding channel is

`E_seed(rho) = (1/24) sum_pi U_pi rho U_pi^dagger`.

It is CPTP. Since the `U_pi` form a group representation, this finite group twirl is also idempotent:

`E_seed^2 = E_seed`.

Interpretation guard: the twirl is a symmetry/coarse-label conditional expectation, not microscopic time evolution and not a license to erase relational polarization information when reference-frame observables are retained.

## What is established

- positive finite physical quotient exists on the symmetric seed;
- physical fiber dimension is exactly 2 at each fundamental cover;
- one-cell seed physical space dimension is exactly 8;
- exact `S4` maps descend unitarily to physical quotients;
- the 24-history register isometry with amplitude magnitude `1/sqrt(24)` is exact without a system projector;
- history-forgetting gives a normalized CPTP seed channel.

Classification:

`PASS_SCOPED_SYMMETRIC_B4_SEED_PHYSICAL_HILBERT_QUOTIENT_AND_UNITARY_HISTORY_ISOMETRY`.

## What remains open

This does **not** yet derive the genuine dynamical fine-to-coarse transports on a deformed/interacting QGR configuration. The `U_pi` here are the exact permutation/frame-symmetry maps of the symmetric seed.

Open:

- physical Hilbert/rigging construction for generic curved QGR configurations;
- dynamical branch transports including nontrivial relational holonomy;
- whether interacting branch maps remain isometries/unitary on the physical quotient;
- finite quantum amplitude/measure over generic fine configurations;
- continuum/projective limit.

## Exact next gate

`QGR-ITER006-G3-DYNAMIC_HISTORY_TRANSPORT_AND_MEASURE`

Derive branch transport from the QGR connection/composition object itself and distinguish symmetry relabeling from genuine curvature/holonomy. A branch-dependent phase or amplitude may not be inserted by hand.

## Reproducibility

See `code/qgr_iter006_g2c_seed_physical_hilbert.py`.
