#!/usr/bin/env python3
"""Iter057AH deterministic localization of the terminal Iter057AG dual witness."""
from __future__ import annotations
import argparse, hashlib, json, math
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import sympy as sp

import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ag_dual_obstruction_witness as ag

PREREG='9b55fb87f89456bb04d325c534cde025fcb9ad2e'
AG_DATA_COMMIT='79f447491834eaa67c2516d50433be619f098dd2'
AG_RESULT_COMMIT='057f6c9699c1e81cfe3042a711715bc65850f6e3'
AG_PAYLOAD='5ecb962af9a1265a8846a6d8de4cd0885c2b53bea630a5729a8c069aae9fd9da'
PASS='PASS_SCOPED_ITER057AH_EXACT_DUAL_WITNESS_LOCALIZED_AND_FACTORIZED_WITH_ORIGINAL_SYSTEM_ACCOUNTING'
INVALID='INVALID_ITER057AH_FROZEN_ITER057AG_WITNESS_OR_ORDERING_CONTRADICTION'
BLOCKED='BLOCKED_ITER057AH_EXACT_LOCALIZATION_NOT_TECHNICALLY_REALIZED'
ROOT=Path(__file__).resolve().parents[1]
AG_DATA=ROOT/'data'/'ITER057AG_CANONICAL_DUAL_WITNESS.json'

def ff(x):
    if isinstance(x,F): return x
    if isinstance(x,sp.Rational): return F(int(x.p),int(x.q))
    return F(str(x))

