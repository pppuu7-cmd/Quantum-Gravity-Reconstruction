# Iter054F terminal result — mixed-order strong-hyperbolicity evolution object not fixed

Date: 2026-09-14

Gate: `ITER054F-WEYL3-MIXED-ORDER-STRONG-HYPERBOLICITY-OBJECT-DEFINITION-AUDIT`

## Provenance

- preregistration: `f4838c50ded00c6d62c9ef822f1f75285eceddf9`
- initial implementation: `823b4a24419f5e616eea256b6ba6359fbba30bd4`
- initial workflow head: `9b719f0b54030a74a5c166e93db1a2898d90bdfe`
- initial run: `34817447178`
- initial run classification: `ITER054F_IMPLEMENTATION_OR_CONTROL_INVALID_A1_CHARPOLY_SYMBOL_IDENTITY`
- control-only repair: `04cc0e065c5eb88385437f233e8f8fc22111332b`
- authoritative exact-retry run: `34817585523`
- aggregate job: `103892887023`
- summary artifact: `10336467977`
- summary digest: `sha256:2ff9d546b8443080fc48c6cf27c2c0b0764b7686b72aff2e53735e7d1bb8a27f`

Raw exact-retry artifacts:

- A0: `10336638836`, digest `sha256:965b08f65019898fce78707addcdb9c13d7f6e18829b194a5c65713e0b630fd6`
- A1: `10337068116`, digest `sha256:419ef7128ff8aac7b67eb6c2bee80015941134c062224b5fbdffaee1be3002e6`
- B0: `10336738559`, digest `sha256:d7bed879f248b2cbf964377e0c4e671d50063860d2f88f5f2a83b0c95bf66860`
- B1: `10336638846`, digest `sha256:8637f5a7909ec33d98877ba7a14078161772f27b838fe1b971f311fdd5377141`

The initial implementation-invalid run remains permanently historical and is not rewritten.

## Frozen terminal classification

**`BLOCKED_OBJECT_DEFINITION_ITER054F_MIXED_ORDER_EVOLUTION_REDUCTION_NOT_FIXED`**

This is a valid terminal BLOCKED result, not a scientific FAIL of the QGR candidate.

All four frozen exact-retry streams were valid:

- A0: frozen QGR authority census valid and returned `BLOCKED_OBJECT_DEFINITION`;
- A1: exact same-characteristic-polynomial diagonalizable-vs-Jordan counterexample valid;
- B0: exact symmetrizable wave-system positive control valid;
- B1: claim/authority firewall valid.

## Exact missing object

The frozen authority does not yet specify/authorize all eight required components of a genuine mixed Einstein + symbolic-`c6` Weyl3 strong-hyperbolicity evolution object:

1. `state_vector_or_reduction_variables`;
2. `time_direction_and_spatial_covector_domain`;
3. `first_order_in_time_or_equivalent_higher_order_formulation`;
4. `principal_evolution_matrix_or_equivalent`;
5. `gauge_variables_and_gauge_evolution_equations`;
6. `constraint_variables_and_principal_constraint_propagation`;
7. `norm_or_symmetrizer_and_open_domain`;
8. `map_to_mixed_einstein_weyl3_and_gr_limit`.

The A0 authority census was source-locked to the preregistration commit, so later repository edits cannot retroactively satisfy this gate.

## New scientific-program fact

A characteristic determinant/root certificate is logically insufficient for strong hyperbolicity. The exact A1 control used

`A_diag = [[v,0],[0,v]]`

and

`A_J = [[v,1],[0,v]]`.

Both have the exact real characteristic polynomial `(mu-v)^2`, but the first has eigenspace dimension two and is diagonalizable while the second has eigenspace dimension one and is defective. Therefore real characteristic roots alone cannot authorize a QGR strong-hyperbolicity claim.

The B0 detector control independently confirms that a properly specified first-order wave principal matrix with `H=I` has real eigenvalues, a complete eigensystem, positive symmetrizer and symmetric `H A`.

## Interpretation ceiling

Iter054F does **not** establish that QGR is non-hyperbolic or ill posed. It establishes that the present durable authority does not yet define the mathematical evolution object required to ask the QGR-specific strong-hyperbolicity question without inserting additional structure.

No preferred first-order reduction, gauge evolution, constraint propagation, symmetrizer, exact-vs-order-reduced treatment, physical mode count, residue/ghost sign, energy positivity, unitarity, quantum amplitude/measure, UV completion, full GR recovery, experiment or new physics is inferred.

`c6` remains symbolic/unfixed. `beta=1` remains unauthorized. Theory established remains 0%.

## Authorized next dependency

Before constructing a preferred evolution reduction, the next high-information gate is to determine whether existing QGR microscopic authority already selects the **dynamical treatment** of the Weyl3 correction: exact finite-`c6` higher-derivative dynamics versus perturbative/order-reduced analytic effective dynamics.

That selection must be derived prospectively from QGR-internal authority, not chosen after observing stability/spectrum outcomes. If no such rule exists, the correct next terminal state is another object-definition/selection BLOCKED result identifying the missing microscopic principle.
