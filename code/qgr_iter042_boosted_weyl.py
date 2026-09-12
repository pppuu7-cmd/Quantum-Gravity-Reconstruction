#!/usr/bin/env python3
"""QGR Iter042: boosted non-static / magnetic-Weyl covariance bridge.

The underlying weak vacuum tidal geometry is unchanged.  A global Lorentz boost is
applied to the coordinate columns of the same Minkowski tetrad, producing time-space
off-diagonal components and coordinate-time dependence without adding fields.
"""
from __future__ import annotations
import argparse,itertools,json,math,os
import numpy as np
from scipy.linalg import expm,logm
from scipy.optimize import least_squares
from qgr_iter007_g6g_common import E,BASIS,RM,ETA,PERMS
from qgr_iter010_g2_common import weyl_proxy,weyl_cubic
from qgr_iter040_weyl_response import H0,safe_log_slope

RMI=np.linalg.inv(RM)
EDGES=list(itertools.combinations(range(4),2))
PERM_INDEX={p:i for i,p in enumerate(PERMS)}
G0=np.array([[1.00,0.35,-0.20],[0.35,-0.25,0.15],[-0.20,0.15,-0.75]],float)
SHAPES=[H0,G0]
SHAPE_NAMES=['H0_diag_1_1_-2','G0_heldout_offdiag']
V0=np.array([0.15,0.0,0.0]); V1=np.array([0.25,0.0,0.0]); V2=np.array([0.0,0.20,0.0]); V3=np.array([0.16,0.12,0.08])
PRIMARY=[V0,V1,V2,V3]
PAIR_A=[(0,V0),(0,V1),(0,V3),(1,V0),(1,V2),(1,V3)]
PAIR_C=[(0,V0),(0,V2),(1,V0),(1,V3)]
PAIR_D=[(0,V0),(0,V3),(1,V0),(1,V3)]
SPEEDS=[0.08,0.12,0.18,0.24]
DIRECTIONS=[np.array([1.,0.,0.]),np.array([0.,1.,0.]),np.array([0.,0.,1.]),np.ones(3)/math.sqrt(3.0)]
HS=[0.10,0.075,0.05]
KAPPAS=[0.025,0.04,0.06,0.08,0.10]
EPS=np.zeros((3,3,3),float)
EPS[0,1,2]=EPS[1,2,0]=EPS[2,0,1]=1.0
EPS[0,2,1]=EPS[2,1,0]=EPS[1,0,2]=-1.0


def boost_matrix(v):
    v=np.asarray(v,float); v2=float(v@v)
    if v2>=1.0: raise ValueError('superluminal boost')
    if v2<1e-30: return np.eye(4)
    gam=1.0/math.sqrt(1.0-v2)
    L=np.eye(4); L[0,0]=gam; L[0,1:]=-gam*v; L[1:,0]=-gam*v
    L[1:,1:]+=((gam-1.0)/v2)*np.outer(v,v)
    return L


def phi_old(y_old,kappa,H):
    s=np.asarray(y_old[1:4],float)
    return 0.5*float(kappa)*float(s@H@s)


def minkowski_tetrad_boosted(y_new,kappa,H,v):
    Lam=boost_matrix(v); Linv=np.linalg.inv(Lam); yold=Linv@np.asarray(y_new,float)
    ph=phi_old(yold,kappa,H)
    if not (1.0+2.0*ph>0.0 and 1.0-2.0*ph>0.0):
        raise ValueError('weak-field tetrad lost invertibility')
    Fold=np.diag([math.sqrt(1.0+2.0*ph),math.sqrt(1.0-2.0*ph),math.sqrt(1.0-2.0*ph),math.sqrt(1.0-2.0*ph)])
    Fnew=Fold@Linv
    gold=Fold.T@ETA@Fold; target=Linv.T@gold@Linv
    ident=float(np.linalg.norm(Fnew.T@ETA@Fnew-target))
    return Fnew,ident


def tetrad_at(x,h,kappa,H,v):
    ynew=RMI@(float(h)*np.asarray(x,float))
    Fm,_=minkowski_tetrad_boosted(ynew,kappa,H,v)
    return RM@Fm@RMI


