#!/usr/bin/env python3
from pathlib import Path
import json
rows=[json.loads(p.read_text()) for p in sorted(Path('iter007-g6c-results').rglob('result.json'))]
by={r['lane']:r for r in rows}
required={'LOCAL_NET_FIBER_PRODUCT','BOUNDARY_RELATIVE_TENSOR_GLUE','PHYSICAL_QUOTIENT_DESCENT','CYLINDRICAL_ALGEBRA_INTERSECTION'}
assert set(by)==required,(set(by),required)
assert by['LOCAL_NET_FIBER_PRODUCT']['region_counts']['union']['regular_configuration_dim']==552
assert by['BOUNDARY_RELATIVE_TENSOR_GLUE']['boundary_matched_relative_tensor_dimension_AxB']==48
assert by['PHYSICAL_QUOTIENT_DESCENT']['physical_quotient_dimension']==2
assert by['CYLINDRICAL_ALGEBRA_INTERSECTION']['linear_coordinate_dimensions']['intersection']==152
summary={
 'iteration':'007-G6C',
 'parallel_lanes':len(rows),
 'lane_classifications':{k:v['classification'] for k,v in sorted(by.items())},
 'key_results':[
  'On the regular finite path-groupoid configuration domain, two face-neighbour B4 regions glue exactly as a fiber product over their shared B3 data; the dimension identity is 352+352-152=552.',
  'The quantum boundary-matching analogue is a relative/fiberwise tensor structure over one shared boundary label, not an unconstrained tensor product with two independent copies of the B3 boundary.',
  'The cylindrical multiplication-observable net is isotonic and has exact overlap intersection equal to the shared-B3 cylindrical algebra in the finite regular coordinate model.',
  'The already-derived Sym2 frame pullback maps QGR-L1 gauge directions to gauge directions and characteristic Hessian nullspaces to nullspaces, so it canonically descends to an isomorphism of the two-dimensional physical quotients without inserting a free 2x2 projector.'
 ],
 'closed_in_scope':[
  'regular finite configuration-space local-net gluing by boundary fiber product',
  'cylindrical multiplication-algebra isotony and B3 intersection',
  'algebraic boundary-matching reason naive Hilbert tensor factorization is wrong for overlapping regions',
  'canonical two-mode quotient descent under finite regular frame pullbacks'
 ],
 'still_open':[
  'analytic disintegration of the full interacting QGR measure into a boundary-relative direct integral',
  'full constrained/gauge-invariant operator-algebra net including derivations and boundary charges',
  'common-target wavepacket/bundle readout for multiple curved history branches whose transported characteristic covectors can differ',
  'normalized local two-mode purity prediction on the G9 curved background',
  'independent microscopic fixation of the absolute h/kappa scale for phenomenology',
  'independent KMQGB pass'
 ],
 'active_blocker':'BLOCKED_MISSING_COMMON_TARGET_CURVED_WAVEPACKET_READOUT_AND_INTERACTING_BOUNDARY_MEASURE_DISINTEGRATION',
 'recommended_next_gate':'G6D_CURVED_WAVEPACKET_QUOTIENT_READOUT_AND_LOCAL_PURITY',
 'claim_lock':'Do not replace relative boundary gluing by a naive tensor product, do not choose a branch-dependent polarization basis as a physical observable, and do not identify the classical h^4 holonomy trace spread with quantum purity loss.'
}
Path('iter007-g6c-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,sort_keys=True))
