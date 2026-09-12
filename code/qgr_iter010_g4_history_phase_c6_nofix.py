#!/usr/bin/env python3
import cmath,json,math

# Extend the already-established branch phase by a real six-derivative contribution:
# K_alpha = 24^-1/2 exp(i [S2_alpha + c6 S6_alpha]) U_alpha.
# CPTP modulus and additive/projective phase composition remain exact for arbitrary real c6.
c6s=[-3.0,-0.7,0.0,0.2,1.0,math.pi,9.0]
S2=[-0.4,0.1,0.7]
S6=[-0.03,0.0,0.05]
max_mod_error=0.0;max_comp_error=0.0
for c6 in c6s:
    for s2,s6 in zip(S2,S6):
        z=cmath.exp(1j*(s2+c6*s6))/math.sqrt(24.0)
        max_mod_error=max(max_mod_error,abs(abs(z)**2-1.0/24.0))
    a2,a6=S2[0],S6[0];b2,b6=S2[2],S6[2]
    lhs=cmath.exp(1j*((a2+b2)+c6*(a6+b6)))
    rhs=cmath.exp(1j*(b2+c6*b6))*cmath.exp(1j*(a2+c6*a6))
    max_comp_error=max(max_comp_error,abs(lhs-rhs))
assert max_mod_error<1e-15
assert max_comp_error<1e-14
out={
 'gate':'ITER010-G4-HISTORY-PHASE-C6-NOFIX',
 'c6_values_checked':c6s,
 'max_branch_modulus_error':max_mod_error,
 'max_additive_phase_composition_error':max_comp_error,
 'classification':'FAIL_SCOPED_HISTORY_KRAUS_NORMALIZATION_AND_ADDITIVE_PROJECTIVE_PHASE_COMPOSITION_REMAIN_EXACT_FOR_ARBITRARY_REAL_C6_AND_CANNOT_SELECT_ITS_VALUE',
 'guard':'This failure concerns the existing normalization/composition mechanism. An independently derived absolute branch phase on a Weyl-active microscopic background could still determine c6.'
}
print(json.dumps(out,sort_keys=True))
