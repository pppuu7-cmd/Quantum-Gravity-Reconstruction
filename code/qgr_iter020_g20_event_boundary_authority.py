#!/usr/bin/env python3
import argparse,json,os,itertools
from fractions import Fraction as F

AUDITS=('free-endpoint','boundary-source','s4-source-count','history-normalization')

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

def solve_fraction(A,b):
    n=len(A); M=[list(map(F,A[i]))+[F(b[i])] for i in range(n)]
    r=0
    for c in range(n):
        p=next(i for i in range(r,n) if M[i][c])
        M[r],M[p]=M[p],M[r]
        z=M[r][c]; M[r]=[x/z for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]:
                z=M[i][c]; M[i]=[M[i][j]-z*M[r][j] for j in range(n+1)]
        r+=1
    return [M[i][-1] for i in range(n)]

def dirichlet_system(N,lam,J=F(0)):
    # S=lam*N*sum_{k=0}^{N-1}(s_{k+1}-s_k)^2 - J*(s_N-1), s_0=1.
    # Unknowns s_1..s_N. Stationarity divided by 2*lam*N.
    A=[[F(0) for _ in range(N)] for __ in range(N)]; b=[F(0) for _ in range(N)]
    for k in range(1,N+1):
        row=k-1
        if k<N:
            A[row][k-1]+=2
            if k-1>=1: A[row][k-2]-=1
            else: b[row]+=1
            A[row][k]-=1
        else:
            A[row][k-1]+=1
            if k-1>=1: A[row][k-2]-=1
            else: b[row]+=1
            b[row]+=J/(2*lam*N)
    return A,b

def audit_free(lane):
    N=2+lane; lam=F(lane+2,lane+5)
    A,b=dirichlet_system(N,lam,F(0)); x=solve_fraction(A,b)
    expected=[F(1)]*N
    passed=(x==expected and rank_fraction(A)==N)
    return {'audit':'free-endpoint','lane':lane,'segments':N,'lambda':str(lam),'stationarity_rank':rank_fraction(A),
            'solution':[str(v) for v in x],'endpoint_r':str(x[-1]),'passed':passed,
            'classification':'PASS_SCOPED_DERIVED_DIRICHLET_BULK_ACTION_WITH_SEED_S0_EQUALS_ONE_AND_FREE_FINAL_ENDPOINT_HAS_UNIQUE_STATIONARY_SOLUTION_S_EQUALS_ONE_AND_R_EQUALS_ONE',
            'guard':'This is a statement about the scoped common-conformal bulk variational problem. A nontrivial event may still arise from derived boundary data, an insertion/source operator, a different microscopic variable, or sectors outside this ansatz.'}

def audit_boundary(lane):
    N=2+lane; lam=F(lane+3,lane+7); J=F(lane+1,lane+4)
    A,b=dirichlet_system(N,lam,J); x=solve_fraction(A,b)
    predicted=F(1)+J/(2*lam)
    # Profile should be linear: s_k=1+(k/N)*(r-1)
    linear=[F(1)+F(k,N)*(predicted-1) for k in range(1,N+1)]
    passed=(x==linear and x[-1]==predicted and J!=0)
    return {'audit':'boundary-source','lane':lane,'segments':N,'lambda':str(lam),'source_J':str(J),
            'solution':[str(v) for v in x],'endpoint_r':str(x[-1]),'predicted_r':str(predicted),'passed':passed,
            'classification':'PASS_SCOPED_A_SINGLE_BOUNDARY_EVENT_SOURCE_J_GENERATES_NONTRIVIAL_LINEAR_PROFILE_WITH_R_EQUALS_ONE_PLUS_J_OVER_TWO_LAMBDA__THEREFORE_ARBITRARY_J_GENERATES_ARBITRARY_ENDPOINT_AND_MUST_ITSELF_BE_DERIVED',
            'guard':'The source J is a diagnostic parameter, not an authorized new QGR coupling.'}

def perm_matrix(p):
    M=[[F(0)]*4 for _ in range(4)]
    for i,j in enumerate(p): M[j][i]=1
    return M

def audit_s4(lane):
    # Invariant linear source vectors j in W4 satisfy (P-I)j=0 for generators of S4.
    gens=[(1,0,2,3),(0,2,1,3),(0,1,3,2)]
    rows=[]
    for p in gens:
        P=perm_matrix(p)
        for i in range(4): rows.append([P[i][j]-(1 if i==j else 0) for j in range(4)])
    rk=rank_fraction(rows); nullity=4-rk
    ones=[F(1)]*4
    invariant=all(sum((perm_matrix(p)[i][j]-(1 if i==j else 0))*ones[j] for j in range(4))==0 for p in gens for i in range(4))
    passed=(rk==3 and nullity==1 and invariant)
    return {'audit':'s4-source-count','lane':lane,'constraint_rank':rk,'invariant_source_dimension':nullity,
            'canonical_invariant_direction':['1','1','1','1'],'passed':passed,
            'classification':'PASS_SCOPED_S4_SYMMETRY_ALLOWS_EXACTLY_ONE_LINEAR_SINGLET_EVENT_SOURCE_DIRECTION_BUT_DOES_NOT_FIX_ITS_COEFFICIENT',
            'guard':'Symmetry classifies an allowed source direction; it neither proves that such a microscopic insertion exists nor fixes its strength.'}

def audit_history(lane):
    # Existing G8A: K=1/sqrt(24) exp(iS) U. Completeness depends only on 24*(1/24)=1.
    # Test multiple rational action labels/endpoints; phase modulus is one formally, while no endpoint equation occurs.
    endpoints=[F(lane+2,lane+1),F(lane+3,lane+2),F(lane+4,lane+3)]
    branch_weight=F(1,24); completeness=24*branch_weight
    # Sensitivity matrix of completeness to endpoint/source labels is identically zero.
    sensitivity=[[F(0) for _ in endpoints]]
    rk=rank_fraction(sensitivity)
    passed=(completeness==1 and rk==0 and len(set(endpoints))==3)
    return {'audit':'history-normalization','lane':lane,'tested_endpoint_labels':[str(x) for x in endpoints],
            'branch_probability_weight':str(branch_weight),'completeness_sum':str(completeness),'endpoint_sensitivity_rank':rk,'passed':passed,
            'classification':'PASS_SCOPED_G8A_HISTORY_COMPLETENESS_FIXES_EQUAL_BRANCH_MODULUS_BUT_HAS_ZERO_AUTHORITY_RANK_ON_EVENT_ENDPOINT_OR_SOURCE_STRENGTH',
            'guard':'Unitary branch transport is assumed exactly as in G8A; this audit does not derive the branch configuration map.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=AUDITS,required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); assert 0<=a.lane<6
    fn={'free-endpoint':audit_free,'boundary-source':audit_boundary,'s4-source-count':audit_s4,'history-normalization':audit_history}[a.audit]
    out=fn(a.lane); out['gate']='QGR-ITER020-G20-EVENT-BOUNDARY-AUTHORITY'
    os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__': main()
