#!/usr/bin/env python3
import argparse, json, math
import numpy as np

import qgr_iter051b0_double_divergence_operator as b
import qgr_iter051b0_r1 as r1
import qgr_iter051b1_weyl3_p_insertion as w3

N=4
HP=(1e-3,5e-4,2.5e-4)
HD=(2e-3,1e-3,5e-4)


def make_fields(seed):
    rng=np.random.default_rng(seed)
    A=np.array([b.sym2(rng.normal(size=(N,N))) for _ in range(N)])*0.004
    H=np.empty((N,N,N,N))
    for c in range(N):
      for d in range(N): H[c,d]=b.sym2(rng.normal(size=(N,N)))
    H=0.5*(H+H.swapaxes(0,1))*0.004
    R0=w3.riemann_from_q(w3.make_q(seed+11,0.10))
    RL=np.array([w3.riemann_from_q(w3.make_q(seed+101+17*c,0.035)) for c in range(N)])
    RQ=np.empty((N,N,N,N,N,N))
    for c in range(N):
      for d in range(N): RQ[c,d]=w3.riemann_from_q(w3.make_q(seed+501+31*c+43*d,0.018))
    RQ=0.5*(RQ+RQ.swapaxes(0,1))
    return A,H,R0,RL,RQ


def metric_at(A,H,x):
    x=np.asarray(x,float); g=b.ETA.copy()
    for c in range(N): g += A[c]*x[c]
    for c in range(N):
      for d in range(N): g += 0.5*H[c,d]*x[c]*x[d]
    dg=np.empty((N,N,N))
    for c in range(N):
      dg[c]=A[c].copy()
      for d in range(N): dg[c]+=H[c,d]*x[d]
    return g,dg


def curvature_at(R0,RL,RQ,x):
    x=np.asarray(x,float); R=R0.copy()
    for c in range(N): R += RL[c]*x[c]
    for c in range(N):
      for d in range(N): R += 0.5*RQ[c,d]*x[c]*x[d]
    return R


def P_actual(fields,x):
    A,H,R0,RL,RQ=fields
    g,_=metric_at(A,H,x); gi=np.linalg.inv(g)
    R=curvature_at(R0,RL,RQ,x)
    return w3.project_algebraic_riemann(w3.complex_step_gradient(R,g,gi))


def extract_P_jets(fields,h):
    z=np.zeros(N); P0=P_actual(fields,z)
    PL=np.empty((N,N,N,N,N))
    PQ=np.empty((N,N,N,N,N,N))
    axes=[]
    for c in range(N):
      e=np.zeros(N); e[c]=h; axes.append(e)
      pp=P_actual(fields,e); pm=P_actual(fields,-e)
      PL[c]=w3.project_algebraic_riemann((pp-pm)/(2*h))
      PQ[c,c]=w3.project_algebraic_riemann((pp-2*P0+pm)/(h*h))
    for c in range(N):
      for d in range(c+1,N):
        ec,ed=axes[c],axes[d]
        val=(P_actual(fields,ec+ed)-P_actual(fields,ec-ed)-P_actual(fields,-ec+ed)+P_actual(fields,-ec-ed))/(4*h*h)
        val=w3.project_algebraic_riemann(val)
        PQ[c,d]=val; PQ[d,c]=val
    return P0,PL,PQ


def first_div_actual(fields,x,h):
    A,H,_,_,_=fields
    g,dg=metric_at(A,H,x); _,G,_=b.conn(g,dg)
    P0=P_actual(fields,x)
    dP=np.empty((N,N,N,N,N))
    for c in range(N):
      e=np.zeros(N); e[c]=h
      dP[c]=(P_actual(fields,x+e)-P_actual(fields,x-e))/(2*h)
    S=b.first_cov(P0,dP,G)
    return np.einsum('aambn->mbn',S)


def direct_D(fields,h):
    A,H,_,_,_=fields; z=np.zeros(N)
    g,dg=metric_at(A,H,z); _,G,_=b.conn(g,dg)
    R0=first_div_actual(fields,z,h)
    D=np.zeros((N,N))
    for bb in range(N):
      e=np.zeros(N); e[bb]=h
      dR=(first_div_actual(fields,e,h)-first_div_actual(fields,-e,h))/(2*h)
      D += dR[:,bb,:]
      for m in range(N):
       for n in range(N):
        for rr in range(N):
          D[m,n]+=G[m,bb,rr]*R0[rr,bb,n]+G[bb,bb,rr]*R0[m,rr,n]+G[n,bb,rr]*R0[m,bb,rr]
    return D


