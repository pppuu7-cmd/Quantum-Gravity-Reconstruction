#!/usr/bin/env python3
"""Iter044: end-to-end QGR-L1 linearized radiative dynamics gate.

Reconstructs QGR-L1 from its exact S4/Noether quadratic family, then tests
QGR dynamics -> TT radiative curvature, off-shell dispersion, gauge robustness,
and flat-background decoupling of the unfixed c6*Weyl^3 operator.
"""
from __future__ import annotations

import argparse
import collections
import itertools
import json
import math
import os
from fractions import Fraction

import numpy as np

V = range(4)
PERMS = list(itertools.permutations(V))
FIELDS = [(i, j) for i in V for j in range(i, 4)]
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
C = np.ones((4, 4), float) - np.eye(4)
E = np.linalg.inv(C)
AAMP = 0.013
K = 1.7
PSIS = [0.0, math.pi / 8, math.pi / 4, 3 * math.pi / 8]
PHIS = [0.23, 1.07]
DIRECTIONS = [np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0])]

# Deterministic incidence -> orthonormal chart frozen in ITERATION_044.md.
_t = np.array([1.0, 1.0, 1.0, 1.0]) / 2.0
_s1 = np.array([1.0, -1.0, 0.0, 0.0]) / math.sqrt(2.0)
_s2 = np.array([1.0, 1.0, -2.0, 0.0]) / math.sqrt(6.0)
_s3 = np.array([1.0, 1.0, 1.0, -3.0]) / math.sqrt(12.0)
O = np.column_stack([_t, _s1, _s2, _s3])
AMAP = np.diag([math.sqrt(3.0), 1.0, 1.0, 1.0]) @ O.T
AINV = np.linalg.inv(AMAP)


def rref(rows, ncols):
    a = [[Fraction(x) for x in row] for row in rows if any(row)]
    pivots = []
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [a[i][j] - f * a[r][j] for j in range(ncols)]
        pivots.append(c)
        r += 1
    return a, pivots


def nullspace_q(rows, ncols):
    a, pivots = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0) for _ in range(ncols)]
        v[f] = 1
        for ri, p in enumerate(pivots):
            v[p] = -a[ri][f]
        basis.append(v)
    return basis


def exp2(i, j):
    e = [0, 0, 0, 0]
    e[i] += 1
    e[j] += 1
    return tuple(e)


def exp_plus(e, i):
    z = list(e)
    z[i] += 1
    return tuple(z)


def build_orbits(fields):
    findex = {f: i for i, f in enumerate(fields)}
    field_pairs = [(a, b) for a in range(len(fields)) for b in range(a, len(fields))]
    mom_pairs = [(i, j) for i in V for j in range(i, 4)]
    terms = [(a, b, i, j) for a, b in field_pairs for i, j in mom_pairs]

    def pfield(f, p):
        return tuple(sorted((p[f[0]], p[f[1]])))

    def pterm(t, p):
        a, b, i, j = t
        na = findex[pfield(fields[a], p)]
        nb = findex[pfield(fields[b], p)]
        if na > nb:
            na, nb = nb, na
        ni, nj = sorted((p[i], p[j]))
        return na, nb, ni, nj

    unseen = set(terms)
    orbits = []
    while unseen:
        x = min(unseen)
        orb = {pterm(x, p) for p in PERMS}
        orbits.append(orb)
        unseen -= orb
    return orbits


def derivative_R(fields):
    out = {}
    for a, (i, j) in enumerate(fields):
        out[a] = [(i, i, 2)] if i == j else [(j, i, 1), (i, j, 1)]
    return out


def rows_HR(fields, orbits, R):
    n = len(orbits)
    eq = collections.defaultdict(lambda: [0] * n)
    for oi, orb in enumerate(orbits):
        for a, b, i, j in orb:
            e = exp2(i, j)
            for g, v, c in R[b]:
                eq[(a, g, exp_plus(e, v))][oi] += c
            if a != b:
                for g, v, c in R[a]:
                    eq[(b, g, exp_plus(e, v))][oi] += c
    return list(eq.values())


ORBITS = build_orbits(FIELDS)
_BASIS = nullspace_q(rows_HR(FIELDS, ORBITS, derivative_R(FIELDS)), len(ORBITS))
assert len(ORBITS) == 38 and len(_BASIS) == 2
SELECTED = [_BASIS[0][i] + Fraction(1, 2) * _BASIS[1][i] for i in range(len(ORBITS))]


def hessian(k):
    H = np.zeros((10, 10), float)
    for oi, orb in enumerate(ORBITS):
        c = float(SELECTED[oi])
        if c == 0.0:
            continue
        for a, b, i, j in orb:
            val = c * float(k[i]) * float(k[j])
            H[a, b] += val
            if a != b:
                H[b, a] += val
    return H


