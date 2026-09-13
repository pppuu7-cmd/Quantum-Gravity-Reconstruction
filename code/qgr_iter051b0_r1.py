#!/usr/bin/env python3
import argparse,json,numpy as np
import qgr_iter051b0_double_divergence_operator as b

N=b.N

def transform_jets(jets,L):
    A,H,P0,PL,PQ=jets; M=np.linalg.inv(L)
    A2=np.einsum('ck,ai,bj,cab->kij',M,M,M,A)
    H2=np.einsum('ck,dl,ai,bj,cdab->klij',M,M,M,M,H)
    P02=np.einsum('ia,mj,kb,nl,ajbl->imkn',L,L,L,L,P0)
    PL2=np.einsum('cr,ia,mj,kb,nl,cajbl->rimkn',M,L,L,L,L,PL)
    PQ2=np.einsum('cr,ds,ia,mj,kb,nl,cdajbl->rsimkn',M,M,L,L,L,L,PQ)
    return A2,H2,P02,PL2,PQ2

def direct_P(P,L):
    out=np.zeros_like(P)
    for i in range(N):
      for m in range(N):
       for k in range(N):
        for n in range(N):
         s=0.0
         for a in range(N):
          for j in range(N):
           for q in range(N):
            for l in range(N): s+=L[i,a]*L[m,j]*L[k,q]*L[n,l]*P[a,j,q,l]
         out[i,m,k,n]=s
    return out

def run(lane):
    seed=51000+137*lane; jets=b.make_jets(seed); hs=[2e-3,1e-3,5e-4]
    dets=[]; invres=[]
    for h in hs:
      for c in range(N):
       for sg in (-1,1):
        x=np.zeros(N); x[c]=sg*h; g=b.samples(jets,x)[0]; gi=np.linalg.inv(g)
        dets.append(np.linalg.det(g)); invres.append(np.max(np.abs(g@gi-np.eye(N))))
    Da,_,_,P0=b.analytic_D(jets); nums=[b.numeric_D(jets,h) for h in hs]; errs=[b.relnorm(x,Da) for x in nums]
    cov=[]; pctrl=[]; lor=[]
    for L in (b.boost(0.17), b.boost(-0.13)@b.rot(0.29)):
      jt=transform_jets(jets,L)
      pctrl.append(b.relnorm(jt[2],direct_P(P0,L),floor=1e-14))
      lor.append(float(np.max(np.abs(L.T@b.ETA@L-b.ETA))))
      Dt=b.analytic_D(jt)[0]
      expected=np.einsum('ia,jb,ab->ij',L,L,Da)
      cov.append(b.relnorm(Dt,expected))
    valid=(max(dets)<0 and max(invres)<=1e-11 and b.psym(P0)<=1e-11 and np.linalg.norm(Da)>=1e-8 and np.linalg.norm(nums[-1])>=1e-8 and max(pctrl)<=1e-12 and max(lor)<=1e-12)
    refine=(errs[-1] <= 1.20*errs[-2]) or (np.linalg.norm(nums[-1]-Da)<=2e-8)
    passed=valid and errs[-1]<=3e-5 and refine and max(cov)<=3e-7
    out={'lane':lane,'seed':seed,'valid':bool(valid),'pass':bool(passed),'analytic_norm':float(np.linalg.norm(Da)),'numeric_norm_finest':float(np.linalg.norm(nums[-1])),'relative_errors':errs,'refinement_ok':bool(refine),'covariance_residuals':cov,'P_transform_control_residuals':pctrl,'lorentz_metric_residuals':lor,'max_inverse_residual':float(max(invres)),'max_metric_det':float(max(dets)),'P_symmetry_residual':b.psym(P0)}
    print(json.dumps(out,sort_keys=True))
    if not passed: raise SystemExit(2)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); args=ap.parse_args(); run(args.lane)
