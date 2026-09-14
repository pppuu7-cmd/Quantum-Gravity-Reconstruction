#!/usr/bin/env python3
"""Iter056S exact held-out validation of the balanced B4 pair-tensor cubic bridge."""
from __future__ import annotations
import argparse, itertools, json, os
from pathlib import Path
import sympy as sp

GATE='ITER056S-BALANCED-B4-PAIR-TENSOR-TO-TIDAL-CUBIC-SHAPE-HELDOUT-VALIDATION'
PREREG='f3e0daf1f164953c382753867ccba80852ec8283'
LANES=[
    ('G0',sp.Rational(1),sp.Rational(2)),
    ('G1',sp.Rational(2),sp.Rational(-3)),
    ('G2',sp.Rational(-2),sp.Rational(5)),
    ('G3',sp.Rational(3),sp.Rational(4)),
    ('G4',sp.Rational(5),sp.Rational(-1)),
    ('G5',sp.Rational(7,3),sp.Rational(-2,5)),
    ('H0-shape',sp.Rational(3,2),sp.Rational(3,2)),
    ('cubic-null',sp.Rational(5,3),sp.Rational(-5,3)),
]
TT1=[0,1,-1,-1,1,0]
TT2=[1,0,-1,-1,0,1]
EDGES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
t=sp.Matrix([1,1,1,1])
z=sp.symbols('lambda')
Q=sp.Matrix([
    [1/sp.sqrt(2), 1/sp.sqrt(6), 1/sp.sqrt(12)],
    [-1/sp.sqrt(2), 1/sp.sqrt(6), 1/sp.sqrt(12)],
    [0, -2/sp.sqrt(6), 1/sp.sqrt(12)],
    [0, 0, -3/sp.sqrt(12)],
])
PERMS=list(itertools.permutations(range(4)))

def simp0(x):
    return sp.simplify(x)==0

def make_H(a,b):
    xs=[sp.expand(a*TT1[i]+b*TT2[i]) for i in range(6)]
    H=sp.zeros(4)
    for x,(i,j) in zip(xs,EDGES):
        H[i,j]=x; H[j,i]=x
    return H,xs

def perm_matrix(p):
    P=sp.zeros(4)
    for i in range(4): P[p[i],i]=1
    return P

def rank_pred(a,b):
    vals=[2*a,2*b,-2*(a+b)]
    return sum(1 for v in vals if sp.simplify(v)!=0)

