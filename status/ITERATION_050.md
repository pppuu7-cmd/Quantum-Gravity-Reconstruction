# Iteration 050 — Covariant Weyl^3 curvature-directional variation prerequisite

Status: **PREREGISTERED BEFORE IMPLEMENTATION/PRODUCTION**
Date: 2026-09-13

## Motivation
Iter048 and Iter049 established scoped nonzero variational response of the coefficient of symbolic `c6` in two independent curved symmetry reductions. A third reduction is not allowed merely to accumulate evidence. The next prerequisite must leave symmetry reduction.

## Frozen scientific object
In four spacetime dimensions define

`I3 = C_{mu nu}^{ rho sigma} C_{rho sigma}^{ alpha beta} C_{alpha beta}^{ mu nu}`

with Lorentzian metric and the standard Weyl projection of an algebraic Riemann tensor. `c6` is an overall symbolic coefficient and remains unfixed.

This gate concerns the **local curvature-direction derivative** of `I3` at fixed metric: for an algebraic-curvature perturbation `delta R` generated independently of the target curvature,

`D_R I3[delta R]`.

The analytic comparator is obtained by first applying the fixed-metric linear Weyl projector to `delta R`, then differentiating the cubic contraction, giving the three cyclic insertions of `delta C`. No field equation or integration-by-parts identity is assumed.

## Frozen lane families
Use 12 deterministic non-symmetry-reduced Lorentzian algebraic-curvature lanes generated from independent Riemann-normal-coordinate second-metric-jet seeds. Each lane uses an independent directional second-jet seed. No lane may be selected after observing the result.

Controls:
1. algebraic Riemann symmetries and first Bianchi residuals;
2. Weyl trace residual;
3. centered finite-difference directional derivatives at `h={1e-3,5e-4,2.5e-4,1.25e-4}`;
4. analytic-vs-numerical derivative convergence with the expected centered-difference trend;
5. two fixed proper Lorentz basis transformations per lane, transforming metric, curvature and direction covariantly;
6. conformally-flat curvature controls with `C=0`, requiring `I3=0` and cubic first directional derivative zero at that base point;
7. a nonzero-Weyl calibration condition so trivial all-zero lanes cannot pass.

## Frozen thresholds
- algebraic Riemann symmetry/Bianchi max residual `<= 1e-11`;
- Weyl trace max residual `<= 1e-10`;
- Lorentz-basis scalar covariance relative discrepancy `<= 1e-9`;
- Lorentz-basis analytic directional-derivative covariance relative discrepancy `<= 1e-8`;
- finest-step analytic-vs-centered-FD derivative relative discrepancy `<= 2e-6` (absolute fallback `<= 1e-9` when analytic derivative magnitude is below `1e-6`);
- last two FD errors must not worsen by more than factor `1.05`; at least one halving step among the final two must improve error by factor `>= 2.5` unless already below absolute `1e-10`;
- conformally-flat `|I3| <= 1e-11` and `|D_R I3| <= 1e-10`;
- nonzero calibration: at least 10/12 generic lanes must satisfy `|I3| > 1e-7` and `|D_R I3| > 1e-7`.

## Frozen classification
- `INVALID_COVARIANT_CURVATURE_DATA_OR_CONTROL` if algebraic/trace/null validity controls fail.
- `SCIENTIFIC_FAIL_WEYL3_CURVATURE_DIRECTIONAL_CERTIFICATE` if valid data fail derivative agreement/convergence or Lorentz covariance.
- `PASS_SCOPED_COVARIANT_WEYL3_CURVATURE_DIRECTIONAL_VARIATION_PREREQUISITE` only if all 12 generic lanes and all frozen controls pass.

## Claim lock
Even a complete PASS certifies only a fixed-metric curvature-direction/P-tensor prerequisite for the local Weyl-cubic invariant on the frozen generic panel. It is **not** the full metric functional derivative of `sqrt(-g) I3`, does not establish the covariant `∇∇P` term, is not a global theorem, does not fix `c6`, does not authorize `beta=1`, and does not establish QGR as a theory or provide experimental confirmation.

## Next-gate rule
Only after terminal classification may a full metric functional-derivative gate be preregistered. If this gate fails scientifically, preserve the failure and localize projector/contraction/covariance defects without retuning thresholds. Numerical/infrastructure failure must be repaired minimally without changing this frozen scientific object.