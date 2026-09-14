# Iter054F preregistration — strong-hyperbolicity evolution-object definition audit

Date: 2026-09-14

Gate: `ITER054F-WEYL3-MIXED-ORDER-STRONG-HYPERBOLICITY-OBJECT-DEFINITION-AUDIT`

Status at freeze: **PREREGISTERED BEFORE SUBSTANTIVE OUTPUTS**

## Scientific question

After the terminal scoped Iter054E regime-separation certificate, does existing QGR authority already define a sufficiently complete mixed Einstein + Weyl3 evolution object on which a genuine strong-hyperbolicity/symmetrizer question is mathematically well posed, or is the required evolution reduction still underdetermined?

This gate tests object definition and logical sufficiency. It does not select a preferred reduction and does not attempt to rescue missing structure by inventing one.

## Dependency

Strong hyperbolicity is a property of an explicitly specified evolution system/principal evolution symbol on an open covector/background region. A characteristic determinant or list of real roots alone does not determine eigenvector completeness, uniform conditioning, constraint propagation or a symmetrizer.

Iter054D established only a finite fourth-order gauge-completion/quotient certificate. Iter054E established only a finite exact mixed-order root/regime proxy. Both explicitly left the strong-hyperbolicity objects open.

## Frozen required QGR evolution object

A QGR-specific strong-hyperbolicity gate is authorized only if current durable repository authority already supplies all of the following without post-hoc construction:

1. an explicit state vector / reduction-variable set `U`;
2. a fixed time direction and spatial covector domain;
3. a first-order-in-time evolution system, or a rigorously specified equivalent higher-order formulation with a stated strong-hyperbolicity definition;
4. an explicit principal evolution matrix/symbol `A(n)` or equivalent eigensystem-bearing object;
5. gauge variables and gauge-fixing evolution equations, not only an algebraic principal gauge completion;
6. constraint variables and their principal propagation subsystem;
7. a declared norm/symmetrizer notion and an open background/covector domain on which uniform bounds are to be tested;
8. an explicit map back to the mixed Einstein + symbolic-`c6` Weyl3 equations and an exact GR-limit relation.

The gate must not infer any missing item from notation, a determinant, a root table or a finite rank certificate.

## Frozen authority sources

The QGR-specific inventory is frozen to the durable authority present before this preregistration:

- `recovery/state.json` after Iter054E terminalization;
- `recovery/CURRENT_FRONT.md` after Iter054E terminalization;
- `prereg/ITER054D-WEYL3-PRINCIPAL-ORDER-GAUGE-FIXING-CHARACTERISTIC-AUDIT.md`;
- `results/ITER054D_TERMINAL_RESULT.md`;
- `prereg/ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT.md`;
- `results/ITER054E_TERMINAL_RESULT.md`.

No later file may be used to retroactively satisfy the inventory in this gate.

## Frozen streams

### A0 — QGR evolution-object authority census

Read the frozen authority sources and require positive, explicit authority for all eight required object fields above.

A0 outcomes are frozen:

- `OBJECT_DEFINED` only if all eight are explicitly present and authorized;
- `BLOCKED_OBJECT_DEFINITION` if one or more are explicitly absent/unresolved or not authorized;
- `INVALID_PROVENANCE` if a required frozen authority source is missing/unreadable or its identity cannot be established.

The lane must report the exact missing fields. Absence is not a scientific inconsistency of QGR; it is an object-definition blocker for the next hyperbolicity claim.

### A1 — same-polynomial diagonalizable-vs-defective counterexample

Use exact symbolic matrices with real symbolic/rational `v`:

`A_diag = [[v,0],[0,v]]`

`A_J = [[v,1],[0,v]]`.

Require exactly:

1. both have the identical characteristic polynomial `(mu-v)^2`;
2. both have only the real eigenvalue `v` with algebraic multiplicity two;
3. `A_diag` has eigenspace dimension two / is diagonalizable;
4. `A_J` has eigenspace dimension one / is defective;
5. therefore characteristic-polynomial/root data alone cannot imply strong hyperbolicity.

Any failure of these exact predicates invalidates the control implementation.

### B0 — symmetrizable wave-system positive control

Use the exact first-order 1+1 wave principal matrix

`A_wave = [[0,1],[1,0]]`

with candidate symmetrizer `H=I`.

Require exactly:

1. eigenvalues are `-1,+1` and real;
2. two independent eigenvectors exist;
3. `H` is positive definite;
4. `H*A_wave` is symmetric;
5. the eigensystem is nondefective.

This is only a detector positive control, not a QGR model claim.

### B1 — authority / overclaim firewall

B1 must record that this gate does not establish strong hyperbolicity, well-posedness, energy positivity, constraint propagation, physical mode count, residue/ghost sign, unitarity, quantum amplitude/measure, UV completion, full GR recovery, experiment or new physics.

`c6` remains symbolic/unfixed and `beta=1` remains unauthorized.

## Frozen aggregate classifier

If A1 and B0 controls are exact and B1 firewall is valid:

- if A0=`OBJECT_DEFINED`, classification is `ITER054F_EVOLUTION_OBJECT_DEFINED_READY_FOR_SEPARATE_STRONG_HYPERBOLICITY_GATE`;
- if A0=`BLOCKED_OBJECT_DEFINITION`, classification is `BLOCKED_OBJECT_DEFINITION_ITER054F_MIXED_ORDER_EVOLUTION_REDUCTION_NOT_FIXED`;
- if provenance/control implementation is invalid, classification is `INVALID_IMPLEMENTATION_OR_PROVENANCE_ITER054F`.

A valid BLOCKED result is a terminal scientific-program result and must not be converted into a PASS or candidate failure.

## Interpretation ceiling

Even `OBJECT_DEFINED` would authorize only a separate prospective strong-hyperbolicity test. It would not itself prove hyperbolicity. A BLOCKED result means the present QGR reconstruction does not yet define the mathematical object required for that test; it does not show the underlying candidate is physically inconsistent.

No post-output addition of a preferred reduction, gauge evolution law, constraint subsystem, norm or symmetrizer is allowed inside Iter054F. Such a construction would require a distinct prospectively preregistered gate.
