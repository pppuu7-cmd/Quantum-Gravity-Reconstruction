#!/usr/bin/env python3
import argparse, itertools, json, math
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
GINV = ETA.copy()
H_CS = 1e-30


def make_q(seed, scale=0.18):
    rng = np.random.default_rng(seed)
    q = rng.normal(size=(4, 4, 4, 4)) * scale
    q = (q + q.swapaxes(0, 1)) / 2
    q = (q + q.swapaxes(2, 3)) / 2
    return q


def riemann_from_q(q):
    R = np.zeros((4, 4, 4, 4), dtype=q.dtype)
    for a, b, c, d in itertools.product(range(4), repeat=4):
        R[a, b, c, d] = 0.5 * (
            q[a, d, b, c] + q[b, c, a, d]
            - q[a, c, b, d] - q[b, d, a, c]
        )
    return R


def ricci_scalar(R, g, gi):
    Ric = np.einsum('ac,abcd->bd', gi, R)
    scal = np.einsum('bd,bd->', gi, Ric)
    return Ric, scal


def weyl(R, g, gi):
    Ric, scal = ricci_scalar(R, g, gi)
    C = np.empty_like(R)
    for a, b, c, d in itertools.product(range(4), repeat=4):
        C[a, b, c, d] = (
            R[a, b, c, d]
            - 0.5 * (
                g[a, c] * Ric[b, d] - g[a, d] * Ric[b, c]
                - g[b, c] * Ric[a, d] + g[b, d] * Ric[a, c]
            )
            + (scal / 6.0) * (g[a, c] * g[b, d] - g[a, d] * g[b, c])
        )
    return C


def i3_complex(R, g, gi):
    C = weyl(R, g, gi)
    Cup = np.einsum('ce,df,abef->abcd', gi, gi, C)
    return np.einsum('abcd,cdef,efab->', Cup, Cup, Cup)


def analytic_direction(R, dR, g, gi):
    C = weyl(R, g, gi)
    dC = weyl(dR, g, gi)
    Cu = np.einsum('ce,df,abef->abcd', gi, gi, C)
    dCu = np.einsum('ce,df,abef->abcd', gi, gi, dC)
    return (
        np.einsum('abcd,cdef,efab->', dCu, Cu, Cu)
        + np.einsum('abcd,cdef,efab->', Cu, dCu, Cu)
        + np.einsum('abcd,cdef,efab->', Cu, Cu, dCu)
    )


def complex_step_gradient(R, g, gi):
    G = np.zeros(R.shape, dtype=float)
    Rc = R.astype(complex)
    for idx in np.ndindex(R.shape):
        X = Rc.copy()
        X[idx] += 1j * H_CS
        G[idx] = float(np.imag(i3_complex(X, g, gi)) / H_CS)
    return G


def alt4(T):
    out = np.zeros_like(T)
    for p in itertools.permutations(range(4)):
        inversions = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        out += (-1.0 if inversions % 2 else 1.0) * T.transpose(p)
    return out / 24.0


def project_algebraic_riemann(G):
    T = 0.25 * (
        G - G.swapaxes(0, 1) - G.swapaxes(2, 3)
        + G.swapaxes(0, 1).swapaxes(2, 3)
    )
    T = 0.5 * (T + T.transpose(2, 3, 0, 1))
    return T - alt4(T)


def algebraic_residual(T):
    cyc = T + T.transpose(0, 2, 3, 1) + T.transpose(0, 3, 1, 2)
    return float(max(
        np.max(np.abs(T + T.swapaxes(0, 1))),
        np.max(np.abs(T + T.swapaxes(2, 3))),
        np.max(np.abs(T - T.transpose(2, 3, 0, 1))),
        np.max(np.abs(cyc)),
    ))


def weyl_trace_residual(C, gi):
    tr = np.einsum('ac,abcd->bd', gi, C)
    return float(np.max(np.abs(tr)))


def conformally_flat_from_ricci(seed):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(4, 4))
    Ric = (X + X.T) / 2
    scal = float(np.einsum('ab,ab->', GINV, Ric))
    R = np.zeros((4, 4, 4, 4))
    for a, b, c, d in itertools.product(range(4), repeat=4):
        R[a, b, c, d] = (
            0.5 * (
                ETA[a, c] * Ric[b, d] - ETA[a, d] * Ric[b, c]
                - ETA[b, c] * Ric[a, d] + ETA[b, d] * Ric[a, c]
            )
            - (scal / 6.0) * (ETA[a, c] * ETA[b, d] - ETA[a, d] * ETA[b, c])
        )
    return R


def boost_x(v):
    ga = 1.0 / math.sqrt(1.0 - v * v)
    A = np.eye(4)
    A[0, 0] = ga
    A[1, 1] = ga
    A[0, 1] = -ga * v
    A[1, 0] = -ga * v
    return A


