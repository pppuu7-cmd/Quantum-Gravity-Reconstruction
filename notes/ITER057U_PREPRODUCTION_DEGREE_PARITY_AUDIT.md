# Iter057U preproduction degree/parity audit

Date: 2026-09-15
Preregistration: `72eb0c6ffdcff789d7929a766e8f237475f89aaf`.
Production head: `2159f89bc62ea636d3584fccc84d2737b02311a1`.

This note records structural checks before production evidence is consumed. It does not add or weaken any Iter057U decision criterion.

## Even-parity chain

The frozen canonical Einstein seed contains only even total coordinate degrees 0,2,4,6,8. Hence under `x -> -x`:

- `g` and `g^{-1}` are even;
- `Gamma` is odd;
- `Riemann`, `Ricci`, scalar curvature and Weyl are even;
- `Q ~ C^2` and projected `P` are even;
- the first covariant divergence of `P` is odd;
- the second covariant divergence is even;
- the algebraic `P.R` insertion and `I3` terms are even;
- therefore `E_W3` and `Shat=-E_W3` are even.

Thus normalized source coefficients at total coordinate degrees 1 and 3 are structurally expected to vanish. This is only a preproduction expectation: frozen control G still requires the evaluator to represent/check the unrestricted basis directly rather than deleting odd slots by ansatz.

## Kappa grading

With the canonical local seed grading, curvature degree `2n` carries one additional power of `kappa` relative to coordinate order. Therefore the Weyl-cubic Euler source has the expected grading

- degree 0: `Shat^(0) ~ kappa^3`;
- degree 2: `Shat^(2) ~ kappa^4`;
- degree 4: `Shat^(4) ~ kappa^5`.

The Iter057U artifact should therefore export degree-four normalized coefficients naturally as `Shat_ab[alpha]/kappa^5`; failure of this exact grading would be diagnostic evidence of a seed/normalization/degree-bookkeeping problem, not a fitted rescaling opportunity.

## Basis bookkeeping

For 10 independent symmetric tensor components in four coordinates, the unrestricted normalized Taylor basis through degree four has counts

- degree 0: `10*C(3,3)=10`;
- degree 1: `10*C(4,3)=40`;
- degree 2: `10*C(5,3)=100`;
- degree 3: `10*C(6,3)=200`;
- degree 4: `10*C(7,3)=350`;
- total: `700`.

These are bookkeeping counts, not matrix ranks and not scientific fit criteria.

All global/physical claim locks remain unchanged; `c6` is symbolic/unfixed and `beta=1` remains unauthorized.
