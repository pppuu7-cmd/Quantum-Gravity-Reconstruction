#!/usr/bin/env python3
"""Finite-cell curvature/Weyl proxy utilities for Iter010 G2.

These utilities intentionally operate on the already-frozen repaired-G9 transport helper.
They construct six adjacent-swap relative holonomies, interpret their logarithms as a
finite-cell curvature two-form proxy, convert the base two-form indices to the same
Minkowski frame, and remove Ricci traces to obtain a Weyl proxy.  This is a diagnostic
of the existing background, not a new microscopic action.
"""
import itertools
import numpy as np
from scipy.linalg import logm
from qgr_iter007_g6g_common import solve_paths,RM,ETA,PERMS

EDGES=list(itertools.combinations(range(4),2))
PERM_INDEX={p:i for i,p in enumerate(PERMS)}

def plane_logs(h):
    dat=solve_paths(h); Ls=dat['L_paths']; out={}
    for i,j in EDGES:
        rest=[k for k in range(4) if k not in (i,j)]
        p=(i,j,*rest); q=(j,i,*rest)
        H=np.linalg.solve(Ls[PERM_INDEX[q]],Ls[PERM_INDEX[p]])
        Lam=np.linalg.inv(RM)@H@RM
        X=np.real_if_close(logm(Lam),tol=1000).real
        out[(i,j)]=X
    return dat,out

def curvature_proxy(h):
    dat,X=plane_logs(h)
    # R^A_{ B i j} in the original tetrahedral/null base directions.
    Rorig=np.zeros((4,4,4,4),float)
    for (i,j),M in X.items():
        Rorig[:,:,i,j]=M/(h*h)
        Rorig[:,:,j,i]=-M/(h*h)
    # f_alpha = sum_i RM[i,alpha] e_i, so transform the base 2-form indices.
    Rmix=np.einsum('ia,jb,ABij->ABab',RM,RM,Rorig)
    # Lower the tangent-vector first index using eta.
    Rlow=np.einsum('AC,CBab->ABab',ETA,Rmix)
    return dat,X,Rlow

def ricci_scalar(R):
    Ric=np.zeros((4,4),float)
    for b in range(4):
        for d in range(4):
            Ric[b,d]=sum(ETA[a,a]*R[a,b,a,d] for a in range(4))
    scalar=sum(ETA[b,b]*Ric[b,b] for b in range(4))
    return Ric,float(scalar)

def weyl_proxy(R):
    Ric,scalar=ricci_scalar(R); g=ETA; W=np.zeros_like(R)
    for a,b,c,d in itertools.product(range(4),repeat=4):
        W[a,b,c,d]=(
            R[a,b,c,d]
            -0.5*(g[a,c]*Ric[d,b]-g[a,d]*Ric[c,b]-g[b,c]*Ric[d,a]+g[b,d]*Ric[c,a])
            +(scalar/6.0)*(g[a,c]*g[d,b]-g[a,d]*g[c,b])
        )
    return W,Ric,scalar

def weyl_cubic(W):
    # C_ab^{ cd } C_cd^{ ef } C_ef^{ ab }; eta is diagonal here.
    Cup=np.zeros_like(W)
    for a,b,c,d in itertools.product(range(4),repeat=4):
        Cup[a,b,c,d]=ETA[c,c]*ETA[d,d]*W[a,b,c,d]
    return float(np.einsum('abcd,cdef,efab',Cup,Cup,Cup))

def pair_symmetry_error(R):
    n=float(np.linalg.norm(R))
    return float(np.linalg.norm(R-np.transpose(R,(2,3,0,1)))/(n if n else 1.0))
