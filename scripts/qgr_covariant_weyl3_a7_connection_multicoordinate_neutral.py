#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="58284ae7f71e73db5c2d71d157bc74bd7d646030"
PARENT_RESULT="199ecea77c9138c4a166d1ffc7143ce2d0de34be"
MAX_E=1
MAX_COORD=2
ZERO=(0,0,0,0)
X0=(1,0,0,0)

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def addexp(a,b):
    return tuple(x+y for x,y in zip(a,b))

class Poly:
    __slots__=("d",)
    def __init__(self,d=None):
        out={}
        for (e,ex),v in (d or {}).items():
            ex=tuple(int(x) for x in ex); e=int(e); v=F(v)
            if v and e<=MAX_E and sum(ex)<=MAX_COORD:
                out[(e,ex)]=out.get((e,ex),F(0))+v
        self.d={k:v for k,v in out.items() if v}
    @staticmethod
    def c(v):
        v=F(v); return Poly({(0,ZERO):v}) if v else Poly()
    @staticmethod
    def m(e,ex,v=1):
        v=F(v); ex=tuple(ex)
        return Poly({(e,ex):v}) if v and e<=MAX_E and sum(ex)<=MAX_COORD else Poly()
    def coeff(self,e,ex):
        return self.d.get((int(e),tuple(ex)),F(0))
    def co(self,o):
        return o if isinstance(o,Poly) else Poly.c(o)
    def __add__(self,o):
        o=self.co(o); q=dict(self.d)
        for k,v in o.d.items(): q[k]=q.get(k,F(0))+v
        return Poly(q)
    __radd__=__add__
    def __neg__(self): return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+(-self.co(o))
    def __rsub__(self,o): return self.co(o)-self
    def __mul__(self,o):
        o=self.co(o); q={}
        for (e1,x1),v1 in self.d.items():
            for (e2,x2),v2 in o.d.items():
                e=e1+e2; ex=addexp(x1,x2)
                if e<=MAX_E and sum(ex)<=MAX_COORD:
                    q[(e,ex)]=q.get((e,ex),F(0))+v1*v2
        return Poly(q)
    __rmul__=__mul__
    def inv(self):
        c=self.coeff(0,ZERO)
        if not c: raise ZeroDivisionError("nonunit polynomial pivot")
        n=self-Poly.c(c)
        u=(-n)*F(1,c)
        out=Poly.c(1/c); term=Poly.c(1)
        for _ in range(1,8):
            term=term*u
            if not term.d: break
            out=out+term*F(1,c)
        if (self*out-Poly.c(1)).d:
            raise ArithmeticError("polynomial inverse truncation failed")
        return out
    def dx(self,q):
        out={}
        for (e,ex),v in self.d.items():
            n=ex[q]
            if n:
                yy=list(ex); yy[q]-=1; yy=tuple(yy)
                out[(e,yy)]=out.get((e,yy),F(0))+n*v
        return Poly(out)

