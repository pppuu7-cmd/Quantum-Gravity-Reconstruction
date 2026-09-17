#!/usr/bin/env python3
"""Fresh isolated replay of historical Iter057AA for terminal-only comparison.

This lane is not imported or read by either corrected constructor lane.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'code'))
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa

PREREG='ddf4d41be23b09e5a4709149d85d85688a533fab'
AA_IMPL='29e6fb029f2d468b81e8d7b4e6dbe18d22baedd4'
AA_TERMINAL='2c84ddcb5dd22cfe06cd3a1a273b4a0e141b605e'
AA_PASS='PASS_SCOPED_ITER057AA_CORRECTED_DODECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_EIGHTH_EVEN_ORDER__O_C6_Q10_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED'

def fs(x):
    x=F(x);return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def jsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();old=aa.compute();sparse={}
    for r in old.get('Shat_normalized_sparse',[]):
        if int(r.get('degree',-1))==8:sparse[(int(r['pair'][0]),int(r['pair'][1]),tuple(int(x) for x in r['alpha']))]=F(r['value'])
    vec=[]
    for p in aa.PAIRS:
        for al in aa.alphas(8):vec.append({'pair':list(p),'alpha':list(al),'value':fs(sparse.get((p[0],p[1],tuple(al)),F(0)))})
    controls={'historical_AA_fresh_compute_pass':old.get('pass') is True,'historical_AA_classification_exact':old.get('classification')==AA_PASS,'historical_AA_degree8_basis_1650':len(vec)==1650,'historical_AA_target_isolation':True,'AA_implementation_pinned':AA_IMPL=='29e6fb029f2d468b81e8d7b4e6dbe18d22baedd4','AA_terminal_pinned':AA_TERMINAL=='2c84ddcb5dd22cfe06cd3a1a273b4a0e141b605e'}
    ok=all(controls.values());out={'gate':'CORRECTED_DEGREE8_WEYL3_SOURCE_RECONSTRUCTION','preregistration_commit':PREREG,'lane':'historical_iter057aa_comparator','classification':'READY_HISTORICAL_ITER057AA_DEGREE8_COMPARATOR' if ok else 'INVALID_HISTORICAL_ITER057AA_COMPARATOR_CONTROL_FAILURE','controls':controls,'historical_degree8_vector_sha256':jsha(vec),'historical_degree8_nonzero_count':sum(F(z['value'])!=0 for z in vec),'historical_degree8_vector':vec,'c6':'SYMBOLIC_UNFIXED_FACTORED_OUT'}
    p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');q=dict(out);q.pop('historical_degree8_vector');print(json.dumps(q,sort_keys=True,indent=2));return 0 if ok else 2
if __name__=='__main__':raise SystemExit(main())
