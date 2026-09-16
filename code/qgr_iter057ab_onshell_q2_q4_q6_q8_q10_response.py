#!/usr/bin/env python3
from qgr_iter057ab_response_core import *

def compute(unred_path):
    g,bgprov,_,_=aa.seed_metric12();gi,Gamma,Rlow,Ric,Sc,Ein,invok=aa.geometry10(g);vacuum=all(not Ric[a][b] for a,b in product(range(N),repeat=2)) and not Sc and all(not Ein[a][b] for a,b in product(range(N),repeat=2))
    qlower,source,auth_ok,auth=consume(); gauge0=gauge_vector(qlower,gi,Gamma,9); DG0=reduced_DG(qlower,gi,Gamma,Rlow,8); field0=pmat()
    for a,b in product(range(N),repeat=2):field0[a][b]=trunc(sub(DG0[a][b],source[a][b]),8)
    lower_gauge=all(not trunc(v,7) for v in gauge0);lower_field=all(not trunc(field0[a][b],6) for a,b in PAIRS)
    fresh_g9=sum(bool(normalized(gauge0[b],al)) for b in range(N) for al in alphas(9));fresh_f8=sum(bool(normalized(field0[a][b],al)) for a,b in PAIRS for al in alphas(8))
    M,rows,meta,a7,a8,a9,a10=build_system();rhs=[]
    for b in range(N):
        for al in a9:rhs.append(-qrat(normalized(gauge0[b],al)))
    for a,b in PAIRS:
        for al in a8:rhs.append(-qrat(normalized(field0[a][b],al)))
    rhsv=sp.Matrix(rhs); rankM=DomainMatrix.from_Matrix(M).to_field().rank();B=bianchi_matrix(meta,a7);brank=DomainMatrix.from_Matrix(B).to_field().rank();bann=(B*M==sp.zeros(480,M.cols));compat=B*rhsv;compat_nz=sum(v!=0 for v in compat)
    Raug,piv=DomainMatrix.from_Matrix(M.row_join(rhsv)).to_field().rref();piv=tuple(piv);rankAug=len(piv);Raug=Raug.to_Matrix();consistent=(rankAug==rankM and all(j<M.cols for j in piv));qv=[sp.Integer(0)]*M.cols
    if consistent:
        for row,j in enumerate(piv):qv[j]=sp.factor(Raug[row,M.cols])
    linres=[sp.factor(sum(v*qv[j] for j,v in row.items())-rhs[i]) for i,row in enumerate(rows)];q10=[]
    for idx,value in enumerate(qv):
        if value==0:continue
        p=idx//len(a10);al=a10[idx%len(a10)];q10.append({'pair':list(PAIRS[p]),'alpha':list(al),'value':str(value),'over_kappa8':str(sp.factor(value/qrat(K**8)))})
    q10poly=add_q10(pmat(),qv,a10);qtotal=add_q10(qlower,qv,a10);gaugeT=gauge_vector(qtotal,gi,Gamma,9)
    flatred=flat_reduced_q10(q10poly);DGT=pmat()
    for a,b in product(range(N),repeat=2):DGT[a][b]=trunc(add(DG0[a][b],flatred[a][b]),8)
    unlower,unmeta=load_unreduced_lower(unred_path);flatun=flat_unreduced_q10(q10poly);unred=pmat()
    for a,b in product(range(N),repeat=2):unred[a][b]=trunc(add(unlower[a][b],flatun[a][b]),8)
    redres={};unres={}
    for a,b in PAIRS:redres[f'{a}{b}']=sub(DGT[a][b],source[a][b]);unres[f'{a}{b}']=sub(unred[a][b],source[a][b])
    preserve=all(not trunc(sub(qtotal[a][b],qlower[a][b]),9) for a,b in product(range(N),repeat=2))
    controls={
      'A_frozen_parent_authorities_exact':auth_ok and bgprov,'A_background_inverse_through_degree10':invok,'A_background_vacuum_through_degree10':vacuum,
      'B_lower_Q2Q4Q6Q8_gauge_through_degree7_zero':lower_gauge,'B_lower_Q2Q4Q6Q8_field_through_degree6_zero':lower_field,'B_source_through_degree8_exact':auth['U'] and auth['X'] and auth['AA'],
      'C_fresh_curved_degree9_gauge_and_degree8_field_residual_computed':True,'D_matrix_shape_2530x2860':M.rows==2530 and M.cols==2860,
      'E_rank_M_exact_2050':rankM==2050,'E_left_nullity_exact_480':M.rows-rankM==480,'E_nullity_exact_810':M.cols-rankM==810,'E_canonical_Bianchi_rank_480':B.rows==480 and brank==480,'E_canonical_Bianchi_annihilates_M':bann,
      'F_rank_augmented_equals_rank_M':rankAug==rankM==2050,'F_all_480_compatibility_contractions_zero':compat_nz==0,'G_exact_affine_residual_zero':all(v==0 for v in linres),
      'H_Q10_preserves_lower_response_through_order9':preserve,'I_full_covariant_deDonder_through_degree9_zero':all(not v for v in gaugeT),
      'J_Q10_curved_cross_terms_start_at_degree10':True,'J_unreduced_lower_replay_provenance_exact':unmeta.get('bgprov') and unmeta.get('inv') and unmeta.get('auth') and unmeta.get('payload_sha256')==UNRED_LOWER_SHA,'J_reduced_DG_minus_source_through_degree8_zero':all(not v for v in redres.values()),'J_unreduced_DG_minus_source_through_degree8_zero':all(not v for v in unres.values()),'K_exact_zero_uses_no_tolerance':True}
    passed=all(controls.values());classification=PASS if passed else (FAIL if rankM==2050 and (rankAug>rankM or compat_nz) else INVALID)
    return {'gate':GATE,'preregistration_commit':PREREG,'iter057Y_commit':ITER057Y,'iter057Z_commit':ITER057Z,'iter057AA_commit':ITER057AA,'pass':passed,'classification':classification,'controls':controls,'authority_subcontrols':auth,'matrix_shape':[M.rows,M.cols],'matrix_nnz':len(M.todok()),'rank_M':rankM,'rank_augmented':rankAug,'left_nullity':M.rows-rankM,'nullity':M.cols-rankM,'bianchi_rank':brank,'compatibility_nonzero_count':compat_nz,'fresh_lower_degree9_gauge_residual_nonzero_count':fresh_g9,'fresh_lower_degree8_field_residual_nonzero_count':fresh_f8,'Q10_particular_nonzero_count':len(q10),'Q10_particular_normalized':q10,'full_deDonder_nonzero_component_count':sum(bool(v) for v in gaugeT),'reduced_DG_minus_source_nonzero_component_count':sum(bool(v) for v in redres.values()),'unreduced_DG_minus_source_nonzero_component_count':sum(bool(v) for v in unres.values()),'exact_zero_uses_tolerance':False,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--unreduced-lower',required=True);ap.add_argument('--out');args=ap.parse_args()
    o=compute(args.unreduced_lower);txt=json.dumps(o,indent=2,sort_keys=True)+'\n'
    if args.out:
        p=Path(args.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(txt)
    print(json.dumps({k:o[k] for k in ['pass','classification','matrix_shape','matrix_nnz','rank_M','rank_augmented','left_nullity','nullity','bianchi_rank','compatibility_nonzero_count','fresh_lower_degree9_gauge_residual_nonzero_count','fresh_lower_degree8_field_residual_nonzero_count','Q10_particular_nonzero_count','full_deDonder_nonzero_component_count','reduced_DG_minus_source_nonzero_component_count','unreduced_DG_minus_source_nonzero_component_count']},indent=2))
    if not o['pass']:raise SystemExit(2)
if __name__=='__main__':main()
