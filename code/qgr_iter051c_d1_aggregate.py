#!/usr/bin/env python3
import glob, json, os, sys
import numpy as np

files=sorted(glob.glob('artifacts/**/lane-*.json',recursive=True))
rows=[]; parse_errors=[]
for path in files:
    try:
        with open(path,'r',encoding='utf-8-sig') as f: rows.append(json.load(f))
    except Exception as exc:
        parse_errors.append({'path':path,'error':repr(exc)})

expected=6
unique=len({r.get('lane') for r in rows})
valid=[r for r in rows if r.get('valid') is True]
complete=(len(rows)==expected and unique==expected and not parse_errors)
summary={
  'gate':'ITER051C-D1-ASSEMBLY-TERM-LOCALIZATION',
  'expected_lanes':expected,'artifact_rows':len(rows),'unique_lanes':unique,
  'valid_count':len(valid),'parse_errors':parse_errors,
  'interpretation_lock':'DIAGNOSTIC_ONLY_NOT_REPLACEMENT_EOM_AUTHORITY',
  'c6_status':'SYMBOLIC_UNFIXED'
}

if complete and len(valid)==expected:
    rows=sorted(rows,key=lambda r:r['lane'])
    blocks=[]; targets=[]
    for r in rows:
        a=np.array(r['a_reduced'],float); i=np.array(r['i_reduced'],float); j=np.array(r['j_reduced'],float)
        blocks.append(np.column_stack([a,i,j])); targets.append(np.array(r['exact_target'],float))
    M=np.vstack(blocks); y=np.concatenate(targets)
    coeff,resid,rank,svals=np.linalg.lstsq(M,y,rcond=None)
    fit=M@coeff
    fitrel=float(np.linalg.norm(fit-y)/max(np.linalg.norm(y),1e-14))
    cond=float(np.linalg.cond(M))
    loos=[]
    for lane in range(expected):
        keep=[k for k in range(expected) if k!=lane]
        Mk=np.vstack([blocks[k] for k in keep]); yk=np.concatenate([targets[k] for k in keep])
        ck=np.linalg.lstsq(Mk,yk,rcond=None)[0]
        loos.append(ck)
    loo_spread=max(float(np.linalg.norm(x-coeff)/max(np.linalg.norm(coeff),1e-14)) for x in loos)
    hypotheses={'H0_historical':[1.,1.,2.],'H1_flip_D':[1.,1.,-2.],'H2_flip_I':[1.,-1.,2.],'H3_flip_I_D':[1.,-1.,-2.],'H4_global_sign':[-1.,-1.,-2.]}
    hres={name:float(np.linalg.norm(M@np.array(v)-y)/max(np.linalg.norm(y),1e-14)) for name,v in hypotheses.items()}
    max_steps={k:max(float(r['final_step_changes'][k]) for r in rows) for k in ('a','i','j')}
    localized=(rank==3 and cond<=1e6 and fitrel<=1e-5 and loo_spread<=5e-4)
    classification='DIAGNOSTIC_LOCALIZED_STABLE_G51C_ASSEMBLY_COEFFICIENT_PATTERN' if localized else 'DIAGNOSTIC_INCONCLUSIVE_G51C_ASSEMBLY_TERM_LOCALIZATION'
    summary.update({
      'classification':classification,'matrix_rank':int(rank),'condition_number':cond,
      'least_squares_coefficients_A_I_J':coeff.tolist(),'global_fit_relative_residual':fitrel,
      'leave_one_lane_out_coefficients':[x.tolist() for x in loos],
      'leave_one_lane_out_max_relative_spread':loo_spread,
      'reference_hypothesis_relative_residuals':hres,'max_final_step_changes':max_steps,
      'singular_values':svals.tolist()
    })
else:
    summary['classification']='CONTROL_INVALID_G51C_D1'

os.makedirs('iter051c-d1-summary',exist_ok=True)
with open('iter051c-d1-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,indent=2,sort_keys=True)
print(json.dumps(summary,sort_keys=True))
if summary['classification']=='CONTROL_INVALID_G51C_D1': sys.exit(2)
