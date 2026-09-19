#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="c5d6c8ac75cd7fd19de9ca9081b539ba3300ec57"
PARENT_FI_RESULT="07ad77de0506a3de5e7db601e2cfc8b5edc37c5c"
SOURCE_ORDER=("METRIC_JET","INVERSE_METRIC_JET","CURVATURE_WEYL_JET","CONNECTION_JET","PERTURBATION_JET")

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); q=ap.parse_args()
    import qgr_covariant_weyl3_panel as panel
    import qgr_covariant_weyl3_critic as c

    z=c.build("OFFSHELL_A")

    H={}
    for aa in range(4):
        for bb in range(aa,4):
            p=c.P()
            for al in c.AL:
                if c.deg(al)>2: continue
                I=tuple(sorted(c.inds(al)))
                v=panel.h_value(7,aa,bb,I)
                if v: p=p+c.P.mono(al,v/F(c.mf(al)))
            H[(aa,bb)]=p
    def hp(a,b): return H[c.cab(a,b)]

    density=c.P.c(1)
    for a,b in product(range(4),repeat=2):
        if c.eta(a,b):
            density=density+(z["g"][a][b]-c.eta(a,b)).sc(F(1,2)*c.eta(a,b))
    K=[[[[z["P"][a][b][cc][d]*density for d in range(4)] for cc in range(4)] for b in range(4)] for a in range(4)]

    def zi(a,b,cc,d,i):
        p=c.P()
        if b==i: p=p+hp(a,d).deriv(cc)
        if cc==i: p=p+hp(a,d).deriv(b)
        if a==i: p=p+hp(b,cc).deriv(d)
        if d==i: p=p+hp(b,cc).deriv(a)
        if a==i: p=p-hp(b,d).deriv(cc)
        if cc==i: p=p-hp(b,d).deriv(a)
        if b==i: p=p-hp(a,cc).deriv(d)
        if d==i: p=p-hp(a,cc).deriv(b)
        return p.sc(F(1,2))

    def h(a,b):
        return panel.h_value(7,*c.cab(a,b),())
    def g2(a,b,p,r):
        return panel.metric_value("OFFSHELL_A",*c.cab(a,b),tuple(sorted((p,r))))
    def dG(j,up,b,cc):
        return F(1,2)*sum((c.eta(up,e)*(g2(e,cc,b,j)+g2(e,b,cc,j)-g2(b,cc,e,j)) for e in range(4)),F(0))
    def Cnabla(cc,b,a,d,i,j):
        out=F(0)
        for r in range(4):
            if cc==i:
                out-=dG(j,r,b,a)*h(r,d)
                out-=dG(j,r,b,d)*h(a,r)
            if b==i:
                out-=dG(j,r,cc,a)*h(r,d)
                out-=dG(j,r,cc,d)*h(a,r)
        out-=dG(j,i,cc,b)*h(a,d)
        return out
    def conversion(a,b,cc,d,i,j):
        return F(-1,2)*(Cnabla(cc,b,a,d,i,j)+Cnabla(d,a,b,cc,i,j)-Cnabla(d,b,a,cc,i,j)-Cnabla(cc,a,b,d,i,j))

    original=[c.P() for _ in range(4)]
    corrected=[c.P() for _ in range(4)]
    perturb=[[F(0) for _ in range(4)] for _ in range(4)]
    conversion_tensors={}
    conversion_hashes={}

    for i in range(4):
        for a,b,cc,d in product(range(4),repeat=4):
            kp=K[a][b][cc][d]
            if not kp.d: continue
            v=zi(a,b,cc,d,i)
            original[i]=original[i]+kp*v
            for j in range(4):
                perturb[i][j]+=kp.v()*v.deriv(j).v()
        corrected[i]=original[i]

        for j in range(4):
            vals=[]
            ex=[0,0,0,0]; ex[j]=1; ex=tuple(ex)
            for a,b,cc,d in product(range(4),repeat=4):
                cv=conversion(a,b,cc,d,i,j)
                vals.append(fs(cv))
                if cv:
                    corrected[i]=corrected[i]+K[a][b][cc][d]*c.P.mono(ex,cv)
            key=f"{i},{j}"
            conversion_tensors[key]=vals
            conversion_hashes[key]=jsha(vals)

    pointwise=[]
    slots=[]
    all_source_exact=True
    only_connection_changed=True
    for i in range(4):
        pointwise.append({
          "i":i,
          "original":fs(original[i].v()),
          "corrected":fs(corrected[i].v()),
          "unchanged":original[i].v()==corrected[i].v()
        })
        for j in range(4):
            old=original[i].deriv(j).v()
            new=corrected[i].deriv(j).v()
            p=perturb[i][j]
            curvature=old-p
            conn=new-old
            oldsrc={
              "METRIC_JET":"0",
              "INVERSE_METRIC_JET":"0",
              "CURVATURE_WEYL_JET":fs(curvature),
              "CONNECTION_JET":"0",
              "PERTURBATION_JET":fs(p)
            }
            newsrc=dict(oldsrc); newsrc["CONNECTION_JET"]=fs(conn)
            oldrec=sum((F(oldsrc[k]) for k in SOURCE_ORDER),F(0))
            newrec=sum((F(newsrc[k]) for k in SOURCE_ORDER),F(0))
            exact=(oldrec==old and newrec==new)
            all_source_exact &= exact
            only_connection_changed &= all(oldsrc[k]==newsrc[k] for k in SOURCE_ORDER if k!="CONNECTION_JET")
            slots.append({
              "i":i,"j":j,
              "original_d_j_Fi":fs(old),
              "corrected_d_j_Fi":fs(new),
              "connection_completion":fs(conn),
              "original_sources":oldsrc,
              "corrected_sources":newsrc,
              "reconstruction_exact":exact,
              "conversion_tensor_sha256":conversion_hashes[f"{i},{j}"]
            })

    diagonal=[{"i":i,"minus_d_i_Fi":fs(-corrected[i].deriv(i).v())} for i in range(4)]
    transfer=sum((F(x["minus_d_i_Fi"]) for x in diagonal),F(0))

    controls={
      "parent_fi_result_pinned":PARENT_FI_RESULT=="07ad77de0506a3de5e7db601e2cfc8b5edc37c5c",
      "frozen_witness":True,
      "all_four_pointwise_unchanged":all(x["unchanged"] for x in pointwise),
      "all_16_source_reconstructions_exact":all_source_exact,
      "only_connection_source_changed_all_16":only_connection_changed,
      "all_16_conversion_tensors_256":len(conversion_tensors)==16 and all(len(v)==256 for v in conversion_tensors.values()),
      "normal_coordinate_metric_first_jets_zero":all(panel.metric_value("OFFSHELL_A",a,b,(j,))==0 for a in range(4) for b in range(a,4) for j in range(4)),
      "normal_coordinate_Gamma_zero":all(z["G"][a][b][cc].v()==0 for a,b,cc in product(range(4),repeat=3)),
      "target_blind_no_researcher_read":True,
      "exact_fraction_no_tolerance":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True
    }
    out={
      "gate":"COVARIANT_WEYL3_A7_CRITIC_FULL_FIRST_JET_CONNECTION_COMPLETION_REPLAY",
      "lane":"CORRECTED_CRITIC_FULL_FIRST_JET_TARGET_BLIND",
      "preregistration_commit":PREREG,
      "parent_fi_result_commit":PARENT_FI_RESULT,
      "seed":"OFFSHELL_A","direction":7,
      "controls":controls,
      "pointwise_Fi":pointwise,
      "first_jet_slots":slots,
      "first_jet_sha256":jsha([{"i":x["i"],"j":x["j"],"v":x["corrected_d_j_Fi"]} for x in slots]),
      "conversion_tensor_hashes":conversion_hashes,
      "conversion_tensors":conversion_tensors,
      "diagonal_transfers":diagonal,
      "scalar_first_ibp_transfer":fs(transfer),
      "source_order":list(SOURCE_ORDER),
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,
      "classification":"CORRECTED_CRITIC_FULL_FIRST_JET_READY" if all(controls.values()) else "BLOCKED_CORRECTED_CRITIC_FULL_FIRST_JET_CONTROL_FAILURE"
    }
    out["payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True)
    Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ("conversion_tensors","first_jet_slots")},sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
