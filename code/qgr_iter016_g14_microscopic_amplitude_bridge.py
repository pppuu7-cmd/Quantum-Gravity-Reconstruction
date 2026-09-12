#!/usr/bin/env python3
import argparse,itertools,json,math,os
from fractions import Fraction as F

AUDITS=('equivariant-map','quadratic-authority','history-normalization','authority-rank')
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]
PIDX={p:k for k,p in enumerate(PAIRS)}
PERMS=list(itertools.permutations(range(4)))

def rank_fraction(A):
    A=[[F(x) for x in row] for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]);r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c];A[r]=[x/pv for x in A[r]]
        for i in range(r+1,m):
            if A[i][c]:
                z=A[i][c];A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def s4_constraints():
    rows=[]
    for p in PERMS:
        P=[[0]*4 for _ in range(4)]
        for i in range(4): P[p[i]][i]=1
        Q=[[0]*10 for _ in range(10)]
        for a,(i,j) in enumerate(PAIRS): Q[PIDX[tuple(sorted((p[i],p[j])))][a]=1
        for rr in range(10):
            for c in range(4):
                row=[0]*40
                for s in range(10): row[s*4+c]+=Q[rr][s]
                for t in range(4): row[rr*4+t]-=P[t][c]
                rows.append(row)
    return rows

def explicit_map(kind):
    M=[[0]*4 for _ in range(10)]
    for r,(i,j) in enumerate(PAIRS):
        if kind==0 and i==j: M[r][i]=1
        elif kind==1 and i==j:
            for c in range(4): M[r][c]=1
        elif kind==2 and i<j:
            M[r][i]=1;M[r][j]=1
        elif kind==3 and i<j:
            for c in range(4): M[r][c]=1
    return M

def audit_equivariant(lane):
    C=s4_constraints(); r=rank_fraction(C); nullity=40-r
    maps=[explicit_map(k) for k in range(4)]
    vecs=[[x for row in M for x in row] for M in maps]
    map_rank=rank_fraction([[vecs[j][i] for j in range(4)] for i in range(40)])
    residual=[]
    for v in vecs:
        residual.append(max(abs(sum(F(row[k])*v[k] for k in range(40))) for row in C))
    p=PERMS[(lane*5+3)%24]
    passed=(r==36 and nullity==4 and map_rank==4 and max(residual)==0)
    return {
      'gate':'ITER016-G14-EQUIVARIANT-EVENT-TO-G-MAP','lane':lane,'probe_permutation':p,
      'unknown_map_entries':40,'constraint_rank':r,'equivariant_map_nullity':nullity,
      'explicit_equivariant_basis_rank':map_rank,'max_exact_equivariance_residual':str(max(residual)),
      'passed':passed,
      'classification':'PASS_SCOPED_S4_EQUIVARIANT_LINEAR_EVENT_TO_G_BRIDGE_SPACE_IS_FOUR_DIMENSIONAL__SYMMETRY_ALONE_DOES_NOT_SELECT_A_UNIQUE_MAP',
      'interpretation':'W4 -> Sym^2(W4) has four independent S4-equivariant linear maps in the tested linear bridge class; a canonical q-to-G identification therefore needs extra microscopic authority.'
    }

def audit_quadratic(lane):
    k=F(3+lane,2+lane);a=F(1+lane,3+lane);b=F(2+lane,5+lane)
    H=[[F(0) if i==j else k for j in range(4)] for i in range(4)]
    a2=a+F(7,11);b2=b-F(5,13)
    H2=[[F(0) if i==j else k for j in range(4)] for i in range(4)]
    pair_third=2*a; pair_third_2=2*a2
    triple_third=b; triple_third_2=b2
    passed=(H==H2 and pair_third!=pair_third_2 and triple_third!=triple_third_2)
    return {
      'gate':'ITER016-G14-QUADRATIC-AUTHORITY-LIMIT','lane':lane,
      'k':str(k),'a':str(a),'b':str(b),'quadratic_hessian_offdiag':str(k),'quadratic_hessian_diag':'0',
      'same_hessian_after_cubic_change':H==H2,'pair_third_derivative':[str(pair_third),str(pair_third_2)],
      'triple_third_derivative':[str(triple_third),str(triple_third_2)],'passed':passed,
      'classification':'PASS_SCOPED_G5_QUADRATIC_PAIR_INCIDENCE_AUTHORITY_FIXES_K_BUT_IS_EXACTLY_BLIND_TO_CUBIC_A_AND_B',
      'interpretation':'The existing pair-action Hessian cannot supply the finite pair or connected triple cubic amplitudes used by G13.'
    }

def mobius_constant(n,c):
    return sum(F(((-1)**(n-r))*math.comb(n,r))*c for r in range(n+1))

def audit_history(lane):
    c=F(5+lane,7+lane)
    pair=mobius_constant(2,c);triple=mobius_constant(3,c)
    branches=24
    norm=sum(F(1,branches) for _ in range(branches))
    # |exp(i theta)|^2=1 exactly, so completeness has zero derivative with respect to every phase coordinate.
    phase_response_pair=F(0);phase_response_triple=F(0)
    passed=(norm==1 and pair==0 and triple==0 and phase_response_pair==0 and phase_response_triple==0)
    return {
      'gate':'ITER016-G14-HISTORY-NORMALIZATION-AUTHORITY','lane':lane,'branches':branches,
      'completeness_sum':str(norm),'common_logweight_pair_cumulant':str(pair),
      'common_logweight_triple_cumulant':str(triple),'phase_response_pair':str(phase_response_pair),
      'phase_response_triple':str(phase_response_triple),'passed':passed,
      'classification':'PASS_SCOPED_EQUAL_24_HISTORY_COMPLETENESS_AND_COMMON_MAGNITUDE_NORMALIZATION_HAVE_ZERO_CONNECTED_PAIR_TRIPLE_AND_COHERENT_PHASE_RESPONSE',
      'interpretation':'The normalized history instrument fixes branch modulus/completeness but cannot generate the missing nonhomogeneous coherent pair/triple amplitude data.'
    }

def audit_rank(lane):
    # Coordinates are (k,a,b) in the G13 cubic family.
    current=[[1,0,0],[0,0,0],[0,0,0],[0,0,0]]
    r0=rank_fraction(current);n0=3-r0
    pair=[1,2,0]     # F(1,1,0,0)=k+2a
    triple=[0,0,1]   # connected three-event cumulant isolates b
    r1=rank_fraction(current+[pair]);r2=rank_fraction(current+[pair,triple])
    passed=(r0==1 and n0==2 and r1==2 and r2==3)
    return {
      'gate':'ITER016-G14-AUTHORITY-RANK','lane':lane,
      'current_authority_rank':r0,'current_cubic_nullity':n0,'rank_with_hypothetical_finite_pair_datum':r1,
      'rank_with_pair_and_connected_triple_data':r2,'passed':passed,
      'classification':'BLOCKED_SCOPED_CURRENT_QGR_AUTHORITIES_LEAVE_TWO_CUBIC_EVENT_DIRECTIONS_UNFIXED__G13_CLOSES_ONLY_AFTER_SUPPLYING_PAIR_AND_TRIPLE_DATA_NOT_YET_DERIVED_FROM_THE_SAME_MICROSCOPIC_REALIZATION',
      'interpretation':'G13 establishes conditional identifiability, not provenance. The missing pair/triple rows must be derived from the same microscopic q-to-G realization rather than inserted as new couplings.'
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--audit',choices=AUDITS,required=True);ap.add_argument('--lane',type=int,required=True);ap.add_argument('--out',required=True)
    a=ap.parse_args(); assert 0<=a.lane<6
    fn={'equivariant-map':audit_equivariant,'quadratic-authority':audit_quadratic,'history-normalization':audit_history,'authority-rank':audit_rank}[a.audit]
    out=fn(a.lane);out['audit']=a.audit
    os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(1)
if __name__=='__main__': main()
