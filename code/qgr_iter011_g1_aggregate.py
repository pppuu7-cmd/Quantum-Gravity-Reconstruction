#!/usr/bin/env python3
import glob,json,math
files=glob.glob('iter011-g1-results/*/result.json')
recs={}
for f in files:
    d=json.load(open(f))
    recs[d['gate']]=d
required={
 'ITER011-G1-JACOBIAN-REFINEMENT-SCALING',
 'ITER011-G1-JACOBIAN-AMPLITUDE-PARITY',
 'ITER011-G1-LOCAL-JACOBIAN-COMPOSITION-DIAGNOSTIC',
}
assert required<=set(recs),(required,set(recs))
ref=recs['ITER011-G1-JACOBIAN-REFINEMENT-SCALING']
par=recs['ITER011-G1-JACOBIAN-AMPLITUDE-PARITY']
comp=recs['ITER011-G1-LOCAL-JACOBIAN-COMPOSITION-DIAGNOSTIC']
# Determine whether the Jacobian supplies an odd/cubic curvature signal, while
# preserving the crucial measure-vs-phase distinction.
c1,c2,c3=par['fit_coefficients_kappa_kappa2_kappa3']
odd_ratios=[p['odd_over_even_abs'] for p in par['parity_pairs']]
odd_material=max(odd_ratios)>1e-3
if odd_material:
    decision='JACOBIAN_HAS_ODD_TIDAL_COMPONENT_BUT_REMAINS_REAL_MEASURE_DATUM__C6_PHASE_NULL_NOT_LIFTED'
else:
    decision='JACOBIAN_DOMINANTLY_EVEN_REAL_MEASURE_CORRECTION__NO_WEYL3_PHASE_AUTHORITY__C6_PHASE_NULL_NOT_LIFTED'
out={
 'gate':'ITER011-G1-AGGREGATE',
 'lanes':sorted(recs),
 'refinement_abs_h_slope':ref['flat_subtracted_abs_h_slope'],
 'amplitude_fit_k1_k2_k3':[c1,c2,c3],
 'max_odd_over_even_abs':max(odd_ratios),
 'composition_rows':comp['rows'],
 'decision':decision,
 'c6_fixed':False,
 'scientific_guard':'The torsion/coarea Jacobian is a positive real measure factor derived from the constraint map. No canonical relation converting log|det dT/domega| into the coherent Lorentzian action phase has been derived. Therefore this audit cannot numerically assign c6 even if curvature-cubic dependence is visible.',
 'next_gate':'Derive the correct glued Haar/coarea measure on shared connection variables and separately search for a nonhomogeneous microscopic coherent phase/action datum; do not identify measure log-weight with iS/hbar.'
}
open('iter011-g1-summary.json','w').write(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,sort_keys=True))
