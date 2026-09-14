# Iter056Y preregistration — covariant Weyl3 principal-rank bound and mixed-order obligation

Date: 2026-09-15
Gate: `ITER056Y-WEYL3-COVARIANT-PRINCIPAL-RANK-BOUND-AND-MIXED-ORDER-OBLIGATION`

## Motivation

Iter056X supplies an explicit off-shell covariant Euler response for the Weyl-cubic local operator,

`E_W3^{ab} = (1/2) g^{ab} I3 - P^{(a|cde|} R^{b)}_cde - 2 nabla_mu nabla_nu P^{mu(ab)nu}`,

with exact identities

`nabla_a E_W3^{ab}=0`

and

`g_ab E_W3^{ab}=-I3`.

Earlier Iter054C/D constructed finite exact local fourth-order principal-symbol and gauge-completion panels, but did not derive a global algebraic rank bound on the physical quotient from these covariant identities.

## Frozen question

For a non-null covector `k_a`, do the Iter056X Noether and trace identities imply that the pure `k^4` Weyl3 metric principal symbol is necessarily rank-deficient on the six-dimensional symmetric-tensor quotient by four diffeomorphism gauge directions?

If yes, determine the exact rank/nullity bound and its consequence for future hyperbolicity analysis. The gate must not infer a physical treatment choice, ghost sign, or instability from the rank bound alone.

## Frozen obligations

A. Linearize the Iter056X identities and isolate only the homogeneous fourth-order-in-`k` part of the metric linearization.

B. Show or refute the output constraints

`k_a sigma4^{ab}(k)[h] = 0`

and

`g_ab sigma4^{ab}(k)[h] = 0`

for every symmetric perturbation `h_ab`.

C. Independently retain the four exact pure-gauge input null directions

`h_ab = k_a xi_b + k_b xi_a`

already expected from diffeomorphism invariance.

D. For non-null `k`, dimension-count the simultaneous transverse+tracefree output subspace and the gauge quotient. PASS requires the count to be derived, not sampled.

E. Compare the exact bound only after derivation with existing Iter054C/D finite exact evidence. Those panels may be consistency controls, not premises for choosing the bound.

F. State the PDE consequence narrowly: whether the pure fourth-order correction can or cannot serve as a uniformly nondegenerate principal operator on all physical quotient directions. Do not promote this to strong-hyperbolicity failure of the full mixed-order system without a mixed-order characteristic analysis.

G. Keep `c6` symbolic/unfixed and preserve all canonical claim locks.

## Frozen classifications

Maximum PASS:

`PASS_SCOPED_ITER056Y_WEYL3_K4_SYMBOL_RANK_BOUND_FORCES_MIXED_ORDER_PHYSICAL_QUOTIENT_ANALYSIS`.

Scientific FAIL if the exact covariant identities imply no such rank deficiency or contradict the proposed dimension count:

`SCIENTIFIC_FAIL_ITER056Y_PROPOSED_WEYL3_K4_RANK_BOUND_FALSE`.

INVALID if index convention, non-null condition, or quotient dimension is not specified consistently:

`INVALID_ITER056Y_PRINCIPAL_RANK_BOUND_CONVENTION_INCOMPLETE`.

## Claim locks

No exact-vs-order-reduced physical treatment selection; no strong-hyperbolicity verdict for the full system; no physical mode/ghost interpretation; no fixed/running `c6`; no `beta=1`; no quantum unitarity/UV/full-QG claim. `theory established=0%`.