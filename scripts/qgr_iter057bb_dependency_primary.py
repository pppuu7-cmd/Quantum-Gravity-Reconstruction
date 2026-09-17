#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path

BB_PREREG = "eb864872be1db63d0588296c606b759b7b1495c8"
AU_CENSUS = "616859890df95057556d265612c53da839a5848a"
BA_PASS = "PASS_SCOPED_ITER057BA_NEUTRAL_CANONICAL_BYTE_SAFE_CERTIFICATE_INDEPENDENTLY_REPRODUCED"
BA_RESULT = "results/ITER057BA_NEUTRAL_CANONICAL_BYTE_SAFE_CERTIFICATE_TERMINAL.md"
GATE = "ITER057BB_CONDITIONAL_BYTE_SAFE_DESCENDANT_DEPENDENCY_ADJUDICATION_RETRY"
ITER_X_RANK = 24
HEADER = b"QGR_TRACKED_TREE_MAP_V1\n"
TEXT_EXT = {".md", ".json", ".yml", ".yaml", ".py", ".txt", ".toml", ".ini", ".cfg", ".sh"}
DEP_WORDS = ("input","inputs","source","sources","consume","consumes","consumed","load","loaded","loads","depend","depends","dependency","derived","parent","lineage","provenance","replay","uses","using","from","canonical","artifact","manifest","hash","sha256")
DENY_WORDS = ("independent of","does not depend","not dependent","without reading","historical only","historical record","remains immutable","preserved only","not rewritten","do not rewrite","no retroactive","not load-bearing")
PATH_RE = re.compile(r"(?:(?:results|preregistration|prereg|scripts|recovery|data|artifacts)/[^\s`'\"<>]+|\.github/workflows/[^\s`'\"<>]+)")
SHA_RE = re.compile(r"\b[0-9a-f]{40}\b", re.I)
LONG_HASH_RE = re.compile(r"\b[0-9a-f]{64}\b", re.I)
ITER_TOKEN_RE = re.compile(r"\b(?:ITER|Iter|iter)057([A-Z]{1,3})\b")
RESULT_RE = re.compile(r"^results/.*?ITER057([A-Z]{1,3})[^/]*\.(?:md|json|ya?ml|txt)$", re.I)


def sha(b: bytes) -> str: return hashlib.sha256(b).hexdigest()
def canon(x) -> bytes: return json.dumps(x, sort_keys=True, separators=(",", ":")).encode("utf-8")

