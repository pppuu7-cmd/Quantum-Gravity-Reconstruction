# Iter054E initial run — implementation-invalid control predicate

Date: 2026-09-14

Gate: `ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT`

Preregistration: `ed62acf961cae4a0d200364285d94a56e61a294d`

Initial production head: `59c5a09ac693c79bdc1827efa91e283cf30a36ab`

Initial run: `34815920355`

## Terminal status of the initial run

Classification: **`ITER054E_IMPLEMENTATION_OR_CONTROL_INVALID_A0_STRUCTURAL_EQUALITY`**.

This is not a scientific FAIL of the frozen mixed-order proxy family.

The A1, B0 and B1 streams completed successfully. A0 failed only its `factorization` predicate for all 12 frozen rational lambda witnesses, while the independently frozen GR limit, GR root, higher-derivative root, singular-branch identity and sign-flip control all passed.

## Exact defect

The preregistered obligation is the algebraic identity

`P(z;eps,lambda) = z*(1 + eps*lambda*z)`

for

`P = z + eps*lambda*z^2`.

The implementation used

`sp.factor(expr) == z*(1+e*lv*z)`.

For rational `lv`, SymPy may return an algebraically equivalent but structurally different canonical form such as `z*(e*z + 3)/3` rather than `z*(1 + e*z/3)`. Python/SymPy structural `==` therefore returns `False` even though the frozen algebraic identity is exact.

The control-only repair is to test exact algebraic equality by simplifying the difference to zero. No polynomial, witness, root, scaling, threshold, PASS/FAIL criterion, negative control, branch definition or interpretation ceiling is changed.

## Retry authority

An exact frozen retry is authorized after this control-only implementation repair. The historical initial run remains permanently implementation-invalid and must not be rewritten as PASS or scientific FAIL.

## Claim ceiling

No scientific conclusion about strong hyperbolicity, well-posedness, physical spectrum, ghost sign, unitarity, `c6`, `beta`, quantum amplitude/measure, UV completion, GR recovery, experiment or new physics follows from this implementation-invalid run.
