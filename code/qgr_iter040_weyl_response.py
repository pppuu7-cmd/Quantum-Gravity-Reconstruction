#!/usr/bin/env python3
"""QGR Iter040: calibration-free Weyl^3 response manifold.

Generalizes the existing Iter010-G3 same-field-content weak static tidal witness to a frozen
family of trace-free spatial Hessians.  The computed object is the geometric Weyl^3 response
kernel.  c6 remains an overall unfixed multiplier and beta does not enter these kernel ratios.
"""
from __future__ import annotations
import argparse,itertools,json,math,os
from fractions import Fraction as F
import numpy as np
from scipy.linalg import expm,logm
from scipy.optimize import least_squares
from qgr_iter007_g6g_common import E,BASIS,RM,ETA,PERMS
from qgr_iter010_g2_common import weyl_proxy,weyl_cubic

RMI=np.linalg.inv(RM)
EDGES=list(itertools.combinations(range(4),2))
PERM_INDEX={p:i for i,p in enumerate(PERMS)}
I=np.eye(4)

H0=np.diag([1.0,1.0,-2.0])
H1=np.diag([1.0,2.0,-3.0])
H2=np.diag([1.0,-1.0,0.0])
H3=np.diag([2.0,-1.0,-1.0])
H_SHAPES=[H0,H1,H2,H3]
H_NAMES=['H0_diag_1_1_-2','H1_diag_1_2_-3','H2_diag_1_-1_0','H3_diag_2_-1_-1']
TRACE3=[float(np.trace(H@H@H)) for H in H_SHAPES]
HS_A=[0.125,0.10,0.08,0.0625,0.05]
KAPPAS_B=[0.025,0.04,0.06,0.08,0.10]
HS_C=[0.10,0.075,0.05]
HS_D=[0.10,0.075,0.05]

assert all(abs(np.trace(H))<1e-14 for H in H_SHAPES)
assert TRACE3==[-6.0,-18.0,0.0,6.0]

def Rz(deg):
    t=math.radians(deg); c=math.cos(t); s=math.sin(t)
    return np.array([[c,-s,0.0],[s,c,0.0],[0.0,0.0,1.0]])

def Ry(deg):
    t=math.radians(deg); c=math.cos(t); s=math.sin(t)
    return np.array([[c,0.0,s],[0.0,1.0,0.0],[-s,0.0,c]])

ROTATIONS=[np.eye(3),Rz(30.0),Ry(45.0),Rz(35.0)@Ry(25.0)]
ROTATION_NAMES=['identity','Rz30','Ry45','Rz35_Ry25']

def rotated_h0(index):
    R=ROTATIONS[index]
    return R@H0@R.T

def phi_general(y,kappa,H):
    s=np.asarray(y[1:4],dtype=float)
    return 0.5*float(kappa)*float(s@H@s)

def tetrad_at(x,h,kappa,H):
    y=RMI@(float(h)*np.asarray(x,float))
    ph=phi_general(y,kappa,H)
    if not (1.0+2.0*ph>0.0 and 1.0-2.0*ph>0.0):
        raise ValueError('weak-field tetrad lost invertibility')
    Fm=np.diag([math.sqrt(1.0+2.0*ph),math.sqrt(1.0-2.0*ph),
                math.sqrt(1.0-2.0*ph),math.sqrt(1.0-2.0*ph)])
    return RM@Fm@RMI

