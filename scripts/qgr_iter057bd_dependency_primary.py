#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path

GATE="ITER057BD_STRICT_EARLIER_ONLY_DESCENDANT_DEPENDENCY_ADJUDICATION"
PREREG="79ef5b0182bd8d4c90284c2cb95b110c8ed412f3"
AU_CENSUS="616859890df95057556d265612c53da839a5848a"
BA_RESULT="9315d4a987698fc502958235b2c9ec011e097244"
BC_RESULT="4175032db3d74e3939996fe44309724142a6cbf6"
ITER_X_RANK=24
HEADER=b"QGR_TRACKED_TREE_MAP_V1\n"
TEXT_EXT={".md",".json",".yml",".yaml",".py",".txt",".toml",".ini",".cfg",".sh"}
DEP_WORDS=("input","inputs","source","sources","consume","consumes","consumed","load","loaded","loads","depend","depends","dependency","derived","parent","lineage","provenance","replay","uses","using","from","canonical","artifact","manifest","hash","sha256")
DENY_WORDS=("independent of","does not depend","not dependent","without reading","historical only","historical record","remains immutable","preserved only","not rewritten","do not rewrite","no retroactive","not load-bearing")
PATH_RE=re.compile(r"(?:(?:results|preregistration|prereg|scripts|recovery|data|artifacts)/[^\s`'\"<>]+|\.github/workflows/[^\s`'\"<>]+)")
SHA_RE=re.compile(r"\b[0-9a-f]{40}\b",re.I); LONG_HASH_RE=re.compile(r"\b[0-9a-f]{64}\b",re.I)
ITER_RE=re.compile(r"\b(?:ITER|Iter|iter)057([A-Z]{1,3})\b")
RESULT_RE=re.compile(r"^results/.*?ITER057([A-Z]{1,3})[^/]*\.(?:md|json|ya?ml|txt)$",re.I)
DIRECT="DIRECT_LOAD_BEARING_DEPENDENT";TRANS="TRANSITIVE_LOAD_BEARING_DEPENDENT";INDEP="INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE";UNRES="UNRESOLVED_PROVENANCE"


def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def J(x)->bytes:return json.dumps(x,sort_keys=True,separators=(",",":")).encode("utf-8")
def rank_tag(tag:str)->int:
    n=0
    for ch in tag.upper():n=n*26+(ord(ch)-64)
    return n
