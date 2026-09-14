# Iter057G pre-output normalization invalidation

Date: 2026-09-15
Status: `PRE-OUTPUT CONTROL NORMALIZATION INVALID / NO SCIENTIFIC RESULT`

Original preregistration: `d428fc70e000f9eda1d30b9e662e63cfa1a40c93`
Original pre-output target: `3bf10b324911a98df5d093e58f55abd4fae4f7aa`
Exact normalization bridge: `725c1e180641e05bc5701ccbb193bd34168e8dd2`

This record is committed before any Iter057F degree-two trace vector has been consumed.

## Defect

Iter057G correctly froze the exact tensor identity

`g_ab E_W3^{ab}=-I3_full`,

but its exact RHS target used the six-dimensional independent-bivector scalar

`J=tr(W^3)`

as though it were identical to the unrestricted full-index scalar

`I3_full=C_ab{}^{cd} C_cd{}^{ef} C_ef{}^{ab}`.

The exact representation bridge subsequently derived from index counting is

`I3_full = 8 J`.

Therefore the original target

`T_old,j = 3 tr(Wbar^2 dW_j)`

is low by a factor eight in the full-EOM convention.

## Correct full-tensor target

For the frozen cosine perturbation,

`delta W|_{s^2}=-dW`,

so

`delta I3_full|_{s^2} = -24 tr(Wbar^2 dW)`.

The degree-two trace identity is therefore

`trace_eta(L2_j)=+24 tr(Wbar^2 dW_j)=8 T_old,j`.

In the symmetric basis order

`(00,01,02,03,11,12,13,22,23,33)`,

the corrected exact target is

`T_full = (-48,96,0,0,-48,0,0,-144,0,144)/625`

or numerically

`(-0.0768, 0.1536, 0, 0, -0.0768, 0, 0, -0.2304, 0, 0.2304)`.

## Authority consequence

The original Iter057G preregistration must not be executed/promoted as written. It remains an immutable record of an invalid control normalization discovered before outputs.

A successor trace-Ward gate must freeze the corrected factor-eight target prospectively.

No numerical `L2` output was used to derive the factor. The correction follows solely from the exact ordered-antisymmetric-index versus independent-bivector representation count.