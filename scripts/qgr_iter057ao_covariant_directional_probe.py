#!/usr/bin/env python3
"""Iter057AO phase-1 exact covariant Weyl^3 directional-density probe.

Non-terminal implementation step under the frozen AO preregistration.  It builds
metric 2-jets and symmetric direction 2-jets at one coordinate point, derives
Levi-Civita/Riemann/Ricci/scalar/Weyl source-faithfully, and differentiates the
Weyl-cubic density exactly with SymPy.  It intentionally does NOT claim the
frozen compact-support/IBP Noether control; terminal AO classification is
therefore forbidden from this script alone.
"""
import hashlib, json
from sympy import Matrix, Rational, symbols, diff, simplify, sqrt

N=4
eps,c6=symbols('eps c6')
SEED='ITER057AO-COVARIANT-WEYL3-V1'
HELD='ITER057AO-COVARIANT-WEYL3-HELDOUT-V1'

def q(seed,*idx,mod=11):
    b=(seed+':' + ':'.join(map(str,idx))).encode(); n=int(hashlib.sha256(b).hexdigest()[:16],16)
    return Rational((n%(2*mod+1))-mod, 13)

def jets(seed):
    # g_ab, first derivatives g_ab,c, second derivatives g_ab,cd; h analogues.
    g=[[Rational(0) for _ in range(N)] for _ in range(N)]
    h=[[Rational(0) for _ in range(N)] for _ in range(N)]
    dg=[[[Rational(0) for _ in range(N)] for _ in range(N)] for _ in range(N)]
    dh=[[[Rational(0) for _ in range(N)] for _ in range(N)] for _ in range(N)]
    ddg=[[[[Rational(0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    ddh=[[[[Rational(0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a in range(N):
      for b in range(a,N):
        gv=(Rational(-1 if a==0 else 1) if a==b else 0)+q(seed,'g',a,b,mod=2)/20
        hv=q(seed,'h',a,b,mod=5)
        g[a][b]=g[b][a]=gv; h[a][b]=h[b][a]=hv
        for c in range(N):
          v=q(seed,'dg',a,b,c,mod=4)/7; w=q(seed,'dh',a,b,c,mod=4)/7
          dg[a][b][c]=dg[b][a][c]=v; dh[a][b][c]=dh[b][a][c]=w
          for d in range(c,N):
            v=q(seed,'ddg',a,b,c,d,mod=4)/9; w=q(seed,'ddh',a,b,c,d,mod=4)/9
            ddg[a][b][c][d]=ddg[a][b][d][c]=ddg[b][a][c][d]=ddg[b][a][d][c]=v
            ddh[a][b][c][d]=ddh[a][b][d][c]=ddh[b][a][c][d]=ddh[b][a][d][c]=w
    return g,h,dg,dh,ddg,ddh

def density(seed):
    g,h,dg,dh,ddg,ddh=jets(seed)
    G=Matrix([[g[a][b]+eps*h[a][b] for b in range(N)] for a in range(N)])
    Gi=G.inv()
    D=lambda a,b,c: dg[a][b][c]+eps*dh[a][b][c]
    DD=lambda a,b,c,d: ddg[a][b][c][d]+eps*ddh[a][b][c][d]
    # lower-index Christoffel Gamma_{abc}=1/2(g_ab,c+g_ac,b-g_bc,a)
    Gam=[[[ (D(a,b,c)+D(a,c,b)-D(b,c,a))/2 for c in range(N)] for b in range(N)] for a in range(N)]
    # R_abcd = 1/2(g_ad,bc+g_bc,ad-g_ac,bd-g_bd,ac) + g^ef(G_ead G_fbc-G_eac G_fbd)
    R=[[[[Rational(0) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    for a in range(N):
      for b in range(N):
       for c in range(N):
        for d in range(N):
         x=(DD(a,d,b,c)+DD(b,c,a,d)-DD(a,c,b,d)-DD(b,d,a,c))/2
         x+=sum(Gi[e,f]*(Gam[e][a][d]*Gam[f][b][c]-Gam[e][a][c]*Gam[f][b][d]) for e in range(N) for f in range(N))
         R[a][b][c][d]=x
    Ric=[[sum(Gi[a,c]*R[a][b][c][d] for a in range(N) for c in range(N)) for d in range(N)] for b in range(N)]
    Scal=sum(Gi[b,d]*Ric[b][d] for b in range(N) for d in range(N))
    C=[[[[Rational(0) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    for a in range(N):
      for b in range(N):
       for c in range(N):
        for d in range(N):
         C[a][b][c][d]=R[a][b][c][d]-(G[a,c]*Ric[d][b]-G[a,d]*Ric[c][b]-G[b,c]*Ric[d][a]+G[b,d]*Ric[c][a])/2 + Scal*(G[a,c]*G[d,b]-G[a,d]*G[c,b])/6
    # C_ab^cd and trace control C_ab^ad.
    Cup=[[[[sum(Gi[c,e]*Gi[d,f]*C[a][b][e][f] for e in range(N) for f in range(N)) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    tr=[simplify(sum(Cup[a][b][a][d] for a in range(N))) for b in range(N) for d in range(N)]
    I=sum(Cup[a][b][c][d]*Cup[c][d][e][f]*Cup[e][f][a][b] for a in range(N) for b in range(N) for c in range(N) for d in range(N) for e in range(N) for f in range(N))
    L=c6*sqrt(-G.det())*I
    dL=simplify(diff(L,eps).subs(eps,0)/c6)
    return G.det().subs(eps,0), all(simplify(x.subs(eps,0))==0 for x in tr), dL

def main():
    manifest={'gate':'ITER057AO','phase':'PHASE1_NONTERMINAL_COVARIANT_DENSITY_PROBE','seed':SEED,'heldout_seed':HELD,'arithmetic':'exact_rational_symbolic','dimension':4}
    manifest_sha=hashlib.sha256(json.dumps(manifest,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    out={'manifest':manifest,'manifest_sha256':manifest_sha,'terminal_classification_authorized':False}
    for label,seed in [('generic',SEED),('heldout',HELD)]:
        detg,trace_ok,dL=density(seed)
        out[label]={'det_g':str(detg),'invertible':detg!=0,'weyl_trace_exact':trace_ok,'directional_density_nonzero':dL!=0,'directional_density_sha256':hashlib.sha256(str(dL).encode()).hexdigest(),'directional_density_chars':len(str(dL))}
    out['classification']='PARTIAL_EXACT_ITER057AO_SOURCE_LEVEL_COVARIANT_DENSITY_DIRECTIONAL_PROBE__NO_TERMINAL_PASS'
    raw=json.dumps(out,sort_keys=True,separators=(',',':')); out['scientific_payload_sha256']=hashlib.sha256(raw.encode()).hexdigest()
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=='__main__': main()
