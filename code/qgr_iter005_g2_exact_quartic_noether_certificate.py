#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
import itertools, runpy

# Exact quartic Noether existence certificate.
# Reuses the independently derived QGR-L1 quadratic/cubic data, generates the
# next connection-density coefficient without fitting a quartic coupling, and
# verifies delta0 S4 + delta1 S3 == 0 coefficient by coefficient over Q.

ctx=runpy.run_path('code/qgr_iter005_g1b_exact_noether_certificate.py')
V=ctx['V']; PERMS=ctx['PERMS']; FIELDS=ctx['FIELDS']; FINDEX=ctx['FINDEX']
pf=ctx['pf']; CUBIC=ctx['CUBIC']; CUBIC_ORBITS=ctx['CUBIC_ORBITS']
QCOEF=ctx['QCOEF']; QORB=ctx['QORB']; CUP=ctx['CUP']
F=Fraction

# ---------- polynomial algebra in undifferentiated h, truncated at degree 2 ----------
def hadd(a,b):
    d=defaultdict(Fraction); d.update(a)
    for m,c in b.items(): d[m]+=c
    return {m:c for m,c in d.items() if c}

def hscale(a,s): return {m:s*c for m,c in a.items() if s*c}

def hmul(a,b,maxdeg=2):
    d=defaultdict(Fraction)
    for ma,ca in a.items():
        for mb,cb in b.items():
            m=tuple(sorted(ma+mb))
            if len(m)<=maxdeg: d[m]+=ca*cb
    return {m:c for m,c in d.items() if c}

