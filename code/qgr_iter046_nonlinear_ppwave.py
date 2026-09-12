#!/usr/bin/env python3
"""Iter046: exact nonlinear pp-wave sector of the all-orders two-derivative QGR-L1 action.

The frozen QGR authority is S_local = a int sqrt(|det G|) R[G].  This code
constructs the metric geometry directly and evaluates its Euler-Lagrange tensor
(up to the irrelevant common nonzero factor a): the Einstein tensor obtained by
variation of that already-reconstructed action.  It does not insert a pp-wave
field equation as the solver.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os

import numpy as np
import sympy as sp

u, v, x, y = sp.symbols("u v x y", real=True)
COORDS = (u, v, x, y)
N = 4
R = sp.Rational

P2 = x**2 - y**2
X2 = 2*x*y
P3 = x**3 - 3*x*y**2
P4 = x**4 - 6*x**2*y**2 + y**4
BASES = [P2, X2, P3, P4]
FPROF = [
    sp.Integer(1),
    1 + u,
    1 + u + u**2/R(3),
    1 - u/R(2) + u**3/R(5),
]
AMPS = [R(1,20), R(1,10), R(1,5), R(1,2), R(3,4)]
POINT = {u:R(1,7), v:0, x:R(2,5), y:R(-1,3)}

A_SPECS = [
    (0,0,0),(1,1,1),(2,2,2),(3,3,3),
    (0,2,4),(1,3,0),(2,0,3),(3,1,2),
    (0,3,1),(1,2,4),(2,1,0),(3,0,4),
]
B_SPECS = [
    (0,0,R(0)),(1,1,R(1,3)),(2,2,R(-2,5)),
    (3,3,R(3,7)),(1,4,R(-1,2)),(2,0,R(2,3)),
]
LAMBDAS = [R(0), R(1,2), R(-2,3), R(1), R(3,2), R(-1,3)]
C_SPECS = [
    (0,2),(1,4),(2,1),(3,3),(1,0),(2,4),
]
D_SPECS = [
    (0,R(1,20),R(1,10)),
    (1,R(1,10),R(1,2)),
    (2,R(1,20),R(3,4)),
    (3,R(1,5),R(1,2)),
    (1,R(1,20),R(1,5)),
    (2,R(1,10),R(3,4)),
]

# Frozen invertible constant coordinate maps old_q = M new_q.
E_MATRICES = [
    sp.Matrix([[1,0,0,0],[R(1,5),1,R(1,7),0],[0,0,1,R(1,9)],[0,0,0,1]]),
    sp.Matrix([[1,0,R(1,8),0],[0,1,0,R(-1,6)],[0,0,1,0],[0,0,R(1,10),1]]),
    sp.Matrix([[1,R(1,11),0,0],[0,1,R(1,9),0],[0,0,1,R(-1,8)],[0,0,0,1]]),
    sp.Matrix([[R(6,5),0,0,0],[R(-1,7),R(5,6),0,0],[0,R(1,12),R(7,6),0],[0,0,R(-1,10),R(9,8)]]),
]
E_SPECS = [
    (0,1,1),(1,2,2),(2,3,0),(3,0,4),
]


def simp(z):
    return sp.simplify(sp.cancel(z))


def pp_metric(H):
    return sp.Matrix([
        [H, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])


def geometry(g, coords):
    """Direct metric geometry: inverse, Gamma, mixed Riemann, Ricci, scalar, Einstein."""
    gi = g.inv().applyfunc(simp)
    Gamma = [[[sp.Integer(0) for _ in range(N)] for __ in range(N)] for ___ in range(N)]
    for r,a,b in itertools.product(range(N), repeat=3):
        Gamma[r][a][b] = simp(R(1,2)*sum(
            gi[r,s]*(sp.diff(g[s,b],coords[a]) + sp.diff(g[s,a],coords[b]) - sp.diff(g[a,b],coords[s]))
            for s in range(N)
        ))

    Rm = [[[[sp.Integer(0) for _ in range(N)] for __ in range(N)] for ___ in range(N)] for ____ in range(N)]
    for r,s,a,b in itertools.product(range(N), repeat=4):
        Rm[r][s][a][b] = simp(
            sp.diff(Gamma[r][s][b], coords[a]) - sp.diff(Gamma[r][s][a], coords[b])
            + sum(Gamma[r][a][l]*Gamma[l][s][b] - Gamma[r][b][l]*Gamma[l][s][a] for l in range(N))
        )

    Ric = sp.MutableDenseMatrix(N,N,[0]*(N*N))
    for s,b in itertools.product(range(N), repeat=2):
        Ric[s,b] = simp(sum(Rm[r][s][r][b] for r in range(N)))
    Rsc = simp(sum(gi[a,b]*Ric[a,b] for a,b in itertools.product(range(N), repeat=2)))
    Ein = (Ric - R(1,2)*g*Rsc).applyfunc(simp)
    return gi, Gamma, Rm, Ric, Rsc, Ein


def matrix_zero(M):
    return all(simp(M[i,j]) == 0 for i,j in itertools.product(range(M.rows), range(M.cols)))


def riemann_nonzero_count(Rm):
    return sum(simp(Rm[a][b][c][d]) != 0 for a,b,c,d in itertools.product(range(N), repeat=4))


def lorentzian_inertia_at(g, point):
    M = np.array(g.subs(point).evalf(), dtype=float)
    vals = np.linalg.eigvalsh(M)
    pos = int(np.count_nonzero(vals > 1e-10))
    neg = int(np.count_nonzero(vals < -1e-10))
    zero = int(len(vals) - pos - neg)
    return [pos, neg, zero], [float(z) for z in vals]


def stream_a(index):
    bi, fi, ai = A_SPECS[index]
    H = AMPS[ai]*FPROF[fi]*BASES[bi]
    g = pp_metric(H)
    _,_,Rm,_,_,Ein = geometry(g, COORDS)
    detg = simp(g.det())
    inertia, eig = lorentzian_inertia_at(g, POINT)
    nz = riemann_nonzero_count(Rm)
    control = detg != 0 and inertia == [3,1,0]
    science = matrix_zero(Ein) and nz > 0
    return {
        "gate":"ITER046-QGR-L1-EXACT-NONLINEAR-PPWAVE-RADIATIVE-SECTOR",
        "stream":"A","index":index,"basis":bi,"f_profile":fi,"amplitude":str(AMPS[ai]),
        "metric_det":str(detg),"inertia":inertia,"eigenvalues":eig,
        "einstein_zero_exact":matrix_zero(Ein),"riemann_nonzero_components":nz,
        "control_valid":bool(control),"lane_pass":bool(control and science),
    }


def stream_b(index):
    fi, ai, hm = B_SPECS[index]
    H = AMPS[ai]*FPROF[fi]*((x**2+y**2) + hm*P2)
    g = pp_metric(H)
    _,_,Rm,_,_,Ein = geometry(g, COORDS)
    lap = simp(sp.diff(H,x,2)+sp.diff(H,y,2))
    guu = simp(Ein[0,0])
    others_zero = all(simp(Ein[i,j]) == 0 for i,j in itertools.product(range(N),repeat=2) if (i,j)!=(0,0))
    identity = simp(guu + R(1,2)*lap) == 0
    control = lap != 0 and guu != 0 and riemann_nonzero_count(Rm) > 0
    science = (not matrix_zero(Ein)) and others_zero and identity
    return {
        "gate":"ITER046-QGR-L1-EXACT-NONLINEAR-PPWAVE-RADIATIVE-SECTOR",
        "stream":"B","index":index,"f_profile":fi,"amplitude":str(AMPS[ai]),"harmonic_mix":str(hm),
        "transverse_laplacian":str(lap),"G_uu":str(guu),
        "other_einstein_components_zero_exact":bool(others_zero),
        "Guu_minus_half_laplacian_identity_exact":bool(identity),
        "control_valid":bool(control),"lane_pass":bool(control and science),
    }


def stream_c(index):
    fi, ai = C_SPECS[index]
    lam = LAMBDAS[index]
    H = AMPS[ai]*FPROF[fi]*(P2 + lam*X2)
    g = pp_metric(H)
    _,_,Rm,_,_,Ein = geometry(g, COORDS)
    nz = riemann_nonzero_count(Rm)
    control = simp(g.det()) != 0 and nz > 0
    science = matrix_zero(Ein)
    return {
        "gate":"ITER046-QGR-L1-EXACT-NONLINEAR-PPWAVE-RADIATIVE-SECTOR",
        "stream":"C","index":index,"lambda":str(lam),"f_profile":fi,"amplitude":str(AMPS[ai]),
        "einstein_zero_exact":matrix_zero(Ein),"riemann_nonzero_components":nz,
        "control_valid":bool(control),"lane_pass":bool(control and science),
    }


def stream_d(index):
    fi, a, b = D_SPECS[index]
    Q = P2 + R(2,3)*X2 + R(1,4)*P3 + R(1,10)*P4
    H1 = a*FPROF[fi]*Q
    H2 = b*FPROF[fi]*Q
    _,_,Rm1,_,_,Ein1 = geometry(pp_metric(H1), COORDS)
    _,_,Rm2,_,_,Ein2 = geometry(pp_metric(H2), COORDS)
    ratio = simp(b/a)
    scaling = all(simp(Rm2[i][j][k][l] - ratio*Rm1[i][j][k][l]) == 0
                  for i,j,k,l in itertools.product(range(N),repeat=4))
    nz = riemann_nonzero_count(Rm1)
    control = nz > 0 and a != 0 and b != 0 and a != b
    science = matrix_zero(Ein1) and matrix_zero(Ein2) and scaling
    return {
        "gate":"ITER046-QGR-L1-EXACT-NONLINEAR-PPWAVE-RADIATIVE-SECTOR",
        "stream":"D","index":index,"f_profile":fi,"a":str(a),"b":str(b),"ratio":str(ratio),
        "einstein_a_zero_exact":matrix_zero(Ein1),"einstein_b_zero_exact":matrix_zero(Ein2),
        "full_riemann_exact_amplitude_scaling":bool(scaling),"riemann_nonzero_components":nz,
        "control_valid":bool(control),"lane_pass":bool(control and science),
    }


def stream_e(index):
    # Use independent coordinate symbols and transform the full metric tensor.
    U,V,X,Y = sp.symbols("U V X Y", real=True)
    new_coords = (U,V,X,Y)
    M = E_MATRICES[index]
    bi,fi,ai = E_SPECS[index]
    H = AMPS[ai]*FPROF[fi]*BASES[bi]
    gold = pp_metric(H)
    old_vec = M*sp.Matrix(new_coords)
    subs = {u:old_vec[0], v:old_vec[1], x:old_vec[2], y:old_vec[3]}
    gnew = (M.T*gold.subs(subs)*M).applyfunc(simp)
    _,_,Rm,_,_,Ein = geometry(gnew, new_coords)
    jac = simp(M.det())
    detg = simp(gnew.det())
    nz = riemann_nonzero_count(Rm)
    control = jac != 0 and detg != 0 and nz > 0
    science = matrix_zero(Ein)
    return {
        "gate":"ITER046-QGR-L1-EXACT-NONLINEAR-PPWAVE-RADIATIVE-SECTOR",
        "stream":"E","index":index,"basis":bi,"f_profile":fi,"amplitude":str(AMPS[ai]),
        "jacobian_det":str(jac),"metric_det":str(detg),
        "einstein_zero_exact":matrix_zero(Ein),"riemann_nonzero_components":nz,
        "control_valid":bool(control),"lane_pass":bool(control and science),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stream", required=True, choices=list("ABCDE"))
    ap.add_argument("--index", required=True, type=int)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    limits = {"A":12,"B":6,"C":6,"D":6,"E":4}
    if not (0 <= args.index < limits[args.stream]):
        raise SystemExit("index outside frozen stream")
    fn = {"A":stream_a,"B":stream_b,"C":stream_c,"D":stream_d,"E":stream_e}[args.stream]
    out = fn(args.index)
    out["classification"] = f"ITER046_{args.stream}_LANE_PASS" if out["lane_pass"] else f"ITER046_{args.stream}_LANE_FAIL"
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out,"w",encoding="utf-8") as f:
        json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))

if __name__ == "__main__":
    main()
