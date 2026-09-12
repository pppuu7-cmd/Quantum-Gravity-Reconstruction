#!/usr/bin/env python3
"""QGR Iter036: expanded-patch persistence of G35 verified finite torsion branches.

Two frozen modes:
  amplitude: gamma targets 0.8, 1.0, 1.2 at h=1
  refine:    h targets 0.75, 0.50, 0.35 at gamma=1

The h deformation is a local shrinking-cell/background-sampling proxy, not the full
QGR projective refinement map. All conclusions remain scoped numerical statements.
"""
import argparse, json, math, os
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
VERIFIED=[(0,3),(1,2),(1,3),(2,2),(2,3),(3,1),(4,2),(5,3)]
AMP_TARGETS=[0.8,1.0,1.2]
H_TARGETS=[0.75,0.50,0.35]
assert max(np.linalg.norm(X.T@C+C@X) for X in B)<1e-12

def safe(v):
    try:
        x=float(v)
        return x if math.isfinite(x) else None
    except Exception:
        return None

def L_from(p6):
    return expm(np.tensordot(p6,B,axes=(0,0)))

class System:
    def __init__(self,gamma=1.0,h=1.0):
        self.gamma=float(gamma); self.h=float(h)
    def Omega(self,x):
        y=self.h*np.asarray(x,dtype=float)
        return math.exp(self.gamma*float(a@y+0.5*y@Q@y))
    def residual(self,x,z):
        x=np.asarray(x,dtype=int); Om=self.Omega(x)
        try: L=[L_from(z[6*i:6*i+6]) for i in range(4)]
        except Exception: return np.full(24,1e50)
        out=[]
        for i in range(4):
            for j in range(i+1,4):
                xi=x.copy(); xi[i]+=1; xj=x.copy(); xj[j]+=1
                try:
                    lhs=Om*I[:,i]+np.linalg.solve(L[i],self.Omega(xi)*I[:,j])
                    rhs=Om*I[:,j]+np.linalg.solve(L[j],self.Omega(xj)*I[:,i])
                    rr=lhs-rhs
                except Exception:
                    rr=np.full(4,1e50)
                if not np.all(np.isfinite(rr)): rr=np.full(4,1e50)
                out.extend(rr)
        return np.asarray(out,dtype=float)
    def solve(self,x,z0,max_nfev=2400):
        try:
            return least_squares(lambda z:self.residual(x,z),z0,xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=max_nfev)
        except Exception:
            return None
    def polish(self,x,z0):
        try:
            rr=root(lambda z:self.residual(x,z),z0,method='lm',
                    options={'ftol':1e-12,'xtol':1e-12,'gtol':1e-12,'maxiter':5000})
            rn=float(np.linalg.norm(self.residual(x,rr.x)))
            return rr.x,rn,bool(np.all(np.isfinite(rr.x)))
        except Exception:
            return None,float('inf'),False

def Ls(z):
    return [L_from(z[6*i:6*i+6]) for i in range(4)]

def metric_errors(z):
    return [float(np.linalg.norm(L.T@C@L-C)) for L in Ls(z)]

def edge_A(sys,x,z):
    x=np.asarray(x,dtype=int); out=[]
    for i,L in enumerate(Ls(z)):
        xi=x.copy(); xi[i]+=1
        out.append((sys.Omega(x)/sys.Omega(xi))*L)
    return out

def edge_fingerprint(A):
    return [[float(np.trace(M)),float(np.trace(M@M)),float(np.linalg.det(M))] for M in A]

def max_edge_distance(A,Bb):
    return max(float(np.linalg.norm(x-y)) for x,y in zip(A,Bb))

def best_cell(sys,x,seeds,max_nfev=2600):
    best=None; best_r=float('inf')
    for seed in seeds:
        sol=sys.solve(x,np.asarray(seed),max_nfev)
        if sol is None or not np.all(np.isfinite(sol.x)): continue
        rn=float(np.linalg.norm(sys.residual(x,sol.x)))
        if rn<best_r:
            best=sol.x.copy(); best_r=rn
    if best is None: return None,float('inf')
    pz,prn,pfinite=sys.polish(x,best)
    if pfinite and prn<best_r:
        best=pz; best_r=prn
    return best,float(best_r)

def continue_origin(z0,gamma0,h0,gamma1,h1,steps=6):
    z=np.asarray(z0).copy(); rows=[]
    for k in range(1,steps+1):
        t=k/steps
        g=(1-t)*gamma0+t*gamma1
        h=(1-t)*h0+t*h1
        sys=System(g,h)
        z2,rn=best_cell(sys,np.zeros(4,dtype=int),[z],2800)
        ok=bool(z2 is not None and rn<1e-8 and max(metric_errors(z2))<1e-7)
        rows.append({'step':k,'gamma':g,'h':h,'residual_norm':safe(rn),
                     'max_metric_error':safe(max(metric_errors(z2))) if z2 is not None else None,
                     'success':ok})
        if not ok:
            return None,rows
        z=z2
    return z,rows

