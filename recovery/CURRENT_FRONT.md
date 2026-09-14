# QGR Current Research Front

Updated: 2026-09-14
Primary active gate: `Iter054E / mixed-order Einstein+Weyl3 characteristic and regime audit`
Project phase: `MODEL_CONSTRUCTION / WEYL3 HYPERBOLICITY`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- Quantum amplitude/measure transition: **not authorized**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID results are immutable.

## Iter054C — TERMINAL SCOPED PASS

Run `34808147191`; classification `PASS_SCOPED_ITER054C_WEYL3_LOCAL_METRIC_PRINCIPAL_SYMBOL_GAUGE_DEGENERACY_CONFIRMED_HYPERBOLICITY_NOT_AUTHORIZED`.

Finite exact local fourth-order Weyl3 metric principal-symbol certificate only; no hyperbolicity theorem.

## Iter054D — TERMINAL SCOPED PASS

Gate: `ITER054D-WEYL3-PRINCIPAL-ORDER-GAUGE-FIXING-CHARACTERISTIC-AUDIT`.

Authoritative production:

- preregistration `b3d758c25449027d23a5879c3df135c4903c37d4`
- implementation `862b1e6e8f1c1da259819069cb2f553bc6a9bd52`
- production head `a81bd1a7a4044d8b639fab9fb3641269ae89a779`
- run `34811376305`
- aggregate job `103873320736`
- summary artifact `10334957634`
- digest `sha256:5b75f82c9eef94af5add54b5577de5ca26432d92eb20f164b91475679f66a869`
- classification `PASS_SCOPED_ITER054D_WEYL3_PRINCIPAL_ORDER_GAUGE_COMPLETION_QUOTIENT_INVARIANCE_HYPERBOLICITY_NOT_AUTHORIZED`

Raw frozen evidence: A0 passes all four exact gauge-functional/rank/homogeneity/negative-control probes. A1 passes all 48 frozen background/covector cases: both `alpha=1` and `alpha=7/3` lift exactly four gauge null directions, preserve quotient bilinears, and detect a deliberately wrong completion. B0 retains two exact null-covector diagnostics where the fourth-order gauge completion vanishes; correction-only rank/nullity data are diagnostic only. B1 explicitly leaves the full mixed-order Einstein+Weyl3 principal system, full characteristic polynomial, open-region real-characteristic audit, strong hyperbolicity/symmetrizer, constraint propagation, energy estimate and physical ghost/residue interpretation unresolved.

Durable terminal note: `results/ITER054D_TERMINAL_RESULT.md` at commit `fedcb69def11d95fbca186fcae0b05eaa4e737cd`.

Interpretation lock: finite exact fourth-order principal gauge-completion/quotient-invariance certificate only. It does not establish full-system characteristics, strong hyperbolicity, well-posedness, physical mode count, ghost sign, unitarity, UV completion, or experiment. `c6` remains symbolic/unfixed; theory established remains 0%.

## Active blocker / Iter054E

Next gate: `ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT`.

Required prospective obligations before outputs:

1. assemble a frozen mixed-order symbol/polynomial with an Einstein second-order piece plus the Weyl3 fourth-order correction, retaining `c6` symbolic;
2. freeze backgrounds and timelike/spacelike/null covector or frequency/momentum panels before execution;
3. verify exact GR-limit recovery as `c6 -> 0` and separate the GR-connected branch from any singular high-frequency branch rather than assigning physical weights;
4. distinguish statements about a finite characteristic panel from strong hyperbolicity on an open region;
5. include deliberate malformed-sign/scaling negative controls;
6. fail closed on energy estimate, gauge-constraint propagation, ghost/residue sign, physical spectrum, quantum unitarity and amplitude/measure claims.

## Locked next sequence

1. Prospectively preregister Iter054E with symbolic `c6`, frozen mixed-order equations/polynomials, witnesses and classifier.
2. Implement and run exactly as frozen; no post-output witness or threshold changes.
3. If the finite mixed-order characteristic/regime audit passes, open a separate strong-hyperbolicity/open-region/symmetrizer gate rather than overclaiming.
4. Only after that may a physical Weyl-active spectrum/stability gate be opened.
5. Quantum amplitude/measure remains downstream.
