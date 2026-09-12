#!/usr/bin/env python3
import glob,json,numpy as np
rows=[json.load(open(f)) for f in glob.glob('iter011-g1b-results/*/result.json')]
rows=sorted(rows,key=lambda r:r['h'],reverse=True)
assert len(rows)==3,rows
hs=np.array([r['h'] for r in rows]); ev=np.array([abs(r['even']) for r in rows]); od=np.array([abs(r['odd']) for r in rows])
se=float(np.polyfit(np.log(hs),np.log(ev),1)[0])
so=float(np.polyfit(np.log(hs),np.log(od),1)[0])
rat=np.array([r['odd_over_even_abs'] for r in rows])
sr=float(np.polyfit(np.log(hs),np.log(rat),1)[0])
# Odd contamination that decays parametrically faster than the even sector is
# evidence against a continuum parity-odd/Weyl^3 measure contribution.
decision='ODD_COMPONENT_DECAYS_FASTER_THAN_EVEN__CONSISTENT_WITH_DISCRETIZATION_TAIL' if so>se+0.5 else 'ODD_COMPONENT_NOT_YET_SEPARATED_FROM_CONTINUUM_SCALING'
out={'gate':'ITER011-G1B-PARITY-REFINEMENT-AGGREGATE','rows':rows,'even_h_slope':se,'odd_h_slope':so,'odd_over_even_h_slope':sr,'decision':decision,'c6_fixed':False,'guard':'This concerns the real torsion-Jacobian measure sector only; it cannot by itself define the coherent Lorentzian Weyl^3 action coefficient.'}
open('iter011-g1b-summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,sort_keys=True))
