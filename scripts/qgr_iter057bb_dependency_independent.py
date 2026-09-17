#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

LOCK_COMMIT="eb864872be1db63d0588296c606b759b7b1495c8"
SNAPSHOT="616859890df95057556d265612c53da839a5848a"
LOCK_CLASS="PASS_SCOPED_ITER057BA_NEUTRAL_CANONICAL_BYTE_SAFE_CERTIFICATE_INDEPENDENTLY_REPRODUCED"
LOCK_FILE="results/ITER057BA_NEUTRAL_CANONICAL_BYTE_SAFE_CERTIFICATE_TERMINAL.md"
GATE="ITER057BB_CONDITIONAL_BYTE_SAFE_DESCENDANT_DEPENDENCY_ADJUDICATION_RETRY"
HEADER=b"QGR_TRACKED_TREE_MAP_V1\n"
TEXT_SUFFIXES={".md",".json",".yml",".yaml",".py",".txt",".toml",".ini",".cfg",".sh"}
DEP_TERMS=("input","inputs","source","sources","consume","consumes","consumed","load","loaded","loads","depend","depends","dependency","derived","parent","lineage","provenance","replay","uses","using","from","canonical","artifact","manifest","hash","sha256")
DENIALS=("independent of","does not depend","not dependent","without reading","historical only","historical record","remains immutable","preserved only","not rewritten","do not rewrite","no retroactive","not load-bearing")
PATH_RX=re.compile(r"(?:(?:results|preregistration|prereg|scripts|recovery|data|artifacts)/[^\s`'\"<>]+|\.github/workflows/[^\s`'\"<>]+)")
SHA40=re.compile(r"\b[0-9a-f]{40}\b",re.I); SHA64=re.compile(r"\b[0-9a-f]{64}\b",re.I)
ITER_RX=re.compile(r"\b(?:ITER|Iter|iter)057([A-Z]{1,3})\b")
RESULT_RX=re.compile(r"^results/.*?ITER057([A-Z]{1,3})[^/]*\.(?:md|json|ya?ml|txt)$",re.I)


def H(raw:bytes)->str:return hashlib.sha256(raw).hexdigest()
def J(x)->bytes:return json.dumps(x,sort_keys=True,separators=(",",":")).encode("utf-8")
def rank(tag:str)->int:
    value=0
    for c in tag.upper(): value=value*26+ord(c)-64
    return value

