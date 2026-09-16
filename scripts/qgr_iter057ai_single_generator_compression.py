#!/usr/bin/env python3
"""Iter057AI exact single-generator compression of the AG/AH dual certificate."""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as sp

import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ag_dual_obstruction_witness as ag

PREREG='0a5e142aa18ca39fabb1817bf24d0909b0b75ba5'
AG_DATA_COMMIT='79f447491834eaa67c2516d50433be619f098dd2'
AH_DATA_COMMIT='e4c82732af6a0a150c5f2aa245e58a63b2d09c13'
AG_SHA='5ecb962af9a1265a8846a6d8de4cd0885c2b53bea630a5729a8c069aae9fd9da'
AH_SHA='8e7c74aa9d5c154f5be7fb8bcc8f0db8937e5a605d983ea20bf9fad067b9d661'
PASS='PASS_SCOPED_ITER057AI_DUAL_CERTIFICATE_COMPRESSES_TO_SINGLE_S3_SCALAR_BIANCHI_GENERATOR'
INVALID='INVALID_ITER057AI_FROZEN_AG_AH_AUTHORITY_CONTRADICTION'
BLOCKED='BLOCKED_ITER057AI_SINGLE_GENERATOR_COMPRESSION_NOT_TECHNICALLY_REALIZED'
ROOT=Path(__file__).resolve().parents[1]
AG_DATA=ROOT/'data'/'ITER057AG_CANONICAL_DUAL_WITNESS.json'
AH_DATA=ROOT/'data'/'ITER057AH_DUAL_WITNESS_LOCALIZATION.json'

def ff(x):
    if isinstance(x,F): return x
    if isinstance(x,sp.Rational): return F(int(x.p),int(x.q))
    return F(str(x))

def load_y():
    agd=json.loads(AG_DATA.read_text()); ahd=json.loads(AH_DATA.read_text())
    y=[F(0)]*ag.NROWS
    for r in agd['canonical_y']:
        i=int(r['compatibility_index']); y[i]=F(r['value'])
    prov=(agd.get('scientific_payload_sha256')==AG_SHA and agd.get('classification')==ag.PASS and ahd.get('scientific_payload_sha256')==AH_SHA and ahd.get('classification')=='PASS_SCOPED_ITER057AH_EXACT_DUAL_WITNESS_LOCALIZED_AND_FACTORIZED_WITH_ORIGINAL_SYSTEM_ACCOUNTING' and ahd.get('y_b_support')==[0] and ahd.get('y_parity_support')==[[1,0,0,0]] and ahd.get('spatial_stabilizer_order')==6)
    return agd,ahd,y,prov

def monomial(vars,alpha):
    m=sp.Integer(1)
    for v,e in zip(vars,alpha): m*=v**int(e)
    return m

def y_polys(y,vars):
    a11=z.alphas(11); n=len(a11); P=[sp.Integer(0)]*4
    for i,c in enumerate(y):
        if c:
            b=i//n; al=a11[i%n]; P[b]+=sp.Rational(c.numerator,c.denominator)*monomial(vars,al)
    return [sp.expand(p) for p in P]

def w_polys(w,meta,vars):
    G=[sp.Integer(0)]*4; Fp={pair:sp.Integer(0) for pair in z.PAIRS}
    for i,c in w.items():
        typ,obj,al=meta[i]; q=sp.Rational(c.numerator,c.denominator)*monomial(vars,al)
        if typ=='G': G[int(obj)] += q
        else: Fp[tuple(obj)] += q
    return [sp.expand(p) for p in G],{k:sp.expand(v) for k,v in Fp.items()}

def primitive_integer(poly):
    P=sp.Poly(sp.expand(poly)); coeffs=P.coeffs(); den=1
    for c in coeffs: den=math.lcm(den,int(sp.denom(c)))
    ints=[int(c*den) for c in coeffs]; g=0
    for v in ints:g=math.gcd(g,abs(v))
    g=max(g,1); prim=sp.expand(poly*sp.Rational(den,g)); scale=sp.Rational(g,den)
    return prim,scale,den,g

