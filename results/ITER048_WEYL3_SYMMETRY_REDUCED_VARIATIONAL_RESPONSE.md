# QGR Iter048 — Weyl^3 symmetry-reduced variational response

Date: 2026-09-13
Status: `PASS_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE`

## Authority and provenance

- Preregistration: `status/ITERATION_048.md`
- Preregistration commit: `278ec25f089430a09d8b64540cbc57ed481f4fce`
- Scientific implementation commit: `b618e848785e96ed6968e5ca06282d84c7925950`
- Frozen aggregate commit: `4da8340f0dbc1a2ff1a51a55ff1fb8061592b992`
- Initial workflow commit: `983521bef48fcb2feb73f3c1f0137e5a679079c9`
- Workflow YAML-only correction: `3513818d3f50a93c1d62743d7013cae1bc7f4b61`
- Run-authority record: `status/ITERATION_048_RUN_AUTHORITY.md`, commit `9ddba17221e83ca96255a8a382a82692462eb21d`
- First trigger run `34719340456`: `ITER048_PREPRODUCTION_WORKFLOW_INVALID_ZERO_SCIENTIFIC_EVIDENCE`; zero jobs and zero scientific artifacts; no scientific authority.
- Authoritative trigger/head: `68cf38c745f146039cf63ed0f345e24bd87d5f01`
- Authoritative run: `34719396082`
- Aggregate job: `103622629715`
- Aggregate artifact: `10305449033`
- Aggregate digest: `sha256:2d183a735d97408c1145b077cb9817ec6f4456aaa7d3e405de916ff596cafb97`

The preregistered scientific criteria were unchanged after production inspection. The only retry change was workflow serialization; the invalid first run produced no scientific evidence.

## Terminal aggregate

The frozen aggregate downloaded and consumed all **24/24** scientific lane artifacts and returned:

- expected scientific lanes: **24**;
- found scientific lanes: **24**;
- passes: **24**;
- fails: **0**;
- controls valid: **true**;
- stream counts: `A=6, B=6, C=6, D=6`;
- `c6_status = SYMBOLIC_UNFIXED_COEFFICIENT_ONLY`.

Terminal classification:

`PASS_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE`

Scope lock:

`LAPSE_RETAINING_AXISYMMETRIC_BIANCHI_I_REDUCED_VARIATION_ONLY_NOT_FULL_COVARIANT_SIX_DERIVATIVE_EOM`

## What was derived

Using the lapse-retaining axisymmetric Bianchi-I metric

`ds^2 = -N(t)^2 dt^2 + a(t)^2 dx^2 + b(t)^2(dy^2+dz^2)`,

the production code constructs the full metric curvature and Weyl tensor directly, forms the coefficient of `c6` in

`L6 = N a b^2 W3`,

and derives the generalized higher-derivative Euler-Lagrange operators `E_N`, `E_a`, `E_b` **before** any Kasner or isotropic background substitution.

No numerical value or sign was assigned to `c6`.

## Representative exact evidence

### A — exact vacuum Kasner activation

For the exact axisymmetric Ricci-flat Kasner profile

`N=1`, `a=t^(-1/3)`, `b=t^(2/3)`,

the production result is exactly

- `W3 = 256/(243 t^6)`;
- `L6 = 256/(243 t^5)`;
- `E_N = 1024/(243 t^5)`;
- `E_a = 4096/(243 t^(14/3))`;
- `E_b = -5632/(243 t^(17/3))`.

All three reduced variational responses are nonzero for positive finite `t`. The Ricci tensor remains exactly zero for the uncorrected Kasner background.

Thus a nonzero `c6` would contribute nontrivially to the reduced field equations on this Weyl-active background.

### B — curved conformally-flat negative control

A representative isotropic control used

`N=1+t^2/7`, `a=b=2+t+t^3/5` at `t=1/4`.

It has **24 nonzero Riemann components** at the witness, yet after the generic variational derivation and only then imposing isotropy:

- Weyl tensor = 0 exactly;
- `W3 = 0`;
- `E_N = E_a = E_b = 0` exactly.

This excludes generic nonzero curvature itself as the source of the six-derivative response.

### C — generic anisotropic power-law certificate

For the held-out pair `p=-2/3`, `q=1/2`, the exact production output gives

- `W3 = 42875/(13122 t^6)`;
- `L6 = 42875/(13122 t^(17/3))`;
- `E_N = 145775/(13122 t^(17/3))`;
- `E_a = 608825/(13122 t^5)`;
- `E_b = -420175/(6561 t^(37/6))`.

All preregistered power-law certificate formulae matched exactly.

### D — time-reparameterization control

For `t = tau^(1/2)`, the reparameterized Kasner witness remained exactly Ricci-flat and gave

- `W3 = 256/(243 tau^3)`;
- reduced density `L6 = 128/(243 tau^3)`;

in exact agreement with the preregistered one-dimensional density transformation law.

## Scientific interpretation

Iter047 established where the selected QGR `Weyl^3` scalar is algebraically active. Iter048 goes one step further: in a lapse-retaining, anisotropic, curved symmetry reduction, the coefficient multiplying `c6` in the **actual generalized variational equations** is nonzero on exact Kasner and exactly zero in the conformally-flat isotropic controls.

This closes a real roadmap blocker between “nonzero invariant” and “dynamical response” for one independent curved symmetry sector.

## What is not established

A full PASS here does **not** establish:

- the complete four-dimensional covariant Euler-Lagrange tensor of `Weyl^3`;
- that the full corrected theory admits or excludes a nearby Kasner solution;
- a numerical value or sign of `c6`;
- generic strong-field or nonlinear stability;
- renormalizability or quantum unitarity;
- experimental confirmation;
- physical correctness of the full QGR candidate.

`theory established` therefore remains **0%**.

## Next frontier

The next high-value step should leave this Bianchi-I reduction. Preferred targets are:

1. an independent lapse-retaining **spherically symmetric variational reduction** evaluated only after generic variation on Schwarzschild/Petrov-D, or
2. a genuinely covariant directional-variation / functional-derivative certificate for `sqrt(-g) Weyl^3`.

Either route must keep `c6` symbolic and must not be promoted beyond its actual scope.
