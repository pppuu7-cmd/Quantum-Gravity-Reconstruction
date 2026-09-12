#!/usr/bin/env python3
"""QGR Iter041: preregistered held-out Weyl^3 generalization stress.

No beta/c6 fit occurs here.  The numerical object is the existing Iter040 finite-cell
Weyl^3 response kernel evaluated on new off-diagonal trace-free tidal Hessians and
new held-out rotations/null profiles.
"""
from __future__ import annotations
import argparse,json,math,os
import numpy as np
from qgr_iter040_weyl_response import (
    curvature_proxy_general,H0,H2,Rz,Ry,safe_log_slope
)

G0=np.array([[1.00,0.35,-0.20],[0.35,-0.25,0.15],[-0.20,0.15,-0.75]],float)
G1=np.array([[0.70,-0.40,0.30],[-0.40,0.80,-0.10],[0.30,-0.10,-1.50]],float)
G2=np.array([[1.40,0.25,0.45],[0.25,-0.90,-0.35],[0.45,-0.35,-0.50]],float)
G3=np.array([[0.45,0.55,-0.25],[0.55,0.35,0.40],[-0.25,0.40,-0.80]],float)
G4=np.array([[1.10,-0.20,0.50],[-0.20,-0.30,0.25],[0.50,0.25,-0.80]],float)
G5=np.array([[0.90,0.45,0.10],[0.45,-1.20,-0.30],[0.10,-0.30,0.30]],float)
G_SHAPES=[G0,G1,G2,G3,G4,G5]
G_NAMES=[f'G{i}_heldout_offdiag' for i in range(6)]
G_TRACE3=[float(np.trace(H@H@H)) for H in G_SHAPES]
EXPECTED_TRACE3=[0.737625,-1.965,1.77975,-0.263625,0.75675,-1.44225]
for H,t,e in zip(G_SHAPES,G_TRACE3,EXPECTED_TRACE3):
    assert abs(float(np.trace(H)))<2e-14
    assert np.allclose(H,H.T,atol=0,rtol=0)
    assert abs(t-e)<2e-12,(t,e)
    assert abs(t)>1e-8

HS=[0.10,0.075,0.05]
KAPPAS=[0.025,0.04,0.06,0.08,0.10]
AMP_SHAPE_INDICES=[0,1,2,5]
NULL_ROTATIONS=[Rz(17.0),Ry(31.0),Rz(23.0)@Ry(19.0),Rz(47.0)@Ry(28.0)]
NULL_ROT_NAMES=['Rz17','Ry31','Rz23_Ry19','Rz47_Ry28']
G0_ROTATIONS=[Rz(13.0),Ry(29.0),Rz(37.0)@Ry(21.0),Rz(53.0)@Ry(34.0)]
G0_ROT_NAMES=['Rz13','Ry29','Rz37_Ry21','Rz53_Ry34']


def controls_ok(r):
    vals=[r.get('weyl_norm'),r.get('weyl_cubic'),r.get('max_torsion_residual'),
          r.get('min_jacobian_singular'),r.get('max_metric_error')]
    return bool(all(v is not None and math.isfinite(float(v)) for v in vals)
                and r['max_torsion_residual']<3e-9
                and r['min_jacobian_singular']>1e-8
                and r['max_metric_error']<1e-7)


def relerr(a,b):
    if not (math.isfinite(float(a)) and math.isfinite(float(b))) or abs(float(b))<=1e-20:
        return float('inf')
    return abs(float(a)-float(b))/abs(float(b))


def q_for(H,h,kappa):
    tr3=float(np.trace(H@H@H))
    assert abs(tr3)>1e-12
    r=curvature_proxy_general(float(h),float(kappa),H)
    q=float(r['weyl_cubic']/tr3)
    return r,q,tr3


def stream_a(index):
    H=G_SHAPES[index]
    r,q,tr3=q_for(H,0.05,0.04)
    ref,q0,_=q_for(H0,0.05,0.04)
    err=relerr(q,q0)
    control=controls_ok(r) and controls_ok(ref)
    scientific=bool(math.isfinite(q) and abs(q)>1e-12 and r['weyl_norm']>1e-8 and err<0.02)
    passed=bool(control and scientific)
    return {'gate':'ITER041','stream':'A','index':index,'shape_name':G_NAMES[index],
            'trace_H3':tr3,'q':q,'q_H0_control':q0,'relative_q_error':err,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'A_HELDOUT_SHAPE_TRANSFER_PASS' if passed else ('A_CONTROL_INVALID' if not control else 'A_SCIENTIFIC_NOT_PROMOTED'),
            'row':r,'reference_row':ref}


