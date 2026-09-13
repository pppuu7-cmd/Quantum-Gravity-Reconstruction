#!/usr/bin/env python3
import json, os
import sympy as sp
import qgr_iter049_weyl3_spherical_variational as s49

r=s49.r; R=sp.Rational
GATE='ITER051C-D2Z-EXACT-SPHERICAL-ZERO-CONDITIONING'

fv=2+r/R(8)+r**2/R(12)
nv=1+r/R(5)
sv=R(3,2)+r+r**3/R(50)
rv=R(6,5)

try:
    auth=s49.authority(); EF0,EN0,ES0=auth[7],auth[8],auth[9]
    EF=sp.cancel(sp.together(s49.prof(EF0,fv,nv,sv)))
    EN=sp.cancel(sp.together(s49.prof(EN0,fv,nv,sv)))
    ES=sp.cancel(sp.together(s49.prof(ES0,fv,nv,sv)))
    num,den=map(sp.factor,sp.fraction(ES))
    poly=sp.Poly(num,r)
    roots=sp.nroots(poly,n=50,maxsteps=300)
    positive=[]
    for z in roots:
        zr=sp.re(z); zi=sp.im(z)
        if abs(float(sp.N(zi,30)))<1e-25 and float(sp.N(zr,30))>0:
            positive.append(sp.N(zr,45))
    positive=sorted(positive,key=lambda z:float(z))
    r0=min(positive,key=lambda z:abs(float(z)-float(rv))) if positive else None
    dES=sp.diff(ES,r)
    vals=[sp.simplify(x.subs(r,rv)) for x in (EF,EN,ES)]
    dec=[sp.N(x,45) for x in vals]
    d_at=sp.N(dES.subs(r,rv),45)
    d_root=sp.N(dES.subs(r,r0),45) if r0 is not None else None
    dist=abs(float(r0)-float(rv)) if r0 is not None else None
    kappa=float(abs(sp.N(rv*dES.subs(r,rv)/ES.subs(r,rv),45)))
    amp=float(abs(dec[2])/max(abs(dec[0]),abs(dec[1])))
    simple=(r0 is not None and abs(float(d_root))>1e-30)
    confirmed=bool(r0 is not None and dist<=0.1 and simple and kappa>=100 and amp<=1e-3)
    cls='DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_CONFIRMED' if confirmed else 'DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_NOT_CONFIRMED'
    out={
      'gate':GATE,'classification':cls,'profile':'D2_B3_EXACT','witness_radius':'6/5',
      'ES_expression':str(ES),'ES_numerator_factorized':str(num),'ES_denominator_factorized':str(den),
      'ES_numerator_degree':int(sp.degree(num,r)),'ES_denominator_degree':int(sp.degree(den,r)),
      'exact_EF_EN_ES_at_6_over_5':[str(x) for x in vals],
      'decimal_EF_EN_ES_at_6_over_5':[str(x) for x in dec],
      'positive_real_numerator_roots':[str(x) for x in positive],
      'nearest_positive_root':str(r0) if r0 is not None else None,
      'distance_to_6_over_5':dist,'dES_dr_at_6_over_5':str(d_at),
      'dES_dr_at_nearest_root':str(d_root) if d_root is not None else None,
      'root_simple_nonzero_derivative':simple,'radial_relative_condition_kappa':kappa,
      'angular_to_large_component_amplitude_ratio':amp,
      'frozen_criteria':{'root_distance_max':0.1,'kappa_min':100.0,'amplitude_ratio_max':1e-3},
      'control_valid':True,'c6_status':'SYMBOLIC_UNFIXED',
      'interpretation_lock':'EXACT_REDUCED_COMPONENT_CONDITIONING_ONLY; D2 FAIL UNCHANGED; D2N STILL REQUIRED; FULL_EOM_NOT_ESTABLISHED; THEORY_ESTABLISHED_0'
    }
except Exception as e:
    out={'gate':GATE,'classification':'ITER051C_D2Z_IMPLEMENTATION_INVALID','control_valid':False,'error':repr(e),'c6_status':'SYMBOLIC_UNFIXED'}

os.makedirs('iter051c-d2z-output',exist_ok=True)
with open('iter051c-d2z-output/result.json','w') as f: json.dump(out,f,sort_keys=True,indent=2)
print(json.dumps(out,sort_keys=True))
if out['classification']=='ITER051C_D2Z_IMPLEMENTATION_INVALID': raise SystemExit(3)
if out['classification']=='DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_NOT_CONFIRMED': raise SystemExit(2)
