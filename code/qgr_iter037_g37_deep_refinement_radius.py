#!/usr/bin/env python3
"""QGR Iter037 G37: two independent branch-persistence stress streams.

Stream A (deep): six G36 jointly-persistent witnesses at h = 0.25, 0.18, 0.12, 0.08;
checks 15-cell extension, invariant separation and origin torsion-Jacobian conditioning.

Stream B (radius): the same witnesses at h=0.5 on positive-orthant simplex patches R=3,4;
every multi-parent cell is independently continued from every available immediate parent and
must agree numerically before a representative can seed the next shell.

All conclusions are scoped finite numerical statements. The h deformation is not the full QGR
projective refinement map, and finite radius is not a global compactness theorem.
"""
import argparse, itertools, json, math, os
import numpy as np
import qgr_iter036_g36_expanded_patch_persistence as g36

JOINT_SEED_INDICES=[0,1,3,4,5,7]
H_TARGETS=[0.25,0.18,0.12,0.08]
RADII=[3,4]
ORIGIN=np.zeros(4,dtype=int)


def safe(v):
    try:
        x=float(v)
        return x if math.isfinite(x) else None
    except Exception:
        return None


def jac_stats(sys,z):
    try:
        sol=sys.solve(ORIGIN,np.asarray(z),max_nfev=2)
        if sol is None: return None
        sv=np.linalg.svd(sol.jac,compute_uv=False)
        mn=float(sv.min()); mx=float(sv.max())
        return {'min_singular':safe(mn),'max_singular':safe(mx),
                'condition':safe(mx/mn) if mn>0 else None}
    except Exception:
        return None


def fp_distance(a,b):
    return max(abs(a[i][j]-b[i][j]) for i in range(len(a)) for j in range(len(a[i])))


def continue_to_h(z0,h1,steps=12):
    return g36.continue_origin(z0,1.0,1.0,1.0,float(h1),steps=steps)


def deep_lane(g36_seed_index,target_h):
    ref0,cand0,base=g36.reconstruct_baseline(g36_seed_index)
    result={'gate':'ITER037-G37','stream':'deep','g36_seed_index':g36_seed_index,
            'target_h':float(target_h),**base,
            'claim_lock':'Finite-h shrinking-cell proxy only; not a projective-limit theorem.'}
    if ref0 is None or cand0 is None or not base.get('baseline_ok'):
        result.update({'reference_controls_valid':False,'lane_pass':False,
                       'classification':'BASELINE_RECONSTRUCTION_FAILED'})
        return result
    ref,ref_cont=continue_to_h(ref0,target_h)
    cand,cand_cont=continue_to_h(cand0,target_h)
    result['reference_continuation']=ref_cont
    result['candidate_continuation']=cand_cont
    if ref is None or cand is None:
        result.update({'reference_controls_valid':ref is not None,'lane_pass':False,
                       'classification':'TARGET_CONTINUATION_FAILED'})
        return result
    sys=g36.System(1.0,target_h)
    ref_rn=float(np.linalg.norm(sys.residual(ORIGIN,ref)))
    cand_rn=float(np.linalg.norm(sys.residual(ORIGIN,cand)))
    ref_me=max(g36.metric_errors(ref)); cand_me=max(g36.metric_errors(cand))
    ref_patch,ref_rows=g36.expanded_patch(sys,ref)
    cand_patch,cand_rows=g36.expanded_patch(sys,cand)
    ref_patch_ok=bool(len(ref_patch)==15 and all(r['success'] for r in ref_rows))
    cand_patch_ok=bool(len(cand_patch)==15 and all(r['success'] for r in cand_rows))
    ref_hol=g36.expanded_holonomy(ref_patch) if ref_patch_ok else []
    cand_hol=g36.expanded_holonomy(cand_patch) if cand_patch_ok else []
    hid=g36.holonomy_distance(cand_hol,ref_hol) if ref_patch_ok and cand_patch_ok else None
    ref_fp=g36.edge_fingerprint(g36.edge_A(sys,ORIGIN,ref))
    cand_fp=g36.edge_fingerprint(g36.edge_A(sys,ORIGIN,cand))
    fpd=fp_distance(cand_fp,ref_fp)
    js_ref=jac_stats(sys,ref); js_cand=jac_stats(sys,cand)
    zdist=float(np.linalg.norm(cand-ref))
    controls=bool(ref_rn<1e-9 and ref_me<1e-7 and ref_patch_ok and len(ref_hol)==30 and
                  js_ref and js_ref.get('min_singular') is not None and js_ref['min_singular']>1e-8)
    resolved=bool((hid is not None and hid>1e-9) or fpd>1e-9)
    passed=bool(controls and cand_rn<1e-9 and cand_me<1e-7 and cand_patch_ok and len(cand_hol)==30 and
                resolved and js_cand and js_cand.get('min_singular') is not None and js_cand['min_singular']>1e-8)
    result.update({
        'reference_origin_residual':safe(ref_rn),'candidate_origin_residual':safe(cand_rn),
        'reference_max_metric_error':safe(ref_me),'candidate_max_metric_error':safe(cand_me),
        'reference_patch_valid':ref_patch_ok,'candidate_patch_valid':cand_patch_ok,
        'reference_holonomy_count':len(ref_hol),'candidate_holonomy_count':len(cand_hol),
        'expanded_holonomy_invariant_distance':safe(hid) if hid is not None else None,
        'edge_fingerprint_distance':safe(fpd),'invariant_distinction_resolved':resolved,
        'reference_jacobian':js_ref,'candidate_jacobian':js_cand,
        'coordinate_root_distance':safe(zdist),'coordinate_root_distance_over_h':safe(zdist/target_h),
        'reference_controls_valid':controls,'lane_pass':passed,
        'classification':'DEEP_REFINEMENT_RESOLVED_DISTINCT_PATCH' if passed else
                         'DEEP_REFINEMENT_LANE_NOT_PROMOTED'
    })
    return result


