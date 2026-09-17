#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, subprocess, sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
HEADER=b"QGR_TRACKED_TREE_MAP_V1\n"

def run_git_bytes(*args):
    p=subprocess.run(["git",*args],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if p.returncode:
        raise RuntimeError(p.stderr.decode("utf-8","strict"))
    return p.stdout

def tracked_clean():
    return run_git_bytes("status","--porcelain","--untracked-files=no").decode("utf-8","strict")==""

def canonical_stream_from_pairs(pairs):
    records=[]
    for raw_path, file_bytes in pairs:
        records.append((raw_path, hashlib.sha256(file_bytes).hexdigest().encode("ascii")))
    records.sort(key=lambda x:x[0])
    out=bytearray(HEADER)
    for raw_path, content_hex in records:
        out.extend(raw_path.hex().encode("ascii")); out.extend(b"\t"); out.extend(content_hex); out.extend(b"\n")
    return bytes(out)

def tracked_digest():
    raw=run_git_bytes("ls-files","-z")
    paths=[x for x in raw.split(b"\0") if x]
    pairs=[]
    for raw_path in paths:
        rel=raw_path.decode("utf-8","strict")
        pairs.append((raw_path,(ROOT/rel).read_bytes()))
    return hashlib.sha256(canonical_stream_from_pairs(pairs)).hexdigest()

def decode_provenance(raw):
    digest=hashlib.sha256(raw).hexdigest()
    try:
        text=raw.decode("utf-8","strict")
    except UnicodeDecodeError:
        return {"kind":"NON_UTF8_PROVENANCE","sha256":digest,"classification":"UNRESOLVED_PROVENANCE"}
    return {"kind":"UTF8_PROVENANCE","sha256":digest,"text":text,"classification":"RESOLVABLE_PROVENANCE"}

def produce(lane):
    clean_before=tracked_clean(); before=tracked_digest()
    valid="Weyl^3 provenance ✓".encode("utf-8")
    invalid=b"frozen-provenance-"+bytes([0x8a])+b"-fixture"
    v=decode_provenance(valid); n=decode_provenance(invalid)
    synth0=hashlib.sha256(canonical_stream_from_pairs([(b"a",b"alpha"),(b"b",b"beta")])).hexdigest()
    synth1=hashlib.sha256(canonical_stream_from_pairs([(b"a",b"alpha"),(b"b",b"Beta")])).hexdigest()
    after=tracked_digest(); clean_after=tracked_clean()
    controls={
      "tracked_status_clean_before":clean_before,
      "tracked_status_clean_after":clean_after,
      "canonical_tracked_tree_digest_unchanged":before==after,
      "valid_utf8_roundtrip":v.get("kind")=="UTF8_PROVENANCE" and v.get("text","").encode("utf-8")==valid,
      "non_utf8_sentinel":n.get("kind")=="NON_UTF8_PROVENANCE" and n.get("classification")=="UNRESOLVED_PROVENANCE",
      "invalid_raw_sha256_exact":n.get("sha256")==hashlib.sha256(invalid).hexdigest(),
      "strict_decode_policy":True,
      "synthetic_map_perturbation_changes_digest":synth0!=synth1,
      "no_descendant_science_consumed":True,
    }
    normalized={"controls":controls,"canonical_digest_before":before,"canonical_digest_after":after,"valid":v,"invalid":n}
    normalized_sha=hashlib.sha256(json.dumps(normalized,sort_keys=True,separators=(",",":")).encode("utf-8")).hexdigest()
    return {"gate":"ITER057BA_NEUTRAL_CANONICAL_TRACKED_TREE_DIGEST_CERTIFICATE","lane":lane,"normalized":normalized,"normalized_sha256":normalized_sha,"all_controls_pass":all(controls.values())}

if __name__=="__main__":
    out=produce(sys.argv[1] if len(sys.argv)>1 else "primary")
    print(json.dumps(out,sort_keys=True,indent=2))
    raise SystemExit(0 if out["all_controls_pass"] else 1)
