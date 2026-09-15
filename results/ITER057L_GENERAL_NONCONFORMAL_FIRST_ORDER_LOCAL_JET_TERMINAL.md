# Iter057L terminal result — general nonconformal first-order local jet

Date: 2026-09-15
Gate: `ITER057L-GENERAL-NONCONFORMAL-FIRST-ORDER-BACKGROUND-JET`
Preregistration: `dc4084c0ba62049403dd7260214eb39ca23f9116`
Derivation: `93a850eb3adb78dba7a905632faca649a72db6dd`

## Terminal classification

**`PASS_SCOPED_ITER057L_GENERAL_QAB_FIRST_ORDER_LOCAL_JET_SOURCE_COMPATIBLE__OPEN_NEIGHBORHOOD_SOLUTION_NOT_ESTABLISHED`**

## Exact constructive result

For arbitrary symmetric first-order source

`S_ab=-E_W3_ab[g0]/A_E`,

define a trace-reversed quadratic correction jet

`qbar_ab=(1/2)Q_ab,cd x^c x^d+O(|x|^3)`

with

`Q_ab,cd = -(5/9) eta_cd S_ab`

`          + (1/18)(eta_ac S_bd+eta_ad S_bc+eta_bc S_ad+eta_bd S_ac)`

`          + (2/9) eta_ab S_cd`

`          - (1/18) eta_ab eta_cd S`.

This exact universal tensor satisfies

`eta^{ac}Q_ab,cd=0`

and

`eta^{cd}Q_ab,cd=-2S_ab`.

Under the repository curvature convention, the Ricci-flat de Donder reduction is

`DG_ab[q]=-(1/2)[Box qbar_ab+2R_acbd qbar^cd]`.

Because `qbar(0)=0`, the curvature term vanishes at the frozen point and the construction gives

`DG_ab[q](0)=S_ab`

for every symmetric `S_ab`.

## Independent exact control

A symbolic check with ten algebraically independent source components verified identically:

- both tensor-pair symmetries of `Q`;
- all 16 first-derivative de Donder constraints;
- all 10 reduced Einstein equations;
- all 10 direct unreduced normal-coordinate Einstein equations;
- exact equality of reduced and unreduced responses.

No numerical tolerance and no G3 diagonal specialization were used in this control.

Iter056X supplies exact source conservation `nabla^a S_ab=0`. The G3/H0 source is static and inversion-even, hence `nabla_c S_ab(0)=0`; the quadratic correction and exact de Donder contraction give matching first derivative field/gauge compatibility at the frozen origin.

## Relation to Iter057J and Iter057K

Iter057J remains a terminal scientific FAIL of the **conformal** open-neighborhood continuation because `A_E K_0011=16 kappa^4 != 0`.

This Iter057L PASS demonstrates that this obstruction does not extend to the unrestricted symmetric correction problem at the local second-jet level.

Historical Iter057K remains a terminal technical BLOCKED production attempt; it is not retroactively reclassified. Its missing expensive exact-control records are irrelevant to the independent universal Iter057L right-inverse construction.

## Scope ceiling

This PASS establishes only source-compatible local Taylor data through the first source-owned derivative order. It does not establish:

- a quartic correction satisfying the next nontrivial even source jet;
- an actual solution on an open neighborhood;
- convergence of a formal Taylor series;
- global or asymptotic boundary conditions;
- a corrected all-orders on-shell background;
- physical characteristics, hyperbolicity, modes/ghosts, stability, unitarity, regulator removal, UV completion, or experiment.

The next bounded scientific target is therefore the prospectively frozen second-even-jet/quartic extension of the general correction, with exact gauge and source compatibility.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.