def fstr(x):
    x=ff(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def canonical_y_from_file():
    d=json.loads(AG_DATA.read_text())
    y=[F(0)]*ag.NROWS
    for r in d['canonical_y']:
        i=int(r['compatibility_index']);
        if y[i]: raise ValueError('duplicate canonical y index')
        y[i]=F(r['value'])
    ok=(d.get('preregistration_commit')=='11dfc1e4db79ff691fe121ab38281f3532f931bf' and d.get('scientific_payload_sha256')==AG_PAYLOAD and d.get('classification')==ag.PASS and d.get('y_nonzero_count')==56 and d.get('w_nonzero_count')==308)
    return d,y,ok

def localize_y(y):
    a11=z.alphas(11); n=len(a11); rows=[]; reconstructed=[F(0)]*ag.NROWS
    for i,v in enumerate(y):
        if not v: continue
        b=i//n; beta=a11[i%n]
        rows.append({'compatibility_index':i,'b':b,'beta':list(beta),'value':fstr(v),'parity':[q%2 for q in beta]})
        reconstructed[b*n+a11.index(beta)]=v
    return a11,rows,reconstructed

def polynomial_data(rows):
    t,x,yv,zv=sp.symbols('t x y z'); vars=(t,x,yv,zv); polys=[]
    for b in range(4):
        p=sp.Integer(0); vals=[]
        for r in rows:
            if r['b']!=b: continue
            v=F(r['value']); vals.append(v); mon=sp.Integer(1)
            for q,e in zip(vars,r['beta']): mon*=q**e
            p += sp.Rational(v.numerator,v.denominator)*mon
        p=sp.expand(p)
        fac=sp.factor(p)
        if vals:
            den=1
            for v in vals: den=math.lcm(den,v.denominator)
            ints=[v.numerator*(den//v.denominator) for v in vals]
            g=0
            for a in ints:g=math.gcd(g,abs(a))
            g=max(g,1); primitive=sp.expand(p*sp.Rational(den,g)); scale=sp.Rational(g,den)
            prim_ok=sp.expand(scale*primitive-p)==0
        else:
            den=1;g=1;primitive=sp.Integer(0);scale=sp.Integer(1);prim_ok=True
        fac_ok=sp.expand(fac-p)==0
        polys.append({'b':b,'expanded':str(p),'factorized':str(fac),'factorization_reconstructs':bool(fac_ok),'primitive_integer_polynomial':str(primitive),'primitive_scale':str(scale),'common_denominator':den,'integer_content_gcd':g,'primitive_reconstructs':bool(prim_ok),'nonzero_term_count':sum(1 for r in rows if r['b']==b)})
    stabilizer=[]; spatial=(x,yv,zv)
    for perm in permutations(range(3)):
        mapping={spatial[i]:spatial[perm[i]] for i in range(3)}
        if all(sp.expand(sp.sympify(pd['expanded']).xreplace(mapping)-sp.sympify(pd['expanded']))==0 for pd in polys):
            stabilizer.append(list(perm))
    return polys,stabilizer

def key_parity(typ,al): return typ+':' + ''.join(str(int(e)%2) for e in al)

def localize_w(w,meta14,r0):
    rows=[]; by_type=defaultdict(lambda:{'support_count':0,'contribution':F(0)})
    by_component=defaultdict(lambda:{'support_count':0,'contribution':F(0)})
    by_parity=defaultdict(lambda:{'support_count':0,'contribution':F(0)})
    total=F(0)
    for i,wi in sorted(w.items()):
        typ,obj,al=meta14[i]; ri=ff(r0[i]); c=wi*ri; total+=c
        obj_ser=int(obj) if typ=='G' else list(obj)
        ck=f'G:{obj}' if typ=='G' else f'F:{obj[0]}{obj[1]}'
        pk=key_parity(typ,al)
        by_type[typ]['support_count']+=1; by_type[typ]['contribution']+=c
        by_component[ck]['support_count']+=1; by_component[ck]['contribution']+=c
        by_parity[pk]['support_count']+=1; by_parity[pk]['contribution']+=c
        rows.append({'affine_row_index':i,'type':typ,'component':obj_ser,'alpha':list(al),'parity':[int(e)%2 for e in al],'w':fstr(wi),'r0':fstr(ri),'contribution':fstr(c)})
    def ser(d): return {k:{'support_count':v['support_count'],'contribution':fstr(v['contribution'])} for k,v in sorted(d.items())}
    return rows,ser(by_type),ser(by_component),ser(by_parity),total

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old-root',required=True);ap.add_argument('--af-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    agdoc,y,file_ok=canonical_y_from_file(); a11,yrows,yrec=localize_y(y); polys,stabilizer=polynomial_data(yrows)
    recs,cols,lane_controls,coverage,dup=ag.assemble(Path(a.old_root),Path(a.af_root))
    M14,rows14,L,r0,O0,prov,inv,ann=ag.canonical_object(); bt,norm=ag.residuals(cols,O0,y); w=ag.induced_w(L,y); origres,wdot=ag.verify_original(rows14,r0,w,M14.cols)
    # metadata returned by rhs14/system is frozen row ordering used by L and r0.
    _,_,meta14,_,_,_=ag.ad.rhs14(ag.ad.canonical_seed12()[0])
    wrows,bytype,bycomp,byparity,contrib_total=localize_w(w,meta14,r0)
    # Exact support characterization is reported, not assumed by the gate.
    b_support=sorted({r['b'] for r in yrows}); parity_support=sorted({tuple(r['parity']) for r in yrows})
    controls={
      'A_frozen_AG_data_provenance':file_ok,
      'A_AG_payload_sha256':agdoc.get('scientific_payload_sha256')==AG_PAYLOAD,
      'B_y_localization_reconstructs_exactly':yrec==y,
      'B_y_nonzero_count_56':len(yrows)==56,
      'C_all_polynomial_factorizations_reconstruct':all(p['factorization_reconstructs'] for p in polys),
      'C_all_primitive_integer_forms_reconstruct':all(p['primitive_reconstructs'] for p in polys),
      'D_lane_payload_controls_exact':lane_controls and coverage and not dup,
      'D_BT_y_exact_zero':all(v==0 for v in bt),
      'D_O0T_y_exact_one':norm==1,
      'E_w_nonzero_count_308':len(wrows)==308,
      'E_wT_M14_exact_zero':not origres,
      'E_wT_r0_exact_one':wdot==1,
      'E_grouped_contributions_sum_one':contrib_total==1,
      'F_lower_authority_and_inverse':prov and inv and ann,
      'G_no_numerical_tolerance':True,
    }
    passed=all(controls.values())
    cls=PASS if passed else (INVALID if not (file_ok and yrec==y) else BLOCKED)
    payload={'gate':'ITER057AH-EXACT-DUAL-WITNESS-LOCALIZATION-AND-FACTORIZATION','preregistration':PREREG,'ag_data_commit':AG_DATA_COMMIT,'ag_result_commit':AG_RESULT_COMMIT,'ag_scientific_payload_sha256':AG_PAYLOAD,'classification':cls,'controls':controls,
      'compatibility_basis_size':len(a11)*4,'localized_y':yrows,'y_b_support':b_support,'y_parity_support':[list(p) for p in parity_support],'generating_polynomials':polys,'spatial_permutation_stabilizer':stabilizer,'spatial_stabilizer_order':len(stabilizer),
      'induced_w':wrows,'w_group_by_type':bytype,'w_group_by_component':bycomp,'w_group_by_parity':byparity,'w_contribution_total':fstr(contrib_total),
      'BT_y_nonzero_count':sum(v!=0 for v in bt),'O0T_y':fstr(norm),'wT_M14_nonzero_count':len(origres),'wT_r0':fstr(wdot),'exact_zero_uses_tolerance':False,
      'scope':'exact localization/factorization of the frozen finite local Iter057AG certificate only; no new branch or global/all-orders/quantum claim'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    brief={k:v for k,v in payload.items() if k not in ('localized_y','induced_w','generating_polynomials')}; print(json.dumps(brief,indent=2,sort_keys=True)); return 0 if passed else 2
if __name__=='__main__': raise SystemExit(main())