def direct_control_errors(h,kappa,H,v):
    Lam=boost_matrix(v)
    lor=float(np.linalg.norm(Lam.T@ETA@Lam-ETA))
    mx=0.0
    sample=set(itertools.product([0,1],repeat=4))
    for bits in list(sample):
        for d in range(4):
            q=list(bits); q[d]+=1; sample.add(tuple(q))
    for x in sample:
        y=RMI@(float(h)*np.asarray(x,float))
        _,e=minkowski_tetrad_boosted(y,kappa,H,v); mx=max(mx,e)
    return lor,mx


def solve_connection(h,kappa,H,v):
    def L(z): return expm(np.tensordot(z,BASIS,axes=(0,0)))
    def residual(x,z):
        x=np.asarray(x,int); Fx=tetrad_at(x,h,kappa,H,v); Ls=[L(z[6*i:6*i+6]) for i in range(4)]; out=[]
        for i in range(4):
            for j in range(i+1,4):
                xi=x.copy(); xi[i]+=1; xj=x.copy(); xj[j]+=1
                lhs=Fx[:,i]+np.linalg.solve(Ls[i],tetrad_at(xi,h,kappa,H,v)[:,j])
                rhs=Fx[:,j]+np.linalg.solve(Ls[j],tetrad_at(xj,h,kappa,H,v)[:,i])
                out.extend(lhs-rhs)
        return np.asarray(out,float)
    sols={}; maxres=0.0; minsv=float('inf'); maxmetric=0.0
    for bits in itertools.product([0,1],repeat=4):
        s=least_squares(lambda z:residual(bits,z),np.zeros(24),xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=1400)
        rn=float(np.linalg.norm(s.fun))
        if not np.all(np.isfinite(s.x)) or rn>=3e-9: raise RuntimeError(f'torsion solve failed {bits} rn={rn}')
        mats=[L(s.x[6*i:6*i+6]) for i in range(4)]; sv=np.linalg.svd(s.jac,compute_uv=False)
        me=max(float(np.linalg.norm(M.T@E@M-E)) for M in mats)
        maxres=max(maxres,rn); minsv=min(minsv,float(sv.min())); maxmetric=max(maxmetric,me); sols[bits]=mats
    paths=[]
    for p in PERMS:
        x=[0,0,0,0]; A=np.eye(4)
        for d in p: A=sols[tuple(x)][d]@A; x[d]+=1
        paths.append(A)
    lor,ident=direct_control_errors(h,kappa,H,v)
    return {'L_paths':paths,'max_torsion_residual':maxres,'min_jacobian_singular':minsv,'max_metric_error':maxmetric,
            'boost_lorentz_error':lor,'boost_metric_identity_error':ident}


def weyl_quadratic(W):
    s=np.diag(ETA)
    signs=np.einsum('a,b,c,d->abcd',s,s,s,s)
    return float(np.sum(W*W*signs))


def electric_magnetic(W):
    Ep=np.asarray(W[0,1:4,0,1:4],float)
    Bp=np.zeros((3,3),float)
    for i,j,k,l in itertools.product(range(3),repeat=4):
        Bp[i,j]+=0.5*EPS[i,k,l]*W[k+1,l+1,0,j+1]
    return Ep,Bp


def curvature_proxy_boosted(h,kappa,H,v):
    dat=solve_connection(float(h),float(kappa),np.asarray(H,float),np.asarray(v,float)); Ls=dat['L_paths']; X={}
    for i,j in EDGES:
        rest=[k for k in range(4) if k not in (i,j)]; p=(i,j,*rest); q=(j,i,*rest)
        Hol=np.linalg.solve(Ls[PERM_INDEX[q]],Ls[PERM_INDEX[p]])
        M=RMI@Hol@RM; me=float(np.linalg.norm(M.T@ETA@M-ETA))
        if me>=3e-8: raise RuntimeError(f'holonomy Lorentz error {me}')
        X[(i,j)]=np.real_if_close(logm(M),tol=1000).real
    Rorig=np.zeros((4,4,4,4),float)
    for (i,j),M in X.items(): Rorig[:,:,i,j]=M/(h*h); Rorig[:,:,j,i]=-M/(h*h)
    Rmix=np.einsum('ia,jb,ABij->ABab',RM,RM,Rorig); Rlow=np.einsum('AC,CBab->ABab',ETA,Rmix)
    W,Ric,scalar=weyl_proxy(Rlow); Epart,Bpart=electric_magnetic(W)
    I2=weyl_quadratic(W); I3=float(weyl_cubic(W)); wn=float(np.linalg.norm(W))
    return {'h':float(h),'kappa':float(kappa),'velocity':np.asarray(v,float).tolist(),'speed':float(np.linalg.norm(v)),
            'weyl_norm':wn,'weyl_quadratic':I2,'weyl_cubic':I3,'abs_weyl_cubic':abs(I3),
            'electric_norm':float(np.linalg.norm(Epart)),'magnetic_norm':float(np.linalg.norm(Bpart)),
            'electric_part':Epart.tolist(),'magnetic_part':Bpart.tolist(),'ricci_norm':float(np.linalg.norm(Ric)),'scalar':float(scalar),
            **{k:dat[k] for k in ['max_torsion_residual','min_jacobian_singular','max_metric_error','boost_lorentz_error','boost_metric_identity_error']}}


