# Iter057G preregistration — exact trace-Ward validation of the G3 Weyl3 degree-two block

Date: 2026-09-15
Gate: `ITER057G-G3-WEYL3-L2-TRACE-WARD-VALIDATION`

## Timing / independence lock

This gate is frozen while Iter057F production run `34905773224` is still in progress and before any Iter057F lane/aggregate artifact has been consumed.

It is motivated by the pre-output protocol audit `results/ITER057F_PREOUTPUT_PROTOCOL_AUDIT.md`, which identified that an isolated subprincipal gauge-null condition is not a generally valid curved-background Ward identity. Iter057F's historical A-G contract is not changed.

## Frozen source and extraction dependency

Use the same source-owned G3/H0 origin, `(-,+,+,+)` convention, `kappa=0.08=2/25`, null covector `k=(1,1,0,0)`, and 10 symmetric metric basis elements as Iter057F.

This gate may consume the finest Iter057F extracted `L2_j` matrices only if the corresponding raw lane passes the following **non-gauge** controls from the frozen Iter057F contract:

- source/signature validity;
- amplitude convergence for `L2` and `L4`;
- stencil convergence for `L2` and `L4`;
- held-out frequency prediction;
- direct no-fit exact `L4` column recovery.

The Iter057F aggregate subprincipal gauge-null predicate is not a prerequisite for this successor because this gate was frozen specifically to provide the correct independent lower-order Ward control.

If one or more raw lanes fail those non-gauge extraction controls, classify this gate `BLOCKED_BY_INVALID_EXTRACTION_INPUT`, not PASS/FAIL of the Ward identity.

## Exact trace identity

Iter056X established the off-shell four-dimensional identity

`g_ab E_W3^{ab} = - I3`.

Linearize around the G3 source background at the origin under the frozen plane-wave perturbation

`h_ab(x)=H_j,ab cos(s k.x)`.

By Iter057E,

`delta E_W3(0;s)=L0_j + s^2 L2_j + s^4 L4_j`.

The term `h_ab Ebar^{ab}` from varying the metric in the trace identity is independent of `s`, so it contributes only to degree zero. `I3` depends algebraically on metric and curvature, so its linearization has only degree zero and degree two in `s`.

Therefore the degree-two coefficient satisfies the exact standalone identity

**`eta_ab (L2_j)^{ab} = - (delta I3_j)_s2`.**

## Frozen exact RHS construction and sign

Use the exact Iter054C background Weyl operator

`Wbar = tensor_to_bivector_operator(background_weyl_tensor(E))`,

with

`E = kappa * diag(1,1,-2)`

in the frozen `(-,+,+,+)` convention.

For basis input `H_j`, let

`dW_j = metric_to_weyl_operator(k,H_j)`

be the existing Iter054C principal metric-to-Weyl map. Its convention corresponds to replacing two derivatives by `+k_mu k_nu`.

The actual cosine perturbation has

`partial_mu partial_nu cos(s k.x)|_0 = -s^2 k_mu k_nu`,

so its degree-two Weyl variation is

`(delta W_j)_s2 = - dW_j`.

Since `I3=tr(W^3)` in the bivector-operator representation used by the Iter054C chain,

`(delta I3_j)_s2 = 3 tr(Wbar^2 (delta W_j)_s2)`

`                  = -3 tr(Wbar^2 dW_j)`.

Hence the frozen exact trace target is

**`T_j = +3 tr(Wbar^2 dW_j)`.**

No sign/scale fitting against numerical outputs is allowed.

## Frozen numerical comparison

For each of the ten finest extracted Iter057F `L2_j` output tensors compute

`trace_eta(L2_j)=sum_ab eta_ab (L2_j)_ab`.

Compare directly with exact rational `T_j` converted to high precision.

For each lane require

`abs(trace_eta(L2_j)-T_j) / max(abs(T_j), ||L2_j||_F, 1e-10) <= 1e-2`.

Also require aggregate relative residual

`||trace_vector - T_exact||_2 / max(||T_exact||_2,1e-10) <= 5e-3`.

The exact target vector must be computed before reading the numerical trace vector inside the implementation; no per-component sign or scale adjustment is permitted.

## Frozen classifications

Maximum PASS:

`PASS_SCOPED_ITER057G_EXTRACTED_G3_WEYL3_L2_SATISFIES_EXACT_TRACE_WARD_IDENTITY`.

Scientific/implementation discrepancy if all extraction inputs are otherwise valid but the frozen trace identity comparison fails:

`INVALID_ITER057G_EXTRACTED_L2_FAILS_EXACT_TRACE_WARD_CONTROL`.

Blocked input:

`BLOCKED_BY_INVALID_EXTRACTION_INPUT_ITER057G`.

## Interpretation ceiling

PASS would validate one exact tensor Ward identity for the extracted `L2` at one source-owned background point/covector. It would not prove a global closed-form `L2`, full characteristics, hyperbolicity, physical cone splitting, ghost content, stability, treatment selection, unitarity or UV completion.

`c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.