def expanded_patch(sys,origin_z):
    zero=(0,0,0,0); roots={zero:np.asarray(origin_z).copy()}; rows=[]
    e=[np.eye(4,dtype=int)[i] for i in range(4)]
    for i in range(4):
        x=e[i]; z,rn=best_cell(sys,x,[origin_z])
        ok=bool(z is not None and rn<1e-8 and max(metric_errors(z))<1e-7)
        rows.append({'cell':x.tolist(),'kind':'first','residual_norm':safe(rn),
                     'max_metric_error':safe(max(metric_errors(z))) if z is not None else None,'success':ok})
        if ok: roots[tuple(x)]=z
    for i in range(4):
        x=2*e[i]; parent=roots.get(tuple(e[i]))
        seeds=[parent] if parent is not None else [origin_z]
        z,rn=best_cell(sys,x,seeds)
        ok=bool(z is not None and rn<1e-8 and max(metric_errors(z))<1e-7)
        rows.append({'cell':x.tolist(),'kind':'axial2','residual_norm':safe(rn),
                     'max_metric_error':safe(max(metric_errors(z))) if z is not None else None,'success':ok})
        if ok: roots[tuple(x)]=z
    for i in range(4):
        for j in range(i+1,4):
            x=e[i]+e[j]; zi=roots.get(tuple(e[i])); zj=roots.get(tuple(e[j]))
            seeds=[s for s in (zi,zj) if s is not None]
            if zi is not None and zj is not None: seeds.append(0.5*(zi+zj))
            if not seeds: seeds=[origin_z]
            z,rn=best_cell(sys,x,seeds)
            ok=bool(z is not None and rn<1e-8 and max(metric_errors(z))<1e-7)
            rows.append({'cell':x.tolist(),'kind':'mixed2','residual_norm':safe(rn),
                         'max_metric_error':safe(max(metric_errors(z))) if z is not None else None,'success':ok})
            if ok: roots[tuple(x)]=z
    return roots,rows

def expanded_holonomy(roots):
    e=[np.eye(4,dtype=int)[i] for i in range(4)]
    lm={x:Ls(z) for x,z in roots.items()}
    out=[]
    bases=[np.zeros(4,dtype=int)]+e
    for b in bases:
        bt=tuple(b)
        if bt not in lm: continue
        for i in range(4):
            for j in range(i+1,4):
                xi=tuple(b+e[i]); xj=tuple(b+e[j])
                if xi not in lm or xj not in lm: continue
                P1=lm[xi][j]@lm[bt][i]
                P2=lm[xj][i]@lm[bt][j]
                try: H=np.linalg.inv(P2)@P1
                except Exception: continue
                out.append({'base':list(bt),'plane':[i,j],
                            'trace':float(np.trace(H)),'trace2':float(np.trace(H@H)),
                            'det':float(np.linalg.det(H)),
                            'norm_H_minus_I':float(np.linalg.norm(H-I)),
                            'metric_error':float(np.linalg.norm(H.T@C@H-C))})
    return out

def holonomy_distance(A,Bb):
    ma={(tuple(x['base']),tuple(x['plane'])):x for x in A}
    mb={(tuple(x['base']),tuple(x['plane'])):x for x in Bb}
    keys=sorted(set(ma)&set(mb))
    if not keys: return None
    vals=[]
    for k in keys:
        x,y=ma[k],mb[k]
        vals.extend([abs(x['trace']-y['trace']),abs(x['trace2']-y['trace2']),abs(x['det']-y['det'])])
    return max(vals) if vals else None

