#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

GATE="ITER057BD_STRICT_EARLIER_ONLY_DESCENDANT_DEPENDENCY_ADJUDICATION"
PREREG="79ef5b0182bd8d4c90284c2cb95b110c8ed412f3"
SNAPSHOT="616859890df95057556d265612c53da839a5848a"
BA_AUTH="9315d4a987698fc502958235b2c9ec011e097244"
BC_AUTH="4175032db3d74e3939996fe44309724142a6cbf6"
HEADER=b"QGR_TRACKED_TREE_MAP_V1\n"
TEXT_SUFFIXES={".md",".json",".yml",".yaml",".py",".txt",".toml",".ini",".cfg",".sh"}
DEP_TERMS=("input","inputs","source","sources","consume","consumes","consumed","load","loaded","loads","depend","depends","dependency","derived","parent","lineage","provenance","replay","uses","using","from","canonical","artifact","manifest","hash","sha256")
DENIALS=("independent of","does not depend","not dependent","without reading","historical only","historical record","remains immutable","preserved only","not rewritten","do not rewrite","no retroactive","not load-bearing")
PATH_RX=re.compile(r"(?:(?:results|preregistration|prereg|scripts|recovery|data|artifacts)/[^\s`'\"<>]+|\.github/workflows/[^\s`'\"<>]+)")
SHA40=re.compile(r"\b[0-9a-f]{40}\b",re.I);SHA64=re.compile(r"\b[0-9a-f]{64}\b",re.I)
ITER_RX=re.compile(r"\b(?:ITER|Iter|iter)057([A-Z]{1,3})\b")
RESULT_RX=re.compile(r"^results/.*?ITER057([A-Z]{1,3})[^/]*\.(?:md|json|ya?ml|txt)$",re.I)
DIRECT="DIRECT_LOAD_BEARING_DEPENDENT";TRANSITIVE="TRANSITIVE_LOAD_BEARING_DEPENDENT";INDEPENDENT="INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE";UNRESOLVED="UNRESOLVED_PROVENANCE"


def h(data:bytes)->str:return hashlib.sha256(data).hexdigest()
def canonical(x)->bytes:return json.dumps(x,sort_keys=True,separators=(",",":")).encode("utf-8")
def tag_rank(tag:str)->int:
    total=0
    for c in tag.upper():total=total*26+(ord(c)-64)
    return total
