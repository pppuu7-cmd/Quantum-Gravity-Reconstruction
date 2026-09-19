# Preregistration — COVARIANT_WEYL3_A7_CRITIC_SLOT00_CONNECTION_COMPLETION_REPLAY

Date: 2026-09-19
Status: **FROZEN BEFORE CORRECTED-INTERFACE IMPLEMENTATION**

## Parent authorities

Fi first-jet causal audit:
- result commit `07ad77de0506a3de5e7db601e2cfc8b5edc37c5c`;
- run `35404041767`;
- first divergence `(i,j)=(0,0)`;
- Researcher and Critic agree exactly in metric, inverse-metric, curvature/Weyl and perturbation source classes;
- first source-class divergence is `CONNECTION_JET`;
- frozen Researcher direct-metric lane has a nonzero connection jet;
- frozen Critic Palatini lane serialized `CONNECTION_JET=0`.

Independent connection authorities:
- multicoordinate neutral result `17b79ca06ff2208e9b09a8ec74fa509a18e5ec4c`: complete neutral extraction matches Lane B;
- formal result `8ee3437b0cad15ff2d47d6b87840b38bdc535c81`: A is exactly negative B over the complete formal basis;
- partial-to-covariant conversion result `81fcf14aa119eb00a9522c0d5e694fe1290b54ea`: conversion tensor derived from `partial partial = covariant Hessian - C_nabla` matches formal B exactly.

Historical parent results remain immutable.

## Scientific question

If the frozen Critic Palatini `Fi` construction is replayed at the already-localized first slot `(i,j)=(0,0)` with the independently established partial-to-covariant connection completion inserted at the Riemann-variation interface, does the corrected Critic first jet agree exactly with the frozen Researcher direct-metric first jet at that slot?

## Frozen corrected interface

Reconstruct the original Critic objects from the same repository sources and witness:

`OFFSHELL_A / d=7 / i=0 / j=0`.

Reconstruct the original pointwise `Fi[0]` and original `d_0 Fi[0]` exactly.

Independently derive the numeric 256-component partial-to-covariant conversion tensor from:
- the frozen repository metric second jets;
- the frozen perturbation value `h_ab`;
- the tensor identity `partial partial = covariant Hessian - C_nabla`;
- repository Riemann derivative ordering.

Do not import Researcher science code, formal Lane B code, multicoordinate code, or any parent target value.

For every Riemann free component `abcd`, add to the Critic variation polynomial only the scoped linear term

`x0 * K_conversion_abcd`

for `i=0`.

This leaves the pointwise `Fi[0]` unchanged while adding the derived connection completion to `d_0 Fi[0]`.

No other source class or slot is modified.

## Target-blind serialization

Before reading parent Researcher values, serialize:
- original Critic pointwise `Fi[0]`;
- corrected Critic pointwise `Fi[0]`;
- original Critic `d_0Fi[0]`;
- correction contribution;
- corrected Critic `d_0Fi[0]`;
- numeric conversion tensor and SHA256;
- reconstructed source classes at slot 00.

## Mandatory controls

- exact rational arithmetic;
- same frozen witness and parent Critic construction;
- original Critic pointwise and slot computations reproduce independently;
- corrected pointwise `Fi[0]` equals original pointwise exactly;
- only `CONNECTION_JET` is altered in the frozen source-class ledger;
- correction tensor serialized before target comparison;
- source implementation contains no frozen Researcher slot value, Researcher connection value, or Lane-B tensor hash;
- no tolerance, coefficient fitting, sign choice, free-index permutation, or adjustment of any other slot.

## Frozen terminal taxonomy

- `CORRECTED_CRITIC_SLOT00_EXACTLY_MATCHES_RESEARCHER`
- `CORRECTED_CRITIC_SLOT00_REMAINS_DIFFERENT`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

## Interpretation ceiling

A terminal exact match would close the already-localized slot-00 connection interface and identify the old Critic zero-connection serialization as incomplete at that scoped first jet. It would not automatically reclassify the parent covariant FAIL, because other first-jet slots and the full first-IBP transfer require a separately preregistered corrected replay before any parent-level conclusion.

`c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no experimental, global QGR, unitarity, UV-completion, physical-c6, or new-physics claim.