def relnorm(A,B,floor=1e-14):
    return float(np.linalg.norm(A-B)/max(np.linalg.norm(A),np.linalg.norm(B),floor))


def pjet_alg_res(P0,PL,PQ):
    vals=[w3.algebraic_residual(P0)]
    vals += [w3.algebraic_residual(PL[c]) for c in range(N)]
    vals += [w3.algebraic_residual(PQ[c,d]) for c in range(N) for d in range(N)]
    return float(max(vals))


def direct_P0_covariance(fields,L):
    A,H,R0,RL,RQ=fields
    P0=P_actual(fields,np.zeros(N))
    Rt=w3.transform_cov4(R0,L)
    gt=L.T@b.ETA@L; git=np.linalg.inv(gt)
    Pt=w3.project_algebraic_riemann(w3.complex_step_gradient(Rt,gt,git))
    expected=w3.transform_contra4(P0,L)
    return relnorm(Pt,expected)


def run(lane):
    seed=72001+173*lane
    fields=make_fields(seed); A,H,R0,RL,RQ=fields

    dets=[]; invs=[]
    for h in (max(HD),max(HP)):
      for c in range(N):
       for sg in (-1,1):
        x=np.zeros(N); x[c]=sg*h
        g,_=metric_at(A,H,x); gi=np.linalg.inv(g)
        dets.append(float(np.linalg.det(g)))
        invs.append(float(np.max(np.abs(g@gi-np.eye(N)))))

    extracted=[]; Drefs=[]; palg=[]
    for h in HP:
      P0,PL,PQ=extract_P_jets(fields,h)
      jets=(A,H,P0,PL,PQ)
      Drefs.append(b.analytic_D(jets)[0])
      extracted.append(jets)
      palg.append(pjet_alg_res(P0,PL,PQ))
    Dref=Drefs[-1]
    pref_conv=relnorm(Drefs[-1],Drefs[-2])

    directs=[direct_D(fields,h) for h in HD]
    direct_errs=[relnorm(D,Dref) for D in directs]
    direct_step=relnorm(directs[-1],directs[-2])

    cov=[]; p0cov=[]
    finest=extracted[-1]
    for L in (b.boost(0.17), b.boost(-0.13)@b.rot(0.29)):
      jt=r1.transform_jets(finest,L)
      Dt=b.analytic_D(jt)[0]
      expected=np.einsum('ia,jb,ab->ij',L,L,Dref)
      cov.append(relnorm(Dt,expected))
      p0cov.append(direct_P0_covariance(fields,L))

    zero_fields=(A,H,np.zeros_like(R0),np.zeros_like(RL),np.zeros_like(RQ))
    zero_p_norm=float(np.linalg.norm(P_actual(zero_fields,np.zeros(N))))

    valid=(max(dets)<0 and max(invs)<=1e-11 and max(palg)<=2e-10 and
           np.linalg.norm(Dref)>1e-6 and np.linalg.norm(directs[-1])>1e-6 and
           zero_p_norm<=2e-10)
    passed=(valid and pref_conv<=2e-5 and direct_errs[-1]<=2e-5 and
            direct_step<=1e-5 and max(cov)<=2e-7 and max(p0cov)<=2e-9)

    out={
      'gate':'ITER051B2-WEYL3-P-CONNECTION-RESPONSE',
      'lane':lane,'seed':seed,'valid':bool(valid),'pass':bool(passed),
      'D_reference_norm':float(np.linalg.norm(Dref)),
      'D_direct_finest_norm':float(np.linalg.norm(directs[-1])),
      'P_jet_reference_convergence':pref_conv,
      'direct_vs_reference_residuals':direct_errs,
      'direct_final_step_change':direct_step,
      'D_covariance_residuals':cov,
      'P0_direct_covariance_residuals':p0cov,
      'P_jet_algebraic_residuals':palg,
      'zero_curvature_P_norm':zero_p_norm,
      'max_inverse_residual':float(max(invs)),
      'max_metric_det':float(max(dets)),
    }
    print(json.dumps(out,sort_keys=True))
    if not passed: raise SystemExit(2)


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True)
    args=ap.parse_args(); run(args.lane)