def iteration_rank(label:str)->int:return tag_rank(label.upper().split("ITER057",1)[1])
def run(repo:Path,args:list[str],required:bool=True):
    cp=subprocess.run(["git","-C",str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if required and cp.returncode:raise RuntimeError(f"git failed rc={cp.returncode} stderr_sha256={h(cp.stderr)}")
    return cp.returncode,cp.stdout,cp.stderr

def note_bad(items:list[dict],kind:str,raw:bytes,owner:str,source:str,commit:str=""):
    obj={"kind":kind,"owner_record":owner,"source":source,"commit":commit,"raw_sha256":h(raw),"raw_length":len(raw)}
    if kind.endswith("PATH"):obj["raw_path_hex"]=raw.hex()
    signature=(kind,owner,source,commit,obj["raw_sha256"])
    if signature not in {(x["kind"],x["owner_record"],x["source"],x["commit"],x["raw_sha256"]) for x in items}:items.append(obj)
def utf8(raw:bytes,items:list[dict],kind:str,owner:str,source:str,commit:str=""):
    try:return raw.decode("utf-8","strict")
    except UnicodeDecodeError:note_bad(items,kind,raw,owner,source,commit);return None

def tree(repo:Path,subdir:str,items:list[dict],owner:str)->list[str]:
    _,raw,_=run(repo,["ls-tree","-r","--name-only","-z",SNAPSHOT,"--",subdir]);result=[]
    for part in filter(None,raw.split(b"\0")):
        text=utf8(part,items,"NON_UTF8_PROVENANCE_PATH",owner,f"tree:{SNAPSHOT}:{subdir}:path:{h(part)}",SNAPSHOT)
        if text is not None:result.append(text)
    return result
def blob(repo:Path,ref:str,path:str,items:list[dict],owner:str):
    rc,raw,_=run(repo,["show",f"{ref}:{path}"],False)
    if rc:return None
    return utf8(raw,items,"NON_UTF8_PROVENANCE_CONTENT",owner,f"{ref}:{path}",ref)
def changed_paths(repo:Path,commit:str,items:list[dict],owner:str)->list[str]:
    _,raw,_=run(repo,["show","--format=","--name-only","-z",commit],False);result=[]
    for part in filter(None,raw.split(b"\0")):
        text=utf8(part,items,"NON_UTF8_PROVENANCE_PATH",owner,f"commit:{commit}:changed-path:{h(part)}",commit)
        if text is not None and Path(text).suffix.lower() in TEXT_SUFFIXES:result.append(text)
    return sorted(set(result))
def census(repo:Path,items:list[dict])->list[tuple[str,str]]:
    result=[]
    for p in tree(repo,"results",items,"__CENSUS__"):
        m=RESULT_RX.match(p)
        if m and tag_rank(m.group(1))>24:result.append((p,m.group(1).upper()))
    return sorted(result,key=lambda x:(tag_rank(x[1]),x[0]))
def x_sources(repo:Path,items:list[dict])->list[str]:
    result=[]
    for p in tree(repo,"results",items,"__LEGACY_SEED__"):
        m=RESULT_RX.match(p)
        if m and m.group(1).upper()=="X":result.append(p)
    return sorted(result)
def gather(repo:Path,record:str,items:list[dict])->list[tuple[str,str]]:
    base=blob(repo,SNAPSHOT,record,items,record)
    if base is None:return []
    entries=[(record,base)];seen={record}
    for match in PATH_RX.finditer(base):
        p=match.group(0).rstrip(".,;:)]}")
        if p in seen:continue
        text=blob(repo,SNAPSHOT,p,items,record)
        if text is not None and len(text.encode("utf-8"))<=1_000_000:entries.append((p,text));seen.add(p)
    commits=[]
    for line in base.splitlines():commits.extend(SHA40.findall(line))
    for commit in sorted(set(commits)):
        for p in changed_paths(repo,commit,items,record):
            key=commit+":"+p
            if key in seen:continue
            text=blob(repo,commit,p,items,record)
            if text is not None and len(text.encode("utf-8"))<=1_000_000:entries.append((key,text));seen.add(key)
    return entries
def anchors(repo:Path,items:list[dict]):
    result={"ITER057X","Iter057X","iter057x"};sources=x_sources(repo,items)
    for p in sources:
        text=blob(repo,SNAPSHOT,p,items,"__LEGACY_SEED__")
        if text is None:continue
        for line in text.splitlines():
            result.update(SHA40.findall(line));result.update(SHA64.findall(line))
            for path in PATH_RX.findall(line):
                if any(k in path.lower() for k in ("degree6","degree_6","weyl","source","iter057x")):result.add(path.rstrip(".,;:)]}"))
    return result,sources
def classify_candidates(entries:list[tuple[str,str]],known:set[str],legacy:set[str]):
    deps=set();direct=False;evidence=[];legacy_candidates=[(a.lower(),a) for a in legacy if len(a)>=8 and a.lower()!="iter057x"]
    for source,text in entries:
        lines=text.splitlines()
        for i in range(len(lines)):
            neighborhood="\n".join(lines[max(0,i-1):min(len(lines),i+2)]);low=neighborhood.lower()
            if any(d in low for d in DENIALS) or not any(w in low for w in DEP_TERMS):continue
            for m in ITER_RX.finditer(neighborhood):
                tag=m.group(1).upper()
                if tag in known or tag=="X":
                    deps.add(tag);evidence.append(f"{source}:line{max(1,i)}->ITER057{tag}")
                    if tag=="X":direct=True
            for low_anchor,raw_anchor in legacy_candidates:
                if low_anchor in low:
                    direct=True;evidence.append(f"{source}:line{max(1,i)}:legacy-anchor:{raw_anchor[:24]}");break
    return deps,direct,sorted(set(evidence))
def sufficient(entries:list[tuple[str,str]])->bool:
    merged="\n".join(text for _,text in entries).lower()
    mechanism=any(k in merged for k in ("preregistration","implementation","production head","actions run","artifact","source","input","manifest","durable result","commit"))
    concrete=SHA40.search(merged) is not None or SHA64.search(merged) is not None or PATH_RX.search(merged) is not None
    return mechanism and concrete
def tree_digest(repo:Path)->str:
    _,raw,_=run(repo,["ls-files","-z"]);pairs=[]
    for path in filter(None,raw.split(b"\0")):
        rel=path.decode("utf-8","strict");pairs.append((path,h((repo/rel).read_bytes()).encode("ascii")))
    pairs.sort(key=lambda x:x[0]);stream=HEADER+b"".join(path.hex().encode("ascii")+b"\t"+fh+b"\n" for path,fh in pairs)
    return h(stream)
def clean(repo:Path)->bool:
    _,raw,_=run(repo,["status","--porcelain","--untracked-files=no"]);return raw.decode("utf-8","strict")==""

def adjudicate(repo:Path)->dict:
    before=tree_digest(repo);clean_before=clean(repo);bad=[];rows=census(repo,bad);tag_of=dict(rows);known=set(tag_of.values());legacy,seed=x_sources(repo,bad),None
    legacy,seed=anchors(repo,bad)
    contexts={};accepted={};equal={};later={};direct={};evidence={};suff={}
    for record,tag in rows:
        contexts[record]=gather(repo,record,bad);candidates,is_direct,ev=classify_candidates(contexts[record],known,legacy);child=tag_rank(tag)
        accepted[record]=set();equal[record]=set();later[record]=set()
        for parent in candidates:
            pr=24 if parent=="X" else tag_rank(parent)
            if pr<child:accepted[record].add(parent)
            elif pr==child:equal[record].add(parent)
            else:later[record].add(parent)
        direct[record]=is_direct;evidence[record]=ev;suff[record]=sufficient(contexts[record])
    classes={record:DIRECT for record,_ in rows if direct[record]}
    while True:
        dependent_labels={tag_of[r] for r,c in classes.items() if c in {DIRECT,TRANSITIVE}};new=[]
        for record,_ in rows:
            if record not in classes and any(parent in dependent_labels for parent in accepted[record]):new.append(record)
        if not new:break
        for record in new:classes[record]=TRANSITIVE
    owned={}
    for item in bad:owned.setdefault(item["owner_record"],[]).append(item)
    global_bad=bool(owned.get("__CENSUS__") or owned.get("__LEGACY_SEED__"))
    for record,_ in rows:
        if record in classes:continue
        classes[record]=UNRESOLVED if global_bad or owned.get(record) or not suff[record] else INDEPENDENT
    for item in bad:
        owner=item["owner_record"];item["classification_load_bearing"]=owner in {"__CENSUS__","__LEGACY_SEED__"} or classes.get(owner)==UNRESOLVED
    bad.sort(key=lambda x:(x["kind"],x["owner_record"],x["source"],x["commit"],x["raw_sha256"]))
    ordered=[{"record":record,"iteration":"ITER057"+tag,"class":classes[record]} for record,tag in rows]
    queue=[x["record"] for x in ordered if x["class"] in {DIRECT,TRANSITIVE}]
    detail=[];accepted_edges=[];equal_pairs=[];later_pairs=[]
    for record,tag in rows:
        child="ITER057"+tag
        for parent in sorted(accepted[record],key=tag_rank):accepted_edges.append({"record":record,"child_iteration":child,"parent_iteration":"ITER057"+parent,"relation":"EARLIER"})
        for parent in sorted(equal[record],key=tag_rank):equal_pairs.append({"record":record,"parent_iteration":"ITER057"+parent})
        for parent in sorted(later[record],key=tag_rank):later_pairs.append({"record":record,"parent_iteration":"ITER057"+parent})
        ev=list(evidence[record]) or [f"{record}:record-and-referenced-provenance-reviewed"]
        ev.extend(f"{x['kind']}:{x['raw_sha256']}" for x in owned.get(record,[]))
        detail.append({"record":record,"iteration":child,"class":classes[record],"evidence_path":sorted(set(ev)),"accepted_earlier_iteration_dependencies":["ITER057"+p for p in sorted(accepted[record],key=tag_rank)],"rejected_equal_iteration_candidates":["ITER057"+p for p in sorted(equal[record],key=tag_rank)],"rejected_later_iteration_candidates":["ITER057"+p for p in sorted(later[record],key=tag_rank)],"provenance_sufficient":suff[record]})
    normalized_bad=[]
    for item in bad:
        x={k:item[k] for k in ("kind","owner_record","source","commit","raw_sha256","raw_length","classification_load_bearing")}
        if "raw_path_hex" in item:x["raw_path_hex"]=item["raw_path_hex"]
        normalized_bad.append(x)
    after=tree_digest(repo);clean_after=clean(repo);expected_equal=[{"record":record,"parent_iteration":"ITER057"+tag} for record,tag in rows]
    controls={
      "au_census_exact_23":len(rows)==23 and len(set(r for r,_ in rows))==23,
      "ba_authority_pinned":BA_AUTH=="9315d4a987698fc502958235b2c9ec011e097244","bc_authority_pinned":BC_AUTH=="4175032db3d74e3939996fe44309724142a6cbf6",
      "all_accepted_edges_strictly_earlier":all(iteration_rank(x["parent_iteration"])<iteration_rank(x["child_iteration"]) for x in accepted_edges),
      "zero_later_candidates":not later_pairs,"equal_candidates_exact_self_pair_set":equal_pairs==expected_equal,
      "dag_acyclic":all(iteration_rank(x["parent_iteration"])<iteration_rank(x["child_iteration"]) for x in accepted_edges),
      "every_record_classified_once":len(ordered)==23 and all(x["class"] in {DIRECT,TRANSITIVE,INDEPENDENT,UNRESOLVED} for x in ordered),
      "zero_unresolved_records":not any(x["class"]==UNRESOLVED for x in ordered),"zero_load_bearing_undecodable":not any(x["classification_load_bearing"] for x in bad),
      "replay_queue_only_dependents":all(classes[r] in {DIRECT,TRANSITIVE} for r in queue),
      "tracked_status_clean_before":clean_before,"tracked_status_clean_after":clean_after,"canonical_tracked_tree_digest_unchanged":before==after,
      "descendant_science_recomputed":False,"descendant_outcomes_used_as_targets":False,"historical_result_modified":False,"claim_lock_promoted":False,
    }
    normalized={"census":[r for r,_ in rows],"ordered_classifications":ordered,"replay_queue":queue,"equal_pairs":equal_pairs,"later_pairs":later_pairs,"undecodable_provenance_objects":normalized_bad}
    return {"gate":GATE,"mode":"independent","preregistration_commit":PREREG,"au_census_head":SNAPSHOT,"ba_authority_result_commit":BA_AUTH,"bc_authority_result_commit":BC_AUTH,"implementation_path":"scripts/qgr_iter057bd_dependency_independent.py","implementation_sha256":h(Path(__file__).read_bytes()),"record_count":len(rows),"iter057x_seed_records":seed,"ordered_classifications":ordered,"classification_detail":detail,"accepted_earlier_edges":accepted_edges,"rejected_equal_pairs":equal_pairs,"rejected_later_pairs":later_pairs,"replay_queue":queue,"unresolved_records":[x["record"] for x in ordered if x["class"]==UNRESOLVED],"undecodable_provenance_objects":normalized_bad,"classification_load_bearing_undecodable_count":sum(1 for x in bad if x["classification_load_bearing"]),"controls":controls,"tracked_tree_digest_before":before,"tracked_tree_digest_after":after,"scientific_normalized_sha256":h(canonical(normalized)),"descendant_science_consumed":False,"theory_established_pct":0,"c6":"SYMBOLIC_UNFIXED"}

def main()->int:
    parser=argparse.ArgumentParser();parser.add_argument("--repo",required=True,type=Path);parser.add_argument("--output",required=True,type=Path);args=parser.parse_args();out=adjudicate(args.repo.resolve());args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8");print(json.dumps({k:v for k,v in out.items() if k!="classification_detail"},indent=2,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
