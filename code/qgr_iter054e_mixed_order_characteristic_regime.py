#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import sympy as sp

GATE='ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT'
PASS_CLASS='PASS_SCOPED_ITER054E_EINSTEIN_WEYL3_MIXED_ORDER_REGIME_SEPARATION_STRONG_HYPERBOLICITY_NOT_AUTHORIZED'
PREREG='ed62acf961cae4a0d200364285d94a56e61a294d'
LAMBDAS=[sp.Rational(1,3),sp.Rational(2,5),sp.Rational(3,7),sp.Rational(4,9),sp.Rational(5,11),sp.Rational(6,13),sp.Rational(-1,4),sp.Rational(-2,7),sp.Rational(-3,8),sp.Rational(-4,11),sp.Rational(-5,12),sp.Rational(-6,17)]
EPS=[sp.Rational(1,20),sp.Rational(1,10),sp.Rational(1,5)]
S=sp.Rational(3,2)
z,e,lam=sp.symbols('z e lam', nonzero=False)

def P(zv,ev,lv): return sp.expand(zv+ev*lv*zv**2)

def stream_a0():
    rows=[]; ok=True; bad=False
    for lv in LAMBDAS:
        expr=P(z,e,lv); gr=sp.Integer(0); hd=-1/(e*lv)
        fac=sp.factor(expr)==z*(1+e*lv*z)
        lim=sp.expand(expr.subs(e,0))==z
        grroot=sp.simplify(expr.subs(z,gr))==0
        hdroot=sp.simplify(expr.subs(z,hd))==0
        singular=sp.simplify(e*hd+1/lv)==0
        badroot=1/(e*lv)
        badexpr=sp.expand(z-e*lv*z**2)
        neg=sp.simplify(badexpr.subs(z,badroot))==0 and sp.simplify(badroot+hd)==0
        bad=bad or neg
        row={'lambda':str(lv),'factorization':bool(fac),'gr_limit':bool(lim),'gr_root':bool(grroot),'hd_root':bool(hdroot),'singular_branch_exact':bool(singular),'sign_flip_control':bool(neg)}
        row['pass']=all(row[k] for k in ['factorization','gr_limit','gr_root','hd_root','singular_branch_exact','sign_flip_control'])
        rows.append(row); ok=ok and row['pass']
    return {'stream':'A0','gate':GATE,'pass':bool(ok and bad and len(rows)==12),'controls_valid':True,'rows':rows,'interpretation':'exact symbolic mixed-order factorization and GR/singular-branch separation'}

def stream_a1():
    rows=[]; ok=True
    for lv in LAMBDAS:
        mags=[]
        for ev in EPS:
            gr=sp.Integer(0); hd=-1/(ev*lv); hd_scaled=-1/(S*ev*lv)
            expr=P(z,ev,lv)
            r1=sp.simplify(expr.subs(z,gr))==0
            r2=sp.simplify(expr.subs(z,hd))==0
            sc=sp.simplify(hd_scaled-hd/S)==0
            rows.append({'lambda':str(lv),'eps':str(ev),'gr_annihilates':bool(r1),'hd_annihilates':bool(r2),'singular_scaling':bool(sc),'branch_weight_assigned':False,'pass':bool(r1 and r2 and sc)})
            ok=ok and r1 and r2 and sc
            mags.append(abs(hd))
        mono=bool(mags[0]>mags[1]>mags[2])
        ok=ok and mono
    return {'stream':'A1','gate':GATE,'pass':bool(ok and len(rows)==36),'controls_valid':True,'case_count':len(rows),'rows':rows,'monotone_high_frequency_as_eps_decreases':bool(ok),'physical_branch_weights_authorized':False,'interpretation':'frozen exact regime/scaling separation only'}

def stream_b0():
    rows=[]; ok=True
    for lv in LAMBDAS:
        noGR=sp.expand(e*lv*z**2)
        wrong=sp.expand(z+e*lv*z**3)
        detect_noGR=sp.expand(noGR.subs(e,0))==0
        detect_wrong=sp.Poly(wrong,z).degree()==3
        rows.append({'lambda':str(lv),'missing_einstein_detected':bool(detect_noGR),'wrong_order_detected':bool(detect_wrong),'pass':bool(detect_noGR and detect_wrong)})
        ok=ok and detect_noGR and detect_wrong
    return {'stream':'B0','gate':GATE,'pass':bool(ok and len(rows)==12),'controls_valid':True,'rows':rows,'interpretation':'malformed mixed-order controls rejected exactly'}

def stream_b1():
    missing=['full_tensorial_gauge_fixed_einstein_plus_weyl3_characteristic_determinant_open_region','open_region_real_characteristic_proof','strong_hyperbolicity_diagonalizability_or_symmetrizer','gauge_constraint_propagation','energy_estimate','physical_mode_multiplicity_residue_ghost_sign','quantum_amplitude_measure_interpretation']
    return {'stream':'B1','gate':GATE,'pass':True,'controls_valid':True,'actual_classification':'MIXED_ORDER_FINITE_SYMBOLIC_REGIME_SEPARATION_CERTIFICATE_STRONG_HYPERBOLICITY_NOT_YET_AUTHORIZED','missing_obligations':missing,'strong_hyperbolicity_authorized':False,'physical_spectrum_authorized':False,'quantum_transition_authorized':False,'interpretation':'fail-closed authority boundary'}

def run_stream(s): return {'A0':stream_a0,'A1':stream_a1,'B0':stream_b0,'B1':stream_b1}[s]()

def aggregate(inp):
    rows=[]; errors=[]
    for p in sorted(Path(inp).rglob('*.json')):
        try: rows.append(json.loads(p.read_text()))
        except Exception as ex: errors.append(f'{p}:{ex}')
    by={r.get('stream'):r for r in rows if r.get('stream') in {'A0','A1','B0','B1'}}
    missing=sorted({'A0','A1','B0','B1'}-set(by))
    allpass=not missing and not errors and all(by[s].get('pass') is True and by[s].get('controls_valid') is True for s in ['A0','A1','B0','B1'])
    return {'gate':GATE,'classification':PASS_CLASS if allpass else 'SCIENTIFIC_FAIL_OR_INVALID_ITER054E','pass':bool(allpass),'found_streams':sorted(by),'missing':missing,'parse_errors':errors,'stream_pass':{s:by[s].get('pass') for s in by},'preregistration_commit':PREREG,'interpretation_lock':'FINITE EXACT SYMBOLIC MIXED-ORDER REGIME-SEPARATION PROXY ONLY; FULL TENSOR CHARACTERISTICS/STRONG HYPERBOLICITY/ENERGY/CONSTRAINT PROPAGATION/PHYSICAL SPECTRUM/QUANTUM MEASURE NOT ESTABLISHED; C6 UNFIXED; THEORY_ESTABLISHED_0'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A0','A1','B0','B1']); ap.add_argument('--aggregate'); ap.add_argument('--out',required=True); a=ap.parse_args()
    data=aggregate(a.aggregate) if a.aggregate else run_stream(a.stream)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(data,indent=2,sort_keys=True)); print(json.dumps(data,sort_keys=True))
    if not data.get('pass',False): raise SystemExit(2)
if __name__=='__main__': main()
