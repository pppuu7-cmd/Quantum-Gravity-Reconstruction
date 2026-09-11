# QGR Construction Constitution v1.0

Status: **FROZEN FOR CANDIDATE CONSTRUCTION**

Purpose: prevent criterion drift, hindsight fitting, hidden degrees of freedom, and accidental promotion of incomplete objects.

## 1. Separation of powers

- RQIR supplies frozen methodological/comparator logic.
- KMQGB supplies independent known-framework and candidate benchmarking.
- QGR constructs candidate theory objects.
- QGR results may inform future scientific questions, but QGR may not rewrite a benchmark gate merely because a QGR branch fails it.

Any proposed benchmark change must be justified independently of the QGR candidate and versioned outside this repository before re-evaluation.

## 2. Evidence classes

Every material claim must carry one of:

- `PROVED`: exact derivation under explicit assumptions.
- `NUMERICALLY_VERIFIED`: reproducible computation with recorded domain/tolerance.
- `SOURCE_GROUNDED`: externally established result with exact applicability conditions.
- `CONJECTURED`: plausible but unproved.
- `BLOCKED`: required object/evidence is unavailable.
- `REFUTED_IN_SCOPE`: explicit contradiction/counterexample inside the stated scope.

A conjecture may not be used downstream as if proved. A scoped refutation may not be promoted to a family-level no-go without a coverage theorem.

## 3. Candidate-state vocabulary

Use only:

- `UNFORMED`
- `PROPOSED`
- `PARTIAL`
- `PASS_SCOPED`
- `BLOCKED`
- `FAIL_SCOPED`
- `PROMOTABLE`
- `REJECTED`

`PROMOTABLE` does not mean true. It means sufficiently specified to enter independent frozen benchmarking.

## 4. Anti-overfitting rules

A candidate is penalized or rejected if it requires:

- arbitrary functions introduced only after observing a failed gate;
- independent counterterms/coefficients without a generating physical principle;
- regulator prescriptions selected solely to recover the target answer;
- IR parameters that cannot be identified with UV parameters through one realization;
- switching between inequivalent models at different gates;
- fitting GR, causality, or a target observable by definition rather than deriving it;
- hidden branch selection after seeing benchmark results.

If additional freedom is unavoidable, its dimension, symmetry, priors/measure, and physical origin must be explicit.

## 5. Same-realization rule

The strongest target is one chain:

`microscopic definition -> quantum dynamics -> physical states/amplitudes -> controlled coarse graining/continuum -> Lorentzian geometry -> GR regime -> normalized observable -> comparator`.

Evidence from mutually incompatible realizations cannot be spliced into a PASS.

## 6. Finite-definition obligation

The theory must specify why its physical amplitudes/observables exist. Acceptable routes can include a genuinely finite construction, a canonical distributional extension, a controlled renormalization prescription fixed by physical principles, or another mathematically explicit mechanism. Merely listing available local counterterms is insufficient.

## 7. Rigidity obligation

Before fitting empirical targets, estimate the effective freedom of the candidate. Prefer architectures where symmetry, consistency, composition, positivity/causality, and continuum closure determine most or all coefficients.

A candidate with enough unconstrained freedom to mimic arbitrary outcomes is not a successful reconstruction.

## 8. Low-energy obligation

Recovery of classical gravity must be demonstrated, not named. The target includes:

- effective 4D Lorentzian geometry;
- Einstein/GR dynamics in a controlled regime or a precisely bounded deformation;
- parameter identity across scales;
- clear approximation domain and corrections.

## 9. Quantum-consistency obligation

The candidate must state its Hilbert/state-space or generalized probabilistic structure, observables, composition rule, and physical positivity/unitarity condition appropriate to the framework. If conventional unitarity is emergent rather than fundamental, the replacement principle and recovery theorem must be explicit.

## 10. Causality obligation

The candidate must specify the causal object used operationally and show that causal consistency is not imposed only after integration or by deleting unwanted histories without a derived measure rule.

## 11. Observable closure

At least one nontrivial observable must be normalized and computable through the same UV-to-IR realization. A theory that produces only formal amplitudes with no controlled observable map remains `PARTIAL/BLOCKED`.

## 12. Uncertainty and comparator

Comparisons require a common domain plus propagated theoretical, numerical, and matching uncertainty. Precision cannot compensate for an unidentified observable or parameter map.

## 13. Falsification-first policy

For every candidate branch, record before heavy computation:

1. what would kill the branch;
2. the cheapest decisive test;
3. which assumptions are being tested;
4. what remains valid if the branch fails.

Prefer tests with high expected information gain per unit compute.

## 14. Claim locks

Until independently authorized, QGR must not claim:

- all existing quantum-gravity frameworks fail;
- a fundamentally new model is logically necessary;
- QGR is unique;
- QGR is experimentally confirmed;
- a scoped divergence/extension burden is a full no-go.

## 15. Versioning

This constitution is `v1.0`. Any modification requires:

- a new version;
- an explicit rationale independent of a desired candidate outcome;
- a changelog;
- re-audit of any candidate promoted under an earlier constitution.
