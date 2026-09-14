# Iter055Z terminal result — GR-limit continuity is not a sufficient mixed-order branch selector

Date: 2026-09-14
Preregistration: `0e88f1bcb6dd42fcc1149fd6475e1e2f7eb38757`

## Terminal classification

`FAIL_SCOPED_ITER055Z_GR_LIMIT_CONTINUITY_ALONE_DOES_NOT_EXCLUDE_SINGULAR_BRANCH__STRONGER_ASYMPTOTIC_SELECTION_REQUIRED`

## 1. Exact control solution

For

`u'' + eps u'''' = 0`, `eps>0`,

the characteristic equation is

`r^2(1+eps r^2)=0`.

Hence the exact real solution space is

`u_eps(t)=a_eps+b_eps t+c_eps cos(t/sqrt(eps))+d_eps sin(t/sqrt(eps))`.

The lower-order/GR-limit equation `u''=0` has solutions

`u_GR(t)=a+b t`.

The `cos/sin` terms are the fast singular-scale branch of this control.

## 2. Ordinary convergence does not remove the fast branch

Take fixed `a,b` and

`u_eps(t)=a+b t+delta(eps) sin(t/sqrt(eps))`

with any nonzero `delta(eps)->0`.

On every compact interval `|t|<=T`,

`sup |u_eps-u_GR| <= |delta(eps)| ->0`,

while the fast branch remains nonzero for every `eps>0`.

Therefore field-level GR-limit continuity alone is not a branch selector.

## 3. Any fixed finite C^m topology can also be fooled

The n-th time derivative of the fast term has magnitude bounded by

`|delta(eps)| eps^(-n/2)`.

For any preregistered fixed finite `m`, choosing for example

`delta(eps)=eps^((m+1)/2)`

makes all derivatives of order `0<=n<=m` tend uniformly to zero on compact intervals, while the fast component remains nonzero for every `eps>0`.

Thus no unspecified statement of convergence in a fixed finite derivative norm is sufficient.

## 4. Even C-infinity compact convergence does not remove the branch

Choose the stronger witness

`delta(eps)=exp(-1/eps)`.

For every fixed derivative order `n`,

`sup |partial_t^n [delta(eps) sin(t/sqrt(eps))]| <= exp(-1/eps) eps^(-n/2) ->0`.

Therefore, on every compact time interval, `u_eps -> u_GR` simultaneously in every finite `C^n` seminorm: the family converges in the usual `C^infinity` Frechet topology while a nonzero fast branch is present at each positive `eps`.

The fast component is **beyond all algebraic orders** in `eps`: it is invisible to every finite-order perturbative expansion and to the full formal power series at `eps=0`.

## 5. What stronger information would actually distinguish the sector

The counterexample shows that a future mixed-order treatment rule needs more than smooth convergence to GR. Logical possibilities include, but are not selected here:

- require real-analytic dependence or membership in a specified asymptotic power-series sector in the higher-derivative parameter;
- explicitly project onto the regular perturbative branch/order-reduce the equations;
- impose a uniform norm that weights the singular derivative scale strongly enough and is itself physically/source-defined;
- specify microscopic initial-data/preparation conditions that set the fast-sector amplitudes exactly to zero;
- derive another QGR-internal superselection/treatment principle.

Each option changes the dynamical object and therefore requires its own prospective QGR candidate-version gate.

## Relation to existing QGR results

Iter054E established a regular GR-connected branch and singular formal branch in a mixed-order symbolic proxy. Iter054F showed that the QGR-specific mixed-order evolution object is not yet defined. Iter054G-R showed that exact versus order-reduced physical treatment is not source-selected. Iter055W/Y sharpened the scaling consequences of retaining a nonzero Weyl3 correction.

Iter055Z adds a treatment-principle falsification result: **“choose solutions that smoothly approach GR” is not strong enough to define the order-reduced/regular sector.** Exponentially small fast components survive every finite-order and smooth compact convergence test.

## Next highest-information gate

The next admissible selector-control question is whether **analytic/formal-power-series dependence on the higher-derivative parameter** is sufficient to exclude the singular branch in the same control, and whether existing QGR microscopic/refinement authority supplies any reason to require such analyticity of physical solutions rather than merely analyticity of the action/operator coefficients. These are distinct obligations: mathematical sufficiency and QGR source authority should be audited separately.

## Claim ceiling

No QGR treatment rule is selected. No tensorial QGR extra mode, ghost, instability, strong hyperbolicity, unitarity, c6 running, cutoff, UV completion, regulator removal, full GR recovery, experiment or theory establishment is inferred. Theory established remains 0%.

No GitHub Actions run was required; the result is exact ODE/asymptotic analysis.
