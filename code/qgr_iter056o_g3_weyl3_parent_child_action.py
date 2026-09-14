#!/usr/bin/env python3
"""Iter056O: parent->children Weyl3 local action-kernel refinement on the G3/H0 family."""
from __future__ import annotations
import argparse, itertools, json, math, os
from pathlib import Path
import numpy as np
from scipy.linalg import expm, logm
from scipy.optimize import least_squares
import qgr_iter040_weyl_response as g40

GATE='ITER056O-G3-WEYL3-PARENT-CHILD-LOCAL-ACTION-KERNEL-REFINEMENT'
PREREG='8c20980c41f575909609c059708822ab903ce203'
KAPPA=0.08
BASES=[np.zeros(4),np.full(4,0.10)]
PARENT_HS=[0.10,0.05]
H0=np.diag([1.0,1.0,-2.0])
BITS=list(itertools.product([0,1],repeat=4))
I=np.eye(4)


def L_from(z6):
    return expm(np.tensordot(z6,g40.BASIS,axes=(0,0)))


def translated_tetrad(local_x, base, h):
    x=np.asarray(base,dtype=float)/float(h)+np.asarray(local_x,dtype=float)
    return g40.tetrad_at(x,float(h),KAPPA,H0)


def solve_connection_at(base,h):
    base=np.asarray(base,dtype=float); h=float(h)
    def residual(local_x,z):
        x=np.asarray(local_x,dtype=float)
        Fx=translated_tetrad(x,base,h)
        try:
            Ls=[L_from(z[6*i:6*i+6]) for i in range(4)]
        except Exception:
            return np.full(24,1e50)
        out=[]
        for i in range(4):
            for j in range(i+1,4):
                xi=x.copy(); xi[i]+=1.0
                xj=x.copy(); xj[j]+=1.0
                try:
                    lhs=Fx[:,i]+np.linalg.solve(Ls[i],translated_tetrad(xi,base,h)[:,j])
                    rhs=Fx[:,j]+np.linalg.solve(Ls[j],translated_tetrad(xj,base,h)[:,i])
                    rr=lhs-rhs
                except Exception:
                    rr=np.full(4,1e50)
                if not np.all(np.isfinite(rr)):
                    rr=np.full(4,1e50)
                out.extend(rr)
        return np.asarray(out,float)

    sols={}; maxres=0.0; minsv=float('inf'); maxmetric=0.0
    for bits in BITS:
        s=least_squares(lambda z:residual(bits,z),np.zeros(24),
                        xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=1400)
        rn=float(np.linalg.norm(s.fun))
        sv=np.linalg.svd(s.jac,compute_uv=False)
        mats=[L_from(s.x[6*i:6*i+6]) for i in range(4)]
        me=max(float(np.linalg.norm(M.T@g40.E@M-g40.E)) for M in mats)
        finite=bool(np.all(np.isfinite(s.x)) and np.all(np.isfinite(sv)))
        if not finite or rn>=3e-9 or float(sv.min())<=1e-8 or me>=1e-7:
            return None,{'controls_valid':False,'failed_bits':list(bits),'residual_norm':rn,
                         'min_jacobian_singular':float(sv.min()) if len(sv) else 0.0,
                         'max_metric_error':me,'finite':finite}
        maxres=max(maxres,rn); minsv=min(minsv,float(sv.min())); maxmetric=max(maxmetric,me)
        sols[bits]=mats
    paths=[]
    for p in g40.PERMS:
        x=[0,0,0,0]; A=np.eye(4)
        for d in p:
            A=sols[tuple(x)][d]@A; x[d]+=1
        paths.append(A)
    return paths,{'controls_valid':True,'max_torsion_residual':maxres,
                  'min_jacobian_singular':minsv,'max_metric_error':maxmetric}


