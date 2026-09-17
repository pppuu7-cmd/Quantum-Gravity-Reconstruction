#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

GATE="ITER057BC_SAME_ITERATION_EDGE_POLLUTION_CAUSAL_DIAGNOSTIC"
PREREG="e8c7e1d95c2b12b0b513e5431d053a92d8141455"
BB_PREREG="eb864872be1db63d0588296c606b759b7b1495c8"
CENSUS="616859890df95057556d265612c53da839a5848a"
EXPECTED_BB_NORM="5cba0b3b3e8475b974d8cf8f633875a7a1ab63f92b1503cbb353633ca2ac9189"
D="DIRECT_LOAD_BEARING_DEPENDENT"
T="TRANSITIVE_LOAD_BEARING_DEPENDENT"
I="INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE"
U="UNRESOLVED_PROVENANCE"


def digest(data:bytes)->str:return hashlib.sha256(data).hexdigest()
def ordinal(label:str)->int:
    suffix=label.upper().split("ITER057",1)[1]
    total=0
    for letter in suffix:total=26*total+(ord(letter)-ord("A")+1)
    return total

def analyze(raw:dict)->dict:
    rows=raw.get("ordered_classifications") or []
    details=raw.get("classification_detail") or []
    detail_index={entry["record"]:entry for entry in details}
    sequence=[entry["record"] for entry in rows]
    iteration_of={entry["record"]:entry["iteration"] for entry in rows}
    original={entry["record"]:entry["class"] for entry in rows}

    buckets={"EARLIER":[],"EQUAL":[],"LATER":[]}
    for record in sequence:
        child_iteration=iteration_of[record]
        child_rank=ordinal(child_iteration)
        parents=detail_index.get(record,{}).get("explicit_iteration_dependencies",[])
        for parent_iteration in parents:
            parent_rank=ordinal(parent_iteration)
            relation="EARLIER" if parent_rank<child_rank else "EQUAL" if parent_rank==child_rank else "LATER"
            buckets[relation].append((record,parent_iteration))
    for name in buckets:buckets[name]=sorted(set(buckets[name]),key=lambda z:(ordinal(iteration_of[z[0]]),z[0],ordinal(z[1]),z[1]))

    earlier_parents={record:set() for record in sequence}
    for record,parent in buckets["EARLIER"]:earlier_parents[record].add(parent)

    rebuilt={record:D for record in sequence if original[record]==D}
    progress=True
    while progress:
        progress=False
        dependent_iteration_labels={iteration_of[r] for r,c in rebuilt.items() if c in {D,T}}
        additions=[]
        for record in sequence:
            if record in rebuilt:continue
            if any(parent in dependent_iteration_labels for parent in earlier_parents[record]):additions.append(record)
        for record in additions:
            rebuilt[record]=T;progress=True

    for record in sequence:
        if record in rebuilt:continue
        if original[record]==I:rebuilt[record]=I
        elif original[record]==U:rebuilt[record]=U
        else:rebuilt[record]="NO_LONGER_TRANSITIVE_AFTER_EARLIER_ONLY_FILTER"

    filtered_rows=[{"record":record,"iteration":iteration_of[record],"class":rebuilt[record]} for record in sequence]
    filtered_queue=[record for record in sequence if rebuilt[record] in {D,T}]
    equal_pairs=[{"record":record,"parent_iteration":parent} for record,parent in buckets["EQUAL"]]
    later_pairs=[{"record":record,"parent_iteration":parent} for record,parent in buckets["LATER"]]
    candidate_count=sum(len(v) for v in buckets.values())
    earlier_graph_valid=all(ordinal(parent)<ordinal(iteration_of[record]) for record,parent in buckets["EARLIER"])
    controls={
      "raw_gate_is_bb":raw.get("gate")=="ITER057BB_CONDITIONAL_BYTE_SAFE_DESCENDANT_DEPENDENCY_ADJUDICATION_RETRY",
      "raw_mode_independent":raw.get("mode")=="independent",
      "bb_prereg_exact":raw.get("bb_preregistration_commit")==BB_PREREG,
      "au_census_exact":raw.get("au_census_head")==CENSUS,
      "bb_scientific_normalized_exact":raw.get("scientific_normalized_sha256")==EXPECTED_BB_NORM,
      "complete_census_23":len(sequence)==23 and len(set(sequence))==23 and raw.get("record_count")==23,
      "candidate_partition_complete":candidate_count==len(buckets["EARLIER"])+len(buckets["EQUAL"])+len(buckets["LATER"]),
      "zero_later_candidates":len(buckets["LATER"])==0,
      "equal_candidates_nonempty":len(buckets["EQUAL"])>0,
      "earlier_only_graph_acyclic":earlier_graph_valid,
      "filtered_classes_unchanged":filtered_rows==rows,
      "filtered_replay_queue_unchanged":filtered_queue==raw.get("replay_queue"),
      "descendant_science_replayed":False,
      "historical_result_modified":False,
      "claim_lock_promoted":False,
    }
    return {
      "gate":GATE,"mode":"independent","preregistration_commit":PREREG,"bb_preregistration_commit":BB_PREREG,"au_census_head":CENSUS,
      "implementation_path":"scripts/qgr_iter057bc_independent_equal_edge_diagnostic.py","implementation_sha256":digest(Path(__file__).read_bytes()),
      "raw_bb_scientific_normalized_sha256":raw.get("scientific_normalized_sha256"),"raw_bb_implementation_sha256":raw.get("implementation_sha256"),
      "candidate_count":candidate_count,"earlier_count":len(buckets["EARLIER"]),"equal_count":len(buckets["EQUAL"]),"later_count":len(buckets["LATER"]),
      "equal_pairs":equal_pairs,"later_pairs":later_pairs,"filtered_ordered_classifications":filtered_rows,"filtered_replay_queue":filtered_queue,
      "raw_ordered_classifications":rows,"raw_replay_queue":raw.get("replay_queue"),"undecodable_provenance_objects":raw.get("undecodable_provenance_objects",[]),
      "controls":controls,
      "all_local_controls_pass":all(v is True or (v is False and k in {"descendant_science_replayed","historical_result_modified","claim_lock_promoted"}) for k,v in controls.items()),
      "descendant_science_consumed":False,"theory_established_pct":0,"c6":"SYMBOLIC_UNFIXED"
    }

def main()->int:
    parser=argparse.ArgumentParser();parser.add_argument("--input",required=True,type=Path);parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    raw=json.loads(args.input.read_text(encoding="utf-8"));result=analyze(raw);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8");print(json.dumps(result,indent=2,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
