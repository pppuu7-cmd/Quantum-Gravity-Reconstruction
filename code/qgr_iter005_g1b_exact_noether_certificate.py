#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
import itertools

# Exact sparse-polynomial certificate for delta0 S3 + delta1 S2 == 0.
# No numerical approximation is used.

V=range(4)
PERMS=list(itertools.permutations(V))
LEG_PERMS=list(itertools.permutations(range(3)))
FIELDS=[(i,j) for i in V for j in range(i,4)]
FINDEX={f:i for i,f in enumerate(FIELDS)}


def F(s): return Fraction(s)

def pf(a,p):
    i,j=FIELDS[a]
    return FINDEX[tuple(sorted((p[i],p[j])))]

def canon_cubic(a,b,c,i,j):
    if (c,j)<(b,i): b,c,i,j=c,b,j,i
    return (a,b,c,i,j)

def pterm_cubic(t,p):
    a,b,c,i,j=t
    return canon_cubic(pf(a,p),pf(b,p),pf(c,p),p[i],p[j])

# Deterministic 399 raw cubic S4 orbits.
terms=set()
for a in range(10):
    for b in range(10):
        for c in range(10):
            for i in V:
                for j in V:
                    terms.add(canon_cubic(a,b,c,i,j))
unseen=set(terms); CUBIC_ORBITS=[]
while unseen:
    t=min(unseen)
    orb={pterm_cubic(t,p) for p in PERMS}
    CUBIC_ORBITS.append(tuple(sorted(orb)))
    unseen-=orb
assert len(CUBIC_ORBITS)==399

# Exact rational cubic solution reconstructed from the unique Noether system.
CUBIC={
72:F('-1/2'),75:F('1/2'),83:F('1/2'),84:F('1/2'),86:F('-1/2'),88:F('-1/4'),
90:F('-1/2'),91:F('1/4'),98:F('1/2'),100:F('-1/2'),127:F('1/8'),128:F('-1/8'),
135:F('3/4'),137:F('1/8'),138:F('-1/2'),139:F('-1/8'),142:F('1/2'),145:F('-3/4'),
152:F('-3/4'),155:F('1/2'),156:F('-1/2'),158:F('-1/2'),159:F('1/2'),162:F('3/2'),
201:F('1/2'),202:F('1/4'),209:F('-1'),210:F('-1/2'),214:F('-1/2'),218:F('1/2'),
224:F('1/2'),226:F('1/2'),234:F('1/2'),239:F('1/2'),240:F('-1/2'),244:F('-1/2'),
248:F('-1/2'),249:F('-1/2'),256:F('1'),257:F('1/2'),261:F('1/2'),265:F('-1/2'),
267:F('-1/2'),269:F('-1/2'),275:F('-1'),277:F('-1/2'),278:F('1/2'),281:F('1'),
286:F('-1/2'),288:F('-1/2'),291:F('-1/2'),296:F('-1/2'),298:F('1/2'),300:F('1'),
305:F('1/2'),306:F('1'),311:F('1'),314:F('1/2'),315:F('1'),316:F('1/2'),
317:F('-1/2'),318:F('-3/2'),320:F('-1'),339:F('1/2'),341:F('1'),343:F('-1/2'),
345:F('-1'),355:F('-1/2'),356:F('-1'),359:F('1/2'),360:F('1'),387:F('1/2'),
388:F('-1/2'),394:F('-1/2'),395:F('1')}
assert len(CUBIC)==75

# Polynomial helpers in independent momenta p0..p3,q0..q3; r=-p-q.
def lin_var(idx,coef=F(1)):
    e=[0]*8; e[idx]=1
    return {tuple(e):coef}
def padd(*args):
    d=defaultdict(Fraction)
    for a in args:
        for e,c in a.items(): d[e]+=c
    return {e:c for e,c in d.items() if c}
def pmul(a,b):
    d=defaultdict(Fraction)
    for e,c in a.items():
        for f,v in b.items():
            d[tuple(e[i]+f[i] for i in range(8))]+=c*v
    return {e:c for e,c in d.items() if c}

def pscale(a,s): return {e:s*c for e,c in a.items() if s*c}

P=[lin_var(i) for i in range(4)]
Q=[lin_var(4+i) for i in range(4)]
R=[padd(pscale(P[i],-1),pscale(Q[i],-1)) for i in range(4)]
K=[P,Q,R]

# Gauge component of a symmetric field index: delta0 h_ij=p_i xi_j+p_j xi_i.
def gauge_component(a):
    i,j=FIELDS[a]; out={}
    out[j]=padd(out.get(j,{}),P[i])
    out[i]=padd(out.get(i,{}),P[j])
    return out

