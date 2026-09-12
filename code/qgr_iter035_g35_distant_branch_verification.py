#!/usr/bin/env python3
"""QGR Iter035: verify G34 distant-root candidates on a one-star patch.

Same nonlinear torsion system as Iter006 G9 / Iter034. A candidate is promoted only
if it survives independent polishing, metric compatibility, invariant edge transport
comparison, four-neighbor extension, and plaquette-holonomy invariant comparison.
This remains a scoped numerical result, not a global branch-count theorem.
"""
import argparse,json,math,os
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares, root

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
SCALES=[0.5,1.5,3.0,6.0]
assert max(np.linalg.norm(X.T@C+C@X) for X in B)<1e-12

def Omega(x):
    x=np.asarray(x,dtype=float)
    return math.exp(float(a@x+0.5*x@Q@x))

def L_from(p6): return expm(np.tensordot(p6,B,axes=(0,0)))

def residual(x,z):
    x=np.asarray(x,dtype=int); Om=Omega(x)
    try: L=[L_from(z[6*i:6*i+6]) for i in range(4)]
    except Exception: return np.full(24,1e50)
    out=[]
    for i in range(4):
        for j in range(i+1,4):
            xi=x.copy(); xi[i]+=1; xj=x.copy(); xj[j]+=1
            try:
                lhs=Om*I[:,i]+np.linalg.solve(L[i],Omega(xi)*I[:,j])
                rhs=Om*I[:,j]+np.linalg.solve(L[j],Omega(xj)*I[:,i])
                rr=lhs-rhs
            except Exception:
                rr=np.full(4,1e50)
            if not np.all(np.isfinite(rr)): rr=np.full(4,1e50)
            out.extend(rr)
    return np.asarray(out,dtype=float)

def solve_ls(x,z0,max_nfev=1800):
    try:
        return least_squares(lambda z:residual(x,z),z0,xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=max_nfev)
    except Exception:
        return None

def polish_root(x,z0):
    try:
        rr=root(lambda z:residual(x,z),z0,method='lm',options={'ftol':1e-12,'xtol':1e-12,'gtol':1e-12,'maxiter':5000})
        rn=float(np.linalg.norm(residual(x,rr.x)))
        return rr.x,rn,bool(np.all(np.isfinite(rr.x)))
    except Exception:
        return None,float('inf'),False

def Ls(z): return [L_from(z[6*i:6*i+6]) for i in range(4)]

def metric_errors(z): return [float(np.linalg.norm(L.T@C@L-C)) for L in Ls(z)]

def jac_stats(x,z):
    sol=solve_ls(x,z,20)
    if sol is None: return None
    sv=np.linalg.svd(sol.jac,compute_uv=False)
    sign,logdet=np.linalg.slogdet(sol.jac)
    return {'min_singular':float(sv.min()),'max_singular':float(sv.max()),
            'condition':float(sv.max()/sv.min()) if sv.min()>0 else float('inf'),
            'slogdet_sign':float(sign),'log_abs_det':float(logdet)}

def edge_A(x,z):
    x=np.asarray(x,dtype=int); out=[]
    for i,L in enumerate(Ls(z)):
        xi=x.copy(); xi[i]+=1
        out.append((Omega(x)/Omega(xi))*L)
    return out

def edge_fingerprint(A):
    return [[float(np.trace(M)),float(np.trace(M@M)),float(np.linalg.det(M))] for M in A]

def max_edge_distance(A,Bb): return max(float(np.linalg.norm(x-y)) for x,y in zip(A,Bb))

def solve_patch(origin_z):
    origin=np.zeros(4,dtype=int)
    sols={tuple(origin):origin_z.copy()}
    rows=[]
    for k in range(4):
        x=np.eye(4,dtype=int)[k]
        sol=solve_ls(x,origin_z,2200)
        rn=float(np.linalg.norm(sol.fun)) if sol is not None else float('inf')
        ok=bool(sol is not None and rn<1e-8 and np.all(np.isfinite(sol.x)))
        row={'neighbor':k,'residual_norm':rn,'success':ok}
        if ok:
            z2,rn2,finite=polish_root(x,sol.x)
            if finite and rn2<rn: z_use=z2; rn=rn2
            else: z_use=sol.x
            row['polished_residual_norm']=float(np.linalg.norm(residual(x,z_use)))
            row['max_metric_error']=max(metric_errors(z_use))
            sols[tuple(x)]=z_use
        rows.append(row)
    return sols,rows

def plaquette_invariants(sols):
    zero=(0,0,0,0)
    if len(sols)<5: return None
    lm={x:Ls(z) for x,z in sols.items()}
    invs=[]
    for i in range(4):
        for j in range(i+1,4):
            xi=tuple(np.eye(4,dtype=int)[i]); xj=tuple(np.eye(4,dtype=int)[j])
            P1=lm[xi][j]@lm[zero][i]
            P2=lm[xj][i]@lm[zero][j]
            H=np.linalg.inv(P2)@P1
            invs.append({'plane':[i,j],
                'norm_H_minus_I':float(np.linalg.norm(H-I)),
                'trace':float(np.trace(H)),
                'trace2':float(np.trace(H@H)),
                'det':float(np.linalg.det(H)),
                'metric_error':float(np.linalg.norm(H.T@C@H-C))})
    return invs

