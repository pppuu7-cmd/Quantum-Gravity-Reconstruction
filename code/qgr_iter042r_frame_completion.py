#!/usr/bin/env python3
"""Iter042R: diagnose mixed internal/coordinate frame use in boosted Weyl observables."""
from __future__ import annotations
import argparse,itertools,json,math,os
import numpy as np
from scipy.linalg import logm
from qgr_iter010_g2_common import weyl_proxy,weyl_cubic
from qgr_iter042_boosted_weyl import (
    ETA,RM,RMI,EDGES,PERM_INDEX,SHAPES,SHAPE_NAMES,H0,G0,
    V0,V1,V2,V3,PAIR_A,HS,boost_matrix,minkowski_tetrad_boosted,
    solve_connection,weyl_quadratic,electric_magnetic
)

PAIR_C=[(1,V0),(1,V2),(1,V3),(0,V0)]
# Four emergence cases followed by two parity cases.
PAIR_D_EM=[(0,V0),(0,V3),(1,V0),(1,V3)]
PAIR_D_PAR=[(0,V0),(1,V3)]


def relerr(a,b):
    return abs(float(a)-float(b))/max(abs(float(b)),1e-30)


def controls_ok(dat):
    vals=[dat['max_torsion_residual'],dat['min_jacobian_singular'],dat['max_metric_error'],
          dat['boost_lorentz_error'],dat['boost_metric_identity_error']]
    return bool(all(math.isfinite(float(v)) for v in vals)
                and dat['max_torsion_residual']<3e-9
                and dat['min_jacobian_singular']>1e-8
                and dat['max_metric_error']<1e-7
                and dat['boost_lorentz_error']<1e-12
                and dat['boost_metric_identity_error']<1e-11)


def curvature_views(h,kappa,H,v):
    dat=solve_connection(float(h),float(kappa),np.asarray(H,float),np.asarray(v,float))
    Ls=dat['L_paths']; X={}
    for i,j in EDGES:
        rest=[k for k in range(4) if k not in (i,j)]
        p=(i,j,*rest); q=(j,i,*rest)
        Hol=np.linalg.solve(Ls[PERM_INDEX[q]],Ls[PERM_INDEX[p]])
        M=RMI@Hol@RM
        if float(np.linalg.norm(M.T@ETA@M-ETA))>=3e-8:
            raise RuntimeError('holonomy Lorentz control failed')
        X[(i,j)]=np.real_if_close(logm(M),tol=1000).real
    Rorig=np.zeros((4,4,4,4),float)
    for (i,j),M in X.items():
        Rorig[:,:,i,j]=M/(h*h); Rorig[:,:,j,i]=-M/(h*h)
    # First pair remains internal Lorentz-frame indices; last pair becomes coordinate Minkowski axes.
    Rmix=np.einsum('ia,jb,ABij->ABab',RM,RM,Rorig)
    Rmixed_low=np.einsum('AC,CBab->ABab',ETA,Rmix)
    # Complete the first pair into the same boosted-coordinate basis using the base tetrad.
    F0,_=minkowski_tetrad_boosted(np.zeros(4),float(kappa),np.asarray(H,float),np.asarray(v,float))
    Rcoord=np.einsum('Aa,Bb,ABcd->abcd',F0,F0,Rmixed_low)
    Wmixed,Ricm,sm=weyl_proxy(Rmixed_low)
    Wcoord,Ricc,sc=weyl_proxy(Rcoord)
    out={k:dat[k] for k in ['max_torsion_residual','min_jacobian_singular','max_metric_error','boost_lorentz_error','boost_metric_identity_error']}
    out.update({
        'mixed_w2':float(weyl_quadratic(Wmixed)),
        'mixed_w3':float(weyl_cubic(Wmixed)),
        'coord_w2':float(weyl_quadratic(Wcoord)),
        'coord_w3':float(weyl_cubic(Wcoord)),
        'coord_weyl_norm':float(np.linalg.norm(Wcoord)),
        'mixed_ricci_norm':float(np.linalg.norm(Ricm)),
        'coord_ricci_norm':float(np.linalg.norm(Ricc)),
        'mixed_scalar':float(sm),'coord_scalar':float(sc),
    })
    Epart,Bpart=electric_magnetic(Wcoord)
    out.update({'coord_electric_norm':float(np.linalg.norm(Epart)),
                'coord_magnetic_norm':float(np.linalg.norm(Bpart)),
                'coord_electric_part':Epart.tolist(),'coord_magnetic_part':Bpart.tolist()})
    return out,Wcoord


def stream_a(index):
    si=index//4; v=[V0,V1,V2,V3][index%4]; H=SHAPES[si]
    base,W0=curvature_views(.05,.04,H,np.zeros(3))
    Lam=boost_matrix(v); Linv=np.linalg.inv(Lam)
    Wt=np.einsum('pa,qb,rc,sd,pqrs->abcd',Linv,Linv,Linv,Linv,W0)
    w20=float(weyl_quadratic(W0)); w30=float(weyl_cubic(W0))
    w2t=float(weyl_quadratic(Wt)); w3t=float(weyl_cubic(Wt))
    e2=relerr(w2t,w20); e3=relerr(w3t,w30); le=float(np.linalg.norm(Lam.T@ETA@Lam-ETA))
    control=controls_ok(base) and le<1e-12
    scientific=e2<1e-10 and e3<1e-10
    passed=bool(control and scientific)
    return {'gate':'ITER042R','stream':'A','index':index,'shape':SHAPE_NAMES[si],'velocity':v.tolist(),
            'w2_relative_change':e2,'w3_relative_change':e3,'lorentz_error':le,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'A_EXACT_SCALAR_CONTRACTION_PASS' if passed else ('A_CONTROL_INVALID' if not control else 'A_SCALAR_CONTRACTION_FAIL')}


