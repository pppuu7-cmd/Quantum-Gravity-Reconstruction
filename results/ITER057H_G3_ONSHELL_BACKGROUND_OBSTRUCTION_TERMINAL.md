# Iter057H terminal result — G3/H0 on-shell background obstruction

Date: 2026-09-15
Gate: `ITER057H-G3-H0-ONSHELL-BACKGROUND-OBSTRUCTION-FOR-EINSTEIN-WEYL3-TRUNCATION`
Prospective preregistration: `155a8a1896164ecb88fc6c1c589cde2bbe50cfef`

## Terminal classification

**`PASS_SCOPED_ITER057H_G3_H0_IS_OFFSHELL_FOR_NONZERO_C6_EINSTEIN_WEYL3_TRUNCATION__ONSHELL_BACKGROUND_REQUIRED_FOR_PHYSICAL_CHARACTERISTICS`**

## Frozen equation

Audit the local two-operator classical truncation

`E_total_ab = A_E G_ab + c6 E_W3_ab = 0`,

with finite nonzero Einstein normalization `A_E` and symbolic `c6`.

No cosmological constant, matter source or additional curvature operator is included in this scoped gate.

## Exact trace obstruction

At the source-owned G3/H0 origin, Iter057D established

`R_ab=0`, `R=0`, hence `G_ab=0`,

and in the current curvature convention

`I3=-96 kappa^3`.

Iter056X established the exact Weyl3 Euler trace identity

`g_ab E_W3^{ab}=-I3`.

Taking the trace of the frozen total equation gives

`g_ab E_total^{ab}`

`= -A_E R + c6 (-I3)`

`= 96 c6 kappa^3`.

Therefore, for

`A_E != 0`, `c6 != 0`, `kappa != 0`,

**the trace is nonzero and the frozen G3/H0 metric is not an on-shell background of the Einstein+Weyl3 truncation at the origin.**

The conclusion is exact and does not depend on a numerical value or sign of `c6`.

## Frozen escape-route audit

The trace obstruction disappears only by changing the frozen problem, for example:

1. `c6=0` — removes the Weyl3 operator and is not a derivation of the QGR coefficient;
2. `kappa=0` — collapses the probe to the Weyl-inactive background;
3. changing/correcting the background and/or adding a matter/source/additional-operator contribution that can participate in the trace equation.

None of these routes is authorized by this result.

## Consequence for Iter057F3 and later symbols

The G3/H0 source remains valid and useful for **off-shell operator reconstruction**: its explicit source-owned jet can determine `L4`, `L2`, and `L0` of the local Weyl3 Euler operator.

But a mixed-order matrix pencil assembled on this background cannot by itself be promoted to the physical characteristic/mode structure of exact Einstein+Weyl3 equations. For such a promotion one needs a background satisfying the relevant full equations/constraints, or an independently justified perturbatively corrected on-shell background construction.

This sharpens the interpretation ceiling of the current symbol programme before any F3 numerical result is consumed.

## What is not proved

This PASS does **not** show that no Weyl-active on-shell Einstein+Weyl3 solution exists. It addresses only the frozen Ricci-flat G3/H0 tidal source at its origin.

It does not establish hyperbolicity failure, birefringence, a ghost, instability, treatment selection, unitarity or UV completion.

## Production decision

No numerical CI was launched. The result follows exactly from already-certified source curvature and the exact Iter056X trace identity; numerical load would add no authority.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.