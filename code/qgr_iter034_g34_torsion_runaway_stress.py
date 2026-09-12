#!/usr/bin/env python3
"""QGR Iter034: nonlinear torsion branch stress test.

Uses the same C, o(C) basis and conformal finite-curvature frame family as Iter006 G9.
This is a scoped numerical search, never a global theorem.
"""
import argparse,json,math,os
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

C=np.array([[0.,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
B=np.array([
    [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
    [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
    [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
    [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
    [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
    [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
],dtype=float)
a=np.array([0.22,-0.17,0.13,0.09])
Q=np.array([[0,0.05,-0.02,0.03],[0.05,0,0.04,-0.01],[-0.02,0.04,0,0.02],[0.03,-0.01,0.02,0]])
I=np.eye(4)
assert max(np.linalg.norm(X.T@C+C@X) for X in B)<1e-12

def Omega(x,gamma=1.0):
    x=np.asarray(x,dtype=float)
    return math.exp(float(gamma*(a@x+0.5*x@Q@x)))

def L_from(p6): return expm(np.tensordot(p6,B,axes=(0,0)))

def residual(x,z,gamma=1.0):
    x=np.asarray(x,dtype=int); Om=Omega(x,gamma)
    try: L=[L_from(z[6*i:6*i+6]) for i in range(4)]
    except Exception: return np.full(24,1e100)
    out=[]
    for i in range(4):
        for j in range(i+1,4):
            xi=x.copy(); xi[i]+=1; xj=x.copy(); xj[j]+=1
            try:
                lhs=Om*I[:,i]+np.linalg.solve(L[i],Omega(xi,gamma)*I[:,j])
                rhs=Om*I[:,j]+np.linalg.solve(L[j],Omega(xj,gamma)*I[:,i])
                r=lhs-rhs
            except Exception:
                r=np.full(4,1e100)
            if not np.all(np.isfinite(r)): r=np.full(4,1e100)
            out.extend(r)
    return np.asarray(out,dtype=float)

def solve(z0,gamma=1.0,max_nfev=1200):
    try:
        return least_squares(lambda z: residual(np.zeros(4,dtype=int),z,gamma),z0,
            xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=max_nfev)
    except Exception as e:
        return None

def transport_vector(z):
    mats=[L_from(z[6*i:6*i+6]) for i in range(4)]
    return np.concatenate([M.ravel() for M in mats])

def summarize_solution(sol,ref_transport=None):
    if sol is None:
        return {'success':False,'exception_or_solver_failure':True}
    rn=float(np.linalg.norm(sol.fun)) if np.all(np.isfinite(sol.fun)) else float('inf')
    good=bool(rn<1e-7 and np.all(np.isfinite(sol.x)))
    out={'success':good,'residual_norm':rn,'parameter_norm':float(np.linalg.norm(sol.x)),
         'nfev':int(sol.nfev),'optimizer_success_flag':bool(sol.success)}
    if good:
        sv=np.linalg.svd(sol.jac,compute_uv=False)
        out['jacobian_min_singular']=float(sv.min())
        out['jacobian_condition']=float(sv.max()/sv.min()) if sv.min()>0 else float('inf')
        tv=transport_vector(sol.x)
        out['transport_norm']=float(np.linalg.norm(tv))
        if ref_transport is not None:
            out['transport_distance_from_reference']=float(np.linalg.norm(tv-ref_transport))
    return out

def reference():
    r=solve(np.zeros(24),1.0,1500)
    if r is None or np.linalg.norm(r.fun)>=1e-8: raise RuntimeError('reference G9 root failed')
    return r,transport_vector(r.x)

def large_start(lane):
    ref,rt=reference(); rng=np.random.default_rng(34000+lane)
    d=rng.normal(size=24); d/=np.linalg.norm(d)
    scales=[0.5,1.5,3.0,6.0]
    rows=[]
    for sc in scales:
        sol=solve(ref.x+sc*d,1.0)
        row=summarize_solution(sol,rt); row['start_scale']=sc
        rows.append(row)
    distinct=[r for r in rows if r.get('success') and r.get('transport_distance_from_reference',0)>1e-3]
    return {'gate':'ITER034-G34-LARGE-START-DISTANT-BASIN-SCAN','mode':'large-start','lane':lane,
      'reference':summarize_solution(ref,rt),'starts':rows,'converged_count':sum(r.get('success',False) for r in rows),
      'distinct_transport_root_candidates':len(distinct),'completed':True,
      'guard':'Finite deterministic large-start scan only; absence of a distinct root is not global uniqueness.'}

def background_continuation(lane):
    ref,rt=reference(); target=1.0+0.5*(lane+1)
    gammas=np.linspace(1.0,target,5)
    z=ref.x.copy(); rows=[]
    for g in gammas:
        sol=solve(z,float(g),1600)
        row=summarize_solution(sol,rt); row['gamma']=float(g); rows.append(row)
        if sol is None or not row.get('success'): break
        z=sol.x.copy()
    good=[r for r in rows if r.get('success')]
    mins=[r['jacobian_min_singular'] for r in good if 'jacobian_min_singular' in r]
    return {'gate':'ITER034-G34-BACKGROUND-STRENGTH-CONTINUATION','mode':'background-continuation','lane':lane,
      'target_gamma':target,'steps':rows,'completed_steps':len(good),'requested_steps':len(gammas),
      'minimum_observed_jacobian_gap':min(mins) if mins else None,'completed':True,
      'guard':'Continuation is along the fixed G9 conformal-frame family only; it is not the full configuration space.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['large-start','background-continuation'],required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    x=ap.parse_args(); assert 0<=x.lane<6
    out=large_start(x.lane) if x.mode=='large-start' else background_continuation(x.lane)
    os.makedirs(os.path.dirname(x.out),exist_ok=True)
    with open(x.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True,allow_nan=False); f.write('\n')
    print(json.dumps(out,sort_keys=True,allow_nan=False))
if __name__=='__main__': main()
