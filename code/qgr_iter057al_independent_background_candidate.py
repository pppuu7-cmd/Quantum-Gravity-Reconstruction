#!/usr/bin/env python3
import argparse,json,hashlib
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import qgr_iter057al_generic_exact as z

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'data'/'ITER057AL_FROZEN_SEED_MANIFEST.json'
PREREG='c712f5034963048a8ab9a4ad812a47000a89be47'
MANIFEST_SHA='1e58ef49d36ac75efdd066f6b55ce2e48d9d8bce0307a9283ebe4483b026888f'
PASS='ADMISSIBLE_EXACT_ITER057AL_R12_BACKGROUND_CANDIDATE'
FAIL='EXACT_SOURCE_INCONSISTENT_ITER057AL_CANDIDATE'
EXPECTED={4:(164,16,186),6:(494,80,346),8:(1096,224,554),10:(2050,480,810),12:(3436,880,1114)}

def load_manifest():
 d=json.loads(MANIFEST.read_text());q=dict(d);got=q.pop('manifest_payload_sha256',None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 if got!=calc or got!=MANIFEST_SHA or d.get('preregistration')!=PREREG:raise RuntimeError('frozen manifest provenance mismatch')
 return d

def coeff_records(vec,d):
 A=z.alphas(d);key=f'R{d}_over_kappa{d//2}';out=[]
 for idx,v in enumerate(vec):
  if v==0:continue
  p=idx//len(A);a=A[idx%len(A)];out.append({'pair':list(z.PAIRS[p]),'alpha':list(a),key:str(sp.factor(v))})
 return out

def solve_stage(g,d):
 n=d-2;p=d//2;_,_,_,Ein,inv=z.geometry(g,n);lower=all(not z.homog(Ein[a][b],k) for a,b in z.PAIRS for k in range(0,n,2));target={(a,b):z.homog(Ein[a][b],n) for a,b in z.PAIRS}
 M,rows,meta,af,ag,au=z.build_system(d);rhs=[sp.Rational(0)]*(4*len(ag))
 for pair in z.PAIRS:
  poly=target[pair]
  for al in af:
   raw=poly.get(al,F(0));rhs.append(-z.qrat(raw*F(z.fact(al))/(z.K**p)))
 rhs=sp.Matrix(rhs);rankM=DomainMatrix.from_Matrix(M).to_field().rank();ann,comps=z.bianchi(rows,meta,rhs,d);cnz=sum(x!=0 for x in comps)
 Aug=M.row_join(rhs);R,piv=DomainMatrix.from_Matrix(Aug).to_field().rref();R=R.to_Matrix();piv=tuple(piv);rankAug=len(piv);consistent=(rankAug==rankM and all(j<M.cols for j in piv))
 vec=[sp.Rational(0)]*M.cols
 if consistent:
  for row,j in enumerate(piv):vec[j]=sp.factor(R[row,M.cols])
 residual=M*sp.Matrix(vec)-rhs if consistent else sp.Matrix([1]);rnz=sum(x!=0 for x in residual);records=coeff_records(vec,d) if consistent else []
 if consistent:z.add_rbar_layer(g,d,vec)
 _,Ric2,Sc2,Ein2,inv2=z.geometry(g,n);gnz=sum(bool(z.trunc(x,d-1)) for x in z.flat_gauge(g,d-1));ricnz=sum(bool(z.trunc(Ric2[a][b],n)) for a,b in z.PAIRS);enz=sum(bool(z.trunc(Ein2[a][b],n)) for a,b in z.PAIRS);scnz=bool(z.trunc(Sc2,n))
 erank,eleft,enull=EXPECTED[d]
 ok=bool(inv and lower and ann and cnz==0 and consistent and rnz==0 and rankM==erank and M.rows-rankM==eleft and M.cols-rankM==enull and len(comps)==eleft and inv2 and gnz==0 and ricnz==0 and not scnz and enz==0)
 return {'degree':d,'matrix_shape':list(M.shape),'matrix_nnz':sum(len(x) for x in rows),'rank':rankM,'rank_augmented':rankAug,'left_nullity':M.rows-rankM,'nullity':M.cols-rankM,'canonical_bianchi_count':len(comps),'compatibility_nonzero_count':cnz,'lower_Einstein_exact_zero_before_stage':lower,'target_Einstein_nonzero_component_count':sum(bool(x) for x in target.values()),'particular_nonzero_count':len(records),'affine_residual_nonzero_count':rnz,'inverse_after_ok':inv2,'final_deDonder_nonzero_count':gnz,'final_Ricci_nonzero_count':ricnz,'final_scalar_nonzero':bool(scnz),'final_Einstein_nonzero_count':enz,'coefficients':records,'ok':ok}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();mf=load_manifest();cs={c['candidate_id']:c for c in mf['candidates']}
 if a.candidate not in cs:raise SystemExit('candidate not frozen in manifest')
 c=cs[a.candidate];g,lam=z.seed2(F(c['family_parameter_r']));_,_,_,E0,inv0=z.geometry(g,0);seedE=sum(bool(E0[x][y]) for x,y in z.PAIRS);seedG=sum(bool(v) for v in z.flat_gauge(g,1));stages=[]
 for d in [4,6,8,10,12]:
  s=solve_stage(g,d);stages.append(s)
  if not s['ok']:break
 vals=[F(x) for x in c['quadratic_eigenvalues_over_kappa']];i2=sum(x*x for x in vals);i3=sum(x*x*x for x in vals);J=i3*i3/(i2**3)
 controls={'manifest_exact':True,'seed_static_harmonic_linear_vacuum':seedE==0 and seedG==0 and inv0,'seed_invariant_recomputed':str(i2)==c['I2_over_kappa2'] and str(i3)==c['I3_over_kappa3'] and str(J)==c['J_shape_invariant'],'independent_from_AF_by_scale_rotation_invariant_J':str(J)!=mf['canonical_AF_reference']['J_shape_invariant'],'all_five_exact_completion_stages_pass':len(stages)==5 and all(x['ok'] for x in stages),'no_R14_quantity_computed':True,'exact_rational_only':True}
 cls=PASS if all(controls.values()) else FAIL
 payload={'gate':'ITER057AL-INDEPENDENT-ONSHELL-R12-BACKGROUND-AUTHORITY','preregistration':PREREG,'manifest_payload_sha256':MANIFEST_SHA,'candidate':c,'classification':cls,'controls':controls,'stages':stages,'final_metric_max_degree':12,'scope':'finite local on-shell R12 candidate only; no R14 obstruction/witness quantity computed'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'candidate':a.candidate,'classification':cls,'scientific_payload_sha256':payload['scientific_payload_sha256'],'stages':[{k:s[k] for k in ['degree','rank','rank_augmented','compatibility_nonzero_count','particular_nonzero_count','ok']} for s in stages]},indent=2,sort_keys=True));return 0 if cls==PASS else 2
if __name__=='__main__':raise SystemExit(main())
