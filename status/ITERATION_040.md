# Iteration 040 — calibration-free Weyl-active response manifold

Date: 2026-09-12
Status: `PREREGISTERED / READY FOR PRODUCTION`

## Motivation

Iter039 established that the current QGR authority has an exact source-scale null direction and no
absolute identifying equations for `(u=beta^2,c6)`. Therefore beta is an explicit matching/calibration
parameter under current authority and c6 remains an unfixed Wilson direction until a genuine
Weyl-active absolute datum exists.

This does **not** mean QGR has no predictions before calibration. The G10 same-field-content
Weyl-active construction already establishes a nonzero local Weyl-cubic response direction, and
G32+G38 now provide a scoped principal projective-action/refinement mechanism. Iter040 therefore asks
for **parameter-free shape information** of the Weyl-cubic response: signs, nulls, amplitude powers,
shape ratios and rotational invariance. In the six-derivative correction `Delta S6 = c6 * K_W3`, c6
is retained as an overall unfixed multiplier; this gate audits the response kernel `K_W3`, not an
absolute measured phase.

No beta or c6 value is fitted or introduced.

## Frozen generalized tidal family

Use the existing G10 G3 weak static vacuum metric form

`Phi(y) = (kappa/2) y_spatial^T H y_spatial`,
`g00 = 1+2 Phi`, `gij = -(1-2 Phi) delta_ij`,

with trace-free symmetric spatial Hessian H. This stays inside the same QGR second-moment/torsion
field arena; no new field components are added.

Frozen unrotated Hessian shapes:

- `H0 = diag(1,1,-2)`, `tr(H0^3)=-6` (original G10 G3 witness);
- `H1 = diag(1,2,-3)`, `tr(H1^3)=-18`;
- `H2 = diag(1,-1,0)`, `tr(H2^3)=0` but `H2 != 0`;
- `H3 = diag(2,-1,-1)`, `tr(H3^3)=+6`.

Thus H2 is a frozen null-test for the parity-even cubic Weyl response, while H0/H3 form a sign-reversed
pair and H1 supplies a distinct nonzero cubic magnitude.

## Stream A — refinement and cubic-null/sign structure

Four lanes, one per H shape. Each lane computes the same G10 holonomy-curvature/Weyl proxy at
`h=[0.125,0.10,0.08,0.0625,0.05]`, fixed `kappa=0.06`.

For H0/H1/H3 PASS requires:

- all torsion solves residual-qualified and Jacobian-nondegenerate under the inherited G10 tolerance;
- Weyl norm remains nonzero and refinement-stable;
- the sign of Weyl^3 at the finest two h values agrees with `sign tr(H^3)` up to one common global
  convention sign inferred from H0 (i.e. relative signs H0/H1 same, H3 opposite);
- `|W3|/||W||^3` remains finite and nonzero at the finest level.

For H2 PASS requires:

- nonzero Weyl norm;
- `|W3|/||W||^3 < 0.08` at the finest level;
- that normalized cubic-null residual decreases from the coarsest to the finest grid.

This is a finite numerical continuum-proxy check, not an analytic curvature theorem.

## Stream B — amplitude power law

Three lanes for H0/H1/H3 at fixed `h=0.05`, amplitudes
`kappa=[0.025,0.04,0.06,0.08,0.10]`.

PASS requires log-log slopes:

- Weyl norm vs kappa in `[0.85,1.15]`;
- absolute Weyl^3 vs kappa in `[2.70,3.30]`.

This generalizes the original single-shape G10 G3 cubic-amplitude result.

## Stream C — shape-ratio universality

Three lanes compare the nonzero shapes at each of `h=[0.10,0.075,0.05]`, fixed `kappa=0.05`.

Define `q(H,h)=W3(H,h)/tr(H^3)`. PASS requires, at the lane h:

- all q values finite and nonzero;
- max relative spread of q across H0/H1/H3 `<0.20` at h=0.10, `<0.12` at h=0.075`, and `<0.08` at h=0.05.

If PASS, ratios of the six-derivative response kernels approach the exact tidal cubic-shape ratios
`tr(H_a^3)/tr(H_b^3)` independent of c6.

## Stream D — rotational invariance recovery

Four lanes rotate H0 by frozen proper spatial rotations while keeping the lattice/basis construction
otherwise unchanged:

- identity;
- 30 degrees about z;
- 45 degrees about y;
- composition Rz(35 deg) Ry(25 deg).

Each lane computes `h=[0.10,0.075,0.05]`, fixed kappa=0.05. Relative to the identity continuum-proxy
sequence, PASS requires:

- Weyl norm and Weyl^3 remain finite/nonzero;
- relative difference in the normalized cubic response `W3/||W||^3` at the finest h `<0.10`;
- finest-h discrepancy is smaller than the coarsest-h discrepancy unless already `<1e-4`.

The identity lane is a control. This is numerical recovery of rotational invariant response within the
finite discretization, not a proof of exact lattice rotational symmetry.

## Stream E — calibration-free prediction table

Six exact/control lanes construct only dimensionless or normalized response relations from the frozen
Hessian invariants. PASS requires exact algebraic facts:

- H0:H1:H3 cubic traces = `-6:-18:+6 = 1:3:-1` up to a common factor;
- H2 has nonzero quadratic norm but zero cubic trace;
- multiplying the response by arbitrary nonzero c6 leaves all nonzero-shape response ratios and the
  H2 null unchanged;
- beta does not enter the pure Weyl^3 response-kernel ratios.

These relations are model-response predictions conditional on the Weyl^3 operator structure; they are
not absolute phase predictions.

## Production matrix

- Stream A: 4 lanes;
- Stream B: 3 lanes;
- Stream C: 3 lanes;
- Stream D: 4 lanes;
- Stream E: 6 lanes;
- total **20 scientific lanes** + aggregate, fail-fast disabled.

## Terminal classification

`PASS_SCOPED_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD_ESTABLISHED`
requires every frozen A–E lane to pass.

If PASS, QGR gains a parameterized/testable six-derivative response manifold even while c6 is unfixed:
relative tidal-shape ratios, amplitude cubic law, sign reversal, cubic-null profile and rotationally
invariant continuum-proxy structure. A future genuine Weyl-active absolute phase measurement/matching
datum would set the common c6 amplitude rather than determine these shape relations anew.

`PARTIAL_OR_CONTROL_INVALID_WEYL3_RESPONSE_MANIFOLD`
if any frozen stream fails.

## Claim locks

- c6 remains an unfixed overall coefficient;
- beta remains an explicit matching/calibration parameter under G39;
- response-kernel ratios are not absolute quantum phases;
- the weak tidal family is a scoped same-field-content realization, not arbitrary spacetime;
- finite discretization convergence is not an analytic continuum theorem;
- theory established remains 0%;
- no experimental confirmation;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.
