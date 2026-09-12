#!/usr/bin/env python3
"""Iter049: radial-gauge-unfixed spherical reduced variation of Weyl^3.

Preregistered in status/ITERATION_049.md before implementation. c6 remains
symbolic/unfixed; all reported reduced Euler-Lagrange expressions are the
coefficient multiplying c6.
"""
from __future__ import annotations
import argparse,itertools,json,os
import sympy as sp

R=sp.Rational
D=4
t,r,th,ph=sp.symbols('t r theta phi', positive=True, real=True)
coords=(t,r,th,ph)
F=sp.Function('F')(r); N=sp.Function('N')(r); S=sp.Function('S')(r)

def simp(x): return sp.factor(sp.cancel(sp.simplify(x)))
def zero_exact(x): return sp.trigsimp(simp(x),method='fu')==0
def matrix_zero(M): return all(simp(M[i,j])==0 for i,j in itertools.product(range(M.rows),range(M.cols)))
def tensor_zero(T): return all(zero_exact(T[a][b][c][d]) for a,b,c,d in itertools.product(range(D),repeat=4))

def geometry(g):
    gi=g.inv().applyfunc(simp)
    G=[[[0 for _ in range(D)] for __ in range(D)] for ___ in range(D)]
    for a,b,c in itertools.product(range(D),repeat=3):
        G[a][b][c]=simp(R(1,2)*sum(gi[a,d]*(sp.diff(g[d,c],coords[b])+sp.diff(g[d,b],coords[c])-sp.diff(g[b,c],coords[d])) for d in range(D)))
    Rm=[[[[0 for _ in range(D)] for __ in range(D)] for ___ in range(D)] for ____ in range(D)]
    for a,b,c,d in itertools.product(range(D),repeat=4):
        Rm[a][b][c][d]=simp(sp.diff(G[a][b][d],coords[c])-sp.diff(G[a][b][c],coords[d])+sum(G[a][c][e]*G[e][b][d]-G[a][d][e]*G[e][b][c] for e in range(D)))
    Ric=sp.MutableDenseMatrix(D,D,[0]*(D*D))
    for b,d in itertools.product(range(D),repeat=2): Ric[b,d]=simp(sum(Rm[a][b][a][d] for a in range(D)))
    Rsc=simp(sum(gi[a,b]*Ric[a,b] for a,b in itertools.product(range(D),repeat=2)))
    Rlow=[[[[simp(sum(g[a,e]*Rm[e][b][c][d] for e in range(D))) for d in range(D)] for c in range(D)] for b in range(D)] for a in range(D)]
    C=[[[[0 for _ in range(D)] for __ in range(D)] for ___ in range(D)] for ____ in range(D)]
    for a,b,c,d in itertools.product(range(D),repeat=4):
        C[a][b][c][d]=simp(Rlow[a][b][c][d]-R(1,2)*(g[a,c]*Ric[b,d]-g[a,d]*Ric[b,c]-g[b,c]*Ric[a,d]+g[b,d]*Ric[a,c])+Rsc*R(1,6)*(g[a,c]*g[b,d]-g[a,d]*g[b,c]))
    Cm=[[[[simp(sum(gi[c,e]*gi[d,f]*C[a][b][e][f] for e in range(D) for f in range(D))) for d in range(D)] for c in range(D)] for b in range(D)] for a in range(D)]
    W3=simp(sum(Cm[a][b][c][d]*Cm[c][d][e][f]*Cm[e][f][a][b] for a,b,c,d,e,f in itertools.product(range(D),repeat=6)))
    return Rm,Ric,Rsc,C,W3

def authority():
    g=sp.diag(-F**2,N**2,S**2,S**2*sp.sin(th)**2)
    Rm,Ric,Rsc,C,W3=geometry(g)
    Q=simp(-F*N**3-F*N*S*sp.diff(S,r,2)+F*N*sp.diff(S,r)**2+F*S*sp.diff(N,r)*sp.diff(S,r)+N*S**2*sp.diff(F,r,2)-N*S*sp.diff(F,r)*sp.diff(S,r)-S**2*sp.diff(F,r)*sp.diff(N,r))
    W3target=simp(-R(4,9)*Q**3/(F**3*N**9*S**6))
    L6=simp(F*N*S**2*W3)
    Ltarget=simp(-R(4,9)*Q**3/(F**2*N**8*S**4))
    def EL(q): return simp(sp.diff(L6,q)-sp.diff(sp.diff(L6,sp.diff(q,r)),r)+sp.diff(sp.diff(L6,sp.diff(q,r,2)),r,2))
    EF,EN,ES=EL(F),EL(N),EL(S)
    noether=simp(EF*sp.diff(F,r)+ES*sp.diff(S,r)-N*sp.diff(EN,r))
    cert=(simp(W3-W3target)==0 and simp(L6-Ltarget)==0 and noether==0)
    return g,Rm,Ric,Rsc,C,W3,L6,EF,EN,ES,Q,cert,noether

