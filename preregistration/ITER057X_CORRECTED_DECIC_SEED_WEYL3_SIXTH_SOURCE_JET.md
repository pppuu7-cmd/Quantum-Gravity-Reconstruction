# Iter057X preregistration — corrected-decic-seed Weyl3 sixth source jet

Status: PROSPECTIVELY FROZEN
Date: 2026-09-16
Gate: `ITER057X-CORRECTED-DECIC-SEED-WEYL3-SIXTH-SOURCE-JET`
Parent seed authority: Iter057W terminal `90b4a8d0512bffa70c488111a71e78690368c009`.
Lower source authority: Iter057U terminal `20256a1779a3f76c46fcabe9f95cd0dd8c082305`.
Canonical decic data: `data/ITER057W_CANONICAL_R10_NORMALIZED.csv` from commit `e8982c84cc3b4baa0ca40ed8ff7876164b728880`.

## Question

What is the complete exact corrected-seed Weyl3 Euler source `Shat_ab=-E_W3,ab` through coordinate degree six on the production-owned canonical Einstein seed `g10`, and does it satisfy all lower-source replay, homogeneity, symmetry, trace-Ward, Noether and parity controls exactly?

This gate computes a source only. It does not solve the next `O(c6)` response, fit/sign-select/run `c6`, or alter any canonical Einstein-seed coefficient.

## Why this gate is next

The Weyl3 Euler tensor contains two covariant derivatives of an object quadratic in curvature. A source coefficient at coordinate degree six can depend on the background metric ten-jet. Iter057W has now fixed that canonical ten-jet and established vacuum Einstein cancellation through coordinate degree eight. Therefore the degree-six Weyl3 source can now be source-owned without borrowing an unfixed higher seed jet.

## Frozen background and arithmetic

Use exact rational/Fraction polynomial arithmetic only. Reconstruct exactly the canonical metric

`g10 = eta + G2 + R4 + R6 + R8 + R10`

with the already-fixed Iter057O/Iter057Q/Iter057T/Iter057W canonical particular coefficients. No lower homogeneous freedom may be re-solved or changed.

The metric inverse is required through coordinate degree eight. Since the perturbation begins at degree two, include the exact Neumann series through `h^4`. Compute Christoffels through degree nine and curvature through degree eight. Numerical zero tests/tolerances are forbidden.

## Frozen Weyl3 convention

Use exactly the same Weyl3 invariant, Riemann/Weyl sign convention, `P=dI3/dR` projection and Euler-tensor convention already terminally validated in Iter057U. On the canonical Ricci-flat seed through the required order, the Weyl tensor equals the Riemann tensor through the consumed truncation.

Construct, in exact polynomial arithmetic:

- curvature/Weyl through degree eight;
- `P^{abcd}` through degree eight;
- `I3` and `P.R` through degree six;
- first covariant divergence of `P` through degree seven;
- double covariant divergence through degree six;
- algebraic `P.Riemann` insertion through degree six;
- `E_W3^{ab}` and `E_W3,ab` through degree six;
- `Shat_ab=-E_W3,ab` through degree six.

## Frozen obligations

A. Verify exact Iter057W `R10` provenance, exactly 283 nonzero normalized coefficients, and pure degree ten.

B. Reconstruct the full canonical seed and require inverse identities, Ricci tensor, scalar curvature and Einstein tensor to vanish exactly through coordinate degree eight.

C. Compute the full Weyl3 source through coordinate degree six directly from the frozen tensor formula; no fitted/source-interpolated model is allowed.

D. Verify the cubic homogeneity identity `P.R = 3 I3` exactly through coordinate degree six.

E. Verify symmetry of `E_W3,ab` exactly through coordinate degree six.

F. Verify the trace Ward identity in the same Iter057U convention, `g^{ab} E_W3,ab + I3 = 0`, exactly through coordinate degree six.

G. Verify the covariant Noether identity `nabla_a E_W3^{ab}=0` exactly through coordinate degree five.

H. Require every odd source coefficient of coordinate degrees one, three and five to vanish exactly.

I. Replay the complete terminal Iter057U source at degrees zero, two and four exactly, coefficient by coefficient. No historical pre-Iter057U source may be substituted.

J. Audit the complete symmetric-tensor Taylor basis through degree six:

- degree 0: `10*C(3,3)=10` slots;
- degree 1: `10*C(4,3)=40`;
- degree 2: `10*C(5,3)=100`;
- degree 3: `10*C(6,3)=200`;
- degree 4: `10*C(7,3)=350`;
- degree 5: `10*C(8,3)=560`;
- degree 6: `10*C(9,3)=840`;
- total: `2100` slots.

Export every nonzero normalized source coefficient. Degree-six records must additionally report `Shat/kappa^6`. Report total degree-six nonzero count, time-containing count and off-diagonal count.

K. Record the finite-order scope ceiling and retain all physical/quantum claim locks.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057X_CORRECTED_DECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_SIXTH_EVEN_ORDER__O_C6_Q8_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED`

iff A-K pass exactly.

BLOCKED:

`BLOCKED_ITER057X_EXACT_WEYL3_DEGREE6_SOURCE_NOT_TECHNICALLY_REALIZED`

if the exact degree-six tensor source cannot be computed without altering the frozen problem.

INVALID:

`INVALID_ITER057X_SEED_MUTATION_OLD_SOURCE_REUSE_RESTRICTED_ANSATZ_NORMALIZATION_OR_EXACTNESS_CONTROL`

if canonical seed coefficients are changed, a restricted ansatz is substituted, an obsolete source is reused, numerical zero/tolerance is used, or any mandatory replay/Ward/Noether/parity control fails.

## Scope ceiling

A PASS would establish only the exact local Weyl3 Euler source through coordinate degree six on one finite canonical Ricci-flat seed jet. It would not establish the next `O(c6)` metric response, an all-orders solution, convergence, an open-neighborhood/global/asymptotic solution, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory established remains `0%`.