# delta0 S3 coefficient dictionary keyed by (xi_mu,B_b,C_c,momentum_exponent).
ACT=defaultdict(Fraction)
for oi,cc in CUBIC.items():
    for a,b,c,i,j in CUBIC_ORBITS[oi]:
        for perm in LEG_PERMS:
            ext=[perm[0],perm[1],perm[2]] # 0=gauge A,1=B,2=C
            fslots=[a,b,c]
            Afield=fslots[ext.index(0)]
            Bidx=fslots[ext.index(1)]
            Cidx=fslots[ext.index(2)]
            d1=K[ext[1]][i]; d2=K[ext[2]][j]
            for mu,gp in gauge_component(Afield).items():
                pol=pmul(pmul(gp,d1),d2)
                for e,v in pol.items(): ACT[(mu,Bidx,Cidx,e)]+=cc*v
ACT={k:v for k,v in ACT.items() if v}

# Deterministic quadratic Hessian orbits and already selected QGR-L1 coefficients.
def canon_q(a,b,i,j):
    if a>b:a,b=b,a
    if i>j:i,j=j,i
    return (a,b,i,j)
def pterm_q(t,p):
    a,b,i,j=t
    return canon_q(pf(a,p),pf(b,p),p[i],p[j])
qterms={(a,b,i,j) for a in range(10) for b in range(a,10) for i in V for j in range(i,4)}
unseen=set(qterms); QORB=[]
while unseen:
    t=min(unseen); orb={pterm_q(t,p) for p in PERMS}; QORB.append(tuple(sorted(orb))); unseen-=orb
assert len(QORB)==38
QCOEF={14:F('1/2'),15:F('1/2'),20:F('-1'),21:F('-1/2'),22:F('1/2'),26:F('-1'),
27:F('-1'),32:F('1'),33:F('1/2'),34:F('-1/2'),36:F('-1'),37:F('1/2')}


def Hpoly(Kmom):
    H=[[{} for _ in range(10)] for __ in range(10)]
    for oi,cc in QCOEF.items():
        for a,b,i,j in QORB[oi]:
            pol=pscale(pmul(Kmom[i],Kmom[j]),cc)
            H[a][b]=padd(H[a][b],pol)
            if a!=b:H[b][a]=padd(H[b][a],pol)
    return H
HQ=Hpoly(Q); HR=Hpoly(R)

# C^{ij}=J-I, used to raise the relational-frame parameter in delta1.
CUP=[[0 if i==j else 1 for j in V] for i in V]

def delta1_coeffs(hK):
    D=[[[{} for _ in V] for __ in range(10)] for ___ in range(10)]
    for a,(i,j) in enumerate(FIELDS):
        # xi^k D_k h_ij
        for mu in V:
            pol={}
            for k in V:
                if CUP[k][mu]: pol=padd(pol,hK[k])
            D[a][a][mu]=padd(D[a][a][mu],pol)
        # h_kj D_i xi^k + h_ik D_j xi^k
        for k in V:
            b=FINDEX[tuple(sorted((k,j)))]
            for mu in V:
                if CUP[k][mu]: D[a][b][mu]=padd(D[a][b][mu],P[i])
            b=FINDEX[tuple(sorted((i,k)))]
            for mu in V:
                if CUP[k][mu]: D[a][b][mu]=padd(D[a][b][mu],P[j])
    return D
DQ=delta1_coeffs(Q); DR=delta1_coeffs(R)

# delta1 S2 source dictionary for external ordering xi(p),B(q),C(r).
SRC=defaultdict(Fraction)
for Cidx in range(10):
    for out in range(10):
        hp=HR[Cidx][out]
        if not hp: continue
        for Bidx in range(10):
            for mu in V:
                dp=DQ[out][Bidx][mu]
                if dp:
                    for e,v in pmul(hp,dp).items(): SRC[(mu,Bidx,Cidx,e)]+=v
for Bidx in range(10):
    for out in range(10):
        hp=HQ[Bidx][out]
        if not hp: continue
        for Cidx in range(10):
            for mu in V:
                dp=DR[out][Cidx][mu]
                if dp:
                    for e,v in pmul(hp,dp).items(): SRC[(mu,Bidx,Cidx,e)]+=v
SRC={k:v for k,v in SRC.items() if v}

# Exact coefficient-wise Noether identity.
assert len(ACT)==len(SRC)==8376
keys=set(ACT)|set(SRC)
residual={k:ACT.get(k,F(0))+SRC.get(k,F(0)) for k in keys}
residual={k:v for k,v in residual.items() if v}
assert residual=={}

print({
    'raw_cubic_orbits':399,
    'nonzero_rational_solution_coefficients':len(CUBIC),
    'solution_denominators':sorted({c.denominator for c in CUBIC.values()}),
    'expanded_noether_coefficients_each_side':8376,
    'nonzero_exact_residual_coefficients':0,
    'identity':'delta0 S3 + delta1 S2 == 0',
    'classification':'PASS_SCOPED_EXACT_RATIONAL_CUBIC_NOETHER_CERTIFICATE',
    'guard':'quartic/all-orders completion remains open',
})
