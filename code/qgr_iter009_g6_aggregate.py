#!/usr/bin/env python3
import glob,json,os

files=sorted(glob.glob('iter009-g6-results/**/result.json',recursive=True))
assert len(files)==6,(len(files),files)
rows=[]
for f in files:
    with open(f) as fh: d=json.load(fh)
    rows.append({'file':f,'gate':d.get('gate'),'classification':d.get('classification')})
classes=[r['classification'] for r in rows]
assert sum(c.startswith('PASS_SCOPED') for c in classes)==5,classes
assert sum(c.startswith('BLOCKED_SCOPED_C6_') for c in classes)==1,classes
required={
 'ITER009-G6-TORSION-JACOBIAN-EXACT',
 'ITER009-G6-L2-STRONG-CONTINUITY',
 'ITER009-G6-DENSE-DOMAIN-EXTENSION',
 'ITER009-G6-TRACE-CLASS-CHANNEL-LIMIT',
 'ITER009-G6-SERIAL-ACCUMULATION',
 'ITER009-G6-C6-IDENTIFIABILITY-DECISION',
}
assert {r['gate'] for r in rows}==required,{r['gate'] for r in rows}
out={
 'iteration':'009-G6',
 'parallel_lanes':6,
 'aggregate_success':True,
 'lane_results':rows,
 'key_results':[
   'The repaired torsion equations have exact 24/24 rational Jacobian rank at the flat seed, giving a unique local analytic microscopic connection branch by the implicit-function theorem.',
   'The established one-particle characteristic Lorentz representation is strongly continuous on its full physical L2 Hilbert space, first on a dense C_c domain and then by unitary extension.',
   'Strong branch convergence and strong adjoint convergence imply trace-norm convergence of the finite 24-history channel for every normal one-particle state.',
   'At fixed macroscopic interval T with N~T/h cells, a uniform regular O(h^2) per-cell relative branch generator accumulates at worst as O(T h), while regular c6 O(h^4) terms accumulate as O(c6 T h^3).',
   'The current QGR authority still does not identify c6 for absolute curved coherent observables; this is a genuine UV-matching blocker and must not be fitted post hoc.'
 ],
 'classification':'PASS_SCOPED_ONE_PARTICLE_STRONG_AND_NORMAL_STATE_TRACE_CLASS_REFINEMENT_LIMIT_ESTABLISHED_IN_THE_REGULAR_WEAK_CURVATURE_BRANCH__C6_ABSOLUTE_CURVED_UV_MATCHING_REMAINS_BLOCKED',
 'iteration_decision':'ITER009_CAN_CLOSE_100_PERCENT_WITH_C6_EXPLICITLY_HANDED_FORWARD_AS_A_BLOCKER_RATHER_THAN_SILENTLY_FIXED',
 'recommended_next_gate':'ITER010_G1_EXACT_FINITE_CELL_UV_ACTION_OR_EQUIVALENT_MICROSCOPIC_C6_MATCHING',
 'claim_lock':'Do not promote the one-particle strong/trace-class result to a full interacting nonperturbative Hilbert-space completion, and do not call c6 derived.'
}
with open('iter009-g6-summary.json','w') as fh: json.dump(out,fh,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
