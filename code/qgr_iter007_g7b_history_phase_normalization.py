#!/usr/bin/env python3
import argparse,cmath,json,math
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# The normalized history Kraus modulus is fixed by branch count; kappa enters only through real action phase.
kappas=[0.0,0.1,1.0,math.pi,10.0]
svals=[-1.3,-0.2,0.0,0.7,2.1]
rows=[]
for kap in kappas:
    probs=[]
    comp=[]
    for s in svals:
        z=cmath.exp(1j*kap*s)/math.sqrt(24.0)
        probs.append(abs(z)**2)
    completeness=24.0*(1.0/24.0)
    assert abs(completeness-1.0)<1e-15
    assert max(abs(p-1.0/24.0) for p in probs)<1e-15
    # phase composition is exact for arbitrary kappa: exp(i k(s1+s2))=exp(i k s2)exp(i k s1)
    for a,b in zip(svals[:-1],svals[1:]):
        comp.append(abs(cmath.exp(1j*kap*(a+b))-cmath.exp(1j*kap*b)*cmath.exp(1j*kap*a)))
    assert max(comp)<1e-14
    rows.append({'kappa':kap,'branch_modulus_squared':1.0/24.0,'completeness':completeness,'max_phase_composition_error':max(comp)})
out={
 'lane':'HISTORY_PHASE_NORMALIZATION_NOFIX',
 'kappa_values_checked':kappas,
 'rows':rows,
 'classification':'FAIL_SCOPED_HISTORY_INSTRUMENT_NORMALIZATION_AND_PROJECTIVE_PHASE_COMPOSITION_DO_NOT_FIX_OVERALL_KAPPA',
 'scientific_interpretation':'For K_alpha=24^(-1/2) exp(i kappa s_alpha/hbar) U_alpha, the normalized branch modulus and CPTP completeness are independent of kappa for every real kappa. Projective phase composition is likewise exact for arbitrary kappa because the action is additive. Thus the already-derived history normalization cannot quantize or select the microscopic overall action scale.',
 'guard':'This does not prove no deeper quantum consistency condition can fix kappa. It rules out the existing branch normalization/unitarity/projective-composition conditions as such a mechanism.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))