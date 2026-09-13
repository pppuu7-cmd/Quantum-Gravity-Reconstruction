# Historical runtime audit and parallelization plan for a possible corrected full Iter053 replacement

Date: 2026-09-14
Status: operational analysis only. No partial substantive values from the active Iter053T runs are used. This note is not a preregistration and does not authorize a new gate.

## Historical evidence

The terminal Iter053R production run `34782291893` provides direct wall-clock evidence for the cost of the frozen A4+B2+C2 object.

Representative job timings from the immutable historical run:

- A0 substantive lane: about 70 minutes (`20:56:47Z -> 22:07:14Z`).
- A1 substantive lane: about 71 minutes (`20:56:42Z -> 22:07:25Z`).
- C0 substantive lane: about 57 minutes (`20:56:42Z -> 21:54:02Z`).
- C1 substantive lane: about 97 minutes (`20:56:46Z -> 22:33:33Z`).

The C implementation already used a local two-process split for base/transformed sides, so the large C1 wall clock is not evidence that a single serial C function is adequate. Hosted-runner CPU availability and nested multiprocessing can vary substantially.

## Consequence

If a full corrected replacement becomes scientifically authorized, the execution architecture should be frozen to expose more of the mathematically independent work to GitHub Actions-level parallelism rather than relying mainly on nested `ProcessPoolExecutor` inside one runner.

The scientific lane definitions must not change. Only execution decomposition may change prospectively.

## Recommended frozen execution DAG

### Stage 1: independent computational artifacts

For each A lane `Ai`, predeclare two independent components:

1. `Ai-direct`: GL7/GL8 direct action variation, epsilon convergence, signature/inverse/collar controls.
2. `Ai-weighted`: GJ2/GJ3 H5 bulk, correct-sign and wrong-sign bulk, H5-side controls.

For each B lane `Bi`:

1. `Bi-direct`: GL7/GL8 direct null value and direct controls.
2. `Bi-weighted`: GJ2/GJ3 weighted H5 null value plus sampled W3/P/H5 controls.

For each C index `Ci`, predeclare four independent heavy components:

1. `Ci-base-direct`;
2. `Ci-base-weighted`;
3. `Ci-transformed-direct`;
4. `Ci-transformed-weighted`.

The transformed weighted component must use the prospectively authorized explicit unfactored polynomial source if the active Iter053T gates terminally authorize that correction.

All Stage-1 jobs should use `fail-fast:false` and write raw deterministic artifacts. No Stage-1 result may alter another Stage-1 input, threshold, seed, order or execution path.

This architecture exposes up to:

- A: `4 x 2 = 8` jobs;
- B: `2 x 2 = 4` jobs;
- C: `2 x 4 = 8` jobs;

for a total of **20 independent computational jobs** before combiners, subject to hosted-runner concurrency limits.

## Stage 2: deterministic lane combiners

After all required components for a scientific lane are present:

- four `A-combine` jobs compute the frozen A predicates;
- two `B-combine` jobs compute the frozen B predicates;
- two `C-combine` jobs combine base/transformed direct+weighted results and compute both per-frame generic predicates and frame-covariance predicates.

Combiners perform no new scientific computation beyond deterministic arithmetic on frozen artifacts. They must fail INVALID on missing/duplicate/mismatched artifact identity.

## Stage 3: one frozen aggregate

Only after all eight A4+B2+C2 scientific lane combiners are terminal should one aggregate classifier produce the gate verdict.

The aggregate must preserve exactly the prospectively frozen full-replacement classifier and must not inspect runner success as a substitute for lane JSON predicates.

## Provenance controls required by the split

Each Stage-1 artifact should record at minimum:

- gate identifier;
- lane/component identifier;
- metric seed and perturbation seed;
- source code commit/head;
- support radius;
- GL/GJ order as applicable;
- epsilon tuple as applicable;
- H5 derivative step as applicable;
- coordinate frame and shear index for C;
- explicit polynomial-source identity for weighted components;
- signature/inverse/control validity;
- deterministic raw outputs used by the combiner.

Each combiner must reject any mismatch in these frozen identities.

## Why the split is scientifically safe

The original lane verdicts are functions of independently computable direct and weighted quantities. No threshold or input depends on the numerical result of the other component. Therefore predeclared direct/weighted decomposition does not change the scientific decision rule provided that:

1. the decomposition is frozen before execution;
2. identical original inputs are used;
3. each scientific lane is reconstructed only after all its required components are present;
4. missing components classify INVALID rather than being silently dropped;
5. no cross-lane selection is allowed.

## Why the split is operationally preferable

Historical Iter053R jobs occupied individual runners for roughly one to one-and-a-half hours. Exposing direct/weighted and C-frame components to Actions-level parallelism can reduce critical-path wall clock substantially when sufficient runners are available, while nested multiprocessing remains sensitive to per-runner CPU allocation.

The execution split is not itself scientific evidence and must never be used to relax convergence thresholds or reinterpret historical Iter053R.

## Current lock

Do not launch this architecture while either active Iter053T companion is non-terminal. It is only an outcome-independent execution blueprint for a possible future prospectively preregistered full corrected replacement.
