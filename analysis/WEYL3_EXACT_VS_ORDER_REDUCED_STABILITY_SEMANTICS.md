# Analytic control — exact versus perturbative stability semantics for the QGR Weyl^3 correction

Date: 2026-09-14

Status: outcome-independent analytic control. **Not a dynamical-treatment authority and not a stability gate.** It explains why that authority is required.

## Setup

The established QGR operator power counting writes the local correction schematically as

`S = S2 + c6 h^4 S6[Weyl^3] + higher orders`,

with `c6` symbolic/unfixed. On a nonzero-Weyl background, the curvature Hessian of the cubic term produces a four-derivative contribution to the linearized metric equation. After gauge reduction, write the raw local high-frequency operator schematically as

`P(k) = P2(k) + c6 h^4 P4(k; Cbar) + ...`,

where `P2` is homogeneous of degree 2 in the wave covector and the leading Weyl-cubic correction is homogeneous of degree 4 and linear in the background Weyl tensor at principal order.

This note does not assume that the omitted terms are known.

## 1. Local perturbative control parameter

In a local orthonormal frame, the relative size of the quartic term to the two-derivative term has the schematic dimensionless scaling

`epsilon_HD(k) ~ |c6| h^4 ||Cbar|| ||k||^2`.

Using `h^2 = Gamma ell_Q^2`, this is

`epsilon_HD(k) ~ |c6| Gamma^2 ell_Q^4 ||Cbar|| ||k||^2`.

For a perturbative six-derivative truncation, a necessary local consistency condition is

`epsilon_HD(k) << 1`

in the tested wave-covector domain, together with whatever independent bounds are required on omitted higher operators.

Because `c6` is unfixed, current QGR authority does not provide a numerical universal `k` cutoff from this condition alone.

## 2. Why exact truncation creates nonperturbative roots

Consider a single diagonalized toy eigenchannel of the raw symbol,

`lambda(k) = q2(k) + alpha q4(k)`,

with `alpha ~ c6 h^4 Cbar` in the local background. Besides roots continuously connected to `q2=0`, an exact solution of the finite higher-derivative polynomial can generically contain additional roots whose covector scale grows as the inverse higher-derivative coefficient.

In the scalar model

`k^2 + alpha k^4 = 0`,

the branches are

`k^2 = 0`,
`k^2 = -1/alpha`.

The second root lies precisely where `|alpha k^2| ~ 1`: the higher-derivative correction is no longer perturbative relative to the leading symbol. In an EFT interpretation, such a root is not automatically a physical degree of freedom of the truncated theory because the same scale is where omitted higher-order operators need not be negligible.

This scalar model is illustrative, not a claim that the tensor QGR symbol diagonalizes into this exact form.

## 3. Perturbative physical branches

If QGR ultimately authorizes a perturbative treatment, the physically controlled characteristic information at first correction order should be extracted from branches continuously connected to the lower-order QGR-L1 modes as `c6 h^4 -> 0`, within the frozen validity domain.

The future calculation must determine whether the projected `P4`:

- shifts an existing characteristic cone at `O(c6 h^4)`;
- changes polarization mixing/rank on the lower-order characteristic surface;
- is removable in part by a perturbative field redefinition or use of lower-order EOM;
- creates a genuine obstruction within `epsilon_HD << 1`.

A root that exists only at `epsilon_HD ~ 1` is categorically different from an instability or loss of hyperbolicity already present on the perturbative continuation of the physical branch.

## 4. Order reduction

A perturbative order-reduction prescription uses the lower-order equations and their differentiated consequences to eliminate higher-time-derivative pieces consistently to the retained order. The exact map is model-, gauge- and background-dependent and has **not** been derived by current QGR authority.

Therefore QGR may not simply delete quartic terms by hand. A future order-reduction gate must prospectively derive:

- the lower-order constraint/evolution split;
- which derivative substitutions are valid to `O(c6 h^4)`;
- preservation of diffeomorphism constraints/Bianchi identities;
- the resulting reduced initial-data space;
- the resulting characteristic operator on physical modes;
- the approximation/validity domain.

## 5. Field-redefinition firewall

At a fixed EFT order, local perturbative field redefinitions can move operators proportional to lower-order EOM without changing on-shell observables in their valid scope. QGR already used this logic to remove curvature-squared pure-vacuum bulk directions at first correction order.

Consequently, if `Weyl^3` is treated perturbatively, a physical stability statement should be formulated in terms of quantities invariant under the allowed perturbative field-redefinition/EOM equivalence, or the chosen representative must be shown not to change the claimed physical conclusion.

Exact additional roots of a finite truncated higher-derivative equation are generally not protected by such an equivalence and therefore should not be promoted to new physical modes merely because they are roots of one representative equation.

The on-shell six-derivative census establishes that the parity-even Weyl-cubed class itself survives the scoped vacuum quotient; it does not by itself make every exact root of a chosen truncated PDE representation physically invariant.

## 6. Exact-dynamics alternative

If a future QGR authority instead derives that the `c6 Weyl^3` corrected equation is to be treated as an exact fundamental evolution law in its own right, then the full higher-derivative initial-data problem and all gauge-reduced characteristic branches become part of the candidate dynamics. Under that interpretation, extra physical roots, Ostrogradsky-like sectors, non-hyperbolic directions, or constraint inconsistencies can be fatal.

But exact treatment must be positively derived from the QGR realization; it cannot be selected after seeing whether the spectrum is favorable.

## 7. Decision tree for a future stability program

After full functional-variation closure:

1. **Dynamical-treatment authority first.** Exact fundamental higher-derivative evolution or perturbative/order-reduced EFT evolution must be frozen from QGR construction principles.
2. **If exact:** analyze the full gauge-reduced quartic characteristic polynomial and initial-data count, including all additional branches.
3. **If perturbative:** derive the order-reduced physical evolution and test only controlled branches/observables within a prospectively frozen `epsilon_HD` domain, while using the raw quartic symbol as a diagnostic rather than automatically as a physical spectrum.
4. **In either case:** keep `c6` symbolic, test covariance/gauge constraints, use conformally-flat null controls, and include Weyl-active Petrov-D/Kasner/type-N probes without post-hoc background selection.

## Claim ceiling

This note selects neither treatment. It proves no ghost, no absence of ghost, no hyperbolicity theorem, no unitarity statement and no value/sign of `c6`. It only constrains how a future gate must distinguish mathematical roots from physically authorized degrees of freedom. `theory established=0%`.