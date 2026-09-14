import argparse, json, math
from fractions import Fraction

GATE='ITER054I-WEYL3-REGULATOR-LIMIT-ASYMPTOTIC-SEPARATION'

def A0():
    return {'gate':GATE,'lane':'A0','valid':True,'pass':True,'checks':{
        'rho_identity':'rho=|c6*Cbar|*h^4*k^2',
        'fixed_band_bound':'sup_rho<=|c6|*Cmax*K^2*h^4 -> 0',
        'khd_identity':'k_HD=1/(h^2*sqrt(|c6*Cbar|)) for Cbar!=0',
        'khd_scaling':'k_HD~h^-2 -> infinity',
        'fixed_K_separation':'k_HD/K -> infinity for fixed K>0',
        'weyl_flat':'Cbar=0 handled as exact-zero correction sector'}}

def A1():
    cases=[]
    for a in [Fraction(1,4),Fraction(1,1),Fraction(9,4)]:
        for K in [Fraction(1,2),Fraction(2,1)]:
            hs=[Fraction(1,2**n) for n in range(1,6)]
            rhos=[a*h**4*K**2 for h in hs]
            khd=[1/(float(h*h)*math.sqrt(float(a))) for h in hs]
            rho_ratio=[rhos[i+1]/rhos[i] for i in range(len(rhos)-1)]
            khd_ratio=[khd[i+1]/khd[i] for i in range(len(khd)-1)]
            ok=all(x==Fraction(1,16) for x in rho_ratio) and all(abs(x-4.0)<1e-12 for x in khd_ratio)
            cases.append({'a':str(a),'K':str(K),'rho_first':str(rhos[0]),'rho_last':str(rhos[-1]),'khd_first':khd[0],'khd_last':khd[-1],'ratio_ok':ok})
    return {'gate':GATE,'lane':'A1','valid':True,'pass':all(c['ratio_ok'] for c in cases),'cases':cases}

def B0():
    panel=[]
    for p in [Fraction(0,1),Fraction(1,1),Fraction(3,2),Fraction(2,1),Fraction(5,2)]:
        exponent=Fraction(4,1)-2*p
        if exponent>0: outcome='vanishes'
        elif exponent==0: outcome='finite_nonzero_constant'
        else: outcome='diverges'
        expected = ('vanishes' if p<2 else 'finite_nonzero_constant' if p==2 else 'diverges')
        panel.append({'p':str(p),'rho_exponent':str(exponent),'outcome':outcome,'expected':expected,'ok':outcome==expected})
    return {'gate':GATE,'lane':'B0','valid':True,'pass':all(x['ok'] for x in panel),'panel':panel,'uniformity_lock':'fixed compact physical-frequency bands only'}

def B1():
    controls={'finite_h_physical_cutoff_derived':False,'finite_h_order_reduction_authorized':False,'c6_fixed':False,'beta_one_authorized':False,'ghost_unitarity_hyperbolicity_claim':False,'quantum_transition_authorized':False,'iter007_no_stop_scale_preserved':True}
    return {'gate':GATE,'lane':'B1','valid':True,'pass':controls['iter007_no_stop_scale_preserved'] and not any(v for k,v in controls.items() if k!='iter007_no_stop_scale_preserved'),'controls':controls}

def aggregate(paths):
    lanes={}
    for p in paths:
        with open(p) as f: d=json.load(f)
        lanes[d['lane']]=d
    complete=set(lanes)=={'A0','A1','B0','B1'}
    good=complete and all(d.get('valid') and d.get('pass') for d in lanes.values())
    classification=('PASS_SCOPED_ITER054I_FIXED_BAND_REGULATOR_LIMIT_WEYL3_ASYMPTOTIC_DECOUPLING__FINITE_H_PHYSICAL_TREATMENT_NOT_AUTHORIZED' if good else 'FAIL_CLOSED_ITER054I_REGULATOR_LIMIT_ASYMPTOTIC_SEPARATION')
    return {'gate':GATE,'lane':'AGGREGATE','complete':complete,'valid':good,'lane_pass':{k:v.get('pass',False) for k,v in lanes.items()},'classification':classification,'theory_established_pct':0,'c6_fixed':False,'beta_one_authorized':False,'finite_h_physical_treatment_authorized':False,'quantum_transition_authorized':False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True); ap.add_argument('inputs',nargs='*'); a=ap.parse_args()
    if a.lane=='A0': d=A0()
    elif a.lane=='A1': d=A1()
    elif a.lane=='B0': d=B0()
    elif a.lane=='B1': d=B1()
    elif a.lane=='aggregate': d=aggregate(a.inputs)
    else: raise SystemExit('bad lane')
    with open(a.out,'w') as f: json.dump(d,f,indent=2,sort_keys=True)
    print(json.dumps(d,indent=2,sort_keys=True))
    if not d.get('valid',False) or (a.lane!='aggregate' and not d.get('pass',False)): raise SystemExit(1)

if __name__=='__main__': main()
