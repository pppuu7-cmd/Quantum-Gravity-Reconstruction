#!/usr/bin/env python3
import glob,json,os,sys
files=sorted(glob.glob('iter022-g22-results/qgr-g22-*/*.json'))
rows=[]
for p in files:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
expected={'reparam-invariance':6,'authority-rank':6,'beta-invariant-ratios':6,'preparation-vs-calibration':6}
ok=(len(rows)==24 and counts==expected and all(r.get('passed') for r in rows))
out={
 'gate':'ITER022-G22-AGGREGATE','scope':'CONDITIONAL_ON_G21_SINGLE_SCALAR_EVENT_RESPONSE_MAP',
 'lane_count':len(rows),'audit_counts':counts,'all_lane_gates_passed':ok,
 'scientific_status':'PARTIAL_SCOPED_CONDITIONAL_ON_A_SINGLE_EVENT_RESPONSE_SCALE_BETA__BOOLEAN_COUNT_SPACE_QUADRATIC_PAIR_AND_TRIPLE_AMPLITUDE_DATA_HAVE_ONE_EXACT_EVENT_UNIT_REPARAMETRIZATION_NULL_DIRECTION__BETA_INVARIANT_CUBIC_TO_QUADRATIC_RATIOS_EXIST__BETA_MUST_BE_DISTINGUISHED_AS_UNIVERSAL_CALIBRATION_VERSUS_PHYSICAL_BOUNDARY_PREPARATION_DATA',
 'strongest_positive':'Including beta does not create an uncontrolled new multi-parameter sector. The quadratic and cubic count-space authority has exactly one normalization null direction, and exact beta-invariant cubic/quadratic ratios can be formed. Therefore absolute event-unit calibration is not required to formulate all microscopic shape information.',
 'strongest_blocker':'QGR still does not supply the values of the beta-invariant finite pair/triple microscopic ratios from the same realization. In addition, a physically changed boundary amplitude at fixed theory coefficients is preparation data, while a universal event-unit change is only calibration; these roles must not be conflated.',
 'c6_relation':'This gate does not fix c6. Iter010 already requires one derived absolutely normalized Weyl-active curved microscopic action/phase target. A beta field/event-unit convention cannot substitute for that nonhomogeneous UV datum.',
 'decision':'DO_NOT_TRY_TO_FIX_A_UNIVERSAL_BETA_BY_SYMMETRY_OR_HISTORY_NORMALIZATION__USE_BETA_INVARIANT_MICROSCOPIC_RATIO_AUTHORITY_FOR_LOCAL_CUBIC_SHAPE_AND_KEEP_PHYSICAL_BOUNDARY_AMPLITUDES_AS_PREPARATION_DATA__C6_REMAINS_SEPARATE_UNTIL_AN_ABSOLUTE_CURVED_UV_PHASE_TARGET_IS_DERIVED',
 'next_gate':'QGR-ITER023-G23-SAME-REALIZATION-BETA-INVARIANT-PAIR-TRIPLE-CUMULANT-RATIO-FROM-BOOLEAN-EVENT-MEASURE',
 'beta_absolute_fixed':False,'beta_reparam_nullity':1,'c6_fixed':False,
 'claim_locks':['conditional on G21 proving a single beta map','beta absolute physical value derived = NO','finite pair/triple invariant ratios derived from QGR microphysics = NO','c6 fixed = NO','do not use beta=1 as a physical derivation','do not use preparation data as theory coupling authority']
}
os.makedirs('iter022-g22-summary',exist_ok=True)
with open('iter022-g22-summary/summary.json','w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps(out,sort_keys=True))
if not ok: sys.exit(2)
