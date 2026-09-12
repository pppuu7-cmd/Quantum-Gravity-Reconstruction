#!/usr/bin/env python3
"""Iter047: exact metric-level activation map for the QGR Weyl^3 operator.

Preregistered in status/ITERATION_047.md before this implementation.
This is an invariant/operator-activation gate only.  c6 is never fitted or set.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os

import sympy as sp

N = 4
R = sp.Rational


def simp(z):
    return sp.factor(sp.cancel(sp.simplify(z)))


def matrix_zero(M):
    return all(simp(M[i,j]) == 0 for i,j in itertools.product(range(M.rows), range(M.cols)))


def tensor4_zero(T):
    return all(simp(T[a][b][c][d]) == 0 for a,b,c,d in itertools.product(range(N), repeat=4))


def tensor4_nonzero_count(T):
    return sum(simp(T[a][b][c][d]) != 0 for a,b,c,d in itertools.product(range(N), repeat=4))


def geometry_weyl(g, coords):
    """Direct exact geometry and frozen W2/W3 contraction convention."""
    gi = g.inv().applyfunc(simp)
    Gamma = [[[sp.Integer(0) for _ in range(N)] for __ in range(N)] for ___ in range(N)]
    for a,b,c in itertools.product(range(N), repeat=3):
        Gamma[a][b][c] = simp(R(1,2)*sum(
            gi[a,d]*(sp.diff(g[d,c],coords[b]) + sp.diff(g[d,b],coords[c]) - sp.diff(g[b,c],coords[d]))
            for d in range(N)
        ))

    Rm = [[[[sp.Integer(0) for _ in range(N)] for __ in range(N)] for ___ in range(N)] for ____ in range(N)]
    for a,b,c,d in itertools.product(range(N), repeat=4):
        Rm[a][b][c][d] = simp(
            sp.diff(Gamma[a][b][d],coords[c]) - sp.diff(Gamma[a][b][c],coords[d])
            + sum(Gamma[a][c][e]*Gamma[e][b][d] - Gamma[a][d][e]*Gamma[e][b][c] for e in range(N))
        )

    Ric = sp.MutableDenseMatrix(N,N,[0]*(N*N))
    for b,d in itertools.product(range(N), repeat=2):
        Ric[b,d] = simp(sum(Rm[a][b][a][d] for a in range(N)))
    Rsc = simp(sum(gi[a,b]*Ric[a,b] for a,b in itertools.product(range(N), repeat=2)))

    Rlow = [[[[simp(sum(g[a,e]*Rm[e][b][c][d] for e in range(N)))
               for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    C = [[[[sp.Integer(0) for _ in range(N)] for __ in range(N)] for ___ in range(N)] for ____ in range(N)]
    for a,b,c,d in itertools.product(range(N), repeat=4):
        C[a][b][c][d] = simp(
            Rlow[a][b][c][d]
            - R(1,2)*(g[a,c]*Ric[b,d] - g[a,d]*Ric[b,c] - g[b,c]*Ric[a,d] + g[b,d]*Ric[a,c])
            + Rsc*R(1,6)*(g[a,c]*g[b,d] - g[a,d]*g[b,c])
        )

    # C_ab^{ cd}
    Cm = [[[[simp(sum(gi[c,e]*gi[d,f]*C[a][b][e][f] for e in range(N) for f in range(N)))
             for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    W2 = simp(sum(Cm[a][b][c][d]*Cm[c][d][a][b]
                  for a,b,c,d in itertools.product(range(N), repeat=4)))
    W3 = simp(sum(Cm[a][b][c][d]*Cm[c][d][e][f]*Cm[e][f][a][b]
                  for a,b,c,d,e,f in itertools.product(range(N), repeat=6)))
    return gi, Rm, Ric, Rsc, C, W2, W3


# ---------- Stream A: harmonic pp waves ----------
u,v,x,y = sp.symbols('u v x y', real=True)
PP_COORDS = (u,v,x,y)
P2 = x**2-y**2
X2 = 2*x*y
P3 = x**3-3*x*y**2
P4 = x**4-6*x**2*y**2+y**4
PP_SPECS = [
    (R(1,20), P2),
    (R(1,10), X2),
    (R(1,5), (1+u)*P3),
    (R(1,2), (1-u+u**2)*P4),
    (R(3,10), (1+u**2)* (P2 + R(2,3)*X2)),
    (R(2,5), (1-u/R(3))* (P3 + R(1,4)*P4)),
]

def pp_metric(H):
    return sp.Matrix([[H,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])


def stream_a(index):
    amp, profile = PP_SPECS[index]
    g = pp_metric(amp*profile)
    _,Rm,Ric,Rsc,C,W2,W3 = geometry_weyl(g, PP_COORDS)
    rnz = tensor4_nonzero_count(Rm)
    control = simp(g.det()) != 0 and rnz > 0
    science = matrix_zero(Ric) and Rsc == 0 and W2 == 0 and W3 == 0
    return {
        'gate':'ITER047-EXACT-WEYL3-CURVATURE-CLASS-ACTIVATION-MAP',
        'stream':'A','index':index,'amplitude':str(amp),
        'metric_det':str(simp(g.det())),'riemann_nonzero_components':rnz,
        'ricci_zero_exact':matrix_zero(Ric),'scalar_zero_exact':bool(Rsc==0),
        'weyl_zero_exact':tensor4_zero(C),'W2':str(W2),'W3':str(W3),
        'c6_status':'SYMBOLIC_UNFIXED','control_valid':bool(control),
        'lane_pass':bool(control and science),
    }


# ---------- Stream B: Schwarzschild ----------
t,r,th,ph = sp.symbols('t r theta phi', positive=True, real=True)
M = sp.symbols('M', positive=True, real=True)
SCHW_COORDS=(t,r,th,ph)
B_SPECS=[
    (R(1,5),R(3),R(4)),(R(1,3),R(4),R(6)),(R(1,2),R(5),R(7)),
    (R(2,3),R(6),R(9)),(R(3,4),R(7),R(10)),(R(4,5),R(8),R(12)),
]

def schwarzschild_metric():
    f=1-2*M/r
    return sp.diag(-f,1/f,r**2,r**2*sp.sin(th)**2)


def stream_b(index):
    mval,r1,r2=B_SPECS[index]
    _,Rm,Ric,Rsc,C,W2,W3=geometry_weyl(schwarzschild_metric(),SCHW_COORDS)
    target2=48*M**2/r**6
    target3=96*M**3/r**9
    formula2=simp(W2-target2)==0
    formula3=simp(W3-target3)==0
    w31=simp(W3.subs({M:mval,r:r1}))
    w32=simp(W3.subs({M:mval,r:r2}))
    radial=simp(w32/w31-(r1/r2)**9)==0
    # Independent exact mass-cubic check at fixed radius.
    m2=2*mval
    mass=simp(W3.subs({M:m2,r:r1})/w31-8)==0
    control=matrix_zero(Ric) and Rsc==0 and tensor4_nonzero_count(Rm)>0 and w31!=0 and w32!=0
    science=formula2 and formula3 and radial and mass
    return {
        'gate':'ITER047-EXACT-WEYL3-CURVATURE-CLASS-ACTIVATION-MAP',
        'stream':'B','index':index,'mass':str(mval),'r1':str(r1),'r2':str(r2),
        'ricci_zero_exact':matrix_zero(Ric),'scalar_zero_exact':bool(Rsc==0),
        'W2_formula':str(W2),'W3_formula':str(W3),
        'W2_target_exact':bool(formula2),'W3_target_exact':bool(formula3),
        'W3_r1':str(w31),'W3_r2':str(w32),
        'radial_ninth_power_scaling_exact':bool(radial),'mass_cubic_scaling_exact':bool(mass),
        'c6_status':'SYMBOLIC_UNFIXED','control_valid':bool(control),
        'lane_pass':bool(control and science),
    }


# ---------- Stream C: Kasner ----------
T,X,Y,Z=sp.symbols('T X Y Z', positive=True, real=True)
K_COORDS=(T,X,Y,Z)
PERMS=[
    (-R(1,3),R(2,3),R(2,3)),(R(2,3),-R(1,3),R(2,3)),(R(2,3),R(2,3),-R(1,3)),
    (-R(1,3),R(2,3),R(2,3)),(R(2,3),-R(1,3),R(2,3)),(R(2,3),R(2,3),-R(1,3)),
]
C_TIMES=[(R(1),R(2)),(R(2),R(3)),(R(3,2),R(5,2)),(R(2,3),R(4,3)),(R(3),R(4)),(R(4),R(6))]

def kasner_metric(p):
    return sp.diag(-1,T**(2*p[0]),T**(2*p[1]),T**(2*p[2]))


def stream_c(index):
    p=PERMS[index]; t1,t2=C_TIMES[index]
    _,Rm,Ric,Rsc,C,W2,W3=geometry_weyl(kasner_metric(p),K_COORDS)
    w21=simp(W2.subs(T,t1)); w22=simp(W2.subs(T,t2))
    w31=simp(W3.subs(T,t1)); w32=simp(W3.subs(T,t2))
    scale2=simp(w22/w21-(t1/t2)**4)==0
    scale3=simp(w32/w31-(t1/t2)**6)==0
    control=matrix_zero(Ric) and Rsc==0 and tensor4_nonzero_count(Rm)>0 and w21!=0 and w31!=0
    science=(W2!=0 and W3!=0 and scale2 and scale3)
    return {
        'gate':'ITER047-EXACT-WEYL3-CURVATURE-CLASS-ACTIVATION-MAP',
        'stream':'C','index':index,'exponents':[str(q) for q in p],'t1':str(t1),'t2':str(t2),
        'ricci_zero_exact':matrix_zero(Ric),'scalar_zero_exact':bool(Rsc==0),
        'W2_formula':str(W2),'W3_formula':str(W3),'W2_t1':str(w21),'W3_t1':str(w31),
        'W2_time_minus4_scaling_exact':bool(scale2),'W3_time_minus6_scaling_exact':bool(scale3),
        'c6_status':'SYMBOLIC_UNFIXED','control_valid':bool(control),
        'lane_pass':bool(control and science),
    }


# ---------- Stream D: conformally-flat FLRW ----------
tau,q1,q2,q3=sp.symbols('tau q1 q2 q3', real=True)
F_COORDS=(tau,q1,q2,q3)
SCALE_FACTORS=[
    1+tau,
    1+tau**2,
    1+tau+tau**2,
    2+tau+tau**3/R(3),
    1-tau/R(2)+tau**2/R(4),
    2+tau**2+tau**4/R(5),
]
F_POINTS=[R(1,3),R(1,2),R(2,3),R(1,4),R(-1,3),R(3,5)]

def flrw_metric(a):
    return sp.diag(-1,a**2,a**2,a**2)


def stream_d(index):
    a=SCALE_FACTORS[index]; p=F_POINTS[index]
    g=flrw_metric(a)
    _,Rm,Ric,Rsc,C,W2,W3=geometry_weyl(g,F_COORDS)
    detp=simp(g.det().subs(tau,p))
    rnz=tensor4_nonzero_count(Rm)
    # At least one curvature component must remain nonzero at the frozen point.
    point_rnz=sum(simp(Rm[i][j][k][l].subs(tau,p))!=0 for i,j,k,l in itertools.product(range(N),repeat=4))
    control=detp!=0 and rnz>0 and point_rnz>0
    science=tensor4_zero(C) and W2==0 and W3==0
    return {
        'gate':'ITER047-EXACT-WEYL3-CURVATURE-CLASS-ACTIVATION-MAP',
        'stream':'D','index':index,'scale_factor':str(a),'tau_point':str(p),
        'metric_det_at_point':str(detp),'riemann_nonzero_components_symbolic':rnz,
        'riemann_nonzero_components_at_point':point_rnz,'ricci_zero_exact':matrix_zero(Ric),
        'scalar_curvature':str(Rsc),'weyl_zero_exact':tensor4_zero(C),'W2':str(W2),'W3':str(W3),
        'c6_status':'SYMBOLIC_UNFIXED','control_valid':bool(control),
        'lane_pass':bool(control and science),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',required=True,choices=list('ABCD'))
    ap.add_argument('--index',required=True,type=int)
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    if not 0 <= args.index < 6:
        raise SystemExit('index outside frozen stream')
    fn={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[args.stream]
    out=fn(args.index)
    out['classification']=f"ITER047_{args.stream}_LANE_PASS" if out['lane_pass'] else f"ITER047_{args.stream}_LANE_FAIL"
    os.makedirs(os.path.dirname(args.out),exist_ok=True)
    with open(args.out,'w',encoding='utf-8') as f:
        json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__':
    main()
