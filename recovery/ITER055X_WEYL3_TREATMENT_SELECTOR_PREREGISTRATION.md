# Iter055X preregistration — physical Weyl3 dynamical-treatment selector authority

Date: 2026-09-14
Gate: `ITER055X-WEYL3-PHYSICAL-DYNAMICAL-TREATMENT-SELECTOR`

## Frozen question
Does existing QGR authority already choose and define the physical dynamical treatment of the `c6*Weyl^3` sector strongly enough to decide whether formal extra higher-derivative characteristic roots are retained as physical dynamics, removed/order-reduced as EFT artifacts, or avoided by a finite physical refinement/UV stop scale?

## Frozen treatment classes
Audit exactly these three classes; do not invent a fourth rescue after reading results.

### A. EXACT_HD
The full six-derivative action/EOM are treated as exact physical equations on the stated continuum/finite-h domain. A source selector must authorize retaining the full higher-derivative principal structure and specify the physical initial-data/evolution problem sufficiently to interpret extra formal roots.

### B. ORDER_REDUCED_EFT
The Weyl3 term is treated perturbatively relative to lower-order GR dynamics. A source selector must state the small expansion parameter/regime, authorize lower-order equation substitution/order reduction, specify retained accuracy/error order, and state that formal extra higher-derivative roots outside the EFT branch are not physical solutions of the truncated effective dynamics.

### C. FINITE_PHYSICAL_REFINEMENT
A nonzero microscopic/refinement/UV stop scale is physical rather than removable. A source selector must independently fix or derive that physical scale/regime and authorize finite-h Weyl3 corrections as part of physical dynamics.

## Frozen authority set
Audit existing QGR sources around Iter009-G3/G4/G5/G6, Iter010 Weyl-active/c6 gates, Iter045 spectrum, Iter053 functional variation, Iter054E-K principal/scaling gates, plus any explicit status/authority note containing treatment, order reduction, EFT, exact EOM, cutoff, refinement stop, ghost/pole or well-posedness language.

## Frozen obligations
1. Separate **action/operator existence** from a physical dynamical treatment rule.
2. Separate formal principal-polynomial/root diagnostics from authorization to count physical propagating modes.
3. Separate removable regulator `h` scaling from a derived finite physical cutoff/refinement stop.
4. For any claimed EFT selector, require an explicit order-reduction rule and error/regime, not generic use of the word “effective”.
5. For any claimed exact-HD selector, require authority beyond computing a six-derivative term or varying it on test backgrounds.
6. For any claimed finite-scale selector, require actual independent scale authority; G7A's `kappa/h^2` degeneracy and explicit “not h=Planck length” guard count against such a selector.
7. Preserve Iter055W: no treatment may be chosen merely because it avoids its reciprocal survival/decoupling fork.

## Frozen classifications
- `PASS_SCOPED_ITER055X_EXACT_HD_TREATMENT_SOURCE_AUTHORIZED` only if existing authority explicitly selects exact higher-derivative physical dynamics with a defined physical evolution interpretation.
- `PASS_SCOPED_ITER055X_ORDER_REDUCED_EFT_TREATMENT_SOURCE_AUTHORIZED` only if existing authority explicitly supplies the perturbative/order-reduced rule and regime/error control.
- `PASS_SCOPED_ITER055X_FINITE_PHYSICAL_REFINEMENT_TREATMENT_SOURCE_AUTHORIZED` only if existing authority independently fixes a nonzero physical refinement/cutoff scale and treatment.
- `BLOCKED_OBJECT_DEFINITION_ITER055X_PHYSICAL_WEYL3_DYNAMICAL_TREATMENT_SELECTOR_NOT_SOURCE_DEFINED` if Weyl3 operator/action/diagnostics exist but none of the three physical treatments is source-authorized.
- `INVALID_PROVENANCE_ITER055X_CONFLICTING_PHYSICAL_TREATMENT_AUTHORITIES` only if existing sources explicitly and irreconcilably select different physical treatments.

## Interpretation ceiling
A BLOCKED result identifies a candidate-defining missing physical-treatment object; it is not a failure of Weyl3 itself and not permission to select order reduction post hoc. A treatment PASS would authorize only its exact scoped regime and would still require its own stability/causality/quantum-consistency tests. No beta/c6 fixing, UV completion, unitarity, GR recovery, experiment or theory-establishment claim follows.

No GitHub Actions run is preregistered; this is a source/authority audit.
