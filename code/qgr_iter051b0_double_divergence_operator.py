#!/usr/bin/env python3
import argparse, json, math
import numpy as np

ETA=np.diag([-1.,1.,1.,1.]); N=4

def sym2(x): return 0.5*(x+x.T)
def projP(T):
    A=0.25*(T-T.swapaxes(0,1)-T.swapaxes(2,3)+T.swapaxes(0,1).swapaxes(2,3))
    return 0.5*(A+A.transpose(2,3,0,1))

def make_jets(seed):
    rng=np.random.default_rng(seed)
    A=np.array([sym2(rng.normal(size=(N,N))) for _ in range(N)])*0.006
    H=np.empty((N,N,N,N))
    for k in range(N):
      for l in range(N): H[k,l]=sym2(rng.normal(size=(N,N)))
    H=0.5*(H+H.swapaxes(0,1))*0.006
    P0=projP(rng.normal(size=(N,N,N,N)))*0.08
    PL=np.array([projP(rng.normal(size=(N,N,N,N))) for _ in range(N)])*0.05
    PQ=np.empty((N,N,N,N,N,N))
    for k in range(N):
      for l in range(N): PQ[k,l]=projP(rng.normal(size=(N,N,N,N)))*0.04
    PQ=0.5*(PQ+PQ.swapaxes(0,1))
    return A,H,P0,PL,PQ

def samples(jets,x):
    A,H,P0,PL,PQ=jets; x=np.asarray(x)
    g=ETA.copy()
    for k in range(N): g+=A[k]*x[k]
    for k in range(N):
      for l in range(N): g+=0.5*H[k,l]*x[k]*x[l]
    dg=np.empty((N,N,N)); ddg=H.copy()
    for c in range(N):
      dg[c]=A[c]
      for l in range(N): dg[c]+=H[c,l]*x[l]
    P=P0.copy()
    for k in range(N): P+=PL[k]*x[k]
    for k in range(N):
      for l in range(N): P+=0.5*PQ[k,l]*x[k]*x[l]
    dP=np.empty((N,N,N,N,N)); ddP=PQ.copy()
    for c in range(N):
      dP[c]=PL[c]
      for l in range(N): dP[c]+=PQ[c,l]*x[l]
    return g,dg,ddg,P,dP,ddP

def conn(g,dg,ddg=None):
    gi=np.linalg.inv(g); G=np.zeros((N,N,N)); dG=None
    for u in range(N):
      for c in range(N):
       for v in range(N):
        for s in range(N): G[u,c,v]+=0.5*gi[u,s]*(dg[c,v,s]+dg[v,c,s]-dg[s,c,v])
    if ddg is not None:
      dgi=np.array([-gi@dg[d]@gi for d in range(N)])
      dG=np.zeros((N,N,N,N))
      for d in range(N):
       for u in range(N):
        for c in range(N):
         for v in range(N):
          for s in range(N):
           aa=dg[c,v,s]+dg[v,c,s]-dg[s,c,v]
           daa=ddg[d,c,v,s]+ddg[d,v,c,s]-ddg[d,s,c,v]
           dG[d,u,c,v]+=0.5*(dgi[d,u,s]*aa+gi[u,s]*daa)
    return gi,G,dG

def first_cov(P,dP,G):
    S=np.zeros((N,N,N,N,N))
    for c in range(N):
     S[c]=dP[c]
     S[c]+=np.einsum('ar,rmbn->ambn',G[:,c,:],P)
     S[c]+=np.einsum('mr,arbn->ambn',G[:,c,:],P)
     S[c]+=np.einsum('br,amrn->ambn',G[:,c,:],P)
     S[c]+=np.einsum('nr,ambr->ambn',G[:,c,:],P)
    return S

def analytic_D(jets):
    g,dg,ddg,P,dP,ddP=samples(jets,np.zeros(N)); gi,G,dG=conn(g,dg,ddg)
    S=first_cov(P,dP,G)
    R=np.einsum('aambn->mbn',S)
    dS=np.zeros((N,N,N,N,N,N))
    for d in range(N):
     for c in range(N):
      X=ddP[d,c].copy()
      for pos in range(4):
       if pos==0:
        X+=np.einsum('ar,rmbn->ambn',dG[d,:,c,:],P)+np.einsum('ar,rmbn->ambn',G[:,c,:],dP[d])
       elif pos==1:
        X+=np.einsum('mr,arbn->ambn',dG[d,:,c,:],P)+np.einsum('mr,arbn->ambn',G[:,c,:],dP[d])
       elif pos==2:
        X+=np.einsum('br,amrn->ambn',dG[d,:,c,:],P)+np.einsum('br,amrn->ambn',G[:,c,:],dP[d])
       else:
        X+=np.einsum('nr,ambr->ambn',dG[d,:,c,:],P)+np.einsum('nr,ambr->ambn',G[:,c,:],dP[d])
      dS[d,c]=X
    D=np.zeros((N,N))
    for m in range(N):
     for n in range(N):
      val=0.0
      for b in range(N):
       for a in range(N): val+=dS[b,a,a,m,b,n]
       for r in range(N):
        val+=G[m,b,r]*R[r,b,n]+G[b,b,r]*R[m,r,n]+G[n,b,r]*R[m,b,r]
      D[m,n]=val
    return D,gi,G,P

