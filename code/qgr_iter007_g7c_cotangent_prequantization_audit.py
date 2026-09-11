#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Conditional audit: if the current continuous configuration space Q_13 is canonically quantized via T*Q_13,
# the canonical symplectic form omega=d theta is exact. Multiplying by any real kappa keeps it exact.
# Therefore the standard prequantization integrality class [kappa omega/(2 pi hbar)] is zero for every kappa;
# no quantization of kappa follows from this canonical route alone.
kappas=[-10.0,-1.0,-0.2,0.0,0.3,1.0,7.0]
rows=[]
for k in kappas:
    de_rham_class='zero_exact_class'
    integral_over_closed_2cycle=0.0
    rows.append({'kappa':k,'scaled_symplectic_form_exact':True,'de_rham_class':de_rham_class,'closed_2cycle_integral':integral_over_closed_2cycle})
out={
 'lane':'COTANGENT_PREQUANTIZATION_NOFIX',
 'conditional_assumption':'canonical phase space is T*Q_13 with theta=p_i dq^i and omega=dtheta',
 'rows':rows,
 'classification':'FAIL_SCOPED_CANONICAL_COTANGENT_PREQUANTIZATION_INTEGRALITY_CANNOT_QUANTIZE_KAPPA_BECAUSE_THE_SYMPLECTIC_FORM_IS_EXACT',
 'scientific_interpretation':'On a cotangent bundle the canonical symplectic form is globally exact. Scaling it by kappa does not change its zero de Rham cohomology class, so the usual prequantization integrality condition is satisfied for every real kappa and cannot select kappa/hbar. A scale-fixing symplectic mechanism would require additional nontrivial compact/topological microscopic structure not present in the current continuous Q_13 construction.',
 'guard':'The cotangent phase-space assumption is a prospective canonical route, not an already-derived full QGR phase space. This result only kills the naive claim that ordinary cotangent prequantization would automatically quantize kappa.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))