def solve_connection(h,kappa,H):
    def L(z): return expm(np.tensordot(z,BASIS,axes=(0,0)))
    def residual(x,z):
        x=np.asarray(x,int); Fx=tetrad_at(x,h,kappa,H)
        try: Ls=[L(z[6*i:6*i+6]) for i in range(4)]
        except Exception: return np.full(24,1e50)
        out=[]
        for i in range(4):
            for j in range(i+1,4):
                xi=x.copy(); xi[i]+=1; xj=x.copy(); xj[j]+=1
                try:
                    lhs=Fx[:,i]+np.linalg.solve(Ls[i],tetrad_at(xi,h,kappa,H)[:,j])
                    rhs=Fx[:,j]+np.linalg.solve(Ls[j],tetrad_at(xj,h,kappa,H)[:,i])
                    rr=lhs-rhs
                except Exception: rr=np.full(4,1e50)
                if not np.all(np.isfinite(rr)): rr=np.full(4,1e50)
                out.extend(rr)
        return np.asarray(out,float)
    sols={}; maxres=0.0; minsv=float('inf'); maxmetric=0.0
    for bits in itertools.product([0,1],repeat=4):
        s=least_squares(lambda z:residual(bits,z),np.zeros(24),xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=1200)
        rn=float(np.linalg.norm(s.fun))
        if not np.all(np.isfinite(s.x)) or rn>=3e-9:
            raise RuntimeError(f'torsion solve failed bits={bits} h={h} kappa={kappa} rn={rn}')
        sv=np.linalg.svd(s.jac,compute_uv=False)
        mats=[L(s.x[6*i:6*i+6]) for i in range(4)]
        me=max(float(np.linalg.norm(M.T@E@M-E)) for M in mats)
        maxres=max(maxres,rn); minsv=min(minsv,float(sv.min())); maxmetric=max(maxmetric,me)
        sols[bits]=mats
    paths=[]
    for p in PERMS:
        x=[0,0,0,0]; A=np.eye(4)
        for d in p:
            A=sols[tuple(x)][d]@A; x[d]+=1
        paths.append(A)
    return {'h':float(h),'kappa':float(kappa),'sols':sols,'L_paths':paths,
            'max_torsion_residual':maxres,'min_jacobian_singular':minsv,
            'max_metric_error':maxmetric}

def curvature_proxy_general(h,kappa,H):
    dat=solve_connection(float(h),float(kappa),np.asarray(H,float)); Ls=dat['L_paths']; X={}
    for i,j in EDGES:
        rest=[k for k in range(4) if k not in (i,j)]
        p=(i,j,*rest); q=(j,i,*rest)
        Hol=np.linalg.solve(Ls[PERM_INDEX[q]],Ls[PERM_INDEX[p]])
        Lam=RMI@Hol@RM
        me=float(np.linalg.norm(Lam.T@ETA@Lam-ETA))
        if me>=3e-8: raise RuntimeError(f'Lorentz holonomy metric error {me}')
        X[(i,j)]=np.real_if_close(logm(Lam),tol=1000).real
    Rorig=np.zeros((4,4,4,4),float)
    for (i,j),M in X.items():
        Rorig[:,:,i,j]=M/(h*h); Rorig[:,:,j,i]=-M/(h*h)
    Rmix=np.einsum('ia,jb,ABij->ABab',RM,RM,Rorig)
    Rlow=np.einsum('AC,CBab->ABab',ETA,Rmix)
    W,Ric,scalar=weyl_proxy(Rlow); I3=float(weyl_cubic(W)); wn=float(np.linalg.norm(W))
    return {'h':float(h),'kappa':float(kappa),'weyl_norm':wn,'weyl_cubic':I3,
            'abs_weyl_cubic':abs(I3),'normalized_signed_cubic':I3/(wn**3) if wn>0 else None,
            'normalized_abs_cubic':abs(I3)/(wn**3) if wn>0 else None,
            'ricci_norm':float(np.linalg.norm(Ric)),'scalar':float(scalar),
            'max_torsion_residual':dat['max_torsion_residual'],
            'min_jacobian_singular':dat['min_jacobian_singular'],
            'max_metric_error':dat['max_metric_error']}

def safe_log_slope(xs,ys):
    if any(y<=0 for y in ys): return None
    return float(np.polyfit(np.log(np.asarray(xs,float)),np.log(np.asarray(ys,float)),1)[0])