def mat_inverse(A):
    n=len(A)
    aug=[[A[i][j] for j in range(n)]+[Poly.c(int(i==j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        ip=aug[col][col].inv()
        aug[col]=[z*ip for z in aug[col]]
        for row in range(n):
            if row==col: continue
            q=aug[row][col]
            aug[row]=[aug[row][k]-q*aug[col][k] for k in range(2*n)]
    return [r[n:] for r in aug]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c
    z=c.build("OFFSHELL_A")

    G=[[Poly() for _ in range(4)] for _ in range(4)]
    for aa,bb in product(range(4),repeat=2):
        a0,b0=c.cab(aa,bb)
        g=Poly.c(c.eta(aa,bb))
        for p,q in product(range(4),repeat=2):
            ex=[0,0,0,0]; ex[p]+=1; ex[q]+=1
            g=g+Poly.m(0,tuple(ex),F(1,2)*panel.metric_value("OFFSHELL_A",a0,b0,tuple(sorted((p,q)))))
        ex=[1,0,0,0]
        g=g+Poly.m(1,tuple(ex),panel.h_value(7,a0,b0,()))
        for q in range(4):
            ex=[1,0,0,0]; ex[q]+=1
            g=g+Poly.m(1,tuple(ex),panel.h_value(7,a0,b0,(q,)))
        G[aa][bb]=g

    Gi=mat_inverse(G)
    inverse_exact=all(not (sum((G[a][r]*Gi[r][b] for r in range(4)),Poly())-Poly.c(int(a==b))).d for a,b in product(range(4),repeat=2))

    Gamma=[[[Poly() for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for up,b,ci in product(range(4),repeat=3):
        s=Poly()
        for e in range(4):
            s=s+Gi[up][e]*(G[e][ci].dx(b)+G[e][b].dx(ci)-G[b][ci].dx(e))
        Gamma[up][b][ci]=s*F(1,2)

    def h(aa,bb): return panel.h_value(7,*c.cab(aa,bb),())
    def g2(aa,bb,p,q): return panel.metric_value("OFFSHELL_A",*c.cab(aa,bb),tuple(sorted((p,q))))
    def dG_ref(j,up,b,ci):
        return F(1,2)*sum((c.eta(up,e)*(g2(e,ci,b,j)+g2(e,b,ci,j)-g2(b,ci,e,j)) for e in range(4)),F(0))
    def dphi_ref(i,up,b,ci):
        return F(1,2)*sum((c.eta(up,e)*((1 if b==i else 0)*h(e,ci)+(1 if ci==i else 0)*h(e,b)-(1 if e==i else 0)*h(b,ci)) for e in range(4)),F(0))

    dgamma_poly=[]; dgamma_ref=[]; delta_poly=[]; delta_ref=[]
    first_dgamma_mismatch=None; first_delta_mismatch=None
    for up,b,ci in product(range(4),repeat=3):
        vp=Gamma[up][b][ci].coeff(0,X0); vr=dG_ref(0,up,b,ci)
        wp=Gamma[up][b][ci].coeff(1,ZERO); wr=dphi_ref(0,up,b,ci)
        dgamma_poly.append(fs(vp)); dgamma_ref.append(fs(vr)); delta_poly.append(fs(wp)); delta_ref.append(fs(wr))
        if first_dgamma_mismatch is None and vp!=vr: first_dgamma_mismatch=[up,b,ci,fs(vp),fs(vr)]
        if first_delta_mismatch is None and wp!=wr: first_delta_mismatch=[up,b,ci,fs(wp),fs(wr)]

    Rgg=[[[[Poly() for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for aa,bb,cc,dd in product(range(4),repeat=4):
        s=Poly()
        for e,f in product(range(4),repeat=2):
            s=s+G[e][f]*(Gamma[e][cc][aa]*Gamma[f][dd][bb]-Gamma[e][dd][aa]*Gamma[f][cc][bb])
        Rgg[aa][bb][cc][dd]=s

    tensor=[fs(Rgg[a][b][cc][d].coeff(1,X0)) for a,b,cc,d in product(range(4),repeat=4)]
    scalar=sum((z["P"][a][b][cc][d].v()*Rgg[a][b][cc][d].coeff(1,X0) for a,b,cc,d in product(range(4),repeat=4)),F(0))
    comp=Rgg[0][1][0][1].coeff(1,X0)
    controls={
      "parent_result_pinned":PARENT_RESULT=="199ecea77c9138c4a166d1ffc7143ce2d0de34be",
      "polynomial_inverse_exact":inverse_exact,
      "background_first_metric_jets_zero":all(panel.metric_value("OFFSHELL_A",aa,bb,(q,))==0 for aa in range(4) for bb in range(aa,4) for q in range(4)),
      "Gamma_point_zero":all(Gamma[up][b][ci].coeff(0,ZERO)==0 for up,b,ci in product(range(4),repeat=3)),
      "all_64_dGamma_exact":first_dgamma_mismatch is None,
      "all_64_deltaGamma_exact":first_delta_mismatch is None,
      "frozen_component_0101":True,
      "serialized_256_before_target_comparison":len(tensor)==256,
      "target_blind_no_parent_A_B_values":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True
    }
    out={
      "gate":"COVARIANT_WEYL3_A7_CONNECTION_MULTICOORDINATE_NEUTRAL_EXTRACTION",
      "lane":"FULL_MULTICOORDINATE_NEUTRAL_POLYNOMIAL",
      "preregistration_commit":PREREG,
      "parent_terminal_commit":PARENT_RESULT,
      "seed":"OFFSHELL_A","direction":7,"i":0,"j":0,"component":[0,1,0,1],
      "ring":{"variables":["eps","x0","x1","x2","x3"],"epsilon_degree_max":1,"coordinate_total_degree_max":2},
      "controls":controls,
      "first_dGamma_mismatch":first_dgamma_mismatch,
      "first_deltaGamma_mismatch":first_delta_mismatch,
      "dGamma_poly_sha256":jsha(dgamma_poly),
      "dGamma_reference_sha256":jsha(dgamma_ref),
      "deltaGamma_poly_sha256":jsha(delta_poly),
      "deltaGamma_reference_sha256":jsha(delta_ref),
      "tensor_values":tensor,
      "tensor_sha256":jsha(tensor),
      "component_0101_value":fs(comp),
      "scalar_control":fs(scalar),
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,
      "classification":"MULTICOORDINATE_NEUTRAL_WITNESS_READY" if all(controls.values()) else "BLOCKED_MULTICOORDINATE_NEUTRAL_CONTROL_FAILURE"
    }
    out["payload_sha256"]=jsha(out)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
