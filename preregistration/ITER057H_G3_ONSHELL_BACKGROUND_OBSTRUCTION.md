# Iter057H preregistration — G3/H0 on-shell background obstruction for Einstein+Weyl3 truncation

Date: 2026-09-15
Gate: `ITER057H-G3-H0-ONSHELL-BACKGROUND-OBSTRUCTION-FOR-EINSTEIN-WEYL3-TRUNCATION`

## Motivation

Iter057D/E/F3 use the source-owned G3/H0 tidal metric as a local Weyl-active probe for operator reconstruction. Before any future physical characteristic/hyperbolicity interpretation, determine whether this same background is actually a solution of the exact local Einstein plus Weyl3 truncated field equations at the frozen origin.

This question is independent of the numerical Iter057F3 extraction.

## Frozen equation class

Audit only the classical local truncation used in the current mixed-symbol chain:

`E_total_ab = A_E G_ab + c6 E_W3_ab = 0`,

where `A_E` is any finite nonzero Einstein normalization and `c6` is symbolic. No cosmological constant, matter source or additional curvature operator is introduced in this gate.

The result is therefore scoped to this two-operator truncation, not an all-operator QGR theorem.

## Frozen source facts

Use only already-established authority:

1. Iter057D source-owned G3/H0 origin:
   - `R_ab(0)=0`, `R(0)=0`, hence `G_ab(0)=0`;
   - in the current principal-curvature convention `I3(0)=-96 kappa^3`, nonzero for `kappa != 0`.
2. Iter056X exact trace identity for the Weyl3 Euler tensor:

   `g_ab E_W3^{ab} = -I3`.

No numerical F/F2/F3 output is needed.

## Frozen obligations

A. Take the trace of the frozen total equation at the G3 origin.

B. Show or refute that for finite nonzero `A_E`, `c6 != 0` and `kappa != 0`, the trace can vanish.

C. Distinguish three logically different escape routes without authorizing any of them:

- `c6=0` (removes the Weyl3 correction and is not a derivation of QGR `c6`);
- `kappa=0` (collapses to the Weyl-inactive background);
- modification of the background and/or inclusion of additional source/operator terms.

D. State the implication for downstream characteristic analysis: a local linearized operator may still be computed off shell as an operator diagnostic, but physical mode/hyperbolicity claims for exact equations require a background satisfying the relevant equations/constraints.

E. Do not infer that no Weyl-active solution of Einstein+Weyl3 exists; the gate concerns only the frozen G3/H0 source metric at the origin.

## Frozen classifications

PASS if the exact trace obstruction is established:

`PASS_SCOPED_ITER057H_G3_H0_IS_OFFSHELL_FOR_NONZERO_C6_EINSTEIN_WEYL3_TRUNCATION__ONSHELL_BACKGROUND_REQUIRED_FOR_PHYSICAL_CHARACTERISTICS`.

Scientific FAIL if the trace can vanish with nonzero `c6,kappa` under the frozen two-operator equation without adding another term:

`SCIENTIFIC_FAIL_ITER057H_PROPOSED_G3_ONSHELL_OBSTRUCTION_FALSE`.

INVALID if a cosmological constant, matter source, extra operator or fitted `c6` is silently inserted.

## Claim locks

No claim that Weyl-active solutions are absent. No treatment selection, hyperbolicity theorem, ghost/mode count, stability, unitarity, UV completion or experiment. `c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.