def cells_by_shell(R):
    shells={s:[] for s in range(R+1)}
    for x in itertools.product(range(R+1),repeat=4):
        s=sum(x)
        if s<=R: shells[s].append(tuple(int(v) for v in x))
    for s in shells: shells[s].sort()
    return shells


def max_root_transport_disagreement(zs):
    if len(zs)<2: return 0.0
    lsets=[g36.Ls(z) for z in zs]
    mx=0.0
    for a,b in itertools.combinations(lsets,2):
        for La,Lb in zip(a,b): mx=max(mx,float(np.linalg.norm(La-Lb)))
    return mx


def extend_radius(sys,origin_z,R):
    shells=cells_by_shell(R)
    roots={(0,0,0,0):np.asarray(origin_z).copy()}
    cell_rows=[]; failures=[]; max_parent_disagreement=0.0
    for s in range(1,R+1):
        for x in shells[s]:
            parents=[]
            for i in range(4):
                if x[i]>0:
                    p=list(x); p[i]-=1; p=tuple(p)
                    if p in roots: parents.append(p)
            parents.sort()
            derived=[]
            for p in parents:
                z,rn=g36.best_cell(sys,np.asarray(x,dtype=int),[roots[p]],3000)
                me=max(g36.metric_errors(z)) if z is not None else float('inf')
                ok=bool(z is not None and rn<1e-8 and me<1e-7)
                derived.append({'parent':p,'z':z,'rn':rn,'me':me,'ok':ok})
            all_parent_ok=bool(parents and len(derived)==len(parents) and all(d['ok'] for d in derived))
            disagreement=max_root_transport_disagreement([d['z'] for d in derived if d['ok']]) if all_parent_ok else float('inf')
            if math.isfinite(disagreement): max_parent_disagreement=max(max_parent_disagreement,disagreement)
            consistent=bool(all_parent_ok and disagreement<1e-5)
            row={'cell':list(x),'shell':s,'parent_count':len(parents),'all_parent_continuations_valid':all_parent_ok,
                 'max_parent_transport_disagreement':safe(disagreement),'path_consistent':consistent,
                 'parent_residuals':[safe(d['rn']) for d in derived],
                 'parent_metric_errors':[safe(d['me']) for d in derived]}
            cell_rows.append(row)
            if not consistent:
                failures.append(row)
                continue
            best=sorted(derived,key=lambda d:(float(d['rn']),d['parent']))[0]
            roots[x]=best['z']
    expected=math.comb(R+4,4)
    return roots,cell_rows,failures,expected,max_parent_disagreement


def patch_holonomy(roots):
    e=[np.eye(4,dtype=int)[i] for i in range(4)]
    lm={x:g36.Ls(z) for x,z in roots.items()}
    out=[]
    for bt in sorted(lm):
        b=np.asarray(bt,dtype=int)
        for i in range(4):
            for j in range(i+1,4):
                xi=tuple(b+e[i]); xj=tuple(b+e[j])
                if xi not in lm or xj not in lm: continue
                P1=lm[xi][j]@lm[bt][i]
                P2=lm[xj][i]@lm[bt][j]
                try: H=np.linalg.inv(P2)@P1
                except Exception: continue
                out.append({'base':list(bt),'plane':[i,j],
                            'trace':float(np.trace(H)),'trace2':float(np.trace(H@H)),
                            'det':float(np.linalg.det(H))})
    return out