def lane_result(idx):
    label,a,b=LANES[idx]
    H,xs=make_H(a,b)
    balances=[sp.expand(sum(H[i,j] for j in range(4) if j!=i)) for i in range(4)]
    balance_ok=all(simp0(x) for x in balances)
    zero_ok=all(simp0(x) for x in H*t)
    actual_char=sp.expand(H.charpoly(z).as_expr())
    expected_char=sp.expand(z*(z-2*a)*(z-2*b)*(z+2*(a+b)))
    char_ok=simp0(actual_char-expected_char)
    tr1=sp.expand(sp.trace(H)); tr2=sp.expand(sp.trace(H**2)); tr3=sp.expand(sp.trace(H**3))
    expected3=sp.expand(-24*a*b*(a+b))
    cubic_ok=simp0(tr3-expected3)
    trace_ok=simp0(tr1)
    perm_ok=True; perm_fail=[]
    for n,p in enumerate(PERMS):
        P=perm_matrix(p); Hp=sp.simplify(P*H*P.T)
        ok2=simp0(sp.trace(Hp**2)-tr2)
        ok3=simp0(sp.trace(Hp**3)-tr3)
        okt=all(simp0(x) for x in Hp*t)
        if not (ok2 and ok3 and okt):
            perm_ok=False; perm_fail.append(n)
    K=sp.simplify(Q.T*H*Q)
    basis_trace=simp0(sp.trace(K))
    basis2=simp0(sp.trace(K**2)-tr2)
    basis3=simp0(sp.trace(K**3)-tr3)
    expected_det=sp.expand((2*a)*(2*b)*(-2*(a+b)))
    det_ok=simp0(sp.det(K)-expected_det)
    spatial_rank=int(K.rank()); rank_ok=(spatial_rank==rank_pred(a,b))
    h0_ok=True
    if label=='H0-shape':
        ev=[]
        for eig,mult in K.eigenvals().items(): ev += [sp.simplify(eig)]*int(mult)
        ev=sorted(ev,key=lambda x: float(x))
        # a=b=3/2 -> spatial eigenvalues (-6,3,3), exactly 3*(-2,1,1)
        h0_ok=(ev==[sp.Rational(-6),sp.Rational(3),sp.Rational(3)])
    null_ok=True
    if label=='cubic-null': null_ok=(simp0(tr3) and H!=sp.zeros(4))
    Hbad=H.copy(); delta=sp.Rational(1,7); Hbad[0,1]+=delta; Hbad[1,0]+=delta
    neg_ok=any(not simp0(x) for x in Hbad*t)
    passed=all([balance_ok,zero_ok,char_ok,cubic_ok,trace_ok,perm_ok,basis_trace,basis2,basis3,det_ok,rank_ok,h0_ok,null_ok,neg_ok])
    return {
        'gate':GATE,'preregistration_commit':PREREG,'production_sha':os.environ.get('GITHUB_SHA','LOCAL'),
        'mode':'lane','lane':idx,'label':label,'a':str(a),'b':str(b),'edge_values':[str(x) for x in xs],
        'balance_ok':balance_ok,'zero_mode_ok':zero_ok,'characteristic_polynomial_ok':char_ok,
        'trace_zero_ok':trace_ok,'trace_h2':str(tr2),'trace_h3':str(tr3),'expected_trace_h3':str(expected3),
        'cubic_identity_ok':cubic_ok,'all_24_permutations_ok':perm_ok,'permutation_failures':perm_fail,
        'fixed_spatial_basis_trace_ok':basis_trace,'fixed_spatial_basis_h2_ok':basis2,
        'fixed_spatial_basis_h3_ok':basis3,'fixed_spatial_basis_det_ok':det_ok,
        'spatial_rank':spatial_rank,'spatial_rank_ok':rank_ok,'h0_shape_ok':h0_ok,
        'cubic_null_special_ok':null_ok,'unbalanced_negative_control_ok':neg_ok,
        'passed':passed,
        'classification':'LANE_PASS_ITER056S' if passed else 'LANE_FAIL_ITER056S'
    }

def load(inp):
    objs=[]; errs=[]
    for p in sorted(Path(inp).rglob('*.json')):
        try: objs.append(json.loads(p.read_text()))
        except Exception as ex: errs.append(f'{p}:{ex}')
    return objs,errs

def aggregate(inp):
    objs,errs=load(inp)
    lanes=[o for o in objs if o.get('gate')==GATE and o.get('mode')=='lane']
    by={}; dup=[]
    for o in lanes:
        i=o.get('lane')
        if i in by: dup.append(i)
        by[i]=o
    expected=set(range(len(LANES))); got=set(by)
    complete=(got==expected and not dup and not errs)
    preregs={o.get('preregistration_commit') for o in lanes}; shas={o.get('production_sha') for o in lanes}
    provenance=(len(preregs)==1 and PREREG in preregs and len(shas)==1)
    implementation_valid=bool(complete and provenance)
    scientific=bool(implementation_valid and all(by[i].get('passed') is True for i in expected))
    if not implementation_valid: cls='INVALID_IMPLEMENTATION_OR_PROVENANCE_ITER056S'
    elif scientific: cls='PASS_SCOPED_CONDITIONAL_ITER056S_BALANCED_PAIR_SECTOR_HAS_EXACT_TIDAL_CUBIC_SHAPE_BRIDGE'
    else: cls='SCIENTIFIC_FAIL_ITER056S_BALANCED_PAIR_CUBIC_SHAPE_HYPOTHESIS'
    return {
        'gate':GATE,'preregistration_commit':PREREG,'mode':'aggregate','classification':cls,
        'pass':scientific,'implementation_valid':implementation_valid,'complete':complete,
        'parse_errors':errs,'missing_lanes':sorted(expected-got),'duplicates':dup,
        'lane_pass':{str(i):bool(by.get(i,{}).get('passed')) for i in sorted(expected)},
        'claim_ceiling':'CONDITIONAL KINEMATIC BALANCED-PAIR TO TRACELESS-SPATIAL CUBIC-SHAPE BRIDGE ONLY'
    }

def write(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    print(json.dumps(obj,sort_keys=True))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int); ap.add_argument('--aggregate'); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.lane is not None: obj=lane_result(a.lane)
    elif a.aggregate: obj=aggregate(a.aggregate)
    else: raise SystemExit('choose --lane or --aggregate')
    write(a.out,obj)

if __name__=='__main__': main()
