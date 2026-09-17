#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FORBIDDEN=[r'candidate_specific_kmqgb_verdict\s*=',r'favorable_comparator_target\s*=',r'post_outcome_threshold\s*=',r'future_benchmark_response\s*=']
# Detector/negative-control sources must contain the forbidden signatures in order
# to prove they are rejected. They are validators, not candidate-construction files.
TEST_ONLY={'qgr_benchmark_leakage_audit.py','qgr_negative_controls.py'}
def audit_text(text):return [p for p in FORBIDDEN if re.search(p,text,re.I)]
def audit(root=ROOT,simulate=False):
    hits=[]
    for base in ('code','templates','synthetic'):
      for p in (root/base).glob('qgr_*'):
        if p.name in TEST_ONLY: continue
        if p.is_file() and p.suffix in {'.py','.json','.md'}:
          for pat in audit_text(p.read_text(errors='replace')):hits.append({'path':str(p.relative_to(root)),'pattern':pat})
    if simulate: hits += [{'path':'SIMULATED_NEGATIVE_CONTROL','pattern':FORBIDDEN[1]}]
    return {'valid':not hits,'classification':'NO_BENCHMARK_TARGET_LEAKAGE' if not hits else 'BENCHMARK_SPECIFIC_TARGET_LEAKAGE','hits':hits,'test_only_exclusions':sorted(TEST_ONLY)}
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--simulate-leak',action='store_true');ap.add_argument('--output');a=ap.parse_args(argv);out=audit(simulate=a.simulate_leak);txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['valid'] else 4
if __name__=='__main__':raise SystemExit(main())