def invariant_reduce(Q,t,x,yv,zv):
    u,a,b,c=sp.symbols('u a b c'); e1,e2,e3=sp.symbols('e1 e2 e3')
    P=sp.Poly(sp.expand(Q),t,x,yv,zv); Rab=sp.Integer(0)
    even=True
    for exps,coef in P.terms():
        if any(e%2 for e in exps): even=False; continue
        et,ex,ey,ez=exps; Rab += coef*u**(et//2)*a**(ex//2)*b**(ey//2)*c**(ez//2)
    Rab=sp.expand(Rab)
    sym,rem,mapping=sp.symmetrize(Rab,[a,b,c],formal=True)
    subs={mapping[0][0]:e1,mapping[1][0]:e2,mapping[2][0]:e3}
    R=sp.expand(sym.subs(subs))
    back=sp.expand(R.subs({u:t**2,e1:x**2+yv**2+zv**2,e2:x**2*yv**2+x**2*zv**2+yv**2*zv**2,e3:x**2*yv**2*zv**2}))
    return {'even_exponents':even,'remainder':str(sp.expand(rem)),'R5':str(R),'back_substitution_exact':sp.expand(back-Q)==0,'R5_factorized':str(sp.factor(R))}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
    agd,ahd,y,prov=load_y(); t,x,yv,zv=sp.symbols('t x y z'); vars=(t,x,yv,zv); Y=y_polys(y,vars); Y0=Y[0]
    g0,seedprov=ag.ad.canonical_seed12(); M14,rows14,meta14,a11,r0,inv=ag.ad.rhs14(g0); L=ag.ad.left_controls(rows14,meta14,a11); ann=(L*M14)==sp.zeros(L.rows,M14.cols); w=ag.induced_w(L,y); origres,wdot=ag.verify_original(rows14,r0,w,M14.cols)
    WG,WF=w_polys(w,meta14,vars)
    targetG=[sp.expand(sp.Rational(1,2)*(-t**2+x**2+yv**2+zv**2)*Y0),sp.Integer(0),sp.Integer(0),sp.Integer(0)]
    targetF={pair:sp.Integer(0) for pair in z.PAIRS};targetF[(0,0)]=sp.expand(-t*Y0);targetF[(0,1)]=sp.expand(x*Y0);targetF[(0,2)]=sp.expand(yv*Y0);targetF[(0,3)]=sp.expand(zv*Y0)
    Gmatch=[sp.expand(WG[i]-targetG[i])==0 for i in range(4)]; Fmatch={f'{p[0]}{p[1]}':sp.expand(WF[p]-targetF[p])==0 for p in z.PAIRS}
    divisible=(Y0!=0 and sp.rem(sp.Poly(Y0,t),sp.Poly(t,t))==0); Qrat=sp.cancel(Y0/t) if divisible else Y0
    Qprim,scale,den,g=primitive_integer(Qrat); y0_reconstruct=sp.expand(scale*t*Qprim-Y0)==0
    invred=invariant_reduce(Qprim,t,x,yv,zv)
    controls={
      'A_frozen_AG_AH_provenance':prov,
      'A_seed_lower_authority':bool(seedprov) and bool(inv) and bool(ann),
      'B_Y1_Y2_Y3_exact_zero':all(Y[i]==0 for i in (1,2,3)),
      'B_Y0_exact_nonzero':Y0!=0,
      'C_WG_single_generator_formula_all4':all(Gmatch),
      'C_WF_single_generator_formula_all10':all(Fmatch.values()),
      'D_wT_M14_exact_zero':not origres,
      'D_wT_r0_exact_one':wdot==1,
      'E_Y0_t_factor_and_primitive_reconstruction':bool(divisible) and y0_reconstruct,
      'F_Q10_even_exponents':invred['even_exponents'],
      'F_S3_symmetric_reduction_zero_remainder':invred['remainder']=='0',
      'F_invariant_back_substitution_exact':invred['back_substitution_exact'],
      'G_no_numerical_tolerance':True,
    }
    passed=all(controls.values()); cls=PASS if passed else (INVALID if not prov else BLOCKED)
    payload={'gate':'ITER057AI-SINGLE-GENERATOR-BIANCHI-NOETHER-COMPRESSION','preregistration':PREREG,'ag_data_commit':AG_DATA_COMMIT,'ah_data_commit':AH_DATA_COMMIT,'classification':cls,'controls':controls,'Y0_nonzero_term_count':len(sp.Poly(Y0,t,x,yv,zv).terms()),'Y0_primitive_scale':str(scale),'Y0_primitive_Q10':str(Qprim),'Y0_reconstruction_exact':y0_reconstruct,
      'WG_nonzero_term_counts':[len(sp.Poly(p,t,x,yv,zv).terms()) if p!=0 else 0 for p in WG],'WF_nonzero_term_counts':{f'{p[0]}{p[1]}':(len(sp.Poly(WF[p],t,x,yv,zv).terms()) if WF[p]!=0 else 0) for p in z.PAIRS},'WG_formula_matches':Gmatch,'WF_formula_matches':Fmatch,
      'single_generator_formulas':{'WG0':'(1/2)*(-t^2+x^2+y^2+z^2)*Y0','WG1':'0','WG2':'0','WG3':'0','WF00':'-t*Y0','WF01':'x*Y0','WF02':'y*Y0','WF03':'z*Y0','all_other_WF':'0'},
      'symmetric_invariant_reduction':invred,'w_nonzero_count':len(w),'wT_M14_nonzero_count':len(origres),'wT_r0':str(wdot),'exact_zero_uses_tolerance':False,'scope':'single-generator algebraic compression of the frozen finite local dual certificate only; no new branch or physical/global/all-orders/quantum claim'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k not in ('Y0_primitive_Q10',)},indent=2,sort_keys=True));return 0 if passed else 2
if __name__=='__main__':raise SystemExit(main())
