#!/usr/bin/env python3
"""Outcome-blind Critic for corrected Iter057Y source=-AT replay."""
from __future__ import annotations
import argparse,csv,hashlib,json,subprocess,sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'code'))
import qgr_iter057y_onshell_q2_q4_q6_q8_response as base

GATE='ITER057Y_CORRECTED_AT_SOURCE_Q2_Q4_Q6_Q8_REPLAY'
PREREG='4bf46437aaa6ced1813b97bbf0f1f9cbb892c0e5'
PARENT_SCIENCE_PREREG='a6466be9dd3b2ce47bba5be1cacbd184b2161c8f'
BASE_REF='98c82292885cec9a38fa400a5e08b1272104f8b8';BASE_PATH='code/qgr_iter057y_onshell_q2_q4_q6_q8_response.py'
AT_PATH=ROOT/'data'/'ITER057AT_CANONICAL_SOURCE_DEGREE6.csv';AT_FILE_SHA='1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b';AT_PREREG='6039cb2ed1380b549bced3d33634362ef57345d4';AT_PRODUCTION='c4e7ccc05ea1b8f4967379fc370812dfa99cce03'
BJ_RESULT=ROOT/'results'/'ITER057BJ_ITER057Y_SOURCE_CONVENTION_COMMENT_PREDICATE_REPAIR_TERMINAL.md';BJ_PAYLOAD='5941deed797bcdf017b4efdae60a66d1ab0c40e71b16425329b54fdb67bbebbd'
V_DATA_REF='85b53cb708deec75f3d745ffdcebc80020761481';V_TERMINAL_REF='0d98273f8a1ec6071692571518f4faec1af8fa7b';V_TERMINAL_PATH='results/ITER057V_ONSHELL_FIRST_ORDER_Q2_Q4_Q6_RESPONSE_TERMINAL.md'
V_CLASS='PASS_SCOPED_ITER057V_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_FOURTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN';V_PRODUCTION='723598530f1c42cdc12eef25cd3e6fe169e807dd';V_RUN='35017363408';V_JOB='104544061621';V_ARTIFACT='10416157241'

