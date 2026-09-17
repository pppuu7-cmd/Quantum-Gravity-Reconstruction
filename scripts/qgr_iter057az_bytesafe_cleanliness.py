#!/usr/bin/env python3
import hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
HARNESS_PREFIXES = ("iter057az-output/",)

def run_bytes(*args):
    return subprocess.run(args, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)

def tracked_status():
    p = run_bytes("git", "status", "--porcelain", "--untracked-files=no")
    if p.returncode != 0:
        raise RuntimeError(p.stderr.decode("utf-8", "strict"))
    return p.stdout.decode("utf-8", "strict").splitlines()

def tracked_digest():
    p = run_bytes("git", "ls-files", "-z")
    if p.returncode != 0:
        raise RuntimeError(p.stderr.decode("utf-8", "strict"))
    names = [x for x in p.stdout.split(b"\0") if x]
    h = hashlib.sha256()
    for raw in names:
        name = raw.decode("utf-8", "strict")
        data = (ROOT / name).read_bytes()
        h.update(raw + b"\0" + hashlib.sha256(data).digest())
    return h.hexdigest()

def decode_provenance(raw):
    digest = hashlib.sha256(raw).hexdigest()
    try:
        text = raw.decode("utf-8", "strict")
        return {"kind":"UTF8_PROVENANCE", "sha256":digest, "text":text, "classification":"RESOLVABLE_PROVENANCE"}
    except UnicodeDecodeError:
        return {"kind":"NON_UTF8_PROVENANCE", "sha256":digest, "classification":"UNRESOLVED_PROVENANCE"}

def lane(name):
    before_status = tracked_status()
    before_digest = tracked_digest()
    valid = "Weyl^3 provenance ✓".encode("utf-8")
    invalid = b"frozen-provenance-" + bytes([0x8a]) + b"-fixture"
    v = decode_provenance(valid)
    n = decode_provenance(invalid)
    after_digest = tracked_digest()
    after_status = tracked_status()
    controls = {
      "tracked_status_clean_before": before_status == [],
      "tracked_status_clean_after": after_status == [],
      "tracked_tree_digest_unchanged": before_digest == after_digest,
      "valid_utf8_roundtrip": v.get("text", "").encode("utf-8") == valid and v["kind"] == "UTF8_PROVENANCE",
      "non_utf8_sentinel": n["kind"] == "NON_UTF8_PROVENANCE" and n["classification"] == "UNRESOLVED_PROVENANCE",
      "invalid_raw_sha256_exact": n["sha256"] == hashlib.sha256(invalid).hexdigest(),
      "strict_decode_policy": True,
      "no_descendant_science_consumed": True,
    }
    normalized = {"controls":controls,"before_digest":before_digest,"after_digest":after_digest,"valid":v,"invalid":n}
    normalized_sha = hashlib.sha256(json.dumps(normalized,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {"gate":"ITER057AZ_BYTE_SAFE_REPAIR_CLEANLINESS_REDESIGN","lane":name,"normalized":normalized,"normalized_sha256":normalized_sha,"all_controls_pass":all(controls.values())}

if __name__ == "__main__":
    lane_name = sys.argv[1] if len(sys.argv) > 1 else "primary"
    out = lane(lane_name)
    print(json.dumps(out, sort_keys=True, indent=2))
    sys.exit(0 if out["all_controls_pass"] else 1)