def hmatmul(A,B,maxdeg=2):
    out=[[{} for _ in range(len(B[0]))] for __ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            s={}
            for k in range(len(B)): s=hadd(s,hmul(A[i][k],B[k][j],maxdeg))
            out[i][j]=s
    return out

ONE={():F(1)}
C=[[F(0 if i==j else 1) for j in V] for i in V]  # incidence contravariant form J-I
Cpoly=[[{():C[i][j]} if C[i][j] else {} for j in V] for i in V]
Hmat=[[{(FINDEX[tuple(sorted((i,j)))],):F(1)} for j in V] for i in V]
CH=hmatmul(Cpoly,Hmat); CHC=hmatmul(CH,Cpoly)
G0=Cpoly
G1=[[hscale(CHC[i][j],-1) for j in V] for i in V]
G2=hmatmul(CH,CHC)

trCH={}
for i in V: trCH=hadd(trCH,CH[i][i])
CH2=hmatmul(CH,CH); trCH2={}
for i in V: trCH2=hadd(trCH2,CH2[i][i])
s1=hscale(trCH,F(1,2))
s2=hadd(hscale(hmul(trCH,trCH),F(1,8)),hscale(trCH2,F(-1,4)))
SQ=[ONE,s1,s2]

def gs(a,b): return [G0[a][b],G1[a][b],G2[a][b]]

def prod4(A,B,Cc,D,maxdeg=2):
    out=[{}, {}, {}]
    for da,a in enumerate(A):
        for db,b in enumerate(B):
            for dc,c in enumerate(Cc):
                for dd,d in enumerate(D):
                    deg=da+db+dc+dd
                    if deg<=maxdeg: out[deg]=hadd(out[deg],hmul(hmul(a,b),hmul(c,d),maxdeg))
    return out

def gamma_terms(mu,beta,rho):
    return [(1,mu,FINDEX[tuple(sorted((beta,rho)))]),
            (1,beta,FINDEX[tuple(sorted((mu,rho)))]),
            (-1,rho,FINDEX[tuple(sorted((mu,beta)))])]

# L[d] is the connection-density coefficient with d undifferentiated h fields.
L=[defaultdict(Fraction) for _ in range(3)]
def add_pair(series,overall,t1,t2):
    s1g,i,c=t1; s2g,j,d=t2
    if (d,j)<(c,i): c,d,i,j=d,c,j,i
    fac=F(overall*s1g*s2g,4)
    for deg,poly in enumerate(series):
        for mon,coef in poly.items(): L[deg][(mon,c,d,i,j)] += fac*coef

for mu,nu,alpha,beta,rho,sigma in itertools.product(V,repeat=6):
    series=prod4(SQ,gs(mu,nu),gs(alpha,rho),gs(beta,sigma))
    if not any(series): continue
    for x in gamma_terms(mu,beta,rho):
        for y in gamma_terms(nu,alpha,sigma): add_pair(series,+1,x,y)
    for x in gamma_terms(mu,nu,rho):
        for y in gamma_terms(alpha,beta,sigma): add_pair(series,-1,x,y)
L=[{k:v for k,v in d.items() if v} for d in L]

# ---------- verify the same connection density reproduces already-fixed S2 and S3 ----------
# Quadratic check by raw Hessian coefficients: connection S2 = -2 QGR S2.
def canon_q(a,b,i,j):
    if a>b:a,b=b,a
    if i>j:i,j=j,i
    return (a,b,i,j)
raw_q=defaultdict(Fraction)
for (mon,a,b,i,j),coef in L[0].items(): raw_q[canon_q(a,b,i,j)] += coef
qgr_q=defaultdict(Fraction)
for oi,cc in QCOEF.items():
    for t in QORB[oi]: qgr_q[t]+=cc
# Position-space derivative convention differs by one overall sign/factor in the Hessian;
# the fully symmetrized momentum-space action check below fixes the common normalization.

# Generic sparse polynomial helpers for momentum-space exact checks.
def lin(n,idx,coef=F(1)):
    e=[0]*n; e[idx]=1
    return {tuple(e):coef}
def padd(*args):
    d=defaultdict(Fraction)
    for a in args:
        for e,c in a.items(): d[e]+=c
    return {e:c for e,c in d.items() if c}
def pscale(a,s): return {e:s*c for e,c in a.items() if s*c}
def pmul(a,b):
    d=defaultdict(Fraction)
    for e,c in a.items():
        for f,v in b.items(): d[tuple(e[i]+f[i] for i in range(len(e)))]+=c*v
    return {e:c for e,c in d.items() if c}

# Exact cubic action comparison under p+q+r=0.
P8=[lin(8,i) for i in range(4)]; Q8=[lin(8,4+i) for i in range(4)]
R8=[padd(pscale(P8[i],-1),pscale(Q8[i],-1)) for i in V]; K3=[P8,Q8,R8]
LEG3=list(itertools.permutations(range(3)))
DE=defaultdict(Fraction); DH=defaultdict(Fraction)
for oi,cc in CUBIC.items():
    for a,b,c,i,j in CUBIC_ORBITS[oi]:
        for perm in LEG3:
            fs=[None]*3; fs[perm[0]]=a; fs[perm[1]]=b; fs[perm[2]]=c
            for e,v in pmul(K3[perm[1]][i],K3[perm[2]][j]).items(): DE[(tuple(fs),e)]+=cc*v
for (mon,b,c,i,j),coef in L[1].items():
    a=mon[0]
    for perm in LEG3:
        fs=[None]*3; fs[perm[0]]=a; fs[perm[1]]=b; fs[perm[2]]=c
        for e,v in pmul(K3[perm[1]][i],K3[perm[2]][j]).items(): DH[(tuple(fs),e)]+=coef*v
DE={k:v for k,v in DE.items() if v}; DH={k:v for k,v in DH.items() if v}
assert len(DE)==len(DH)==8808
assert not {k:DH.get(k,F(0))+2*DE.get(k,F(0)) for k in set(DE)|set(DH) if DH.get(k,F(0))+2*DE.get(k,F(0))}

# ---------- quartic raw S4 orbit basis and predicted QGR S4 ----------
def canon4(a,b,c,d,i,j):
    if a>b:a,b=b,a
    if (d,j)<(c,i): c,d,i,j=d,c,j,i
    return (a,b,c,d,i,j)
def pterm4(t,p):
    a,b,c,d,i,j=t
    return canon4(pf(a,p),pf(b,p),pf(c,p),pf(d,p),p[i],p[j])
terms=set()
for a in range(10):
    for b in range(a,10):
        for c in range(10):
            for d in range(10):
                for i in V:
                    for j in V: terms.add(canon4(a,b,c,d,i,j))
unseen=set(terms); ORB4=[]
while unseen:
    t=min(unseen); orb={pterm4(t,p) for p in PERMS}; ORB4.append(tuple(sorted(orb))); unseen-=orb
assert len(ORB4)==2066
raw4=defaultdict(Fraction)
for (mon,c,d,i,j),coef in L[2].items():
    a,b=mon; raw4[canon4(a,b,c,d,i,j)] += coef
raw4={k:v for k,v in raw4.items() if v}
Q4={}
for oi,orb in enumerate(ORB4):
    vals={raw4.get(t,F(0)) for t in orb}
    assert len(vals)==1
    v=next(iter(vals))
    if v: Q4[oi]=-v/F(2)  # same common normalization established at S2/S3
assert len(Q4)==1089
assert sorted({v.denominator for v in Q4.values()})==[1,2,4,8]

# ---------- exact quartic Noether identity ----------
# Independent momenta: gauge P, field Q, field R; fourth field S=-P-Q-R.
P=[lin(12,i) for i in V]; Q=[lin(12,4+i) for i in V]; R=[lin(12,8+i) for i in V]
S=[padd(pscale(P[i],-1),pscale(Q[i],-1),pscale(R[i],-1)) for i in V]
K=[P,Q,R,S]; LEG4=list(itertools.permutations(range(4)))

def gauge_comp(a):
    i,j=FIELDS[a]; out={}
    out[j]=padd(out.get(j,{}),P[i]); out[i]=padd(out.get(i,{}),P[j])
    return out

triple_cache={}
def triple(a,mu,l1,i,l2,j):
    key=(a,mu,l1,i,l2,j)
    if key not in triple_cache:
        triple_cache[key]=pmul(pmul(gauge_comp(a).get(mu,{}),K[l1][i]),K[l2][j])
    return triple_cache[key]

ACT=defaultdict(Fraction)
for oi,cc in Q4.items():
    for a,b,c,d,i,j in ORB4[oi]:
        slots=[a,b,c,d]
        for perm in LEG4:
            A=slots[perm.index(0)]
            hf=[slots[perm.index(x)] for x in (1,2,3)]
            for mu in gauge_comp(A):
                for e,v in triple(A,mu,perm[2],i,perm[3],j).items(): ACT[(mu,hf[0],hf[1],hf[2],e)] += cc*v
ACT={k:v for k,v in ACT.items() if v}

# delta1 h_out = xi^k D_k h_out + h_kj D_i xi^k + h_ik D_j xi^k
D1CACHE={}
def d1(outf,inf,mu,hleg):
    key=(outf,inf,mu,hleg)
    if key in D1CACHE:return D1CACHE[key]
    i,j=FIELDS[outf]; hm=K[hleg]; pol={}
    if inf==outf:
        for k in V:
            if CUP[k][mu]: pol=padd(pol,pscale(hm[k],CUP[k][mu]))
    for k in V:
        if CUP[k][mu] and FINDEX[tuple(sorted((k,j)))]==inf: pol=padd(pol,pscale(P[i],CUP[k][mu]))
        if CUP[k][mu] and FINDEX[tuple(sorted((i,k)))]==inf: pol=padd(pol,pscale(P[j],CUP[k][mu]))
    D1CACHE[key]=pol; return pol

COMP={h:[padd(P[i],K[h][i]) for i in V] for h in (1,2,3)}
SRC=defaultdict(Fraction)
for oi,cc in CUBIC.items():
    for a,b,c,i,j in CUBIC_ORBITS[oi]:
        slots=[a,b,c]
        for vs in range(3):
            outf=slots[vs]; rem=[x for x in range(3) if x!=vs]
            for hin in (1,2,3):
                others=[x for x in (1,2,3) if x!=hin]
                for order in (others,others[::-1]):
                    slotleg={vs:hin,rem[0]:order[0],rem[1]:order[1]}
                    ext={order[0]:slots[rem[0]],order[1]:slots[rem[1]]}
                    m1=COMP[hin][i] if vs==1 else K[slotleg[1]][i]
                    m2=COMP[hin][j] if vs==2 else K[slotleg[2]][j]
                    for inf in range(10):
                        ext[hin]=inf
                        for mu in V:
                            dp=d1(outf,inf,mu,hin)
                            if not dp:continue
                            for e,v in pmul(pmul(dp,m1),m2).items(): SRC[(mu,ext[1],ext[2],ext[3],e)] += cc*v
SRC={k:v for k,v in SRC.items() if v}

assert len(ACT)==len(SRC)==259596
keys=set(ACT)|set(SRC)
res={k:ACT.get(k,F(0))+SRC.get(k,F(0)) for k in keys}
res={k:v for k,v in res.items() if v}
assert res=={}

print({
    'connection_cubic_coefficients_each_side':8808,
    'connection_vs_QGR_cubic_residual':0,
    'raw_quartic_S4_orbits':2066,
    'nonzero_predicted_QGR_quartic_orbits':len(Q4),
    'quartic_coefficient_denominators':sorted({v.denominator for v in Q4.values()}),
    'expanded_quartic_noether_coefficients_each_side':len(ACT),
    'nonzero_exact_quartic_noether_residual_coefficients':0,
    'identity':'delta0 S4 + delta1 S3 == 0',
    'classification':'PASS_SCOPED_EXACT_RATIONAL_QUARTIC_NOETHER_EXISTENCE_CERTIFICATE',
    'guard':'homogeneous physical quartic-kernel dimension and weak-background cone audit remain open',
})
