#!/usr/bin/env python3
"""Iter054S: fine-to-coarse transport blocking on the existing G3 Weyl-active tidal family."""
import argparse, json, math, os
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
import qgr_iter010_g3_common as g3

GATE='ITER054S-WEYL-ACTIVE-TIDAL-FINE-TO-COARSE-TRANSPORT-BLOCKING'
PREREG='cfd9661e8363518e57c686e0f75f608cdbf99b7d'
KAPPA=0.08
BASES=[np.zeros(4),np.full(4,0.10)]
ELL_PATH=0.20
ELL_LOOP=0.10
NS=[2,4,8,16]
PLANES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
I=np.eye(4)
E=g3.E
BASIS=g3.BASIS


def L_from(z6):
    return expm(np.tensordot(z6,BASIS,axes=(0,0)))


def residual_at(x_index,h,z):
    x=np.asarray(x_index,dtype=float)
    Fx=g3.tetrad_at(x,h,KAPPA)
    Ls=[L_from(z[6*i:6*i+6]) for i in range(4)]
    out=[]
    for i in range(4):
        for j in range(i+1,4):
            xi=x.copy(); xi[i]+=1.0
            xj=x.copy(); xj[j]+=1.0
            lhs=Fx[:,i]+np.linalg.solve(Ls[i],g3.tetrad_at(xi,h,KAPPA)[:,j])
            rhs=Fx[:,j]+np.linalg.solve(Ls[j],g3.tetrad_at(xj,h,KAPPA)[:,i])
            out.extend(lhs-rhs)
    return np.asarray(out,dtype=float)


def solve_local(x_index,h,seed=None):
    z0=np.zeros(24) if seed is None else np.asarray(seed,dtype=float)
    try:
        sol=least_squares(lambda z:residual_at(x_index,h,z),z0,
                          xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=1800)
        rn=float(np.linalg.norm(sol.fun))
        Ls=[L_from(sol.x[6*i:6*i+6]) for i in range(4)]
        me=float(max(np.linalg.norm(L.T@E@L-E) for L in Ls))
        sv=np.linalg.svd(sol.jac,compute_uv=False)
        minsv=float(sv.min()) if len(sv) else 0.0
        finite=bool(np.all(np.isfinite(sol.x)) and np.all(np.isfinite(sv)))
        ok=bool(finite and rn<3e-9 and me<1e-7 and minsv>1e-8)
        return sol.x,Ls,{'ok':ok,'residual_norm':rn,'metric_error':me,'min_jacobian_singular':minsv}
    except Exception as ex:
        return None,None,{'ok':False,'error':repr(ex)}


def path_product(base,direction,length,N,omit_index=None):
    h=float(length)/int(N)
    base=np.asarray(base,dtype=float)
    x0=base/h
    A=np.eye(4); seed=None; rows=[]
    for n in range(N):
        x=x0.copy(); x[direction]+=n
        z,Ls,ctl=solve_local(x,h,seed)
        rows.append({'step':n,'physical_h':h,**ctl})
        if not ctl.get('ok'):
            return None,rows
        seed=z
        if omit_index is not None and n==omit_index:
            continue
        A=Ls[direction]@A
    return A,rows


def diffs(mats):
    return [float(np.linalg.norm(mats[2*n]-mats[n])) for n in (2,4,8)]


def lane_control():
    dat,X,R=g3.curvature_proxy(0.05,KAPPA)
    W,_,_=g3.weyl_proxy(R)
    w3=float(g3.weyl_cubic(W))
    local_ok=bool(dat['max_torsion_residual']<3e-9 and dat['min_jacobian_singular']>1e-8)
    passed=bool(local_ok and math.isfinite(w3) and abs(w3)>0.04)
    return {'gate':GATE,'stream':'control','index':0,'pass':passed,'controls_valid':local_ok,
            'weyl_cubic':w3,'weyl_activity_pass':abs(w3)>0.04,
            'max_torsion_residual':float(dat['max_torsion_residual']),
            'min_jacobian_singular':float(dat['min_jacobian_singular']),
            'classification':'C0_WEYL_ACTIVE_IDENTITY_CONTROL_PASS' if passed else 'C0_CONTROL_INVALID'}


