#!/usr/bin/env python3
import json,math

# Translation on L2(R): in Fourier space (U_a f)^hat(k)=exp(i k a) fhat(k).
# For every nonzero a, sup_k |exp(i k a)-1| = 2 (take k=pi/a), so
# ||U_a-I||_op=2 even as a->0. Nevertheless U_a -> I strongly on every L2 state.
# This demonstrates that full operator-norm/diamond convergence can be too strong for
# continuous one-particle representations; a dense-domain strong criterion can be appropriate.
vals=[]
for a in [1.0,0.5,0.1,0.01]:
    k=math.pi/a
    witness=abs(complex(math.cos(k*a),math.sin(k*a))-1)
    assert abs(witness-2.0)<1e-14
    vals.append({'a':a,'k_witness':k,'spectral_distance':witness})

out={
  'gate':'ITER009-G5-STRONG-VS-NORM',
  'translation_witnesses':vals,
  'operator_norm_difference_for_nonzero_translation':2,
  'strong_continuity_statement':'U_a -> I strongly on L2 as a->0 although operator norm stays 2',
  'classification':'PASS_SCOPED_FULL_OPERATOR_NORM_CONVERGENCE_IS_NOT_NECESSARY_FOR_A_PHYSICALLY_MEANINGFUL_STRONG_REFINEMENT_LIMIT_AND_MAY_FAIL_FOR_CONTINUOUS_UNITARY_REPRESENTATIONS',
  'guard':'This mathematical counterexample does not itself prove the QGR branch representation has a strong limit; that requires state-domain control such as the packet audit.'
}
print(json.dumps(out,sort_keys=True))