def cell_object(base,h):
    paths,ctl=solve_connection_at(base,h)
    if paths is None:
        return {'controls_valid':False,**ctl}
    X={}
    for i,j in g40.EDGES:
        rest=[k for k in range(4) if k not in (i,j)]
        p=(i,j,*rest); q=(j,i,*rest)
        Hol=np.linalg.solve(paths[g40.PERM_INDEX[q]],paths[g40.PERM_INDEX[p]])
        Lam=g40.RMI@Hol@g40.RM
        me=float(np.linalg.norm(Lam.T@g40.ETA@Lam-g40.ETA))
        if not math.isfinite(me) or me>=3e-8:
            return {'controls_valid':False,**ctl,'holonomy_metric_error':me}
        X[(i,j)]=np.real_if_close(logm(Lam),tol=1000).real
    Rorig=np.zeros((4,4,4,4),float)
    for (i,j),M in X.items():
        Rorig[:,:,i,j]=M/(h*h); Rorig[:,:,j,i]=-M/(h*h)
    Rmix=np.einsum('ia,jb,ABij->ABab',g40.RM,g40.RM,Rorig)
    Rlow=np.einsum('AC,CBab->ABab',g40.ETA,Rmix)
    W,Ric,scalar=g40.weyl_proxy(Rlow)
    w3=float(g40.weyl_cubic(W)); wn=float(np.linalg.norm(W))
    F=g40.tetrad_at(np.asarray(base,dtype=float)/float(h),float(h),KAPPA,H0)
    metric=F.T@g40.E@F
    detg=float(np.linalg.det(metric)); sqrtg=math.sqrt(abs(detg))
    action=float((float(h)**4)*sqrtg*w3)
    finite=all(math.isfinite(v) for v in [w3,wn,detg,sqrtg,action,float(np.linalg.norm(Ric)),float(scalar)])
    valid=bool(ctl['controls_valid'] and finite and wn>0.0)
    return {'controls_valid':valid,**ctl,'base':[float(x) for x in base],'h':float(h),
            'weyl_norm':wn,'weyl_cubic':w3,'sqrt_abs_det_g':sqrtg,'det_g':detg,
            'ricci_norm':float(np.linalg.norm(Ric)),'scalar':float(scalar),
            'action_kernel':action}


def child_bits(index):
    if not 0<=index<16: raise ValueError(index)
    return np.asarray(BITS[index],dtype=float)


def make_cell(base_index,parent_h,part):
    base=BASES[base_index]; H=float(parent_h)
    if part==0:
        role='parent'; child_index=None; h=H; cell_base=base.copy()
    else:
        role='child'; child_index=part-1; h=H/2.0
        cell_base=base+h*child_bits(child_index)
    try:
        obj=cell_object(cell_base,h)
        ok=bool(obj.get('controls_valid'))
        err=None
    except Exception as ex:
        obj={'controls_valid':False}; ok=False; err=repr(ex)
    return {'gate':GATE,'preregistration_commit':PREREG,
            'production_sha':os.environ.get('GITHUB_SHA','LOCAL'),
            'mode':'cell','base_index':base_index,'parent_h':H,'part':part,
            'role':role,'child_index':child_index,'cell_base':[float(x) for x in cell_base],
            'cell_h':float(h),'controls_valid':ok,'error':err,'object':obj}


def load_jsons(inp):
    out=[]; errors=[]
    for p in sorted(Path(inp).rglob('*.json')):
        try: out.append(json.loads(p.read_text()))
        except Exception as ex: errors.append(f'{p}:{ex}')
    return out,errors


