# Iter051C — Full Weyl^3 EOM Assembly: Terminal Scientific Failure

Date: 2026-09-13
Gate: `ITER051C-FULL-WEYL3-EOM-ASSEMBLY`

## Frozen authority
- preregistration commit: `4bdb68cfd50ea7b521372bf633c1b1b43d848625`
- implementation commit: `d19aecadfc316c2ec08d75fb5dd188bff245444f`
- aggregate commit: `bf4f5a2aeb376efa2e5af4f1e529bebe7864b937`
- workflow commit: `77df1829163213a6e6b2a9e6c0464adea223e1ec`
- authoritative production head: `a69562cb0552abc283dfef1ffff941809578ffd8`
- authoritative run: `34741060700`
- aggregate job: `103680844833`
- summary artifact: `10311749167`
- summary digest: `sha256:1b4a324a05666a2ff0c67bdb922e87efc600d70d481ab380bb4532baf43c8c99`

Frozen assembly:
`H = A + sqrt(-g) sym(P.R) + 2 sqrt(-g) D`.
The sign/coefficient is not changed after production.

## Terminal classification
`SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`

Aggregate consumed all 18/18 unique scientific lane artifacts with no parse errors and valid controls.
- PASS: 12/18
- FAIL: 6/18
- Stream A generic metric-consistent 4D jets: 4/4 PASS
- Stream B exact G48 reduced-Euler–Lagrange cross-check: 0/6 PASS
- Stream C conformally-flat null controls: 4/4 PASS
- Stream D constant Lorentz-frame covariance: 4/4 PASS

Frozen aggregate worst values:
- A final-step change: `1.6393165790579325e-07` <= `2e-3`
- A H symmetry residual: `2.3092583401052025e-10` <= `3e-7`
- A P algebraic residual: `4.336808689942018e-18` <= `2e-9`
- A Riemann algebraic residual: `2.0816681711721685e-17` <= `2e-9`
- B exact reduced residual: `1.9999998126753908` > `3e-4`
- B final-step change: `2.3681555754359778e-05` <= `2e-4`
- C H norm: `1.3788834741709153e-38` <= `2e-7`
- C |I3|: `7.521872962925854e-46` <= `2e-10`
- C P norm: `1.3341387265554257e-46` <= `3e-9`
- D covariance residual: `5.424006967038421e-08` <= `8e-4`

Representative raw B0 lane (`job 103680735820`) had valid Lorentz/inverse controls and stable finite-difference behavior, but predicted reduced coefficients `[-362.95917635949195, -1133.9315348573639, 2353.026331641177]` versus exact G48 `[230.97374174008783, 1049.9342082457274, -2286.496765074649]`, with relative residuals `[1.6363628660853045, 1.925923811068362, 1.9717259574736143]`. Its raw artifact is `10313185019`, digest `sha256:ad54715270a50dae266c9c673da4ffa17f27d5bcc78ae276c2b673fbbf7a79c2`.

## Interpretation
The frozen full assembly is rejected by its prospectively designated decisive sign/coefficient falsification control. The failure is not an infrastructure failure and cannot be repaired by threshold weakening. The simultaneously passing A/C/D streams show that tensor symmetry, conformally-flat null behavior, numerical stability, and tested frame covariance are not sufficient to establish the Euler–Lagrange assembly.

This result does **not** show that the Weyl^3 operator is absent or that QGR is false. It shows that the particular frozen assembly convention has not reproduced the independently derived exact reduced variation and therefore cannot be promoted as the complete 4D Weyl^3 EOM.

## Next authorized work
Prospectively preregister a diagnostic decomposition of the reduced response into the independently computed `A`, `sqrt(-g) sym(P.R)` and `sqrt(-g) D` pieces. Preserve this G51C failure permanently. Any replacement assembly must be separately preregistered from an independent variational derivation; it may not be selected merely by fitting the failed Stream-B data.

## Claim locks
`c6` remains symbolic and unfixed. `beta=1` remains unauthorized. Full covariant six-derivative EOM remains unestablished. Theory established remains `0%`. No experimental confirmation, absolute-energy positivity, quantum unitarity, or KMQGB `NEW_REQUIRED` claim follows.
