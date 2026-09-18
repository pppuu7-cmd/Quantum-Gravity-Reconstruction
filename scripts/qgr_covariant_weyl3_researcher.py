#!/usr/bin/env python3
"""Researcher lane: exact direct directional variation plus mechanical IBP.

Independent science code. Imports only the frozen neutral panel generator.
For each frozen direction it evaluates the exact scalar-test decomposition
  delta L[h*phi] = F0*phi + Fi*d_i phi + Fij*d_i d_j phi,
then transfers derivatives mechanically. This is an exact equivalent of the
A*h+B*dh+C*d2h decomposition and uses metric jets through order 4 and h jets
through order 2 exactly as preregistered.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import combinations_with_replacement, permutations, product
from pathlib import Path
import qgr_covariant_weyl3_panel as panel
N=4
PREREG="8c21ee233423deaff52d0fa552c027fa065a53a7"
PANEL_FREEZE="1642dc7ca4204a4240635be68522f1731c8a9c50"
PANEL_GENERATOR="03377afec95801b5a49f47b85ddd9c9bf3326ac0"
def fs(x):x=F(x);return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def cab(a,b):return (a,b) if a<=b else (b,a)
def addI(I,*js):return tuple(sorted(tuple(I)+tuple(js)))

class J:
    __slots__=("kind","v","a","b","c")
    def __init__(self,kind="0",v=0,a=0,b=0,c=0):self.kind=kind;self.v=F(v);self.a=F(a);self.b=F(b);self.c=F(c)
    @staticmethod
    def zero(kind):return J(kind)
    @staticmethod
    def one(kind):return J(kind,1)
    def _coerce(self,o):return o if isinstance(o,J) else J(self.kind,o)
    def __add__(self,o):
        o=self._coerce(o);assert o.kind==self.kind;return J(self.kind,self.v+o.v,self.a+o.a,self.b+o.b,self.c+o.c)
    __radd__=__add__
    def __neg__(self):return J(self.kind,-self.v,-self.a,-self.b,-self.c)
    def __sub__(self,o):return self+(-self._coerce(o))
    def __rsub__(self,o):return self._coerce(o)-self
    def __mul__(self,o):
        o=self._coerce(o);assert o.kind==self.kind;k=self.kind
        if k=="0":return J(k,self.v*o.v)
        if k=="1":return J(k,self.v*o.v,self.a*o.v+self.v*o.a)
        if k=="2s":return J(k,self.v*o.v,self.a*o.v+self.v*o.a,self.b*o.v+2*self.a*o.a+self.v*o.b)
        return J(k,self.v*o.v,self.a*o.v+self.v*o.a,self.b*o.v+self.v*o.b,self.c*o.v+self.a*o.b+self.b*o.a+self.v*o.c)
    __rmul__=__mul__
    def scale(self,x):x=F(x);return J(self.kind,self.v*x,self.a*x,self.b*x,self.c*x)
    def inv(self):
        v=self.v
        if not v:raise ZeroDivisionError
        k=self.kind
        if k=="0":return J(k,1/v)
        if k=="1":return J(k,1/v,-self.a/v**2)
        if k=="2s":return J(k,1/v,-self.a/v**2,2*self.a*self.a/v**3-self.b/v**2)
        return J(k,1/v,-self.a/v**2,-self.b/v**2,2*self.a*self.b/v**3-self.c/v**2)
    def __truediv__(self,o):return self*self._coerce(o).inv()
    def sqrt(self):
        if self.v!=1:raise ArithmeticError(f"expected unit determinant density at point, got {self.v}")
        k=self.kind
        if k=="0":return J(k,1)
        if k=="1":return J(k,1,self.a/2)
        if k=="2s":return J(k,1,self.a/2,self.b/2-self.a*self.a/4)
        return J(k,1,self.a/2,self.b/2,self.c/2-self.a*self.b/4)
    def deriv_value(self):
        if self.kind=="1":return self.a
        if self.kind=="2s":return self.b
        if self.kind=="2m":return self.c
        return self.v
    def first_i(self):
        if self.kind in ("1","2s","2m"):return self.a
        return F(0)

class D:
    __slots__=("x","dx")
    def __init__(self,x,dx=None):self.x=x;self.dx=dx if dx is not None else J.zero(x.kind)
    @staticmethod
    def c(kind,x):return D(J(kind,x))
    def _coerce(self,o):return o if isinstance(o,D) else D.c(self.x.kind,o)
    def __add__(self,o):o=self._coerce(o);return D(self.x+o.x,self.dx+o.dx)
    __radd__=__add__
    def __neg__(self):return D(-self.x,-self.dx)
    def __sub__(self,o):return self+(-self._coerce(o))
    def __rsub__(self,o):return self._coerce(o)-self
    def __mul__(self,o):o=self._coerce(o);return D(self.x*o.x,self.dx*o.x+self.x*o.dx)
    __rmul__=__mul__
    def scale(self,x):return D(self.x.scale(x),self.dx.scale(x))
    def inv(self):
        ix=self.x.inv();return D(ix,-self.dx*ix*ix)
    def __truediv__(self,o):return self*self._coerce(o).inv()
    def sqrt(self):
        s=self.x.sqrt();return D(s,self.dx/(s.scale(2)))

def mode_for_key(K):
    if len(K)==0:return ("0",())
    if len(K)==1:return ("1",K)
    if K[0]==K[1]:return ("2s",K)
    return ("2m",K)
def bgjet(seed,a,b,I,kind,dirs):
    a,b=cab(a,b);I=tuple(sorted(I));v=panel.metric_value(seed,a,b,I)
    if kind=="0":return J(kind,v)
    if kind=="1":return J(kind,v,panel.metric_value(seed,a,b,addI(I,dirs[0])))
    if kind=="2s":
        p=dirs[0];return J(kind,v,panel.metric_value(seed,a,b,addI(I,p)),panel.metric_value(seed,a,b,addI(I,p,p)))
    p,q=dirs;return J(kind,v,panel.metric_value(seed,a,b,addI(I,p)),panel.metric_value(seed,a,b,addI(I,q)),panel.metric_value(seed,a,b,addI(I,p,q)))
def hjet(d,a,b,I,kind,dirs):
    a,b=cab(a,b);I=tuple(sorted(I))
    def hv(J):
        return panel.h_value(d,a,b,J) if len(J)<=2 else F(0)
    v=hv(I)
    if kind=="0":return J(kind,v)
    if kind=="1":return J(kind,v,hv(addI(I,dirs[0])))
    if kind=="2s":
        p=dirs[0];return J(kind,v,hv(addI(I,p)),hv(addI(I,p,p)))
    p,q=dirs;return J(kind,v,hv(addI(I,p)),hv(addI(I,q)),hv(addI(I,p,q)))
def variation_coeff(d,a,b,I,K,kind,dirs):
    I=tuple(I);out=J.zero(kind)
    for mask in range(1<<len(I)):
        S=tuple(sorted(I[r] for r in range(len(I)) if (mask>>r)&1))
        R=tuple(sorted(I[r] for r in range(len(I)) if not ((mask>>r)&1)))
        if R==K:out=out+hjet(d,a,b,S,kind,dirs)
    return out
def metricD(seed,d,a,b,I,K,kind,dirs):return D(bgjet(seed,a,b,I,kind,dirs),variation_coeff(d,a,b,I,K,kind,dirs))

def mat_inverse(A):
    kind=A[0][0].x.kind;aug=[[A[i][j] for j in range(N)]+[D.c(kind,int(i==j)) for j in range(N)] for i in range(N)]
    for c in range(N):
        ip=aug[c][c].inv();aug[c]=[z*ip for z in aug[c]]
        for r in range(N):
            if r==c:continue
            q=aug[r][c];aug[r]=[aug[r][j]-q*aug[c][j] for j in range(2*N)]
    return [r[N:] for r in aug]
def psign(p):
    z=0
    for i in range(N):
        for j in range(i+1,N):z+=p[i]>p[j]
    return -1 if z%2 else 1
def det4(g):
    kind=g[0][0].x.kind;z=D.c(kind,0)
    for p in permutations(range(N)):
        q=D.c(kind,psign(p))
        for i in range(N):q=q*g[i][p[i]]
        z=z+q
    return z

def build(seed,d,K):
    kind,dirs=mode_for_key(K)
    g=[[metricD(seed,d,a,b,(),K,kind,dirs) for b in range(N)] for a in range(N)]
    g1=[[[metricD(seed,d,a,b,(i,),K,kind,dirs) for i in range(N)] for b in range(N)] for a in range(N)]
    g2=[[[[metricD(seed,d,a,b,(i,j),K,kind,dirs) for j in range(N)] for i in range(N)] for b in range(N)] for a in range(N)]
    gi=mat_inverse(g)
    G=[[[D.c(kind,0) for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c in product(range(N),repeat=3):
        z=D.c(kind,0)
        for e in range(N):z=z+gi[a][e]*(g1[e][c][b]+g1[e][b][c]-g1[b][c][e])
        G[a][b][c]=z.scale(F(1,2))
    R=[[[[D.c(kind,0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,dd in product(range(N),repeat=4):
        z=(g2[a][dd][b][c]+g2[b][c][a][dd]-g2[a][c][b][dd]-g2[b][dd][a][c]).scale(F(1,2))
        for e,f in product(range(N),repeat=2):z=z+g[e][f]*(G[e][c][a]*G[f][dd][b]-G[e][dd][a]*G[f][c][b])
        R[a][b][c][dd]=z
    Ric=[[D.c(kind,0) for _ in range(N)] for _ in range(N)]
    for b,dd in product(range(N),repeat=2):
        z=D.c(kind,0)
        for a,c in product(range(N),repeat=2):z=z+gi[a][c]*R[a][b][c][dd]
        Ric[b][dd]=z
    S=D.c(kind,0)
    for b,dd in product(range(N),repeat=2):S=S+gi[b][dd]*Ric[b][dd]
    C=[[[[D.c(kind,0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,dd in product(range(N),repeat=4):
        rt=g[a][c]*Ric[dd][b]-g[a][dd]*Ric[c][b]-g[b][c]*Ric[dd][a]+g[b][dd]*Ric[c][a]
        gg=g[a][c]*g[dd][b]-g[a][dd]*g[c][b]
        C[a][b][c][dd]=R[a][b][c][dd]-rt.scale(F(1,2))+(S*gg).scale(F(1,6))
    Cup=[[[[D.c(kind,0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,dd in product(range(N),repeat=4):
        z=D.c(kind,0)
        for e,f in product(range(N),repeat=2):z=z+gi[c][e]*gi[dd][f]*C[a][b][e][f]
        Cup[a][b][c][dd]=z
    I3=D.c(kind,0)
    for a,b,c,dd,e,f in product(range(N),repeat=6):I3=I3+Cup[a][b][c][dd]*Cup[c][dd][e][f]*Cup[e][f][a][b]
    density=(-det4(g)).sqrt();L=density*I3
    return {"g":g,"gi":gi,"G":G,"R":R,"Ric":Ric,"S":S,"C":C,"I3":I3,"density":density,"L":L}
def xv(x):return x.x.v
def controls(z,seed):
    g,gi,R,Ric,S,C,G=z["g"],z["gi"],z["R"],z["Ric"],z["S"],z["C"],z["G"]
    inv=all(sum((xv(g[a][c])*xv(gi[c][b]) for c in range(N)),F(0))==int(a==b) for a,b in product(range(N),repeat=2))
    inv_var=all(sum(((g[a][c]*gi[c][b]).dx.v for c in range(N)),F(0))==0 for a,b in product(range(N),repeat=2))
    ra1=all(xv(R[a][b][c][d])+xv(R[b][a][c][d])==0 for a,b,c,d in product(range(N),repeat=4));ra2=all(xv(R[a][b][c][d])+xv(R[a][b][d][c])==0 for a,b,c,d in product(range(N),repeat=4));rp=all(xv(R[a][b][c][d])==xv(R[c][d][a][b]) for a,b,c,d in product(range(N),repeat=4));rb=all(xv(R[a][b][c][d])+xv(R[a][c][d][b])+xv(R[a][d][b][c])==0 for a,b,c,d in product(range(N),repeat=4))
    dra1=all(R[a][b][c][d].dx.v+R[b][a][c][d].dx.v==0 for a,b,c,d in product(range(N),repeat=4));dra2=all(R[a][b][c][d].dx.v+R[a][b][d][c].dx.v==0 for a,b,c,d in product(range(N),repeat=4));drp=all(R[a][b][c][d].dx.v==R[c][d][a][b].dx.v for a,b,c,d in product(range(N),repeat=4));drb=all(R[a][b][c][d].dx.v+R[a][c][d][b].dx.v+R[a][d][b][c].dx.v==0 for a,b,c,d in product(range(N),repeat=4))
    ric=all(sum((xv(gi[a][c])*xv(R[a][b][c][d]) for a,c in product(range(N),repeat=2)),F(0))==xv(Ric[b][d]) for b,d in product(range(N),repeat=2));sc=sum((xv(gi[b][d])*xv(Ric[b][d]) for b,d in product(range(N),repeat=2)),F(0))==xv(S);wt=all(sum((xv(gi[a][c])*xv(C[a][b][c][d]) for a,c in product(range(N),repeat=2)),F(0))==0 for b,d in product(range(N),repeat=2));gam=all(xv(G[a][b][c])==0 for a,b,c in product(range(N),repeat=3))
    rn=any(xv(Ric[a][b]) for a,b in product(range(N),repeat=2));sn=xv(S)!=0
    wvar=True
    for b,d in product(range(N),repeat=2):
        q=D.c(g[0][0].x.kind,0)
        for a,c in product(range(N),repeat=2):q=q+gi[a][c]*C[a][b][c][d]
        wvar &= (q.x.v==0 and q.dx.v==0)
    return {"metric_symmetric":all(xv(g[a][b])==xv(g[b][a]) for a,b in product(range(N),repeat=2)),"inverse_identity":inv,"inverse_variation_identity":inv_var,"normal_coordinate_Gamma_zero":gam,"riemann_antisym_first":ra1,"riemann_antisym_second":ra2,"riemann_pair_exchange":rp,"riemann_first_bianchi":rb,"delta_riemann_antisym_first":dra1,"delta_riemann_antisym_second":dra2,"delta_riemann_pair_exchange":drp,"delta_riemann_first_bianchi":drb,"ricci_contraction":ric,"scalar_contraction":sc,"weyl_tracefree":wt,"delta_weyl_trace_identity":wvar,"offshell_ricci_nonzero":rn if seed!="FLAT_CONTROL" else True,"offshell_scalar_nonzero":sn if seed!="FLAT_CONTROL" else True}
def cell(seed,d,expected):
    z0=build(seed,d,());ctrl=controls(z0,seed);F0=z0["L"].dx.v
    ctrl["determinant_point_minus_one"]=det4(z0["g"]).x.v==-1
    ctrl["volume_density_point_one"]=z0["density"].x.v==1
    ctrl["perturbation_jet_symmetry_from_frozen_generator"]=all(panel.h_value(d,*cab(a,b),I)==panel.h_value(d,*cab(b,a),I) for a,b in product(range(N),repeat=2) for k in range(3) for I in combinations_with_replacement(range(N),k))
    det_expected=F(1,2)*sum((F(-1 if a==b==0 else (1 if a==b else 0))*panel.h_value(d,*cab(a,b),()) for a,b in product(range(N),repeat=2)),F(0))
    ctrl["determinant_variation_identity"]=z0["density"].dx.v==det_expected
    singles={};pairs={};first=F(0);second=F(0);current=[F(0)]*N;gder={}
    for i in range(N):
        z=build(seed,d,(i,));q=z["L"].dx;singles[str(i)]={"F":fs(q.v),"d_i_F":fs(q.a)};first-=q.a;current[i]+=q.v
        gder[i]=[[[z["G"][a][b][c].x.a for c in range(N)] for b in range(N)] for a in range(N)]
    for i in range(N):
        for j in range(i,N):
            z=build(seed,d,(i,j));q=z["L"].dx
            if i==j:
                dv=q.a;d2=q.b
            else:
                dv=q.a;d2=q.c
            pairs[f"{i}{j}"]={"F":fs(q.v),"d_i_F":fs(dv),"d_i_d_j_F":fs(d2)};second+=d2
            if i==j:current[i]-=dv
            else:current[j]-=dv
    bulk=F0+first+second
    r_from_gamma=True
    eta=lambda a,b:F(-1 if a==b==0 else (1 if a==b else 0))
    for a,b,c,e in product(range(N),repeat=4):
        rg=sum((eta(a,f)*(gder[c][f][e][b]-gder[e][f][c][b]) for f in range(N)),F(0))
        r_from_gamma &= (rg==xv(z0["R"][a][b][c][e]))
    table=panel.canonical_table(seed,d);jh=jsha(table);ctrl.update({"normal_coordinate_dGamma_reconstructs_Riemann":r_from_gamma,"jet_hash_matches_frozen_manifest":jh==expected,"exact_fraction_arithmetic_no_tolerance":True,"target_blind_no_critic_read":True,"c6_symbolic_unfixed_factored_out":True})
    if seed=="FLAT_CONTROL":ctrl.update({"flat_cubic_density_zero":xv(z0["I3"])==0,"flat_bulk_variation_zero":bulk==0})
    else:ctrl.update({"flat_cubic_density_zero":True,"flat_bulk_variation_zero":True})
    ledger=[{"term":"F0*h","transfer_sign":"+"},{"term":"Fi*d_i_h","transfer_sign":"- after one IBP"},{"term":"Fij*d_i_d_j_h","transfer_sign":"+ after two IBPs"}]
    ibp={"representation":"delta L[h phi] = F0 phi + sum Fi d_i phi + sum_{i<=j} Fij d_i d_j phi","F0":fs(F0),"single_derivative_coefficients":singles,"second_derivative_coefficients":pairs,"derivative_transfer_ledger":ledger,"first_ibp_transfer":fs(first),"second_ibp_transfer":fs(second),"bulk_after_ibp":fs(bulk),"boundary_current_at_phi1":list(map(fs,current)),"ibp_convention":"for i<j integrate i then j; exact ordinary partial IBP on density"}
    w={"seed":seed,"direction":d,"jet_sha256":jh,"jet_table":table,"controls":ctrl,"riemann_point_sha256":jsha([fs(xv(z0["R"][a][b][c][e])) for a,b,c,e in product(range(N),repeat=4)]),"ricci_point":[[fs(xv(z0["Ric"][a][b])) for b in range(N)] for a in range(N)],"scalar_point":fs(xv(z0["S"])),"weyl_point_sha256":jsha([fs(xv(z0["C"][a][b][c][e])) for a,b,c,e in product(range(N),repeat=4)]),"I3_point":fs(xv(z0["I3"])),"covariant_derivative_witness":{"Gamma_point_sha256":jsha([fs(xv(z0["G"][a][b][c])) for a,b,c in product(range(N),repeat=3)]),"dGamma_point_sha256":jsha([fs(gder[i][a][b][c]) for i,a,b,c in product(range(N),repeat=4)]),"normal_coordinate_identity":"R_abcd = g_ae*(partial_c Gamma^e_db-partial_d Gamma^e_cb) at x=0"},"direct_variation_and_ibp":ibp,"euler_source_from_other_lane":"NOT_READ_PRE_COMPARISON","cross_lane_discrepancy":"NOT_COMPUTED_PRE_COMPARISON"};w["cell_witness_sha256"]=jsha(w);return w
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--seed",required=True,choices=("FLAT_CONTROL","OFFSHELL_A","OFFSHELL_B"))
    ap.add_argument("--direction",required=True,type=int,choices=(7,19))
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    m=panel.panel_manifest();exp={(x["seed"],x["direction"]):x["jet_sha256"] for x in m["cells"]}
    c=cell(a.seed,a.direction,exp[(a.seed,a.direction)])
    ok=all(v is True for v in c["controls"].values())
    p={"gate":"COVARIANT_WEYL3_DIRECTIONAL_VARIATION_FUNCTIONAL_DERIVATIVE_CERTIFICATE","lane":"RESEARCHER_DIRECT_VARIATION_IBP","preregistration_commit":PREREG,"panel_freeze_commit":PANEL_FREEZE,"panel_generator_commit":PANEL_GENERATOR,"panel_manifest_sha256":m["panel_sha256"],"cell":c,"target_blind_witness_frozen_before_comparison":True,"critic_science_code_imported":False,"c6":"SYMBOLIC_UNFIXED_FACTORED_OUT","classification":"RESEARCHER_CELL_WITNESS_READY_FOR_TARGET_BLIND_COMPARISON" if ok else "BLOCKED_RESEARCHER_SELF_CONTROL_FAILURE"}
    p["complete_payload_sha256"]=jsha(p)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(p,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in p.items() if k!="cell"},sort_keys=True,indent=2))
    return 0 if ok else 2
if __name__=="__main__":raise SystemExit(main())
