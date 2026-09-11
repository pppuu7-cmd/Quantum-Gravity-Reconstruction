#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);a=P.parse_args()

# Finite exact surrogate for a direct-integral boundary decomposition.
# Boundary superselection/matching label b is shared by both regions.
dA=[2,3,4,5]
dB=[5,2,3,4]
naive=sum(dA)*sum(dB)
relative=sum(x*y for x,y in zip(dA,dB))
forbidden=naive-relative
assert naive==196 and relative==48 and forbidden==148

# Check associative gluing over a common boundary label.
dC=[3,1,2,6]
left=sum(dA[i]*dB[i]*dC[i] for i in range(4))
right=sum(dA[i]*(dB[i]*dC[i]) for i in range(4))
assert left==right

out={
 'lane':'BOUNDARY_RELATIVE_TENSOR_GLUE',
 'finite_boundary_sector_dimensions':{'A':dA,'B':dB,'C':dC},
 'naive_tensor_dimension_AxB':naive,
 'boundary_matched_relative_tensor_dimension_AxB':relative,
 'forbidden_cross_boundary_sector_dimension':forbidden,
 'associative_three_region_matched_dimension':left,
 'continuum_analogue':'H_(A union_F B) = direct_integral_F [ H_A(b) tensor H_B(b) ] dmu_F(b), not H_A tensor H_B with independent boundary copies',
 'classification':'PASS_SCOPED_BOUNDARY_MATCHING_REQUIRES_RELATIVE_TENSOR_DIRECT_SUM_OR_DIRECT_INTEGRAL_STRUCTURE_NOT_NAIVE_INDEPENDENT_TENSOR_PRODUCT',
 'scientific_interpretation':'Once the shared B3 data are one physical boundary variable rather than two copies, the quantum gluing analogue is fiberwise/relative tensoring over the same boundary label. A naive independent tensor product contains cross-boundary sectors b_A != b_B that have no counterpart in the glued configuration fiber product.',
 'guard':'The finite-sector calculation proves the algebraic matching logic, not the exact interacting QGR measure decomposition or a continuum direct-integral theorem. Establishing the physical measure/disintegration remains a separate analytic step.'
}
open(a.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