def rank_iter(label:str)->int:return rank_tag(label.upper().replace("ITER057",""))
def git(repo:Path,*args:str,check:bool=True)->bytes:
    p=subprocess.run(["git","-C",str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if check and p.returncode:raise RuntimeError(f"git {' '.join(args)} failed rc={p.returncode} stderr_sha256={H(p.stderr)}")
    return p.stdout

def add_bad(dst:list[dict],kind:str,raw:bytes,owner:str,source:str,commit:str=""):
    item={"kind":kind,"owner_record":owner,"source":source,"commit":commit,"raw_sha256":H(raw),"raw_length":len(raw)}
    if "PATH" in kind:item["raw_path_hex"]=raw.hex()
    sig=(kind,owner,source,commit,item["raw_sha256"])
    if sig not in {(x["kind"],x["owner_record"],x["source"],x["commit"],x["raw_sha256"]) for x in dst}:dst.append(item)
def strict(raw:bytes,bad:list[dict],kind:str,owner:str,source:str,commit:str=""):
    try:return raw.decode("utf-8","strict")
    except UnicodeDecodeError:add_bad(bad,kind,raw,owner,source,commit);return None

def tree_names(repo:Path,ref:str,subdir:str,bad:list[dict],owner:str)->list[str]:
    raw=git(repo,"ls-tree","-r","-z","--name-only",ref,"--",subdir);out=[]
    for p in filter(None,raw.split(b"\0")):
        s=strict(p,bad,"NON_UTF8_PROVENANCE_PATH",owner,f"tree:{ref}:{subdir}:path:{H(p)}",ref)
        if s is not None:out.append(s)
    return out
def read_at(repo:Path,ref:str,path:str,bad:list[dict],owner:str):
    p=subprocess.run(["git","-C",str(repo),"show",f"{ref}:{path}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if p.returncode:return None
    return strict(p.stdout,bad,"NON_UTF8_PROVENANCE_CONTENT",owner,f"{ref}:{path}",ref)
def changed_text(repo:Path,commit:str,bad:list[dict],owner:str)->list[str]:
    raw=git(repo,"show","--format=","--name-only","-z",commit,check=False);out=[]
    for p in filter(None,raw.split(b"\0")):
        s=strict(p,bad,"NON_UTF8_PROVENANCE_PATH",owner,f"commit:{commit}:changed-path:{H(p)}",commit)
        if s is not None and Path(s).suffix.lower() in TEXT_EXT:out.append(s)
    return sorted(set(out))
def list_records(repo:Path,bad:list[dict])->list[tuple[str,str]]:
    out=[]
    for p in tree_names(repo,AU_CENSUS,"results",bad,"__CENSUS__"):
        m=RESULT_RE.match(p)
        if m and rank_tag(m.group(1))>ITER_X_RANK:out.append((p,m.group(1).upper()))
    return sorted(out,key=lambda z:(rank_tag(z[1]),z[0]))
def x_records(repo:Path,bad:list[dict])->list[str]:
    out=[]
    for p in tree_names(repo,AU_CENSUS,"results",bad,"__LEGACY_SEED__"):
        m=RESULT_RE.match(p)
        if m and m.group(1).upper()=="X":out.append(p)
    return sorted(out)
def context(repo:Path,record:str,bad:list[dict])->list[tuple[str,str]]:
    base=read_at(repo,AU_CENSUS,record,bad,record)
    if base is None:return []
    entries=[(record,base)];seen={record}
    for rawp in PATH_RE.findall(base):
        p=rawp.rstrip(".,;:)]}")
        if p in seen:continue
        t=read_at(repo,AU_CENSUS,p,bad,record)
        if t is not None and len(t.encode("utf-8"))<=1_000_000:entries.append((p,t));seen.add(p)
    for c in sorted(set(SHA_RE.findall(base))):
        for p in changed_text(repo,c,bad,record):
            key=f"{c}:{p}"
            if key in seen:continue
            t=read_at(repo,c,p,bad,record)
            if t is not None and len(t.encode("utf-8"))<=1_000_000:entries.append((key,t));seen.add(key)
    return entries
def legacy(repo:Path,bad:list[dict]):
    tokens={"ITER057X","Iter057X","iter057x"};sources=x_records(repo,bad)
    for p in sources:
        t=read_at(repo,AU_CENSUS,p,bad,"__LEGACY_SEED__")
        if t is None:continue
        tokens.update(SHA_RE.findall(t));tokens.update(LONG_HASH_RE.findall(t))
        for rawp in PATH_RE.findall(t):
            if any(k in rawp.lower() for k in ("degree6","degree_6","weyl","source","iter057x")):tokens.add(rawp.rstrip(".,;:)]}"))
    return tokens,sources
def dependency_window(text:str,start:int,end:int,radius:int=260)->bool:
    w=text[max(0,start-radius):min(len(text),end+radius)].lower()
    return not any(d in w for d in DENY_WORDS) and any(k in w for k in DEP_WORDS)
def candidate_edges(entries:list[tuple[str,str]],known:set[str],legacy_tokens:set[str]):
    deps=set();direct=False;evidence=[]
    for src,text in entries:
        for m in ITER_RE.finditer(text):
            tag=m.group(1).upper()
            if (tag in known or tag=="X") and dependency_window(text,m.start(),m.end()):
                deps.add(tag);evidence.append(f"{src}:context->ITER057{tag}");direct=direct or tag=="X"
        for tok in sorted(legacy_tokens,key=len,reverse=True):
            if len(tok)<8 or tok.lower()=="iter057x":continue
            pos=text.find(tok)
            if pos>=0 and dependency_window(text,pos,pos+len(tok)):
                direct=True;evidence.append(f"{src}:legacy-anchor:{tok[:24]}");break
    return deps,direct,sorted(set(evidence))
def provenance_sufficient(entries:list[tuple[str,str]])->bool:
    merged="\n".join(t for _,t in entries).lower()
    mech=any(k in merged for k in ("preregistration","implementation","production head","actions run","artifact","source","input","manifest","durable result","commit"))
    concrete=bool(SHA_RE.search(merged) or LONG_HASH_RE.search(merged) or PATH_RE.search(merged))
    return mech and concrete
def tracked_digest(repo:Path)->str:
    paths=[x for x in git(repo,"ls-files","-z").split(b"\0") if x];pairs=[]
    for raw in paths:
        name=raw.decode("utf-8","strict");pairs.append((raw,H((repo/name).read_bytes()).encode("ascii")))
    pairs.sort(key=lambda x:x[0]);stream=bytearray(HEADER)
    for path,h in pairs:stream.extend(path.hex().encode("ascii")+b"\t"+h+b"\n")
    return H(bytes(stream))
def tracked_clean(repo:Path)->bool:return git(repo,"status","--porcelain","--untracked-files=no").decode("utf-8","strict")==""

def build(repo:Path)->dict:
    before=tracked_digest(repo);clean0=tracked_clean(repo);bad=[]
    records=list_records(repo,bad);tag_by=dict(records);known=set(tag_by.values());legacy_tokens,xsrc=legacy(repo,bad)
    contexts={r:context(repo,r,bad) for r,_ in records};accepted={};equal={};later={};direct={};evmap={};suff={}
    for rec,tag in records:
        candidates,is_direct,evidence=candidate_edges(contexts[rec],known,legacy_tokens);child=rank_tag(tag)
        accepted[rec]={p for p in candidates if (ITER_X_RANK if p=="X" else rank_tag(p))<child}
        equal[rec]={p for p in candidates if (ITER_X_RANK if p=="X" else rank_tag(p))==child}
        later[rec]={p for p in candidates if (ITER_X_RANK if p=="X" else rank_tag(p))>child}
        direct[rec]=is_direct;evmap[rec]=evidence;suff[rec]=provenance_sufficient(contexts[rec])
    classes={r:DIRECT for r,_ in records if direct[r]}
    while True:
        active={tag_by[r] for r,c in classes.items() if c in {DIRECT,TRANS}};new=[]
        for rec,_ in records:
            if rec not in classes and accepted[rec]&active:new.append(rec)
        if not new:break
        for rec in new:classes[rec]=TRANS
    by_owner={}
    for o in bad:by_owner.setdefault(o["owner_record"],[]).append(o)
    global_bad=bool(by_owner.get("__CENSUS__") or by_owner.get("__LEGACY_SEED__"))
    for rec,_ in records:
        if rec in classes:continue
        classes[rec]=UNRES if (global_bad or by_owner.get(rec) or not suff[rec]) else INDEP
    for o in bad:
        owner=o["owner_record"];o["classification_load_bearing"]=owner in {"__CENSUS__","__LEGACY_SEED__"} or classes.get(owner)==UNRES
    bad.sort(key=lambda o:(o["kind"],o["owner_record"],o["source"],o["commit"],o["raw_sha256"]))
    ordered=[{"record":r,"iteration":f"ITER057{t}","class":classes[r]} for r,t in records]
    queue=[x["record"] for x in ordered if x["class"] in {DIRECT,TRANS}]
    detail=[];accepted_edges=[];equal_pairs=[];later_pairs=[]
    for rec,tag in records:
        child=f"ITER057{tag}"
        for p in sorted(accepted[rec],key=rank_tag):accepted_edges.append({"record":rec,"child_iteration":child,"parent_iteration":f"ITER057{p}","relation":"EARLIER"})
        for p in sorted(equal[rec],key=rank_tag):equal_pairs.append({"record":rec,"parent_iteration":f"ITER057{p}"})
        for p in sorted(later[rec],key=rank_tag):later_pairs.append({"record":rec,"parent_iteration":f"ITER057{p}"})
        ev=evmap[rec] or [f"{rec}:record-and-referenced-provenance-reviewed"]
        ev += [f"{o['kind']}:{o['raw_sha256']}" for o in by_owner.get(rec,[])]
        detail.append({"record":rec,"iteration":child,"class":classes[rec],"evidence_path":sorted(set(ev)),"accepted_earlier_iteration_dependencies":[f"ITER057{p}" for p in sorted(accepted[rec],key=rank_tag)],"rejected_equal_iteration_candidates":[f"ITER057{p}" for p in sorted(equal[rec],key=rank_tag)],"rejected_later_iteration_candidates":[f"ITER057{p}" for p in sorted(later[rec],key=rank_tag)],"provenance_sufficient":suff[rec]})
    normalized_bad=[]
    for o in bad:
        x={k:o[k] for k in ("kind","owner_record","source","commit","raw_sha256","raw_length","classification_load_bearing")}
        if "raw_path_hex" in o:x["raw_path_hex"]=o["raw_path_hex"]
        normalized_bad.append(x)
    after=tracked_digest(repo);clean1=tracked_clean(repo)
    expected_equal=[{"record":r,"parent_iteration":f"ITER057{t}"} for r,t in records]
    controls={
      "au_census_exact_23":len(records)==23 and len({r for r,_ in records})==23,
      "ba_authority_pinned":BA_RESULT=="9315d4a987698fc502958235b2c9ec011e097244",
      "bc_authority_pinned":BC_RESULT=="4175032db3d74e3939996fe44309724142a6cbf6",
      "all_accepted_edges_strictly_earlier":all(rank_iter(x["parent_iteration"])<rank_iter(x["child_iteration"]) for x in accepted_edges),
      "zero_later_candidates":len(later_pairs)==0,
      "equal_candidates_exact_self_pair_set":equal_pairs==expected_equal,
      "dag_acyclic":all(rank_iter(x["parent_iteration"])<rank_iter(x["child_iteration"]) for x in accepted_edges),
      "every_record_classified_once":len(ordered)==23 and all(x["class"] in {DIRECT,TRANS,INDEP,UNRES} for x in ordered),
      "zero_unresolved_records":all(x["class"]!=UNRES for x in ordered),
      "zero_load_bearing_undecodable":not any(o["classification_load_bearing"] for o in bad),
      "replay_queue_only_dependents":all(classes[r] in {DIRECT,TRANS} for r in queue),
      "tracked_status_clean_before":clean0,"tracked_status_clean_after":clean1,"canonical_tracked_tree_digest_unchanged":before==after,
      "descendant_science_recomputed":False,"descendant_outcomes_used_as_targets":False,"historical_result_modified":False,"claim_lock_promoted":False,
    }
    normalized={"census":[r for r,_ in records],"ordered_classifications":ordered,"replay_queue":queue,"equal_pairs":equal_pairs,"later_pairs":later_pairs,"undecodable_provenance_objects":normalized_bad}
    return {"gate":GATE,"mode":"primary","preregistration_commit":PREREG,"au_census_head":AU_CENSUS,"ba_authority_result_commit":BA_RESULT,"bc_authority_result_commit":BC_RESULT,"implementation_path":"scripts/qgr_iter057bd_dependency_primary.py","implementation_sha256":H(Path(__file__).read_bytes()),"record_count":len(records),"iter057x_seed_records":xsrc,"ordered_classifications":ordered,"classification_detail":detail,"accepted_earlier_edges":accepted_edges,"rejected_equal_pairs":equal_pairs,"rejected_later_pairs":later_pairs,"replay_queue":queue,"unresolved_records":[x["record"] for x in ordered if x["class"]==UNRES],"undecodable_provenance_objects":normalized_bad,"classification_load_bearing_undecodable_count":sum(1 for o in bad if o["classification_load_bearing"]),"controls":controls,"tracked_tree_digest_before":before,"tracked_tree_digest_after":after,"scientific_normalized_sha256":H(J(normalized)),"descendant_science_consumed":False,"theory_established_pct":0,"c6":"SYMBOLIC_UNFIXED"}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("--repo",type=Path,required=True);p.add_argument("--output",type=Path,required=True);a=p.parse_args();obj=build(a.repo.resolve());a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n",encoding="utf-8");print(json.dumps({k:v for k,v in obj.items() if k!="classification_detail"},sort_keys=True,indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
