# Iter051C D2N/D2Z conditioning diagnostics — terminal

Date: 2026-09-13

## Historical lock
`G51C-D2` remains terminal `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION` (run `34741924103`, aggregate job `103683219373`, artifact `10312601307`, digest `sha256:dcdef4dff571b1ba3350a2e6acec7478e1aec1b6847d5fc7765c17d82b931c78`). Its frozen threshold and 19/20 result are not rewritten.

## D2N independent numerical-conditioning diagnostic
Preregistration `b3fc227d6521b92fc6f5131f99b3812080bf4ee8`; implementation `0fbfbdcb552e170f9a228bf555057b63065d19d6`; aggregate classifier `c294074743955d66b0e14a3fd9a56430c09428a2`; workflow `9ae51dd4e0bcc9db769ef782e16e16987d4be60c`; production head `c6efa69559a0222242e6c79a617c09c3d4e42adc`.

Authoritative run `34742201899`; aggregate job `103684234240`; aggregate artifact `10312526872`; digest `sha256:5809e09fb4365a745399f9db5fd1630b85d9cb280f23dca1d4a03337774b55a4`.

Classification: `PASS_DIAGNOSTIC_D2N_NEAR_NULL_ERROR_COLLAPSES_UNDER_INDEPENDENT_FIVE_POINT_STENCIL`.

8/8 preregistered lanes passed. On the exact D2-B3 replay, the old nested 3-point angular absolute error was `7.838355602488458e-09`, while the independently implemented nested 5-point error was `1.743008620663677e-11`, ratio `0.002223691688739307`. Five-point vector relative residual was `2.5056495286480338e-09`; final-step change `1.2143187845045726e-09`. The historical `+2D` vector residual remained `1.8803596058345882`.

## D2Z exact near-zero diagnostic
Preregistration `645a972a2280e645cf9f5c86d456c7f2ad333b49`; implementation `8edd979ece4b972ad49337f28b22a0ccc4066688`; workflow `4dfa87805bd8d09dd7615ac67614a7835bbfc95b`; production head `6558221ff4de5d688ab6da57aed81bdf358d6b80`.

Authoritative run `34742259726`; job `103683830040`; artifact `10312697366`; digest `sha256:326e868eafc082965602eb9a6b57e792b4fcb45661c5546d117269ae3ed8cf5b`.

Classification: `DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_CONFIRMED`.

At the D2-B3 witness radius `r=6/5`, exact reduced `E_S=-3.9949986160730709e-07`. The nearest positive exact numerator root is `r=1.199993503822622846...`, only `6.496177377135481e-06` away. The derivative at the root is nonzero (`-0.06149851736...`), confirming a simple zero. The radial relative conditioning proxy is `1.8472151595166072e5`; angular-to-large-component amplitude ratio is `3.859380167902877e-05`.

## Scientific interpretation
The two independent diagnostics agree that the sole D2-B3 failure is dominated by numerical conditioning of a near-null exact component under the original nested 3-point derivative. This does **not** convert historical D2 to PASS and does **not** establish the full Weyl^3 EOM. It authorizes only a newly preregistered replacement held-out spherical validation using the independent five-point derivative and fresh radii/profiles.

`c6` remains symbolic/unfixed. Theory established = 0%. No experimental confirmation. `beta=1` remains unauthorized.
