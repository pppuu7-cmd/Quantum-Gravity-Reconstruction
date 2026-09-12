# Iter042 + Iter042R terminal result — 2026-09-12

## Authority

### Iter042 original frozen boosted gate
- head: `b6e1c31c961f2536f10e3f9480053b2a62138253`
- run: `34712954629`
- aggregate job: `103606707505`
- summary artifact: `10304692021`
- digest: `sha256:c762dbe4532ec9adca18043c42e2d9a8768f85c7c2cec44c0a00fc359b351844`
- 24/24 expected lanes present; controls valid.
- frozen aggregate classification: `PARTIAL_SCOPED_NONSTATIC_MAGNETIC_WEYL_COVARIANCE`.

Stream outcomes: A 6/6 PASS, B 0/6 PASS, C 4/4 PASS, D 4/4 PASS, E 4/4 PASS. Maximum finest boosted discrepancy was W2 `0.032577275796710214`, W3 `0.14757516443418453`. Magnetic/Weyl emergence, reversal parity, kappa scaling, and small-velocity growth survived their frozen tests; scalar covariance under the original mixed-frame reconstruction did not.

This is a scientific PARTIAL/FAIL of the original frozen observable reconstruction, not an infrastructure or solver failure. It is retained unchanged as the discovery record.

### Iter042R corrective frame-completion diagnostic
- preregistration commit: `1058f1113987c826635bab898431b0fb906f0a89`
- head: `650a7424d0377388619ca975496c12edf702ddfd`
- run: `34713234061`
- aggregate job: `103610525399`
- summary artifact: `10303868886`
- digest: `sha256:8790997c6ad28eb68d8342d0092d2b6fc5c2f20dcf567819463fe05cd7277f56`
- 24/24 expected lanes present; controls valid.
- classification: `PASS_SCOPED_G42_COVARIANCE_DEFECT_ATTRIBUTED_TO_MIXED_FRAME_RECONSTRUCTION_AND_FRAME_COMPLETION_VALIDATED`.

Stream outcomes: A 8/8, B 6/6, C 4/4, D 6/6. Exact all-four-index Lorentz transform tests gave maximum relative changes W2 `4.0759329624925397e-16`, W3 `5.365683119828423e-15`. After frame completion, maximum finest W2 discrepancy was `4.216879646694534e-05` and W3 discrepancy `6.326024551781252e-05`, while the original mixed-frame W3 discrepancies ranged up to `0.14757516443312207`.

## Scientific classification

`DERIVED/PROVEN (scoped numerical/analytic implementation result)`: the G42 scalar-covariance defect is attributable, on the frozen tested geometries and controls, to contracting curvature components whose first index pair remained internal while the second pair had already been mapped to boosted-coordinate axes. Converting all four curvature indices to one coordinate frame restores the preregistered scalar-covariance tests by a large margin.

This does **not** rewrite the original G42 result, establish global Lorentz covariance of QGR, prove a dynamical solution, fix `beta` or `c6`, select physical branch weights, or constitute experimental evidence.

## Next authorized gate

The recovery lock is now satisfied: an independent radiative geometry may be tested prospectively using the corrected all-coordinate-frame observable reconstruction. Iter043 is to use a source-independent analytic linearized TT vacuum wave as a held-out radiative Weyl tensor control; no G42 thresholds or parameters may be retuned from its output.
