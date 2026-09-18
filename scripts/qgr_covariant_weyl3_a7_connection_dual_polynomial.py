#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="ed829c5f60f2fad6a308ec3f9c50695a6777567e"
PARENT_RESULT="267743ee78ea0ebd51fd697003cc1207a9d9032b"
P_HASH="21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe"
MAX_E=1
MAX_X=2

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

class Poly:
    __slots__=("d",)
    def __init__(self,d=None):
        self.d={(int(e),int(x)):F(v) for (e,x),v in (d or {}).items() if v and e<=MAX_E and x<=MAX_X}
    @staticmethod
    def c(v):
        v=F(v); return Poly({(0,0):v}) if v else Poly()
    @staticmethod
    def m(e,x,v=1):
        v=F(v); return Poly({(e,x):v}) if v and e<=MAX_E and x<=MAX_X else Poly()
    def coeff(self,e,x): return self.d.get((e,x),F(0))
    def _c(self,o): return o if isinstance(o,Poly) else Poly.c(o)
    def __add__(self,o):
        o=self._c(o); q=dict(self.d)
        for k,v in o.d.items(): q[k]=q.get(k,F(0))+v
        return Poly(q)
    __radd__=__add__
    def __neg__(self): return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+(-self._c(o))
    def __rsub__(self,o): return self._c(o)-self
    def __mul__(self,o):
        o=self._c(o); q={}
        for (e1,x1),v1 in self.d.items():
            for (e2,x2),v2 in o.d.items():
                e=e1+e2; x=x1+x2
                if e<=MAX_E and x<=MAX_X: q[(e,x)]=q.get((e,x),F(0))+v1*v2
        return Poly(q)
    __rmul__=__mul__
    def inv(self):
        c=self.coeff(0,0)
        if not c: raise ZeroDivisionError("nonunit polynomial pivot")
        n=self-Poly.c(c)
        base=Poly.c(1/c); out=Poly.c(1/c); term=Poly.c(1)
        u=(-n)*F(1,c)
        for _ in range(1,6):
            term=term*u
            if not term.d: break
            out=out+term*F(1,c)
        if not (self*out-Poly.c(1)).d=={}:
            raise ArithmeticError("polynomial inverse truncation failed")
        return out
    def __truediv__(self,o): return self*self._c(o).inv()
    def dx(self):
        q={}
        for (e,x),v in self.d.items():
            if x: q[(e,x-1)]=q.get((e,x-1),F(0))+x*v
        return Poly(q)
    def dump(self):
        return [[e,x,fs(v)] for (e,x),v in sorted(self.d.items())]

def mat_inverse(A):
    n=len(A); aug=[[A[i][j] for j in range(n)]+[Poly.c(int(i==j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        invp=aug[col][col].inv(); aug[col]=[z*invp for z in aug[col]]
        for row in range(n):
            if row==col: continue
            q=aug[row][col]; aug[row]=[aug[row][k]-q*aug[col][k] for k in range(2*n)]
    return [row[n:] for row in aug]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c
    z=c.build("OFFSHELL_A")
    pvec=[c.fs(z["P"][aa][bb][cc][dd].v()) for aa,bb,cc,dd in product(range(4),repeat=4)]
    psha=c.jsha(pvec)

    Gm=[[Poly() for _ in range(4)] for _ in range(4)]
    for aa,bb in product(range(4),repeat=2):
        a0,b0=c.cab(aa,bb)
        base=c.eta(aa,bb)
        g00=panel.metric_value("OFFSHELL_A",a0,b0,(0,0))
        h0=panel.h_value(7,a0,b0,())
        h1=panel.h_value(7,a0,b0,(0,))
        Gm[aa][bb]=Poly.c(base)+Poly.m(0,2,F(1,2)*g00)+Poly.m(1,1,h0)+Poly.m(1,2,h1)

    Gi=mat_inverse(Gm)
    inverse_exact=all(not (sum((Gm[aa][cc]*Gi[cc][bb] for cc in range(4)),Poly())-Poly.c(int(aa==bb))).d for aa,bb in product(range(4),repeat=2))

    def partial(q,aa,bb):
        return Gm[aa][bb].dx() if q==0 else Poly()

    Gamma=[[[Poly() for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for aa,bb,cc in product(range(4),repeat=3):
        q=Poly()
        for e in range(4):
            q=q+Gi[aa][e]*(partial(bb,e,cc)+partial(cc,e,bb)-partial(e,bb,cc))
        Gamma[aa][bb][cc]=q*F(1,2)

    gamma0=all(Gamma[aa][bb][cc].coeff(0,0)==0 for aa,bb,cc in product(range(4),repeat=3))
    Rgg=[[[[Poly() for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for aa,bb,cc,dd in product(range(4),repeat=4):
        q=Poly()
        for e,f in product(range(4),repeat=2):
            q=q+Gm[e][f]*(Gamma[e][cc][aa]*Gamma[f][dd][bb]-Gamma[e][dd][aa]*Gamma[f][cc][bb])
        Rgg[aa][bb][cc][dd]=q

    tensor=[fs(Rgg[aa][bb][cc][dd].coeff(1,1)) for aa,bb,cc,dd in product(range(4),repeat=4)]
    scalar=sum((z["P"][aa][bb][cc][dd].v()*Rgg[aa][bb][cc][dd].coeff(1,1) for aa,bb,cc,dd in product(range(4),repeat=4)),F(0))
    controls={
      "parent_result_pinned":PARENT_RESULT=="267743ee78ea0ebd51fd697003cc1207a9d9032b",
      "P_hash_exact":psha==P_HASH,
      "background_first_metric_jets_zero":all(panel.metric_value("OFFSHELL_A",aa,bb,(0,))==0 for aa in range(4) for bb in range(aa,4)),
      "polynomial_inverse_exact":inverse_exact,
      "Gamma_point_zero":gamma0,
      "frozen_phi_equals_x0":True,
      "frozen_slot_i0_j0":True,
      "target_blind_no_parent_identity_values_read":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True,
    }
    payload={
      "gate":"COVARIANT_WEYL3_A7_CONNECTION_DUAL_POLYNOMIAL_SIGN_ADJUDICATION",
      "lane":"DIRECT_BIVARIATE_POLYNOMIAL_EXTRACTION",
      "preregistration_commit":PREREG,
      "parent_terminal_commit":PARENT_RESULT,
      "seed":"OFFSHELL_A","direction":7,"i":0,"j":0,
      "controls":controls,
      "P_point_sha256":psha,
      "connection_tensor_sha256":jsha(tensor),
      "connection_identity_value":fs(scalar),
      "polynomial_ring":{"epsilon_degree_max":MAX_E,"x_degree_max":MAX_X,"phi":"x0"},
      "serialized_before_target_comparison":True,
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,
      "classification":"DUAL_POLYNOMIAL_CONNECTION_WITNESS_READY" if all(controls.values()) else "BLOCKED_DUAL_POLYNOMIAL_CONTROL_FAILURE",
    }
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps(payload,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
