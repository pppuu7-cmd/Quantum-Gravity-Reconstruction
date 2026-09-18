# Preregistration — CORRECTED_DEGREE6_EINSTEIN_COMPLETED_QF_DEGREE_FLOW_ADJUDICATION

Date: 2026-09-18
Parent terminal result: `cb55fe8ac6d697616e05a5ccc21c84c40c9a5ab7`

## Frozen question

On an independently verified Einstein-completed higher-order seed whose Ricci tensor and scalar vanish through the geometry boundary used by the source constructor, does the exact homogeneous degree-six Weyl^3 Euler source depend on QF ceiling q=8 rather than q=6, and if so which preregistered contribution/derivative-flow channel causes the first q7→q8 change?

## Frozen design

Use the existing next Einstein-completion layer already present in repository lineage (R12 if its existing controls certify Ricci/scalar zero through the required boundary). Do not alter its coefficients to improve this gate. Before loading the Iter057AT target, two independent implementations must:

1. verify seed provenance and exact inverse;
2. verify Ricci and scalar vanish through the full geometry boundary used for the experiment; if this fails, classify unresolved and stop;
3. compute target-blind exact QF ladder q=6,7,8,9,10 with identical source operator, signs, normalization, basis ordering and homogeneous degree-six output projection;
4. freeze the complete 840-slot source hash at every q;
5. freeze term hashes for algebraic P·R, double-divergence, metric×I3 and index-lowering contributions at every q;
6. emit per-monomial degree-flow provenance for zero-, one-, and two-covariant-derivative stages sufficient to identify any q7→q8 change;
7. only after all preceding evidence is serialized, load the historical Iter057AT ordered-vector target SHA256 `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b` for comparison.

No sign fitting, scale fitting, normalization fitting, target-driven coefficient adjustment, threshold weakening or post-hoc witness selection is allowed. `c6` remains symbolic/unfixed. Corrected degree-eight coefficients and Q10 remain locked.

## Frozen outcomes

- `QF6_SUFFICIENT_ON_EINSTEIN_COMPLETED_SEED`: q6..q10 source vectors agree exactly and required controls pass.
- `QF8_REQUIRED_ON_EINSTEIN_COMPLETED_SEED`: q6=q7, first exact change is q8, q8=q9=q10, both lanes agree on all 840 slots and term/degree-flow witnesses identify the same causal channel, with all seed controls passing.
- `OTHER_QF_THRESHOLD_ON_EINSTEIN_COMPLETED_SEED`: an exact stable threshold other than q8 is independently reproduced with complete witnesses.
- `UNRESOLVED_EINSTEIN_COMPLETED_QF_DEGREE_FLOW`: seed controls fail, lanes disagree, no stable ladder exists, or mandatory term/degree-flow witnesses are incomplete.

Even a positive scoped outcome is only a constructor degree-budget certificate on the frozen finite covariant-jet seed; it is not a global theorem or a complete 4D Weyl^3 functional derivative.

All standing claim locks remain in force: theory established=0%; no experimental confirmation; beta=1 unauthorized; c6 unfixed; finite/symmetry-reduced panels are not global theorems; G45 does not prove absolute energy positivity/quantum unitarity; G35-G37 distant roots do not authorize physical weights; KMQGB NEW_REQUIRED unauthorized.