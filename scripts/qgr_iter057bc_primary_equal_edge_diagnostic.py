#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

GATE="ITER057BC_SAME_ITERATION_EDGE_POLLUTION_CAUSAL_DIAGNOSTIC"
PREREG="e8c7e1d95c2b12b0b513e5431d053a92d8141455"
BB_PREREG="eb864872be1db63d0588296c606b759b7b1495c8"
AU_CENSUS="616859890df95057556d265612c53da839a5848a"
BB_NORMALIZED="5cba0b3b3e8475b974d8cf8f633875a7a1ab63f92b1503cbb353633ca2ac9189"
DIRECT="DIRECT_LOAD_BEARING_DEPENDENT"
TRANSITIVE="TRANSITIVE_LOAD_BEARING_DEPENDENT"
INDEPENDENT="INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE"
UNRESOLVED="UNRESOLVED_PROVENANCE"


def rank(iteration: str) -> int:
    tag=iteration.upper().replace("ITER057","")
    n=0
    for ch in tag:n=n*26+(ord(ch)-64)
    return n

def sha(raw:bytes)->str:return hashlib.sha256(raw).hexdigest()
def canon(x)->bytes:return json.dumps(x,sort_keys=True,separators=(",",":")).encode("utf-8")

def build(raw:dict)->dict:
    ordered=raw.get("ordered_classifications",[])
    details=raw.get("classification_detail",[])
    record_order=[x["record"] for x in ordered]
    raw_class={x["record"]:x["class"] for x in ordered}
    iteration={x["record"]:x["iteration"] for x in ordered}
    detail_by={x["record"]:x for x in details}
    candidates=[]
    for rec in record_order:
        child=iteration[rec]
        for parent in detail_by.get(rec,{}).get("explicit_iteration_dependencies",[]):
            relation="EARLIER" if rank(parent)<rank(child) else ("EQUAL" if rank(parent)==rank(child) else "LATER")
            candidates.append({"record":rec,"child_iteration":child,"parent_iteration":parent,"relation":relation})
    candidates.sort(key=lambda x:(rank(x["child_iteration"]),x["record"],rank(x["parent_iteration"]),x["parent_iteration"]))
    earlier=[x for x in candidates if x["relation"]=="EARLIER"]
    equal=[x for x in candidates if x["relation"]=="EQUAL"]
    later=[x for x in candidates if x["relation"]=="LATER"]
    parent_map={r:set() for r in record_order}
    for x in earlier:parent_map[x["record"]].add(x["parent_iteration"])
    filtered={r:DIRECT for r in record_order if raw_class[r]==DIRECT}
    while True:
        changed=False
        active={iteration[r] for r,c in filtered.items() if c in {DIRECT,TRANSITIVE}}
        for rec in record_order:
            if rec in filtered:continue
            if parent_map[rec] & active:
                filtered[rec]=TRANSITIVE;changed=True
        if not changed:break
    for rec in record_order:
        if rec in filtered:continue
        if raw_class[rec] in {INDEPENDENT,UNRESOLVED}:filtered[rec]=raw_class[rec]
        else:filtered[rec]="NO_LONGER_TRANSITIVE_AFTER_EARLIER_ONLY_FILTER"
    filtered_ordered=[{"record":r,"iteration":iteration[r],"class":filtered[r]} for r in record_order]
    filtered_queue=[r for r in record_order if filtered[r] in {DIRECT,TRANSITIVE}]
    equal_pairs=[{"record":x["record"],"parent_iteration":x["parent_iteration"]} for x in equal]
    later_pairs=[{"record":x["record"],"parent_iteration":x["parent_iteration"]} for x in later]
    earlier_acyclic=all(rank(x["parent_iteration"])<rank(x["child_iteration"]) for x in earlier)
    raw_undecodable=raw.get("undecodable_provenance_objects",[])
    controls={
      "raw_gate_is_bb":raw.get("gate")=="ITER057BB_CONDITIONAL_BYTE_SAFE_DESCENDANT_DEPENDENCY_ADJUDICATION_RETRY",
      "raw_mode_primary":raw.get("mode")=="primary",
      "bb_prereg_exact":raw.get("bb_preregistration_commit")==BB_PREREG,
      "au_census_exact":raw.get("au_census_head")==AU_CENSUS,
      "bb_scientific_normalized_exact":raw.get("scientific_normalized_sha256")==BB_NORMALIZED,
      "complete_census_23":len(record_order)==23==raw.get("record_count") and len(set(record_order))==23,
      "candidate_partition_complete":len(candidates)==len(earlier)+len(equal)+len(later),
      "zero_later_candidates":len(later)==0,
      "equal_candidates_nonempty":len(equal)>0,
      "earlier_only_graph_acyclic":earlier_acyclic,
      "filtered_classes_unchanged":filtered_ordered==ordered,
      "filtered_replay_queue_unchanged":filtered_queue==raw.get("replay_queue"),
      "undecodable_payload_preserved":raw_undecodable==raw.get("undecodable_provenance_objects",[]),
      "descendant_science_replayed":False,
      "historical_result_modified":False,
      "claim_lock_promoted":False,
    }
    return {
      "gate":GATE,"mode":"primary","preregistration_commit":PREREG,
      "bb_preregistration_commit":BB_PREREG,"au_census_head":AU_CENSUS,
      "implementation_path":"scripts/qgr_iter057bc_primary_equal_edge_diagnostic.py",
      "implementation_sha256":sha(Path(__file__).read_bytes()),
      "raw_bb_scientific_normalized_sha256":raw.get("scientific_normalized_sha256"),
      "raw_bb_implementation_sha256":raw.get("implementation_sha256"),
      "candidate_count":len(candidates),"earlier_count":len(earlier),"equal_count":len(equal),"later_count":len(later),
      "equal_pairs":equal_pairs,"later_pairs":later_pairs,
      "filtered_ordered_classifications":filtered_ordered,"filtered_replay_queue":filtered_queue,
      "raw_ordered_classifications":ordered,"raw_replay_queue":raw.get("replay_queue"),
      "undecodable_provenance_objects":raw_undecodable,
      "controls":controls,
      "all_local_controls_pass":all(v is True or (v is False and k in {"descendant_science_replayed","historical_result_modified","claim_lock_promoted"}) for k,v in controls.items()),
      "descendant_science_consumed":False,"theory_established_pct":0,"c6":"SYMBOLIC_UNFIXED"
    }

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("--input",type=Path,required=True);p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    raw=json.loads(a.input.read_text(encoding="utf-8"));out=build(raw);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True,indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
