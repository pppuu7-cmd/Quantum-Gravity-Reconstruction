#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np
import sympy as sp

import qgr_iter051c_d2_sign_heldout as d2
import qgr_iter051c_d2n_near_null as d2n

H5=(2.0e-3,1.0e-3,5.0e-4)
PANEL=[
 (0,1.07),(1,1.11),(2,0.91),(0,1.41),(1,1.52),(2,1.63),
 (3,1.175),(3,1.190),(3,1.195),(3,1.205),(3,1.210),(3,1.335)
]

def relnorm(a,b,floor=1e-14):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(b),floor))

def exact_target(profile,rval):
    EF,EN,ES=d2.spherical_authority()[7:10]
    fv,nv,sv,_=d2.spherical_sympy_profile(profile)
    rr=sp.Rational(str(rval))
    vals=[d2.s49.prof(expr,fv,nv,sv).subs(d2.s49.r,rr) for expr in (EF,EN,ES)]
    return np.array([float(sp.N(v,40)) for v in vals],float)

def lane(index):
    profile,r=PANEL[index]
    metric=d2.SphericalMetric(profile)
    x=np.array([0.0,r,math.pi/2,0.0],float)
    sig,inv,det=d2n.extended_controls(metric,x)
    target=exact_target(profile,r)
    pred=[]; lastz=None
    for h in H5:
        H,z=d2n.assemble_minus5(metric,x,h)
        pred.append(d2.reduced_spherical(H,metric,r)); lastz=z
    finest=pred[-1]
    sg=math.sqrt(-float(np.linalg.det(lastz['g'])))
    hist=d2.reduced_spherical(lastz['A']+lastz['I']+2.0*sg*lastz['D'],metric,r)
    abs_err=np.abs(finest-target)
    comp_ok=[]; modes=[]; rels=[]
    for k in range(3):
        if abs(target[k])>=1e-5:
            rr=float(abs(finest[k]-target[k])/max(abs(target[k]),1e-14))
            rels.append(rr); modes.append('ordinary_relative')
            comp_ok.append(rr<=2e-4)
        else:
            sign_ok=(abs(target[k])<=1e-10) or (np.sign(finest[k])==np.sign(target[k]))
            rels.append(None); modes.append('near_null_absolute')
            comp_ok.append(bool(abs_err[k]<=2e-9 and sign_ok))
    step=relnorm(pred[-1],pred[-2])
    vec=relnorm(finest,target)
    hist_res=relnorm(hist,target)
    valid=bool(sig and inv<=2e-11 and np.linalg.norm(target)>1e-10)
    passed=bool(valid and all(comp_ok) and step<=5e-5 and vec<=1e-4 and float(np.max(abs_err))<=2e-7 and hist_res>=1e-2)
    return {
      'gate':'ITER051C-D2R-FRESH-SPHERICAL-REPLACEMENT-VALIDATION','index':index,
      'profile':profile,'radius':r,'target':target.tolist(),'predictions':[v.tolist() for v in pred],
      'finest_prediction':finest.tolist(),'absolute_errors':abs_err.tolist(),
      'component_modes':modes,'ordinary_relative_residuals':rels,'component_pass':comp_ok,
      'vector_relative_residual':vec,'final_step_change':step,
      'historical_plus2_vector_residual':hist_res,'signature_valid':sig,
      'max_inverse_residual':inv,'max_metric_det':det,'control_valid':valid,'lane_pass':passed,
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    if not 0<=a.index<len(PANEL): raise SystemExit('index out of range')
    out=lane(a.index); os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
