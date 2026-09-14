# Post-Iter054F outcome-independent analysis — exact vs order-reduced Weyl3 dynamics

Date: 2026-09-14

Status: **analysis / preparation only**. This file is not a preregistration, does not classify Iter054F, and does not authorize a downstream gate while Iter054F is non-terminal.

## 1. Why the fork is unavoidable

The current QGR action-level line contains the Einstein two-derivative sector plus a symbolic coefficient `c6` multiplying the curvature-cubic `Weyl^3` operator. Iter054A established a structural point that matters here: a curvature-algebraic cubic metric action generically gives fourth-order metric Euler-Lagrange equations on Weyl-active backgrounds, while the extra exact characteristic branch in a schematic mixed-order polynomial is singular/non-analytic in the small higher-derivative coefficient.

Iter054E then certified the finite exact proxy

`P(z;eps,lambda) = z + eps*lambda*z^2 = z(1+eps*lambda*z)`

with branches

`z_GR = 0`,

`z_HD = -1/(eps*lambda)`.

That algebra does not by itself decide which solutions belong to the physical QGR dynamical domain.

## 2. Exact higher-derivative treatment

If the local action is taken as an exact classical dynamical action at finite nonzero `c6`, the fourth-order Euler-Lagrange system must be supplied with a mathematically explicit higher-derivative evolution formulation (or an equivalent first-order reduction). Generically this entails more initial-data structure than the Einstein second-order branch.

In this treatment the singular branch is part of the exact characteristic equation whenever it lies in the real characteristic domain. Its existence still does **not** determine:

- norm/residue sign;
- whether it is a propagating physical degree of freedom after gauge/constraints;
- whether the system is strongly hyperbolic;
- whether the branch lies inside a valid continuum/microscopic domain;
- quantum ghost/unitarity status.

Those require the full evolution object and physical-state structure.

## 3. Perturbative / order-reduced treatment

If `c6*Weyl^3` is instead an effective correction valid only as a finite expansion around the Einstein branch, the admissible solution space is not automatically the complete solution space of the exact fourth-order equation.

A finite perturbative ansatz analytic in `c6` remains on the GR-connected branch. The proxy branch

`z_HD ~ 1/c6`

is non-analytic at `c6=0` and therefore cannot be obtained from a finite Taylor expansion around the GR branch. In an order-reduced formulation, higher time derivatives may be eliminated order by order using lower-order equations, leaving a lower-order effective evolution system within a declared validity domain.

This does not prove that order reduction is the correct QGR treatment. It only shows that the exact and perturbative formulations are mathematically different theories of admissible histories unless a microscopic principle relates them.

## 4. Schematic scale implication

Because `z` is a squared characteristic scale in the Iter054A/E proxy, the extra exact root corresponds schematically to a momentum/frequency scale

`|k_HD| ~ |eps*lambda|^(-1/2)`

when the sign permits a real branch.

Whether that scale is inside or outside the QGR continuum/EFT validity domain cannot be decided while:

- `c6` is symbolic/unfixed;
- the background-dependent eigenvalue factor represented by `lambda` is not promoted to a full open-region physical eigenchannel;
- no derived continuum cutoff / microscopic matching scale is supplied for this question.

Therefore the existence of the algebraic singular branch is not yet a physical extra-particle theorem.

## 5. What can choose the treatment without post-hoc branch selection

Under the QGR construction constitution, the dynamical treatment cannot be selected merely because one choice gives a preferred stability or spectrum outcome. A legitimate selection must come from an independently derived QGR principle, for example one of the following if the repository can actually derive it:

1. a microscopic continuum-limit theorem showing that the local `Weyl^3` action is the exact finite-`c6` generator on its full solution space;
2. a controlled derivative/scale expansion with a derived cutoff and error estimate that authorizes order reduction;
3. a derived state/measure or coherent-phase prescription that suppresses or excludes non-analytic branches before seeing their stability properties;
4. a canonical auxiliary-field/reduction construction whose additional initial data are independently part of the QGR state space;
5. another explicit microscopic rule that fixes the admissible-history domain.

Absent such authority, choosing exact versus order-reduced dynamics would be an additional model assumption.

## 6. Relation to strong hyperbolicity

Strong hyperbolicity cannot be inferred from the shared characteristic polynomial alone. Even two first-order systems with the same real characteristic polynomial can differ in eigenvector completeness (the frozen Iter054F diagonalizable-vs-Jordan control tests exactly this logical point).

Moreover, an exact fourth-order treatment and an order-reduced second-order treatment require different evolution variables and principal systems. A hyperbolicity verdict is therefore formulation-dependent until QGR fixes the dynamical treatment and the corresponding evolution object.

## 7. Outcome-independent next-question map

If Iter054F terminally finds the evolution object already defined, the next admissible task is a separate open-region hyperbolicity/symmetrizer audit of that exact object.

If Iter054F terminally finds the object underdefined, the next high-information gate should ask whether existing QGR microscopic authority selects one dynamical treatment without post-hoc choice. If no such principle exists, the scientifically correct state is a dynamical-treatment/object-definition blocker, not a guessed reduction.

## Claim ceiling

This analysis does not choose a treatment, prove a ghost, prove stability/instability, fix `c6`, set `beta=1`, establish strong hyperbolicity, define a quantum amplitude/measure, establish UV completion or GR recovery, or raise theory established above 0%.
