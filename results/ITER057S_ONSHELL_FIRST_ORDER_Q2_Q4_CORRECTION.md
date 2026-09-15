# Iter057S terminal result — on-shell first-order Q2/Q4 correction

Date: 2026-09-15
Gate: `ITER057S-ONSHELL-FIRST-ORDER-Q2-Q4-CORRECTION`
Status: TERMINAL SCOPED PASS

## Frozen authority

- Preregistration: `a59858ce6dbc08493325d8ba406229da18013d40`
- Implementation: `0159a788e7568de45610c93295f86b1e2f981d6a`
- Production head: `a54efe452119aa698a82afc7f84cef05a0d5656f`
- Actions run: `34957251270`
- Job: `104342161583`
- Artifact: `10392255734` (`iter057s-onshell-q2-q4-correction`)
- Artifact digest: `sha256:b22aff7c02ef056aaed1df7ed06c06b181d4be601e3b05eac7b361856f7143f5`

## Classification

`PASS_SCOPED_ITER057S_ONSHELL_FIRST_ORDER_Q2_Q4_CORRECTION_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_SECOND_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN`

This classification is based on consumption of the raw exact job output and frozen evidence, not on green CI alone.

## Exact results

- Full unrestricted quartic correction space: 350 coefficients.
- Exact affine system: `180 x 350`.
- `rank(M)=164`.
- `rank([M|r])=164`.
- Nullity: `186`.
- Left-nullity: `16`.
- All 16 canonical Bianchi compatibility contractions: exactly zero.
- One exact particular Q4 solution: 34 nonzero normalized coefficients.
- Corrected Iter057R source replay: PASS.
- Iter057Q seed replay: PASS.
- Source Noether identity through degree one: PASS.
- Direct full-seed unreduced `DG_ab[qhat]-Shat_ab` through coordinate degree two: exactly zero for all ten independent symmetric components.
- Full-seed de Donder condition through degree three: exactly zero.
- Point unreduced residual: exactly zero.
- Numerical tolerance used for exact-zero decisions: no.
- `c6`: symbolic/unfixed and factored out.

## Scope ceiling

This PASS establishes only an exact finite local Taylor coefficient solution for the `O(c6)` response through the second even coordinate order on the canonical Einstein-completed seed available at this stage. It does not establish higher coordinate orders, convergence, an open-neighborhood solution, global/asymptotic boundary data, a complete four-dimensional interacting solution, physical Weyl3 characteristics, strong hyperbolicity, ghost/stability claims, quantum unitarity, regulator removal, UV completion, experiment, or QGR correctness.

`beta=1` remains unauthorized. Theory established remains `0%`. KMQGB `NEW_REQUIRED` is not authorized by this result.