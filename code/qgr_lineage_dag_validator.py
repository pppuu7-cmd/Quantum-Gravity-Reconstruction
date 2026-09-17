#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; HEX=re.compile(r'^[0-9a-f]{40}$')
def validate(dag:dict,root:Path=ROOT,verify_git=True):
    errors=[]; nodes=dag.get('nodes',[]); ids=[n.get('id') for n in nodes]
    if len(ids)!=len(set(ids)):errors.append('duplicate lineage node id')
    known=set(ids); graph={i:[] for i in known}
    for n in nodes:
      nid=n.get('id'); sha=n.get('authority_sha','')
      if not HEX.match(str(sha)):errors.append(f'{nid}: malformed authority sha')
      if verify_git and HEX.match(str(sha)):
        if subprocess.run(['git','-C',str(root),'cat-file','-e',sha+'^{commit}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode:errors.append(f'{nid}: nonexistent authority commit {sha}')
      for field in ('depends_on','supersedes','preserves','invalidates','requires_replay_of','does_not_affect'):
        for ref in n.get(field,[]):
          if ref not in known:errors.append(f'{nid}:{field} missing node {ref}')
      graph[nid]=list(n.get('depends_on',[]))+list(n.get('supersedes',[]))
      if n.get('supersedes') and not n.get('status','').startswith(('PASS','TERMINAL')):errors.append(f'{nid}: silent/nonterminal supersession')
    color={k:0 for k in graph}
    def dfs(v):
      color[v]=1
      for w in graph[v]:
        if color[w]==1:return True
        if color[w]==0 and dfs(w):return True
      color[v]=2;return False
    if any(color[v]==0 and dfs(v) for v in graph):errors.append('lineage dependency cycle')
    for item in dag.get('protected_historical_files',[]):
      path=item['path'] if isinstance(item,dict) else item; expected=item.get('terminal_commit') if isinstance(item,dict) else None
      if not (root/path).exists():errors.append(f'protected historical file missing: {path}');continue
      if expected:
        latest=subprocess.check_output(['git','-C',str(root),'log','-1','--format=%H','--',path],text=True).strip()
        if latest!=expected:errors.append(f'historical result mutated: {path}: latest={latest} expected={expected}')
    return {'valid':not errors,'errors':errors,'node_count':len(nodes)}
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--dag',default=str(ROOT/'protocol/QGR_SCIENTIFIC_LINEAGE_DAG.json'));ap.add_argument('--output');a=ap.parse_args(argv)
    out=validate(json.loads(Path(a.dag).read_text()));txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['valid'] else 1
if __name__=='__main__':raise SystemExit(main())
