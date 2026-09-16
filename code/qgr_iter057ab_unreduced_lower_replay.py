#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from itertools import product
import qgr_iter057ab_onshell_q2_q4_q6_q8_q10_response as ab
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa

def encpoly(p):
    return [{'alpha':list(m),'n':c.numerator,'d':c.denominator} for m,c in sorted(p.items())]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
    g,bg,_,_=aa.seed_metric12();gi,G,R,Ric,Sc,Ein,inv=aa.geometry10(g);q,src,auth,subs=ab.consume();u=ab.unreduced_DG(q,g,gi,G,8)
    core={'bgprov':bg,'inv':inv,'auth':auth,'authority_subcontrols':subs,'unreduced_lower':{f'{a}{b}':encpoly(u[a][b]) for a,b in ab.PAIRS}}
    b=json.dumps(core,sort_keys=True,separators=(',',':')).encode();core['payload_sha256']=hashlib.sha256(b).hexdigest()
    p=Path(args.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(core,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'payload_sha256':core['payload_sha256'],'expected':ab.UNRED_LOWER_SHA,'match':core['payload_sha256']==ab.UNRED_LOWER_SHA,'authority_subcontrols':subs},indent=2))
    if core['payload_sha256']!=ab.UNRED_LOWER_SHA or not auth:raise SystemExit(2)
if __name__=='__main__':main()
