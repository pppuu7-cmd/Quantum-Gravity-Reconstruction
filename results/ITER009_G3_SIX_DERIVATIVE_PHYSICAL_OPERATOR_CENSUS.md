# QGR Iter009-G3 — six-derivative physical operator census and O(h^4) competition

Date: 2026-09-12
Status: `PARTIAL_SCOPED_ON_SHELL_PARITY_EVEN_PURE_VACUUM_SIX_DERIVATIVE_OPERATOR_SHAPE_COLLAPSES_TO_ONE_WEYL_CUBED_CLASS / C6_UNFIXED`

GitHub Actions run `34663353057`: 6 lanes + aggregate SUCCESS.

## G3A — algebraic curvature-cubed basis

On four-dimensional Ricci-flat vacuum, `R_munu=0` and `R=0`, hence `Riemann=Weyl`.

On complexified two-forms the Weyl tensor decomposes into self-dual and anti-self-dual symmetric traceless 3x3 blocks `C_+` and `C_-`. For a traceless 3x3 matrix the independent cubic class invariant is `tr(C^3)`; the script checks the Newton identity `tr(A^3)=3 det(A)` on a generic traceless diagonal representative.

Parity exchanges the two chiral blocks. Thus the cubic algebraic sector has one parity-even combination

`tr(C_+^3)+tr(C_-^3)`

and one parity-odd combination outside the active parity-even branch.

Classification:
`PASS_SCOPED_FOUR_DIMENSIONAL_RICCI_FLAT_ALGEBRAIC_CURVATURE_CUBED_SECTOR_HAS_ONE_PARITY_EVEN_WEYL_CUBED_DIRECTION`.

## G3B — derivative-curvature reduction

At six derivative order, the remaining pure-gravity structures may be represented schematically by curvature-cubed and derivative-curvature terms. In the scoped Ricci-flat bulk sector:

- Ricci/scalar-curvature terms vanish by the vacuum EOM;
- integration by parts maps `(nabla Riemann)^2` to `-Riemann box Riemann` up to a boundary;
- the differential Bianchi/Lichnerowicz relation reduces `box Riemann` to quadratic Riemann terms plus Ricci terms.

Therefore the parity-even derivative-curvature bulk sector reduces to the same Weyl-cubed class after vacuum EOM, Bianchi and IBP quotienting.

Classification:
`PASS_SCOPED_DERIVATIVE_CURVATURE_SIX_DERIVATIVE_BULK_STRUCTURES_REDUCE_TO_THE_SAME_PARITY_EVEN_WEYL_CUBED_CLASS_ON_RICCI_FLAT_VACUUM`.

Boundary terms, matter/off-shell sectors and parity-odd operators remain outside this reduction.

## G3C — nonzero Ricci-flat algebraic witness

A Petrov-D-type purely electric Weyl block with eigenvalues

`(-2,1,1)`

is traceless but has

`tr(C^3)=-6`.

For equal real chiral blocks the parity-even chiral sum is `-12`, so the surviving class is not an identity-zero on the Ricci-flat algebraic curvature sector.

Classification:
`PASS_SCOPED_WEYL_CUBED_PARITY_EVEN_CLASS_HAS_A_NONZERO_RICCI_FLAT_PETROV_D_ALGEBRAIC_WITNESS`.

## G3D — refinement / Gamma scaling

The first local six-derivative correction compatible with the same continuum normalization has the dimensional form

`S6 = a_cont * c6 * h^4 * integral(I6)`,

with `I6~Weyl^3` on Ricci-flat vacuum.

Using

`ell_Q^2=hbar/a_cont`, `Gamma=h^2/ell_Q^2`,

its phase coefficient is

`S6/hbar = c6 * Gamma^2 * ell_Q^2 * integral(I6)`.

At characteristic curvature scale `R_eff`, its relative local effect scales as

`c6 * Gamma^2 * (ell_Q^2 R_eff)^2`.

Therefore this first physically nonredundant local vacuum correction is formally `O(h^4)` / `O(Gamma^2)`, the same refinement power as the already derived finite-history effect.

Classification:
`PASS_SCOPED_FIRST_PHYSICALLY_NONREDUNDANT_LOCAL_VACUUM_SIX_DERIVATIVE_CORRECTION_HAS_THE_SAME_H4_AND_GAMMA2_POWER_COUNTING_AS_THE_EXISTING_HISTORY_EFFECT`.

## G3E — coefficient authority

A repository authority scan finds no frozen exact finite-cell/microscopic matching result that fixes the coefficient `c6` of the parity-even Weyl-cubed class.

Classification:
`BLOCKED_SCOPED_NO_AUTHORITATIVE_QGR_MICROSCOPIC_MATCHING_CURRENTLY_FIXES_THE_UNIQUE_PARITY_EVEN_SIX_DERIVATIVE_VACUUM_COEFFICIENT_C6`.

This is not a no-go theorem: an exact future finite-cell action could in principle determine it.

## G3F — competition with the history effect

The existing history comparator scales as

`Delta_hist ~ C_prep Gamma^2 (ell_Q^2 R_eff)^2`.

A generic observable response to the local six-derivative correction has the same formal order,

`Delta_local ~ c6 F_local Gamma^2 (ell_Q^2 R_eff)^2`.

Thus one may not claim that the **complete** leading `O(h^4)` effective phenomenology is one-parameter unless either

1. `c6` is fixed by the same microscopic realization, or
2. the `Weyl^3` response is proved irrelevant/zero for the specified observable and preparation.

This refines, but does not retract, Iter008: its one-parameter statement remains valid for the explicitly constructed history/two-derivative comparator.

## Consolidated classification

`PARTIAL_SCOPED_ON_SHELL_PARITY_EVEN_PURE_VACUUM_SIX_DERIVATIVE_OPERATOR_SHAPE_COLLAPSES_TO_ONE_WEYL_CUBED_CLASS__ITS_QGR_COEFFICIENT_C6_IS_UNFIXED_AND_COMPETES_AT_THE_SAME_OH4_ORDER_AS_THE_HISTORY_EFFECT`.

## Active blocker

`MISSING_SAME_REALIZATION_MICROSCOPIC_DERIVATION_OR_ELIMINATION_OF_C6_AND_UNIFORM_INFINITE_REFINEMENT_OPERATOR_CONTROL`.

## Next gate

`QGR-ITER009-G4-MICROSCOPIC-C6-MATCHING-OR-OBSERVABLE-DECOUPLING-AND-CHANNEL-CONVERGENCE`

Test in parallel:

1. whether the current exact branch/action/refinement data contain enough structure to fix `c6` without adding a discretization prescription;
2. whether `Weyl^3` has zero quadratic variation about the flat QGR seed and therefore cannot modify the linear one-particle characteristic comparator at tree level;
3. whether a weak curved background activates a quadratic `Weyl^3` response proportional to background Weyl curvature;
4. whether the specific G6H broadband observable uses a domain where that local response is present or absent;
5. whether branch-to-branch channel differences admit a uniform summable bound sufficient for an infinite-refinement limit.
