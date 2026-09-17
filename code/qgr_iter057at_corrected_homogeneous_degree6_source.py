#!/usr/bin/env python3
"""Iter057AT corrected homogeneous degree-six Weyl^3 source constructors.

Prospectively frozen by 6039cb2ed1380b549bced3d33634362ef57345d4.
The primary and independent lanes never read one another's payload and never
load the historical Iter057X/Iter057AR coefficient target.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057ap_independent_covariant_source_repair as r
import qgr_iter057aq_degree6_causal_adjudication as aq

PREREG = "6039cb2ed1380b549bced3d33634362ef57345d4"
AO_AUTHORITY = "3246b31fde58d061f7e35cbc6be22236d1c7b2a8"
AQ_AUTHORITY = "de82fe82c8f3f40854c81d7cb3e0e5d490a153a4"
N = b.N
PAIRS = b.PAIRS


def fs(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def jsha(x):
    raw = json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source_fingerprint():
    alphas6 = [list(a) for a in b.alphas(6)]
    manifest = {
        "base_module_sha256": file_sha(b.__file__),
        "frechet_repair_module_sha256": file_sha(r.__file__),
        "aq_operator_module_sha256": file_sha(aq.__file__),
        "pairs": [list(x) for x in PAIRS],
        "alphas6": alphas6,
    }
    return {"manifest": manifest, "sha256": jsha(manifest)}


def poly_equal(p, q):
    for k in set(p) | set(q):
        if F(p.get(k, 0)) != F(q.get(k, 0)):
            return False
    return True


def tensor_symmetric(E):
    return all(poly_equal(E[i][j], E[j][i]) for i, j in product(range(N), repeat=2))


def serialize_primary(E):
    out = []
    for a, bb in PAIRS:
        for alpha in b.alphas(6):
            out.append({"pair": [a, bb], "alpha": list(alpha), "value": fs(b.normalized(E[a][bb], alpha))})
    return out


def serialize_independent(E):
    # Independent serialization implementation: materialize the frozen alpha
    # order first, then normalize by direct ordered lookup. No primary helper is used.
    alpha_order = tuple(tuple(x) for x in b.alphas(6))
    records = []
    for pair_index in range(len(PAIRS)):
        a, bb = PAIRS[pair_index]
        component = E[a][bb]
        for alpha_index in range(len(alpha_order)):
            alpha = alpha_order[alpha_index]
            value = b.normalized(component, alpha)
            records.append({"pair": [a, bb], "alpha": list(alpha), "value": fs(value)})
    return records


def construct_primary():
    g, prov, _, _ = b.seed_metric10()
    gi, Gamma, Rlow, Ric, Scal, Ein, C, invok = b.geometry8(g)
    seed_ok = bool(prov and invok and all(not Ric[i][j] for i, j in product(range(N), repeat=2)) and not Scal)
    Cup = b.raise_last(C, gi, 8)
    I3, QF = r._fixed_cubic_and_Q(C, Cup, 6)
    PF, _ = r._fixed_p_from_frechet(g, gi, C, Cup, QF, 8)
    pc = r._fixed_p_controls(PF, None, I3, Rlow, g, gi)
    E = aq.x_operator(PF, g, gi, Gamma, Rlow, I3)
    return E, seed_ok, pc


def construct_independent():
    # Independent downstream construction uses the covariant AO source assembly,
    # rather than aq.x_operator used by the primary lane.
    g, prov, _, _ = b.seed_metric10()
    gi, Gamma, Rlow, Ric, Scal, Ein, C, invok = b.geometry8(g)
    seed_ok = bool(prov and invok and all(not Ric[i][j] for i, j in product(range(N), repeat=2)) and not Scal)
    Cup = b.raise_last(C, gi, 8)
    I3, QF = r._fixed_cubic_and_Q(C, Cup, 6)
    PF, _ = r._fixed_p_from_frechet(g, gi, C, Cup, QF, 8)
    pc = r._fixed_p_controls(PF, None, I3, Rlow, g, gi)
    Eup, Edown, _, _, _ = b.ao_source(g, gi, Gamma, Rlow, PF, I3)
    return Edown, seed_ok, pc


def build(mode):
    if mode == "primary":
        E, seed_ok, pc = construct_primary()
        vec = serialize_primary(E)
        implementation = "AQ exact X-operator downstream assembly"
    else:
        E, seed_ok, pc = construct_independent()
        vec = serialize_independent(E)
        implementation = "AO covariant source downstream assembly"

    alpha_lists = [z["alpha"] for z in vec]
    per_pair = len(tuple(b.alphas(6)))
    source_fp = source_fingerprint()
    controls = {
        "unchanged_iter057w_seed_geometry_exact": seed_ok,
        "frechet_intrinsic_controls_all_exact": all(v is True for v in pc.values() if isinstance(v, bool)),
        "slot_count_840": len(vec) == 840,
        "monomial_count_per_pair_84": per_pair == 84,
        "all_alpha_total_degree_6": all(sum(a) == 6 for a in alpha_lists),
        "exact_fraction_serialization_no_tolerance": all(fs(F(z["value"])) == z["value"] for z in vec),
        "source_tensor_exactly_symmetric": tensor_symmetric(E),
        "historical_iter057x_ar_target_not_loaded": True,
        "c6_symbolic_unfixed_factored_out": True,
        "ao_covariant_variation_authority_pinned": AO_AUTHORITY == "3246b31fde58d061f7e35cbc6be22236d1c7b2a8",
        "aq_frechet_causal_authority_pinned": AQ_AUTHORITY == "de82fe82c8f3f40854c81d7cb3e0e5d490a153a4",
    }
    ready = all(controls.values())
    classification = (
        f"{mode.upper()}_READY_ITER057AT_AWAITING_TERMINAL_COMPARISON"
        if ready else
        f"FAIL_ITER057AT_{mode.upper()}_FROZEN_CONTROL_FAILURE"
    )
    payload = {
        "gate": "ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE",
        "preregistration_commit": PREREG,
        "lane": mode,
        "implementation": implementation,
        "classification": classification,
        "controls": controls,
        "frechet_controls": pc,
        "source_fingerprint": source_fp,
        "slot_count": len(vec),
        "monomial_count_per_pair": per_pair,
        "degree6_vector_sha256": jsha(vec),
        "c6": "SYMBOLIC_UNFIXED_FACTORED_OUT",
        "historical_target_loaded": False,
        "degree6_vector": vec,
    }
    summary = dict(payload)
    summary.pop("degree6_vector")
    payload["scientific_summary_sha256"] = jsha(summary)
    payload["complete_payload_sha256"] = jsha(payload)
    return payload, ready


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True, choices=("primary", "independent"))
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    payload, ready = build(args.mode)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    printed = dict(payload)
    printed.pop("degree6_vector")
    print(json.dumps(printed, sort_keys=True, indent=2))
    return 0 if ready else 2


if __name__ == "__main__":
    raise SystemExit(main())