def holonomy_invariant_distance(a,b):
    if a is None or b is None:return float('inf')
    vals=[]
    for x,y in zip(a,b):
        vals.extend([abs(x['trace']-y['trace']),abs(x['trace2']-y['trace2']),abs(x['det']-y['det'])])
    return max(vals) if vals else 0.0

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--scale-index',type=int,required=True); ap.add_argument('--out',required=True)
    q=ap.parse_args(); assert 0<=q.lane<6 and 0<=q.scale_index<4
    origin=np.zeros(4,dtype=int)
    ref=solve_ls(origin,np.zeros(24),2200)
    if ref is None or np.linalg.norm(ref.fun)>=1e-9: raise SystemExit('reference root failed')
    rz,rrn,rfin=polish_root(origin,ref.x)
    if rfin and rrn<float(np.linalg.norm(ref.fun)): refz=rz
    else: refz=ref.x
    refA=edge_A(origin,refz)
    ref_patch,ref_neighbor_rows=solve_patch(refz)
    ref_hol=plaquette_invariants(ref_patch)

    rng=np.random.default_rng(34000+q.lane); d=rng.normal(size=24); d/=np.linalg.norm(d)
    sc=SCALES[q.scale_index]
    cand=solve_ls(origin,refz+sc*d,2400)
    raw_rn=float(np.linalg.norm(cand.fun)) if cand is not None else float('inf')
    origin_ok=bool(cand is not None and raw_rn<1e-8 and np.all(np.isfinite(cand.x)))
    result={'gate':'ITER035-G35-DISTANT-BRANCH-VERIFICATION','lane':q.lane,'scale_index':q.scale_index,'start_scale':sc,
            'reference_neighbor_extension_successes':sum(r['success'] for r in ref_neighbor_rows),
            'reference_holonomy_available':ref_hol is not None,'origin_solver_residual':raw_rn,'origin_solver_success':origin_ok}
    if not origin_ok:
        result.update({'classification':'NO_RESIDUAL_QUALIFIED_ORIGIN_CANDIDATE_FROM_THIS_START','verified_patch_distinct_branch':False})
    else:
        pz,prn,pfinite=polish_root(origin,cand.x)
        cz=pz if pfinite and prn<1e-8 else cand.x
        prn=float(np.linalg.norm(residual(origin,cz)))
        me=max(metric_errors(cz)); candA=edge_A(origin,cz); ed=max_edge_distance(candA,refA)
        fp=edge_fingerprint(candA); rfp=edge_fingerprint(refA)
        fpd=max(abs(fp[i][j]-rfp[i][j]) for i in range(4) for j in range(3))
        central_distinct=bool(ed>1e-4 and fpd>1e-7)
        cpatch,nrows=solve_patch(cz); patch_ok=all(r['success'] and r.get('polished_residual_norm',1)>0 and r.get('polished_residual_norm',1)<1e-8 and r.get('max_metric_error',1)<1e-7 for r in nrows)
        chol=plaquette_invariants(cpatch) if patch_ok else None
        hid=holonomy_invariant_distance(chol,ref_hol) if patch_ok and ref_hol is not None else None
        hol_distinct=bool(hid is not None and hid>1e-6)
        verified=bool(prn<1e-9 and me<1e-7 and central_distinct and patch_ok and hol_distinct)
        result.update({'independent_polished_residual':prn,'max_origin_metric_error':me,'max_gauge_invariant_edge_transport_distance':ed,
            'max_edge_fingerprint_difference':fpd,'central_invariantly_distinct':central_distinct,'candidate_edge_fingerprint':fp,
            'reference_edge_fingerprint':rfp,'neighbor_rows':nrows,'neighbor_extension_successes':sum(r['success'] for r in nrows),
            'patch_extension_success':patch_ok,'plaquette_holonomy_invariant_distance':hid,'holonomy_invariantly_distinct':hol_distinct,
            'origin_jacobian':jac_stats(origin,cz),'candidate_holonomy':chol,'reference_holonomy':ref_hol,
            'verified_patch_distinct_branch':verified,
            'classification':'NUMERICALLY_VERIFIED_SCOPED_DISTINCT_EXTENDABLE_FINITE_TORSION_BRANCH_PATCH' if verified else 'G34_CANDIDATE_NOT_YET_VERIFIED_AS_DISTINCT_EXTENDABLE_PATCH'})
    os.makedirs(os.path.dirname(q.out),exist_ok=True)
    with open(q.out,'w',encoding='utf-8') as f: json.dump(result,f,indent=2,sort_keys=True,allow_nan=False); f.write('\n')
    print(json.dumps(result,sort_keys=True,allow_nan=False))
if __name__=='__main__':main()
