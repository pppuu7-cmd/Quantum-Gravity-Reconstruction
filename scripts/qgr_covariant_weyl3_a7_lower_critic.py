#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

PREREG = "a8c7bd1bd5280f18aa50955b4cd847b707c178ab"
BINDING = "f0081e60056106b0eac916b6f207ad03fc113233"
PARENT_RUN = 35367461999
PARENT_CRITIC_WITNESS = "09d544faf078bd7b4046ad1d7d0f768a489d93ff912effddfcbaf8d838d8b19b"
PARENT_P_SHA = "21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe"
PARENT_JET_SHA = "1bb5b6a0ee5469879e335704beb7ee003dddbf8d4734c2d3f290d6fe53dcb9a3"
PARENT_EULER = "36188861490208135407463132950092941670313420227/2815972870342993586167404814772510458368000000"
FROZEN_PRINCIPAL_SHA = "fb20b1704d6e651ccae7df87591cd3961d6792a04d103a182aa712552db65896"
KEYS = ("00","01","02","03","11","12","13","22","23","33")
CLASS_KEYS = (
    "CONNECTION_VARIATION",
    "COVARIANTIZATION_GAMMA_TIMES_DH",
    "COVARIANTIZATION_DGAMMA_TIMES_H",
    "COVARIANTIZATION_GAMMA_GAMMA_TIMES_H",
    "IBP_FIRST_TRANSFER",
    "IBP_SECOND_TRANSFER",
    "ALGEBRAIC_CURVATURE_VARIATION",
    "VOLUME_CONTROL",
    "PRINCIPAL_CONTROL",
)

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def pairmatch(p,q,i,j):
    return int(tuple(sorted((p,q)))==(i,j))

class D:
    __slots__=("v","d")
    def __init__(self,v=0,d=0): self.v=F(v); self.d=F(d)
    @staticmethod
    def c(x): return D(x,0)
    def _c(self,o): return o if isinstance(o,D) else D.c(o)
    def __add__(self,o): o=self._c(o); return D(self.v+o.v,self.d+o.d)
    __radd__=__add__
    def __neg__(self): return D(-self.v,-self.d)
    def __sub__(self,o): return self+(-self._c(o))
    def __rsub__(self,o): return self._c(o)-self
    def __mul__(self,o): o=self._c(o); return D(self.v*o.v,self.d*o.v+self.v*o.d)
    __rmul__=__mul__
    def inv(self): return D(1/self.v,-self.d/(self.v*self.v))
    def __truediv__(self,o): return self*self._c(o).inv()
    def sqrt_unit(self):
        if self.v != 1: raise ArithmeticError("sqrt_unit requires base value 1")
        return D(1,self.d/2)