def stream_b(index):
    H=G_SHAPES[index]; rows=[]
    for h in HS:
        r,q,tr3=q_for(H,h,0.04)
        ref,q0,_=q_for(H0,h,0.04)
        rows.append({'h':h,'q':q,'q_H0_control':q0,'relative_q_error':relerr(q,q0),
                     'control_valid':controls_ok(r) and controls_ok(ref),'row':r,'reference_row':ref})
    control=all(x['control_valid'] for x in rows)
    coarse=rows[0]['relative_q_error']; fine=rows[-1]['relative_q_error']
    trend=bool(fine<coarse or (fine<1e-4 and coarse<1e-4))
    scientific=bool(math.isfinite(fine) and fine<0.02 and trend)
    passed=bool(control and scientific)
    return {'gate':'ITER041','stream':'B','index':index,'shape_name':G_NAMES[index],
            'trace_H3':G_TRACE3[index],'rows':rows,'coarsest_relative_q_error':coarse,
            'finest_relative_q_error':fine,'trend_pass':trend,'control_valid':control,
            'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'B_HELDOUT_REFINEMENT_TRANSFER_PASS' if passed else ('B_CONTROL_INVALID' if not control else 'B_SCIENTIFIC_NOT_PROMOTED')}


def stream_c(index):
    shape_index=AMP_SHAPE_INDICES[index]; H=G_SHAPES[shape_index]
    rows=[curvature_proxy_general(0.05,k,H) for k in KAPPAS]
    control=all(controls_ok(r) for r in rows)
    ws=safe_log_slope(KAPPAS,[r['weyl_norm'] for r in rows])
    cs=safe_log_slope(KAPPAS,[r['abs_weyl_cubic'] for r in rows])
    scientific=bool(ws is not None and cs is not None and 0.85<ws<1.15 and 2.70<cs<3.30)
    passed=bool(control and scientific)
    return {'gate':'ITER041','stream':'C','index':index,'shape_index':shape_index,
            'shape_name':G_NAMES[shape_index],'rows':rows,'weyl_norm_kappa_slope':ws,
            'weyl_cubic_kappa_slope':cs,'control_valid':control,
            'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'C_HELDOUT_AMPLITUDE_LAW_PASS' if passed else ('C_CONTROL_INVALID' if not control else 'C_SCIENTIFIC_NOT_PROMOTED')}


def stream_d(index):
    R=NULL_ROTATIONS[index]; H=R@H2@R.T
    assert abs(float(np.trace(H@H@H)))<2e-12
    rows=[]
    for h in HS:
        r=curvature_proxy_general(h,0.05,H)
        rows.append({'h':h,**r})
    control=all(controls_ok(r) for r in rows)
    coarse=float(rows[0]['normalized_abs_cubic']); fine=float(rows[-1]['normalized_abs_cubic'])
    trend=bool(fine<coarse or (fine<1e-5 and coarse<1e-5))
    scientific=bool(rows[-1]['weyl_norm']>1e-8 and fine<0.02 and trend)
    passed=bool(control and scientific)
    return {'gate':'ITER041','stream':'D','index':index,'rotation_name':NULL_ROT_NAMES[index],
            'H_rotated':H.tolist(),'trace_H3':float(np.trace(H@H@H)),
            'coarsest_normalized_abs_cubic':coarse,'finest_normalized_abs_cubic':fine,
            'trend_pass':trend,'rows':rows,'control_valid':control,
            'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'D_HELDOUT_ROTATED_NULL_PASS' if passed else ('D_CONTROL_INVALID' if not control else 'D_SCIENTIFIC_NOT_PROMOTED')}


def stream_e(index):
    R=G0_ROTATIONS[index]; H=R@G0@R.T; rows=[]
    for h in HS:
        ref=curvature_proxy_general(h,0.04,G0)
        cur=curvature_proxy_general(h,0.04,H)
        v0=float(ref['normalized_signed_cubic']); v=float(cur['normalized_signed_cubic'])
        rows.append({'h':h,'reference_normalized_signed_cubic':v0,
                     'rotated_normalized_signed_cubic':v,
                     'relative_rotation_discrepancy':relerr(v,v0),
                     'reference_row':ref,'rotated_row':cur,
                     'control_valid':controls_ok(ref) and controls_ok(cur)})
    control=all(x['control_valid'] for x in rows)
    coarse=rows[0]['relative_rotation_discrepancy']; fine=rows[-1]['relative_rotation_discrepancy']
    trend=bool(fine<coarse or (fine<1e-4 and coarse<1e-4))
    scientific=bool(math.isfinite(fine) and fine<0.02 and trend)
    passed=bool(control and scientific)
    return {'gate':'ITER041','stream':'E','index':index,'rotation_name':G0_ROT_NAMES[index],
            'H_rotated':H.tolist(),'coarsest_relative_rotation_discrepancy':coarse,
            'finest_relative_rotation_discrepancy':fine,'trend_pass':trend,'rows':rows,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'E_HELDOUT_ROTATION_COVARIANCE_PASS' if passed else ('E_CONTROL_INVALID' if not control else 'E_SCIENTIFIC_NOT_PROMOTED')}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',choices=['A','B','C','D','E'],required=True)
    ap.add_argument('--index',type=int,required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    limits={'A':6,'B':6,'C':4,'D':4,'E':4}
    assert 0<=a.index<limits[a.stream]
    out={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d,'E':stream_e}[a.stream](a.index)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,sort_keys=True,allow_nan=False)
    print(json.dumps({k:v for k,v in out.items() if k not in ('rows','row','reference_row','H_rotated')},sort_keys=True,allow_nan=False))

if __name__=='__main__':
    main()