def prof(expr,fv,nv,sv): return simp(expr.subs({F:fv,N:nv,S:sv}).doit())
def ricprof(Ric,fv,nv,sv): return sp.Matrix(D,D,lambda i,j:prof(Ric[i,j],fv,nv,sv))
def rmnz(Rm,fv,nv,sv,pt): return sum(prof(Rm[a][b][c][d],fv,nv,sv).subs(r,pt)!=0 for a,b,c,d in itertools.product(range(D),repeat=4))

MASSES=[R(1,5),R(1,4),R(1,3),R(2,5),R(1,2),R(3,5)]
RATIOS=[R(3),R(4),R(5),R(6),R(8),R(10)]
HS=[R(1,7),R(1,6),R(1,5),R(1,7),R(1,6),R(1,5)]
SIGMAS=[1,1,1,-1,-1,-1]
B_RADII=[R(1),R(4,3),R(3,2),R(1),R(4,3),R(3,2)]
MS=[R(1,2),R(2,3),R(3,2),R(2),R(3),R(4)]
DPROFILES=[
 (1+r/R(5),1+r**2/R(7),1+r+r**2/R(11),R(1)),
 (1+r**2/R(6),1+r/R(8),2+r/R(2)+r**3/R(20),R(2,3)),
 (2+r/R(7)+r**2/R(13),1+r**2/R(9),1+r**2/R(4),R(3,2)),
 (1+r/R(3)+r**3/R(50),2+r/R(10),1+r+r**3/R(30),R(4,3)),
 (R(3,2)+r**2/R(8),1+r/R(6)+r**2/R(25),2+r**2/R(5)+r**3/R(40),R(5,4)),
 (1+r/R(9),R(3,2)+r/R(11),1+r/R(2),R(3,4)),
]

def stream_a(i,A):
    g,Rm,Ric,Rsc,C,W3,L6,EF,EN,ES,Q,cert,noether=A
    M=MASSES[i]; rv=RATIOS[i]*M
    m=sp.symbols('M',positive=True,real=True)
    ff=1-2*m/r; fv=sp.sqrt(ff); nv=1/fv; sv=r
    vals=[prof(x,fv,nv,sv) for x in (W3,L6,EF,EN,ES)]
    targets=[96*m**3/r**9,96*m**3/r**7,-48*m**2*(-32*m+15*r)/(r**R(13,2)*sp.sqrt(r-2*m)),-48*m**2*(-8*m+3*r)*sp.sqrt(r-2*m)/r**R(15,2),96*m**2*(-22*m+9*r)/r**8]
    exact=cert and all(simp(x-y)==0 for x,y in zip(vals,targets))
    ric=ricprof(Ric,fv,nv,sv)
    nonzero=all(simp(x.subs({m:M,r:rv}))!=0 for x in vals[2:])
    control=matrix_zero(ric) and prof(Rsc,fv,nv,sv)==0 and rv>2*M
    return {'stream':'A','index':i,'M':str(M),'r':str(rv),'W3':str(vals[0]),'L6':str(vals[1]),'E_F':str(vals[2]),'E_N':str(vals[3]),'E_S':str(vals[4]),'generic_certificate_valid':bool(cert),'ricci_zero_exact':matrix_zero(ric),'all_schwarzschild_formulas_exact':bool(exact),'all_responses_nonzero_at_witness':bool(nonzero),'control_valid':bool(control),'lane_pass':bool(control and exact and nonzero)}