def reduce_lane(inp,base_index,parent_h):
    H=float(parent_h); objs,parse_errors=load_jsons(inp)
    cells=[o for o in objs if o.get('gate')==GATE and o.get('mode')=='cell' and
           o.get('base_index')==base_index and abs(float(o.get('parent_h',-1))-H)<1e-12]
    bypart={}
    duplicates=[]
    for o in cells:
        p=o.get('part')
        if p in bypart: duplicates.append(p)
        bypart[p]=o
    expected=set(range(17)); got=set(bypart)
    complete=bool(got==expected and not duplicates and not parse_errors)
    preregs={o.get('preregistration_commit') for o in cells}
    shas={o.get('production_sha') for o in cells}
    provenance=bool(len(preregs)==1 and PREREG in preregs and len(shas)==1)
    valid=bool(complete and provenance and all(bypart[p].get('controls_valid') is True for p in expected))
    if not valid:
        return {'gate':GATE,'mode':'lane','base_index':base_index,'parent_h':H,
                'complete':complete,'provenance_valid':provenance,'controls_valid':False,'pass':False,
                'parse_errors':parse_errors,'missing_parts':sorted(expected-got),'duplicates':duplicates,
                'classification':'INVALID_IMPLEMENTATION_OR_CONTROL_ITER056O'}
    parent=float(bypart[0]['object']['action_kernel'])
    child_vals=[float(bypart[p]['object']['action_kernel']) for p in range(1,17)]
    child_sum=float(math.fsum(child_vals))
    denom=max(abs(parent),abs(child_sum))
    magnitude_ok=bool(denom>1e-14)
    residual=float(abs(child_sum-parent)/denom) if magnitude_ok else None
    missing_sum=float(math.fsum(child_vals[:-1]))
    missing_sens=float(abs(child_sum-missing_sum)/max(abs(child_sum),1e-30))
    wrong_sum=float(16.0*child_sum)
    wrong_sens=float(abs(wrong_sum-child_sum)/max(abs(child_sum),1e-30))
    neg=bool(missing_sens>0.02 and (H<0.099999 or wrong_sens>5.0))
    return {'gate':GATE,'mode':'lane','preregistration_commit':PREREG,
            'production_sha':next(iter(shas)),'base_index':base_index,'base':BASES[base_index].tolist(),
            'parent_h':H,'child_h':H/2.0,'complete':True,'provenance_valid':True,
            'controls_valid':magnitude_ok,'parent_action_kernel':parent,'children_action_kernel_sum':child_sum,
            'relative_parent_child_residual':residual,'missing_child_sensitivity':missing_sens,
            'wrong_volume_sensitivity':wrong_sens if H>0.099999 else None,
            'negative_controls_pass':neg,'pass':bool(magnitude_ok and neg),
            'classification':'LANE_VALID_ITER056O' if magnitude_ok and neg else 'INVALID_IMPLEMENTATION_OR_CONTROL_ITER056O'}


def aggregate(inp):
    objs,parse_errors=load_jsons(inp)
    lanes=[o for o in objs if o.get('gate')==GATE and o.get('mode')=='lane']
    key={}; dup=[]
    for o in lanes:
        k=(o.get('base_index'),round(float(o.get('parent_h',-1)),8))
        if k in key: dup.append(k)
        key[k]=o
    expected={(b,H) for b in (0,1) for H in (0.10,0.05)}
    got=set(key)
    complete=bool(got==expected and not dup and not parse_errors)
    valid=bool(complete and all(key[k].get('controls_valid') is True and key[k].get('negative_controls_pass') is True for k in expected))
    base_checks={}; scientific=False
    if valid:
        scientific=True
        for b in (0,1):
            coarse=float(key[(b,0.10)]['relative_parent_child_residual'])
            fine=float(key[(b,0.05)]['relative_parent_child_residual'])
            contraction=bool(fine<coarse)
            final=bool(fine<0.10)
            base_checks[str(b)]={'R_0p10':coarse,'R_0p05':fine,'contraction_pass':contraction,'final_threshold_pass':final}
            scientific=scientific and contraction and final
    if not valid:
        cls='INVALID_IMPLEMENTATION_OR_CONTROL_ITER056O'
    elif scientific:
        cls='PASS_SCOPED_ITER056O_G3_WEYL3_PARENT_CHILD_ACTION_KERNEL_REFINEMENT'
    else:
        cls='SCIENTIFIC_FAIL_ITER056O_G3_WEYL3_PARENT_CHILD_ACTION_KERNEL_REFINEMENT'
    return {'gate':GATE,'preregistration_commit':PREREG,'mode':'aggregate','classification':cls,
            'pass':bool(valid and scientific),'implementation_valid':valid,'complete':complete,
            'parse_errors':parse_errors,'missing_lanes':[list(k) for k in sorted(expected-got)],
            'duplicates':[list(k) for k in dup],'base_checks':base_checks,
            'claim_ceiling':'FINITE-PANEL G3 WEYL3 LOCAL ACTION-KERNEL PARENT-CHILD REFINEMENT ONLY'}


def write(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True,allow_nan=False)+'\n')
    print(json.dumps(obj,sort_keys=True,allow_nan=False))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--cell',action='store_true')
    ap.add_argument('--base-index',type=int)
    ap.add_argument('--parent-h',type=float)
    ap.add_argument('--part',type=int)
    ap.add_argument('--reduce')
    ap.add_argument('--aggregate')
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.cell:
        obj=make_cell(a.base_index,a.parent_h,a.part)
    elif a.reduce:
        obj=reduce_lane(a.reduce,a.base_index,a.parent_h)
    elif a.aggregate:
        obj=aggregate(a.aggregate)
    else:
        raise SystemExit('choose --cell, --reduce or --aggregate')
    write(a.out,obj)

if __name__=='__main__':
    main()
