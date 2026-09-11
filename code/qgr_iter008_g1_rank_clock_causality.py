#!/usr/bin/env python3
import argparse,itertools,json,math
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# C=J-I contravariant incidence form; E=C^-1=-I+J/3 covariant response seed.
C=[[0 if i==j else 1 for j in range(4)] for i in range(4)]
E=[[-(1 if i==j else 0)+1/3 for j in range(4)] for i in range(4)]
one=[1,1,1,1]
def quad(M,x):return sum(x[i]*M[i][j]*x[j] for i in range(4) for j in range(4))
clock_covector_norm=quad(C,one)
clock_vector_norm=quad(E,one)
assert abs(clock_covector_norm-12)<1e-12
assert abs(clock_vector_norm-4/3)<1e-12
# Transverse sum-zero sector is 3D and E-negative definite. Test a spanning basis and exact Gram eigenvalues by known formula.
T=[[1,-1,0,0],[1,0,-1,0],[1,0,0,-1]]
Gram=[[sum(T[a][i]*E[i][j]*T[b][j] for i in range(4) for j in range(4)) for b in range(3)] for a in range(3)]
# Gram = -(I+J) in this nonorthogonal basis; eigenvalues -4,-1,-1.
expected=[[-2,-1,-1],[-1,-2,-1],[-1,-1,-2]]
assert all(abs(Gram[i][j]-expected[i][j])<1e-12 for i in range(3) for j in range(3))
# Each Boolean rank level is an antichain: same-rank distinct subsets cannot contain one another.
subsets=[frozenset(s) for r in range(5) for s in itertools.combinations(range(4),r)]
level_sizes=[]
for r in range(5):
 L=[s for s in subsets if len(s)==r];level_sizes.append(len(L))
 for a,b in itertools.combinations(L,2):
  assert not (a<b or b<a)
out={
 'lane':'BOOLEAN_RANK_CLOCK_CAUSALITY',
 'rank_gradient_covector_C_norm':clock_covector_norm,
 'barycentric_vector_E_norm':clock_vector_norm,
 'transverse_sum_zero_dimension':3,
 'transverse_E_Gram':Gram,
 'transverse_Gram_eigenvalues':[-4,-1,-1],
 'rank_level_sizes':level_sizes,
 'all_rank_levels_antichains':True,
 'classification':'PASS_SCOPED_BOOLEAN_RANK_CLOCK_DEFINES_THE_S4_SYMMETRIC_TIMELIKE_DIRECTION_WITH_A_THREE_DIMENSIONAL_NEGATIVE_TRANSVERSE_SECTOR_AND_ANTICHAIN_SLICES',
 'scientific_interpretation':'The unit rank increment has covector (1,1,1,1), the unique S4-symmetric direction already singled out by the incidence form. It is timelike in the (+---) convention. Its sum-zero complement is exactly three-dimensional and negative definite, while fixed-rank Boolean levels are antichains. This gives an intrinsic microscopic 1+3 clock/slice structure without importing continuum time.',
 'guard':'This is a microscopic causal foliation statement. It does not prove global hyperbolicity, observer-independent particle time, or a physical duration for one rank tick.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))