#!/usr/bin/env python3
from __future__ import annotations

import glob
import json
import os
from collections import Counter

GATE = "ITER046-QGR-L1-EXACT-NONLINEAR-PPWAVE-RADIATIVE-SECTOR"
EXPECTED = {"A":12,"B":6,"C":6,"D":6,"E":4}
TOTAL = sum(EXPECTED.values())

files = sorted(glob.glob("iter046-results/**/result.json", recursive=True))
rows = []
for path in files:
    with open(path,"r",encoding="utf-8") as f:
        row = json.load(f)
    if row.get("gate") == GATE:
        rows.append(row)

counts = Counter(r.get("stream") for r in rows)
unique = {(r.get("stream"), r.get("index")) for r in rows}
controls_valid = len(rows) == TOTAL and len(unique) == TOTAL and all(r.get("control_valid") is True for r in rows)
all_pass = controls_valid and all(r.get("lane_pass") is True for r in rows)
stream_full_pass = {
    s: counts.get(s,0) == n and all(r.get("lane_pass") is True for r in rows if r.get("stream") == s)
    for s,n in EXPECTED.items()
}

# A control invalidity has special priority under the frozen preregistration.
b_controls_valid = counts.get("B",0) == EXPECTED["B"] and all(r.get("control_valid") is True for r in rows if r.get("stream") == "B")
if not b_controls_valid:
    classification = "CONTROL_INVALID_NONLINEAR_PPWAVE_GATE"
elif all_pass and all(stream_full_pass.values()):
    classification = "PASS_SCOPED_QGR_L1_EXACT_FINITE_AMPLITUDE_NONLINEAR_PPWAVE_RADIATIVE_SECTOR"
else:
    classification = "PARTIAL_OR_FAIL_QGR_L1_NONLINEAR_PPWAVE_RADIATIVE_SECTOR"

summary = {
    "gate": GATE,
    "classification": classification,
    "expected_scientific_lanes": TOTAL,
    "found_scientific_lanes": len(rows),
    "unique_scientific_lanes": len(unique),
    "passes": sum(bool(r.get("lane_pass")) for r in rows),
    "controls_valid": bool(controls_valid),
    "counts": dict(counts),
    "stream_full_pass": stream_full_pass,
    "A_all_exact_vacuum": all(r.get("einstein_zero_exact") is True for r in rows if r.get("stream") == "A") if counts.get("A",0)==12 else False,
    "A_min_nonzero_riemann_components": min((r.get("riemann_nonzero_components",0) for r in rows if r.get("stream") == "A"), default=0),
    "B_all_nonvacuum_controls_resolved": all(r.get("Guu_minus_half_laplacian_identity_exact") is True and r.get("other_einstein_components_zero_exact") is True for r in rows if r.get("stream") == "B") if counts.get("B",0)==6 else False,
    "C_all_heldout_mixtures_exact_vacuum": all(r.get("einstein_zero_exact") is True for r in rows if r.get("stream") == "C") if counts.get("C",0)==6 else False,
    "D_all_full_riemann_scaling_exact": all(r.get("full_riemann_exact_amplitude_scaling") is True for r in rows if r.get("stream") == "D") if counts.get("D",0)==6 else False,
    "E_all_transformed_charts_exact_vacuum": all(r.get("einstein_zero_exact") is True for r in rows if r.get("stream") == "E") if counts.get("E",0)==4 else False,
    "claim_guard": "special exact nonlinear pp-wave family only; not generic strong-field/nonlinear stability, quantum unitarity, beta/c6 fixing, or experimental confirmation",
}

os.makedirs("iter046-summary", exist_ok=True)
with open("iter046-summary/summary.json","w",encoding="utf-8") as f:
    json.dump(summary,f,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))

# Make aggregate CI reflect frozen terminal gate without hiding partial evidence.
if classification != "PASS_SCOPED_QGR_L1_EXACT_FINITE_AMPLITUDE_NONLINEAR_PPWAVE_RADIATIVE_SECTOR":
    raise SystemExit(1)
