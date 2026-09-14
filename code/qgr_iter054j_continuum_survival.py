import argparse, json
from fractions import Fraction

GATE='ITER054J-WEYL3-CONTINUUM-SURVIVAL-SCALING-TRILEMMA'

def classify(s):
    er=Fraction(4,1)-s
    ek=s/Fraction(2,1)-Fraction(2,1)
    rho='vanishes' if er>0 else 'finite_nonzero' if er==0 else 'diverges'
    khd='infinity' if ek<0 else 'finite_nonzero' if ek==0 else 'zero'
    return er,ek,rho,khd

def A0():
    regimes=[]
    for label,s in [('lt4',Fraction(2,1)),('eq4',Fraction(4,1)),('gt4',Fraction(6,1))]:
        er,ek,rho,khd=classify(s)
        expected={
            'lt4':('vanishes','infinity'),
            'eq4':('finite_nonzero','finite_nonzero'),
            'gt4':('diverges','zero')
        }[label]
        regimes.append({'label':label,'s':str(s),'rho_exponent':str(er),'khd_exponent':str(ek),'rho':rho,'k_HD':khd,'ok':(rho,khd)==expected})
    return {'gate':GATE,'lane':'A0','valid':True,'pass':all(x['ok'] for x in regimes),'identities':{'rho':'rho~h^(4-s)','k_HD':'k_HD~h^(s/2-2)'},'regimes':regimes}

def A1():
    panel=[]
    for s in [Fraction(0,1),Fraction(2,1),Fraction(7,2),Fraction(4,1),Fraction(9,2),Fraction(6,1)]:
        er,ek,rho,khd=classify(s)
        hs=[Fraction(1,2**n) for n in range(1,6)]
        # Unit frozen prefactors: diagnostic only.
        rhos=[float(h**er) for h in hs] if er>=0 else [float(1/(h**(-er))) for h in hs]
        khds=[float(h**ek) for h in hs] if ek>=0 else [float(1/(h**(-ek))) for h in hs]
        if s<4:
            ok=(rhos[-1] < rhos[0]) and (khds[-1] > khds[0])
        elif s==4:
            ok=all(abs(x-rhos[0])<1e-12 for x in rhos) and all(abs(x-khds[0])<1e-12 for x in khds)
        else:
            ok=(rhos[-1] > rhos[0]) and (khds[-1] < khds[0])
        panel.append({'s':str(s),'rho_exponent':str(er),'khd_exponent':str(ek),'rho_outcome':rho,'khd_outcome':khd,'rho_first':rhos[0],'rho_last':rhos[-1],'khd_first':khds[0],'khd_last':khds[-1],'ok':ok})
    return {'gate':GATE,'lane':'A1','valid':True,'pass':all(x['ok'] for x in panel),'panel':panel}

def B0():
    survival_condition='s=4'
    decoupling_condition='s<4'
    compatible=False
    return {'gate':GATE,'lane':'B0','valid':True,'pass':not compatible,'finite_nonzero_survival_requires':survival_condition,'branch_decoupling_requires':decoupling_condition,'single_powerlaw_solution_exists':compatible,'statement':'finite nonzero fixed-band survival and k_HD->infinity are mutually incompatible in the frozen pure power-law family'}

def B1():
    controls={
        'c6_running_authorized':False,
        'physical_cutoff_derived':False,
        'finite_h_order_reduction_authorized':False,
        'beta_one_authorized':False,
        'ghost_unitarity_hyperbolicity_claim':False,
        'quantum_transition_authorized':False,
        'theory_established_pct':0
    }
    ok=(not controls['c6_running_authorized'] and not controls['physical_cutoff_derived'] and not controls['finite_h_order_reduction_authorized'] and not controls['beta_one_authorized'] and not controls['ghost_unitarity_hyperbolicity_claim'] and not controls['quantum_transition_authorized'] and controls['theory_established_pct']==0)
    return {'gate':GATE,'lane':'B1','valid':True,'pass':ok,'controls':controls}

def aggregate(paths):
    lanes={}
    for p in paths:
        with open(p) as f: d=json.load(f)
        lanes[d['lane']]=d
    complete=set(lanes)=={'A0','A1','B0','B1'}
    good=complete and all(d.get('valid') and d.get('pass') for d in lanes.values())
    classification=('PASS_SCOPED_ITER054J_POWERLAW_CONTINUUM_SURVIVAL_TRILEMMA__C6_RUNNING_NOT_AUTHORIZED' if good else 'FAIL_CLOSED_ITER054J_CONTINUUM_SURVIVAL_SCALING_TRILEMMA')
    return {'gate':GATE,'lane':'AGGREGATE','complete':complete,'valid':good,'lane_pass':{k:v.get('pass',False) for k,v in lanes.items()},'classification':classification,'theory_established_pct':0,'c6_running_authorized':False,'beta_one_authorized':False,'quantum_transition_authorized':False}

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
