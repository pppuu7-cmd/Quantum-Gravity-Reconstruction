#!/usr/bin/env python3
import itertools,json,math,os
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from scipy.special import roots_jacobi

import qgr_iter053_compact_support_action as g53
import qgr_iter053_qd_quadrature_conditioning as qd
import qgr_iter051c_full_eom as c
import qgr_iter051c_d2n_near_null as d2n

A=0.24
HSTEP=5.0e-4
METRIC_SEED=302071
PERT_SEED=312083


def rel(a,b,floor=1e-30):
    return float(abs(a-b)/max(abs(a),abs(b),floor))


def gj_tasks(order):
    z,w=roots_jacobi(order,4.0,4.0)
    tasks=[]
    for inds in itertools.product(range(order),repeat=4):
        x=np.array([A*z[i] for i in inds],float)
        wt=(A**4)*float(np.prod([w[i] for i in inds]))
        tasks.append((x.tolist(),wt))
    return tasks


def bulk_node(arg):
    xlist,wt=arg; x=np.asarray(xlist,float)
    metric=c.PolyMetric(METRIC_SEED)
    pert=g53.CompactPerturbation(PERT_SEED)
    sig,inv,det=d2n.extended_controls(metric,x)
    H,z=d2n.assemble_minus5(metric,x,HSTEP)
    p=pert.base.jets(x)[0]
    sg=math.sqrt(-float(np.linalg.det(z['g'])))
    Hwrong=z['A']+z['I']+2.0*sg*z['D']
    val=float(np.einsum('ab,ab->',H,p))
    wrong=float(np.einsum('ab,ab->',Hwrong,p))
    return wt*val,wt*wrong,bool(sig),float(inv),float(det)


def weighted_bulk(order):
    tasks=gj_tasks(order)
    with ProcessPoolExecutor(max_workers=2) as ex:
        rows=list(ex.map(bulk_node,tasks,chunksize=1))
    bulk=float(sum(r[0] for r in rows)); wrong=float(sum(r[1] for r in rows))
    return {
      'order':order,'nodes':len(rows),'bulk':bulk,'wrong_bulk':wrong,
      'signature_valid':bool(all(r[2] for r in rows)),
      'max_inverse_residual':float(max(r[3] for r in rows)),
      'max_metric_det':float(max(r[4] for r in rows))
    }


def main():
    metric=c.PolyMetric(METRIC_SEED); pert=g53.CompactPerturbation(PERT_SEED)
    direct7=qd.direct_integral(metric,pert,7,A)
    direct8=qd.direct_integral(metric,pert,8,A)
    gj2=weighted_bulk(2); gj3=weighted_bulk(3)
    d8=float(direct8['value']); dchange=rel(direct7['value'],d8)
    bchange=rel(gj2['bulk'],gj3['bulk'])
    identity=rel(gj3['bulk'],d8)
    wrongres=rel(gj3['wrong_bulk'],d8)
    controls=bool(direct7['signature_valid'] and direct8['signature_valid'] and
                  direct7['max_inverse_residual']<=3e-11 and direct8['max_inverse_residual']<=3e-11 and
                  gj2['signature_valid'] and gj3['signature_valid'] and
                  gj2['max_inverse_residual']<=3e-11 and gj3['max_inverse_residual']<=3e-11 and
                  np.isfinite([d8,dchange,gj2['bulk'],gj3['bulk'],gj3['wrong_bulk'],bchange,identity,wrongres]).all())
    promising=bool(controls and dchange<=5e-4 and bchange<=2e-2 and identity<=1e-2 and identity<wrongres and abs(d8)>=1e-10)
    out={
      'gate':'ITER053-QD3-WEIGHTED-BULK-GAUSS-JACOBI-PILOT',
      'metric_seed':METRIC_SEED,'perturbation_seed':PERT_SEED,'support_radius':A,
      'direct_GL7':direct7,'direct_GL8':direct8,'direct_GL7_to_GL8_relative_change':dchange,
      'GJ2':gj2,'GJ3':gj3,'GJ2_to_GJ3_bulk_relative_change':bchange,
      'GJ3_bulk_vs_direct_GL8_relative_residual':identity,
      'GJ3_wrong_sign_vs_direct_GL8_relative_residual':wrongres,
      'control_valid':controls,'promising':promising,
      'classification':('PASS_DIAGNOSTIC_ITER053_WEIGHTED_GJ3_BULK_PILOT_PROMISING' if promising else
                        ('DIAGNOSTIC_ITER053_WEIGHTED_GJ3_BULK_PILOT_NOT_YET_RESOLVED' if controls else 'ITER053_QD3_CONTROL_INVALID')),
      'interpretation_lock':'DIAGNOSTIC PILOT ONLY; NO ITER053 SCIENTIFIC RECLASSIFICATION; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0'
    }
    os.makedirs('iter053-qd3-output',exist_ok=True)
    with open('iter053-qd3-output/result.json','w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not controls: raise SystemExit(3)
    if not promising: raise SystemExit(2)

if __name__=='__main__': main()
