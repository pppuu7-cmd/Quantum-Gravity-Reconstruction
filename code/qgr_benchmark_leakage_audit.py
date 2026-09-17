#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FORBIDDEN=[r'candidate_specific_kmqgb_verdict\s*=',r'favorable_comparator_target\s*=',r'post_outcome_threshold\s*=',r'future_benchmark_response\s*=']
def audit_text(text):return [p for p in FORBIDDEN if re.search(p,text,re.I)]
def audit(root=ROOT,simulate=False):
    hits=[]
    for base in ('code','templates','synthetic'):
      for p in (root/base).glob('qgr_*'):
        if p.is_file() and p.suffix in {'.py','.json','.md'}:
          for pat in audit_text(p.read_text(errors='replace')):hits.append({'path':str(p.relative_to(root)),'pattern':pat})
    if simulate: hits += [{'path':'SIMULATED','pattern':audit_text('favorable_comparator_target=PASS')[0]}]
    return {'valid':not hits,'classification':'NO_BENCHMARK_TARGET_LEAKAGE' if not hits else 'BENCHMARK_SPECIFIC_TARGET_LEAKAGE','hits':hits}
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--simulate-leak',action='store_true');ap.add_argument('--output');a=ap.parse_args(argv);out=audit(simulate=a.simulate_leak);txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['valid'] else 4
if __name__=='__main__':raise SystemExit(main())
