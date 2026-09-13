#!/usr/bin/env python3
import argparse,itertools,json,math,os
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from scipy.special import roots_jacobi

import qgr_iter053_compact_support_action as g53
import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051c_full_eom as c
import qgr_iter051b1_weyl3_p_insertion as w3

N=4
A=g53.SUPPORT
EPS=(2.0e-4,1.0e-4,5.0e-5)
HSTEP=5.0e-4


def rel(a,b,floor=1e-30):
    return float(abs(a-b)/max(abs(a),abs(b),floor))


def lane_objects(stream,index):
    if stream=='A': return c.PolyMetric(g53.A_METRIC[index]),g53.CompactPerturbation(g53.A_PERT[index]),g53.A_METRIC[index],g53.A_PERT[index]
    if stream=='B': return it.ConformalMetric(g53.B_METRIC[index]),g53.CompactPerturbation(g53.B_PERT[index]),g53.B_METRIC[index],g53.B_PERT[index]
    if stream=='C': return c.PolyMetric(g53.C_METRIC[index]),g53.CompactPerturbation(g53.C_PERT[index]),g53.C_METRIC[index],g53.C_PERT[index]
    raise ValueError(stream)


def gl_nodes(order):
    z,w=np.polynomial.legendre.leggauss(order)
    return A*z,A*w


def metric_controls(metric,pert,x):
    ok=True; inv=0.0
    g0=metric.jets(x)[0]; h=pert.jets(x)[0]
    for e in (-2*EPS[-1],-EPS[-1],0.0,EPS[-1],2*EPS[-1]):
        g=g0+e*h
        vals=np.linalg.eigvalsh(0.5*(g+g.T))
        ok=ok and bool(np.sum(vals<0)==1 and np.sum(vals>0)==3)
        gi=np.linalg.inv(g); inv=max(inv,float(np.max(np.abs(g@gi-np.eye(N)))))
    return ok,inv


def support_direct(metric,pert,order,u_to_coord=None):
    z,w=gl_nodes(order); totals=np.zeros(len(EPS)); sig=True; inv=0.0
    for inds in itertools.product(range(order),repeat=N):
        u=np.array([z[i] for i in inds],float)
        x=u if u_to_coord is None else np.asarray(u_to_coord(u),float)
        ok,iv=metric_controls(metric,pert,x); sig=sig and ok; inv=max(inv,iv)
        wt=float(np.prod([w[i] for i in inds]))
        for k,e in enumerate(EPS): totals[k]+=wt*g53.direct_density(metric,pert,x,e)
    return {'order':order,'direct':totals.tolist(),'signature_valid':bool(sig),'max_inverse_residual':float(inv)}


def gj_tasks(order):
    z,w=roots_jacobi(order,4.0,4.0)
    for inds in itertools.product(range(order),repeat=N):
        u=np.array([A*z[i] for i in inds],float)
        wt=(A**4)*float(np.prod([w[i] for i in inds]))
        yield u,wt


def weighted_bulk(metric,base_pert,order,u_to_coord=None,p_transform=None,sample=False):
    bulk=0.0; wrong=0.0; sig=True; inv=0.0; max_h=0.0; max_p=0.0; max_w3=0.0
    for u,wt in gj_tasks(order):
        x=u if u_to_coord is None else np.asarray(u_to_coord(u),float)
        s,iv,det=d2n.extended_controls(metric,x); sig=sig and s; inv=max(inv,iv)
        H,z=d2n.assemble_minus5(metric,x,HSTEP)
        p=base_pert.base.jets(u)[0]
        if p_transform is not None: p=np.asarray(p_transform(p),float)
        sg=math.sqrt(-float(np.linalg.det(z['g'])))
        Hwrong=z['A']+z['I']+2.0*sg*z['D']
        bulk+=wt*float(np.einsum('ab,ab->',H,p))
        wrong+=wt*float(np.einsum('ab,ab->',Hwrong,p))
        if sample:
            W3=float(np.real(w3.i3_complex(z['R'],z['g'],np.linalg.inv(z['g']))))
            max_h=max(max_h,float(np.linalg.norm(H))); max_p=max(max_p,float(np.linalg.norm(z['P']))); max_w3=max(max_w3,abs(W3))
    return {'order':order,'bulk':float(bulk),'wrong_bulk':float(wrong),'signature_valid':bool(sig),'max_inverse_residual':float(inv),
            'sample_max_H_norm':float(max_h),'sample_max_P_norm':float(max_p),'sample_max_abs_W3':float(max_w3)}


def collar_control_frame(pert,u_to_coord=None):
    vals=[]; probes=[]
    for axis in range(N):
        for sgn in (-1.0,1.0):
            u=np.zeros(N); u[axis]=sgn*A; probes.append(u)
            u2=np.array([0.07,-0.05,0.03,-0.02]); u2[axis]=sgn*A; probes.append(u2)
    for u in probes:
        x=u if u_to_coord is None else np.asarray(u_to_coord(u),float)
        h,dh,ddh=pert.jets(x); vals.append(max(float(np.max(np.abs(h))),float(np.max(np.abs(dh)))))
    return float(max(vals) if vals else 0.0)


