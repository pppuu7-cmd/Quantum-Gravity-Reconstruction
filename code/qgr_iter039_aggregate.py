#!/usr/bin/env python3
"""Aggregate frozen QGR Iter039 30-lane absolute scale identifiability gate."""
import glob,json,os,sys

AUDITS=['source-null','refinement-beta-blind','current-authority-rank','minimal-calibration-rank','beta-sign']
EXPECTED=30

def main():
    rows=[]
    for p in glob.glob('iter039-results/**/result.json',recursive=True):
        try:
            with open(p,encoding='utf-8') as f: rows.append(json.load(f))
        except Exception: pass
    seen={(r.get('audit'),r.get('lane')) for r in rows}
    counts={a:len({r.get('lane') for r in rows if r.get('audit')==a}) for a in AUDITS}
    passes={a:sum(bool(r.get('passed')) for r in rows if r.get('audit')==a) for a in AUDITS}
    complete=(len(seen)==EXPECTED and all(counts[a]==6 for a in AUDITS))
    allpass=(complete and all(passes[a]==6 for a in AUDITS))
    cls=('PASS_SCOPED_INTERNAL_ABSOLUTE_SCALE_NONIDENTIFIABILITY_AND_MINIMAL_CALIBRATION_RANK_DERIVED'
         if allpass else 'PARTIAL_OR_CONTROL_INVALID_ABSOLUTE_SCALE_IDENTIFIABILITY_AUDIT')
    max_ref=max([r.get('max_output_difference',0.0) for r in rows if r.get('audit')=='refinement-beta-blind'] or [None])
    summary={
        'gate':'ITER039-ABSOLUTE-SOURCE-PHASE-IDENTIFIABILITY',
        'expected_lanes':EXPECTED,'found_unique_lanes':len(seen),'counts':counts,'passes':passes,
        'source_scale_nullity':1 if allpass else None,
        'current_absolute_authority_rank_on_u_c6':0 if allpass else None,
        'minimal_rank_with_one_absolute_target':1 if allpass else None,
        'minimal_rank_with_independent_conformal_plus_weyl_absolute_targets':2 if allpass else None,
        'maximum_g38_output_difference_across_dummy_beta_witnesses':max_ref,
        'classification':cls,
        'decision':'Treat beta as explicit calibration/matching parameter under current authority; do not search it numerically or set beta=1 as physics. c6 remains unfixed until a genuine independent Weyl-active absolute phase/matching datum exists.' if allpass else 'No terminal identifiability decision.',
        'claim_lock':'This is a no-go under current authorized QGR data only; hypothetical calibration rows are not physical data and a future microscopic normalization principle could change the rank.'
    }
    os.makedirs('iter039-summary',exist_ok=True)
    with open('iter039-summary/summary.json','w',encoding='utf-8') as f:
        json.dump(summary,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(summary,sort_keys=True))
    if not complete: sys.exit(2)

if __name__=='__main__': main()
