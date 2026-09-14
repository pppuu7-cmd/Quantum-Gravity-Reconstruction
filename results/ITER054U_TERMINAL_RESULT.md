# Iter054U Terminal Result — G3 Branch-Resolved Weyl3 Differential Operator

Date: 2026-09-14
Gate: `ITER054U-G3-BRANCH-RESOLVED-WEYL3-DIFFERENTIAL-OPERATOR`
Preregistration commit: `e9486d6187c30436b278dc6f70d62d077eb4328d`
Status: `TERMINAL_BLOCKED_MISSING_REQUIRED_OBJECT`
Classification: `BLOCKED_MISSING_REQUIRED_OBJECT_ITER054U_NO_BRANCH_RESOLVED_WEYL3_ACTION_RESPONSE`

## Authority audit

The prospective obligations were checked against the currently authoritative G3/G4/G8A/Iter054S/Iter054T chain.

### A — explicit histories and transport: CLOSED

`code/qgr_iter010_g3_common.py` defines the 24 permutation histories explicitly and computes one Lorentz-transport matrix for each history as `L_paths`. The same Weyl-active realization was subsequently shown by Iter054S to admit source-ordered fine-to-coarse transport blocking in finite-panel scope.

G8A defines the branch operator structure

`K_alpha = 24^(-1/2) exp(i S_alpha / hbar) U_alpha`

with explicit unitary branch transport `U_alpha`; transport therefore cannot be silently discarded.

### B — branch-resolved Weyl3 action response: OPEN / BLOCKING

G4 supplies a genuine nonzero background-level response on the G3 Weyl-active geometry,

`d Phi_abs / d c6 = h^4 Weyl^3`,

but its own guard states that nonzero sensitivity is not a target value and that an absolute microscopic phase/action datum is still required.

No current authoritative object assigns a distinct source-faithful `dS_alpha/dc6` to each explicit G3 permutation history. In particular, the repository does not currently specify an authorized history quadrature / path accumulation / vertex weighting / cell assignment rule that converts the Weyl3 density into branch-resolved action responses on those 24 histories.

Copying the common G4 scalar sensitivity onto all histories would satisfy neither the prospective branch-resolution requirement nor the missing history-to-action map; doing so is explicitly forbidden by the Iter054U preregistration.

### C — source-scale cancellation: CONDITIONALLY AVAILABLE BUT NOT SUFFICIENT

A formal `d/dc6` operation would remove any additive `beta` source term that is genuinely independent of `c6`, and equal-history normalization factors are already controlled by G8A/G27. However, cancellation cannot manufacture the missing branch-resolved Weyl3 action response required by B.

`beta=1` was not used or authorized.

### D — nontrivial c6 sensitivity: BACKGROUND-LEVEL ONLY

The G3 background is Weyl-active and G4 proves nonzero `c6` sensitivity. What is missing is a nontrivial history-resolved differential response that can distinguish explicit branch operators while remaining source-faithful.

### E — no synthetic discretization convention: PRESERVED

No new quadrature, path weighting, source profile, branch phase, measure, or cell-assignment convention was introduced. Because the required branch-response map is absent, the gate is BLOCKED rather than repaired post hoc.

## Scientific consequence

Iter054U sharpens the current blocker beyond Iter054T:

`explicit G3 history + explicit U_alpha + nonzero background Weyl3 sensitivity`

is still insufficient for

`branch-resolved dS_alpha/dc6`.

The missing object is now localized as an **authorized history-resolved Weyl3 action accumulation rule on the same source-faithful G3 realization**. This is more specific than the generic absence of `S_alpha` and cannot be replaced by the common G4 sensitivity.

A future PASS route must therefore provide either:

1. a prospectively motivated physical/source-derived rule that maps the Weyl3 action density onto explicit G3 histories, or
2. an independent operator observable whose branch-resolved `c6` response is derivable without such a path-action assignment.

## Claim locks preserved

- theory established = `0%`;
- no experimental confirmation;
- `beta=1` unauthorized;
- `c6` symbolic/unfixed;
- no microscopic-to-IR `c6` identity;
- no global interacting measure/regulator-removal theorem;
- no strong-hyperbolicity/well-posedness theorem;
- no quantum unitarity/UV-completion/full-GR/new-physics claim;
- KMQGB `NEW_REQUIRED` unauthorized.

No GitHub Actions run was launched for Iter054U because the gate is an authority/object-definition audit and the required object is absent; manufacturing a numerical workload would have been fake load rather than an independent scientific test.