def rot_yz(th):
    A = np.eye(4)
    c, s = math.cos(th), math.sin(th)
    A[2, 2] = c
    A[2, 3] = -s
    A[3, 2] = s
    A[3, 3] = c
    return A


def transform_cov4(T, A):
    return np.einsum('ia,jb,kc,ld,ijkl->abcd', A, A, A, A, T)


def transform_contra4(T, A):
    Ai = np.linalg.inv(A)
    return np.einsum('ai,bj,ck,dl,ijkl->abcd', Ai, Ai, Ai, Ai, T)


def rel(a, b, floor=1e-14):
    return float(abs(a - b) / max(abs(a), abs(b), floor))


def run(lane):
    seed = 6101 + 131 * lane
    R = riemann_from_q(make_q(seed))
    C = weyl(R, ETA, GINV)
    input_alg = algebraic_residual(R)
    input_trace = weyl_trace_residual(C, GINV)

    I3 = float(np.real(i3_complex(R, ETA, GINV)))
    P = project_algebraic_riemann(complex_step_gradient(R, ETA, GINV))
    p_alg = algebraic_residual(P)
    p_norm = float(np.linalg.norm(P))

    direction_residuals = []
    direction_absolute = []
    for k in range(6):
        dR = riemann_from_q(make_q(seed + 1000 + 53 * k, 0.10))
        reference = float(np.real(analytic_direction(R, dR, ETA, GINV)))
        insertion = float(np.einsum('abcd,abcd->', P, dR))
        direction_absolute.append(float(abs(reference - insertion)))
        if abs(reference) < 1e-8:
            direction_residuals.append(float(abs(reference - insertion)))
        else:
            direction_residuals.append(rel(reference, insertion, 1e-8))

    euler_lhs = float(np.einsum('abcd,abcd->', P, R))
    euler_rhs = 3.0 * I3
    euler_rel = rel(euler_lhs, euler_rhs, 1e-12)

    p_covariance = []
    scalar_covariance = []
    frames = (boost_x(0.27), boost_x(-0.19) @ rot_yz(0.37))
    for A in frames:
        Rt = transform_cov4(R, A)
        gt = A.T @ ETA @ A
        git = np.linalg.inv(gt)
        Pt = project_algebraic_riemann(complex_step_gradient(Rt, gt, git))
        Pexpected = transform_contra4(P, A)
        denom = max(float(np.linalg.norm(Pt)), float(np.linalg.norm(Pexpected)), 1e-14)
        p_covariance.append(float(np.linalg.norm(Pt - Pexpected) / denom))
        scalar_covariance.append(rel(float(np.real(i3_complex(Rt, gt, git))), I3, 1e-14))

    Rcf = conformally_flat_from_ricci(seed + 7777)
    cf_I3 = float(abs(i3_complex(Rcf, ETA, GINV)))
    cf_P = project_algebraic_riemann(complex_step_gradient(Rcf, ETA, GINV))
    cf_P_norm = float(np.linalg.norm(cf_P))

    valid = input_alg <= 1e-11 and input_trace <= 1e-10
    directional_ok = max(direction_residuals) <= 2e-10
    euler_ok = euler_rel <= 2e-10
    p_cov_ok = max(p_covariance) <= 2e-9
    scalar_cov_ok = max(scalar_covariance) <= 1e-10
    p_alg_ok = p_alg <= 2e-11
    null_ok = cf_I3 <= 1e-11 and cf_P_norm <= 2e-10
    nonzero = abs(I3) > 1e-7 and p_norm > 1e-6
    passed = valid and directional_ok and euler_ok and p_cov_ok and scalar_cov_ok and p_alg_ok and null_ok and nonzero

    out = {
        'gate': 'ITER051B1-WEYL3-P-INSERTION-CERTIFICATE',
        'lane': lane,
        'seed': seed,
        'valid': bool(valid),
        'pass': bool(passed),
        'I3': I3,
        'P_norm': p_norm,
        'input_algebraic_residual': input_alg,
        'input_weyl_trace_residual': input_trace,
        'P_algebraic_residual': p_alg,
        'heldout_direction_residuals': direction_residuals,
        'heldout_direction_absolute_errors': direction_absolute,
        'euler_relative_residual': euler_rel,
        'P_covariance_residuals': p_covariance,
        'scalar_covariance_residuals': scalar_covariance,
        'conformally_flat_I3': cf_I3,
        'conformally_flat_P_norm': cf_P_norm,
        'checks': {
            'directional_ok': bool(directional_ok),
            'euler_ok': bool(euler_ok),
            'P_covariance_ok': bool(p_cov_ok),
            'scalar_covariance_ok': bool(scalar_cov_ok),
            'P_algebraic_ok': bool(p_alg_ok),
            'null_ok': bool(null_ok),
            'nonzero_calibration': bool(nonzero),
        },
    }
    print(json.dumps(out, sort_keys=True))
    if not passed:
        raise SystemExit(2)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', type=int, required=True)
    args = ap.parse_args()
    run(args.lane)
