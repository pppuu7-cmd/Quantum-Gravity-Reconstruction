#!/usr/bin/env python3
"""Iter048: lapse-retaining axisymmetric Bianchi-I reduced variation of Weyl^3.

Preregistered in status/ITERATION_048.md before implementation.  The code
constructs the geometry and W3 directly from the generic metric, derives the
higher-derivative generalized Euler-Lagrange operators before background
substitution, and reports only the coefficient multiplying the still-unfixed c6.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os

import sympy as sp

R = sp.Rational
DIM = 4
t = sp.symbols('t', positive=True, real=True)
x,y,z = sp.symbols('x y z', real=True)
COORDS=(t,x,y,z)
Nf=sp.Function('N')(t)
af=sp.Function('a')(t)
bf=sp.Function('b')(t)


def simp(v):
    return sp.factor(sp.cancel(sp.simplify(v)))


def matrix_zero(M):
    return all(simp(M[i,j])==0 for i,j in itertools.product(range(M.rows),range(M.cols)))


def tensor4_zero(T):
    return all(simp(T[a][b][c][d])==0 for a,b,c,d in itertools.product(range(DIM),repeat=4))


def geometry(g,coords):
    gi=g.inv().applyfunc(simp)
    G=[[[sp.Integer(0) for _ in range(DIM)] for __ in range(DIM)] for ___ in range(DIM)]
    for a,b,c in itertools.product(range(DIM),repeat=3):
        G[a][b][c]=simp(R(1,2)*sum(
            gi[a,d]*(sp.diff(g[d,c],coords[b])+sp.diff(g[d,b],coords[c])-sp.diff(g[b,c],coords[d]))
            for d in range(DIM)))
    Rm=[[[[sp.Integer(0) for _ in range(DIM)] for __ in range(DIM)] for ___ in range(DIM)] for ____ in range(DIM)]
    for a,b,c,d in itertools.product(range(DIM),repeat=4):
        Rm[a][b][c][d]=simp(
            sp.diff(G[a][b][d],coords[c])-sp.diff(G[a][b][c],coords[d])
            +sum(G[a][c][e]*G[e][b][d]-G[a][d][e]*G[e][b][c] for e in range(DIM)))
    Ric=sp.MutableDenseMatrix(DIM,DIM,[0]*(DIM*DIM))
    for b,d in itertools.product(range(DIM),repeat=2):
        Ric[b,d]=simp(sum(Rm[a][b][a][d] for a in range(DIM)))
    Rsc=simp(sum(gi[a,b]*Ric[a,b] for a,b in itertools.product(range(DIM),repeat=2)))
    Rlow=[[[[simp(sum(g[a,e]*Rm[e][b][c][d] for e in range(DIM)))
              for d in range(DIM)] for c in range(DIM)] for b in range(DIM)] for a in range(DIM)]
    C=[[[[sp.Integer(0) for _ in range(DIM)] for __ in range(DIM)] for ___ in range(DIM)] for ____ in range(DIM)]
    for a,b,c,d in itertools.product(range(DIM),repeat=4):
        C[a][b][c][d]=simp(
            Rlow[a][b][c][d]
            -R(1,2)*(g[a,c]*Ric[b,d]-g[a,d]*Ric[b,c]-g[b,c]*Ric[a,d]+g[b,d]*Ric[a,c])
            +Rsc*R(1,6)*(g[a,c]*g[b,d]-g[a,d]*g[b,c]))
    Cm=[[[[simp(sum(gi[c,e]*gi[d,f]*C[a][b][e][f] for e in range(DIM) for f in range(DIM)))
            for d in range(DIM)] for c in range(DIM)] for b in range(DIM)] for a in range(DIM)]
    W3=simp(sum(Cm[a][b][c][d]*Cm[c][d][e][f]*Cm[e][f][a][b]
                for a,b,c,d,e,f in itertools.product(range(DIM),repeat=6)))
    return Rm,Ric,Rsc,C,W3


def reduced_authority():
    g=sp.diag(-Nf**2,af**2,bf**2,bf**2)
    Rm,Ric,Rsc,C,W3=geometry(g,COORDS)
    L6=simp(Nf*af*bf**2*W3)
    def EL(q):
        return simp(sp.diff(L6,q)-sp.diff(sp.diff(L6,sp.diff(q,t)),t)+sp.diff(sp.diff(L6,sp.diff(q,t,2)),t,2))
    EN,EA,EB=EL(Nf),EL(af),EL(bf)
    return g,Rm,Ric,Rsc,C,W3,L6,EN,EA,EB


def prof(expr,Nx,ax,bx):
    return simp(expr.subs({Nf:Nx,af:ax,bf:bx}).doit())


def ricci_prof(Ric,Nx,ax,bx):
    return sp.Matrix(DIM,DIM,lambda i,j:prof(Ric[i,j],Nx,ax,bx))


def riemann_point_nonzero(Rm,Nx,ax,bx,point):
    return sum(prof(Rm[i][j][k][l],Nx,ax,bx).subs(t,point)!=0
               for i,j,k,l in itertools.product(range(DIM),repeat=4))


K_TIMES=[R(1,2),R(2,3),R(1),R(3,2),R(2),R(3)]
ISO_SPECS=[
    (sp.Integer(1),1+t,R(1,3),False),
    (sp.Integer(1),1+t**2,R(1,2),False),
    (1+t/R(5),1+t+t**2/R(3),R(2,3),False),
    (1+t**2/R(7),2+t+t**3/R(5),R(1,4),False),
    (1-t/R(10)+t**2/R(20),1+t**2/R(4),R(3,5),False),
    (sp.Integer(1),sp.Integer(1),R(1),True),
]
PQ=[(-R(1,2),R(1,3)),(R(1,4),R(3,4)),(-R(2,3),R(1,2)),(R(2,5),-R(1,5)),(R(3,2),R(1,4)),(-R(1,4),R(5,6))]
MVALS=[R(1,2),R(2,3),R(3,2),R(2),R(3),R(4)]


def power_targets(p,q):
    L=R(4,9)*t**(p+2*q-6)*(p-1)**3*(p-q)**3
    EN=-R(8,9)*t**(p+2*q-6)*(p-1)**2*(p-q)**3*(p-3*q+5)
    EA=-R(8,9)*t**(2*q-6)*(p-1)**2*(p-q)**2*(p**2-p*q-p-9*q**2+34*q-30)
    EB= R(8,9)*t**(p+q-6)*(p-1)**2*(p-q)**2*(p**2-4*p*q+5*p-6*q**2+28*q-30)
    W3=R(4,9)*t**(-6)*(p-1)**3*(p-q)**3
    return tuple(map(simp,(W3,L,EN,EA,EB)))


def stream_a(index,auth):
    g,Rm,Ric,Rsc,C,W3,L6,EN,EA,EB=auth
    Nx=sp.Integer(1); ax=t**(-R(1,3)); bx=t**R(2,3); pt=K_TIMES[index]
    ric=ricci_prof(Ric,Nx,ax,bx)
    w=prof(W3,Nx,ax,bx); l=prof(L6,Nx,ax,bx)
    en,ea,eb=[prof(v,Nx,ax,bx) for v in (EN,EA,EB)]
    target_w=R(256,243)/t**6
    target_l=R(256,243)/t**5
    target_en=R(1024,243)/t**5
    target_ea=R(4096,243)/t**R(14,3)
    target_eb=-R(5632,243)/t**R(17,3)
    exact=all(simp(a-b)==0 for a,b in [(w,target_w),(l,target_l),(en,target_en),(ea,target_ea),(eb,target_eb)])
    nonzero=all(simp(v.subs(t,pt))!=0 for v in (w,en,ea,eb))
    control=matrix_zero(ric) and prof(Rsc,Nx,ax,bx)==0
    return {'gate':'ITER048-WEYL3-SYMMETRY-REDUCED-VARIATIONAL-RESPONSE','stream':'A','index':index,'time':str(pt),
            'W3':str(w),'L6':str(l),'E_N':str(en),'E_a':str(ea),'E_b':str(eb),
            'ricci_zero_exact':matrix_zero(ric),'all_frozen_formulas_exact':bool(exact),'responses_nonzero_at_witness':bool(nonzero),
            'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY','control_valid':bool(control),'lane_pass':bool(control and exact and nonzero)}


def stream_b(index,auth):
    g,Rm,Ric,Rsc,C,W3,L6,EN,EA,EB=auth
    Nx,s,pt,mink=ISO_SPECS[index]
    w=prof(W3,Nx,s,s); en,ea,eb=[prof(v,Nx,s,s) for v in (EN,EA,EB)]
    # Weyl tensor checked after generic derivation, before no symmetry shortcut.
    czero=all(prof(C[i][j][k][l],Nx,s,s)==0 for i,j,k,l in itertools.product(range(DIM),repeat=4))
    rnz=riemann_point_nonzero(Rm,Nx,s,s,pt)
    geom_control=(rnz==0 if mink else rnz>0)
    detp=simp((-Nx**2*s**6).subs(t,pt))
    exact=(czero and w==0 and en==0 and ea==0 and eb==0)
    control=detp!=0 and geom_control
    return {'gate':'ITER048-WEYL3-SYMMETRY-REDUCED-VARIATIONAL-RESPONSE','stream':'B','index':index,'time':str(pt),
            'lapse':str(Nx),'scale_factor':str(s),'minkowski_control':bool(mink),'riemann_nonzero_at_witness':rnz,
            'weyl_zero_exact':bool(czero),'W3':str(w),'E_N':str(en),'E_a':str(ea),'E_b':str(eb),
            'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY','control_valid':bool(control),'lane_pass':bool(control and exact)}


def stream_c(index,auth):
    g,Rm,Ric,Rsc,C,W3,L6,EN,EA,EB=auth
    p,q=PQ[index]; Nx=sp.Integer(1); ax=t**p; bx=t**q
    vals=[prof(v,Nx,ax,bx) for v in (W3,L6,EN,EA,EB)]
    targets=list(power_targets(p,q))
    exact=all(simp(v-u)==0 for v,u in zip(vals,targets))
    nonzero=(vals[0]!=0 and any(v!=0 for v in vals[2:]))
    control=(p!=q and p!=1)
    return {'gate':'ITER048-WEYL3-SYMMETRY-REDUCED-VARIATIONAL-RESPONSE','stream':'C','index':index,'p':str(p),'q':str(q),
            'W3':str(vals[0]),'L6':str(vals[1]),'E_N':str(vals[2]),'E_a':str(vals[3]),'E_b':str(vals[4]),
            'all_powerlaw_certificate_formulas_exact':bool(exact),'weyl3_and_response_active':bool(nonzero),
            'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY','control_valid':bool(control),'lane_pass':bool(control and exact and nonzero)}


def stream_d(index,auth):
    g,Rm,Ric,Rsc,C,W3,L6,EN,EA,EB=auth
    m=MVALS[index]
    Nx=m*t**(m-1); ax=t**(-m/R(3)); bx=t**(2*m/R(3))
    ric=ricci_prof(Ric,Nx,ax,bx)
    w=prof(W3,Nx,ax,bx); l=prof(L6,Nx,ax,bx)
    target_w=R(256,243)/t**(6*m)
    target_l=R(256,243)*m/t**(4*m+1)
    exact=(simp(w-target_w)==0 and simp(l-target_l)==0)
    control=matrix_zero(ric) and prof(Rsc,Nx,ax,bx)==0 and m>0
    return {'gate':'ITER048-WEYL3-SYMMETRY-REDUCED-VARIATIONAL-RESPONSE','stream':'D','index':index,'m':str(m),
            'lapse':str(Nx),'a':str(ax),'b':str(bx),'W3':str(w),'L6':str(l),
            'ricci_zero_exact':matrix_zero(ric),'reparameterized_W3_and_density_exact':bool(exact),
            'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY','control_valid':bool(control),'lane_pass':bool(control and exact and w!=0 and l!=0)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',required=True,choices=list('ABCD'))
    ap.add_argument('--index',required=True,type=int)
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    if not 0<=args.index<6:
        raise SystemExit('index outside frozen stream')
    auth=reduced_authority()
    out={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[args.stream](args.index,auth)
    out['classification']=f"ITER048_{args.stream}_LANE_PASS" if out['lane_pass'] else f"ITER048_{args.stream}_LANE_FAIL"
    os.makedirs(os.path.dirname(args.out),exist_ok=True)
    with open(args.out,'w',encoding='utf-8') as f:
        json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__':
    main()