def stream_b(i,A):
    g,Rm,Ric,Rsc,C,W3,L6,EF,EN,ES,Q,cert,noether=A
    h=HS[i]; sig=SIGMAS[i]; pt=B_RADII[i]
    ff=1-sig*h**2*r**2; fv=sp.sqrt(ff); nv=1/fv; sv=r
    vals=[prof(x,fv,nv,sv) for x in (W3,L6,EF,EN,ES)]
    czero=all(zero_exact(prof(C[a][b][c][d],fv,nv,sv)) for a,b,c,d in itertools.product(range(D),repeat=4))
    nz=rmnz(Rm,fv,nv,sv,pt)
    det=simp((-fv**2*nv**2*sv**4).subs(r,pt))
    control=cert and det!=0 and nz>0 and (sig<0 or 1-h**2*pt**2>0)
    exact=czero and all(x==0 for x in vals)
    return {'stream':'B','index':i,'sigma':sig,'H':str(h),'r':str(pt),'riemann_nonzero_components_at_witness':nz,'weyl_zero_exact':bool(czero),'W3':str(vals[0]),'L6':str(vals[1]),'E_F':str(vals[2]),'E_N':str(vals[3]),'E_S':str(vals[4]),'generic_certificate_valid':bool(cert),'control_valid':bool(control),'lane_pass':bool(control and exact)}

def stream_c(i,A):
    g,Rm,Ric,Rsc,C,W3,L6,EF,EN,ES,Q,cert,noether=A
    m=MS[i]; mass=R(1,5); rho=r; RR=rho**m
    fp=1-2*mass/RR; fv=sp.sqrt(fp); nv=sp.diff(RR,rho)/fv; sv=RR
    w=prof(W3,fv,nv,sv); l=prof(L6,fv,nv,sv)
    tw=simp(96*mass**3/RR**9); tl=simp(sp.diff(RR,rho)*96*mass**3/RR**7)
    ric=ricprof(Ric,fv,nv,sv)
    pt=R(2)
    exact=cert and simp(w-tw)==0 and simp(l-tl)==0
    control=matrix_zero(ric) and prof(Rsc,fv,nv,sv)==0 and simp(RR.subs(rho,pt))>2*mass
    return {'stream':'C','index':i,'m':str(m),'M':str(mass),'rho':str(pt),'W3':str(w),'L6':str(l),'ricci_zero_exact':matrix_zero(ric),'reparameterized_invariants_and_density_exact':bool(exact),'generic_certificate_valid':bool(cert),'control_valid':bool(control),'lane_pass':bool(control and exact and w!=0 and l!=0)}

def jet_value(expr,fv,nv,sv,pt):
    mapping={F:fv.subs(r,pt),N:nv.subs(r,pt),S:sv.subs(r,pt)}
    for order in range(1,6):
        mapping[sp.diff(F,r,order)]=sp.diff(fv,r,order).subs(r,pt)
        mapping[sp.diff(N,r,order)]=sp.diff(nv,r,order).subs(r,pt)
        mapping[sp.diff(S,r,order)]=sp.diff(sv,r,order).subs(r,pt)
    return simp(expr.xreplace(mapping))

def stream_d(i,A):
    g,Rm,Ric,Rsc,C,W3,L6,EF,EN,ES,Q,cert,noether=A
    fv,nv,sv,pt=DPROFILES[i]
    vals=[jet_value(x,fv,nv,sv,pt) for x in (EF,EN,ES)]
    nonzero=sum(x!=0 for x in vals)>=2
    det=simp((-fv**2*nv**2*sv**4).subs(r,pt))
    profile_identity=simp(noether.subs({F:fv,N:nv,S:sv}).doit()) if noether!=0 else sp.Integer(0)
    control=cert and det!=0
    return {'stream':'D','index':i,'r':str(pt),'F':str(fv),'N':str(nv),'S':str(sv),'E_F_at_witness':str(vals[0]),'E_N_at_witness':str(vals[1]),'E_S_at_witness':str(vals[2]),'generic_noether_identity_exact':bool(noether==0),'profile_noether_identity_exact':bool(profile_identity==0),'at_least_two_responses_nonzero':bool(nonzero),'generic_certificate_valid':bool(cert),'control_valid':bool(control),'lane_pass':bool(control and noether==0 and profile_identity==0 and nonzero)}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--stream',required=True,choices=list('ABCD')); p.add_argument('--index',required=True,type=int); p.add_argument('--out',required=True); a=p.parse_args()
    if not 0<=a.index<6: raise SystemExit('index outside frozen stream')
    A=authority(); out={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[a.stream](a.index,A)
    out.update({'gate':'ITER049-WEYL3-SPHERICALLY-REDUCED-VARIATIONAL-RESPONSE','c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY','classification':f'ITER049_{a.stream}_LANE_PASS' if out['lane_pass'] else f'ITER049_{a.stream}_LANE_FAIL'})
    os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
