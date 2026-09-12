# QGR Iter046 — exact finite-amplitude nonlinear pp-wave radiative sector

Date: 2026-09-13
Status: `PASS_SCOPED_QGR_L1_EXACT_FINITE_AMPLITUDE_NONLINEAR_PPWAVE_RADIATIVE_SECTOR`

## Authority and provenance

- Preregistration: `status/ITERATION_046.md`
- Preregistration commit: `125d030e90ac86697710c9ed0cee432c5ff54596`
- Implementation commit: `bd7ea711e8f1f98e5727321f77bc90841510b440`
- Aggregate commit: `d625cb2f636ef6781513c30600572156b7c806d3`
- Workflow commit: `0a4c93cae719379ca4b38c10047fc6a41e92ed0b`
- Production trigger/head: `37ff955a57b6822d800b6755282a6bc557c3a0e2`
- Authoritative run: `34718135187`
- Aggregate job: `103621013033`
- Aggregate artifact: `10305972518`
- Aggregate artifact digest: `sha256:ca1cfb10420cb4e79f4324f009c0a664317098b7bb08b717f052d82397961a89`

Frozen thresholds and lane definitions were not changed after production inspection.

## Terminal aggregate

The aggregate consumed all 34 scientific lane artifacts and returned:

- expected scientific lanes: **34**;
- found scientific lanes: **34**;
- unique scientific lanes: **34**;
- passes: **34**;
- controls valid: **true**;
- stream counts: `A=12, B=6, C=6, D=6, E=4`;
- every frozen stream full-pass: **true**.

Classification:

`PASS_SCOPED_QGR_L1_EXACT_FINITE_AMPLITUDE_NONLINEAR_PPWAVE_RADIATIVE_SECTOR`

## What passed

### A — exact nonlinear harmonic pp-wave vacuum

All 12 finite-amplitude harmonic pp-wave witnesses had an exactly vanishing Einstein tensor obtained from the already reconstructed all-orders local two-derivative QGR-L1 action, while retaining nonzero curvature. The aggregate minimum nonzero Riemann-component count was **8**.

### B — nearby non-vacuum falsification controls

All six deliberately non-harmonic controls were correctly rejected as vacuum. As one raw witness, B1 produced exactly

- `G_uu = -u/5 - 1/5`;
- transverse Laplacian `2u/5 + 2/5`;
- exact identity `G_uu = -1/2 Laplacian(H)`;
- all other Einstein-tensor components exactly zero.

Thus the gate is not vacuously returning zero for arbitrary pp-wave profiles.

### C — held-out polarization superpositions

All six held-out finite-amplitude harmonic polarization mixtures remained exact vacuum configurations.

### D — finite-amplitude curvature scaling

All six lanes passed the preregistered exact full-Riemann amplitude-scaling relation between independent nonzero amplitudes while remaining exact vacuum witnesses.

### E — coordinate-covariance anti-artifact

All four frozen invertible coordinate transforms preserved the exact vacuum result with nonzero curvature, excluding the original coordinate chart as the source of the result.

## Scientific interpretation

Within the already reconstructed **metric-only, local, at-most-two-derivative QGR-L1 action**, the candidate admits a nontrivial exact finite-amplitude curved radiative pp-wave family. This extends the earlier linearized TT radiation contract to a genuinely nonlinear exact special family and includes explicit nearby non-vacuum falsification controls.

This is stronger than a perturbative principal-symbol or flat-background TT check, but it remains a **special algebraically structured radiative sector**.

## Claim guard / what is not established

This result does **not** establish:

- generic nonlinear or strong-field stability;
- global hyperbolicity for arbitrary curved solutions;
- that all radiative initial data evolve into regular solutions;
- quantum unitarity or interacting quantum amplitude closure;
- a value of `beta` or `c6`;
- the dynamics of the six-derivative `c6 * Weyl^3` correction;
- experimental confirmation;
- physical distinctness from GR in this two-derivative sector.

`theory established` remains **0%**.

## Next frontier

The highest-value immediate front is no longer another flat/linear TT check. It is to determine how the QGR-specific six-derivative `Weyl^3` operator activates across genuinely different curvature classes with `c6` kept symbolic/unfixed, then move from operator activation to its actual curved-background Euler-Lagrange response or another generic non-special curved-background dynamical gate.
