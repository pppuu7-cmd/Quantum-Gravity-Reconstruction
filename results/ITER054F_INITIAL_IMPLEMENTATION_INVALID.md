# Iter054F initial run — implementation-invalid characteristic-polynomial predicate

Date: 2026-09-14

Gate: `ITER054F-WEYL3-MIXED-ORDER-STRONG-HYPERBOLICITY-OBJECT-DEFINITION-AUDIT`

Preregistration: `f4838c50ded00c6d62c9ef822f1f75285eceddf9`

Implementation: `823b4a24419f5e616eea256b6ba6359fbba30bd4`

Initial workflow head: `9b719f0b54030a74a5c166e93db1a2898d90bdfe`

Initial run: `34817447178`

## Classification

**`ITER054F_IMPLEMENTATION_OR_CONTROL_INVALID_A1_CHARPOLY_SYMBOL_IDENTITY`**

This is not a scientific verdict on the QGR evolution-object blocker.

A0 completed successfully, as did B0 and B1. A1 correctly found the diagonalizable matrix to have eigenspace dimension 2 and the Jordan matrix eigenspace dimension 1, and correctly detected the Jordan defect. The only failed predicate was the same-characteristic-polynomial comparison.

## Exact defect

The implementation used `Matrix.charpoly(mu).as_expr()` with an externally created SymPy symbol `mu` carrying assumptions. SymPy's polynomial generator can be internally distinct from that external symbol even when it prints with the same name. Consequently the printed exact polynomial was `mu**2 - 2*mu*v + v**2`, but the structural/symbol-identity subtraction against the external `(mu-v)**2` did not simplify to zero.

The control-only repair is to compute the characteristic polynomial directly as the exact determinant `det(mu*I-A)` using the same external symbol. The frozen matrices, real-eigenvalue statement, eigenspace predicates, positive control, QGR authority census and aggregate classification rules remain unchanged.

An exact frozen retry is authorized after this control-only repair. This initial run remains permanently implementation-invalid.
