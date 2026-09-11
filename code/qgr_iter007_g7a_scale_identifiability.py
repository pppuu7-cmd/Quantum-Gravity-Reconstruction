#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# log a = const + log kappa - 2 log h
J=[1.0,-2.0]
rank=1 if any(abs(x)>0.0 for x in J) else 0
assert rank==1
# Null direction preserving a: d log kappa = 2 d log h.
v=[2.0,1.0]
null_residual=J[0]*v[0]+J[1]*v[1]
assert abs(null_residual)<1e-14
# A history observable with leading h^4 changes along the continuum-normalization null direction.
dlog_hist=0.0*v[0]+4.0*v[1]
assert abs(dlog_hist-4.0)<1e-14
out={
 'lane':'KAPPA_H_IDENTIFIABILITY',
 'parameter_coordinates':['log_kappa','log_h'],
 'continuum_normalization_jacobian':[J],
 'jacobian_rank':rank,
 'unidentified_null_direction':v,
 'null_direction_residual':null_residual,
 'history_h4_log_derivative_along_null_direction':dlog_hist,
 'classification':'BLOCKED_SCOPED_CONTINUUM_GR_NORMALIZATION_ALONE_CANNOT_IDENTIFY_KAPPA_AND_H_SEPARATELY',
 'scientific_interpretation':'Even if the geometric matching constant is known exactly, one observed continuum normalization a supplies one constraint on two microscopic quantities kappa and h. The one-parameter transformation h->lambda h, kappa->lambda^2 kappa leaves a fixed but changes an h^4 history observable by lambda^4. Therefore the absolute QGR correction cannot be predicted from the GR normalization alone.',
 'guard':'This is an identifiability obstruction, not evidence that h is arbitrary in a future completed microscopic theory. A new derived normalization principle or a second independent observable could lift the degeneracy.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))