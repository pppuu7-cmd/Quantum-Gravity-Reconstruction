#!/usr/bin/env python3
"""Aggregate frozen QGR Iter038 principal regularity/blocking gate."""
import glob,json,os,sys

EXPECTED={'certificate':1,'gap':8,'path':8,'loop':12}
TOTAL=sum(EXPECTED.values())

def main():
    rows=[]
    for p in glob.glob('iter038-results/**/result.json',recursive=True):
        try:
            with open(p,encoding='utf-8') as f: rows.append(json.load(f))
        except Exception: pass
    by={k:[] for k in EXPECTED}
    for r in rows:
        s=r.get('stream')
        if s in by: by[s].append(r)
    unique=set((r.get('stream'),r.get('index')) for r in rows if r.get('stream') in EXPECTED)
    counts={k:len(set(r.get('index') for r in v)) for k,v in by.items()}
    passes={k:sum(bool(r.get('lane_pass')) for r in v) for k,v in by.items()}
    complete=bool(len(unique)==TOTAL and all(counts[k]==EXPECTED[k] for k in EXPECTED))
    cert_pass=bool(counts['certificate']==1 and passes['certificate']==1)
    all_pass=bool(complete and cert_pass and all(passes[k]==EXPECTED[k] for k in EXPECTED))
    if all_pass:
        cls='PASS_SCOPED_PRINCIPAL_COMPACT_REFINEMENT_REGULARITY_AND_FINE_TO_COARSE_BLOCKING'
    elif cert_pass:
        cls='PARTIAL_SCOPED_PRINCIPAL_SMALL_H_REGULARITY_CERTIFIED_BLOCKING_INCOMPLETE'
    else:
        cls='FAIL_OR_BLOCKED_PRINCIPAL_SMALL_H_CERTIFICATE'
    cert=by['certificate'][0] if by['certificate'] else {}
    gap_mins=[]; gap_conds=[]; path_ratios=[]; loop_ratios=[]
    for r in by['gap']:
        for x in r.get('rows',[]):
            if x.get('success') and isinstance(x.get('min_singular'),(int,float)): gap_mins.append(x['min_singular'])
            if x.get('success') and isinstance(x.get('condition'),(int,float)): gap_conds.append(x['condition'])
    for r in by['path']:
        if isinstance(r.get('final_contraction_ratio'),(int,float)): path_ratios.append(r['final_contraction_ratio'])
    for r in by['loop']:
        if isinstance(r.get('final_contraction_ratio'),(int,float)): loop_ratios.append(r['final_contraction_ratio'])
    summary={
        'gate':'ITER038-PRINCIPAL-REFINEMENT-REGULARITY-AND-BLOCKING',
        'expected_lanes':TOTAL,'found_unique_lanes':len(unique),'counts':counts,'passes':passes,
        'exact_linearized_rank':cert.get('rank'),'exact_linearized_determinant':cert.get('determinant'),
        'exact_linearized_min_singular_numeric':cert.get('min_singular_numeric'),
        'minimum_finite_bridge_jacobian_singular':min(gap_mins) if gap_mins else None,
        'maximum_finite_bridge_condition':max(gap_conds) if gap_conds else None,
        'maximum_path_final_contraction_ratio':max(path_ratios) if path_ratios else None,
        'maximum_loop_final_contraction_ratio':max(loop_ratios) if loop_ratios else None,
        'classification':cls,
        'analytic_scope':'Exact common h=0 scaled-residual derivative invertibility + analyticity + compact K=[0,1]^4 supplies a uniform sufficiently-small-h principal IFT branch/gap on this frozen smooth realization; finite B/C/D lanes bridge and test actual blocking but do not prove arbitrary-background/global field-space regularity.',
        'claim_lock':'Does not fix beta, absolute action-phase normalization, c6, global field-space compactness, or theory correctness.'
    }
    os.makedirs('iter038-summary',exist_ok=True)
    with open('iter038-summary/summary.json','w',encoding='utf-8') as f:
        json.dump(summary,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(summary,sort_keys=True))
    if not complete: sys.exit(2)

if __name__=='__main__': main()
