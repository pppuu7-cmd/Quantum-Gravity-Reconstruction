# Iter057F2 preproduction normalization invalidation

Date: 2026-09-15
Status: `PREREGISTERED CONTROL NORMALIZATION INVALID / NO SCIENTIFIC PASS AUTHORITY`

Iter057F2 preregistration: `a6bbabeb93a83f212892eb2c84cbed17d601ece8`
Implementation: `5047b37c18318bea65c580e2b16c7d92df4429d1`
Workflow/run head: `628a254ca773d2f58dadbe54d4492f01faea0635`
Exact factor-eight bridge: `725c1e180641e05bc5701ccbb193bd34168e8dd2`
Trace-target invalidation: `57f4a2a478b3bf909a4091b089cd84bc04701c15`

This invalidation is committed before Iter057F2 scientific basis-lane outputs exist. The run may still execute operationally, but it cannot produce authoritative scientific PASS under its frozen contract.

## Two exact control defects

1. Iter057F2 retained the direct control `L4=Q_Iter054C`. The exact representation bridge is instead

`L4_full = 8 Q_Iter054C`

because the full unrestricted tensor invariant is `I3_full=8 tr(W^3)` in the Iter054C independent-bivector normalization.

2. Iter057F2 retained the original Iter057G trace target

`T_old=3 tr(Wbar^2 dW)`.

The full-EOM trace identity requires

`T_full=24 tr(Wbar^2 dW)=8 T_old`.

## Consequence

Iter057F2 must remain a diagnostic/implementation run only. Its cache-equivalence result, if successful, may still validate that memoization is algebraically identical to the original five-point evaluator. Its scientific lane PASS/FAIL flags cannot establish or refute the source `L2_Weyl3` block because two exact comparison targets are normalized incorrectly.

A new separately preregistered successor must use `8Q` and `8T` from the start while preserving the same source, frequency, epsilon and stencil panels.

No empirical factor was fitted to scientific output; the factor eight is fixed by exact antisymmetric-pair index counting.