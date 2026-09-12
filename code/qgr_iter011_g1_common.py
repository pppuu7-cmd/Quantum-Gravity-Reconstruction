#!/usr/bin/env python3
"""Common numerical authority for Iter011 G1 torsion-Jacobian audits.

This reuses the frozen Iter010-G3 Weyl-active tetrad and six-generator Lorentz
connection, but retains the exact 24x24 least-squares Jacobian dT/domega at each
cell vertex.  It does not introduce a new action or phase rule.
"""
import itertools, math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
import qgr_iter010_g3_common as g3


def tetrad_shifted(x,h,kappa,y0=None):
    if y0 is None:
        y0=np.zeros(4,float)
    y=np.asarray(y0,float)+g3.RMI@(h*np.asarray(x,float))
    ph=float(g3.phi_minkowski(y,kappa))
    if not (1.0+2.0*ph>0.0 and 1.0-2.0*ph>0.0):
        raise ValueError((h,kappa,y.tolist(),ph))
    Fm=np.diag([math.sqrt(1.0+2.0*ph),math.sqrt(1.0-2.0*ph),math.sqrt(1.0-2.0*ph),math.sqrt(1.0-2.0*ph)])
    return g3.RM@Fm@g3.RMI


def cell_jacobian_record(h,kappa,y0=None):
    def L(z): return expm(np.tensordot(z,g3.BASIS,axes=(0,0)))
    def residual(x,z):
        x=np.asarray(x,int); Fx=tetrad_shifted(x,h,kappa,y0)
        Ls=[L(z[6*i:6*i+6]) for i in range(4)]; out=[]
        for i in range(4):
            for j in range(i+1,4):
                xi=x.copy(); xi[i]+=1; xj=x.copy(); xj[j]+=1
                lhs=Fx[:,i]+np.linalg.solve(Ls[i],tetrad_shifted(xi,h,kappa,y0)[:,j])
                rhs=Fx[:,j]+np.linalg.solve(Ls[j],tetrad_shifted(xj,h,kappa,y0)[:,i])
                out.extend(lhs-rhs)
        return np.asarray(out,float)

    rows=[]
    for bits in itertools.product([0,1],repeat=4):
        s=least_squares(lambda z: residual(bits,z),np.zeros(24),xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=900)
        rn=float(np.linalg.norm(s.fun))
        sv=np.linalg.svd(s.jac,compute_uv=False)
        sign,logabs=np.linalg.slogdet(s.jac)
        if rn>=3e-9 or sv.min()<=0 or sign==0:
            raise AssertionError((bits,h,kappa,rn,float(sv.min()),sign))
        rows.append({'bits':list(bits),'residual':rn,'min_sv':float(sv.min()),'logabsdet':float(logabs),'det_sign':float(sign),'omega_norm':float(np.linalg.norm(s.x))})
    vals=np.array([r['logabsdet'] for r in rows])
    return {
      'h':float(h),'kappa':float(kappa),'y0':np.zeros(4).tolist() if y0 is None else np.asarray(y0,float).tolist(),
      'sum_logabsdet':float(vals.sum()),'mean_logabsdet':float(vals.mean()),
      'max_residual':max(r['residual'] for r in rows),'min_sv':min(r['min_sv'] for r in rows),
      'max_omega_norm':max(r['omega_norm'] for r in rows),'vertices':rows,
    }


def flat_subtracted(h,kappa,y0=None):
    curved=cell_jacobian_record(h,kappa,y0)
    flat=cell_jacobian_record(h,0.0,y0)
    out=dict(curved)
    out['flat_sum_logabsdet']=flat['sum_logabsdet']
    out['delta_sum_logabsdet']=curved['sum_logabsdet']-flat['sum_logabsdet']
    out['delta_mean_logabsdet']=curved['mean_logabsdet']-flat['mean_logabsdet']
    return out