def lane_path(index):
    base=BASES[index//4]; direction=index%4
    mats={}; all_rows={}; valid=True
    for N in NS:
        A,rows=path_product(base,direction,ELL_PATH,N)
        all_rows[str(N)]=rows
        if A is None:
            valid=False; break
        mats[N]=A
    ds=diffs(mats) if valid else []
    trend=bool(len(ds)==3 and ds[1]<ds[0] and ds[2]<ds[1])
    ratio=float(ds[2]/ds[1]) if trend and ds[1]>0 else None
    conv=bool(trend and ratio is not None and ratio<0.80)
    neg=False; negdist=None
    if valid:
        malformed,mrows=path_product(base,direction,ELL_PATH,16,omit_index=7)
        all_rows['16_malformed']=mrows
        if malformed is not None:
            negdist=float(np.linalg.norm(mats[16]-malformed))
            neg=bool(negdist>1e-5)
    passed=bool(valid and conv and neg)
    return {'gate':GATE,'stream':'path','index':index,'base':base.tolist(),'direction':direction,
            'length':ELL_PATH,'Ns':NS,'pass':passed,'controls_valid':valid,
            'successive_differences':ds,'final_contraction_ratio':ratio,
            'convergence_pass':conv,'malformed_omit_child_distance':negdist,
            'negative_control_pass':neg,'rows':all_rows,
            'classification':'P_PATH_BLOCKING_PASS' if passed else ('P_CONTROL_INVALID' if not valid else 'P_SCIENTIFIC_NOT_PROMOTED')}


def square_holonomy(base,i,j,length,N):
    base=np.asarray(base,dtype=float)
    Pi,r1=path_product(base,i,length,N)
    bi=base.copy(); bi[i]+=length
    Pj_i,r2=path_product(bi,j,length,N)
    bj=base.copy(); bj[j]+=length
    Pi_j,r3=path_product(bj,i,length,N)
    Pj,r4=path_product(base,j,length,N)
    if any(P is None for P in (Pi,Pj_i,Pi_j,Pj)):
        return None,None,{'ok':False,'side_rows':[r1,r2,r3,r4]}
    H=np.linalg.inv(Pj)@np.linalg.inv(Pi_j)@Pj_i@Pi
    Hrev=np.linalg.inv(Pi)@np.linalg.inv(Pj_i)@Pi_j@Pj
    me=float(np.linalg.norm(H.T@E@H-E))
    orient=float(np.linalg.norm(Hrev-np.linalg.inv(H)))
    ok=bool(me<1e-7 and orient<1e-7)
    return H,Hrev,{'ok':ok,'metric_error':me,'reverse_inverse_error':orient,'side_rows':[r1,r2,r3,r4]}


def lane_loop(index):
    base=BASES[index//6]; i,j=PLANES[index%6]
    mats={}; rows={}; valid=True
    for N in NS:
        H,Hrev,ctl=square_holonomy(base,i,j,ELL_LOOP,N)
        rows[str(N)]=ctl
        if H is None or not ctl.get('ok'):
            valid=False; break
        mats[N]=H
    ds=diffs(mats) if valid else []
    trend=bool(len(ds)==3 and ds[1]<ds[0] and ds[2]<ds[1])
    ratio=float(ds[2]/ds[1]) if trend and ds[1]>0 else None
    conv=bool(trend and ratio is not None and ratio<0.85)
    final_metric=float(rows['16']['metric_error']) if valid else None
    orient_ok=bool(valid and rows['16']['reverse_inverse_error']<1e-7)
    passed=bool(valid and conv and orient_ok)
    return {'gate':GATE,'stream':'loop','index':index,'base':base.tolist(),'plane':[i,j],
            'length':ELL_LOOP,'Ns':NS,'pass':passed,'controls_valid':valid,
            'successive_differences':ds,'final_contraction_ratio':ratio,
            'convergence_pass':conv,'final_metric_error':final_metric,
            'orientation_control_pass':orient_ok,'rows':rows,
            'classification':'L_LOOP_BLOCKING_PASS' if passed else ('L_CONTROL_INVALID' if not valid else 'L_SCIENTIFIC_NOT_PROMOTED')}


def aggregate(inp):
    objs=[]; errors=[]
    for p in sorted(Path(inp).rglob('*.json')):
        try: objs.append(json.loads(p.read_text()))
        except Exception as ex: errors.append(f'{p}:{ex}')
    ctl=[o for o in objs if o.get('stream')=='control']
    paths={o.get('index'):o for o in objs if o.get('stream')=='path'}
    loops={o.get('index'):o for o in objs if o.get('stream')=='loop'}
    complete=bool(len(ctl)==1 and len(paths)==8 and len(loops)==12 and not errors)
    valid=bool(complete and ctl[0].get('controls_valid') is True and
               all(paths[i].get('controls_valid') is True for i in range(8)) and
               all(loops[i].get('controls_valid') is True for i in range(12)))
    scientific=bool(valid and ctl[0].get('pass') is True and
                    all(paths[i].get('pass') is True for i in range(8)) and
                    all(loops[i].get('pass') is True for i in range(12)))
    if not complete or not valid:
        cls='INVALID_IMPLEMENTATION_ITER054S'
    elif scientific:
        cls='PASS_SCOPED_ITER054S_WEYL_ACTIVE_TIDAL_FINE_TO_COARSE_TRANSPORT_BLOCKING'
    else:
        cls='SCIENTIFIC_FAIL_ITER054S_WEYL_ACTIVE_TIDAL_TRANSPORT_BLOCKING'
    return {'gate':GATE,'preregistration_commit':PREREG,'classification':cls,'pass':scientific,
            'implementation_valid':valid,'complete':complete,'parse_errors':errors,
            'control_pass':ctl[0].get('pass') if len(ctl)==1 else None,
            'path_pass_count':sum(paths[i].get('pass') is True for i in range(8) if i in paths),
            'loop_pass_count':sum(loops[i].get('pass') is True for i in range(12) if i in loops),
            'path_count':len(paths),'loop_count':len(loops),
            'claim_ceiling':'FINITE-PANEL WEYL-ACTIVE TIDAL TRANSPORT BLOCKING ONLY; S_ALPHA/C6/MEASURE/UNITARITY/UV/FULL-QG NOT ESTABLISHED'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',choices=['control','path','loop'])
    ap.add_argument('--index',type=int,default=0)
    ap.add_argument('--aggregate')
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.aggregate:
        out=aggregate(a.aggregate)
    elif a.stream=='control':
        out=lane_control()
    elif a.stream=='path':
        assert 0<=a.index<8; out=lane_path(a.index)
    else:
        assert a.stream=='loop' and 0<=a.index<12; out=lane_loop(a.index)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True,allow_nan=False)+'\n')
    compact={k:v for k,v in out.items() if k!='rows'}
    print(json.dumps(compact,sort_keys=True,allow_nan=False))
    if a.aggregate and out['classification']=='INVALID_IMPLEMENTATION_ITER054S':
        raise SystemExit(2)

if __name__=='__main__':
    main()