def stream_b(index):
    si,v=PAIR_A[index]; H=SHAPES[si]; rows=[]
    for h in HS:
        b,_=curvature_views(h,.04,H,v); r,_=curvature_views(h,.04,H,np.zeros(3))
        rows.append({'h':h,'w2_error':relerr(b['coord_w2'],r['coord_w2']),
                     'w3_error':relerr(b['coord_w3'],r['coord_w3']),
                     'control_valid':controls_ok(b) and controls_ok(r),'boosted':b,'unboosted':r})
    control=all(x['control_valid'] for x in rows)
    c2,f2=rows[0]['w2_error'],rows[-1]['w2_error']; c3,f3=rows[0]['w3_error'],rows[-1]['w3_error']
    t2=(f2<c2) or (f2<1e-3 and c2<1e-3); t3=(f3<c3) or (f3<1e-3 and c3<1e-3)
    scientific=f2<.05 and f3<.05 and t2 and t3; passed=bool(control and scientific)
    return {'gate':'ITER042R','stream':'B','index':index,'shape':SHAPE_NAMES[si],'velocity':v.tolist(),'rows':rows,
            'finest_w2_error':f2,'finest_w3_error':f3,'w2_trend_pass':t2,'w3_trend_pass':t3,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'B_FRAME_COMPLETED_SCALAR_COVARIANCE_PASS' if passed else ('B_CONTROL_INVALID' if not control else 'B_SCIENTIFIC_NOT_PROMOTED')}


def stream_c(index):
    si,v=PAIR_C[index]; H=SHAPES[si]; rows=[]
    for h in HS:
        b,_=curvature_views(h,.04,H,v); r,_=curvature_views(h,.04,H,np.zeros(3))
        rows.append({'h':h,
                     'mixed_w2_error':relerr(b['mixed_w2'],r['mixed_w2']),
                     'mixed_w3_error':relerr(b['mixed_w3'],r['mixed_w3']),
                     'completed_w2_error':relerr(b['coord_w2'],r['coord_w2']),
                     'completed_w3_error':relerr(b['coord_w3'],r['coord_w3']),
                     'control_valid':controls_ok(b) and controls_ok(r)})
    control=all(x['control_valid'] for x in rows); fine=rows[-1]
    better=(fine['completed_w3_error'] < 0.5*fine['mixed_w3_error']) or fine['completed_w3_error']<1e-3
    scientific=fine['completed_w3_error']<.05 and better; passed=bool(control and scientific)
    return {'gate':'ITER042R','stream':'C','index':index,'shape':SHAPE_NAMES[si],'velocity':v.tolist(),'rows':rows,
            'mixed_finest_w3_error':fine['mixed_w3_error'],'completed_finest_w3_error':fine['completed_w3_error'],
            'attribution_improvement_pass':better,'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'C_MIXED_FRAME_ATTRIBUTION_PASS' if passed else ('C_CONTROL_INVALID' if not control else 'C_ATTRIBUTION_NOT_ESTABLISHED')}


def stream_d(index):
    if index<4:
        si,v=PAIR_D_EM[index]; H=SHAPES[si]; b,_=curvature_views(.05,.04,H,v)
        ratio=b['coord_magnetic_norm']/max(b['coord_electric_norm'],1e-30)
        control=controls_ok(b); scientific=b['coord_magnetic_norm']>1e-8 and ratio>.01; passed=bool(control and scientific)
        return {'gate':'ITER042R','stream':'D','index':index,'kind':'emergence','shape':SHAPE_NAMES[si],'velocity':v.tolist(),
                'magnetic_norm':b['coord_magnetic_norm'],'magnetic_to_electric_ratio':ratio,
                'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
                'classification':'D_CORRECTED_MAGNETIC_EMERGENCE_PASS' if passed else ('D_CONTROL_INVALID' if not control else 'D_SCIENTIFIC_NOT_PROMOTED')}
    si,v=PAIR_D_PAR[index-4]; H=SHAPES[si]; rows=[]
    for h in HS:
        p,_=curvature_views(h,.04,H,v); m,_=curvature_views(h,.04,H,-v)
        bp=np.asarray(p['coord_magnetic_part']); bm=np.asarray(m['coord_magnetic_part'])
        den=max(.5*(np.linalg.norm(bp)+np.linalg.norm(bm)),1e-30); pe=float(np.linalg.norm(bp+bm)/den)
        rows.append({'h':h,'parity_error':pe,'control_valid':controls_ok(p) and controls_ok(m)})
    control=all(x['control_valid'] for x in rows); coarse=rows[0]['parity_error']; fine=rows[-1]['parity_error']
    trend=(fine<coarse) or (fine<1e-3 and coarse<1e-3); scientific=fine<.10 and trend; passed=bool(control and scientific)
    return {'gate':'ITER042R','stream':'D','index':index,'kind':'parity','shape':SHAPE_NAMES[si],'velocity':v.tolist(),'rows':rows,
            'coarsest_parity_error':coarse,'finest_parity_error':fine,'trend_pass':trend,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'D_CORRECTED_MAGNETIC_PARITY_PASS' if passed else ('D_CONTROL_INVALID' if not control else 'D_SCIENTIFIC_NOT_PROMOTED')}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCD'),required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    lim={'A':8,'B':6,'C':4,'D':6}[a.stream]; assert 0<=a.index<lim
    out={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[a.stream](a.index)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,sort_keys=True,allow_nan=False)
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},sort_keys=True,allow_nan=False))
if __name__=='__main__': main()
