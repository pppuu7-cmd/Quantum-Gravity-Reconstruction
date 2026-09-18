#!/usr/bin/env python3
"""Static independence/source-lock audit for the frozen covariant Weyl^3 gate."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json
from pathlib import Path
PREREG="8c21ee233423deaff52d0fa552c027fa065a53a7"
PANEL_FREEZE="1642dc7ca4204a4240635be68522f1731c8a9c50"
PANEL_GENERATOR="03377afec95801b5a49f47b85ddd9c9bf3326ac0"
PANEL_SHA="f1390bc406d0db37fe10cc908db51c2eabcf5105904e4a71cc707d2dd3137c5f"

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def imports(src):
 t=ast.parse(src);out=[]
 for n in ast.walk(t):
  if isinstance(n,ast.Import):out += [a.name for a in n.names]
  elif isinstance(n,ast.ImportFrom):out.append(n.module or "")
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--researcher',required=True);ap.add_argument('--critic',required=True);ap.add_argument('--panel',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
 rs=Path(a.researcher).read_text();cs=Path(a.critic).read_text();ps=Path(a.panel).read_text();ri=imports(rs);ci=imports(cs)
 localr=[x for x in ri if x.startswith('qgr_')];localc=[x for x in ci if x.startswith('qgr_')]
 forbidden_tokens=('isclose','allclose','abs(diff)','1e-','float(')
 controls={'researcher_only_shared_local_import_is_neutral_panel':localr==['qgr_covariant_weyl3_panel'],'critic_only_shared_local_import_is_neutral_panel':localc==['qgr_covariant_weyl3_panel'],'researcher_contains_no_critic_reference':'CRITIC_INDEPENDENT_COVARIANT_EULER_SOURCE' not in rs,'critic_contains_no_researcher_reference':'RESEARCHER_DIRECT_VARIATION_IBP' not in cs,'researcher_no_historical_science_helper_import':not any('qgr_iter' in x for x in ri),'critic_no_historical_science_helper_import':not any('qgr_iter' in x for x in ci),'researcher_exact_no_tolerance_pattern':not any(x in rs for x in forbidden_tokens),'critic_exact_no_tolerance_pattern':not any(x in cs for x in forbidden_tokens),'authority_constants_present_both':all(x in rs and x in cs for x in (PREREG,PANEL_FREEZE,PANEL_GENERATOR)),'panel_generator_contains_no_science_function_definitions':not any(isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and any(tok in n.name.lower() for tok in ('riemann','ricci','weyl','curvature','euler','variation','ibp')) for n in ast.walk(ast.parse(ps)))}
 spec=importlib.util.spec_from_file_location('qgr_covariant_weyl3_panel',a.panel);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);m=mod.panel_manifest()
 controls.update({'panel_manifest_sha256_exact':m.get('panel_sha256')==PANEL_SHA,'panel_cell_count_six':len(m.get('cells',[]))==6,'panel_each_has_700_metric_and_150_h_entries':all(x.get('g_entries')==700 and x.get('h_entries')==150 for x in m.get('cells',[]))})
 payload={'gate':'COVARIANT_WEYL3_DIRECTIONAL_VARIATION_FUNCTIONAL_DERIVATIVE_CERTIFICATE','classification':'PASS_STATIC_INDEPENDENCE_AND_SOURCE_LOCK_AUDIT' if all(controls.values()) else 'BLOCKED_STATIC_INDEPENDENCE_OR_SOURCE_LOCK_FAILURE','controls':controls,'panel_manifest':m,'source_sha256':{'researcher':sha(a.researcher),'critic':sha(a.critic),'panel':sha(a.panel)},'researcher_imports':ri,'critic_imports':ci}
 payload['payload_sha256']=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest();Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n');print(json.dumps(payload,sort_keys=True,indent=2));return 0 if all(controls.values()) else 2
if __name__=='__main__':raise SystemExit(main())
