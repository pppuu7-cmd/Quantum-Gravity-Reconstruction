# Iter057AR target-blind execution repair

Date: 2026-09-17

Status before repair: `BLOCKED_ITER057AR_PRIMARY_CORRECTED_SOURCE_ARTIFACT_NOT_REALIZED`.

The authoritative blocked run `35183877598` is immutable evidence. Its raw job log shows the constructor terminated before producing `primary.json` because the runner environment lacked the imported dependency `sympy` (`ModuleNotFoundError: No module named 'sympy'`). The workflow nevertheless concluded success because the constructor command was piped through `tee` without `pipefail`.

This repair is execution-only and target-blind. Before any repaired target comparison, freeze the following changes and only these changes:

1. install `sympy` in the production Python environment before invoking the existing constructor;
2. execute the constructor under `set -o pipefail` so a constructor failure cannot be masked by `tee`;
3. assert that `artifacts/iter057ar/primary.json` exists and is non-empty before the digest/upload stage.

Frozen scientific object and criteria are unchanged: Iter057W geometry, exact Frechet constructor, 2100-slot basis/order, exact arithmetic, `c6=SYMBOLIC_UNFIXED`, normalization, acceptance criteria, independent-reproduction firewall, and historical coefficients/targets. No historical target vector or coefficient is read or changed by this repair.

A repaired workflow success is not by itself scientific PASS. Raw constructor output, `primary.json`, manifest digest, frozen controls, and subsequently the independent reproduction required by the original Iter057AR preregistration must still be consumed.