def analyze_generic(metric,pert,u_to_coord=None,p_transform=None):
    d7=support_direct(metric,pert,7,u_to_coord); d8=support_direct(metric,pert,8,u_to_coord)
    g2=weighted_bulk(metric,pert,2,u_to_coord,p_transform); g3=weighted_bulk(metric,pert,3,u_to_coord,p_transform)
    direct=np.array(d8['direct'],float); dstep=rel(direct[-1],direct[-2]); glchange=rel(d7['direct'][-1],direct[-1])
    bchange=rel(g2['bulk'],g3['bulk']); resid=rel(direct[-1],g3['bulk']); cres=rel(d7['direct'][-1],g2['bulk']); qchange=abs(resid-cres)
    wrongres=rel(direct[-1],g3['wrong_bulk']); collar=collar_control_frame(pert,u_to_coord)
    nums=[*d7['direct'],*d8['direct'],g2['bulk'],g3['bulk'],g3['wrong_bulk'],dstep,glchange,bchange,resid,cres,qchange,wrongres,collar]
    valid=bool(d7['signature_valid'] and d8['signature_valid'] and g2['signature_valid'] and g3['signature_valid'] and
               max(d7['max_inverse_residual'],d8['max_inverse_residual'],g2['max_inverse_residual'],g3['max_inverse_residual'])<=3e-11 and collar<=1e-13 and np.isfinite(nums).all())
    passed=bool(valid and abs(direct[-1])>=1e-10 and dstep<=5e-4 and glchange<=5e-4 and bchange<=2e-3 and resid<=3e-3 and qchange<=3e-3 and wrongres>resid)
    return {'direct_GL7':d7,'direct_GL8':d8,'GJ2':g2,'GJ3':g3,'direct_final_step_change':dstep,'direct_GL7_to_GL8_relative_change':glchange,
            'weighted_bulk_GJ2_to_GJ3_relative_change':bchange,'identity_relative_residual':resid,'coarse_identity_relative_residual':cres,
            'coarse_to_fine_identity_residual_change_abs':qchange,'wrong_sign_relative_residual':wrongres,'collar_residual':collar,
            'control_valid':valid,'generic_pass':passed}


def lane_a(i):
    metric,pert,mseed,pseed=lane_objects('A',i); d=analyze_generic(metric,pert)
    d.update({'gate':'ITER053R-WEYL3-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION','stream':'A','index':i,'metric_seed':mseed,'perturbation_seed':pseed})
    d['lane_pass']=bool(d['control_valid'] and d['generic_pass']); return d


def lane_b(i):
    metric,pert,mseed,pseed=lane_objects('B',i)
    d7=support_direct(metric,pert,7); d8=support_direct(metric,pert,8); g2=weighted_bulk(metric,pert,2); g3=weighted_bulk(metric,pert,3,sample=True)
    collar=collar_control_frame(pert); direct=float(d8['direct'][-1]); bulk=float(g3['bulk'])
    nums=[*d7['direct'],*d8['direct'],g2['bulk'],g3['bulk'],g3['sample_max_H_norm'],g3['sample_max_P_norm'],g3['sample_max_abs_W3'],collar]
    valid=bool(d7['signature_valid'] and d8['signature_valid'] and g2['signature_valid'] and g3['signature_valid'] and
               max(d7['max_inverse_residual'],d8['max_inverse_residual'],g2['max_inverse_residual'],g3['max_inverse_residual'])<=3e-11 and collar<=1e-13 and np.isfinite(nums).all())
    passed=bool(valid and abs(direct)<=5e-8 and abs(bulk)<=5e-8 and g3['sample_max_abs_W3']<=2e-10 and g3['sample_max_P_norm']<=3e-9 and g3['sample_max_H_norm']<=3e-7)
    return {'gate':'ITER053R-WEYL3-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION','stream':'B','index':i,'metric_seed':mseed,'perturbation_seed':pseed,
            'direct_GL7':d7,'direct_GL8':d8,'GJ2':g2,'GJ3':g3,'collar_residual':collar,'control_valid':valid,'lane_pass':passed}


def _c_side(arg):
    i,side=arg; metric,pert,mseed,pseed=lane_objects('C',i); L=it.shear(i); Linv=np.linalg.inv(L)
    if side=='base': return analyze_generic(metric,pert)
    mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)
    return analyze_generic(mt,pt,u_to_coord=lambda u:Linv@u,p_transform=lambda p:L.T@p@L)


def lane_c(i):
    metric,pert,mseed,pseed=lane_objects('C',i); L=it.shear(i); Linv=np.linalg.inv(L); mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)
    vals=[]
    for u in (np.zeros(N),np.array([0.08,-0.06,0.05,-0.04])):
        y=Linv@u; g=metric.jets(u)[0]; gt=mt.jets(y)[0]; h=pert.jets(u)[0]; ht=pt.jets(y)[0]
        vals.extend([float(np.max(np.abs(gt-L.T@g@L))),float(np.max(np.abs(ht-L.T@h@L)))])
    tres=max(vals); detres=abs(float(np.linalg.det(L))-1.0)
    with ProcessPoolExecutor(max_workers=2) as ex: base,transformed=list(ex.map(_c_side,[(i,'base'),(i,'transformed')]))
    dcov=rel(base['direct_GL8']['direct'][-1],transformed['direct_GL8']['direct'][-1]); bcov=rel(base['GJ3']['bulk'],transformed['GJ3']['bulk'])
    valid=bool(base['control_valid'] and transformed['control_valid'] and detres<=2e-12 and tres<=3e-11)
    passed=bool(valid and base['generic_pass'] and transformed['generic_pass'] and dcov<=2e-3 and bcov<=2e-3)
    return {'gate':'ITER053R-WEYL3-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION','stream':'C','index':i,'metric_seed':mseed,'perturbation_seed':pseed,
            'det_L':float(np.linalg.det(L)),'transform_algebra_residual':tres,'base':base,'transformed':transformed,
            'direct_covariance_relative_residual':dcov,'bulk_covariance_relative_residual':bcov,'control_valid':valid,'lane_pass':passed}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A','B','C'],required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    lim={'A':4,'B':2,'C':2}[a.stream]
    if not 0<=a.index<lim: raise SystemExit('index out of range')
    out={'A':lane_a,'B':lane_b,'C':lane_c}[a.stream](a.index)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
