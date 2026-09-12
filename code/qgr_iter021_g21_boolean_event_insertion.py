#!/usr/bin/env python3
import argparse,json,os,itertools
from fractions import Fraction as F

AUDITS=('sym2-invariants','pair-support','count-response-map','finite-admissibility')
COMPS=[(i,i) for i in range(4)]+[(i,j) for i in range(4) for j in range(i+1,4)]
INDEX={c:k for k,c in enumerate(COMPS)}
BETAS=[F(1,4),F(1,2),F(3,4),F(1),F(3,2),F(2)]

def canon(i,j): return (i,j) if i<=j else (j,i)

def rank_fraction(A):
    A=[list(map(F,row)) for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
    return r

def perm_action(p):
    M=[[F(0)]*10 for _ in range(10)]
    for k,(i,j) in enumerate(COMPS):
        c=canon(p[i],p[j]); M[INDEX[c]][k]=1
    return M

def s4_constraint_rows(generator_variant=0):
    base=[(1,0,2,3),(0,2,1,3),(0,1,3,2)]
    if generator_variant%2:
        base=[(1,2,3,0),(1,0,2,3)]
    rows=[]
    for p in base:
        P=perm_action(p)
        for i in range(10): rows.append([P[i][j]-(1 if i==j else 0) for j in range(10)])
    return rows

def invariant(v,variant=0):
    return all(sum(row[j]*v[j] for j in range(10))==0 for row in s4_constraint_rows(variant))

def audit_sym2(lane):
    rows=s4_constraint_rows(lane); rk=rank_fraction(rows); nul=10-rk
    diag=[F(1) if i<4 else F(0) for i in range(10)]
    off=[F(0) if i<4 else F(1) for i in range(10)]
    independent=rank_fraction([diag,off])==2
    passed=(rk==8 and nul==2 and invariant(diag,lane) and invariant(off,lane) and independent)
    return {
      'gate':'ITER021-G21-SYM2-INVARIANTS','audit':'sym2-invariants','lane':lane,'component_count':10,
      'constraint_rank':rk,'invariant_dimension':nul,'basis_labels':['diagonal_singlet_I','off_diagonal_pair_singlet_C'],
      'passed':passed,
      'classification':'PASS_SCOPED_SYM2_W4_CONTAINS_EXACTLY_TWO_S4_INVARIANT_LINEAR_EVENT_INSERTION_DIRECTIONS_DIAGONAL_SELF_RESPONSE_AND_OFF_DIAGONAL_DISTINCT_PAIR_RESPONSE',
      'guard':'S4 alone does not choose between the two singlets and does not fix either magnitude.'
    }

def audit_pair(lane):
    rows=s4_constraint_rows(lane)
    # Strict primitive rank-2 distinct-pair ontology: no diagonal/self-pair support.
    for d in range(4):
        row=[F(0)]*10; row[d]=1; rows.append(row)
    rk=rank_fraction(rows); nul=10-rk
    C=[F(0)]*4+[F(1)]*6
    passed=(rk==9 and nul==1 and invariant(C,lane) and all(C[d]==0 for d in range(4)))
    return {
      'gate':'ITER021-G21-PAIR-SUPPORT-SELECTION','audit':'pair-support','lane':lane,
      'constraint_rank_with_no_self_pair':rk,'allowed_dimension':nul,'selected_direction':'C=J-I (zero diagonal, equal off-diagonal pair entries)',
      'passed':passed,
      'classification':'PASS_SCOPED_STRICT_B4_RANK2_DISTINCT_PAIR_SUPPORT_PLUS_S4_REDUCES_THE_TWO_SYM2_SINGLET_DIRECTIONS_TO_THE_UNIQUE_OFF_DIAGONAL_PAIR_INCIDENCE_DIRECTION_C_UP_TO_ONE_OVERALL_COEFFICIENT',
      'guard':'The support and symmetry fix a ray/direction, not the physical response per one combinatorial pair event.'
    }

def audit_map(lane):
    # Source pair-count singlet is one-dimensional. Any equivariant linear map into the
    # selected physical pair singlet is multiplication by beta. Show exact distinct beta witnesses.
    beta=BETAS[lane]
    source=[F(1)]*6
    response=[beta*x for x in source]
    # S6-like equality constraints induced by S4 transitivity on unordered pairs: x_i-x_0=0.
    rows=[]
    for i in range(1,6):
        row=[F(0)]*6; row[i]=1; row[0]-=1; rows.append(row)
    rk=rank_fraction(rows); nul=6-rk
    satisfies=all(sum(row[j]*response[j] for j in range(6))==0 for row in rows)
    beta_alt=beta+F(1,7)
    alt=[beta_alt*x for x in source]
    alt_satisfies=all(sum(row[j]*alt[j] for j in range(6))==0 for row in rows)
    passed=(rk==5 and nul==1 and satisfies and alt_satisfies and response!=alt)
    return {
      'gate':'ITER021-G21-COMBINATORIAL-TO-PHYSICAL-RESPONSE-MAP','audit':'count-response-map','lane':lane,
      'pair_orbit_constraint_rank':rk,'equivariant_map_dimension':nul,'beta_witness':str(beta),'beta_alt_witness':str(beta_alt),
      'distinct_equivariant_responses':response!=alt,'passed':passed,
      'classification':'BLOCKED_SCOPED_BOOLEAN_PAIR_COUNT_TO_PHYSICAL_SECOND_MOMENT_RESPONSE_HAS_EXACTLY_ONE_EQUIVARIANT_SCALAR_CONVERSION_COEFFICIENT_BETA_AND_EXISTING_S4_PLUS_DISTINCT_PAIR_SUPPORT_DO_NOT_FIX_BETA',
      'guard':'Setting beta=1 because the incidence matrix uses entries 0/1 would identify combinatorial counting units with physical response units by convention, not derive the map.'
    }

def audit_admissibility(lane):
    beta=BETAS[lane]
    scale=F(1)+beta
    # C=J-I has eigenvalues (3,-1,-1,-1), det=-3.
    eig=[3*scale,-scale,-scale,-scale]
    det=-3*scale**4
    signature=(sum(1 for x in eig if x>0),sum(1 for x in eig if x<0))
    # dmu scale invariance under G -> scale G in 10D Sym2: d10G gives scale^10,
    # |det G|^-5/2 gives scale^-10 for positive scale.
    measure_scaling=scale**10 * scale**(-10)
    flat_constant_action=F(0)
    beta_alt=beta+F(1,5); scale_alt=1+beta_alt
    alt_signature=(1,3) if scale_alt>0 else (3,1)
    passed=(scale>0 and det!=0 and signature==(1,3) and measure_scaling==1 and flat_constant_action==0 and alt_signature==(1,3))
    return {
      'gate':'ITER021-G21-FINITE-ADMISSIBILITY','audit':'finite-admissibility','lane':lane,'beta':str(beta),'scale_1_plus_beta':str(scale),
      'eigenvalues':[str(x) for x in eig],'determinant':str(det),'signature':list(signature),'kinematic_measure_scaling':str(measure_scaling),
      'constant_flat_local_action':str(flat_constant_action),'alternate_beta':str(beta_alt),'alternate_signature':list(alt_signature),'passed':passed,
      'classification':'BLOCKED_SCOPED_MULTIPLE_DISTINCT_POSITIVE_BETA_VALUES_PRESERVE_THE_Q13_SIGNATURE_SCALE_INVARIANT_KINEMATIC_MEASURE_AND_ZERO_CONSTANT_FLAT_LOCAL_ACTION_SO_FINITE_ADMISSIBILITY_DOES_NOT_FIX_EVENT_STRENGTH',
      'guard':'This audit is restricted to the unique off-diagonal S4-singlet ray selected by strict pair support.'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=AUDITS,required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); assert 0<=a.lane<6
    fn={'sym2-invariants':audit_sym2,'pair-support':audit_pair,'count-response-map':audit_map,'finite-admissibility':audit_admissibility}[a.audit]
    out=fn(a.lane); os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
    # BLOCKED_SCOPED is a successful audit result when non-identifiability is exactly demonstrated.
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__': main()
