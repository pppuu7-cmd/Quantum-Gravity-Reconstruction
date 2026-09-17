#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,struct
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def build(output:Path):
    m=json.loads((ROOT/'release/QGR_PROGRAMME_BUNDLE_CONTENTS.json').read_text()); parts=[b'QGR_PROGRAMME_BUNDLE_V1\n']
    for rel in sorted(m['files']):
      data=(ROOT/rel).read_bytes(); header=json.dumps({'path':rel,'size':len(data),'sha256':hashlib.sha256(data).hexdigest()},sort_keys=True,separators=(',',':')).encode()
      parts += [struct.pack('>I',len(header)),header,struct.pack('>Q',len(data)),data]
    blob=b''.join(parts);output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(blob);return hashlib.sha256(blob).hexdigest()
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args(argv);s=build(Path(a.output));print(json.dumps({'bundle':a.output,'sha256':s,'size':Path(a.output).stat().st_size},sort_keys=True));return 0
if __name__=='__main__':raise SystemExit(main())
