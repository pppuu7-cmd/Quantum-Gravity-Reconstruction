# Iter057I adversarial review — short

Date: 2026-09-15
Reviewed terminal result: `94a1b18b9281e6939ed07a19f06acbc49f655d4d`
Prospective preregistration: `53bd47d2b21d25dfa212bfb46c81a681bb827969`

## Counterexample-first check

The natural failure modes do not defeat the scoped pointwise construction. For a first-order conformal perturbation `q_ab=2 psi g0_ab` with `psi(0)=0` and `partial psi(0)=0`, curvature-times-`q` and first-derivative terms vanish at the frozen point. The exact four-dimensional conformal variation therefore gives

`DG_ab[q](0) = -2 A_ab + 2 eta_ab A`,

with `A_ab=partial_a partial_b psi(0)` and `A=eta^{ab}A_ab`. Its trace is `S=6A`, so the inverse

`A_ab = eta_ab S/6 - S_ab/2`

is correct for an arbitrary symmetric pointwise target. Hence `S_ab=-E_W3_ab[g0](0)/A_E` cancels the `O(c6)` source at that point without fixing `c6`.

A Bianchi/integrability counterexample would require neighborhood or higher-jet compatibility, not merely the frozen field equation at one point. The preregistration and terminal note explicitly leave those conditions open, so no hidden neighborhood solution is needed for this gate.

## Chronology / provenance

Chronology is prospective and clean: preregistration `53bd47d2...` precedes derivation `a6e9663b...`, which precedes terminalization `94a1b18b...`. This is an analytic gate; no production artifact is required for the claimed algebraic pointwise result.

## Scope qualification

The phrase "on-shell" must remain strictly **pointwise and formal through first order in `c6`**. This result does not construct an on-shell background on any open set. Likewise, preservation of the source blocks is limited to the stated first-order derivative-symbol bookkeeping: the Einstein principal `k2` coefficient is unchanged because the pointwise metric is unchanged, while background-induced changes of the Weyl3 `L4/L2` coefficients are `O(c6)` and therefore enter `c6 E_W3` only at `O(c6^2)`. This does not certify the full corrected linearized operator, characteristics, hyperbolicity, modes, ghosts, stability, or a physical treatment.

Historical FAIL/BLOCKED results remain immutable. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; finite/local certificates are not global theorems; classical consistency is not quantum consistency; diagnostic progress is not closure; theory established remains `0%`.

## Verdict

`CONFIRMED_SCOPED`