def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def git_show(ref:str,path:str):return subprocess.run(['git','-C',str(ROOT),'show',f'{ref}:{path}'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)

def parse_csv_independent(path:Path):
    raw=path.read_bytes();meta={};lines=[]
    for line in raw.decode('utf-8','strict').splitlines():
        if line.startswith('# '):
            body=line[2:]
            if '=' in body:k,v=body.split('=',1);meta[k]=v
        elif line.strip():lines.append(line)
    rows=[(int(r['a']),int(r['b']),(int(r['t']),int(r['x']),int(r['y']),int(r['z'])),F(r['value'])) for r in csv.DictReader(lines)]
    return raw,meta,rows

def base_identity():
    cur=(ROOT/BASE_PATH).read_bytes();p=git_show(BASE_REF,BASE_PATH);return p.returncode==0 and cur==p.stdout,H(cur),H(p.stdout) if p.returncode==0 else None

def v_authority_independent(V:dict):
    raw=base.V_PATH.read_bytes();pd=git_show(V_DATA_REF,str(base.V_PATH.relative_to(ROOT)));pt=git_show(V_TERMINAL_REF,V_TERMINAL_PATH);terminal=pt.stdout.decode('utf-8','strict') if pt.returncode==0 else ''
    controls={'canonical_data_git_show_exit_zero':pd.returncode==0,'canonical_data_bytes_exact':pd.returncode==0 and raw==pd.stdout,'canonical_classification_exact':V.get('classification')==V_CLASS,'canonical_production_head_exact':V.get('production_head')==V_PRODUCTION,'canonical_run_exact':str(V.get('source_run'))==V_RUN,'canonical_job_exact':str(V.get('source_job'))==V_JOB,'canonical_artifact_exact':str(V.get('source_artifact'))==V_ARTIFACT,'canonical_digest_exact':V.get('source_digest')==base.V_DIGEST,'canonical_shape_exact':V.get('matrix_shape')==[574,840],'canonical_ranks_exact':V.get('rank_M')==V.get('rank_augmented')==494,'canonical_q6_count_exact':len(V.get('Q6_particular_normalized',[]))==88,'terminal_git_show_exit_zero':pt.returncode==0,'terminal_classification_exact':V_CLASS in terminal,'terminal_production_head_exact':V_PRODUCTION in terminal,'terminal_run_exact':V_RUN in terminal,'terminal_job_exact':V_JOB in terminal,'terminal_artifact_exact':V_ARTIFACT in terminal,'terminal_digest_exact':base.V_DIGEST in terminal,'terminal_canonical_data_ref_exact':V_DATA_REF in terminal}
    return all(controls.values()),controls,H(raw),H(pd.stdout) if pd.returncode==0 else None

def lower_response_and_corrected_source():
    S=json.loads(base.S_PATH.read_text());V=json.loads(base.V_PATH.read_text());U=json.loads(base.U_PATH.read_text());raw,meta,at=parse_csv_independent(AT_PATH)
    s_ok=(S.get('terminal_commit')==base.ITER057S and S.get('source_digest')==base.S_DIGEST and len(S.get('Q4_particular_normalized',[]))==34)
    v_ok,v_controls,vsha,vpinsha=v_authority_independent(V)
    urows=U.get('Shat_normalized_sparse',[]);u_ok=(U.get('terminal_commit')==base.ITER057U and U.get('source_digest')==base.U_DIGEST and len([r for r in urows if r['degree']==4])==64)
    at_ok=(H(raw)==AT_FILE_SHA and meta.get('preregistration')==AT_PREREG and meta.get('production_head')==AT_PRODUCTION and len(at)==140 and len({(a,b,*al) for a,b,al,v in at})==140 and all(sum(al)==6 for a,b,al,v in at))
    q=base.pmat()
    for key,val in S['Q2_normalized'].items():
        a,b,c,d=(int(ch) for ch in key);e=[0,0,0,0];e[c]+=1;e[d]+=1;q[a][b]=base.add(q[a][b],base.mono(tuple(e),F(val)/2))
    for item in S['Q4_particular_normalized']:
        a,b=item['pair'];al=tuple(item['alpha']);term=base.mono(al,F(item['value'])/F(base.fact(al)));q[a][b]=base.add(q[a][b],term)
        if a!=b:q[b][a]=base.add(q[b][a],term)
    for item in V['Q6_particular_normalized']:
        a,b=item['pair'];al=tuple(item['alpha']);term=base.mono(al,F(item['value'])/F(base.fact(al)));q[a][b]=base.add(q[a][b],term)
        if a!=b:q[b][a]=base.add(q[b][a],term)
    for a,b in product(range(base.N),repeat=2):q[a][b]=base.trunc(q[a][b],6)
    source=base.pmat()
    for item in urows:
        a,b=item['pair'];al=tuple(item['alpha']);term=base.mono(al,F(item['value'])/F(base.fact(al)));source[a][b]=base.add(source[a][b],term)
        if a!=b:source[b][a]=base.add(source[b][a],term)
    for a,b,al,val in at:
        term=base.mono(al,-val/F(base.fact(al)));source[a][b]=base.add(source[a][b],term)
        if a!=b:source[b][a]=base.add(source[b][a],term)
    for a,b in product(range(base.N),repeat=2):source[a][b]=base.trunc(source[a][b],6)
    return q,source,{'S':s_ok,'V':v_ok,'V_controls':v_controls,'V_current_sha256':vsha,'V_pinned_sha256':vpinsha,'U':u_ok,'AT':at_ok,'at_file_sha256':H(raw),'at_rows':len(at)}

def independent_bianchi_matrix():
    a5=base.alphas(5);a6=base.alphas(6);a7=base.alphas(7);meta=[]
    for b in range(base.N):
        for al in a7:meta.append(('G',b,al))
    for pair in base.PAIRS:
        for al in a6:meta.append(('F',pair,al))
    lookup={m:i for i,m in enumerate(meta)};entries={};rr=0
    for b in range(base.N):
        for beta in a5:
            for m in range(base.N):
                al=list(beta);al[m]+=2;i=lookup[('G',b,tuple(al))];entries[(rr,i)]=entries.get((rr,i),0)+sp.Rational(base.ETA[m],2)
            for a in range(base.N):
                al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a);i=lookup[('F',pair,tuple(al))];entries[(rr,i)]=entries.get((rr,i),0)+sp.Integer(base.ETA[a])
            rr+=1
    return sp.MutableSparseMatrix(rr,len(meta),entries),meta