def control_ok(r):
    vals=[r['weyl_norm'],r['weyl_quadratic'],r['weyl_cubic'],r['electric_norm'],r['magnetic_norm'],r['max_torsion_residual'],r['min_jacobian_singular'],r['max_metric_error'],r['boost_lorentz_error'],r['boost_metric_identity_error']]
    return bool(all(math.isfinite(float(x)) for x in vals) and r['max_torsion_residual']<3e-9 and r['min_jacobian_singular']>1e-8 and r['max_metric_error']<1e-7 and r['boost_lorentz_error']<1e-12 and r['boost_metric_identity_error']<1e-11)


def relerr(a,b): return abs(float(a)-float(b))/max(abs(float(b)),1e-30)


def stream_a(index):
    si,v=PAIR_A[index]; H=SHAPES[si]; boost=curvature_proxy_boosted(.05,.04,H,v); ref=curvature_proxy_boosted(.05,.04,H,np.zeros(3))
    ratio=boost['magnetic_norm']/max(boost['electric_norm'],1e-30); factor=boost['magnetic_norm']/max(ref['magnetic_norm'],1e-30)
    control=control_ok(boost) and control_ok(ref)
    scientific=boost['magnetic_norm']>1e-8 and ratio>0.01 and (ref['magnetic_norm']<1e-10 or factor>5.0)
    passed=bool(control and scientific)
    return {'gate':'ITER042','stream':'A','index':index,'shape':SHAPE_NAMES[si],'velocity':v.tolist(),'boosted':boost,'unboosted':ref,
            'magnetic_to_electric_ratio':ratio,'magnetic_growth_factor':factor,'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'A_MAGNETIC_WEYL_EMERGENCE_PASS' if passed else ('A_CONTROL_INVALID' if not control else 'A_SCIENTIFIC_NOT_PROMOTED')}


def stream_b(index):
    si,v=PAIR_A[index]; H=SHAPES[si]; rows=[]
    for h in HS:
        b=curvature_proxy_boosted(h,.04,H,v); r=curvature_proxy_boosted(h,.04,H,np.zeros(3))
        rows.append({'h':h,'w2_error':relerr(b['weyl_quadratic'],r['weyl_quadratic']),'w3_error':relerr(b['weyl_cubic'],r['weyl_cubic']),
                     'control_valid':control_ok(b) and control_ok(r),'boosted':b,'unboosted':r})
    control=all(x['control_valid'] for x in rows); c2,f2=rows[0]['w2_error'],rows[-1]['w2_error']; c3,f3=rows[0]['w3_error'],rows[-1]['w3_error']
    trend2=(f2<c2) or (f2<1e-3 and c2<1e-3); trend3=(f3<c3) or (f3<1e-3 and c3<1e-3)
    scientific=f2<.05 and f3<.05 and trend2 and trend3; passed=bool(control and scientific)
    return {'gate':'ITER042','stream':'B','index':index,'shape':SHAPE_NAMES[si],'velocity':v.tolist(),'rows':rows,
            'finest_w2_error':f2,'finest_w3_error':f3,'w2_trend_pass':trend2,'w3_trend_pass':trend3,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'B_SCALAR_LORENTZ_REFINEMENT_PASS' if passed else ('B_CONTROL_INVALID' if not control else 'B_SCIENTIFIC_NOT_PROMOTED')}


def stream_c(index):
    si,v=PAIR_C[index]; H=SHAPES[si]; rows=[]
    for h in HS:
        p=curvature_proxy_boosted(h,.04,H,v); m=curvature_proxy_boosted(h,.04,H,-v)
        bp=np.asarray(p['magnetic_part']); bm=np.asarray(m['magnetic_part']); den=max(.5*(np.linalg.norm(bp)+np.linalg.norm(bm)),1e-30)
        pe=float(np.linalg.norm(bp+bm)/den)
        rows.append({'h':h,'parity_error':pe,'control_valid':control_ok(p) and control_ok(m),'plus':p,'minus':m})
    control=all(x['control_valid'] for x in rows); coarse=rows[0]['parity_error']; fine=rows[-1]['parity_error']
    nonzero=rows[-1]['plus']['magnetic_norm']>1e-8 and rows[-1]['minus']['magnetic_norm']>1e-8
    trend=(fine<coarse) or (fine<1e-3 and coarse<1e-3); scientific=nonzero and fine<.10 and trend; passed=bool(control and scientific)
    return {'gate':'ITER042','stream':'C','index':index,'shape':SHAPE_NAMES[si],'velocity':v.tolist(),'rows':rows,'coarsest_parity_error':coarse,'finest_parity_error':fine,'trend_pass':trend,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'C_BOOST_REVERSAL_MAGNETIC_PARITY_PASS' if passed else ('C_CONTROL_INVALID' if not control else 'C_SCIENTIFIC_NOT_PROMOTED')}


def stream_d(index):
    si,v=PAIR_D[index]; H=SHAPES[si]; rows=[curvature_proxy_boosted(.05,k,H,v) for k in KAPPAS]
    control=all(control_ok(r) for r in rows); s3=safe_log_slope(KAPPAS,[r['abs_weyl_cubic'] for r in rows]); sb=safe_log_slope(KAPPAS,[r['magnetic_norm'] for r in rows])
    scientific=s3 is not None and sb is not None and 2.70<s3<3.30 and .80<sb<1.20; passed=bool(control and scientific)
    return {'gate':'ITER042','stream':'D','index':index,'shape':SHAPE_NAMES[si],'velocity':v.tolist(),'rows':rows,'weyl_cubic_kappa_slope':s3,'magnetic_kappa_slope':sb,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'D_BOOSTED_AMPLITUDE_LAW_PASS' if passed else ('D_CONTROL_INVALID' if not control else 'D_SCIENTIFIC_NOT_PROMOTED')}


def stream_e(index):
    d=DIRECTIONS[index]; rows=[]
    for speed in SPEEDS:
        v=speed*d; r=curvature_proxy_boosted(.05,.04,G0,v); rows.append({'speed':speed,'magnetic_norm':r['magnetic_norm'],'control_valid':control_ok(r),'row':r})
    control=all(x['control_valid'] for x in rows); mags=[x['magnetic_norm'] for x in rows]; monotonic=all(mags[i+1]>mags[i] for i in range(len(mags)-1)); growth=mags[-1]/max(mags[0],1e-30)
    scientific=all(m>1e-8 for m in mags) and monotonic and growth>2.0; passed=bool(control and scientific)
    return {'gate':'ITER042','stream':'E','index':index,'direction':d.tolist(),'rows':rows,'magnetic_monotonic':monotonic,'endpoint_growth':growth,
            'control_valid':control,'scientific_relation_pass':scientific,'lane_pass':passed,
            'classification':'E_SMALL_VELOCITY_MAGNETIC_RESPONSE_PASS' if passed else ('E_CONTROL_INVALID' if not control else 'E_SCIENTIFIC_NOT_PROMOTED')}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCDE'),required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    lim={'A':6,'B':6,'C':4,'D':4,'E':4}[a.stream]; assert 0<=a.index<lim
    out={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d,'E':stream_e}[a.stream](a.index)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,sort_keys=True,allow_nan=False)
    print(json.dumps({k:v for k,v in out.items() if k not in ('rows','boosted','unboosted')},sort_keys=True,allow_nan=False))
if __name__=='__main__': main()
