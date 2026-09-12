#!/usr/bin/env python3
"""Independent analytic-Jacobian authority for Iter011-G1.

The torsion-free root is found numerically, but dT/domega is evaluated with the
Frechet derivative of exp(-A), not the least-squares finite-difference Jacobian.
This is intentionally independent of qgr_iter011_g1_common.py's numerical Jacobian.
"""
import itertools, math
import numpy as np
from scipy.linalg import expm, expm_frechet
from scipy.optimize import least_squares
import qgr_iter010_g3_common as g3

BITS=list(itertools.product([0,1],repeat=4))
FLAT_DET=11664.0
FLAT_LOGDET=math.log(FLAT_DET)

def solve_vertex(bits,h,kappa):
    x=np.asarray(bits,int)
    Fx=g3.tetrad_at(x,h,kappa)
    nbr=[]
    for i in range(4):
        xi=x.copy(); xi[i]+=1
        nbr.append(g3.tetrad_at(xi,h,kappa))

    def unpack(z):
        As=[np.tensordot(z[6*i:6*i+6],g3.BASIS,axes=(0,0)) for i in range(4)]
        Eis=[expm(-A) for A in As]
        return As,Eis

    def residual(z):
        _,Eis=unpack(z); out=[]
        for i in range(4):
            for j in range(i+1,4):
                out.extend(Fx[:,i]+Eis[i]@nbr[i][:,j]-Fx[:,j]-Eis[j]@nbr[j][:,i])
        return np.asarray(out,float)

    sol=least_squares(residual,np.zeros(24),xtol=2e-13,ftol=2e-13,gtol=2e-13,max_nfev=1200)
    rn=float(np.linalg.norm(sol.fun)); assert rn<3e-9,(bits,h,kappa,rn)
    As,_=unpack(sol.x)
    J=np.zeros((24,24),float); row=0
    for i in range(4):
        for j in range(i+1,4):
            for a,B in enumerate(g3.BASIS):
                dEi=expm_frechet(-As[i],-B,compute_expm=False)
                dEj=expm_frechet(-As[j],-B,compute_expm=False)
                J[row:row+4,6*i+a]=dEi@nbr[i][:,j]
                J[row:row+4,6*j+a]-=dEj@nbr[j][:,i]
            row+=4
    sign,logdet=np.linalg.slogdet(J); assert sign!=0
    sv=np.linalg.svd(J,compute_uv=False)
    return {'logabsdet':float(logdet),'det_sign':float(sign),'min_sv':float(sv[-1]),'residual':rn}

def stats(h,kappa):
    rows=[solve_vertex(b,h,kappa) for b in BITS]
    logs=np.array([r['logabsdet'] for r in rows])
    return {
      'h':float(h),'kappa':float(kappa),
      'delta_mean_logabsdet':float(logs.mean()-FLAT_LOGDET),
      'mean_logabsdet':float(logs.mean()),
      'min_sv':float(min(r['min_sv'] for r in rows)),
      'max_residual':float(max(r['residual'] for r in rows)),
    }

def parity(h,kappa):
    p=stats(h,kappa);m=stats(h,-kappa)
    a=p['delta_mean_logabsdet'];b=m['delta_mean_logabsdet']
    return {'h':float(h),'kappa':float(kappa),'even':0.5*(a+b),'odd':0.5*(a-b),'plus':p,'minus':m}

def slope(xs,ys):
    return float(np.polyfit(np.log(np.asarray(xs,float)),np.log(np.abs(np.asarray(ys,float))),1)[0])