def relative_rank(M, rtol=1e-10):
    s = np.linalg.svd(M, compute_uv=False)
    if not len(s) or s[0] == 0:
        return 0
    return int(np.count_nonzero(s > rtol * s[0]))


def vecsym(M):
    return np.array([M[i, j] for i, j in FIELDS], float)


def gauge_matrix(k):
    cols = []
    for a in range(4):
        xi = np.zeros(4)
        xi[a] = 1.0
        cols.append(vecsym(np.outer(k, xi) + np.outer(xi, k)))
    return np.column_stack(cols)


def normalized_h_residual(H, v):
    den = float(np.linalg.norm(H) * np.linalg.norm(v))
    return float(np.linalg.norm(H @ v) / max(den, 1e-30))


def transverse_basis(n):
    refs = [np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, 1.0])]
    ref = min(refs, key=lambda r: abs(float(np.dot(n, r))))
    u = np.cross(n, ref)
    u = u / np.linalg.norm(u)
    v = np.cross(n, u)
    v = v / np.linalg.norm(v)
    return u, v


def polarization(n, psi):
    u, v = transverse_basis(n)
    ep = np.outer(u, u) - np.outer(v, v)
    ex = np.outer(u, v) + np.outer(v, u)
    return math.cos(psi) * ep + math.sin(psi) * ex


def minkowski_h(n, psi, phase=None):
    P = np.zeros((4, 4), float)
    P[1:, 1:] = polarization(n, psi)
    amp = AAMP if phase is None else AAMP * math.cos(phase)
    return amp * P


def linearized_riemann(h, k):
    # Fourier/plane-wave second derivative d_mu d_nu h_ab = -k_mu k_nu h_ab.
    R = np.zeros((4, 4, 4, 4), float)
    def d2(mu, nu, a, b):
        return -k[mu] * k[nu] * h[a, b]
    for a, b, c, d in itertools.product(range(4), repeat=4):
        R[a, b, c, d] = 0.5 * (
            d2(c, b, a, d) + d2(d, a, b, c)
            - d2(d, b, a, c) - d2(c, a, b, d)
        )
    return R


def transform_cov4(R, A):
    return np.einsum('ma,nb,pc,qd,abcd->mnpq', A, A, A, A, R)


def chart_errors():
    e1 = float(np.linalg.norm(AMAP.T @ ETA @ AMAP - C))
    e2 = float(np.linalg.norm(AMAP @ E @ AMAP.T - ETA))
    return e1, e2


def stream_a(index):
    di = index // 8
    rem = index % 8
    pi = rem // 2
    fi = rem % 2
    n, psi, phi = DIRECTIONS[di], PSIS[pi], PHIS[fi]
    p = K * np.concatenate(([1.0], -n))
    k = np.linalg.solve(AMAP, p)
    hm = minkowski_h(n, psi, phi)
    hi = AINV @ hm @ AINV.T
    H = hessian(k)
    G = gauge_matrix(k)
    rank_h = relative_rank(H)
    rank_g = relative_rank(G)
    tt_res = normalized_h_residual(H, vecsym(hi))
    gauge_res = [normalized_h_residual(H, G[:, j]) for j in range(4)]
    Ri = linearized_riemann(hi, k)
    Rm_from_qgr = transform_cov4(Ri, AMAP)
    Rm_direct = linearized_riemann(hm, p)
    rn = float(np.linalg.norm(Rm_direct))
    bridge = float(np.linalg.norm(Rm_from_qgr - Rm_direct) / max(rn, 1e-30))
    pnull = abs(float(p @ ETA @ p))
    knull = abs(float(k @ C @ k))
    ce1, ce2 = chart_errors()
    control = ce1 < 1e-12 and ce2 < 1e-12 and rn > 1e-10
    science = (
        pnull < 1e-12 and knull < 1e-12 and rank_h == 4 and rank_g == 4
        and max(gauge_res) < 1e-10 and tt_res < 1e-10 and bridge < 1e-10
    )
    return {
        'gate': 'ITER044-QGR-L1-END-TO-END-LINEARIZED-TT-RADIATION', 'stream': 'A', 'index': index,
        'direction': n.tolist(), 'psi': psi, 'phi': phi, 'p_null': pnull, 'k_null': knull,
        'hessian_rank': rank_h, 'gauge_rank': rank_g, 'tt_qgr_residual': tt_res,
        'max_gauge_qgr_residual': max(gauge_res), 'curvature_bridge_error': bridge,
        'direct_curvature_norm': rn, 'chart_C_error': ce1, 'chart_E_error': ce2,
        'control_valid': bool(control), 'lane_pass': bool(control and science),
    }


