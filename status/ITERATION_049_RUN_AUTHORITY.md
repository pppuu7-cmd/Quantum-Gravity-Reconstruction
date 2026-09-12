# Iter049 run authority and symbolic-control correction

Date: 2026-09-13

## First production run

Initial production run: `34719814120`
Head: `237cd84006afa867352c27fa274c8aa7c25d14ae`

The run produced valid positive evidence in early Schwarzschild and radial-Noether lanes, but the first de Sitter negative-control lane B0 returned:

- `W3 = 0` exactly;
- `L6 = 0` exactly;
- `E_F = E_N = E_S = 0` exactly;
- `weyl_zero_exact = false`.

A direct component-level diagnostic localized the sole surviving apparent Weyl component after substitution to

`C[1,3,3,2] = r*(sin(2*theta)*tan(theta) + cos(2*theta) - 1)/(2*tan(theta))`.

This expression is identically zero by elementary trigonometric identities:

`sin(2theta) tan(theta) + cos(2theta) - 1 = 2 sin^2(theta) + cos^2(theta) - sin^2(theta) - 1 = 0`.

SymPy's default `trigsimp`/ordinary simplification did not canonicalize this form, while `trigsimp(..., method='fu')` returns exact zero. Therefore the B0 failure is a **symbolic simplification/control false negative**, not evidence of nonzero Weyl curvature in de Sitter.

The preregistered scientific criterion is NOT weakened: the full Weyl tensor must still simplify exactly to zero. The implementation will be corrected only by strengthening canonical trigonometric simplification globally; no witness, analytic target, threshold, stream, or interpretation lock changes.

Run `34719814120` is retained as diagnostic evidence but is **not authoritative for terminal Iter049 classification** because one frozen exact-zero control is known to be mis-evaluated by the simplification layer.

Authority label:

`ITER049_INITIAL_PRODUCTION_SYMBOLIC_CONTROL_INVALID_REQUIRES_CANONICAL_TRIG_RETRY`

The next trigger after the simplifier-only correction is the authoritative production retry, provided it uses the unchanged preregistration and scientific criteria.