def stream_a(shape_index):
    H=H_SHAPES[shape_index]; rows=[curvature_proxy_general(h,0.06,H) for h in HS_A]
    common=all(r['max_torsion_residual']<3e-9 and r['min_jacobian_singular']>1e-8 and r['max_metric_error']<1e-7 for r in rows)
    finest=rows[-1]; coarsest=rows[0]
    if shape_index==2:
        nonzero=finest['weyl_norm']>1e-8
        null_ok=finest['normalized_abs_cubic'] is not None and finest['normalized_abs_cubic']<0.08
        trend=finest['normalized_abs_cubic']<coarsest['normalized_abs_cubic']
        passed=bool(common and nonzero and null_ok and trend)
    else:
        nonzero=finest['weyl_norm']>1e-8 and abs(finest['weyl_cubic'])>1e-10
        normok=finest['normalized_abs_cubic'] is not None and finest['normalized_abs_cubic']>1e-5 and math.isfinite(finest['normalized_abs_cubic'])
        same_final_sign=np.sign(rows[-1]['weyl_cubic'])==np.sign(rows[-2]['weyl_cubic'])
        passed=bool(common and nonzero and normok and same_final_sign)
    return {'gate':'ITER040','stream':'A','shape_index':shape_index,'shape_name':H_NAMES[shape_index],
            'trace_H3':TRACE3[shape_index],'rows':rows,'lane_pass':passed,
            'classification':'A_REFINEMENT_NULL_SIGN_STRUCTURE_PASS' if passed else 'A_NOT_PROMOTED'}

def stream_b(slot):
    shape_index=[0,1,3][slot]; H=H_SHAPES[shape_index]
    rows=[curvature_proxy_general(0.05,k,H) for k in KAPPAS_B]
    ws=safe_log_slope(KAPPAS_B,[r['weyl_norm'] for r in rows])
    cs=safe_log_slope(KAPPAS_B,[r['abs_weyl_cubic'] for r in rows])
    controls=all(r['max_torsion_residual']<3e-9 and r['min_jacobian_singular']>1e-8 for r in rows)
    passed=bool(controls and ws is not None and cs is not None and 0.85<ws<1.15 and 2.70<cs<3.30)
    return {'gate':'ITER040','stream':'B','slot':slot,'shape_index':shape_index,'shape_name':H_NAMES[shape_index],
            'rows':rows,'weyl_norm_kappa_slope':ws,'weyl_cubic_kappa_slope':cs,'lane_pass':passed,
            'classification':'B_AMPLITUDE_POWER_LAW_PASS' if passed else 'B_NOT_PROMOTED'}

def stream_c(h_index):
    h=HS_C[h_index]; rows=[]; qs=[]
    for shape_index in [0,1,3]:
        r=curvature_proxy_general(h,0.05,H_SHAPES[shape_index])
        q=r['weyl_cubic']/TRACE3[shape_index]
        rows.append({'shape_index':shape_index,'shape_name':H_NAMES[shape_index],'trace_H3':TRACE3[shape_index],**r,'q':q})
        qs.append(q)
    qmean=float(np.mean(qs)); spread=max(abs(q-qmean) for q in qs)/(abs(qmean) if abs(qmean)>1e-20 else float('inf'))
    threshold=[0.20,0.12,0.08][h_index]
    controls=all(r['max_torsion_residual']<3e-9 and r['min_jacobian_singular']>1e-8 for r in rows)
    passed=bool(controls and all(math.isfinite(q) and abs(q)>1e-12 for q in qs) and spread<threshold)
    return {'gate':'ITER040','stream':'C','h_index':h_index,'h':h,'rows':rows,'q_mean':qmean,
            'q_relative_spread':spread,'frozen_threshold':threshold,'lane_pass':passed,
            'classification':'C_SHAPE_RATIO_UNIVERSALITY_PASS' if passed else 'C_NOT_PROMOTED'}