def stream_b(index):
    di = index // 4
    pi = index % 4
    n, psi = DIRECTIONS[di], PSIS[pi]
    ratios = [0.8, 0.9, 1.0, 1.1, 1.2]
    rows = []
    hm = minkowski_h(n, psi)
    hi = AINV @ hm @ AINV.T
    for r in ratios:
        p = K * np.concatenate(([1.0], -r * n))
        k = np.linalg.solve(AMAP, p)
        H = hessian(k)
        rows.append({
            'ratio': r,
            'rank': relative_rank(H),
            'residual': normalized_h_residual(H, vecsym(hi)),
            'characteristic_abs': abs(float(k @ C @ k)),
            'minkowski_shell_abs': abs(float(p @ ETA @ p)),
        })
    center = rows[2]
    off = rows[:2] + rows[3:]
    residuals = [x['residual'] for x in rows]
    unique_min = int(np.argmin(residuals)) == 2 and residuals[2] < min(residuals[:2] + residuals[3:])
    control = all(np.isfinite(x['residual']) and np.isfinite(x['characteristic_abs']) for x in rows)
    science = (
        center['rank'] == 4 and center['residual'] < 1e-10 and center['characteristic_abs'] < 1e-12
        and all(x['rank'] == 6 and x['residual'] > 1e-3 and x['characteristic_abs'] > 1e-3 for x in off)
        and unique_min
    )
    return {
        'gate': 'ITER044-QGR-L1-END-TO-END-LINEARIZED-TT-RADIATION', 'stream': 'B', 'index': index,
        'direction': n.tolist(), 'psi': psi, 'samples': rows, 'unique_null_residual_minimum': bool(unique_min),
        'minimum_offshell_residual': min(x['residual'] for x in off),
        'control_valid': bool(control), 'lane_pass': bool(control and science),
    }


C_SPECS = [
    (0, 0, 0), (0, 2, 1), (1, 1, 0), (1, 3, 1),
    (2, 0, 1), (2, 2, 0), (0, 3, 0), (2, 1, 1),
]
XI_RAW = [
    [1, 2, -1, 1], [2, -1, 1, 3], [-1, 1, 2, 1], [3, 1, -2, 1],
    [1, -3, 1, 2], [2, 1, 3, -1], [-2, 2, 1, 1], [1, 1, -2, 3],
]


def stream_c(index):
    di, pi, fi = C_SPECS[index]
    n, psi, phi = DIRECTIONS[di], PSIS[pi], PHIS[fi]
    p = K * np.concatenate(([1.0], -n))
    k = np.linalg.solve(AMAP, p)
    hm = minkowski_h(n, psi, phi)
    hi = AINV @ hm @ AINV.T
    xi = np.array(XI_RAW[index], float)
    xi /= np.linalg.norm(xi)
    g = np.outer(k, xi) + np.outer(xi, k)
    H = hessian(k)
    vg = vecsym(g)
    pure_res = normalized_h_residual(H, vg)
    shifted_res = normalized_h_residual(H, vecsym(hi + g))
    Rphys = transform_cov4(linearized_riemann(hi, k), AMAP)
    Rg = transform_cov4(linearized_riemann(g, k), AMAP)
    Rshift = transform_cov4(linearized_riemann(hi + g, k), AMAP)
    scale = max(float(np.linalg.norm(Rphys)), 1e-30)
    pure_curv = float(np.linalg.norm(Rg) / scale)
    shifted_curv = float(np.linalg.norm(Rshift - Rphys) / scale)
    control = np.linalg.norm(vg) > 1e-8 and scale > 1e-10 and relative_rank(gauge_matrix(k)) == 4
    science = pure_res < 1e-10 and shifted_res < 1e-10 and pure_curv < 1e-10 and shifted_curv < 1e-10
    return {
        'gate': 'ITER044-QGR-L1-END-TO-END-LINEARIZED-TT-RADIATION', 'stream': 'C', 'index': index,
        'direction': n.tolist(), 'psi': psi, 'phi': phi, 'xi': xi.tolist(),
        'pure_gauge_qgr_residual': pure_res, 'shifted_qgr_residual': shifted_res,
        'pure_gauge_curvature_ratio': pure_curv, 'shifted_curvature_error': shifted_curv,
        'control_valid': bool(control), 'lane_pass': bool(control and science),
    }


def ricci_scalar(R):
    Ric = np.zeros((4, 4), float)
    for b in range(4):
        for d in range(4):
            Ric[b, d] = sum(ETA[a, a] * R[a, b, a, d] for a in range(4))
    scalar = sum(ETA[b, b] * Ric[b, b] for b in range(4))
    return Ric, float(scalar)


