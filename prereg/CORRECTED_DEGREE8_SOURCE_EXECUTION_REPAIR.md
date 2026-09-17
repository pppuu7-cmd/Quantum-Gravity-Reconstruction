# Corrected degree-eight source — execution-only dependency/pipefail repair

Status: **PROSPECTIVELY PREREGISTERED / NOT YET PRODUCED**  
Date: 2026-09-17

Parent science preregistration: `ddf4d41be23b09e5a4709149d85d85688a533fab`.
Parent blocked run: `35268178559`.
Durable blocked result: `9a6361886a35c86159c8d80d073573dfefc5a710`.

## Causal execution defect

All corrected/historical computation lanes failed before scientific computation because the workflow omitted `sympy`, required by the frozen Iter057Z/AA seed module. The Python failure was masked by `tee` because the shell did not enable `pipefail`.

## Sole authorized changes

1. add `actions/setup-python@v5` with Python 3.11 and install `sympy==1.14.0` in primary, independent and historical comparator lanes;
2. run each computational shell with `set -euo pipefail`.

Everything else remains byte/semantically frozen from the parent science gate: seed, corrected Frechet constructor, primary and independent source assemblies, AT degree-six exact reduction, `-Edown` historical comparison sign, isolated Iter057AA replay, allowed classifications, terminal classifier, `c6` and claim ceiling.

The blocked run cannot be reclassified. One fresh repaired production run is required.

`c6 = SYMBOLIC_UNFIXED`.
`theory_established = 0`.