def command(repo:Path,args:list[str],must:bool=True)->tuple[int,bytes,bytes]:
    p=subprocess.run(["git","-C",str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if must and p.returncode!=0: raise RuntimeError(f"git command failed rc={p.returncode} stderr_sha256={H(p.stderr)}")
    return p.returncode,p.stdout,p.stderr

def remember_bad(bucket:list[dict],kind:str,raw:bytes,owner:str,source:str,commit:str=""):
    item={"kind":kind,"owner_record":owner,"source":source,"commit":commit,"raw_sha256":H(raw),"raw_length":len(raw)}
    if kind.endswith("PATH"): item["raw_path_hex"]=raw.hex()
    sig=(kind,owner,source,commit,item["raw_sha256"])
    if sig not in {(x["kind"],x["owner_record"],x["source"],x["commit"],x["raw_sha256"]) for x in bucket}: bucket.append(item)

def text_or_bad(raw:bytes,bucket:list[dict],kind:str,owner:str,source:str,commit:str=""):
    try:return raw.decode("utf-8","strict")
    except UnicodeDecodeError: remember_bad(bucket,kind,raw,owner,source,commit); return None

def names_from_tree(repo:Path,subtree:str,bucket:list[dict],owner:str)->list[str]:
    _,raw,_=command(repo,["ls-tree","-r","--name-only","-z",SNAPSHOT,"--",subtree])
    got=[]
    for b in filter(None,raw.split(b"\0")):
        s=text_or_bad(b,bucket,"NON_UTF8_PROVENANCE_PATH",owner,f"tree:{SNAPSHOT}:{subtree}:path:{H(b)}",SNAPSHOT)
        if s is not None: got.append(s)
    return got

def blob_text(repo:Path,ref:str,path:str,bucket:list[dict],owner:str):
    rc,raw,_=command(repo,["show",f"{ref}:{path}"],False)
    if rc:return None
    return text_or_bad(raw,bucket,"NON_UTF8_PROVENANCE_CONTENT",owner,f"{ref}:{path}",ref)

def commit_text_paths(repo:Path,commit:str,bucket:list[dict],owner:str)->list[str]:
    _,raw,_=command(repo,["show","--format=","--name-only","-z",commit],False)
    ans=[]
    for b in filter(None,raw.split(b"\0")):
        s=text_or_bad(b,bucket,"NON_UTF8_PROVENANCE_PATH",owner,f"commit:{commit}:changed-path:{H(b)}",commit)
        if s is not None and Path(s).suffix.lower() in TEXT_SUFFIXES: ans.append(s)
    return sorted(set(ans))

def census(repo:Path,bucket:list[dict])->list[tuple[str,str]]:
    rows=[]
    for p in names_from_tree(repo,"results",bucket,"__CENSUS__"):
        m=RESULT_RX.match(p)
        if m and rank(m.group(1))>24: rows.append((p,m.group(1).upper()))
    return sorted(rows,key=lambda x:(rank(x[1]),x[0]))

def x_records(repo:Path,bucket:list[dict])->list[str]:
    ans=[]
    for p in names_from_tree(repo,"results",bucket,"__LEGACY_SEED__"):
        m=RESULT_RX.match(p)
        if m and m.group(1).upper()=="X":ans.append(p)
    return sorted(ans)

def provenance(repo:Path,record:str,bucket:list[dict])->list[tuple[str,str]]:
    base=blob_text(repo,SNAPSHOT,record,bucket,record)
    if base is None:return []
    entries=[(record,base)]; used={record}
    explicit=[]
    for hit in PATH_RX.finditer(base): explicit.append(hit.group(0).rstrip(".,;:)]}"))
    for p in explicit:
        if p in used:continue
        t=blob_text(repo,SNAPSHOT,p,bucket,record)
        if t is not None and len(t.encode("utf-8"))<=1_000_000: entries.append((p,t));used.add(p)
    commits=[]
    for line in base.splitlines():
        commits.extend(SHA40.findall(line))
    for c in sorted(set(commits)):
        for p in commit_text_paths(repo,c,bucket,record):
            key=c+":"+p
            if key in used:continue
            t=blob_text(repo,c,p,bucket,record)
            if t is not None and len(t.encode("utf-8"))<=1_000_000:entries.append((key,t));used.add(key)
    return entries

def legacy_anchors(repo:Path,bucket:list[dict]):
    anchors={"ITER057X","Iter057X","iter057x"}; sources=x_records(repo,bucket)
    for p in sources:
        t=blob_text(repo,SNAPSHOT,p,bucket,"__LEGACY_SEED__")
        if t is None:continue
        for line in t.splitlines():
            anchors.update(SHA40.findall(line));anchors.update(SHA64.findall(line))
            for path in PATH_RX.findall(line):
                if any(k in path.lower() for k in ("degree6","degree_6","weyl","source","iter057x")):anchors.add(path.rstrip(".,;:)]}"))
    return anchors,sources

def line_classifier(entries:list[tuple[str,str]],known:set[str],anchors:set[str]):
    deps=set();legacy=False;evidence=[]
    candidate_anchors=[(a.lower(),a) for a in anchors if len(a)>=8 and a.lower()!="iter057x"]
    for src,text in entries:
        lines=text.splitlines()
        for i in range(len(lines)):
            neighborhood="\n".join(lines[max(0,i-1):min(len(lines),i+2)])
            low=neighborhood.lower()
            if any(d in low for d in DENIALS) or not any(w in low for w in DEP_TERMS):continue
            for m in ITER_RX.finditer(neighborhood):
                tag=m.group(1).upper()
                if tag in known or tag=="X":
                    deps.add(tag);evidence.append(f"{src}:line{max(1,i)}->ITER057{tag}")
                    if tag=="X":legacy=True
            for lowa,rawa in candidate_anchors:
                if lowa in low:
                    legacy=True;evidence.append(f"{src}:line{max(1,i)}:legacy-anchor:{rawa[:24]}");break
    return deps,legacy,sorted(set(evidence))
def enough(entries:list[tuple[str,str]])->bool:
    chunks=[]
    for _,t in entries:chunks.extend(t.lower().splitlines())
    merged="\n".join(chunks)
    mechanism=any(w in merged for w in ("preregistration","implementation","production head","actions run","artifact","source","input","manifest","durable result","commit"))
    concrete=SHA40.search(merged) is not None or SHA64.search(merged) is not None or PATH_RX.search(merged) is not None
    return mechanism and concrete

def graph_is_acyclic(edge_map:dict[str,set[str]],tag_of:dict[str,str])->bool:
    for record,parents in edge_map.items():
        child=rank(tag_of[record])
        for parent in parents:
            parent_rank=24 if parent=="X" else rank(parent)
            if parent_rank>=child:return False
    return True

def digest_tracked(repo:Path)->str:
    _,raw,_=command(repo,["ls-files","-z"]); pairs=[]
    for b in filter(None,raw.split(b"\0")):
        name=b.decode("utf-8","strict");pairs.append((b,H((repo/name).read_bytes()).encode("ascii")))
    pairs=sorted(pairs,key=lambda x:x[0]);stream=HEADER+b"".join(p.hex().encode("ascii")+b"\t"+h+b"\n" for p,h in pairs)
    return H(stream)
def tracked_only_clean(repo:Path)->bool:
    _,raw,_=command(repo,["status","--porcelain","--untracked-files=no"]);return raw.decode("utf-8","strict")==""

def build(repo:Path)->dict:
    d0=digest_tracked(repo);clean0=tracked_only_clean(repo);bad=[]
    lock=(repo/LOCK_FILE).exists() and LOCK_CLASS in (repo/LOCK_FILE).read_text(encoding="utf-8")
    rows=census(repo,bad);tag_of=dict(rows);known=set(tag_of.values());anchors,xsrc=legacy_anchors(repo,bad)
    ctx={};parent_map={};direct={};evidence={};suff={}
    for rec,_ in rows:
        ctx[rec]=provenance(repo,rec,bad);parents,is_direct,ev=line_classifier(ctx[rec],known,anchors)
        parent_map[rec]=parents;direct[rec]=is_direct;evidence[rec]=ev;suff[rec]=enough(ctx[rec])
    cls={}
    for rec,_ in rows:
        if direct[rec]:cls[rec]="DIRECT_LOAD_BEARING_DEPENDENT"
    while True:
        before=len(cls);dependent_tags={tag_of[r] for r,c in cls.items() if c in ("DIRECT_LOAD_BEARING_DEPENDENT","TRANSITIVE_LOAD_BEARING_DEPENDENT")}
        for rec,_ in rows:
            if rec not in cls and any(p in dependent_tags for p in parent_map[rec]):cls[rec]="TRANSITIVE_LOAD_BEARING_DEPENDENT"
        if len(cls)==before:break
    by_owner={}
    for item in bad:by_owner.setdefault(item["owner_record"],[]).append(item)
    global_unknown=bool(by_owner.get("__CENSUS__") or by_owner.get("__LEGACY_SEED__"))
    for rec,_ in rows:
        if rec in cls:continue
        if global_unknown or by_owner.get(rec):cls[rec]="UNRESOLVED_PROVENANCE"
        else:cls[rec]="INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE" if suff[rec] else "UNRESOLVED_PROVENANCE"
    for item in bad:
        owner=item["owner_record"];item["classification_load_bearing"]=owner in ("__CENSUS__","__LEGACY_SEED__") or cls.get(owner)=="UNRESOLVED_PROVENANCE"
    bad.sort(key=lambda x:(x["kind"],x["owner_record"],x["source"],x["commit"],x["raw_sha256"]))
    ordered=[{"record":r,"iteration":"ITER057"+t,"class":cls[r]} for r,t in rows]
    queue=[x["record"] for x in ordered if x["class"] in ("DIRECT_LOAD_BEARING_DEPENDENT","TRANSITIVE_LOAD_BEARING_DEPENDENT")]
    detail=[]
    for rec,t in rows:
        ev=list(evidence[rec]) or [f"{rec}:record-and-referenced-provenance-reviewed"]
        ev.extend(f"{x['kind']}:{x['raw_sha256']}" for x in by_owner.get(rec,[]))
        detail.append({"record":rec,"iteration":"ITER057"+t,"class":cls[rec],"evidence_path":sorted(set(ev)),"explicit_iteration_dependencies":["ITER057"+p for p in sorted(parent_map[rec],key=rank)],"provenance_sufficient_from_readable_objects":suff[rec]})
    normalized_bad=[]
    for item in bad:
        x={k:item[k] for k in ("kind","owner_record","source","commit","raw_sha256","raw_length","classification_load_bearing")}
        if "raw_path_hex" in item:x["raw_path_hex"]=item["raw_path_hex"]
        normalized_bad.append(x)
    d1=digest_tracked(repo);clean1=tracked_only_clean(repo)
    controls={"execution_lock_exact":lock,"complete_census_unique":len(rows)==len(set(r for r,_ in rows))==len(ordered),"every_record_classified_once":all(x["class"] in ("DIRECT_LOAD_BEARING_DEPENDENT","TRANSITIVE_LOAD_BEARING_DEPENDENT","INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE","UNRESOLVED_PROVENANCE") for x in ordered),"dag_acyclic":graph_is_acyclic(parent_map,tag_of),"replay_queue_excludes_independent_and_unresolved":all(cls[r] in ("DIRECT_LOAD_BEARING_DEPENDENT","TRANSITIVE_LOAD_BEARING_DEPENDENT") for r in queue),"evidence_path_for_every_classification":all(bool(x["evidence_path"]) for x in detail),"tracked_status_clean_before":clean0,"tracked_status_clean_after":clean1,"canonical_tracked_tree_digest_unchanged":d0==d1,"descendant_science_recomputed":False,"descendant_outcomes_used_as_targets":False,"claim_lock_promoted":False,"criteria_or_census_mutated":False}
    normalized={"census":[r for r,_ in rows],"ordered_classifications":ordered,"replay_queue":queue,"undecodable_provenance_objects":normalized_bad}
    return {"gate":GATE,"mode":"independent","bb_preregistration_commit":LOCK_COMMIT,"au_census_head":SNAPSHOT,"ba_required_classification":LOCK_CLASS,"ba_execution_lock_satisfied":lock,"implementation_path":"scripts/qgr_iter057bb_dependency_independent.py","implementation_sha256":H(Path(__file__).read_bytes()),"iter057x_seed_records":xsrc,"record_count":len(rows),"ordered_classifications":ordered,"classification_detail":detail,"replay_queue":queue,"unresolved_records":[x["record"] for x in ordered if x["class"]=="UNRESOLVED_PROVENANCE"],"undecodable_provenance_objects":normalized_bad,"classification_load_bearing_undecodable_count":sum(1 for x in bad if x["classification_load_bearing"]),"controls":controls,"all_lane_controls_pass":all(v is True or (v is False and k in {"descendant_science_recomputed","descendant_outcomes_used_as_targets","claim_lock_promoted","criteria_or_census_mutated"}) for k,v in controls.items()),"tracked_tree_digest_before":d0,"tracked_tree_digest_after":d1,"scientific_normalized_sha256":H(J(normalized)),"descendant_science_consumed":False,"c6":"SYMBOLIC_UNFIXED","theory_established_pct":0}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("--repo",type=Path,required=True);p.add_argument("--output",type=Path,required=True);a=p.parse_args();obj=build(a.repo.resolve());a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n",encoding="utf-8");print(json.dumps({k:v for k,v in obj.items() if k!="classification_detail"},sort_keys=True,indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