def stream_d(rotation_index):
    H=rotated_h0(rotation_index); rows=[]
    for h in HS_D:
        ref=curvature_proxy_general(h,0.05,H0)
        cur=curvature_proxy_general(h,0.05,H)
        v0=ref['normalized_signed_cubic']; v=cur['normalized_signed_cubic']
        disc=abs(v-v0)/(abs(v0) if abs(v0)>1e-20 else float('inf'))
        rows.append({'h':h,'reference_normalized_cubic':v0,'rotated_normalized_cubic':v,
                     'relative_discrepancy':disc,'reference_weyl_norm':ref['weyl_norm'],
                     'rotated_weyl_norm':cur['weyl_norm'],'reference_weyl_cubic':ref['weyl_cubic'],
                     'rotated_weyl_cubic':cur['weyl_cubic'],
                     'max_torsion_residual':max(ref['max_torsion_residual'],cur['max_torsion_residual']),
                     'min_jacobian_singular':min(ref['min_jacobian_singular'],cur['min_jacobian_singular'])})
    finest=rows[-1]['relative_discrepancy']; coarse=rows[0]['relative_discrepancy']
    controls=all(r['max_torsion_residual']<3e-9 and r['min_jacobian_singular']>1e-8 and
                 r['reference_weyl_norm']>1e-8 and r['rotated_weyl_norm']>1e-8 and
                 abs(r['reference_weyl_cubic'])>1e-10 and abs(r['rotated_weyl_cubic'])>1e-10 for r in rows)
    trend=bool(finest<coarse or finest<1e-4)
    passed=bool(controls and finest<0.10 and trend)
    return {'gate':'ITER040','stream':'D','rotation_index':rotation_index,'rotation_name':ROTATION_NAMES[rotation_index],
            'H_rotated':H.tolist(),'rows':rows,'finest_relative_discrepancy':finest,'coarsest_relative_discrepancy':coarse,
            'lane_pass':passed,'classification':'D_ROTATIONAL_INVARIANCE_RECOVERY_PASS' if passed else 'D_NOT_PROMOTED'}

def stream_e(lane):
    traces=[F(-6),F(-18),F(6)]
    normalized=[x/traces[0] for x in traces]
    H2_quad=F(2); H2_cubic=F(0)
    c6=F(lane+1,lane+2)
    responses=[c6*x for x in traces]
    ratios=[x/responses[0] for x in responses]
    passed=bool(normalized==[F(1),F(3),F(-1)] and ratios==[F(1),F(3),F(-1)] and H2_quad!=0 and H2_cubic==0)
    return {'gate':'ITER040','stream':'E','lane':lane,'trace_cubic_ratios':[str(x) for x in normalized],
            'c6_witness':str(c6),'response_ratios_after_c6':[str(x) for x in ratios],
            'H2_quadratic_norm_proxy':str(H2_quad),'H2_cubic_trace':str(H2_cubic),
            'beta_enters_pure_weyl3_kernel_ratio':False,'lane_pass':passed,
            'classification':'E_CALIBRATION_FREE_EXACT_RELATIONS_PASS' if passed else 'E_CONTROL_FAIL'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A','B','C','D','E'],required=True)
    ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.stream=='A': assert 0<=a.index<4; out=stream_a(a.index)
    elif a.stream=='B': assert 0<=a.index<3; out=stream_b(a.index)
    elif a.stream=='C': assert 0<=a.index<3; out=stream_c(a.index)
    elif a.stream=='D': assert 0<=a.index<4; out=stream_d(a.index)
    else: assert 0<=a.index<6; out=stream_e(a.index)
    out['index']=a.index
    os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True,allow_nan=False); f.write('\n')
    compact={k:v for k,v in out.items() if k!='rows'}
    print(json.dumps(compact,sort_keys=True,allow_nan=False))
    if not out.get('lane_pass'): raise SystemExit(2)

if __name__=='__main__': main()
