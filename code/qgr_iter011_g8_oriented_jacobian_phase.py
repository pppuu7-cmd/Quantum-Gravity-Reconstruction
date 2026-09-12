#!/usr/bin/env python3
"""Iter011-G8: oriented torsion/Haar Jacobian phase audit.

Question: after G6/G7 identify the regular coarea correction as an ordinary
analytic measure term, can the *orientation sign* discarded by |det| supply a
parameter-free discrete coherent phase (0 or pi) on the same regular branch?

This is a deliberately narrow kill-test.  A sign flip along a connected path
with nonsingular Jacobians is impossible; therefore we sample deterministic
weak-curvature paths and compare the torsion-Jacobian and exponential Haar
orientation against the same-local-tetrad reference.  A constant relative sign
means there is no geometry-dependent Z2 phase available from this source.
"""
import argparse, json, math
import numpy as np
from scipy.linalg import expm, expm_frechet
from scipy.optimize import least_squares
import qgr_iter010_g3_common as g3
import qgr_iter011_g3_common as g11

AS=np.array([0.12,0.075,0.047,0.030,0.019],float)
KS=np.array([-0.08,-0.04,-0.015,0.015,0.04,0.08],float)


def haar_sign(z):
    A=g11.adjoint(z)
    K=np.zeros((12,12),float)
    K[:6,:6]=-A
    K[:6,6:]=np.eye(6)
    phi=expm(K)[:6,6:]
    s,ld=np.linalg.slogdet(phi)
    if s==0: raise RuntimeError('singular Haar Jacobian')
    return int(s),float(ld)


def solve_signed(Fx,nbr):
    def unpack(z):
        As=[np.tensordot(z[6*i:6*i+6],g3.BASIS,axes=(0,0)) for i in range(4)]
        Es=[expm(-A) for A in As]
        return As,Es
    def residual(z):
        _,Es=unpack(z); out=[]
        for i in range(4):
            for j in range(i+1,4):
                out.extend(Fx[:,i]+Es[i]@nbr[i][:,j]-Fx[:,j]-Es[j]@nbr[j][:,i])
        return np.asarray(out,float)
    sol=least_squares(residual,np.zeros(24),xtol=2e-13,ftol=2e-13,gtol=2e-13,max_nfev=1200)
    rn=float(np.linalg.norm(sol.fun))
    if rn>3e-9: raise RuntimeError(('torsion residual',rn))
    z=sol.x; As,_=unpack(z)
    J=np.zeros((24,24),float); row=0
    for i in range(4):
        for j in range(i+1,4):
            for aa,B in enumerate(g3.BASIS):
                dEi=expm_frechet(-As[i],-B,compute_expm=False)
                dEj=expm_frechet(-As[j],-B,compute_expm=False)
                J[row:row+4,6*i+aa]=dEi@nbr[i][:,j]
                J[row:row+4,6*j+aa]-=dEj@nbr[j][:,i]
            row+=4
    ts,tld=np.linalg.slogdet(J)
    if ts==0: raise RuntimeError('singular torsion Jacobian')
    hs=[]; hlds=[]
    for i in range(4):
        s,ld=haar_sign(z[6*i:6*i+6]); hs.append(s); hlds.append(ld)
    sv=np.linalg.svd(J,compute_uv=False)
    return {'torsion_sign':int(ts),'haar_sign':int(np.prod(hs)),'min_sv':float(sv[-1]),'residual':rn,
            'logabs_torsion':float(tld),'logabs_haar':float(sum(hlds))}


def constant_reference_sign(F):
    nbr=[F.copy() for _ in range(4)]
    J=np.zeros((24,24),float); row=0
    for i in range(4):
        for j in range(i+1,4):
            for aa,B in enumerate(g3.BASIS):
                dE=-B
                J[row:row+4,6*i+aa]=dE@nbr[i][:,j]
                J[row:row+4,6*j+aa]-=dE@nbr[j][:,i]
            row+=4
    s,ld=np.linalg.slogdet(J)
    if s==0: raise RuntimeError('singular reference Jacobian')
    return int(s),float(ld)


def make_points(lane):
    rng=np.random.default_rng(881173+104729*lane)
    pts=[]
    while len(pts)<3:
        y=rng.uniform(-0.095,0.095,size=4)
        # keep away from accidental near-zero vectors but well inside weak chart
        if np.linalg.norm(y)>0.045: pts.append(y)
    return pts

ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); a=ap.parse_args()
rows=[]; relative_signs=[]; minsv=1e9; maxres=0.0
for pi,y0 in enumerate(make_points(a.lane)):
    for k in KS:
        F=g11.tetrad_y(y0,float(k)); rs,_=constant_reference_sign(F)
        for spacing in AS:
            nbr=[g11.tetrad_y(y0+g3.RMI@(float(spacing)*np.eye(4)[i]),float(k)) for i in range(4)]
            r=solve_signed(F,nbr)
            rel=int(r['haar_sign']*r['torsion_sign']*rs)  # inverse has same +/- sign
            relative_signs.append(rel); minsv=min(minsv,r['min_sv']); maxres=max(maxres,r['residual'])
            rows.append({'point':pi,'kappa':float(k),'a':float(spacing),'torsion_sign':r['torsion_sign'],
                         'haar_sign':r['haar_sign'],'reference_torsion_sign':rs,'relative_coarea_orientation':rel,
                         'min_sv':r['min_sv'],'residual':r['residual']})
uniq=sorted(set(relative_signs)); flips=sum(relative_signs[i]!=relative_signs[i-1] for i in range(1,len(relative_signs)))
regular=(minsv>0.20 and maxres<1e-9)
constant=(len(uniq)==1)
classification=('NO_GEOMETRY_DEPENDENT_Z2_PHASE_ON_SAMPLED_REGULAR_BRANCH' if regular and constant
                else 'ORIENTATION_STRUCTURE_REQUIRES_FOLLOWUP')
out={'gate':'ITER011-G8-ORIENTED-JACOBIAN-PHASE','lane':a.lane,'samples':len(rows),
     'unique_relative_orientations':uniq,'sequential_sign_changes':int(flips),'min_sv':float(minsv),'max_residual':float(maxres),
     'regular_branch_guard':bool(regular),'classification':classification,'rows':rows,
     'guard':'A constant orientation sign rules out only a geometry-dependent discrete 0/pi phase from the already-derived regular coarea/Haar Jacobian. It does not exclude a separately derived Lorentzian microscopic phase/action.'}
print(json.dumps(out,sort_keys=True))
