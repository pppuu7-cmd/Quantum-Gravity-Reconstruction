# Iter054E Preregistration

Gate: `ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT`

Status at freeze: **PREREGISTERED BEFORE OUTPUTS**

## Scientific question

Can a frozen finite mixed-order Einstein + Weyl3 quotient characteristic model be assembled with symbolic `c6`, recover its GR-connected branch exactly as `c6 -> 0`, and separate any singular high-frequency branch without converting that finite algebraic evidence into an unsupported strong-hyperbolicity or physical-spectrum claim?

## Authority boundary

This gate is a finite exact symbolic characteristic/regime audit downstream of Iter054D. It is not a full nonlinear PDE theorem and not a proof of strong hyperbolicity. `c6` remains symbolic/unfixed. `beta=1` remains unauthorized. No physical root weights, residues, ghost sign, unitarity, UV completion, experiment or new-physics claim may be inferred.

## Frozen mixed-order characteristic family

On each frozen quotient eigenchannel use the exact dimensionless polynomial

`P(z; eps, lambda) = z + eps*lambda*z^2`,

where `z` denotes the GR second-order characteristic factor, `eps` is a symbolic placeholder proportional to `c6` times the frozen Weyl-active background scale, and `lambda` is a frozen nonzero rational quotient-eigenvalue witness. This is a regime-separation proxy for the mixed second+fourth derivative structure, not the full tensor PDE determinant.

Freeze the 12 exact rational witnesses

`lambda = {1/3, 2/5, 3/7, 4/9, 5/11, 6/13, -1/4, -2/7, -3/8, -4/11, -5/12, -6/17}`.

Freeze control scaling `s=3/2` and exact sample eps values `{1/20, 1/10, 1/5}` only for algebraic cross-checks; symbolic predicates remain authoritative.

No post-output changes of polynomial, witnesses, scaling, controls, branch definitions or interpretation are allowed.

## Frozen streams

### A0 — exact mixed-order factorization and GR limit

For every frozen `lambda`, require exactly:

1. `P = z*(1 + eps*lambda*z)`;
2. `P|eps=0 = z`;
3. the GR-connected root is exactly `z_GR=0` for all eps;
4. the extra root is exactly `z_HD=-1/(eps*lambda)`;
5. `eps*z_HD = -1/lambda` and therefore the extra branch is singular as `eps -> 0` rather than continuously GR-connected;
6. deliberate sign-flip control `P_bad=z-eps*lambda*z^2` must change the extra-root sign.

PASS iff all exact predicates hold for all 12 witnesses and the negative control is detected.

### A1 — frozen regime/scaling separation

For each witness and frozen nonzero eps value require:

1. substitution of both exact roots annihilates `P`;
2. scaling `eps -> s*eps` leaves `z_GR=0` invariant;
3. scaling `eps -> s*eps` maps the singular branch to `z_HD/s` exactly;
4. `|z_HD|` increases as the exact positive magnitude of eps decreases over the frozen positive eps panel;
5. no branch weight or probability is assigned.

PASS iff all predicates hold for all 36 witness/eps cases.

### B0 — malformed mixed-order controls

Freeze two deliberately malformed controls:

- missing-Einstein control `P_noGR = eps*lambda*z^2`;
- wrong-order control `P_wrong = z + eps*lambda*z^3`.

Require exact detection that:

1. `P_noGR|eps=0` is identically zero and therefore fails GR-limit recovery;
2. `P_wrong` has degree 3 in `z` and therefore does not match the frozen second+fourth derivative proxy degree 2;
3. both malformed controls are rejected for all witnesses.

### B1 — authority boundary

PASS only if the result explicitly leaves unresolved:

- derivation of the full tensorial gauge-fixed Einstein+Weyl3 characteristic determinant on an open background/covector region;
- proof of real characteristics on such an open region;
- complete eigenvector/diagonalizability or symmetrizer estimate for strong hyperbolicity;
- gauge/constraint propagation;
- energy estimate;
- physical mode multiplicities, residues and ghost signs;
- quantum amplitude/measure interpretation.

Frozen B1 classification:

`MIXED_ORDER_FINITE_SYMBOLIC_REGIME_SEPARATION_CERTIFICATE_STRONG_HYPERBOLICITY_NOT_YET_AUTHORIZED`

## Aggregate classification

Full scoped PASS string:

`PASS_SCOPED_ITER054E_EINSTEIN_WEYL3_MIXED_ORDER_REGIME_SEPARATION_STRONG_HYPERBOLICITY_NOT_AUTHORIZED`

Any missing stream, parse error, altered witness, failed GR limit, failed singular-branch scaling, invalid negative control, or authority overclaim is FAIL/INVALID.

## Interpretation lock

Even full PASS establishes only a finite exact symbolic mixed-order regime-separation certificate for the frozen proxy family. It does not establish the full tensor characteristic determinant, strong hyperbolicity, well-posedness, an energy estimate, constraint propagation, physical mode count, ghost sign, stability, quantum unitarity, UV completion, full GR recovery of the nonlinear theory, experimental confirmation, or new physics. Candidate-program percentage is roadmap readiness only, never correctness probability.