def reconstruct_baseline(seed_index):
    lane,scale_index=VERIFIED[seed_index]
    sys=System(1.0,1.0); origin=np.zeros(4,dtype=int)
    ref,rn=best_cell(sys,origin,[np.zeros(24)],2800)
    if ref is None or rn>=1e-9:
        return None,None,{'baseline_reference_residual':safe(rn),'baseline_ok':False}
    rng=np.random.default_rng(34000+lane); d=rng.normal(size=24); d/=np.linalg.norm(d)
    cand,rn2=best_cell(sys,origin,[ref+SCALES[scale_index]*d],3000)
    ok=bool(cand is not None and rn2<1e-9)
    return ref,cand,{'baseline_reference_residual':safe(rn),'baseline_candidate_residual':safe(rn2),
                     'baseline_ok':ok,'g35_lane':lane,'g35_scale_index':scale_index,
                     'g35_start_scale':SCALES[scale_index]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['amplitude','refine'],required=True)
    ap.add_argument('--seed-index',type=int,required=True)
    ap.add_argument('--param-index',type=int,required=True)
    ap.add_argument('--out',required=True)
    q=ap.parse_args()
    assert 0<=q.seed_index<len(VERIFIED) and 0<=q.param_index<3
    ref0,cand0,base=reconstruct_baseline(q.seed_index)
    result={'gate':'ITER036-G36-EXPANDED-PATCH-PERSISTENCE',
            'mode':q.mode,'seed_index':q.seed_index,'param_index':q.param_index,**base,
            'claim_lock':'Scoped finite-patch numerical persistence only; refinement mode is a local shrinking-cell proxy, not a projective-limit theorem.'}
    if ref0 is None or cand0 is None or not base['baseline_ok']:
        result.update({'classification':'BASELINE_RECONSTRUCTION_FAILED','verified_persistent_distinct_branch':False})
    else:
        if q.mode=='amplitude':
            gamma1=AMP_TARGETS[q.param_index]; h1=1.0; target=gamma1
        else:
            gamma1=1.0; h1=H_TARGETS[q.param_index]; target=h1
        result['target_value']=target; result['target_gamma']=gamma1; result['target_h']=h1
        ref,ref_cont=continue_origin(ref0,1.0,1.0,gamma1,h1)
        cand,cand_cont=continue_origin(cand0,1.0,1.0,gamma1,h1)
        result['reference_continuation']=ref_cont; result['candidate_continuation']=cand_cont
        cont_ok=bool(ref is not None and cand is not None)
        result['continuation_success']=cont_ok
        if not cont_ok:
            result.update({'classification':'TARGET_CONTINUATION_FAILED','verified_persistent_distinct_branch':False})
        else:
            sys=System(gamma1,h1); origin=np.zeros(4,dtype=int)
            ref_rn=float(np.linalg.norm(sys.residual(origin,ref)))
            cand_rn=float(np.linalg.norm(sys.residual(origin,cand)))
            cand_me=max(metric_errors(cand))
            refA=edge_A(sys,origin,ref); candA=edge_A(sys,origin,cand)
            ed=max_edge_distance(candA,refA)
            fp=edge_fingerprint(candA); rfp=edge_fingerprint(refA)
            fpd=max(abs(fp[i][j]-rfp[i][j]) for i in range(4) for j in range(3))
            ref_patch,ref_rows=expanded_patch(sys,ref)
            cand_patch,cand_rows=expanded_patch(sys,cand)
            ref_patch_ok=bool(len(ref_patch)==15 and all(r['success'] for r in ref_rows))
            cand_patch_ok=bool(len(cand_patch)==15 and all(r['success'] for r in cand_rows))
            ref_hol=expanded_holonomy(ref_patch) if ref_patch_ok else []
            cand_hol=expanded_holonomy(cand_patch) if cand_patch_ok else []
            hid=holonomy_distance(cand_hol,ref_hol) if ref_patch_ok and cand_patch_ok else None
            controls=bool(ref_rn<1e-9 and ref_patch_ok and len(ref_hol)==30)
            verified=bool(controls and cand_rn<1e-9 and cand_me<1e-7 and
                          ed>1e-4 and fpd>1e-7 and cand_patch_ok and len(cand_hol)==30 and
                          hid is not None and hid>1e-6)
            result.update({
                'reference_origin_residual':safe(ref_rn),'candidate_origin_residual':safe(cand_rn),
                'candidate_max_origin_metric_error':safe(cand_me),
                'max_edge_transport_distance':safe(ed),'max_edge_fingerprint_difference':safe(fpd),
                'reference_patch_cells':len(ref_patch),'candidate_patch_cells':len(cand_patch),
                'reference_patch_valid':ref_patch_ok,'candidate_patch_valid':cand_patch_ok,
                'reference_patch_rows':ref_rows,'candidate_patch_rows':cand_rows,
                'reference_holonomy_count':len(ref_hol),'candidate_holonomy_count':len(cand_hol),
                'expanded_holonomy_invariant_distance':safe(hid) if hid is not None else None,
                'reference_controls_valid':controls,
                'verified_persistent_distinct_branch':verified,
                'classification':'VERIFIED_SCOPED_EXPANDED_PATCH_PERSISTENT_DISTINCT_BRANCH'
                    if verified else 'BRANCH_NOT_PROMOTED_IN_THIS_FROZEN_STRESS_LANE'
            })
    os.makedirs(os.path.dirname(q.out),exist_ok=True)
    with open(q.out,'w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True,allow_nan=False); f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('reference_patch_rows','candidate_patch_rows',
          'reference_continuation','candidate_continuation')},sort_keys=True,allow_nan=False))

if __name__=='__main__':
    main()
