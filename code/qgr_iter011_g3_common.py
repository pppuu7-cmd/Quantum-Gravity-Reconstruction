#!/usr/bin/env python3
"""Full regular-branch coarea factor for Iter011-G3.

The already-derived finite-branch measure is
    w_coarea ~ j_Haar(L) / |det(dT/domega)|.
This helper evaluates both pieces on the Iter010-G3 Weyl-active tetrad.  The
connection root is numerical, while dT/domega uses Frechet derivatives of exp.
The Lorentz-group exponential-coordinate Haar density is computed from the
adjoint representation, with no fitted normalization (j_Haar(0)=1).
"""
import itertools, math
import numpy as np
from scipy.linalg import expm, expm_frechet
from scipy.optimize import least_squares
import qgr_iter010_g3_common as g3

BITS=list(itertools.product([0,1],repeat=4))
FLAT_DET=11664.0
FLAT_LOGDET=math.log(FLAT_DET)

# Adjoint representation in the already frozen six-generator E-Lorentz basis.
_BMAT=np.stack([B.reshape(-1) for B in g3.BASIS],axis=1)  # 16 x 6
AD=np.zeros((6,6,6),float)  # AD[i,:,j] are coeffs of [B_i,B_j]
MAX_CLOSURE_RESIDUAL=0.0
for i,Bi in enumerate(g3.BASIS):
    for j,Bj in enumerate(g3.BASIS):
        C=Bi@Bj-Bj@Bi
        c,*_=np.linalg.lstsq(_BMAT,C.reshape(-1),rcond=None)
        AD[i,:,j]=c
        MAX_CLOSURE_RESIDUAL=max(MAX_CLOSURE_RESIDUAL,float(np.linalg.norm(_BMAT@c-C.reshape(-1))))
MAX_UNIMODULAR_TRACE=max(abs(float(np.trace(AD[i]))) for i in range(6))

def adjoint(z):
    return np.tensordot(np.asarray(z,float),AD,axes=(0,0))

def haar_log_density(z):
    """log |det int_0^1 exp(-t ad_X) dt|, X=sum z_a B_a."""
    A=adjoint(z)
    K=np.zeros((12,12),float)
    K[:6,:6]=-A
    K[:6,6:]=np.eye(6)
    phi=expm(K)[:6,6:]
    sign,ld=np.linalg.slogdet(phi)
    if sign==0: raise RuntimeError('singular exponential-coordinate Haar Jacobian')
    return float(ld)

def phi_y(y,kappa):
    return float(g3.phi_minkowski(np.asarray(y,float),kappa))

def tetrad_y(y,kappa):
    ph=phi_y(y,kappa)
    if not (1+2*ph>0 and 1-2*ph>0): raise RuntimeError('left weak Lorentzian chart')
    Fm=np.diag([math.sqrt(1+2*ph),math.sqrt(1-2*ph),math.sqrt(1-2*ph),math.sqrt(1-2*ph)])
    return g3.RM@Fm@g3.RMI

def _solve_from_tetrads(Fx,nbr):
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
    rn=float(np.linalg.norm(sol.fun))
    if rn>3e-9: raise RuntimeError(('torsion residual',rn))
    z=sol.x; As,_=unpack(z)
    J=np.zeros((24,24),float); row=0
    for i in range(4):
        for j in range(i+1,4):
            for a,B in enumerate(g3.BASIS):
                dEi=expm_frechet(-As[i],-B,compute_expm=False)
                dEj=expm_frechet(-As[j],-B,compute_expm=False)
                J[row:row+4,6*i+a]=dEi@nbr[i][:,j]
                J[row:row+4,6*j+a]-=dEj@nbr[j][:,i]
            row+=4
    sign,logdet=np.linalg.slogdet(J)
    if sign==0: raise RuntimeError('singular torsion Jacobian')
    hlog=sum(haar_log_density(z[6*i:6*i+6]) for i in range(4))
    sv=np.linalg.svd(J,compute_uv=False)
    return {
      'z':z,'log_torsion_det':float(logdet),'log_haar':float(hlog),
      'log_coarea':float(hlog-logdet),'min_sv':float(sv[-1]),'residual':rn,
    }

def solve_vertex(bits,h,kappa):
    x=np.asarray(bits,int)
    Fx=g3.tetrad_at(x,h,kappa)
    nbr=[]
    for i in range(4):
        xi=x.copy(); xi[i]+=1
        nbr.append(g3.tetrad_at(xi,h,kappa))
    return _solve_from_tetrads(Fx,nbr)

def centered_cell_stats(h,kappa):
    rows=[solve_vertex(b,h,kappa) for b in BITS]
    td=np.array([r['log_torsion_det'] for r in rows])
    hl=np.array([r['log_haar'] for r in rows])
    # Flat reference: log j_Haar=0 and log det J_T=log 11664.
    dt=float(td.mean()-FLAT_LOGDET)
    dh=float(hl.mean())
    return {
      'h':float(h),'kappa':float(kappa),
      'delta_torsion_logdet':dt,
      'delta_haar_logdensity':dh,
      'delta_log_coarea':float(dh-dt),
      'min_sv':float(min(r['min_sv'] for r in rows)),
      'max_residual':float(max(r['residual'] for r in rows)),
    }

def constant_reference_logdet(F):
    # Same local zero-jet tetrad at anchor and all four neighbours. z=0 is exact.
    nbr=[F.copy() for _ in range(4)]
    z=np.zeros(24); As=[np.zeros((4,4)) for _ in range(4)]
    J=np.zeros((24,24),float); row=0
    for i in range(4):
        for j in range(i+1,4):
            for a,B in enumerate(g3.BASIS):
                dE=-B
                J[row:row+4,6*i+a]=dE@nbr[i][:,j]
                J[row:row+4,6*j+a]-=dE@nbr[j][:,i]
            row+=4
    sign,ld=np.linalg.slogdet(J)
    if sign==0: raise RuntimeError('singular constant-reference Jacobian')
    return float(ld)

def generic_local_stats(a,kappa,y0):
    y0=np.asarray(y0,float); F=tetrad_y(y0,kappa)
    nbr=[tetrad_y(y0+g3.RMI@(a*np.eye(4)[i]),kappa) for i in range(4)]
    cur=_solve_from_tetrads(F,nbr)
    ld0=constant_reference_logdet(F)
    # Same-local-tetrad subtraction removes zero-jet frame-coordinate dependence.
    return {
      'a':float(a),'kappa':float(kappa),'y0':[float(v) for v in y0],
      'delta_torsion_local':float(cur['log_torsion_det']-ld0),
      'delta_haar_local':float(cur['log_haar']),
      'delta_log_coarea_local':float(cur['log_haar']-(cur['log_torsion_det']-ld0)),
      'min_sv':cur['min_sv'],'residual':cur['residual'],
    }

def logslope(xs,ys):
    return float(np.polyfit(np.log(np.asarray(xs,float)),np.log(np.abs(np.asarray(ys,float))),1)[0])
