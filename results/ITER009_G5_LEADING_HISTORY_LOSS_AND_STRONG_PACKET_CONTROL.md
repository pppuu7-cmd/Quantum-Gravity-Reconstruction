# QGR Iter009-G5 — leading history-loss c6 order and strong packet control

Date: 2026-09-12
Status: `PASS_SCOPED_LEADING_OH4_HISTORY_MIXTURE_PURITY_C6_INDEPENDENT_UNDER_REGULAR_OH4_GEOMETRY_RESPONSE / PACKET_STRONG_CONTROL / FULL_DOMAIN_OPEN`

GitHub Actions run `34664051772`: 6 lanes + aggregate SUCCESS.

## G5A — c6 order in the history-mixture loss

Assume the self-consistent branch-relative generator has the regular same-realization expansion

`Delta X = h^2 Delta A + c6 h^4 Delta B + ...`.

The leading overlap/purity loss is quadratic in the small branch-relative generator. Therefore

`Q(Delta X,Delta X)`

contains

- `h^4 Q(A,A)`,
- `2 c6 h^6 Q(A,B)`,
- `c6^2 h^8 Q(B,B)`.

Thus the leading `O(h^4)` history-mixture loss is `c6` independent and the first `c6` dependence appears at `O(h^6)`, provided no singular `1/h` enhancement changes the regular power counting.

Classification:
`PASS_SCOPED_IF_SELF_CONSISTENT_C6_GEOMETRY_CORRECTIONS_ENTER_BRANCH_GENERATORS_AT_OH4_THE_LEADING_QUADRATIC_HISTORY_MIXTURE_LOSS_AT_OH4_IS_C6_INDEPENDENT_AND_C6_FIRST_ENTERS_AT_OH6`.

## G5B — common geometry shifts

Any common unitary correction `V` applied to all branch outputs maps

`rho_out -> V rho_out V^dagger`.

Purity is exactly invariant:

`Tr[(V rho V^dagger)^2]=Tr[rho^2]`.

Therefore a common `O(h^4)c6` geometry shift cannot change the history-mixture purity at any order.

## G5C — observable-specific boundary

A common unitary can change an absolute coherent observable linearly. An explicit qubit witness with

`rho=|0><0|`, `O=sigma_x`, `V=exp(-i epsilon sigma_y/2)`

gives `<O>_epsilon=sin(epsilon)` and unit linear response at zero.

Hence `c6` decoupling is specific to the relative history-mixture purity class; absolute phase/time-delay/coherent propagation observables can remain `O(h^4)c6` sensitive.

## G5D — extended repaired-G9 branch spread

The repaired-G9 relative Lorentz-generator calculation was extended to

`h = 1/4, 1/8, 1/16, 1/32, 1/64`.

The exact workflow test again finds a log-log slope in the predeclared `1.8..2.2` window and a bounded `h^-2`-rescaled RMS with max/min ratio below `1.35` over the tested sequence.

Classification:
`NUMERICALLY_VERIFIED_SCOPED_REPAIRED_G9_BRANCH_RELATIVE_LORENTZ_GENERATOR_REMAINS_OH2_TO_H_1_OVER_64_WITH_BOUNDED_H_MINUS2_RESCALED_RMS`.

This is a deeper numerical asymptotic check, not an analytic uniform theorem.

## G5E — exact packet strong-distance scaling

Use the exact G6F overlaps

`A0(gamma)=2/(1+gamma)`,

`A1(gamma)=4(2+gamma)/(3(1+gamma)^2)`.

If the relative rapidity `r=O(h^2)`, then `gamma=cosh r=1+O(h^4)`. For normalized states,

`||psi_r-psi_0||^2 = 2(1-Re A)`.

Therefore both specified packet families have state distance `O(r)=O(h^2)`. The numerical exact-formula audit gives log-h slopes in `1.9..2.1`; a dyadic `h^2` series is summable.

Classification:
`PASS_SCOPED_GIVEN_THE_VERIFIED_OH2_RELATIVE_RAPIDITY_LAW_THE_SPECIFIED_G6F_PACKET_STATES_HAVE_OH2_STRONG_DISTANCE_AND_A_SUMMABLE_DYADIC_REFINEMENT_BOUND`.

## G5F — strong versus operator-norm convergence

Full operator norm is not a necessary convergence topology for continuous unitary representations. For translations on `L2(R)`,

`||U_a-I||_op=2`

for every nonzero `a` (Fourier witness `k=pi/a`), while `U_a->I` strongly as `a->0`.

This shows why the previous diamond/operator-norm criterion was sufficient but overly strong. QGR should target a justified strong limit on the physical state domain, then trace-norm convergence for normal states.

## Consolidated classification

`PASS_SCOPED_LEADING_OH4_HISTORY_MIXTURE_PURITY_IS_C6_INDEPENDENT_UNDER_REGULAR_SELF_CONSISTENT_OH4_C6_GEOMETRY_CORRECTIONS__SPECIFIED_G6F_PACKET_DOMAIN_HAS_SUMMABLE_STRONG_REFINEMENT_CONTROL__ABSOLUTE_COHERENT_C6_RESPONSE_AND_FULL_DOMAIN_LIMIT_REMAIN_OPEN`.

## Next gate

`QGR-ITER009-G6-DENSE-DOMAIN-STRONG-LIMIT-AND-MICROSCOPIC-C6-IDENTIFIABILITY-DECISION`

Required:

1. establish local uniqueness/continuity of the microscopic torsion branch at the flat refinement point by auditing the exact `24x24` Jacobian rank;
2. use strong continuity of the induced Lorentz/Koopman action on the physical `L2` characteristic Hilbert space;
3. promote finite branch strong convergence to trace-norm convergence of the 24-history channel for normal states;
4. audit serial fixed-macroscopic-time accumulation of `O(h^2)` branch-relative corrections;
5. make a final decision whether `c6` is identifiable from current microscopic authority or must be handed to a new finite-cell UV iteration;
6. close Iter009 either positively or with an explicit scoped blocker rather than leaving an ambiguous percentage.
