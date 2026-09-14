#!/usr/bin/env python3
import argparse, json, os, re
from pathlib import Path

GATE='ITER054L-QUANTUM-AMPLITUDE-MEASURE-CLOSURE-AUTHORITY'
ROOT=Path('.')
GOV=[Path('README.md'),Path('docs/CONSTITUTION.md'),Path('docs/ROADMAP.md'),Path('docs/KMQGB_HANDOFF.md')]
CAND_DIRS=[Path('iterations'),Path('analysis'),Path('status')]
TEXT_EXT={'.md','.txt','.json','.py'}

PATTERNS={
 'amplitude_measure':[r'\bamplitude\b',r'\bmeasure\b',r'path integral',r'probability weight'],
 'normalization':[r'normaliz',r'partition function',r'\bZ\b',r'sum of weights',r'total probability'],
 'regulator_removal':[r'regulator removal',r'renormaliz',r'distributional extension',r'continuum limit',r'h\s*->\s*0',r'h→0'],
 'c6_identity':[r'\bc6\b',r'Weyl\^?3',r'Weyl3'],
 'cross_level_observable':[r'observable',r'microscopic.*IR',r'IR.*microscopic',r'UV.*IR',r'common-domain']
}

def read(p):
 try:return p.read_text(encoding='utf-8',errors='ignore')
 except:return ''

def hits(text, pats):
 out=[]
 for p in pats:
  if re.search(p,text,re.I|re.S): out.append(p)
 return out

def candidate_files():
 fs=[]
 for d in CAND_DIRS:
  if not d.exists(): continue
  for p in d.rglob('*'):
   if p.is_file() and p.suffix.lower() in TEXT_EXT: fs.append(p)
 return sorted(fs)

def witness_map(files):
 wm={k:[] for k in PATTERNS}
 for p in files:
  t=read(p)
  for k,ps in PATTERNS.items():
   hs=hits(t,ps)
   if hs: wm[k].append({'path':str(p),'patterns':hs[:4]})
 return wm

def lane_a0():
 wm=witness_map([p for p in GOV if p.exists()])
 return {'gate':GATE,'lane':'A0','valid':True,'pass':True,'source_count':sum(p.exists() for p in GOV),'governance_witnesses':wm,'note':'governance hits are obligations/discovery evidence only, not physical authority'}

def lane_a1():
 fs=candidate_files(); wm=witness_map(fs)
 presence={k:bool(v) for k,v in wm.items()}
 return {'gate':GATE,'lane':'A1','valid':True,'pass':True,'source_count':len(fs),'candidate_witnesses':wm,'category_presence':presence,'note':'keyword/source witnesses require later raw-source semantic review'}

def lane_b0():
 fs=candidate_files(); joint=[]; obs=[]
 for p in fs:
  t=read(p)
  if re.search(r'\bc6\b|Weyl\^?3|Weyl3',t,re.I) and re.search(r'microscopic|UV|event|state|measure|amplitude',t,re.I):
   joint.append(str(p))
  if re.search(r'observable',t,re.I) and re.search(r'microscopic|UV',t,re.I) and re.search(r'\bIR\b|infrared|Einstein|GR',t,re.I):
   obs.append(str(p))
 return {'gate':GATE,'lane':'B0','valid':True,'pass':True,'candidate_c6_identity_review_paths':joint,'cross_level_observable_review_paths':obs,'explicit_c6_identity_authorized':False,'cross_level_observable_authorized':False,'note':'paths are review candidates only; authorization remains false pending semantic review'}

def lane_b1():
 s=json.loads(read(Path('recovery/state.json')) or '{}'); locks=s.get('claim_locks',{})
 required=['qgr_theory_established','qgr_experimentally_confirmed','beta_set_to_one_authorized','qgr_six_derivative_coefficient_fixed','quantum_amplitude_measure_transition_authorized','uv_complete','new_model_required_by_kmqgb']
 vals={k:locks.get(k,None) for k in required}
 ok=all(vals.get(k) is False for k in required)
 return {'gate':GATE,'lane':'B1','valid':True,'pass':ok,'controls':vals}

def aggregate(paths):
 lanes={}
 for p in paths:
  x=json.loads(Path(p).read_text()); lanes[x['lane']]=x
 complete=all(k in lanes and lanes[k].get('valid') for k in ['A0','A1','B0','B1'])
 candidate=lanes.get('A1',{}).get('category_presence',{})
 missing=[k for k in PATTERNS if not candidate.get(k,False)]
 review_paths={'c6_identity':lanes.get('B0',{}).get('candidate_c6_identity_review_paths',[]),'cross_level_observable':lanes.get('B0',{}).get('cross_level_observable_review_paths',[])}
 all_categories=(len(missing)==0 and bool(review_paths['c6_identity']) and bool(review_paths['cross_level_observable']))
 classification='SOURCE_AUTHORITY_PRESENT_FOR_REVIEW_ITER054L' if complete and all_categories and lanes['B1'].get('pass') else 'REQUIRES_SOURCE_AUTHORITY_REVIEW_ITER054L'
 return {'gate':GATE,'lane':'AGGREGATE','complete':complete,'valid':complete,'classification':classification,'missing_discovery_categories':missing,'review_paths':review_paths,'physical_quantum_measure_authorized':False,'c6_fixed':False,'beta_one_authorized':False,'theory_established_pct':0}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True); ap.add_argument('inputs',nargs='*'); a=ap.parse_args()
 if a.lane=='A0': x=lane_a0()
 elif a.lane=='A1': x=lane_a1()
 elif a.lane=='B0': x=lane_b0()
 elif a.lane=='B1': x=lane_b1()
 elif a.lane=='aggregate': x=aggregate(a.inputs)
 else: raise SystemExit(2)
 Path(a.out).write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
 print(json.dumps(x,indent=2,sort_keys=True))
 if a.lane!='aggregate' and not x.get('pass',True): raise SystemExit(1)

if __name__=='__main__': main()
