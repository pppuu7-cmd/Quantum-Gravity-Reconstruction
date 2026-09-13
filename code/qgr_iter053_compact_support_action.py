#!/usr/bin/env python3
import argparse, itertools, json, math, os
from concurrent.futures import ProcessPoolExecutor
import numpy as np

import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051c_full_eom as c
import qgr_iter051b1_weyl3_p_insertion as w3

N=4
BOX=0.32
SUPPORT=0.24
ORDERS=(3,4)
EPS=(2.0e-4,1.0e-4,5.0e-5)
HSTEP=5.0e-4
A_METRIC=[302071,302303,302537,302771]
A_PERT=[312083,312317,312551,312787]
B_METRIC=[322097,322333]
B_PERT=[332111,332347]
C_METRIC=[342127,342361]
C_PERT=[352139,352373]


def rel(a,b,floor=1e-14):
    return float(abs(a-b)/max(abs(a),abs(b),floor))


def bump1(s):
    a=SUPPORT
    if abs(s)>=a:
        return 0.0,0.0,0.0
    q=1.0-(s/a)**2
    b=q**4
    bp=-8.0*s*q**3/(a*a)
    bpp=-8.0*q**3/(a*a)+48.0*s*s*q*q/(a**4)
    return b,bp,bpp


def bump_jets(x):
    vals=[bump1(float(s)) for s in x]
    b=np.array([v[0] for v in vals]); bp=np.array([v[1] for v in vals]); bpp=np.array([v[2] for v in vals])
    B=float(np.prod(b))
    dB=np.zeros(N); ddB=np.zeros((N,N))
    for a in range(N):
        p=1.0
        for k in range(N): p*=bp[k] if k==a else b[k]
        dB[a]=p
        for q in range(N):
            p2=1.0
            for k in range(N):
                if a==q and k==a: p2*=bpp[k]
                elif k==a or k==q: p2*=bp[k]
                else: p2*=b[k]
            ddB[a,q]=p2
    return B,dB,ddB


class CompactPerturbation:
    def __init__(self,seed): self.base=it.Perturbation(seed)
    def jets(self,x):
        x=np.asarray(x,float)
        p,dp,ddp=self.base.jets(x)
        B,dB,ddB=bump_jets(x)
        h=B*p
        dh=np.empty_like(dp); ddh=np.empty_like(ddp)
        for a in range(N):
            dh[a]=dB[a]*p+B*dp[a]
            for b in range(N):
                ddh[a,b]=ddB[a,b]*p+dB[a]*dp[b]+dB[b]*dp[a]+B*ddp[a,b]
        return h,dh,ddh


def quad(order):
    z,w=np.polynomial.legendre.leggauss(order)
    z=BOX*z; w=BOX*w
    for inds in itertools.product(range(order),repeat=N):
        x=np.array([z[i] for i in inds],float)
        wt=float(np.prod([w[i] for i in inds]))
        yield x,wt


def mapped_point(y,L):
    return np.asarray(y,float) if L is None else np.asarray(L,float)@np.asarray(y,float)


def direct_density(metric,pert,x,eps):
    return it.direct_directional(metric,pert,np.asarray(x,float),eps)


def node_data(metric,pert,x):
    sig,inv,det=it.controls(metric,pert,np.asarray(x,float))
    H,z=d2n.assemble_minus5(metric,np.asarray(x,float),HSTEP)
    h=pert.jets(x)[0]
    sg=math.sqrt(-float(np.linalg.det(z['g'])))
    Hwrong=z['A']+z['I']+2.0*sg*z['D']
    bulk=float(np.einsum('ab,ab->',H,h))
    wrong=float(np.einsum('ab,ab->',Hwrong,h))
    W3=float(np.real(w3.i3_complex(z['R'],z['g'],np.linalg.inv(z['g']))))
    return sig,inv,det,bulk,wrong,float(np.linalg.norm(H)),float(np.linalg.norm(z['P'])),abs(W3)


def integrate(metric,pert,order,map_L=None,collect_controls=True):
    directs=np.zeros(len(EPS)); bulk=0.0; wrong=0.0
    sig=True; inv=0.0; max_h=0.0; max_p=0.0; max_w3=0.0
    for y,wt in quad(order):
        x=mapped_point(y,map_L)
        for k,e in enumerate(EPS): directs[k]+=wt*direct_density(metric,pert,x,e)
        s,iv,det,b,w,hn,pn,w3n=node_data(metric,pert,x)
        bulk+=wt*b; wrong+=wt*w
        sig=sig and s; inv=max(inv,iv); max_h=max(max_h,hn); max_p=max(max_p,pn); max_w3=max(max_w3,w3n)
    return {'direct':directs.tolist(),'bulk':float(bulk),'wrong_bulk':float(wrong),
            'signature_valid':bool(sig),'max_inverse_residual':float(inv),
            'sample_max_H_norm':float(max_h),'sample_max_P_norm':float(max_p),'sample_max_abs_W3':float(max_w3)}


def collar_control(pert):
    vals=[]
    probes=[]
    for axis in range(N):
        for sgn in (-1.0,1.0):
            x=np.zeros(N); x[axis]=sgn*SUPPORT; probes.append(x)
            x2=np.array([0.07,-0.05,0.03,-0.02]); x2[axis]=sgn*SUPPORT; probes.append(x2)
    for x in probes:
        h,dh,ddh=pert.jets(x)
        vals.append(max(float(np.max(np.abs(h))),float(np.max(np.abs(dh)))))
    return float(max(vals) if vals else 0.0)


def generic_metrics(i):
    return c.PolyMetric(A_METRIC[i]),CompactPerturbation(A_PERT[i])


