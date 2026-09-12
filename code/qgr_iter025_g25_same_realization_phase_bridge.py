#!/usr/bin/env python3
"""QGR Iter025 / G25 — same-realization finite-curved phase bridge authority audit.

Frozen scientific question:
Can the already-derived QGR action/source machinery, without adding or fitting a
new event-dependent source law, produce the three physical finite-curved phase
samples required by G24 to identify (K,A,B)?

This audit deliberately distinguishes an action that can evaluate authorized
boundary data from a microscopic rule that supplies those boundary data.
"""
import argparse, json, os
from fractions import Fraction as F

AUDITS=(
    'current-bridge-rank',
    'free-endpoint-collapse',
    'source-map-nonuniqueness',
    'three-probe-source-authority',
)
PATTERNS=((1,1,0,0),(2,1,0,0),(1,1,1,0))


def features(n):
    e2=F(0); p21=F(0); e3=F(0)
    for i in range(4):
        for j in range(i+1,4):
            e2 += F(n[i]*n[j])
            p21 += F(n[i]*n[i]*n[j] + n[i]*n[j]*n[j])
    for i in range(4):
        for j in range(i+1,4):
            for k in range(j+1,4):
                e3 += F(n[i]*n[j]*n[k])
    return (e2,p21,e3)


def rank_fraction(A):
    A=[list(map(F,r)) for r in A]
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
        if r==m: break
    return r


def on_shell_dirichlet_phase(J,lam):
    # G20: r=1+J/(2 lambda). G19 bulk action lambda(r-1)^2.
    # The boundary-source term makes the stationary total action
    # S*=lambda(r-1)^2-J(r-1)=-J^2/(4 lambda).
    dr=J/(2*lam)
    return -J*J/(4*lam), F(1)+dr


def audit_current(lane):
    # G19 fixes the response functional once endpoint/source data are supplied;
    # G20 fixes only the S4 singlet direction, not an event-count -> J coefficient.
    # G23/G24 add no numerical phase datum. Thus the authority Jacobian of existing
    # derived inputs on a general cubic symmetric source map (u,v,w) is zero.
    rows=[[F(0),F(0),F(0)] for _ in range(6)]
    rk=rank_fraction(rows)
    return {
      'gate':'QGR-ITER025-G25-CURRENT-BRIDGE-RANK','audit':'current-bridge-rank','lane':lane,
      'source_map_parameters':['u_e2','v_p21','w_e3'],'current_authority_rank':rk,
      'current_authority_nullity':3-rk,'passed':rk==0,
      'classification':'BLOCKED_SCOPED_EXISTING_QGR_ACTION_AND_SOURCE_RESULTS_HAVE_ZERO_AUTHORITY_RANK_ON_THE_EVENT_COUNT_TO_BOUNDARY_SOURCE_MAP_REQUIRED_TO_GENERATE_G24_PHASE_SAMPLES',
      'guard':'The existing action evaluates supplied boundary/source data; this does not imply that the event-to-source map is zero, only that it is not yet derived.'
    }


def audit_free(lane):
    lam=F(lane+2,lane+5)
    samples=[]; endpoints=[]
    for _ in PATTERNS:
        S,r=on_shell_dirichlet_phase(F(0),lam)
        samples.append(S); endpoints.append(r)
    # With no insertion/source authority G20 selects r=1 for every probe and all
    # finite phase differences collapse to zero, which cannot provide rank-3 data.
    passed=(set(samples)=={F(0)} and set(endpoints)=={F(1)})
    return {
      'gate':'QGR-ITER025-G25-FREE-ENDPOINT-COLLAPSE','audit':'free-endpoint-collapse','lane':lane,
      'lambda':str(lam),'phase_samples':[str(x) for x in samples],
      'endpoints':[str(x) for x in endpoints],'passed':passed,
      'classification':'BLOCKED_SCOPED_WITHOUT_A_DERIVED_EVENT_INSERTION_THE_EXISTING_COMMON_CONFORMAL_ACTION_MAPS_ALL_THREE_G24_PROBES_TO_THE_IDENTITY_ENDPOINT_AND_ZERO_PHASE_DIFFERENCE',
      'guard':'This is a scoped consequence of the G19/G20 common-conformal variational problem, not a theorem that full QGR finite-curved phases vanish.'
    }


def audit_nonunique(lane):
    lam=F(lane+3,lane+7)
    # Two prospectively fixed, exact, S4-symmetric cubic source laws. Both respect
    # the structural source direction found in G20, but existing QGR does not choose
    # their coefficients. They therefore witness nonuniqueness of phase predictions.
    c1=(F(1),F(0),F(0))
    c2=(F(1),F(1,lane+2),F(lane+1,lane+5))
    def phases(c):
        out=[]
        for n in PATTERNS:
            f=features(n); J=sum(f[i]*c[i] for i in range(3))
            S,_=on_shell_dirichlet_phase(J,lam); out.append(S)
        return out
    p1=phases(c1); p2=phases(c2)
    different=(p1!=p2)
    passed=different and c1!=c2
    return {
      'gate':'QGR-ITER025-G25-SOURCE-MAP-NONUNIQUENESS','audit':'source-map-nonuniqueness','lane':lane,
      'lambda':str(lam),'source_law_1':[str(x) for x in c1],'source_law_2':[str(x) for x in c2],
      'phase_vector_1':[str(x) for x in p1],'phase_vector_2':[str(x) for x in p2],
      'passed':passed,
      'classification':'BLOCKED_SCOPED_MULTIPLE_EXACT_S4_SYMMETRIC_EVENT_DEPENDENT_SOURCE_LAWS_ARE_COMPATIBLE_WITH_THE_EXISTING_G19_G20_STRUCTURAL_RESULTS_BUT_PREDICT_DIFFERENT_G24_PHASE_TRIPLES',
      'guard':'These source laws are witnesses of underdetermination, not candidate QGR physics and must not be fitted or promoted.'
    }


def audit_three_probe(lane):
    M=[features(n) for n in PATTERNS]
    rk=rank_fraction(M)
    # A general S4-symmetric count-to-source law through cubic order already needs
    # three coefficients on the G24 basis. Existing symmetry fixes the W4 direction
    # but not these event-dependent scalar weights.
    return {
      'gate':'QGR-ITER025-G25-THREE-PROBE-SOURCE-AUTHORITY','audit':'three-probe-source-authority','lane':lane,
      'feature_matrix':[[str(x) for x in r] for r in M],'rank':rk,
      'undetermined_source_coefficients':3,'passed':rk==3,
      'classification':'BLOCKED_SCOPED_THE_G24_THREE_PROBE_BASIS_IS_FULL_RANK_NOT_ONLY_FOR_ACTION_COEFFICIENTS_BUT_ALSO_FOR_A_GENERIC_S4_SYMMETRIC_EVENT_DEPENDENT_SOURCE_MAP__SYMMETRY_DIRECTION_ALONE_CANNOT_SUPPLY_ITS_THREE_SCALAR_VALUES',
      'guard':'A future microscopic derivation may impose a more restrictive source law, but such a restriction is not present in the current derived QGR authority chain.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=AUDITS,required=True)
    ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); assert 0<=a.lane<6
    fn={'current-bridge-rank':audit_current,'free-endpoint-collapse':audit_free,
        'source-map-nonuniqueness':audit_nonunique,'three-probe-source-authority':audit_three_probe}[a.audit]
    out=fn(a.lane); os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__': main()
