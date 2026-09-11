# QGR Iter005-G2 — quartic two-derivative kinematic count

Date: 2026-09-11
Status: `PASS_SCOPED_QUARTIC_KINEMATIC_SPACE_COUNTED / QUARTIC_NOETHER_OPEN`

## Question

How large is the complete local quartic action space with total derivative degree two before imposing the next Noether consistency equation?

## Exact setup

The field remains

`H = Sym^2(W4)`

with ten components.

For four identical bosonic legs, the leg permutation group is `S4`.

After total momentum conservation

`k1+k2+k3+k4=0`,

the independent leg-momentum representation is the three-dimensional standard representation `U3` of the leg `S4`.

The degree-two momentum-polynomial representation is

`Sym^2(W4 tensor U3)`.

The quartic field factor is `H^tensor4` with the same leg `S4` permuting the four copies. Averaging the combined character over spatial `S4` and leg `S4` gives the exact invariant multiplicity

`1694`.

Therefore the complete bosonic local `S4`-invariant quartic vertex space with total derivative degree two, after the momentum-conservation / integration-by-parts quotient, is **1694-dimensional**.

Classification:

`PASS_SCOPED_COMPLETE_KINEMATIC_QUARTIC_TWO_DERIVATIVE_VERTEX_COUNT_1694`.

## Interpretation

This is substantially larger than the cubic physical action space (`317`). It means that quartic consistency cannot be inferred merely from finite symmetry and derivative counting.

The active quartic Noether equation is

`delta_0 S4 + delta_1 S3 = 0`,

where both `delta_1` and the unique cubic `S3` are already fixed by previous QGR gates.

Because the source is fixed, the next question is sharply defined: does it lie in the image of the quartic linearized Noether map, and if so, is the physical quartic solution unique modulo kinematic/null directions?

## Guard

No Einstein-Hilbert quartic term is inserted or used in this count. A later comparison is allowed only after an internal QGR solution is found.

## Reproducibility

`code/qgr_iter005_g2_quartic_two_derivative_count.py`
