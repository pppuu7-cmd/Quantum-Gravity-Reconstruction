#!/usr/bin/env python3
import argparse,itertools,json,os,math
import numpy as np
from scipy.special import roots_jacobi

import qgr_iter053_compact_support_action as g53
import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051c_full_eom as c

N=4
A=g53.SUPPORT
ORDER=3
HSTEPS=(1.0e-3,5.0e-4,2.5e-4)


def rel(a,b,floor=1e-30):
    return float(abs(a-b)/max(abs(a),abs(b),floor))


def nodes():
    z,w=roots_jacobi(ORDER,4.0,4.0)
    for inds in itertools.product(range(ORDER),repeat=N):
        u=np.array([A*z[i] for i in inds],float)
        wt=(A**4)*float(np.prod([w[i] for i in inds]))
        yield u,wt


def lane(index,hstep):
    metric=c.PolyMetric(g53.C_METRIC[index])
    pert=g53.CompactPerturbation(g53.C_PERT[index])
    L=it.shear(index); Linv=np.linalg.inv(L)
    mt=c.TransformMetric(metric,L)
    detres=abs(float(np.linalg.det(L))-1.0)
    rows=[]; base_sum=0.0; trans_sum=0.0
    max_alg=0.0; max_inv=0.0; sig=True; nonzero=0; max_res=0.0; wrong_max=0.0; max_H_res=0.0
    for u,wt in nodes():
        y=Linv@u
        gb=metric.jets(u)[0]; gt=mt.jets(y)[0]
        max_alg=max(max_alg,float(np.max(np.abs(gt-L.T@gb@L))))
        sb,ib,_=d2n.extended_controls(metric,u); st,itv,_=d2n.extended_controls(mt,y)
        sig=sig and sb and st; max_inv=max(max_inv,ib,itv)
        Hb,_=d2n.assemble_minus5(metric,u,hstep)
        Ht,_=d2n.assemble_minus5(mt,y,hstep)
        p=pert.base.jets(u)[0]; pt=L.T@p@L
        cb=float(np.einsum('ab,ab->',Hb,p)); ct=float(np.einsum('ab,ab->',Ht,pt))
        rr=rel(cb,ct); max_res=max(max_res,rr)
        if max(abs(cb),abs(ct))>=1e-12: nonzero+=1
        base_sum+=wt*cb; trans_sum+=wt*ct
        Hexp=Linv@Hb@Linv.T
        max_H_res=max(max_H_res,float(np.linalg.norm(Ht-Hexp)/max(np.linalg.norm(Ht),np.linalg.norm(Hexp),1e-30)))
        Hwrong=L@Hb@L.T
        cwrong=float(np.einsum('ab,ab->',Hwrong,pt))
        wrong_max=max(wrong_max,rel(ct,cwrong))
        rows.append(rr)
    sumres=rel(base_sum,trans_sum)
    finite=bool(np.isfinite([max_alg,max_inv,max_res,sumres,wrong_max,max_H_res,base_sum,trans_sum,*rows]).all())
    valid=bool(detres<=2e-12 and max_alg<=3e-11 and max_inv<=3e-11 and sig and finite and wrong_max>=1e-3)
    passed=bool(valid and max_res<=2e-3 and sumres<=2e-3 and nonzero>=70)
    return {
      'gate':'ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT','index':index,'hstep':hstep,
      'metric_seed':g53.C_METRIC[index],'perturbation_seed':g53.C_PERT[index],
      'node_count':len(rows),'nontrivial_node_count':nonzero,'det_L':float(np.linalg.det(L)),
      'det_residual':detres,'max_metric_transform_residual':max_alg,'max_inverse_residual':max_inv,
      'signature_valid':bool(sig),'max_nodewise_contraction_relative_residual':max_res,
      'weighted_GJ3_sum_base':base_sum,'weighted_GJ3_sum_transformed':trans_sum,
      'weighted_GJ3_sum_covariance_relative_residual':sumres,
      'max_H_tensor_density_relative_residual_diagnostic':max_H_res,
      'wrong_congruence_max_relative_residual':wrong_max,'control_valid':valid,'lane_pass':passed,
      'claim_lock':'Finite localization only; no compact-support closure, c6, beta=1, quantum or theory-establishment promotion.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); ap.add_argument('--hstep',type=float,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.index not in (0,1) or a.hstep not in HSTEPS: raise SystemExit('frozen panel violation')
    out=lane(a.index,a.hstep); os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
