#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import sympy as sp

GATE = "ITER054B-WEYL3-PRINCIPAL-HESSIAN-AND-WELLPOSEDNESS-OBLIGATION"
PASS_CLASS = "PASS_SCOPED_ITER054B_WEYL3_PRINCIPAL_HESSIAN_ACTIVATION_WELLPOSEDNESS_NOT_AUTHORIZED"
PREREG = "019717fad9ad68cc89b5d5cd7dd20c5b3830c882"
N = 6


def tf_sym_matrix(seed, offset=0):
    M = sp.zeros(N)
    for a in range(N):
        for b in range(a, N):
            num = (seed + 2 + offset) * (a + 1) + (seed + 3) * (b + 2) + (a + 1) * (b + 1)
            den = seed + offset + a + b + 7
            v = sp.Rational(num, den)
            M[a, b] = v
            M[b, a] = v
    tr = sp.trace(M) / N
    return sp.simplify(M - tr * sp.eye(N))


def triple(i):
    return tf_sym_matrix(i, 0), tf_sym_matrix(i + 11, 3), tf_sym_matrix(i + 23, 5)


def F(W):
    return sp.expand(sp.trace(W * W * W))


def hessian_target(W, H, K):
    return sp.expand(3 * sp.trace(W * (H * K + K * H)))


def direct_mixed(W, H, K):
    s, t = sp.symbols('s t')
    expr = sp.expand(F(W + s * H + t * K))
    return sp.expand(expr.coeff(s, 1).coeff(t, 1))


def stream_a0():
    W, H, K = triple(0)
    direct = direct_mixed(W, H, K)
    target = hessian_target(W, H, K)
    residual = sp.simplify(direct - target)
    bad = sp.expand(3 * sp.trace(W * H * K))
    bad_residual = sp.simplify(direct - bad)
    ok = residual == 0 and bad_residual != 0 and sp.trace(W) == 0 and sp.trace(H) == 0 and sp.trace(K) == 0
    return {
        "stream": "A0", "gate": GATE, "pass": bool(ok), "controls_valid": True,
        "exact_residual": str(residual), "negative_control_residual": str(bad_residual),
        "direct_ops": int(sp.count_ops(direct)), "target_ops": int(sp.count_ops(target)),
        "interpretation": "exact finite algebraic Hessian identity only"
    }


def stream_a1():
    lam = sp.Rational(7, 5)
    rows = []
    nonzero = 0
    for i in range(12):
        W, H, K = triple(i)
        d = direct_mixed(W, H, K)
        target = hessian_target(W, H, K)
        swapped = hessian_target(W, K, H)
        scaled = hessian_target(lam * W, H, K)
        exact = sp.simplify(d - target) == 0
        sym = sp.simplify(target - swapped) == 0
        scale = sp.simplify(scaled - lam * target) == 0
        nz = sp.simplify(target) != 0
        nonzero += int(nz)
        rows.append({"i": i, "exact": bool(exact), "symmetric": bool(sym), "scaling": bool(scale), "nonzero": bool(nz)})
    ok = all(r["exact"] and r["symmetric"] and r["scaling"] for r in rows) and nonzero >= 10
    return {"stream": "A1", "gate": GATE, "pass": bool(ok), "controls_valid": True,
            "sample_count": 12, "nonzero_count": nonzero, "samples": rows}


def stream_b0():
    null_count = 0
    active_count = 0
    vals = []
    for i in range(12):
        W, H, K = triple(i)
        z = sp.simplify(hessian_target(sp.zeros(N), H, K))
        a = sp.simplify(hessian_target(W, H, K))
        null_count += int(z == 0)
        active_count += int(a != 0)
        vals.append({"i": i, "null_zero": bool(z == 0), "active_nonzero": bool(a != 0)})
    ok = null_count == 12 and active_count >= 10
    return {"stream": "B0", "gate": GATE, "pass": bool(ok), "controls_valid": True,
            "null_zero_count": null_count, "active_nonzero_count": active_count, "samples": vals,
            "interpretation": "background activation of finite algebraic Hessian only"}


def authority_classifier(gauge_fixed_principal_symbol, hyperbolicity_estimate, energy_estimate, constraint_propagation):
    obligations = [gauge_fixed_principal_symbol, hyperbolicity_estimate, energy_estimate, constraint_propagation]
    if not all(obligations):
        return "WELLPOSEDNESS_NOT_AUTHORIZED_FROM_ALGEBRAIC_HESSIAN_ALONE"
    return "PDE_OBLIGATIONS_SYNTHETICALLY_PRESENT_REQUIRES_SEPARATE_SCIENTIFIC_GATE"


def stream_b1():
    actual = authority_classifier(False, False, False, False)
    negative = authority_classifier(True, True, True, True)
    expected = "WELLPOSEDNESS_NOT_AUTHORIZED_FROM_ALGEBRAIC_HESSIAN_ALONE"
    ok = actual == expected and negative != expected
    return {"stream": "B1", "gate": GATE, "pass": bool(ok), "controls_valid": True,
            "actual_classification": actual, "synthetic_all_obligations_control": negative,
            "missing_obligations": ["gauge_fixed_covariant_metric_principal_symbol", "hyperbolicity_estimate", "energy_estimate", "constraint_propagation"],
            "interpretation": "fail-closed authority boundary; no physical mode/ghost claim"}


def run_stream(s):
    return {"A0": stream_a0, "A1": stream_a1, "B0": stream_b0, "B1": stream_b1}[s]()


def aggregate(inp):
    rows, errors = [], []
    for p in sorted(Path(inp).rglob('*.json')):
        try:
            rows.append(json.loads(p.read_text()))
        except Exception as e:
            errors.append(f"{p}:{e}")
    by = {r.get('stream'): r for r in rows if r.get('stream') in {'A0','A1','B0','B1'}}
    missing = sorted({'A0','A1','B0','B1'} - set(by))
    allpass = not missing and not errors and all(by[s].get('pass') is True and by[s].get('controls_valid') is True for s in ['A0','A1','B0','B1'])
    return {
        "gate": GATE,
        "classification": PASS_CLASS if allpass else "SCIENTIFIC_FAIL_OR_INVALID_ITER054B",
        "pass": allpass,
        "found_streams": sorted(by),
        "missing": missing,
        "parse_errors": errors,
        "stream_pass": {s: by[s].get('pass') for s in by},
        "preregistration_commit": PREREG,
        "interpretation_lock": "FINITE ALGEBRAIC WEYL3 HESSIAN ACTIVATION ONLY; GAUGE-FIXED COVARIANT METRIC PRINCIPAL SYMBOL AND WELL-POSEDNESS NOT ESTABLISHED; NO PHYSICAL MODE/GHOST/STABILITY CLAIM; C6 UNFIXED; THEORY_ESTABLISHED_0"
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stream', choices=['A0','A1','B0','B1'])
    ap.add_argument('--aggregate')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    data = aggregate(a.aggregate) if a.aggregate else run_stream(a.stream)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(data, indent=2, sort_keys=True))
    print(json.dumps(data, sort_keys=True))
    if not data.get('pass', False):
        raise SystemExit(2)

if __name__ == '__main__':
    main()