def compute():
    ident,cursha,pinsha=base_identity();bj=BJ_RESULT.read_text() if BJ_RESULT.exists() else '';bj_ok=('PASS_SCOPED_ITER057BJ_Y_SOURCE_CONVENTION_MAP_MINUS_AT_INDEPENDENTLY_ESTABLISHED' in bj and BJ_PAYLOAD in bj and 'S_std_corrected = -AT' in bj)
    q,source,auth=lower_response_and_corrected_source();g,bgprov=base.seed_metric10();gi,Gamma,Rlow,invok,vacuum=base.geometry8(g);gauge=base.gauge_vector(q,gi,Gamma,7);DG=base.reduced_DG(q,gi,Gamma,Rlow,6);field=base.pmat()
    for a,b in product(range(base.N),repeat=2):field[a][b]=base.trunc(base.sub(DG[a][b],source[a][b]),6)
    rhs=[]
    for b in range(base.N):
        for al in base.alphas(7):rhs.append(-base.qrat(base.normalized(gauge[b],al)))
    for a,b in base.PAIRS:
        for al in base.alphas(6):rhs.append(-base.qrat(base.normalized(field[a][b],al)))
    rhsv=sp.Matrix(rhs);B,meta=independent_bianchi_matrix();compat=B*rhsv;compat_nz=sum(v!=0 for v in compat);brank=DomainMatrix.from_Matrix(B).to_field().rank()
    controls={'pinned_geometric_kernel_byte_exact':ident,'BJ_MAP_MINUS_terminal_authority_exact':bj_ok,'S_authority_exact':auth['S'],'V_authority_exact':auth['V'],'U_authority_exact':auth['U'],'AT_authority_exact':auth['AT'],'AT_file_sha_exact':auth['at_file_sha256']==AT_FILE_SHA,'AT_140_unique_degree6_rows':auth['at_rows']==140,'source_convention_is_minus_AT':True,'background_provenance_exact':bgprov,'background_inverse_through_degree8':invok,'background_vacuum_through_degree8':vacuum,'rhs_length_1320':len(rhs)==1320,'canonical_bianchi_shape_224x1320':B.rows==224 and B.cols==1320,'canonical_bianchi_rank_224':brank==224,'primary_result_not_loaded':True,'exact_arithmetic_no_tolerance':True}
    valid=all(controls.values());classification='CRITIC_INVALID_IMPLEMENTATION_CONTROL_FAILURE' if not valid else ('CRITIC_EXACT_COMPATIBILITY_SUPPORTS_Q8_SOLVABILITY' if compat_nz==0 else 'CRITIC_EXACT_BIANCHI_OBSTRUCTION_TO_Q8_SOLVABILITY')
    return {'gate':GATE,'lane':'outcome_blind_critic','preregistration_commit':PREREG,'parent_science_preregistration':PARENT_SCIENCE_PREREG,'classification':classification,'controls':controls,'iter057V_authority_repair_controls':auth['V_controls'],'iter057V_current_sha256':auth['V_current_sha256'],'iter057V_pinned_sha256':auth['V_pinned_sha256'],'compatibility_nonzero_count':compat_nz,'bianchi_rank':brank,'source_convention':'MAP_MINUS','degree6_source_expression':'-AT','base_current_sha256':cursha,'base_pinned_sha256':pinsha,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT','theory_established_pct':0}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);a=ap.parse_args();out=compute();p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);txt=json.dumps(out,sort_keys=True,indent=2)+'\n';p.write_text(txt);print(txt,end='');return 0
if __name__=='__main__':raise SystemExit(main())
