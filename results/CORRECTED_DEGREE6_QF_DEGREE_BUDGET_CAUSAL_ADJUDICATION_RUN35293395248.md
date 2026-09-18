# Terminal result — corrected degree6 QF degree-budget causal adjudication

Date: 2026-09-18

Gate: `CORRECTED_DEGREE6_QF_DEGREE_BUDGET_CAUSAL_ADJUDICATION`

Preregistration: `10643a75f85da4ea447d00115006d78714ecfa24`.
Execution-only repair preregistration: `eac1aa993256876a9e1fe86721eda741b5920dc4`.
Authoritative repaired production head: `70181617c4b9db90d40976052d8c72cc91985865`.
Authoritative run: `35293395248`.

Jobs:
- Researcher `105440863046`
- Critic `105440863307`
- Frozen aggregate `105447170826`

Artifacts/digests:
- Researcher `10527787236` / `sha256:ee33eeb76c16f960537d7390b3556a2ee802bbaea4b972e684a9045502bbbe21`
- Critic `10528211790` / `sha256:abdd7c2eadc0db1ab09cba0ec02972a84eed1d1a9a941d954e46a7b196592839`
- Terminal `10527582423` / `sha256:57ede639ce1ae2760a5e9b8ada441662e2a4e15772836cc32f0d057e72d2b4f5`

Frozen aggregate payload SHA256: `73a4158058a2313666c33fa3c0c6b17d0404dab531eb8bb91af6ed3cd7097882`.

## Terminal classification

`UNRESOLVED_QF_DEGREE_BUDGET` (the workflow aggregate emitted the implementation label `BLOCKED_QF_BUDGET_LANES`; under the preregistered outcome vocabulary this maps to the frozen unresolved outcome because exact controls/provenance were not all satisfied).

This is not a theory PASS and does not reclassify Iter057AT or corrected Iter057Y.

## Raw evidence consumed

Both lanes executed the repaired environment and independently produced the same provisional source-hash ladder:

- q=6: `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`
- q=7: `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`
- q=8: `2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d`
- q=9: `2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d`
- q=10: `2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d`

Both lanes therefore provisionally report first change at q=8 and plateau from q=8. QF6 reproduces the durable Iter057AT ordered 840-vector exactly, and the target was loaded only after the ladder freeze.

However the preregistered gate cannot classify `QF8_REQUIRED_FOR_DEGREE6_SOURCE` yet. Both lane payloads have `ricci_zero=false` and `scalar_zero=false`; more importantly, the implementation does not yet emit the preregistered term-by-term hashes (algebraic P·R, double-divergence, metric×I3, index-lowering) or the required per-monomial derivative degree-flow table. Therefore the causal condition “change carried by terms allowed to descend through the double divergence” is not certified. The aggregate correctly remains non-PASS.

The provisional q=8 plateau is evidence motivating the next diagnostic only; it is not authorized as a terminal scientific conclusion.

## Locks

`c6=SYMBOLIC_UNFIXED`; `beta=1` unauthorized; corrected degree-eight coefficients and corrected Q10 remain LOCKED; theory established 0%; no experimental confirmation; finite panels are not global theorems; no quantum-unitarity, measure, regulator-removal, UV-completion, unique-theory, new-physics, or KMQGB `NEW_REQUIRED` claim is authorized.