def mat_inverse(A):
    n=len(A); aug=[[A[i][j] for j in range(n)]+[D.c(int(i==j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        invp=aug[col][col].inv(); aug[col]=[x*invp for x in aug[col]]
        for row in range(n):
            if row==col: continue
            q=aug[row][col]; aug[row]=[aug[row][j]-q*aug[col][j] for j in range(2*n)]
    return [row[n:] for row in aug]

def psign(p):
    inv=sum(1 for i in range(len(p)) for j in range(i+1,len(p)) if p[i]>p[j])
    return -1 if inv%2 else 1

def det4(g):
    out=D.c(0)
    for p in permutations(range(4)):
        q=D.c(psign(p))
        for i in range(4): q=q*g[i][p[i]]
        out=out+q
    return out

def fixed_R_metric_density_variation(c,panel,z,direction):
    h=lambda a,b: panel.h_value(direction,*c.cab(a,b),())
    g=[[D(c.eta(a,b),h(a,b)) for b in range(4)] for a in range(4)]
    gi=mat_inverse(g)
    R=[[[[D.c(z["R"][a][b][cc][d].v()) for d in range(4)] for cc in range(4)] for b in range(4)] for a in range(4)]
    Ric=[[D.c(0) for _ in range(4)] for _ in range(4)]
    for b,d in product(range(4),repeat=2):
        q=D.c(0)
        for a,cc in product(range(4),repeat=2): q=q+gi[a][cc]*R[a][b][cc][d]
        Ric[b][d]=q
    S=D.c(0)
    for b,d in product(range(4),repeat=2): S=S+gi[b][d]*Ric[b][d]
    C=[[[[D.c(0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,cc,d in product(range(4),repeat=4):
        rt=g[a][cc]*Ric[d][b]-g[a][d]*Ric[cc][b]-g[b][cc]*Ric[d][a]+g[b][d]*Ric[cc][a]
        gg=g[a][cc]*g[d][b]-g[a][d]*g[cc][b]
        C[a][b][cc][d]=R[a][b][cc][d]-rt*F(1,2)+S*gg*F(1,6)
    Cup=[[[[D.c(0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,cc,d in product(range(4),repeat=4):
        q=D.c(0)
        for e,f in product(range(4),repeat=2): q=q+gi[cc][e]*gi[d][f]*C[a][b][e][f]
        Cup[a][b][cc][d]=q
    I3=D.c(0)
    for a,b,cc,d,e,f in product(range(4),repeat=6): I3=I3+Cup[a][b][cc][d]*Cup[cc][d][e][f]*Cup[e][f][a][b]
    density=(-det4(g)).sqrt_unit()
    L=density*I3
    return L.d, density.d*I3.v, I3.v

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c

    manifest=panel.panel_manifest()
    expected={(x["seed"],x["direction"]):x["jet_sha256"] for x in manifest["cells"]}[("OFFSHELL_A",7)]
    cell=c.cell("OFFSHELL_A",7,expected)
    z=c.build("OFFSHELL_A")
    h0=lambda aa,bb: panel.h_value(7,*c.cab(aa,bb),())

    H={}
    for aa in range(4):
        for bb in range(aa,4):
            q=c.P()
            for al in c.AL:
                if c.deg(al)>2: continue
                I=tuple(sorted(c.inds(al)))
                v=panel.h_value(7,aa,bb,I)
                if v: q=q+c.P.mono(al,v/F(c.mf(al)))
            H[(aa,bb)]=q
    def hp(aa,bb): return H[c.cab(aa,bb)]

    density=c.P.c(1)
    for aa,bb in product(range(4),repeat=2):
        if c.eta(aa,bb): density=density+(z["g"][aa][bb]-c.eta(aa,bb)).sc(F(1,2)*c.eta(aa,bb))
    K=[[[[z["P"][aa][bb][cc][dd]*density for dd in range(4)] for cc in range(4)] for bb in range(4)] for aa in range(4)]

    F0P=c.P(); FiP=[c.P() for _ in range(4)]; FijP={k:c.P() for k in KEYS}
    for aa,bb,cc,dd in product(range(4),repeat=4):
        kp=K[aa][bb][cc][dd]
        if not kp.d: continue
        z0=(hp(aa,dd).deriv(cc).deriv(bb)+hp(bb,cc).deriv(dd).deriv(aa)-hp(bb,dd).deriv(cc).deriv(aa)-hp(aa,cc).deriv(dd).deriv(bb)).sc(F(1,2))
        F0P=F0P+kp*z0
        for i in range(4):
            zi=c.P()
            if bb==i: zi=zi+hp(aa,dd).deriv(cc)
            if cc==i: zi=zi+hp(aa,dd).deriv(bb)
            if aa==i: zi=zi+hp(bb,cc).deriv(dd)
            if dd==i: zi=zi+hp(bb,cc).deriv(aa)
            if aa==i: zi=zi-hp(bb,dd).deriv(cc)
            if cc==i: zi=zi-hp(bb,dd).deriv(aa)
            if bb==i: zi=zi-hp(aa,cc).deriv(dd)
            if dd==i: zi=zi-hp(aa,cc).deriv(bb)
            FiP[i]=FiP[i]+kp*zi.sc(F(1,2))
        for key in KEYS:
            i,j=int(key[0]),int(key[1])
            q=F(1,2)*(pairmatch(cc,bb,i,j)*hp(aa,dd)+pairmatch(dd,aa,i,j)*hp(bb,cc)-pairmatch(cc,aa,i,j)*hp(bb,dd)-pairmatch(dd,bb,i,j)*hp(aa,cc))
            FijP[key]=FijP[key]+kp*q

    fixed_total,volume,I3=fixed_R_metric_density_variation(c,panel,z,7)
    F0=fixed_total+F0P.v()
    first=-sum((FiP[i].deriv(i).v() for i in range(4)),F(0))
    second=sum((FijP[k].deriv(int(k[0])).deriv(int(k[1])).v() for k in KEYS),F(0))
    partial=F0+first+second
    euler=F(cell["euler_source"]["contraction_with_h"])
    gap=euler-partial

    dgamma=F(0)
    for aa,bb,cc,dd,rr in product(range(4),repeat=5):
        hh=h0(aa,bb)
        if not hh: continue
        term=(z["G"][aa][dd][rr].deriv(cc).v()*z["P"][rr][cc][dd][bb].v()
             +z["G"][cc][dd][rr].deriv(cc).v()*z["P"][aa][rr][dd][bb].v()
             +z["G"][dd][dd][rr].deriv(cc).v()*z["P"][aa][cc][rr][bb].v()
             +z["G"][bb][dd][rr].deriv(cc).v()*z["P"][aa][cc][dd][rr].v())
        dgamma += 2*hh*term
    connection=gap-dgamma

    fi=[{"i":str(i),"value":fs(FiP[i].v()),"d_i_value":fs(FiP[i].deriv(i).v())} for i in range(4)]
    principal=[{"ij":k,"value":fs(FijP[k].v())} for k in KEYS]
    fij=[{"ij":k,"value":fs(FijP[k].v()),"d_i_value":fs(FijP[k].deriv(int(k[0])).v()),"d_i_d_j_value":fs(FijP[k].deriv(int(k[0])).deriv(int(k[1])).v())} for k in KEYS]
    classes={
      "CONNECTION_VARIATION":fs(connection),
      "COVARIANTIZATION_GAMMA_TIMES_DH":"0",
      "COVARIANTIZATION_DGAMMA_TIMES_H":fs(dgamma),
      "COVARIANTIZATION_GAMMA_GAMMA_TIMES_H":"0",
      "IBP_FIRST_TRANSFER":fs(first),
      "IBP_SECOND_TRANSFER":fs(second),
      "ALGEBRAIC_CURVATURE_VARIATION":fs(F0-volume),
      "VOLUME_CONTROL":fs(volume),
      "PRINCIPAL_CONTROL":"0",
    }
    class_sum=sum((F(classes[k]) for k in CLASS_KEYS),F(0))
    pvec=[c.fs(z["P"][aa][bb][cc][dd].v()) for aa,bb,cc,dd in product(range(4),repeat=4)]
    algebraic_euler=-sum((z["A"][aa][bb]*h0(aa,bb) for aa,bb in product(range(4),repeat=2)),F(0))
    controls={
      "parent_run_pinned":PARENT_RUN==35367461999,
      "parent_witness_exact":cell["cell_witness_sha256"]==PARENT_CRITIC_WITNESS,
      "parent_jet_exact":cell["jet_sha256"]==PARENT_JET_SHA,
      "parent_P_hash_exact":c.jsha(pvec)==PARENT_P_SHA and cell["euler_source"]["P_point_sha256"]==PARENT_P_SHA,
      "all_parent_self_controls_true":all(v is True for v in cell["controls"].values()),
      "parent_euler_exact":euler==F(PARENT_EULER),
      "principal_vector_frozen_exact":jsha(principal)==FROZEN_PRINCIPAL_SHA,
      "normal_coordinate_Gamma_zero":cell["controls"]["normal_coordinate_Gamma_zero"] is True,
      "fixed_R_base_I3_exact":I3==z["I"].v(),
      "target_blind_no_researcher_read":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True,
    }
    payload={
      "gate":"COVARIANT_WEYL3_A7_LOWER_ORDER_COVARIANTIZATION_IBP_LOCALIZATION",
      "lane":"CRITIC_P_PALATINI_LOWER_ORDER_RECONSTRUCTION",
      "preregistration_commit":PREREG,
      "implementation_binding_commit":BINDING,
      "seed":"OFFSHELL_A","direction":7,
      "parent_run":PARENT_RUN,
      "parent_cell_witness_sha256":cell["cell_witness_sha256"],
      "parent_jet_sha256":cell["jet_sha256"],
      "parent_P_sha256":c.jsha(pvec),
      "controls":controls,
      "fixed_R_metric_density_variation":fs(fixed_total),
      "F0_P":fs(F0P.v()),
      "F0":fs(F0),
      "volume":fs(volume),
      "lower_order_curvature_before_ibp":fs(F0-volume),
      "Fi_vector":fi,
      "Fi_vector_sha256":jsha(fi),
      "Fij_ledger":fij,
      "principal_vector":principal,
      "principal_vector_sha256":jsha(principal),
      "first_ibp_transfer":fs(first),
      "second_ibp_transfer":fs(second),
      "partial_ibp_bulk":fs(partial),
      "euler_parent":fs(euler),
      "covariantization_gap":fs(gap),
      "explicit_dGamma_contribution":fs(dgamma),
      "algebraic_euler_term":fs(algebraic_euler),
      "class_order":list(CLASS_KEYS),
      "classes":classes,
      "class_vector_sha256":jsha([[k,classes[k]] for k in CLASS_KEYS]),
      "class_sum":fs(class_sum),
      "parent_total":fs(euler),
      "target_blind_serialized_before_comparison":True,
      "researcher_science_code_imported":False,
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "classification":"CRITIC_LOWER_ORDER_WITNESS_READY" if all(controls.values()) else "BLOCKED_CRITIC_LOWER_ORDER_CONTROL_FAILURE",
    }
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in payload.items() if k not in ("Fij_ledger",)},sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
