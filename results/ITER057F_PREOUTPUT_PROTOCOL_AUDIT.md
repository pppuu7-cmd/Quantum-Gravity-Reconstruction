# Iter057F pre-output protocol audit — degree-two gauge control qualification

Date: 2026-09-15
Status: `PRE-OUTPUT METHODOLOGY AUDIT / NO SCIENTIFIC RESULT YET`

Active gate: `ITER057F-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-EXTRACTION`
Preregistration: `8df569f7414a9d634b72e54264b529245b356288`
Running production: `34905773224`

This note is committed while all ten Iter057F basis lanes are still `in_progress`, before any lane artifact or aggregate result is available. It does not change the frozen Iter057F contract and does not inspect/tune against outputs.

## Qualified frozen predicate

Iter057F control G froze the requirement that the extracted degree-two block satisfy

`L2[k_(a xi_b)] = 0`

for the four principal pure-gauge polarization tensors.

That condition is **not a generally valid standalone subprincipal gauge identity on a curved background**.

## Why

For a natural covariant Euler tensor `E[g]`, exact diffeomorphism covariance gives

`D E[gbar][L_xi gbar] = L_xi E[gbar]`.

At principal order, the highest-degree symbol annihilates the principal gauge polarization. This correctly underlies the Iter054C/057A `L4` gauge-null control.

At lower differential order the identity is hierarchical. A genuine curved-background Lie-derivative perturbation contains not only the leading principal piece

`h_ab ~ k_a xi_b + k_b xi_a`,

but also connection/background-dependent lower-derivative pieces. Acting on those pieces with the higher-degree operator contributes at the same frequency degree as `L2` acting on the leading polarization. Equivalently, the differentiated Noether identity couples subprincipal symbols to derivatives of higher-symbol coefficient tensors.

At the G3 origin the pointwise odd-degree operator coefficients vanish by inversion parity, but their spatial derivatives need not vanish. Hence this hierarchy does not reduce in general to the isolated statement `L2[k_(a xi_b)]=0`.

Therefore:

- if Iter057F control G passes, that is an additional scoped property of the extracted G3-origin `L2`, not a generally required gauge theorem;
- if control G fails while the source, convergence, held-out-frequency and exact-`L4` controls pass, the frozen Iter057F aggregate must still retain its preregistered `INVALID` classification, but that INVALID would not by itself invalidate the numerical `L2` extraction;
- the gate must not be repaired or reclassified after output.

## Correct independent degree-two Ward control available prospectively

The exact Iter056X trace identity

`g_ab E_W3^{ab} = -I3`

is algebraic in the Euler tensor and does not involve derivatives of the output. Linearizing and comparing the degree-two frequency coefficient at the G3 origin gives a valid standalone identity:

`gbar_ab L2^{ab}[h] = - (delta I3[h])_degree2`.

The right-hand side is independently computable from the source background Weyl tensor and the principal metric-to-Weyl map. This supplies a clean no-fit validation of any extracted `L2` and does not assume an incorrect isolated subprincipal gauge-null condition.

A separate successor gate should freeze this trace-Ward comparison before consuming Iter057F outputs. Historical Iter057F remains immutable under its original A-G contract.
