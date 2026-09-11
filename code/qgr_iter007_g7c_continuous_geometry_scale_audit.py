#!/usr/bin/env python3
import argparse,json,math
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Q_13 is the open set of nondegenerate symmetric Lorentzian forms. Positive rescaling preserves signature.
# The invariant measure is also exactly unchanged under G->s^2G.
scales=[10.0**p for p in [-6,-3,-1,0,1,3,6]]
rows=[]
for s in scales:
    measure_ratio=(s**20)*(s**8)**(-2.5)
    assert math.isclose(measure_ratio,1.0,rel_tol=1e-12,abs_tol=1e-12)
    rows.append({'s':s,'signature_preserved_for_positive_rescaling':True,'measure_ratio':measure_ratio})
out={
 'lane':'CONTINUOUS_GEOMETRY_SCALE_AUDIT',
 'configuration_space':'Q_13 = nondegenerate symmetric 4x4 forms of fixed Lorentzian signature',
 'positive_rescaling_orbit':'G -> s^2 G for arbitrary s>0 remains in Q_13',
 'rows':rows,
 'classification':'BLOCKED_SCOPED_CURRENT_CONTINUOUS_QGR_CONFIGURATION_SPACE_AND_INVARIANT_MEASURE_CONTAIN_NO_DERIVED_MINIMUM_NONZERO_GEOMETRIC_SCALE',
 'scientific_interpretation':'The current kinematic geometry is continuous: every regular Lorentzian response lies on an arbitrary positive rescaling orbit, and the existing measure is exactly neutral along that orbit. No area/length gap or smallest nonzero response value has been derived. Consequently the finite cell spacing h cannot presently be identified with a spectrum gap of the QGR geometry.',
 'guard':'This is about the current representation. A future discrete spectrum, compact variable, quantum constraint, or microscopic counting theorem could change the conclusion.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))