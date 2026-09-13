#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np

import qgr_iter053_compact_support_action as g53
import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_full_eom as c

N=4
BOX=g53.BOX
SUPPORT=g53.SUPPORT
EPS=5.0e-5
ORDERS=(3,4,5,6)
DIRECT_ORDERS=(3,4,5)
EXACT_1D=(256.0/315.0)*SUPPORT
EXACT_BUMP=EXACT_1D**4


def rel(a,b,floor=1e-30):
    return float(abs(a-b)/max(abs(a),abs(b),floor))


def lane_objects(stream,index):
    if stream=='A':
        return c.PolyMetric(g53.A_METRIC[index]), g53.CompactPerturbation(g53.A_PERT[index]), g53.A_METRIC[index], g53.A_PERT[index]
    if stream=='B':
        return it.ConformalMetric(g53.B_METRIC[index]), g53.CompactPerturbation(g53.B_PERT[index]), g53.B_METRIC[index], g53.B_PERT[index]
    if stream=='C':
        return c.PolyMetric(g53.C_METRIC[index]), g53.CompactPerturbation(g53.C_PERT[index]), g53.C_METRIC[index], g53.C_PERT[index]
    raise ValueError(stream)


def nodes(order,radius):
    z,w=np.polynomial.legendre.leggauss(order)
    return radius*z, radius*w


def bump_value(x):
    return float(g53.bump_jets(np.asarray(x,float))[0])


def pure_bump_stats(order,radius):
    z,w=nodes(order,radius)
    one_nonzero=sum(abs(float(s))<SUPPORT for s in z)
    count=0; integ=0.0
    for inds in itertools.product(range(order),repeat=N):
        x=np.array([z[i] for i in inds],float)
        B=bump_value(x)
        if B!=0.0: count+=1
        wt=float(np.prod([w[i] for i in inds]))
        integ += wt*B
    return {
      'order':order,'radius':radius,'one_dim_nonzero_nodes':one_nonzero,
      'tensor_nonzero_nodes':count,'tensor_total_nodes':order**N,
      'nonzero_fraction':float(count/(order**N)),
      'pure_bump_integral':float(integ),'pure_bump_relative_error':rel(integ,EXACT_BUMP)
    }


def metric_control(metric,pert,x):
    ok=True; inv=0.0
    h=pert.jets(x)[0]
    g0=metric.jets(x)[0]
    for e in (-2*EPS,-EPS,0.0,EPS,2*EPS):
        g=g0+e*h
        vals=np.linalg.eigvalsh(0.5*(g+g.T))
        ok=ok and bool(np.sum(vals<0)==1 and np.sum(vals>0)==3)
        gi=np.linalg.inv(g)
        inv=max(inv,float(np.max(np.abs(g@gi-np.eye(N)))))
    return ok,inv


def direct_integral(metric,pert,order,radius):
    z,w=nodes(order,radius)
    total=0.0; used=0; sig=True; inv=0.0
    for inds in itertools.product(range(order),repeat=N):
        x=np.array([z[i] for i in inds],float)
        # The compact perturbation and all epsilon metric changes are exactly zero outside support.
        if bump_value(x)==0.0:
            continue
        ok,iv=metric_control(metric,pert,x); sig=sig and ok; inv=max(inv,iv)
        wt=float(np.prod([w[i] for i in inds]))
        total += wt*it.direct_directional(metric,pert,x,EPS)
        used += 1
    return {'order':order,'radius':radius,'value':float(total),'evaluated_nonzero_nodes':used,
            'signature_valid':bool(sig),'max_inverse_residual':float(inv)}


def run(stream,index):
    metric,pert,mseed,pseed=lane_objects(stream,index)
    outer={str(n):pure_bump_stats(n,BOX) for n in ORDERS}
    support={str(n):pure_bump_stats(n,SUPPORT) for n in ORDERS}
    douter={str(n):direct_integral(metric,pert,n,BOX) for n in DIRECT_ORDERS}
    dsupp={str(n):direct_integral(metric,pert,n,SUPPORT) for n in DIRECT_ORDERS}
    d_o34=rel(douter['3']['value'],douter['4']['value'])
    d_s34=rel(dsupp['3']['value'],dsupp['4']['value'])
    d_s45=rel(dsupp['4']['value'],dsupp['5']['value'])
    all_controls=all(v['signature_valid'] and v['max_inverse_residual']<=3e-11 for v in list(douter.values())+list(dsupp.values()))
    outer4err=outer['4']['pure_bump_relative_error']; support5err=support['5']['pure_bump_relative_error']
    improvement=float(outer4err/max(support5err,1e-30))
    confirmed=bool(all_controls and outer['3']['tensor_nonzero_nodes']==1 and outer['4']['tensor_nonzero_nodes']==16 and improvement>=100.0)
    return {
      'gate':'ITER053-QD-COMPACT-SUPPORT-QUADRATURE-CONDITIONING','stream':stream,'index':index,
      'metric_seed':mseed,'perturbation_seed':pseed,'outer':outer,'support':support,
      'direct_outer':douter,'direct_support':dsupp,'direct_outer_3_to_4_change':d_o34,
      'direct_support_3_to_4_change':d_s34,'direct_support_4_to_5_change':d_s45,
      'pure_bump_exact_integral':EXACT_BUMP,'support5_vs_outer4_pure_bump_error_improvement':improvement,
      'control_valid':bool(all_controls),'aliasing_confirmed':confirmed,
      'classification':'PASS_DIAGNOSTIC_ITER053_OUTER_BOX_QUADRATURE_ALIASING_CONFIRMED' if confirmed else 'DIAGNOSTIC_ITER053_QUADRATURE_ALIASING_NOT_CONFIRMED'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A','B','C'],required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    lim={'A':4,'B':2,'C':2}[a.stream]
    if not 0<=a.index<lim: raise SystemExit('index out of range')
    out=run(a.stream,a.index)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['aliasing_confirmed']: raise SystemExit(2)

if __name__=='__main__': main()
