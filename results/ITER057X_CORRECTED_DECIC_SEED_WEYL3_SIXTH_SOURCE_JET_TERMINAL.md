# Iter057X terminal result — corrected-decic-seed Weyl3 sixth source jet

Date: 2026-09-16
Gate: `ITER057X-CORRECTED-DECIC-SEED-WEYL3-SIXTH-SOURCE-JET`
Preregistration: `b5f88ced655c4fa409c4ccb9c27eb84054ecfad7`
Implementation: `920b73f8430983255081b9bcd3ec6d222b737b08`
Parent seed authority: Iter057W terminal `90b4a8d0512bffa70c488111a71e78690368c009`
Canonical R10 data: `e8982c84cc3b4baa0ca40ed8ff7876164b728880`
Lower source authority: Iter057U terminal `20256a1779a3f76c46fcabe9f95cd0dd8c082305`
Frozen lower source data: `5c14dead0adcc8d85d33a96384c086953a5047c8`
Frozen pre-terminal payload digest: `7a8fdc92ad9bfa2a5033ef981105f7b72ca4421b`
Canonical new degree-six source data: `a1c5a3ef9a87b16653f36617dd501cb72096e357`

## Terminal classification

**`PASS_SCOPED_ITER057X_CORRECTED_DECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_SIXTH_EVEN_ORDER__O_C6_Q8_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED`**

This is exactly the prospectively frozen maximum scoped PASS.

## Reproducibility evidence

The complete exact evaluator was executed twice as separate processes from the immutable terminal Iter057Q/Iter057T/Iter057U/Iter057W coefficient authorities. Both executions independently reconstructed the full canonical decic seed, recomputed the degree-eight geometry, and recomputed the Weyl3 tensor source through degree six.

The two complete JSON objects are exactly equal.

The prospectively frozen scientific payload consists of

- classification;
- all A-K controls;
- complete basis counts;
- source nonzero counts;
- all 230 nonzero normalized source records through degree six;
- lower-source replay mismatches;
- `I3(0)/kappa^3`.

For both executions the canonical payload is exactly 23,397 UTF-8 bytes and has

`sha256:7a85a8b78e6876810ecefc6e1b37efea956caa41f26d54f4f8b9dcf16ca45249`.

The complete JSON-object hash is also identical:

`sha256:9ad2ed58b221eb1af2beb13ca0799a8d8efc18e05aa2daee950b70b5014abbbd`.

Ubuntu and Windows GitHub Actions reproduction workflows were also launched prospectively as runs `35036275106` and `35036300374`. At terminalization they remained queued behind the older non-authoritative heavy Iter057W/SymPy diagnostic lane. They are supplemental reproducibility checks, not a frozen PASS obligation for Iter057X; no result from them was used to choose or alter the classification.

## Canonical decic background replay

The evaluator consumes the production-owned Iter057W decic correction, exactly 283 nonzero normalized `R10/kappa^5` coefficients, and reconstructs

`g10 = eta + G2 + R4 + R6 + R8 + R10`.

Exact controls give

- inverse identity through coordinate degree eight;
- `Ric_ab=0` through degree eight;
- `R=0` through degree eight;
- `G_ab=0` through degree eight.

Thus the Weyl tensor can be identified with the all-lowered Riemann tensor through precisely the consumed truncation, as frozen in the preregistration.

## Exact Weyl3 reconstruction

Using the same sign, projection and Euler-tensor convention terminally validated in Iter057U, the evaluator computes exactly:

- curvature/Weyl through degree eight;
- `P=dI3/dR` through degree eight;
- `I3` and `P.R` through degree six;
- first covariant divergence of `P` through degree seven;
- double covariant divergence through degree six;
- algebraic `P.Riemann` insertion through degree six;
- `E_W3^{ab}`, `E_W3,ab`, and `Shat_ab=-E_W3,ab` through degree six.

The cubic origin normalization remains

`I3(0)/kappa^3 = 96`.

## Frozen identities and controls

All prospectively frozen A-K controls are exactly true:

- exact Iter057W R10 provenance and pure-degree-ten preservation;
- inverse/Ricci/scalar/Einstein background replay through degree eight;
- direct source construction through degree six;
- `P.R = 3 I3` through degree six;
- symmetry of `E_W3,ab` through degree six;
- trace Ward identity `g^{ab}E_W3,ab + I3 = 0` through degree six;
- covariant Noether identity `nabla_a E_W3^{ab}=0` through degree five;
- all odd source coefficients at degrees one, three and five vanish exactly;
- complete coefficient-by-coefficient Iter057U replay at degrees zero, two and four has zero mismatches;
- complete 2100-slot symmetric-tensor Taylor basis audit passes;
- no numerical tolerance or numerical rank/zero decision is used.

## Complete source counts

The full nonzero source counts through coordinate degree six are

- degree 0: 4;
- degree 1: 0;
- degree 2: 22;
- degree 3: 0;
- degree 4: 64;
- degree 5: 0;
- degree 6: **140**.

The new degree-six layer contains

- **140** nonzero normalized coefficients;
- **82** coefficients whose monomial contains time;
- **60** off-diagonal tensor-component coefficients.

The complete degree-six authority, including both exact values and `Shat/kappa^6`, is frozen in `data/ITER057X_CANONICAL_SOURCE_DEGREE6.csv`. Lower degrees remain owned by the terminal Iter057U data.

The complete audited Taylor basis through degree six contains

`10 + 40 + 100 + 200 + 350 + 560 + 840 = 2100`

slots.

## Consequence

The corrected Weyl3 Euler source is now source-owned through coordinate degree six on the production-owned canonical metric ten-jet. The next local-series question is therefore well-posed: whether the already-fixed first-order `O(c6)` Q2/Q4/Q6 response can be extended by a completely unrestricted pure degree-eight trace-reversed response jet so that covariant de Donder gauge and `DG[qhat]=Shat` hold exactly through gauge degree seven and field/source degree six.

The principal degree-eight response complex is the same unrestricted `1320 x 1650` flat polynomial complex already structurally characterized at the octic seed layer; its source-independent targets are rank 1096, left-nullity 224 and nullity 554. Affine compatibility with the new Iter057X source is not implied by those structural numbers and must be tested prospectively in the next gate.

## Scope ceiling

This PASS establishes only a finite local exact Weyl3 source jet through coordinate degree six on one canonical finite Ricci-flat seed jet. It does not establish the next `O(c6)` response, an all-orders/convergent solution, an open-neighborhood/global/asymptotic solution, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory established remains `0%`.
