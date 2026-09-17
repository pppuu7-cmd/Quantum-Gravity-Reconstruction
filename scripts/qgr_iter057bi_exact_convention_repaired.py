#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json
from fractions import Fraction as F
from pathlib import Path

GATE='ITER057BI_ITER057Y_SOURCE_CONVENTION_EXTRACTOR_REPAIR'
PREREG='098cccf263d9812d81026e3f3e8fe4418b9766ab'
AQ_CLASS='PASS_SCOPED_ITER057AQ_DISCREPANCY_LOCALIZED_TO_LEGACY_P_CONSTRUCTION'
AQ_PREREG='3ac98107c7a659f63271c9836583e929bc35adb4'
X_PREREG='b5f88ced655c4fa409c4ccb9c27eb84054ecfad7'
X_IMPL='920b73f8430983255081b9bcd3ec6d222b737b08'
X_PAYLOAD='7a85a8b78e6876810ecefc6e1b37efea956caa41f26d54f4f8b9dcf16ca45249'
AT_FILE_SHA='1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b'
AT_VECTOR_SHA='5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b'


def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def J(x)->bytes:return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def fs(x:F)->str:return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def read_csv(path:Path):
    raw=path.read_bytes();meta={};descriptive=[];body=[]
    for line in raw.decode('utf-8','strict').splitlines():
        if line.startswith('# '):
            payload=line[2:]
            if '=' in payload:
                k,v=payload.split('=',1);meta[k]=v
            else:
                descriptive.append(payload)
        elif line.strip():body.append(line)
    return raw,meta,descriptive,list(csv.DictReader(body))
def relation(a:list[dict],b:list[dict]):
    same=True;neg=True;m_same=0;m_neg=0
    for x,y in zip(a,b):
        vx=F(x['value']);vy=F(y['value'])
        if vx!=vy:same=False;m_same+=1
        if vx!=-vy:neg=False;m_neg+=1
    if same:return 'SAME',m_same,m_neg
    if neg:return 'NEGATIVE',m_same,m_neg
    return 'NEITHER',m_same,m_neg
def reconstruct(rows:list[dict],template:list[dict]):
    sparse={}
    for r in rows:
        key=(int(r['a']),int(r['b']),int(r['t']),int(r['x']),int(r['y']),int(r['z']))
        if key in sparse:raise ValueError('duplicate sparse source row')
        sparse[key]=F(r['value'])
    return [{'pair':list(z['pair']),'alpha':list(z['alpha']),'value':fs(sparse.get(tuple(z['pair']+z['alpha']),F(0)))} for z in template]
def strip_degree(cell:list[dict]):return [{'pair':list(z['pair']),'alpha':list(z['alpha']),'value':fs(F(z['value']))} for z in cell if int(z['degree'])==6]