def radius_lane(g36_seed_index,R):
    ref0,cand0,base=g36.reconstruct_baseline(g36_seed_index)
    result={'gate':'ITER037-G37','stream':'radius','g36_seed_index':g36_seed_index,'radius':int(R),**base,
            'target_h':0.5,'claim_lock':'Finite positive-orthant radius patch only; not global compactness.'}
    if ref0 is None or cand0 is None or not base.get('baseline_ok'):
        result.update({'reference_controls_valid':False,'lane_pass':False,'classification':'BASELINE_RECONSTRUCTION_FAILED'})
        return result
    ref,ref_cont=continue_to_h(ref0,0.5,steps=8)
    cand,cand_cont=continue_to_h(cand0,0.5,steps=8)
    result['reference_continuation']=ref_cont; result['candidate_continuation']=cand_cont
    if ref is None or cand is None:
        result.update({'reference_controls_valid':ref is not None,'lane_pass':False,'classification':'TARGET_CONTINUATION_FAILED'})
        return result
    sys=g36.System(1.0,0.5)
    ref_roots,ref_rows,ref_fail,expected,ref_dis=extend_radius(sys,ref,R)
    cand_roots,cand_rows,cand_fail,expected2,cand_dis=extend_radius(sys,cand,R)
    assert expected==expected2
    ref_ok=bool(len(ref_roots)==expected and not ref_fail)
    cand_ok=bool(len(cand_roots)==expected and not cand_fail)
    ref_hol=patch_holonomy(ref_roots) if ref_ok else []
    cand_hol=patch_holonomy(cand_roots) if cand_ok else []
    hid=g36.holonomy_distance(cand_hol,ref_hol) if ref_ok and cand_ok else None
    ref_fp=g36.edge_fingerprint(g36.edge_A(sys,ORIGIN,ref)); cand_fp=g36.edge_fingerprint(g36.edge_A(sys,ORIGIN,cand))
    fpd=fp_distance(cand_fp,ref_fp)
    controls=bool(ref_ok and len(ref_hol)>0)
    passed=bool(controls and cand_ok and hid is not None and hid>1e-8 and fpd>1e-9)
    result.update({
        'expected_cells':expected,'reference_cells':len(ref_roots),'candidate_cells':len(cand_roots),
        'reference_patch_path_consistent':ref_ok,'candidate_patch_path_consistent':cand_ok,
        'reference_failure_count':len(ref_fail),'candidate_failure_count':len(cand_fail),
        'reference_max_parent_transport_disagreement':safe(ref_dis),
        'candidate_max_parent_transport_disagreement':safe(cand_dis),
        'reference_holonomy_count':len(ref_hol),'candidate_holonomy_count':len(cand_hol),
        'patch_holonomy_invariant_distance':safe(hid) if hid is not None else None,
        'origin_edge_fingerprint_distance':safe(fpd),
        'reference_controls_valid':controls,'lane_pass':passed,
        'reference_failures':ref_fail[:12],'candidate_failures':cand_fail[:12],
        'classification':'LARGE_RADIUS_PATH_CONSISTENT_DISTINCT_BRANCH' if passed else
                         'LARGE_RADIUS_LANE_NOT_PROMOTED'
    })
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',choices=['deep','radius'],required=True)
    ap.add_argument('--seed-slot',type=int,required=True)
    ap.add_argument('--target-index',type=int,required=True)
    ap.add_argument('--out',required=True)
    q=ap.parse_args()
    assert 0<=q.seed_slot<len(JOINT_SEED_INDICES)
    g36_seed=JOINT_SEED_INDICES[q.seed_slot]
    if q.stream=='deep':
        assert 0<=q.target_index<len(H_TARGETS)
        result=deep_lane(g36_seed,H_TARGETS[q.target_index])
    else:
        assert 0<=q.target_index<len(RADII)
        result=radius_lane(g36_seed,RADII[q.target_index])
    result['seed_slot']=q.seed_slot; result['target_index']=q.target_index
    os.makedirs(os.path.dirname(q.out),exist_ok=True)
    with open(q.out,'w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True,allow_nan=False); f.write('\n')
    compact={k:v for k,v in result.items() if k not in ('reference_continuation','candidate_continuation',
             'reference_failures','candidate_failures')}
    print(json.dumps(compact,sort_keys=True,allow_nan=False))

if __name__=='__main__':
    main()