def analyze_generic(metric,pert,map_L=None):
    coarse=integrate(metric,pert,ORDERS[0],map_L)
    fine=integrate(metric,pert,ORDERS[1],map_L)
    direct=np.array(fine['direct'],float)
    dstep=rel(direct[-1],direct[-2],1e-14)
    resid=rel(direct[-1],fine['bulk'],1e-14)
    cres=rel(coarse['direct'][-1],coarse['bulk'],1e-14)
    qchange=abs(resid-cres)
    bchange=rel(fine['bulk'],coarse['bulk'],1e-14)
    wrongres=rel(direct[-1],fine['wrong_bulk'],1e-14)
    valid=bool(coarse['signature_valid'] and fine['signature_valid'] and fine['max_inverse_residual']<=3e-11 and
               np.isfinite([*direct,fine['bulk'],fine['wrong_bulk'],dstep,resid,qchange,bchange,wrongres]).all())
    passed=bool(valid and abs(direct[-1])>=1e-10 and dstep<=5e-4 and resid<=3e-3 and qchange<=3e-3 and bchange<=2e-3 and wrongres>resid)
    return {'coarse':coarse,'fine':fine,'direct_final_step_change':dstep,'identity_relative_residual':resid,
            'coarse_identity_relative_residual':cres,'quadrature_identity_residual_change_abs':qchange,
            'bulk_coarse_to_fine_relative_change':bchange,'wrong_sign_relative_residual':wrongres,
            'control_valid':valid,'generic_pass':passed}


def lane_a(i):
    metric,pert=generic_metrics(i)
    d=analyze_generic(metric,pert)
    collar=collar_control(pert)
    d.update({'gate':'ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION','stream':'A','index':i,
              'metric_seed':A_METRIC[i],'perturbation_seed':A_PERT[i],'collar_residual':collar})
    d['control_valid']=bool(d['control_valid'] and collar<=1e-13)
    d['lane_pass']=bool(d['control_valid'] and d['generic_pass'])
    return d


def lane_b(i):
    metric=it.ConformalMetric(B_METRIC[i]); pert=CompactPerturbation(B_PERT[i])
    coarse=integrate(metric,pert,ORDERS[0]); fine=integrate(metric,pert,ORDERS[1])
    collar=collar_control(pert); direct=float(fine['direct'][-1]); bulk=float(fine['bulk'])
    valid=bool(fine['signature_valid'] and fine['max_inverse_residual']<=3e-11 and collar<=1e-13 and
               np.isfinite([direct,bulk,fine['sample_max_H_norm'],fine['sample_max_P_norm'],fine['sample_max_abs_W3']]).all())
    passed=bool(valid and abs(direct)<=5e-8 and abs(bulk)<=5e-8 and fine['sample_max_abs_W3']<=2e-10 and
                fine['sample_max_P_norm']<=3e-9 and fine['sample_max_H_norm']<=3e-7)
    return {'gate':'ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION','stream':'B','index':i,
            'metric_seed':B_METRIC[i],'perturbation_seed':B_PERT[i],'coarse':coarse,'fine':fine,
            'collar_residual':collar,'control_valid':valid,'lane_pass':passed}


def transform_residuals(metric,pert,L):
    mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)
    vals=[]
    for y in (np.zeros(N),np.array([0.08,-0.06,0.05,-0.04])):
        x=L@y
        g=metric.jets(x)[0]; gt=mt.jets(y)[0]
        h=pert.jets(x)[0]; ht=pt.jets(y)[0]
        vals.append(float(np.max(np.abs(gt-L.T@g@L))))
        vals.append(float(np.max(np.abs(ht-L.T@h@L))))
    return max(vals),mt,pt


def _c_analysis_worker(args):
    i,side=args
    metric=c.PolyMetric(C_METRIC[i]); pert=CompactPerturbation(C_PERT[i]); L=it.shear(i)
    if side=='base':
        return analyze_generic(metric,pert,map_L=L)
    mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)
    return analyze_generic(mt,pt,map_L=None)


def lane_c(i):
    metric=c.PolyMetric(C_METRIC[i]); pert=CompactPerturbation(C_PERT[i]); L=it.shear(i)
    tres,mt,pt=transform_residuals(metric,pert,L)
    # Implementation-only wall-clock repair after the authoritative production C lanes
    # hit the six-hour hosted-runner limit. The two frozen evaluations are independent,
    # use identical seeds/points/orders/thresholds, and are now executed concurrently.
    with ProcessPoolExecutor(max_workers=2) as ex:
        base,transformed=list(ex.map(_c_analysis_worker,[(i,'base'),(i,'transformed')]))
    dcov=rel(base['fine']['direct'][-1],transformed['fine']['direct'][-1],1e-14)
    bcov=rel(base['fine']['bulk'],transformed['fine']['bulk'],1e-14)
    detres=abs(float(np.linalg.det(L))-1.0)
    collar=max(collar_control(pert),collar_control(pt))
    valid=bool(base['control_valid'] and transformed['control_valid'] and detres<=2e-12 and tres<=3e-11 and collar<=1e-13)
    passed=bool(valid and base['generic_pass'] and transformed['generic_pass'] and dcov<=2e-3 and bcov<=2e-3)
    return {'gate':'ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION','stream':'C','index':i,
            'metric_seed':C_METRIC[i],'perturbation_seed':C_PERT[i],'det_L':float(np.linalg.det(L)),
            'transform_algebra_residual':tres,'collar_residual':collar,'base':base,'transformed':transformed,
            'direct_covariance_relative_residual':dcov,'bulk_covariance_relative_residual':bcov,
            'control_valid':valid,'lane_pass':passed}


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
