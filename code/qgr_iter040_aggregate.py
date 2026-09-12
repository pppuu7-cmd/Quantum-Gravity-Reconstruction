#!/usr/bin/env python3
"""Aggregate frozen QGR Iter040 calibration-free Weyl^3 response manifold."""
import glob,json,os,sys

EXPECTED={'A':4,'B':3,'C':3,'D':4,'E':6}
TOTAL=sum(EXPECTED.values())

def main():
    rows=[]
    for p in glob.glob('iter040-results/**/result.json',recursive=True):
        try:
            with open(p,encoding='utf-8') as f: rows.append(json.load(f))
        except Exception: pass
    by={k:[] for k in EXPECTED}
    for r in rows:
        s=r.get('stream')
        if s in by: by[s].append(r)
    counts={k:len({r.get('index') for r in v}) for k,v in by.items()}
    passes={k:sum(bool(r.get('lane_pass')) for r in v) for k,v in by.items()}
    unique={(r.get('stream'),r.get('index')) for r in rows if r.get('stream') in EXPECTED}
    complete=bool(len(unique)==TOTAL and all(counts[k]==EXPECTED[k] for k in EXPECTED))

    # Global relative-sign control required by preregistration: use finest-h Stream A values.
    A={r.get('shape_index'):r for r in by['A']}
    signs={}
    for idx in (0,1,3):
        rr=A.get(idx,{}).get('rows') or []
        if rr:
            v=rr[-1].get('weyl_cubic')
            if isinstance(v,(int,float)) and v!=0: signs[idx]=1 if v>0 else -1
    sign_pattern_ok=bool(len(signs)==3 and signs[0]==signs[1] and signs[3]==-signs[0])

    all_lane_pass=bool(complete and all(passes[k]==EXPECTED[k] for k in EXPECTED))
    full=bool(all_lane_pass and sign_pattern_ok)
    cls=('PASS_SCOPED_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD_ESTABLISHED'
         if full else 'PARTIAL_OR_CONTROL_INVALID_WEYL3_RESPONSE_MANIFOLD')

    slopes_w=[r.get('weyl_norm_kappa_slope') for r in by['B'] if isinstance(r.get('weyl_norm_kappa_slope'),(int,float))]
    slopes_c=[r.get('weyl_cubic_kappa_slope') for r in by['B'] if isinstance(r.get('weyl_cubic_kappa_slope'),(int,float))]
    spreads=[r.get('q_relative_spread') for r in by['C'] if isinstance(r.get('q_relative_spread'),(int,float))]
    rotd=[r.get('finest_relative_discrepancy') for r in by['D'] if isinstance(r.get('finest_relative_discrepancy'),(int,float))]
    h2=A.get(2,{})
    h2rows=h2.get('rows') or []
    h2fin=h2rows[-1].get('normalized_abs_cubic') if h2rows else None

    summary={
        'gate':'ITER040-CALIBRATION-FREE-WEYL3-RESPONSE-MANIFOLD',
        'expected_lanes':TOTAL,'found_unique_lanes':len(unique),'counts':counts,'passes':passes,
        'finest_A_signs':signs,'relative_sign_pattern_ok':sign_pattern_ok,
        'H2_finest_normalized_abs_cubic':h2fin,
        'weyl_norm_amplitude_slope_range':[min(slopes_w),max(slopes_w)] if slopes_w else None,
        'weyl_cubic_amplitude_slope_range':[min(slopes_c),max(slopes_c)] if slopes_c else None,
        'shape_q_relative_spread_by_h':sorted([(r.get('h'),r.get('q_relative_spread')) for r in by['C']],reverse=True),
        'maximum_finest_rotation_discrepancy':max(rotd) if rotd else None,
        'classification':cls,
        'prediction_contract':{
            'relative_nonzero_tidal_cubic_shape_ratio':'H0:H1:H3 = 1:3:-1 up to one common c6/convention factor',
            'cubic_null_profile':'H2 has nonzero Weyl curvature but vanishing leading cubic tidal invariant',
            'amplitude_law':'Weyl norm ~ kappa; Weyl^3 response ~ kappa^3 in the frozen weak-field family',
            'absolute_amplitude':'requires c6 matching; not predicted numerically by current authority',
            'beta_role':'does not enter pure Weyl^3 response-kernel ratios'
        },
        'claim_lock':'Scoped same-field-content weak tidal response manifold only. c6 and beta remain unfixed/calibrated as classified by Iter039; response ratios are not absolute quantum phases.'
    }
    os.makedirs('iter040-summary',exist_ok=True)
    with open('iter040-summary/summary.json','w',encoding='utf-8') as f:
        json.dump(summary,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(summary,sort_keys=True))
    if not complete: sys.exit(2)

if __name__=='__main__': main()
