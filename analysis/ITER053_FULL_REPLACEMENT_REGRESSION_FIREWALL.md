# Regression firewall for a possible full corrected Iter053 replacement

Date: 2026-09-14
Status: outcome-independent implementation audit aid only. This is not a preregistration and does not authorize a replacement while the active Iter053T productions are non-terminal.

## Purpose

A future full corrected A4+B2+C2 replacement, if authorized, should change exactly one semantic data path relative to historical Iter053R:

`transformed C weighted polynomial-factor extraction`.

Everything else belongs to the same frozen scientific object and must remain semantically invariant. This note records a fail-closed regression firewall so that an implementation repair cannot accidentally become a broader, scientifically different gate.

## Historical Iter053R data-flow decomposition

### A lanes

Historical A uses:

- `metric = PolyMetric(A_METRIC[i])`;
- `pert = CompactPerturbation(A_PERT[i])`;
- direct support-domain GL7/GL8 action variation from the full compact perturbation;
- weighted GJ2/GJ3 H5 bulk with the known compact-support factor in the Jacobi weight and polynomial tensor extracted as `pert.base.jets(u)[0]`;
- correct-sign and wrong-sign H5 controls.

Because `CompactPerturbation.base` is exactly the underlying polynomial `Perturbation`, replacing implicit wrapper-depth extraction with explicit `poly_source=pert.base` is semantically identical for every A lane.

### B lanes

Historical B uses the same `CompactPerturbation` wrapper around its polynomial perturbation and the same base weighted extraction. Therefore explicit `poly_source=pert.base` is also semantically identical for B0/B1.

The conformally-flat/null controls, direct integration, W3/P/H5 samples, signature, inverse and collar controls must remain unchanged.

### C base side

Historical C base is also already correct:

- full compact perturbation for direct variation/control;
- polynomial `pert.base` for the reduced weighted integral;
- geometry and source parameter both evaluated in the base frame.

A corrected explicit reducer should produce the same base-side scientific object.

### C transformed direct/control side

Historical transformed C direct/control construction is not the diagnosed defect:

- `mt = TransformMetric(metric,L)`;
- `pt = TransformPerturbation(pert,L)`;
- source parameter `u` maps to transformed coordinate `y=L^-1 u`;
- direct action variation uses `mt,pt` at `y`;
- collar/signature/inverse and transformation-algebra controls use the same full transformed perturbation.

The terminal Iter053R evidence already showed direct frame covariance at approximately `3.2e-12` or better on C0/C1. These paths must remain semantically unchanged in the replacement.

### C transformed weighted side — the only intended semantic correction

Historical Iter053R passed the full transformed wrapper `pt` into a reducer that then evaluated

`pt.base.jets(u)[0]`.

Because `pt.base` is the whole `CompactPerturbation`, that returns `B(u)p(u)` rather than the required unfactored polynomial tensor.

The corrected transformed weighted path must instead receive the original polynomial source explicitly:

`poly_source = pert.base`

and construct

`p_y(u)=L^T poly_source.jets(u)[0] L`

while evaluating transformed geometry at `y=L^-1u` and using exactly one external GJ support weight.

No other C scientific object should change.

## Prospective regression-validity requirements for a future full replacement

If a future gate becomes authorized, its preregistration should classify an unexpected change in an unchanged path as **INVALID_IMPLEMENTATION**, not as new physical evidence.

At minimum freeze the following implementation-validity obligations before execution.

### R1 — A-path identity

The replacement A implementation must use exactly the same seeds, metric/perturbation constructors, support radius, direct epsilon stencil, GL7/GL8 rules, GJ2/GJ3 rules, H5 derivative step and wrong-sign formula as Iter053R.

The source object for weighted A must be explicitly recorded as the underlying polynomial `Perturbation`.

### R2 — B-path identity

The replacement B implementation must preserve the same conformal metric/perturbation seeds, null controls, direct/weighted rules and W3/P/H5 sample definitions.

### R3 — C-base identity

The replacement C base path must use the same base metric, full compact perturbation and explicit polynomial source that historical Iter053R already intended.

### R4 — C-transformed direct identity

The transformed direct/collar/control path must remain `TransformMetric + TransformPerturbation` at `y=L^-1u` with the same determinant-one shears and thresholds.

### R5 — corrected source-object identity

The transformed **weighted** source must record that its polynomial-source class/object is the underlying `Perturbation`, not `CompactPerturbation` and not `TransformPerturbation`.

At frozen structural nodes verify to numerical roundoff:

`p_weighted_transformed = L^T pert.base.jets(u)[0] L`.

### R6 — no double support factor

At the same structural nodes verify that the reducer's polynomial-source object does not contain the compact bump. A diagnostic comparison against the historical legacy extraction may be retained, but the legacy value must never enter the corrected scientific integral.

### R7 — unchanged frozen scientific classifier

All original Iter053R A/B/C thresholds and wrong-sign requirements must be copied without relaxation. The replacement may add object-identity validity controls, but they must not weaken any scientific threshold.

## Historical-reference values and their correct role

Historical terminal Iter053R A4+B2 and C-base values are useful as **regression references**, not as pooled scored evidence for a future replacement.

A future replacement must recompute all frozen lanes fresh. It may compare fresh unchanged-path outputs against immutable historical values as an implementation consistency control, but it cannot count historical PASS lanes toward the new aggregate.

If a fresh unchanged path differs materially for unexplained reasons, the gate should become INVALID pending localization rather than silently accepting the difference as a new physical outcome.

The exact numerical tolerance for such a historical regression comparison, if included as a scored validity check, must be prospectively frozen from deterministic/numerical reproducibility evidence before the replacement production. It must not be chosen after seeing the fresh values.

## Why this firewall matters

A replacement that changes several code paths at once would make a later PASS scientifically ambiguous: it would be impossible to know whether recovery came from the diagnosed transformed-source correction or from an untracked change elsewhere.

The single-path repair plus unchanged-path regression controls make the causal interpretation falsifiable:

- if only transformed weighted C changes and closure is restored, that supports the diagnosed wrapper-depth defect;
- if unchanged A/B/C-base/direct paths move unexpectedly, the implementation repair is not isolated and the replacement should be treated as invalid until explained;
- if the isolated correction is implemented correctly but the full frozen contract still fails, that is a genuine scientific/numerical failure of the corrected replacement under its scope rather than a reason to relax thresholds.

## Claim ceiling

This note is not scientific evidence for a replacement PASS. Historical Iter053R remains a permanent scientific FAIL, active Iter053T gates retain independent authority, `c6` remains symbolic/unfixed, `beta=1` remains unauthorized and theory established remains `0%`.
