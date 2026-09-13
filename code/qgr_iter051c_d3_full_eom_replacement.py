#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np

import qgr_iter051c_full_eom as c
import qgr_iter051c_d2_sign_heldout as d2
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051b1_weyl3_p_insertion as w3

H5=(2.0e-3,1.0e-3,5.0e-4)
A_SEEDS=[141003,141211,141421,141631]
B_PANEL=[(-0.7,0.2,0.85),(0.2,0.65,1.15),(-0.4,0.9,1.35),(0.55,-0.15,1.6),(1.25,0.35,1.9),(-0.15,0.72,2.4)]
C_TIMES=[0.55,0.85,1.25]
D_SEEDS=[151007,151219,151433]


def relnorm(a,b,floor=1e-14):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(b),floor))


def relscalar(a,b,floor=1e-14):
    return float(abs(a-b)/max(abs(b),floor))


def assembly(metric,x,h):
    H,z=d2n.assemble_minus5(metric,np.asarray(x,float),h)
    return H,z


def hist_plus(z):
    sg=math.sqrt(-float(np.linalg.det(z['g'])))
    return z['A']+z['I']+2.0*sg*z['D']


def lane_a(i):
    metric=c.PolyMetric(A_SEEDS[i]); x=np.zeros(4)
    sig,inv,det=d2n.extended_controls(metric,x)
    rows=[assembly(metric,x,h) for h in H5]
    H,z=rows[-1]; Hp,_=rows[-2]
    out={
      'gate':'ITER051C-D3-FIVEPOINT-FULL-EOM-REPLACEMENT','stream':'A','index':i,'seed':A_SEEDS[i],
      'signature_valid':sig,'max_inverse_residual':inv,'max_metric_det':det,
      'riemann_algebraic_residual':c.riemann_alg(z['R']),'P_algebraic_residual':w3.algebraic_residual(z['P']),
      'H_norm':float(np.linalg.norm(H)),'H_symmetry_residual':float(np.max(np.abs(H-H.T))),
      'H_final_step_change':relnorm(H,Hp),'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'}
    valid=bool(sig and inv<=2e-11 and out['riemann_algebraic_residual']<=2e-9 and out['P_algebraic_residual']<=2e-9)
    passed=bool(valid and out['H_norm']>1e-7 and out['H_symmetry_residual']<=3e-7 and out['H_final_step_change']<=8e-4)
    out['control_valid']=valid; out['lane_pass']=passed; return out


def reduced_bianchi(H,t,p,q):
    a=t**p; b=t**q
    return np.array([-2.0*H[0,0],2.0*a*H[1,1],2.0*b*(H[2,2]+H[3,3])],float)


def lane_b(i):
    p,q,t=B_PANEL[i]; metric=c.BianchiMetric(p,q); x=np.array([t,0,0,0],float)
    sig,inv,det=d2n.extended_controls(metric,x)
    rows=[assembly(metric,x,h) for h in H5]
    pred=[reduced_bianchi(H,t,p,q) for H,z in rows]
    z=rows[-1][1]; hist=reduced_bianchi(hist_plus(z),t,p,q)
    _,EN,EA,EB=c.exact_targets(t,p,q); target=np.array([EN,EA,EB],float)
    cres=[relscalar(pred[-1][k],target[k],1e-14) for k in range(3)]
    vec=relnorm(pred[-1],target); step=relnorm(pred[-1],pred[-2]); hres=relnorm(hist,target)
    out={
      'gate':'ITER051C-D3-FIVEPOINT-FULL-EOM-REPLACEMENT','stream':'B','index':i,'p':p,'q':q,'time':t,
      'prediction':pred[-1].tolist(),'exact_target':target.tolist(),'component_relative_residuals':cres,
      'vector_relative_residual':vec,'final_step_change':step,'historical_plus2_vector_residual':hres,
      'signature_valid':sig,'max_inverse_residual':inv,'max_metric_det':det,'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'}
    valid=bool(sig and inv<=2e-11 and np.min(np.abs(target))>1e-10)
    passed=bool(valid and max(cres)<=1e-3 and vec<=5e-4 and step<=8e-5 and hres>=1e-2)
    out['control_valid']=valid; out['lane_pass']=passed; return out


def lane_c(i):
    metric=d2.FreshFLRW(i); t=C_TIMES[i]; x=np.array([t,0,0,0],float)
    sig,inv,det=d2n.extended_controls(metric,x)
    H,z=assembly(metric,x,H5[-1])
    I3=float(np.real(w3.i3_complex(z['R'],z['g'],np.linalg.inv(z['g']))))
    out={
      'gate':'ITER051C-D3-FIVEPOINT-FULL-EOM-REPLACEMENT','stream':'C','index':i,'time':t,
      'riemann_norm':float(np.linalg.norm(z['R'])),'I3_abs':abs(I3),'P_norm':float(np.linalg.norm(z['P'])),
      'H_norm':float(np.linalg.norm(H)),'signature_valid':sig,'max_inverse_residual':inv,
      'max_metric_det':det,'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'}
    valid=bool(sig and inv<=2e-11 and out['riemann_norm']>1e-6)
    passed=bool(valid and out['I3_abs']<=2e-10 and out['P_norm']<=3e-9 and out['H_norm']<=2e-7)
    out['control_valid']=valid; out['lane_pass']=passed; return out


def lane_d(i):
    base=c.PolyMetric(D_SEEDS[i]); L=c.lorentz(i); trans=c.TransformMetric(base,L); x=np.zeros(4)
    sig0,inv0,_=d2n.extended_controls(base,x); sig1,inv1,_=d2n.extended_controls(trans,x)
    rows=[assembly(base,x,h) for h in H5]; H,z=rows[-1]; Hp,_=rows[-2]
    Ht,zt=assembly(trans,x,H5[-1]); M=np.linalg.inv(L); expected=M@H@M.T
    metric_control=float(np.max(np.abs(trans.jets(x)[0]-L.T@base.jets(x)[0]@L)))
    inv_control=float(np.max(np.abs(M@L-np.eye(4))))
    out={
      'gate':'ITER051C-D3-FIVEPOINT-FULL-EOM-REPLACEMENT','stream':'D','index':i,'seed':D_SEEDS[i],
      'det_L':float(np.linalg.det(L)),'metric_transform_residual':metric_control,'inverse_transform_residual':inv_control,
      'H_norm':float(np.linalg.norm(H)),'H_final_step_change':relnorm(H,Hp),
      'covariance_relative_residual':relnorm(Ht,expected),'signature_valid':bool(sig0 and sig1),
      'max_inverse_residual':max(inv0,inv1),'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'}
    valid=bool(sig0 and sig1 and max(inv0,inv1)<=2e-11 and abs(out['det_L']-1.0)<=2e-12 and metric_control<=2e-11 and inv_control<=2e-11)
    passed=bool(valid and out['H_norm']>1e-7 and out['H_final_step_change']<=8e-4 and out['covariance_relative_residual']<=1.5e-3)
    out['control_valid']=valid; out['lane_pass']=passed; return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices='ABCD',required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    limits={'A':4,'B':6,'C':3,'D':3}
    if not 0<=a.index<limits[a.stream]: raise SystemExit('index outside frozen panel')
    out={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}[a.stream](a.index)
    out['classification']='LANE_PASS' if out['lane_pass'] else 'LANE_FAIL'
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
