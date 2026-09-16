#!/usr/bin/env python3
"""Exact degree-12 directional Einstein operator for Iter057AM.

For a pure degree-12 metric direction h12, the degree-12 variation of Einstein
around the frozen held-out background depends only on the quadratic metric
layer G2.  This module evaluates that bilinear term directly.  It is not an
authority until fixed controls 0,557,1113 agree coefficient-for-coefficient
with the full nonlinear held-out finite difference frozen in Iter057AM.
"""
import argparse,json,hashlib
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as sp

import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ad_branch_obstruction as ad
import qgr_iter057am_heldout_obstruction_worker as w

PREREG=w.PREREG
CONTROLS=w.CONTROL_INDICES


def pzero(): return z.pmat()

def metric_minus_eta(g):
    s=z.pmat()
    for a,b in product(range(4),repeat=2):
        s[a][b]=dict(g[a][b])
        if a==b:s[a][b]=z.sub(s[a][b],z.const(z.ETA[a]))
    return s

def direction_metric(v,a12):
    h=z.pmat(); ad.add_direction(h,v,a12); return h

def raised(m):
    out=z.pmat()
    for a,b in product(range(4),repeat=2):out[a][b]=z.scale(m[a][b],F(z.ETA[a]*z.ETA[b]))
    return out

