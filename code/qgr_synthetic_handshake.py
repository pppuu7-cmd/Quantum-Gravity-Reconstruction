#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,subprocess,sys,tempfile
from pathlib import Path
from qgr_candidate_export_validator import validate_candidate
from qgr_kmqgb_adapter import adapt,sha256_bytes
ROOT=Path(__file__).resolve().parents[1]
def run(candidate:Path,kroot:Path,adapted:Path):
    raw=candidate.read_bytes();q=json.loads(raw);native=validate_candidate(q)
    if not native['valid']:return {'valid':False,'stage':'QGR_VALIDATOR','native':native}
    a=adapt(q,sha256_bytes(raw));adapted.parent.mkdir(parents=True,exist_ok=True);adapted.write_text(json.dumps(a,sort_keys=True,indent=2)+'\n')
    env=dict(os.environ);env['PYTHONPATH']=str(kroot/'code')
    cp=subprocess.run([sys.executable,str(kroot/'code/kg_candidate_record_v13_validator.py'),str(adapted)],env=env,text=True,capture_output=True)
    try:up=json.loads(cp.stdout)
    except Exception:up={'raw':cp.stdout,'stderr':cp.stderr}
    statuses={v.get('status') for v in a['promotion_gates'].values()};blocked_preserved=(q['status']=='BLOCKED' and statuses=={'BLOCKED'} and set(q['blockers'])<=set(a['qgr_blockers']) and a['qgr_claim_locks']==q['claim_locks'] and a['qgr_artifact_hashes']==q['artifact_hashes'] and a['qgr_theory_claim_authorized'] is False)
    valid=cp.returncode==0 and bool(up.get('valid')) and blocked_preserved and not up.get('promotion_allowed',False)
    return {'valid':valid,'classification':'QGR_KMQGB_SYNTHETIC_HANDSHAKE_PASS' if valid else 'QGR_KMQGB_SYNTHETIC_HANDSHAKE_INVALID','native':native,'upstream':up,'blocked_preserved':blocked_preserved,'scientific_status':'BLOCKED','adapted_sha256':sha256_bytes(adapted.read_bytes()),'native_sha256':sha256_bytes(raw)}
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--candidate',default=str(ROOT/'synthetic/qgr_synthetic_blocked_candidate_v1.json'));ap.add_argument('--kmqgb-root',required=True);ap.add_argument('--adapted-output',required=True);ap.add_argument('--output');a=ap.parse_args(argv)
    out=run(Path(a.candidate),Path(a.kmqgb_root),Path(a.adapted_output));txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['valid'] else 1
if __name__=='__main__':raise SystemExit(main())
