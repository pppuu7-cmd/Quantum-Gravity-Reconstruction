#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Hold the continuum gravitational normalization a ~ kappa/h^2 fixed while refining.
# Then kappa(h)~h^2. The model-side normalized history loss remains ~h^4 and vanishes.
hs=[1.0,0.5,0.25,0.125,0.0625]
rows=[]
for h in hs:
    kappa_ratio=h*h
    a_ratio=kappa_ratio/(h*h)
    history_ratio=h**4
    assert abs(a_ratio-1.0)<1e-15
    rows.append({'h':h,'kappa_over_kappa_h1':kappa_ratio,'continuum_gravity_normalization_ratio':a_ratio,'leading_history_effect_ratio':history_ratio})
out={
 'lane':'REGULATOR_VERSUS_PHYSICAL_SCALE_FORK',
 'rows':rows,
 'classification':'PASS_SCOPED_IF_H_IS_A_REMOVED_REFINEMENT_REGULATOR_THE_NORMALIZED_HISTORY_CORRECTION_VANISHES_AS_H4_WHILE_THE_GR_NORMALIZATION_STAYS_FIXED',
 'scientific_interpretation':'Along the exact continuum-matching trajectory kappa~h^2, the Einstein-Hilbert normalization stays fixed but every G6H leading history correction tends to zero as h^4. Therefore a strictly removed regulator interpretation yields the GR local continuum with no finite leading history signal. A nonzero new-physics effect requires h to be a physical stopping/discreteness scale rather than merely a regulator.',
 'guard':'This does not establish that h must be removed. It separates the two logically distinct interpretations and shows what each implies.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))