def Ctensor(m):
    C=[[[{} for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for d,b,c in product(range(4),repeat=3):
        C[d][b][c]=z.add(z.add(z.deriv(m[d][c],b),z.deriv(m[d][b],c)),z.neg(z.deriv(m[b][c],d)))
    return C

def gamma_eta(C):
    G=[[[{} for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,c in product(range(4),repeat=3):G[a][b][c]=z.scale(C[a][b][c],F(z.ETA[a],2))
    return G

def gamma13(s,h,Cs,Ch):
    # k^{ad}=-(eta*s*eta)^{ad}; delta g^{-1,ad}=-h^{ad} at leading order.
    sr=raised(s);hr=raised(h);out=[[[{} for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,c in product(range(4),repeat=3):
        q={}
        for d in range(4):
            q=z.add(q,z.mul(z.scale(sr[a][d],-1),Ch[d][b][c],13))
            q=z.add(q,z.mul(z.scale(hr[a][d],-1),Cs[d][b][c],13))
        out[a][b][c]=z.scale(z.homog(q,13),F(1,2))
    return out

def ricci_from_derivative(G,degree):
    R=z.pmat()
    for b,d in product(range(4),repeat=2):
        q={}
        for a in range(4):q=z.add(q,z.sub(z.deriv(G[a][d][b],a),z.deriv(G[a][a][b],d)))
        R[b][d]=z.homog(q,degree)
    return R

def directional_einstein12(seed2,h):
    s=metric_minus_eta(seed2);Cs=Ctensor(s);Ch=Ctensor(h)
    Gs=gamma_eta(Cs);Gh11=gamma_eta(Ch);Gh13=gamma13(s,h,Cs,Ch)
    Ric0=ricci_from_derivative(Gs,0)
    dRic10=ricci_from_derivative(Gh11,10)
    dRic12=ricci_from_derivative(Gh13,12)
    # degree-12 Gamma*Gamma cross terms
    for b,d in product(range(4),repeat=2):
        q=dict(dRic12[b][d])
        for a,e in product(range(4),repeat=2):
            q=z.add(q,z.mul(Gh11[a][a][e],Gs[e][d][b],12))
            q=z.add(q,z.mul(Gs[a][a][e],Gh11[e][d][b],12))
            q=z.sub(q,z.mul(Gh11[a][d][e],Gs[e][a][b],12))
            q=z.sub(q,z.mul(Gs[a][d][e],Gh11[e][a][b],12))
        dRic12[b][d]=z.homog(q,12)
    sr=raised(s);hr=raised(h)
    dR10={}
    for a in range(4):dR10=z.add(dR10,z.scale(dRic10[a][a],z.ETA[a]))
    dR10=z.homog(dR10,10)
    dR12={}
    for a in range(4):dR12=z.add(dR12,z.scale(dRic12[a][a],z.ETA[a]))
    for a,b in product(range(4),repeat=2):
        dR12=z.add(dR12,z.mul(z.scale(sr[a][b],-1),dRic10[a][b],12))
        dR12=z.add(dR12,z.mul(z.scale(hr[a][b],-1),Ric0[a][b],12))
    dR12=z.homog(dR12,12)
    R0={}
    for a in range(4):R0=z.add(R0,z.scale(Ric0[a][a],z.ETA[a]))
    R0=z.homog(R0,0)
    dEin=z.pmat()
    for b,d in product(range(4),repeat=2):
        q=dict(dRic12[b][d])
        if b==d:q=z.add(q,z.scale(dR12,-F(z.ETA[b],2)))
        q=z.add(q,z.scale(z.mul(s[b][d],dR10,12),-F(1,2)))
        q=z.add(q,z.scale(z.mul(h[b][d],R0,12),-F(1,2)))
        dEin[b][d]=z.homog(q,12)
    controls={
      'background_linear_Ricci0_zero':all(not Ric0[a][b] for a,b in z.PAIRS),
      'principal_directional_Einstein10_zero':all(not dRic10[a][b] for a,b in z.PAIRS) and not dR10,
    }
    return dEin,controls

def compatibility_column(dEin):
    a11=z.alphas(11);out=[]
    for b in range(4):
        for beta in a11:
            val=F(0)
            for a in range(4):
                al=list(beta);al[a]+=1;al=tuple(al);pair=(a,b) if a<=b else (b,a)
                val += -F(z.ETA[a])*dEin[pair[0]][pair[1]].get(al,F(0))
            out.append(sp.Rational(val.numerator,val.denominator))
    return sp.Matrix(out)

def direct_column(authority,index):
    d,sha=w.load_authority(authority);a12,basis,M14,rows14,meta14,L,rank12,kok=w.structural()
    if not(0<=index<len(basis)):raise ValueError(index)
    g2=w.seed2(d);h=direction_metric(basis[index],a12);dEin,controls=directional_einstein12(g2,h);col=compatibility_column(dEin)
    return d,sha,basis,a12,col,controls

def full_column(d,basis,a12,index):
    gf,_=w.full_seed12(d);_,_,meta14,_,_,_,_=__import__('qgr_iter057ac_tetradecic_einstein_seed_completion').system()
    r0,inv0=w.rhs_vector(gf,meta14);ad.add_direction(gf,basis[index],a12);ri,invi=w.rhs_vector(gf,meta14)
    # reconstruct L from frozen system
    import qgr_iter057ac_tetradecic_einstein_seed_completion as ac
    M14,rows14,meta14,a11,a12x,a13,a14=ac.system();L=ad.left_controls(rows14,meta14,a11)
    return L*(ri-r0),bool(inv0 and invi)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--authority',required=True);ap.add_argument('--indices',default='0,557,1113');ap.add_argument('--output',required=True);a=ap.parse_args();inds=[int(x) for x in a.indices.split(',') if x]
    rows=[];allok=True
    for i in inds:
        d,sha,basis,a12,col,ctrl=direct_column(a.authority,i);fc,inv=full_column(d,basis,a12,i);eq=(col==fc);allok=allok and all(ctrl.values()) and inv and eq
        rows.append({'index':i,'direct_nonzero_count':sum(x!=0 for x in col),'full_nonzero_count':sum(x!=0 for x in fc),'coefficient_exact_match':eq,'direct_controls':ctrl,'full_inverse_ok':inv})
    payload={'gate':'ITER057AM-DIRECT-DIRECTIONAL-FIXED-CONTROL-VALIDATION','preregistration':PREREG,'heldout_candidate':w.HELDOUT,'indices':inds,'controls':rows,'all_fixed_controls_exact':allok,'classification':'CONFIRM_ITER057AM_DIRECT_G2_X_R12_OPERATOR' if allok else 'CONTRADICTION_ITER057AM_DIRECT_G2_X_R12_OPERATOR'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps(payload,indent=2,sort_keys=True));return 0 if allok else 2
if __name__=='__main__':raise SystemExit(main())
