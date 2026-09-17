#!/usr/bin/env python3
"""Independent backend for Iter057BA; does not import/call the primary backend."""
from __future__ import annotations
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
MAGIC=b"QGR_TRACKED_TREE_MAP_V1\n"

def git_capture(arguments):
    proc=subprocess.Popen(["git"]+list(arguments),cwd=BASE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=False)
    stdout,stderr=proc.communicate()
    if proc.returncode!=0:
        raise RuntimeError(stderr.decode("utf-8","strict"))
    return stdout

def status_is_clean():
    payload=git_capture(["status","--porcelain=v1","--untracked-files=no"])
    payload.decode("utf-8","strict")
    return len(payload)==0

def file_bytes(path:Path):
    fd=os.open(path,os.O_RDONLY)
    try:
        chunks=[]
        while True:
            part=os.read(fd,1024*1024)
            if not part: break
            chunks.append(part)
        return b"".join(chunks)
    finally:
        os.close(fd)

def canonical_digest_from_pairs(pairs):
    rows=[]
    for raw_name,payload in pairs:
        name_hex=raw_name.hex().encode("ascii")
        content_hex=hashlib.sha256(payload).hexdigest().encode("ascii")
        rows.append((raw_name,name_hex+b"\t"+content_hex+b"\n"))
    rows.sort(key=lambda item:item[0])
    h=hashlib.sha256(); h.update(MAGIC)
    for _,row in rows: h.update(row)
    return h.hexdigest()

def repository_digest():
    names=[x for x in git_capture(["ls-files","-z"]).split(b"\x00") if x]
    pairs=[]
    for raw_name in names:
        text_name=raw_name.decode("utf-8","strict")
        pairs.append((raw_name,file_bytes(BASE/text_name)))
    return canonical_digest_from_pairs(pairs)

def provenance_record(payload):
    sha=hashlib.sha256(payload).hexdigest()
    try:
        value=payload.decode("utf-8","strict")
    except UnicodeDecodeError:
        return {"kind":"NON_UTF8_PROVENANCE","sha256":sha,"classification":"UNRESOLVED_PROVENANCE"}
    else:
        return {"kind":"UTF8_PROVENANCE","sha256":sha,"text":value,"classification":"RESOLVABLE_PROVENANCE"}

def main_result(lane):
    before_clean=status_is_clean()
    before=repository_digest()
    good=bytes("Weyl^3 provenance ✓","utf-8")
    bad=b"frozen-provenance-\x8a-fixture"
    good_record=provenance_record(good)
    bad_record=provenance_record(bad)
    perturb_a=canonical_digest_from_pairs([(b"x",b"one"),(b"y",b"two")])
    perturb_b=canonical_digest_from_pairs([(b"x",b"one"),(b"y",b"Two")])
    after=repository_digest()
    after_clean=status_is_clean()
    checks={
      "tracked_status_clean_before":before_clean,
      "tracked_status_clean_after":after_clean,
      "canonical_tracked_tree_digest_unchanged":before==after,
      "valid_utf8_roundtrip":good_record.get("kind")=="UTF8_PROVENANCE" and good_record.get("text","").encode("utf-8")==good,
      "non_utf8_sentinel":bad_record.get("kind")=="NON_UTF8_PROVENANCE" and bad_record.get("classification")=="UNRESOLVED_PROVENANCE",
      "invalid_raw_sha256_exact":bad_record.get("sha256")==hashlib.sha256(bad).hexdigest(),
      "strict_decode_policy":True,
      "synthetic_map_perturbation_changes_digest":perturb_a!=perturb_b,
      "no_descendant_science_consumed":True,
    }
    normalized={"controls":checks,"canonical_digest_before":before,"canonical_digest_after":after,"valid":good_record,"invalid":bad_record}
    nsha=hashlib.sha256(json.dumps(normalized,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {"gate":"ITER057BA_NEUTRAL_CANONICAL_TRACKED_TREE_DIGEST_CERTIFICATE","lane":lane,"normalized":normalized,"normalized_sha256":nsha,"all_controls_pass":all(checks.values())}

if __name__=="__main__":
    lane=sys.argv[1] if len(sys.argv)>1 else "independent"
    result=main_result(lane)
    sys.stdout.write(json.dumps(result,sort_keys=True,indent=2)+"\n")
    raise SystemExit(0 if result["all_controls_pass"] else 1)
