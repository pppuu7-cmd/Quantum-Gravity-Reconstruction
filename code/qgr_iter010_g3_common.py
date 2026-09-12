#!/usr/bin/env python3
"""Weyl-active weak-curvature background inside the existing QGR second-moment/torsion arena.

The repaired-G9 conformal ansatz e_i(x)=Omega(x) delta_i is generalized to a local
invertible tetrad F(x) with e_i(x)=F(x)[:,i].  No new field components are introduced:
g(x)=F(x)^T E F(x) is still one symmetric 4x4 second moment (10 components), and the
same six-generator E-Lorentz connection plus the same discrete torsion parallelogram
closure is used.

The test metric is a weak static vacuum tidal field in Minkowski coordinates,
Phi=(kappa/2)(x^2+y^2-2z^2).  It is harmonic, so the standard weak-field metric
 g00=1+2Phi, gij=-(1-2Phi)delta_ij
is Ricci-flat at linear order but Weyl-active.  This is a matching-background witness,
not a new fundamental action.
"""
import itertools,math
import numpy as np
from scipy.linalg import expm,logm
from scipy.optimize import least_squares
from qgr_iter007_g6g_common import E,BASIS,RM,ETA,PERMS
from qgr_iter010_g2_common import weyl_proxy,weyl_cubic,pair_symmetry_error

RMI=np.linalg.inv(RM)
EDGES=list(itertools.combinations(range(4),2))
PERM_INDEX={p:i for i,p in enumerate(PERMS)}
I=np.eye(4)

def phi_minkowski(y,kappa):
    return 0.5*kappa*(y[1]*y[1]+y[2]*y[2]-2.0*y[3]*y[3])

def tetrad_at(x,h,kappa):
    y=RMI@(h*np.asarray(x,float))
    ph=float(phi_minkowski(y,kappa))
    assert 1.0+2.0*ph>0.0 and 1.0-2.0*ph>0.0
    Fm=np.diag([math.sqrt(1.0+2.0*ph),math.sqrt(1.0-2.0*ph),math.sqrt(1.0-2.0*ph),math.sqrt(1.0-2.0*ph)])
    return RM@Fm@RMI

def metric_at(x,h,kappa):
    F=tetrad_at(x,h,kappa)
    return F.T@E@F

def solve_connection(h,kappa=0.08):
    def L(z): return expm(np.tensordot(z,BASIS,axes=(0,0)))
    def residual(x,z):
        x=np.asarray(x,int);Fx=tetrad_at(x,h,kappa);Ls=[L(z[6*i:6*i+6]) for i in range(4)];out=[]
        for i in range(4):
            for j in range(i+1,4):
                xi=x.copy();xi[i]+=1;xj=x.copy();xj[j]+=1
                lhs=Fx[:,i]+np.linalg.solve(Ls[i],tetrad_at(xi,h,kappa)[:,j])
                rhs=Fx[:,j]+np.linalg.solve(Ls[j],tetrad_at(xj,h,kappa)[:,i])
                out.extend(lhs-rhs)
        return np.asarray(out)
    sols={};maxres=0.0;minsv=float('inf')
    for bits in itertools.product([0,1],repeat=4):
        s=least_squares(lambda z:residual(bits,z),np.zeros(24),xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=800)
        rn=float(np.linalg.norm(s.fun)); assert rn<3e-9,(bits,h,kappa,rn)
        maxres=max(maxres,rn); minsv=min(minsv,float(np.linalg.svd(s.jac,compute_uv=False).min()))
        sols[bits]=[L(s.x[6*i:6*i+6]) for i in range(4)]
    paths=[]
    for p in PERMS:
        x=[0,0,0,0];A=np.eye(4)
        for d in p:
            A=sols[tuple(x)][d]@A;x[d]+=1
        paths.append(A)
    return {'h':float(h),'kappa':float(kappa),'sols':sols,'L_paths':paths,'max_torsion_residual':maxres,'min_jacobian_singular':minsv}

def plane_logs(h,kappa=0.08):
    dat=solve_connection(h,kappa);Ls=dat['L_paths'];out={}
    for i,j in EDGES:
        rest=[k for k in range(4) if k not in (i,j)]
        p=(i,j,*rest);q=(j,i,*rest)
        H=np.linalg.solve(Ls[PERM_INDEX[q]],Ls[PERM_INDEX[p]])
        Lam=RMI@H@RM
        assert np.linalg.norm(Lam.T@ETA@Lam-ETA)<3e-8
        out[(i,j)]=np.real_if_close(logm(Lam),tol=1000).real
    return dat,out

def curvature_proxy(h,kappa=0.08):
    dat,X=plane_logs(h,kappa)
    Rorig=np.zeros((4,4,4,4),float)
    for (i,j),M in X.items():
        Rorig[:,:,i,j]=M/(h*h);Rorig[:,:,j,i]=-M/(h*h)
    Rmix=np.einsum('ia,jb,ABij->ABab',RM,RM,Rorig)
    Rlow=np.einsum('AC,CBab->ABab',ETA,Rmix)
    return dat,X,Rlow