def numeric_R(jets,x,h):
    g,dg,_,P,_,_=samples(jets,x); _,G,_=conn(g,dg)
    dP=np.zeros((N,N,N,N,N))
    for c in range(N):
      e=np.zeros(N); e[c]=h
      Pp=samples(jets,x+e)[3]; Pm=samples(jets,x-e)[3]
      dP[c]=(Pp-Pm)/(2*h)
    S=first_cov(P,dP,G)
    return np.einsum('aambn->mbn',S)

def numeric_D(jets,h):
    x=np.zeros(N); g,dg,_,_,_,_=samples(jets,x); gi,G,_=conn(g,dg)
    R0=numeric_R(jets,x,h)
    D=np.zeros((N,N))
    for b in range(N):
      e=np.zeros(N); e[b]=h
      Rp=numeric_R(jets,e,h); Rm=numeric_R(jets,-e,h)
      dR=(Rp-Rm)/(2*h)
      D+=dR[:,b,:]
      for m in range(N):
       for n in range(N):
        for r in range(N): D[m,n]+=G[m,b,r]*R0[r,b,n]+G[b,b,r]*R0[m,r,n]+G[n,b,r]*R0[m,b,r]
    return D

def boost(v):
    ga=1/math.sqrt(1-v*v); L=np.eye(N); L[0,0]=ga; L[1,1]=ga; L[0,1]=-ga*v; L[1,0]=-ga*v; return L

def rot(th):
    L=np.eye(N); c=math.cos(th); s=math.sin(th); L[2,2]=c; L[2,3]=-s; L[3,2]=s; L[3,3]=c; return L

def transform_jets(jets,L):
    A,H,P0,PL,PQ=jets; M=np.linalg.inv(L)
    A2=np.einsum('ck,ai,bj,cab->kij',M,M,M,A)
    H2=np.einsum('ck,dl,ai,bj,cdab->klij',M,M,M,M,H)
    P02=np.einsum('ia,jm,kb,ln,ajbl->imkn',L,L,L,L,P0)
    PL2=np.einsum('cr,ia,jm,kb,ln,cajbl->rimkn',M,L,L,L,L,PL)
    PQ2=np.einsum('cr,ds,ia,jm,kb,ln,cdajbl->rsimkn',M,M,L,L,L,L,PQ)
    return A2,H2,P02,PL2,PQ2

def relnorm(A,B,floor=1e-14): return float(np.linalg.norm(A-B)/max(np.linalg.norm(A),np.linalg.norm(B),floor))

def psym(P):
    return float(max(np.max(np.abs(P+P.swapaxes(0,1))),np.max(np.abs(P+P.swapaxes(2,3))),np.max(np.abs(P-P.transpose(2,3,0,1)))))

def run(lane):
    seed=51000+137*lane; jets=make_jets(seed); hs=[2e-3,1e-3,5e-4]
    dets=[]; invres=[]
    for h in hs:
      for c in range(N):
       for sg in (-1,1):
        x=np.zeros(N); x[c]=sg*h; g=samples(jets,x)[0]; gi=np.linalg.inv(g)
        dets.append(np.linalg.det(g)); invres.append(np.max(np.abs(g@gi-np.eye(N))))
    Da,_,_,P0=analytic_D(jets); nums=[numeric_D(jets,h) for h in hs]; errs=[relnorm(x,Da) for x in nums]
    cov=[]
    for L in (boost(0.17), boost(-0.13)@rot(0.29)):
      jt=transform_jets(jets,L); Dt=analytic_D(jt)[0]; expected=np.einsum('ia,jb,ab->ij',L,L,Da); cov.append(relnorm(Dt,expected))
    valid=(max(dets)<0 and max(invres)<=1e-11 and psym(P0)<=1e-11 and np.linalg.norm(Da)>=1e-8 and np.linalg.norm(nums[-1])>=1e-8)
    refine=(errs[-1] <= 1.20*errs[-2]) or (np.linalg.norm(nums[-1]-Da)<=2e-8)
    passed=valid and errs[-1]<=3e-5 and refine and max(cov)<=3e-7
    out={'lane':lane,'seed':seed,'valid':bool(valid),'pass':bool(passed),'analytic_norm':float(np.linalg.norm(Da)),'numeric_norm_finest':float(np.linalg.norm(nums[-1])),'relative_errors':errs,'refinement_ok':bool(refine),'covariance_residuals':cov,'max_inverse_residual':float(max(invres)),'max_metric_det':float(max(dets)),'P_symmetry_residual':psym(P0)}
    print(json.dumps(out,sort_keys=True))
    if not passed: raise SystemExit(2)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); args=ap.parse_args(); run(args.lane)
