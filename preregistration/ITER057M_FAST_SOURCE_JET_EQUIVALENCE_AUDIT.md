# Iter057M fast exact source-jet equivalence audit

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Parent gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Parent preregistration: `9760ca0324dce13cf141a9f93b6ff69ea4c75605`
Candidate evaluator: `f9181c7dda617ce4061fa90e73164e6cdbecd714`

## Purpose

Independently validate the component sign and finite-Taylor construction used by the fast exact G3/H0 Weyl3 source-jet evaluator without waiting for global rational simplification of the historical Iter057K implementation.

This is an implementation/equivalence control inside Iter057M. It does not alter any scientific decision rule and cannot by itself terminalize Iter057M.

## Frozen independent reference

Construct a second implementation using ordinary SymPy tensor expressions, not the custom Fraction polynomial engine. Use symbolic `kappa` and the frozen `(-,+,+,+)` G3 metric jet.

The reference must independently:

1. construct the exact metric/inverse jet, Christoffel, Riemann, Ricci, scalar and Weyl objects;
2. construct `Q^{abcd}=C^{ab}{}_{ef} C^{efcd}` explicitly with correct index raising;
3. lower/project onto the algebraic-Riemann subspace, apply the four-dimensional Weyl projector, and set `P=3 Pi_W Pi_R[Q]`;
4. verify exactly at the origin `P^{abcd}R_abcd=3 I3`;
5. evaluate `D^{ii}=nabla_mu nabla_nu P^{mu(ii)nu}` for all four diagonal components and factor out `kappa^3`.

The reference may truncate at coordinate degree two because only the origin value of the second divergence is being compared in this audit. This truncation is exact for the requested origin component.

## Candidate controls

The fast candidate must independently pass, with exact rational arithmetic:

- `P.R=3 I3` at the origin;
- `g^{ab} E_W3_ab=-I3` through degree two;
- `nabla_a E_W3^{ab}=0` through degree one;
- symmetry of `E_W3_ab` through degree two.

## Frozen comparison

The audit passes only if the independent symbolic reference and fast candidate agree exactly on:

- `I3(0)/kappa^3`;
- all four `D^{ii}(0)/kappa^3` values;
- the sign convention implied by the authoritative Iter056X formula `E_W3^{ab}=1/2 g^{ab} I3-P^{(a|cde|}R^{b)}_cde-2D^{ab}`.

No numerical tolerance or downstream Iter057J/Iter057M target may be used in the comparison.

## Interpretation

A PASS validates the fast evaluator's origin component convention and its finite-jet implementation strategy against an independent exact realization of the Iter056X analytic formula. It does not replace the separate source-second-jet, Q4, unreduced-substitution and terminal Iter057M obligations.

The older Iter057K-lineage replay run `34952811799` remains an independent historical-lineage cross-check if it completes. A timeout of that run is technical only and does not override a clean exact equivalence proof here.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.