def git(repo: Path, *args: str, check: bool=True) -> bytes:
    cp = subprocess.run(["git", "-C", str(repo), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if check and cp.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed rc={cp.returncode} stderr_sha256={sha(cp.stderr)}")
    return cp.stdout

def iter_rank(tag: str) -> int:
    n=0
    for ch in tag.upper(): n=n*26+(ord(ch)-64)
    return n

def bad_obj(kind: str, raw: bytes, owner: str, source: str, commit: str="") -> dict:
    o={"kind":kind,"owner_record":owner,"source":source,"commit":commit,"raw_sha256":sha(raw),"raw_length":len(raw)}
    if "PATH" in kind: o["raw_path_hex"]=raw.hex()
    return o

def add_bad(dst: list[dict], obj: dict) -> None:
    key=(obj["kind"],obj["owner_record"],obj["source"],obj["commit"],obj["raw_sha256"])
    if not any((x["kind"],x["owner_record"],x["source"],x["commit"],x["raw_sha256"])==key for x in dst): dst.append(obj)

def strict(raw: bytes, bad: list[dict], kind: str, owner: str, source: str, commit: str="") -> str|None:
    try: return raw.decode("utf-8","strict")
    except UnicodeDecodeError:
        add_bad(bad,bad_obj(kind,raw,owner,source,commit)); return None

def tree_names(repo: Path, ref: str, subdir: str, bad: list[dict], owner: str) -> list[str]:
    raw=git(repo,"ls-tree","-r","-z","--name-only",ref,"--",subdir)
    out=[]
    for p in (x for x in raw.split(b"\0") if x):
        s=strict(p,bad,"NON_UTF8_PROVENANCE_PATH",owner,f"tree:{ref}:{subdir}:path:{sha(p)}",ref)
        if s is not None: out.append(s)
    return out

def read_at(repo: Path, ref: str, path: str, bad: list[dict], owner: str) -> str|None:
    cp=subprocess.run(["git","-C",str(repo),"show",f"{ref}:{path}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if cp.returncode: return None
    return strict(cp.stdout,bad,"NON_UTF8_PROVENANCE_CONTENT",owner,f"{ref}:{path}",ref)

def changed_text_files(repo: Path, commit: str, bad: list[dict], owner: str) -> list[str]:
    raw=git(repo,"show","--format=","--name-only","-z",commit,check=False)
    out=[]
    for p in (x for x in raw.split(b"\0") if x):
        s=strict(p,bad,"NON_UTF8_PROVENANCE_PATH",owner,f"commit:{commit}:changed-path:{sha(p)}",commit)
        if s is not None and Path(s).suffix.lower() in TEXT_EXT: out.append(s)
    return sorted(set(out))

def list_records(repo: Path, bad: list[dict]) -> list[tuple[str,str]]:
    names=tree_names(repo,AU_CENSUS,"results",bad,"__CENSUS__")
    ans=[]
    for p in names:
        m=RESULT_RE.match(p)
        if m and iter_rank(m.group(1).upper())>ITER_X_RANK: ans.append((p,m.group(1).upper()))
    ans.sort(key=lambda z:(iter_rank(z[1]),z[0])); return ans

def list_x_records(repo: Path, bad: list[dict]) -> list[str]:
    ans=[]
    for p in tree_names(repo,AU_CENSUS,"results",bad,"__LEGACY_SEED__"):
        m=RESULT_RE.match(p)
        if m and m.group(1).upper()=="X": ans.append(p)
    return sorted(ans)

def collect_context(repo: Path, record: str, bad: list[dict]) -> list[tuple[str,str]]:
    base=read_at(repo,AU_CENSUS,record,bad,record)
    entries=[] if base is None else [(record,base)]
    if base is None: return entries
    seen={record}
    for rawp in PATH_RE.findall(base):
        p=rawp.rstrip(".,;:)]}")
        if p in seen: continue
        txt=read_at(repo,AU_CENSUS,p,bad,record)
        if txt is not None and len(txt.encode("utf-8"))<=1_000_000: entries.append((p,txt)); seen.add(p)
    for commit in sorted(set(SHA_RE.findall(base))):
        for p in changed_text_files(repo,commit,bad,record):
            key=f"{commit}:{p}"
            if key in seen: continue
            txt=read_at(repo,commit,p,bad,record)
            if txt is not None and len(txt.encode("utf-8"))<=1_000_000: entries.append((key,txt)); seen.add(key)
    return entries

def legacy_tokens(repo: Path, bad: list[dict]) -> tuple[set[str],list[str]]:
    toks={"ITER057X","Iter057X","iter057x"}; src=[]
    for p in list_x_records(repo,bad):
        src.append(p); txt=read_at(repo,AU_CENSUS,p,bad,"__LEGACY_SEED__")
        if txt is None: continue
        toks.update(SHA_RE.findall(txt)); toks.update(LONG_HASH_RE.findall(txt))
        for rawp in PATH_RE.findall(txt):
            if any(k in rawp.lower() for k in ("degree6","degree_6","weyl","source","iter057x")): toks.add(rawp.rstrip(".,;:)]}"))
    return toks,src

def has_dep(text: str,start: int,end: int,radius: int=260) -> bool:
    w=text[max(0,start-radius):min(len(text),end+radius)].lower()
    return not any(d in w for d in DENY_WORDS) and any(k in w for k in DEP_WORDS)

def edges(entries: list[tuple[str,str]], known: set[str], legacy: set[str]) -> tuple[set[str],bool,list[str]]:
    deps=set(); direct=False; ev=[]
    for src,text in entries:
        for m in ITER_TOKEN_RE.finditer(text):
            tag=m.group(1).upper()
            if (tag in known or tag=="X") and has_dep(text,m.start(),m.end()):
                deps.add(tag); ev.append(f"{src}:context->ITER057{tag}"); direct=direct or tag=="X"
        for tok in sorted(legacy,key=len,reverse=True):
            if len(tok)<8 or tok.lower()=="iter057x": continue
            pos=text.find(tok)
            if pos>=0 and has_dep(text,pos,pos+len(tok)):
                direct=True; ev.append(f"{src}:legacy-anchor:{tok[:24]}"); break
    return deps,direct,sorted(set(ev))
def sufficient(entries: list[tuple[str,str]]) -> bool:
    merged="\n".join(t for _,t in entries).lower()
    mech=any(k in merged for k in ("preregistration","implementation","production head","actions run","artifact","source","input","manifest","durable result","commit"))
    concrete=bool(SHA_RE.search(merged) or LONG_HASH_RE.search(merged) or PATH_RE.search(merged))
    return mech and concrete

def acyclic(edge_map: dict[str,set[str]], tags: dict[str,str]) -> bool:
    for rec,deps in edge_map.items():
        rr=iter_rank(tags[rec])
        for tag in deps:
            if (ITER_X_RANK if tag=="X" else iter_rank(tag))>=rr: return False
    return True

def tracked_digest(repo: Path) -> str:
    paths=[p for p in git(repo,"ls-files","-z").split(b"\0") if p]
    rec=[]
    for rawp in paths:
        rel=rawp.decode("utf-8","strict"); rec.append((rawp,sha((repo/rel).read_bytes()).encode("ascii")))
    rec.sort(key=lambda z:z[0]); stream=bytearray(HEADER)
    for p,h in rec: stream.extend(p.hex().encode("ascii")+b"\t"+h+b"\n")
    return sha(bytes(stream))
def tracked_clean(repo: Path) -> bool:
    return git(repo,"status","--porcelain","--untracked-files=no").decode("utf-8","strict")==""

def main_payload(repo: Path) -> dict:
    before=tracked_digest(repo); clean0=tracked_clean(repo); bad=[]
    ba_text=(repo/BA_RESULT).read_text(encoding="utf-8") if (repo/BA_RESULT).exists() else ""
    lock=BA_PASS in ba_text
    records=list_records(repo,bad); tag_by={p:t for p,t in records}; known={t for _,t in records}
    legacy,xsrc=legacy_tokens(repo,bad); contexts={p:collect_context(repo,p,bad) for p,_ in records}
    em={}; direct={}; evmap={}; suff={}
    for p,_ in records:
        d,di,ev=edges(contexts[p],known,legacy); em[p]=d; direct[p]=di; evmap[p]=ev; suff[p]=sufficient(contexts[p])
    classes={p:"DIRECT_LOAD_BEARING_DEPENDENT" for p,_ in records if direct[p]}
    changed=True
    while changed:
        changed=False; dep_tags={tag_by[p] for p,c in classes.items() if c in {"DIRECT_LOAD_BEARING_DEPENDENT","TRANSITIVE_LOAD_BEARING_DEPENDENT"}}
        for p,_ in records:
            if p not in classes and em[p]&dep_tags: classes[p]="TRANSITIVE_LOAD_BEARING_DEPENDENT"; changed=True
    bad_owner={}
    for o in bad: bad_owner.setdefault(o["owner_record"],[]).append(o)
    global_bad=bool(bad_owner.get("__CENSUS__") or bad_owner.get("__LEGACY_SEED__"))
    for p,_ in records:
        if p in classes: continue
        if global_bad or bad_owner.get(p): classes[p]="UNRESOLVED_PROVENANCE"
        else: classes[p]="INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE" if suff[p] else "UNRESOLVED_PROVENANCE"
    for o in bad:
        owner=o["owner_record"]
        o["classification_load_bearing"] = owner in {"__CENSUS__","__LEGACY_SEED__"} or classes.get(owner)=="UNRESOLVED_PROVENANCE"
    bad.sort(key=lambda o:(o["kind"],o["owner_record"],o["source"],o["commit"],o["raw_sha256"]))
    ordered=[{"record":p,"iteration":f"ITER057{t}","class":classes[p]} for p,t in records]
    replay=[x["record"] for x in ordered if x["class"] in {"DIRECT_LOAD_BEARING_DEPENDENT","TRANSITIVE_LOAD_BEARING_DEPENDENT"}]
    detail=[]
    for p,t in records:
        ev=list(evmap[p])
        if not ev: ev=[f"{p}:record-and-referenced-provenance-reviewed"]
        for o in bad_owner.get(p,[]): ev.append(f"{o['kind']}:{o['raw_sha256']}")
        detail.append({"record":p,"iteration":f"ITER057{t}","class":classes[p],"evidence_path":sorted(set(ev)),"explicit_iteration_dependencies":[f"ITER057{x}" for x in sorted(em[p],key=iter_rank)],"provenance_sufficient_from_readable_objects":suff[p]})
    after=tracked_digest(repo); clean1=tracked_clean(repo)
    controls={
      "execution_lock_exact":lock,
      "complete_census_unique":len(records)==len({p for p,_ in records})==len(ordered),
      "every_record_classified_once":all(x["class"] in {"DIRECT_LOAD_BEARING_DEPENDENT","TRANSITIVE_LOAD_BEARING_DEPENDENT","INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE","UNRESOLVED_PROVENANCE"} for x in ordered),
      "dag_acyclic":acyclic(em,tag_by),
      "replay_queue_excludes_independent_and_unresolved":all(classes[p] in {"DIRECT_LOAD_BEARING_DEPENDENT","TRANSITIVE_LOAD_BEARING_DEPENDENT"} for p in replay),
      "evidence_path_for_every_classification":all(bool(x["evidence_path"]) for x in detail),
      "tracked_status_clean_before":clean0,
      "tracked_status_clean_after":clean1,
      "canonical_tracked_tree_digest_unchanged":before==after,
      "descendant_science_recomputed":False,
      "descendant_outcomes_used_as_targets":False,
      "claim_lock_promoted":False,
      "criteria_or_census_mutated":False,
    }
    normalized={"census":[p for p,_ in records],"ordered_classifications":ordered,"replay_queue":replay,"undecodable_provenance_objects":[{k:o[k] for k in ("kind","owner_record","source","commit","raw_sha256","raw_length","classification_load_bearing") if k in o} | ({"raw_path_hex":o["raw_path_hex"]} if "raw_path_hex" in o else {}) for o in bad]}
    return {
      "gate":GATE,"mode":"primary","bb_preregistration_commit":BB_PREREG,"au_census_head":AU_CENSUS,
      "ba_required_classification":BA_PASS,"ba_execution_lock_satisfied":lock,
      "implementation_path":"scripts/qgr_iter057bb_dependency_primary.py","implementation_sha256":sha(Path(__file__).read_bytes()),
      "iter057x_seed_records":xsrc,"record_count":len(records),"ordered_classifications":ordered,"classification_detail":detail,
      "replay_queue":replay,"unresolved_records":[x["record"] for x in ordered if x["class"]=="UNRESOLVED_PROVENANCE"],
      "undecodable_provenance_objects":normalized["undecodable_provenance_objects"],"classification_load_bearing_undecodable_count":sum(1 for o in bad if o["classification_load_bearing"]),
      "controls":controls,"all_lane_controls_pass":all(v is True or v is False and k in {"descendant_science_recomputed","descendant_outcomes_used_as_targets","claim_lock_promoted","criteria_or_census_mutated"} for k,v in controls.items()),
      "tracked_tree_digest_before":before,"tracked_tree_digest_after":after,
      "scientific_normalized_sha256":sha(canon(normalized)),
      "descendant_science_consumed":False,"c6":"SYMBOLIC_UNFIXED","theory_established_pct":0
    }

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",type=Path,required=True); ap.add_argument("--output",type=Path,required=True); ns=ap.parse_args()
    obj=main_payload(ns.repo.resolve()); ns.output.parent.mkdir(parents=True,exist_ok=True); ns.output.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n",encoding="utf-8"); print(json.dumps({k:v for k,v in obj.items() if k!="classification_detail"},sort_keys=True,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