def weyl(R):
    Ric, scalar = ricci_scalar(R)
    W = np.zeros_like(R)
    g = ETA
    for a, b, c, d in itertools.product(range(4), repeat=4):
        W[a, b, c, d] = (
            R[a, b, c, d]
            - 0.5 * (g[a, c] * Ric[d, b] - g[a, d] * Ric[c, b] - g[b, c] * Ric[d, a] + g[b, d] * Ric[c, a])
            + (scalar / 6.0) * (g[a, c] * g[d, b] - g[a, d] * g[c, b])
        )
    return W


def weyl_cubic(W):
    Cup = np.zeros_like(W)
    for a, b, c, d in itertools.product(range(4), repeat=4):
        Cup[a, b, c, d] = ETA[c, c] * ETA[d, d] * W[a, b, c, d]
    return float(np.einsum('abcd,cdef,efab', Cup, Cup, Cup))


D_WITNESSES = [
    ([1.3, -0.4, 0.7, 0.2], [[0.2,0.1,-0.03,0.07],[0.1,0.5,0.11,-0.08],[-0.03,0.11,-0.4,0.06],[0.07,-0.08,0.06,0.3]]),
    ([0.9,0.6,-0.2,0.5], [[0.1,-0.12,0.08,0.02],[-0.12,-0.3,0.07,0.09],[0.08,0.07,0.45,-0.05],[0.02,0.09,-0.05,0.22]]),
    ([1.1,0.2,0.8,-0.3], [[-0.15,0.04,0.13,-0.06],[0.04,0.32,-0.09,0.05],[0.13,-0.09,0.18,0.12],[-0.06,0.05,0.12,-0.28]]),
    ([0.7,-0.5,0.4,0.9], [[0.05,0.09,-0.11,0.03],[0.09,0.27,0.02,-0.14],[-0.11,0.02,-0.31,0.08],[0.03,-0.14,0.08,0.19]]),
]


def stream_d(index):
    p0, h0 = D_WITNESSES[index]
    p = np.array(p0, float)
    h = np.array(h0, float)
    eps = [-2.0, -1.0, 0.0, 1.0, 2.0]
    vals = {}
    norms = {}
    for e in eps:
        W = weyl(linearized_riemann(e * h, p))
        vals[str(int(e))] = weyl_cubic(W)
        norms[str(int(e))] = float(np.linalg.norm(W))
    mag = max(abs(x) for x in vals.values())
    odd1 = abs(vals['1'] + vals['-1']) / max(mag, 1e-30)
    odd2 = abs(vals['2'] + vals['-2']) / max(mag, 1e-30)
    ratio = vals['2'] / vals['1'] if abs(vals['1']) > 1e-30 else float('nan')
    second1 = abs(vals['1'] + vals['-1'] - 2 * vals['0']) / max(mag, 1e-30)
    second2 = abs(vals['2'] + vals['-2'] - 2 * vals['0']) / (4.0 * max(mag, 1e-30))
    control = abs(vals['1']) > 1e-10 and norms['1'] > 1e-8 and all(np.isfinite(x) for x in vals.values())
    science = (
        abs(vals['0']) < 1e-14 and odd1 < 1e-12 and odd2 < 1e-12
        and abs(ratio - 8.0) / 8.0 < 1e-10 and second1 < 1e-12 and second2 < 1e-12
    )
    return {
        'gate': 'ITER044-QGR-L1-END-TO-END-LINEARIZED-TT-RADIATION', 'stream': 'D', 'index': index,
        'w3_by_epsilon': vals, 'weyl_norm_by_epsilon': norms, 'oddness_e1': odd1, 'oddness_e2': odd2,
        'cubic_ratio_2_over_1': ratio, 'centered_second_variation_e1': second1,
        'centered_second_variation_e2': second2,
        'interpretation': 'c6 multiplies a cubic-curvature operator whose flat-background quadratic Hessian vanishes; c6 remains unfixed',
        'control_valid': bool(control), 'lane_pass': bool(control and science),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stream', choices=['A', 'B', 'C', 'D'], required=True)
    ap.add_argument('--index', type=int, required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    limits = {'A': 24, 'B': 12, 'C': 8, 'D': 4}
    assert 0 <= a.index < limits[a.stream]
    fn = {'A': stream_a, 'B': stream_b, 'C': stream_c, 'D': stream_d}[a.stream]
    out = fn(a.index)
    out['classification'] = f"ITER044_{a.stream}_LANE_PASS" if out['lane_pass'] else (f"ITER044_{a.stream}_CONTROL_INVALID" if not out['control_valid'] else f"ITER044_{a.stream}_SCIENTIFIC_FAIL")
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w', encoding='utf-8') as f:
        json.dump(out, f, sort_keys=True, allow_nan=False)
    print(json.dumps(out, sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()
