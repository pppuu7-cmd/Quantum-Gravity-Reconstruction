# QGR Current Research Front

Updated: 2026-09-18

## Programme status

`candidate_program_roadmap_readiness = 100%` — roadmap/infrastructure readiness only, not correctness probability. `theory_established = 0%`. No experimental confirmation.

## Preserved authority

Iter049 authority remains `ITER049-WEYL3-SPHERICALLY-REDUCED-VARIATIONAL-RESPONSE`, authoritative retry run `34719948722`, preregistration `72b21197d594ab6c5f36a34dfbd18a68b97d0a1d`, retry head `c8e574b2a78ae02c3e1476ef1daf7efc8268c342`. Initial run `34719814120` remains diagnostic/non-authoritative. Iter048 terminal PASS 24/24 remains recorded and must not be repeated.

Einstein-completed QF degree-flow authority remains run `35312874182`, classification `QF8_REQUIRED_ON_EINSTEIN_COMPLETED_SEED`, frozen payload SHA256 `64e11805fdc9229b7221ce6dea3f94f8abf1de3b76e63f3da76df1b431811797`, durable result commit `c518f55ae9a9c584c00d5044a8ec48ae697074f2`. Scoped construction only; not the complete 4D covariant Weyl^3 Euler-Lagrange theorem.

## Latest terminal scientific/localization result

Gate `COVARIANT_WEYL3_OFFSHELL_A7_PRINCIPAL_SYMBOL_CAUSAL_LOCALIZATION`, preregistration `5c5d6197ff15573f2110729ddd41c4e64c005e7a`, authoritative run `35368354816`, production head `d2b9802e79c8b244457c50690b449a852e92741c`.

Jobs: Researcher `105676145129`, Critic `105676144975`, terminal `105676380927`.

Artifacts/digests: Researcher `10557168059` / `sha256:60208238c2d25aa4834e5b12dbd358b40408a71b032b3dd230b4362e025c5e36`; Critic `10556793874` / `sha256:2ad8e346cbd161d593497a55b35b1351350abf0bb623c2191d43fbf033262268`; terminal `10557212958` / `sha256:b6c83393e18c4b0b85a8c25867b65f3e42bfd096348f1176570375b57e9eb067`.

Frozen terminal payload SHA256 `9dbcf7fab9dc9a26b6228f3915aeb12a10a91cac052705e237b6d9797b78842d`.

Classification: `PRINCIPAL_SYMBOL_AND_VOLUME_MATCH__LOWER_ORDER_COVARIANTIZATION_OR_IBP_LOCALIZATION_REQUIRED`.

All ten ordered principal-symbol slots agree exactly and the metric-volume term agrees exactly. The parent full off-shell discrepancy is independently reproduced and remains nonzero: `-86355995554365317186893343264769708206041673/10039118967354700841951532316479538176000000`. Thus the surviving mismatch is localized away from the tested principal symbol and volume term.

Durable result commit: `feba733ef0e7d1423be4e38ad5c9c9c8b623a5ea`.

## Active next task

The lower-order causal-localization gate is now terminal.

Authoritative run: `35403445578`.
Durable terminal result commit: `6ccfededab41dbe01b071916a5aa746491273276`.
Classification: `LOWER_ORDER_LOCALIZED_EXACT`.

Exact ordered result:
- `LOWER_ORDER_CURVATURE_VARIATION_BEFORE_IBP`: MATCH;
- pointwise first-derivative coefficients `Fi`: MATCH;
- `FIRST_DERIVATIVE_IBP_TRANSFER`: **FIRST EXACT DIVERGENCE**;
- `SECOND_DERIVATIVE_LOWER_ORDER_IBP`: MATCH, with A7 principal control still exact;
- downstream connection/covariantization classes differ, but are downstream of the frozen first divergence;
- `ALGEBRAIC_EULER_TERM`: NOT REACHED.

Frozen Stage-3 scalar transfer difference:
`-86355995554365317186893343264769708206041673/20078237934709401683903064632959076352000000`.

The immutable per-coordinate transfer ledger shows the smallest ordered slot is `i=0`, already nonzero:
`-433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000`.

Both class sums reconstruct their parent totals exactly and the class-difference sum exactly reconstructs the frozen parent discrepancy. Source lock, target-blind serialization, exact arithmetic, volume control, principal control, c6 lock, and Q10 lock all passed.

No repair is authorized. The next admissible task is to prospectively freeze one narrow product-rule decomposition of `-d_0 F_0` into derivative-on-background-coefficient, derivative-on-h-jet, and explicitly defined connection/covariantization completion pieces, then locate the first exact subterm divergence.

## Infrastructure note

The initial PR #33 event before scientific execution created no Actions run because the workflow terminal fallback contained invalid YAML heredoc indentation. Prospective execution-only repair was frozen in `a9fd6e1aeb80f4c638f7950f40363a776f5c98ac`, applied in `395c62ca147e2979252c183a43843b7db9aa8adc`, and the execution binding was refreshed in `c54217accd99acbcb47fc9f4eb82d7c9f05649b4`. No scientific job ran before that repair.

## Locks

Corrected degree-eight coefficients and corrected Q10 remain LOCKED. `c6=SYMBOLIC_UNFIXED`. `beta=1` unauthorized. `theory_established=0%`. No experimental confirmation. Finite/symmetry-reduced panels are not global theorems. No quantum-unitarity, UV-completion, physical-c6, new-physics, or global-QGR claim is authorized.
