# Iter055L terminal result — minimal bounded one-particle / boundary sector-bridge class

Date: 2026-09-14
Preregistration: `c6d1150c66e09db8f52ff6c49407f87ab787507c`

## Terminal classification

`PASS_SCOPED_ITER055L_SMEARING_CLASS_MINIMAL_DOMAIN_PRESERVING_BRIDGE__PROFILE_SELECTION_STILL_NEW_INPUT`

## 1. SMEAR boundedness and existing-domain preservation

Let `H_char` be the already-authoritative G6F physical one-particle Hilbert space. For any finite family of physical kernels `phi_j in H_char`, define

`B_j[a] = <phi_j, a>_(H_char)`.

By Cauchy-Schwarz,

`|B_j[a]| <= ||phi_j|| ||a||`

for every `a in H_char`. Thus each smeared boundary observable is a bounded linear functional on the **entire existing G6F Hilbert completion**. No restriction of the one-particle state domain is required.

Because `phi_j` is itself chosen in the physical quotient Hilbert space, the functional depends only on the physical quotient class and does not require a gauge representative.

This is precisely the mathematical repair that raw point restriction lacked in Iter055K: the non-square-integrable evaluation kernel is replaced by an actual Hilbert-dual kernel.

## 2. Finite-frame covariance of the class

G6F already supplies unitary/isometric finite-frame maps `U_A` on the physical characteristic Hilbert space. Transform states and observable kernels together:

`a -> U_A a`,
`phi_j -> U_A phi_j`.

Then

`<U_A phi_j, U_A a> = <phi_j,a>`.

Therefore the **class** of physical Hilbert-dual smearings is covariant without choosing a preferred basis, observer or polarization gauge. A concrete kernel need not be Lorentz invariant; it transforms covariantly with the observable/preparation it defines.

## 3. Refinement compatibility is an exact kernel relation

Suppose a coarse boundary observable is required to be a fixed linear combination of fine observables,

`B_c = sum_f M_cf B_f`.

Then Hilbert duality gives the exact class-level condition

`phi_c = sum_f conjugate(M_cf) phi_f`

(with the convention adjusted to the chosen inner-product linearity). Thus refinement compatibility can be tested directly on kernels. The class does not manufacture a refinement rule; it exposes the rule that any concrete profile must satisfy.

## 4. Existing Iter009-G6 channel remains defined

SMEAR does not alter `H_char`. The established finite 24-history one-particle channel and its trace-class strong-limit statement therefore remain defined on exactly the same normal-state domain. A future concrete bridge can test channel/observable intertwining without first replacing the proven one-particle Hilbert space.

## 5. TRACE cannot satisfy the frozen minimality requirement

Raw point values are not defined continuously on the full `L2` completion (Iter055K). Making them continuous requires additional regularity: a proper subspace/domain with stronger topology, a selected representative class, weighted decay, bandlimit/cutoff, Sobolev/trace assumptions, or equivalent structure.

Such a construction may be mathematically viable as a **new candidate version**, but it no longer preserves the full established G6F `L2` state domain. The frozen Iter055L minimality test therefore rejects TRACE as the minimal domain-preserving extension.

The covariance control strengthens this conclusion for the simplest weighted repairs: the Lorentz group is transitive on the nonzero future null cone, including energy rescalings by boosts along a null direction. Hence a scalar weight depending only on null momentum and invariant under the full finite-frame/Lorentz action cannot provide a nontrivial ultraviolet scale profile; observer-frequency weights, Euclidean momentum norms, fixed cutoffs and bandlimits introduce extra structure. This does not rule out every covariant regular dense subspace; it shows that such a stronger-domain repair is additional structure rather than a consequence of the existing `L2` definition.

## 6. Residual freedom remains large and is explicit

Iter055L selects only the **mathematical class** of the minimal domain-preserving bridge. It does not select the kernels `phi_j`.

Different square-integrable physical kernels correspond to different coarse boundary observables/profiles. Existing QGR authority does not yet fix:

- support/shape of each kernel;
- physical smearing scale;
- metric-versus-connection kernel relation;
- exact mapping to B3 cells/vertices/edges;
- refinement matrices or kernel refinement law;
- detector/preparation interpretation.

Therefore the next scientific problem is profile/source selection inside the surviving SMEAR class, not interacting dynamics yet.

## Scientific consequence

The dependency chain is narrowed to

`G6F / Iter009-G6 one-particle Hilbert+channel`

`-> bounded covariant physical smearing bridge class`

`-> [MISSING concrete source-motivated kernel/refinement family]`

`-> operational overlap/intertwining test`

`-> new interacting boundary dynamics axiom selection`.

This is genuine narrowing: the raw point bridge is dead, and a stronger trace-domain repair is not minimal if the established G6F state space is to be preserved. But no concrete physical smearing has yet been derived.

## Next highest-information gate

Audit whether existing finite-cell/B3 geometry, physical measure, compact-support perturbation structure, or local observable definitions determine a **canonical covariant smearing/refinement kernel family** without a tunable width/profile. If not, record kernel selection as explicit new candidate input and freeze a minimal parameterized kernel class with counterexample/identifiability tests before any dynamics work.

## Claim ceiling

No concrete overlap map, boundary channel, interacting dynamics, beta/c6 fixing, Weyl3 treatment, regulator removal, full unitarity, UV completion, GR recovery, experiment or theory establishment is obtained. Theory established remains 0%.

No GitHub Actions run was required; the class comparison is exact Hilbert-space analysis.
