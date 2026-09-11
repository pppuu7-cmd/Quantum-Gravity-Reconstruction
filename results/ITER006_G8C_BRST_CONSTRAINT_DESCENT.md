# QGR Iter006-G8C — BRST constraint descent from the derived frame-pullback algebra

Date: 2026-09-11
Status: `PASS_SCOPED_ALGEBRAIC_PHYSICAL_CONSTRAINT_DESCENT / POSITIVE_GENERIC_PHYSICAL_INNER_PRODUCT_OPEN`

## Question

Can the generic curved derivative/frame constraint structure be implemented without a global normalized average over a noncompact gauge group and without choosing a preferred gauge-fixed projector?

## Input already established

QGR derived the finite/infinitesimal frame-pullback transformation of the same second-moment field and verified the exact algebra

`[delta_xi,delta_eta] G = delta_[xi,eta] G`,

with

`[xi,eta]^i = xi^k D_k eta^i - eta^k D_k xi^i`.

No structure constants/functions were fitted to gravity; this algebra follows from composition of the relational frame relabelings.

## Nilpotent differential

Introduce the Grassmann-odd ghost field `c` valued in the same frame-relabeling generator space and define

`s G = L_c G`,

` s c = -(1/2)[c,c]`.

For any covariant QGR tensor/response observable `O`, define

`s O = L_c O`

with the corresponding tensorial pullback action.

Using the already proved commutator identity and the Jacobi identity of the vector-field bracket gives

`s^2 G = 0`,

`s^2 c = 0`,

and therefore `s^2=0` on the covariant observable algebra.

No new continuous coupling or history function appears in this construction.

## Physical observable algebra

Define the algebraic physical observables on a generic curved finite complex by the ghost-number-zero cohomology

`A_phys = H^0(s)`.

This replaces the need to define physical states by a normalized noncompact group average.

At the symmetric seed, this is compatible with the previously constructed ordinary quotient

`ker H / im R`,

which has two physical modes per fundamental cover.

## Compatibility with finite transports and blocking

The finite edge/path transports are constructed covariantly from the same QGR frame/connection data. Therefore a frame relabeling acts functorially on path transports, and the blocked transport

`A_p = product_e A_e`

transforms in the same way as the fine composition.

Hence the exact path-groupoid blocking map is an `s`-chain map:

`B s = s B`.

It therefore induces a well-defined map on BRST cohomology classes.

This is the algebraic physical-descent counterpart of the exact strong-curvature projective observable closure established in G7B.

## Compatibility with the history instrument

If the branch configuration map is covariant and the branch action is gauge invariant on the verified local domain, the branch operator

`K_alpha=24^(-1/2) exp(iS_alpha/hbar) U_alpha`

intertwines the BRST differential. Thus the normalized history instrument descends to cohomology on that domain.

Through the currently verified local action order, this gives a scoped algebraic physical channel rather than merely a kinematic channel.

## Classification

`PASS_SCOPED_NILPOTENT_BRST_COMPLEX_AND_PROJECTIVE_CONSTRAINT_DESCENT_FROM_DERIVED_QGR_GAUGE_ALGEBRA`.

## Boundary

BRST cohomology is not by itself a proof of a positive-definite generic curved physical inner product. Remaining tasks are:

- construct/verify positivity of the generic physical state pairing or an operational positive-state completion;
- control singular/reducible gauge orbits and possible cohomology jumps;
- prove global finiteness of strong-curvature torsion-free branch sums;
- extend the interacting action/control beyond the currently verified local order;
- close continuum/RG and normalized phenomenological observables.