def build(aq_path:Path,x_path:Path,at_path:Path):
    aq=json.loads(aq_path.read_text(encoding='utf-8'));xraw,xmeta,xcomments,xrows=read_csv(x_path);atraw,atmeta,atcomments,atrows=read_csv(at_path)
    cells=aq.get('cells',{});oxpl=strip_degree(cells.get('OX_PL',[]));oxpf=strip_degree(cells.get('OX_PF',[]));oaopl=strip_degree(cells.get('OAO_PL',[]));oaopf=strip_degree(cells.get('OAO_PF',[]))
    if len(oxpl)!=840 or len(oxpf)!=840:raise ValueError('AQ degree-six cell cardinality is not 840')
    xvec=reconstruct(xrows,oxpl);atvec=reconstruct(atrows,oxpf)
    xrel,xsame_m,xneg_m=relation(xvec,oxpl);atrel,atsame_m,atneg_m=relation(atvec,oxpf)
    pl_operator_rel=relation(oxpl,oaopl)[0];pf_operator_rel=relation(oxpf,oaopf)[0]
    at_hash=H(J(atvec));oxpf_hash=H(J(oxpf));x_hash=H(J(xvec));oxpl_hash=H(J(oxpl))
    mapping='MAP_PLUS' if xrel=='SAME' and atrel=='SAME' else ('MAP_MINUS' if xrel=='NEGATIVE' and atrel=='SAME' else 'UNRESOLVED')
    controls={
      'aq_prereg_exact':aq.get('preregistration')==AQ_PREREG,
      'aq_terminal_classification_exact':aq.get('classification')==AQ_CLASS,
      'aq_controls_all_true':bool(aq.get('controls')) and all(v is True for v in aq['controls'].values()),
      'aq_target_coefficients_not_loaded':aq.get('controls',{}).get('D_target_coefficients_not_loaded') is True,
      'aq_cells_complete_degree6_840':len(oxpl)==len(oxpf)==len(oaopl)==len(oaopf)==840,
      'ox_pl_equals_oao_pl':pl_operator_rel=='SAME','ox_pf_equals_oao_pf':pf_operator_rel=='SAME',
      'x_descriptive_comment_preserved':len(xcomments)>=1 and 'ITER057X canonical authority' in xcomments,
      'x_metadata_exact':xmeta.get('preregistration')==X_PREREG and xmeta.get('implementation')==X_IMPL and xmeta.get('scientific_payload_sha256')==X_PAYLOAD,
      'x_sparse_140_unique_degree6':len(xrows)==140 and len({(r['a'],r['b'],r['t'],r['x'],r['y'],r['z']) for r in xrows})==140 and all(sum(int(r[k]) for k in ('t','x','y','z'))==6 for r in xrows),
      'x_relation_is_exact_same_or_negative':xrel in {'SAME','NEGATIVE'},
      'at_file_sha_exact':H(atraw)==AT_FILE_SHA,
      'at_sparse_140_unique_degree6':len(atrows)==140 and len({(r['a'],r['b'],r['t'],r['x'],r['y'],r['z']) for r in atrows})==140 and all(sum(int(r[k]) for k in ('t','x','y','z'))==6 for r in atrows),
      'at_equals_fresh_ox_pf_exact':atrel=='SAME','at_vector_sha_exact':at_hash==oxpf_hash==AT_VECTOR_SHA,
      'no_sign_scale_fit':True,'corrected_y_response_not_executed':True,'historical_file_modified':False,'claim_lock_promoted':False}
    positive=all(v is True for k,v in controls.items() if k not in {'corrected_y_response_not_executed','historical_file_modified','claim_lock_promoted'}) and controls['corrected_y_response_not_executed'] is True and controls['historical_file_modified'] is False and controls['claim_lock_promoted'] is False
    if not positive:mapping='UNRESOLVED'
    return {'gate':GATE,'lane':'exact_repaired','preregistration_commit':PREREG,'controls':controls,'historical_x_relation_to_ox_pl':xrel,'historical_x_same_mismatch_count':xsame_m,'historical_x_negative_mismatch_count':xneg_m,'corrected_at_relation_to_ox_pf':atrel,'corrected_at_same_mismatch_count':atsame_m,'corrected_at_negative_mismatch_count':atneg_m,'ox_pl_oao_pl_relation':pl_operator_rel,'ox_pf_oao_pf_relation':pf_operator_rel,'x_full_840_vector_sha256':x_hash,'ox_pl_degree6_vector_sha256':oxpl_hash,'at_full_840_vector_sha256':at_hash,'ox_pf_degree6_vector_sha256':oxpf_hash,'x_csv_sha256':H(xraw),'at_csv_sha256':H(atraw),'x_descriptive_comments':xcomments,'corrected_source_map':mapping,'implied_corrected_source_expression':'-AT' if mapping=='MAP_MINUS' else ('+AT' if mapping=='MAP_PLUS' else None),'all_controls_pass':positive and mapping!='UNRESOLVED','corrected_y_science_consumed':False,'theory_established_pct':0,'c6':'SYMBOLIC_UNFIXED'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--aq-output',type=Path,required=True);p.add_argument('--x-source',type=Path,required=True);p.add_argument('--at-source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=build(a.aq_output,a.x_source,a.at_source);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n');print(json.dumps(o,sort_keys=True,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
