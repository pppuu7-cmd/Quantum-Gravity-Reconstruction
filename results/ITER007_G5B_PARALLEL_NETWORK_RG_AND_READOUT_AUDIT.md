# QGR Iter007-G5B — parallel network RG, physical representation, and scale audit

Date: 2026-09-12
Status: `PASS_SCOPED_MULTILANE_AUDIT / NEW_FULL_NETWORK_COMPOSITION_BLOCKER`
GitHub Actions run: `34653064309`
Head: `876016920a0a6487fce5edc9cc5f80a5f71dcaa3`

## Objective

Run the open G5B/G6 questions in independent lanes rather than extrapolating the one-dimensional causal-path result to the full four-dimensional network.

Five GitHub Actions lanes ran in parallel and the fail-closed aggregate completed successfully.

## Lane 1 — full-network RG scaling

A single small-cell history channel has

`E_h = I + h^4 D + O(h^5)`.

If a fixed physical support of effective cell-counting dimension `d_eff` contains `O(h^-d_eff)` locally traced cells, naive leading accumulation scales as

`h^(4-d_eff)`.

Therefore

- `d_eff=1`: `h^3`;
- `d_eff=2`: `h^2`;
- `d_eff=3`: `h`;
- `d_eff=4`: `h^0`.

The exact-24-history numerical stress toy confirms the first three slopes and approaches a nonzero four-dimensional purity-loss plateau of about `0.0333` for the recorded normalization.

Classification:

`PASS_SCOPED_PATH_IRRELEVANT_BUT_LOCAL_TRACE_4D_BULK_MARGINAL`.

This **does not** prove that the physical QGR full-network composition is local product tracing. It proves that the previous path-level `O(L h^3)` argument cannot by itself establish four-dimensional continuum suppression.

## Lane 2 — physical seed representation

The exact four-cover physical seed space has S4 character

`[8,0,0,-1,0]`

and decomposes as

`8 = 2 + 3 + 3prime`.

The signed pair/two-form ordering-commutator representation has character

`[6,0,-2,0,0]`

and decomposes as

`6 = 3 + 3prime`.

The ordering covariance eigenspaces are

- eigenvalue `1/3`: `3prime`;
- eigenvalue `5/3`: `3`.

For the isolated two-dimensional physical polarization irrep `E`,

`End(E)=1 + sign + 2`.

Hence there is no linear S4-equivariant map

`3 + 3prime -> End(E)`.

Classification:

`PASS_SCOPED_PHYSICAL_SEED_8D_EQUALS_2_PLUS_3_PLUS_3PRIME_AND_ORDERING_NOISE_LIVES_IN_3_PLUS_3PRIME`.

Consequence: a physical two-mode purity prediction must specify the directional/fiber transport or an allowed quadratic contraction. An arbitrary two-by-two noise matrix cannot be inserted.

## Lane 3 — competing higher-derivative operators

For parity-even metric-only local bulk terms at four derivative order in 4D, the raw curvature-squared basis is

- `R^2`;
- `R_ab R^ab`;
- `R_abcd R^abcd`.

Modulo the Euler/Gauss-Bonnet combination, there are two dynamical bulk directions. `box R` is a boundary term.

However, any Hamiltonian/unitary correction preserves purity by cyclicity,

`d Tr(rho^2)/dt = 0`,

whereas the positive QGR history double-commutator can decrease purity.

Classification:

`PASS_SCOPED_PURITY_LOSS_DISCRIMINATES_HISTORY_CHANNEL_FROM_UNKNOWN_UNITARY_CURVATURE_SQUARED_ACTION_TERMS`.

This does not set the curvature-squared coefficients to zero; it only shows that they cannot fake the proposed purity-loss signature.

## Lane 4 — coherent composition before trace

For two independent cells with 24 orthogonal history labels each, keeping both history registers coherently and tracing only after both cells gives the explicit `24^2=576` product-Kraus sum.

This reduced state agrees with sequential local channel composition to numerical precision below `1e-12`, and the product instrument remains complete.

Classification:

`PASS_SCOPED_DELAYING_TRACE_OVER_INDEPENDENT_PRODUCT_HISTORY_REGISTERS_DOES_NOT_CANCEL_LOCAL_CHANNEL`.

Thus merely postponing the partial trace cannot cancel the putative four-dimensional marginal effect. Cancellation would require a **derived non-product cross-cell identification/recombination of histories**.

## Lane 5 — physical scale audit

Let the continuum Einstein-Hilbert coefficient be `a`, with dimension `L^-2`, and let `kappa` be the dimensionless microscopic coefficient multiplying the dimensionless cell curvature `h^2 R`.

Then

`kappa = a h^2`.

If `a=1/(16 pi G_N)` in natural units,

`h^2 = 16 pi kappa G_N`.

The current QGR construction fixes the relative nonlinear structure but has not independently fixed the absolute dimensionless `kappa`. Hence `h` is not separately predicted for path observables.

Classification:

`PARTIAL_H_NOT_INDEPENDENTLY_FIXED_FOR_PATH_OBSERVABLES_BUT_EXPLICIT_H_CANCELS_IN_NAIVE_4D_LOCAL_TRACE_DENSITY`.

In the naive four-dimensional locally traced accumulation, explicit `h^4` per cell is canceled by `h^-4` cell counting, so the unresolved microscopic length no longer suppresses the leading bulk channel.

## Aggregate conclusion

All five GitHub Actions lanes and the aggregate passed.

The dominant question has changed. The main uncertainty is no longer simply the numerical value of `h`. It is:

> Does the microscopic CCRC/QGR refinement composition actually produce independent product history registers that are traced locally across the four-dimensional network, or does the same realization derive a constrained/shared history object whose coarse channel has different scaling?

If local product histories are forced, the leading positive history channel is marginal in four-dimensional cell counting and retains microscopic S4/Lorentz anisotropy. That would be a sharp phenomenological prediction and potentially a falsification route.

If a correlated/shared history structure is derived, its cancellation or altered scaling must follow from the pre-existing composition rules; it may not be introduced solely to remove the marginal channel.

## New blocker

`BLOCKED_FULL_NETWORK_HISTORY_COMPOSITION_AND_PHYSICAL_READOUT_MAP__PRODUCT_REGISTER_LOCAL_TRACE_GIVES_MARGINAL_4D_LORENTZ_ANISOTROPIC_CHANNEL`.

## Next gate

`QGR-ITER007-G6A-FULL_NETWORK_HISTORY_COMPOSITION_AND_PHYSICAL_READOUT_MAP`

1. derive adjacent-cell history identification from CCRC composition/refinement;
2. determine whether global histories are a Cartesian product, a constrained subset, or a quotient under shared events;
3. derive the projective trace/coarse operation rather than assume it;
4. derive the directional/fiber map from the `2+3+3prime` physical seed space to a concrete two-mode preparation/readout;
5. if product/local trace is forced, accept the marginal channel and proceed to a phenomenological exclusion test;
6. do not add cross-cell interference weights or correlations only to force Lorentz restoration.

## Reproducibility

- `.github/workflows/qgr-iter007-parallel-g5b-g6.yml`
- `code/qgr_iter007_parallel_bulk_rg.py`
- `code/qgr_iter007_parallel_seed_rep.py`
- `code/qgr_iter007_parallel_operator_census.py`
- `code/qgr_iter007_parallel_coherent_trace.py`
- `code/qgr_iter007_parallel_scale_audit.py`
- `code/qgr_iter007_parallel_aggregate.py`
