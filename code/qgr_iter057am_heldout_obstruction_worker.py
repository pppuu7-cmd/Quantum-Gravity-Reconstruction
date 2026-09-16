#!/usr/bin/env python3
"""Iter057AM held-out R14 obstruction worker.

Frozen scientific gate: d555671e69d2be898c7cfdd470f072bbb810a0be.
Shard evaluator uses the exact fact that the coordinate-degree-12 directional
Einstein response of a pure degree-12 metric direction depends only on G2.
Fixed controls 0,557,1113 compare this optimized path coefficient-for-coefficient
against the full held-out R12 background finite difference.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ac_tetradecic_einstein_seed_completion as ac
import qgr_iter057ad_branch_obstruction as ad

PREREG='d555671e69d2be898c7cfdd470f072bbb810a0be'
AL_PREREG='c712f5034963048a8ab9a4ad812a47000a89be47'
AL_SHA='5484179f3d86414918d0aed05e4c5a63dca802f4f8f1631c8259e8bf576c9fc5'
AL_CLASS='ADMISSIBLE_EXACT_ITER057AL_R12_BACKGROUND_CANDIDATE'
HELDOUT='AL-R1-4'; NROWS=1456; NCOLS=1114
CONTROL_INDICES=(0,557,1113)


def phash(d):
    q=dict(d); got=q.pop('scientific_payload_sha256',None)
    calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return got,calc,got==calc


def load_authority(path):
    d=json.loads(Path(path).read_text()); got,calc,ok=phash(d)
    c=d.get('candidate',{})
    controls=(ok and got==AL_SHA and d.get('preregistration')==AL_PREREG and
              d.get('classification')==AL_CLASS and c.get('candidate_id')==HELDOUT and
              c.get('J_shape_invariant')=='392/20577' and all(d.get('controls',{}).values()) and
              [int(s['degree']) for s in d.get('stages',[])]==[4,6,8,10,12])
    if not controls: raise RuntimeError('held-out Iter057AL authority mismatch')
    return d,got


def seed2(d):
    r=F(d['candidate']['family_parameter_r']); vals=(r,F(2)-r,F(-2)); q={}
    for axis,v in enumerate(vals,1):
        ex=[0,0,0,0]; ex[axis]=2; q=z.add(q,z.mono(ex,z.K*v))
    g=z.pmat()
    for a in range(4): g[a][a]=z.add(z.const(z.ETA[a]),z.scale(q,-1))
    return g


def full_seed12(d):
    g=seed2(d); pure=True
    for s in d['stages']:
        deg=int(s['degree']); key=f'R{deg}_over_kappa{deg//2}'
        _,p=z.add_trace_reversed_layer(g,s['coefficients'],deg//2,key,deg); pure=pure and p
    return g,pure


def lower_replay(g):
    Ric,Sc,Ein,inv=ac.einstein(g,12); gau=ac.gauge(g)
    ric=sum(bool(z.trunc(Ric[a][b],10)) for a,b in z.PAIRS)
    ein=sum(bool(z.trunc(Ein[a][b],10)) for a,b in z.PAIRS)
    sc=bool(z.trunc(Sc,10)); gg=sum(bool(z.trunc(x,11)) for x in gau)
    return {'inverse_ok':bool(inv),'Ricci_through10_nonzero_count':ric,'scalar_through10_nonzero':sc,
            'Einstein_through10_nonzero_count':ein,'deDonder_through11_nonzero_count':gg,
            'exact_lower_replay':bool(inv and ric==0 and not sc and ein==0 and gg==0)}


def rhs_vector(g,meta14):
    gau=ac.gauge(g); Ric,Sc,Ein,inv=ac.einstein(g,12); out=[]
    for typ,x,al in meta14:
        v=gau[x].get(al,z.F(0)) if typ=='G' else Ein[x[0]][x[1]].get(al,z.F(0))
        out.append(-sp.Rational(v.numerator,v.denominator))
    return sp.Matrix(out),bool(inv)


def structural():
    M12,rows12,meta12,a12,basis=ad.kernel_data()
    if M12.shape!=(4316,4550) or len(basis)!=NCOLS: raise RuntimeError('M12/kernel structure mismatch')
    M14,rows14,meta14,a11,a12_14,a13,a14=ac.system(); L=ad.left_controls(rows14,meta14,a11)
    if M14.shape!=(6790,6800) or L.shape!=(1456,6790) or L*M14!=sp.zeros(1456,6800): raise RuntimeError('R14 left complex mismatch')
    return M12,a12,basis,M14,rows14,meta14,L


def sparse_vec(v): return [[i,str(x)] for i,x in enumerate(v) if x!=0]


def baseline(authority,out):
    d,sha=load_authority(authority); g,pure=full_seed12(d); replay=lower_replay(g)
    M12,a12,basis,M14,rows14,meta14,L=structural()
    kernel_ok=all(not any(M12*sp.Matrix(v)) for v in basis)
    r0,inv=rhs_vector(g,meta14); O0=L*r0
    payload={'gate':'ITER057AM-HELDOUT-NO-REFIT-R14-OBSTRUCTION-TRANSPORT','preregistration':PREREG,
      'mode':'baseline','heldout_candidate':HELDOUT,'heldout_scientific_payload_sha256':sha,
      'heldout_pure_layers':pure,'heldout_lower_replay':replay,
      'M12_shape':list(M12.shape),'kernel_dimension':len(basis),'kernel_exact_annihilation':kernel_ok,
      'M14_shape':list(M14.shape),'L14_shape':list(L.shape),'L14_annihilates_M14':True,
      'r0_inverse_ok':inv,'O0_nonzero_count':sum(x!=0 for x in O0),'O0_nonzero':sparse_vec(O0),
      'controls':{'heldout_authority_exact':True,'heldout_lower_replay_exact':replay['exact_lower_replay'],
        'M12_kernel_exact':kernel_ok,'R14_left_complex_exact':True,'exact_rational_only':True}}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest()
    p=Path(out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k!='O0_nonzero'},indent=2,sort_keys=True)); return 0 if all(payload['controls'].values()) else 2


def shard(authority,start,stop,out):
    d,sha=load_authority(authority); M12,a12,basis,M14,rows14,meta14,L=structural()
    start=max(0,start); stop=min(NCOLS,stop)
    if not (0<=start<stop<=NCOLS): raise RuntimeError('invalid frozen shard range')
    gseed=seed2(d); rseed,invseed=rhs_vector(gseed,meta14)
    controls_here=[i for i in CONTROL_INDICES if start<=i<stop]
    rfull=None
    if controls_here:
        gf,pure=full_seed12(d); rfull,invfull=rhs_vector(gf,meta14)
        if not pure or not invfull: raise RuntimeError('full control background reconstruction failed')
    cols=[]; mismatch=0; kernel_local=True
    for i in range(start,stop):
        v=basis[i]
        if any(M12*sp.Matrix(v)): kernel_local=False; raise RuntimeError('kernel direction failed exact annihilation')
        gs=seed2(d); ad.add_direction(gs,v,a12); ri,invi=rhs_vector(gs,meta14); col=L*(ri-rseed)
        ctrl=None
        if i in controls_here:
            gf,_=full_seed12(d); ad.add_direction(gf,v,a12); rif,invf=rhs_vector(gf,meta14); fullcol=L*(rif-rfull)
            ctrl=bool(invf and fullcol==col)
            if not ctrl:mismatch+=1
        cols.append({'index':i,'nonzero':sparse_vec(col),'optimized_inverse_ok':invi,'direct_full_control_exact':ctrl})
    payload={'gate':'ITER057AM-HELDOUT-NO-REFIT-R14-OBSTRUCTION-TRANSPORT','preregistration':PREREG,
      'mode':'shard','heldout_candidate':HELDOUT,'heldout_scientific_payload_sha256':sha,'lane':[start,stop],
      'column_count':len(cols),'kernel_local_exact_annihilation':kernel_local,'optimized_seed_inverse_ok':invseed,
      'fixed_control_indices_in_lane':controls_here,'direct_full_control_mismatch_count':mismatch,
      'optimization_identity':'degree12 directional R12->R14 Einstein response depends only on G2; fixed full-background finite-difference controls required',
      'columns':cols,'classification':'PARTIAL_EXACT_SHARD_ONLY__NO_ITER057AM_TERMINAL_CLASSIFICATION'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest()
    p=Path(out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    ok=kernel_local and invseed and mismatch==0 and all(x['optimized_inverse_ok'] for x in cols)
    print(json.dumps({k:v for k,v in payload.items() if k!='columns'},indent=2,sort_keys=True)); return 0 if ok else 2


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--authority',required=True);ap.add_argument('--mode',choices=['baseline','shard'],required=True);ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int,default=0);ap.add_argument('--output',required=True);a=ap.parse_args()
    return baseline(a.authority,a.output) if a.mode=='baseline' else shard(a.authority,a.start,a.stop,a.output)
if __name__=='__main__':raise SystemExit(main())
