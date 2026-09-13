#!/usr/bin/env python3
import argparse, json, os
import numpy as np

import qgr_iter051c_full_eom as c


def reduce_tensor(T,t,p,q):
    a=t**p; b=t**q
    return np.array([-2.0*T[0,0], 2.0*a*T[1,1], 2.0*b*(T[2,2]+T[3,3])],dtype=float)


def relnorm(a,b,floor=1e-14):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),floor))


def run(idx,outpath):
    p,q=c.PQ[idx]; t=c.BT[idx]
    metric=c.BianchiMetric(p,q); x=np.array([t,0,0,0],float)
    sig,inv,_=c.stencil_controls(metric,x)
    rows=[]
    for h in c.HS:
        z=c.assemble(metric,x,h)
        sg=float(np.sqrt(-np.linalg.det(z['g'])))
        rows.append({
            'h':h,
            'a':reduce_tensor(z['A'],t,p,q),
            'i':reduce_tensor(z['I'],t,p,q),
            'j':reduce_tensor(sg*z['D'],t,p,q),
        })
    W,EN,EA,EB=c.exact_targets(t,p,q)
    target=np.array([EN,EA,EB],dtype=float)
    finest=rows[-1]; prev=rows[-2]
    changes={k:relnorm(finest[k],prev[k]) for k in ('a','i','j')}
    h0=finest['a']+finest['i']+2.0*finest['j']
    valid=bool(sig and inv<=2e-11 and np.min(np.abs(target))>1e-10 and max(changes.values())<=5e-4)
    out={
      'gate':'ITER051C-D1-ASSEMBLY-TERM-LOCALIZATION',
      'lane':idx,'p':p,'q':q,'time':t,'W3_exact':W,
      'signature_valid':bool(sig),'max_inverse_residual':float(inv),
      'a_reduced':finest['a'].tolist(),'i_reduced':finest['i'].tolist(),'j_reduced':finest['j'].tolist(),
      'exact_target':target.tolist(),'historical_h0_prediction':h0.tolist(),
      'historical_h0_relative_residual':relnorm(h0,target,1e-12),
      'final_step_changes':changes,'valid':valid,
      'interpretation':'DIAGNOSTIC_ONLY_NOT_REPLACEMENT_AUTHORITY',
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }
    os.makedirs(os.path.dirname(outpath),exist_ok=True)
    with open(outpath,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,sort_keys=True))
    if not valid: raise SystemExit(2)


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    args=ap.parse_args()
    if not 0<=args.lane<6: raise SystemExit('lane outside frozen D1 panel')
    run(args.lane,args.out)
