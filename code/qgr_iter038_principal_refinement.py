#!/usr/bin/env python3
"""QGR Iter038: principal refinement regularity and actual fine-to-coarse blocking.

Modes:
  certificate  exact h->0 24x24 Jacobian rank/determinant certificate;
  gap          finite-range principal-branch bridge at frozen compact-domain positions;
  path         fixed-physical-path principal fine-product convergence;
  loop         elementary square holonomy fine-blocking convergence.

Scope is the frozen smooth conformal realization on K=[0,1]^4. This code does not fix beta,
absolute action-phase normalization, c6, or establish a global strong-curvature theorem.
"""
import argparse,json,math,os
import numpy as np
import sympy as sp
from scipy.optimize import least_squares
import qgr_iter036_g36_expanded_patch_persistence as g36

I=np.eye(4); C=g36.C; B=g36.B
PAIRS=[(i,j) for i in range(4) for j in range(i+1,4)]
HS=[0.25,0.125,0.0625,0.03125,0.015625,0.0078125]
NS_PATH=[4,8,16,32,64]
NS_LOOP=[4,8,16,32]
POSITIONS=[
    [0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
    [1,1,1,1],[0.25,0.25,0.25,0.25],[0.5,0.1,0.3,0.7]
]
PLANES=PAIRS


def Omega(x):
    x=np.asarray(x,dtype=float)
    return math.exp(float(g36.a@x+0.5*x@g36.Q@x))


def residual(z,x,h):
    x=np.asarray(x,dtype=float); Om=Omega(x)
    try: L=[g36.L_from(z[6*i:6*i+6]) for i in range(4)]
    except Exception: return np.full(24,1e50)
    out=[]
    for i,j in PAIRS:
        xi=x.copy(); xi[i]+=h; xj=x.copy(); xj[j]+=h
        try:
            lhs=Om*I[:,i]+np.linalg.solve(L[i],Omega(xi)*I[:,j])
            rhs=Om*I[:,j]+np.linalg.solve(L[j],Omega(xj)*I[:,i])
            rr=lhs-rhs
        except Exception: rr=np.full(4,1e50)
        if not np.all(np.isfinite(rr)): rr=np.full(4,1e50)
        out.extend(rr)
    return np.asarray(out,dtype=float)


def solve_principal(x,h,max_nfev=1800):
    try:
        s=least_squares(lambda z:residual(z,x,h),np.zeros(24),
                        xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=max_nfev)
        rn=float(np.linalg.norm(s.fun)); me=max(g36.metric_errors(s.x))
        ok=bool(np.all(np.isfinite(s.x)) and rn<1e-8 and me<1e-7)
        sv=np.linalg.svd(s.jac,compute_uv=False) if ok else np.array([])
        return s.x,rn,me,ok,sv
    except Exception:
        return None,float('inf'),float('inf'),False,np.array([])


def integer_M():
    rows=[]
    for i,j in PAIRS:
        for aa in range(4):
            row=np.zeros(24,dtype=int)
            for m in range(6):
                row[6*i+m]+=int(B[m,aa,j])
                row[6*j+m]-=int(B[m,aa,i])
            rows.append(row)
    return np.asarray(rows,dtype=int)

MINT=integer_M(); MF=MINT.astype(float)


def linear_w(x):
    x=np.asarray(x,dtype=float); grad=g36.a+g36.Q@x
    src=[]
    for i,j in PAIRS:
        for aa in range(4):
            src.append(grad[i]*(1 if aa==j else 0)-grad[j]*(1 if aa==i else 0))
    return np.linalg.solve(MF,np.asarray(src,dtype=float))


def max_L_minus_I(z):
    return float(max(np.linalg.norm(L-I) for L in g36.Ls(z)))


def observed_orders(vals):
    out=[]
    for (h0,v0),(h1,v1) in zip(vals[:-1],vals[1:]):
        out.append(float(math.log(v1/v0)/math.log(h1/h0)) if v0>0 and v1>0 else None)
    return out


def edge_A(z,x,h,direction):
    x=np.asarray(x,dtype=float); xp=x.copy(); xp[direction]+=h
    L=g36.L_from(z[6*direction:6*direction+6])
    return (Omega(x)/Omega(xp))*L


def path_product(base,direction,length,N):
    h=float(length)/N; A=np.eye(4); max_r=0.; max_me=0.; min_sv=float('inf')
    for n in range(N):
        x=np.asarray(base,dtype=float).copy(); x[direction]+=n*h
        z,rn,me,ok,sv=solve_principal(x,h,1600)
        if not ok:
            return None,{'success':False,'failed_step':n,'residual_norm':rn if math.isfinite(rn) else None,
                         'metric_error':me if math.isfinite(me) else None}
        max_r=max(max_r,rn); max_me=max(max_me,me); min_sv=min(min_sv,float(sv.min()))
        A=edge_A(z,x,h,direction)@A
    return A,{'success':True,'N':N,'max_residual':max_r,'max_metric_error':max_me,
              'minimum_jacobian_singular':min_sv}


def diff_sequence(mats,ns):
    return [float(np.linalg.norm(mats[b]-mats[a])) for a,b in zip(ns[:-1],ns[1:])]


def certificate_lane():
    Ms=sp.Matrix(MINT.tolist())
    rank=int(Ms.rank()); det=int(Ms.det())
    sv=np.linalg.svd(MF,compute_uv=False)
    passed=bool(rank==24 and det!=0)
    return {'gate':'ITER038','stream':'certificate','rank':rank,'determinant':det,
            'min_singular_numeric':float(sv.min()),'max_singular_numeric':float(sv.max()),
            'condition_numeric':float(sv.max()/sv.min()),'lane_pass':passed,
            'classification':'EXACT_SMALL_H_JACOBIAN_INVERTIBILITY_CERTIFICATE_PASS' if passed else
                             'EXACT_SMALL_H_JACOBIAN_CERTIFICATE_FAIL',
            'analytic_consequence':'Common invertible h=0 scaled-residual derivative plus analyticity and compact K gives uniform sufficiently-small-h principal IFT branch and positive local Jacobian gap on K; no explicit optimal h0 or global field-space theorem claimed.'}


def gap_lane(index):
    x=np.asarray(POSITIONS[index],dtype=float); w=linear_w(x); rows=[]; ok_all=True
    for h in HS:
        z,rn,me,ok,sv=solve_principal(x,h,2000)
        if not ok:
            ok_all=False; rows.append({'h':h,'success':False,'residual_norm':rn if math.isfinite(rn) else None,
                                       'metric_error':me if math.isfinite(me) else None}); continue
        rows.append({'h':h,'success':True,'residual_norm':rn,'metric_error':me,
                     'min_singular':float(sv.min()),'max_singular':float(sv.max()),
                     'condition':float(sv.max()/sv.min()),'max_L_minus_I':max_L_minus_I(z),
                     'scaled_linear_error':float(np.linalg.norm(z/h-w))})
    vals=[(r['h'],r['max_L_minus_I']) for r in rows if r.get('success')]
    orders=observed_orders(vals) if len(vals)==len(HS) else []
    mins=[r['min_singular'] for r in rows if r.get('success')]
    errs=[r['scaled_linear_error'] for r in rows if r.get('success')]
    pass_gap=bool(ok_all and mins and min(mins)>0.20)
    pass_order=bool(len(orders)==5 and orders[-1] is not None and orders[-2] is not None and orders[-1]>0.8 and orders[-2]>0.8)
    pass_err=bool(len(errs)==6 and errs[-3]>errs[-2]>errs[-1])
    passed=bool(pass_gap and pass_order and pass_err)
    return {'gate':'ITER038','stream':'gap','position_index':index,'position':x.tolist(),'rows':rows,
            'observed_orders':orders,'finite_gap_bridge_ok':pass_gap,'first_order_scaling_ok':pass_order,
            'scaled_linear_error_trend_ok':pass_err,'lane_pass':passed,
            'classification':'PRINCIPAL_FINITE_RANGE_GAP_BRIDGE_PASS' if passed else 'PRINCIPAL_FINITE_RANGE_GAP_BRIDGE_NOT_PROMOTED'}


def path_lane(index):
    direction=index%4
    if index<4: base=np.zeros(4); length=1.0
    else: base=np.full(4,0.25); length=0.5
    mats={}; rows=[]; all_ok=True
    for N in NS_PATH:
        A,r=path_product(base,direction,length,N); rows.append(r)
        if A is None: all_ok=False; break
        mats[N]=A
    diffs=diff_sequence(mats,NS_PATH) if all_ok else []
    dec=bool(len(diffs)==4 and diffs[-1]<diffs[-2]<diffs[-3])
    ratio=diffs[-1]/diffs[-2] if dec and diffs[-2]>0 else None
    passed=bool(all_ok and dec and ratio is not None and ratio<0.75)
    return {'gate':'ITER038','stream':'path','path_index':index,'direction':direction,'base':base.tolist(),
            'length':length,'rows':rows,'successive_product_differences':diffs,
            'final_contraction_ratio':ratio,'lane_pass':passed,
            'classification':'FIXED_PHYSICAL_PATH_FINE_BLOCKING_PASS' if passed else 'FIXED_PHYSICAL_PATH_FINE_BLOCKING_NOT_PROMOTED'}


def square_holonomy(base,i,j,length,N):
    Pi,r1=path_product(base,i,length,N)
    bi=np.asarray(base,dtype=float).copy(); bi[i]+=length
    Pj_i,r2=path_product(bi,j,length,N)
    bj=np.asarray(base,dtype=float).copy(); bj[j]+=length
    Pi_j,r3=path_product(bj,i,length,N)
    Pj,r4=path_product(base,j,length,N)
    if any(P is None for P in (Pi,Pj_i,Pi_j,Pj)):
        return None,{'success':False,'side_rows':[r1,r2,r3,r4]}
    try: H=np.linalg.inv(Pj)@np.linalg.inv(Pi_j)@Pj_i@Pi
    except Exception: return None,{'success':False,'side_rows':[r1,r2,r3,r4]}
    me=float(np.linalg.norm(H.T@C@H-C))
    return H,{'success':True,'N':N,'side_rows':[r1,r2,r3,r4],'metric_error':me,
              'trace':float(np.trace(H)),'trace2':float(np.trace(H@H)),'det':float(np.linalg.det(H))}


def loop_lane(index):
    plane_index=index%6; base_kind=index//6; i,j=PLANES[plane_index]
    base=np.zeros(4) if base_kind==0 else np.full(4,0.25); length=0.5
    mats={}; rows=[]; all_ok=True
    for N in NS_LOOP:
        H,r=square_holonomy(base,i,j,length,N); rows.append(r)
        if H is None or not r.get('success') or r['metric_error']>=1e-7:
            all_ok=False; break
        mats[N]=H
    diffs=diff_sequence(mats,NS_LOOP) if all_ok else []
    dec=bool(len(diffs)==3 and diffs[-1]<diffs[-2])
    ratio=diffs[-1]/diffs[-2] if dec and diffs[-2]>0 else None
    passed=bool(all_ok and dec and ratio is not None and ratio<0.80)
    return {'gate':'ITER038','stream':'loop','loop_index':index,'plane':[i,j],'base':base.tolist(),'length':length,
            'rows':rows,'successive_holonomy_differences':diffs,'final_contraction_ratio':ratio,
            'lane_pass':passed,'classification':'ELEMENTARY_LOOP_FINE_BLOCKING_PASS' if passed else
                                                   'ELEMENTARY_LOOP_FINE_BLOCKING_NOT_PROMOTED'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['certificate','gap','path','loop'],required=True)
    ap.add_argument('--index',type=int,default=0); ap.add_argument('--out',required=True); q=ap.parse_args()
    if q.stream=='certificate': result=certificate_lane()
    elif q.stream=='gap': assert 0<=q.index<8; result=gap_lane(q.index)
    elif q.stream=='path': assert 0<=q.index<8; result=path_lane(q.index)
    else: assert 0<=q.index<12; result=loop_lane(q.index)
    result['index']=q.index
    os.makedirs(os.path.dirname(q.out),exist_ok=True)
    with open(q.out,'w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True,allow_nan=False); f.write('\n')
    compact={k:v for k,v in result.items() if k not in ('rows',)}
    print(json.dumps(compact,sort_keys=True,allow_nan=False))

if __name__=='__main__': main()
