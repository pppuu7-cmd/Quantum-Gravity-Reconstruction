#!/usr/bin/env python3
"""Iter057AJ exact uniqueness test in the frozen AH parity/S3 sector."""
from __future__ import annotations
import argparse, hashlib, itertools, json, math
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix

import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ag_dual_obstruction_witness as ag

PREREG='1ba092655a159dfa8dea5d9d0832346ff451dda0'
PASS='PASS_SCOPED_ITER057AJ_S3_PARITY_SECTOR_DUAL_CERTIFICATE_UNIQUE_UP_TO_SCALE'
FAIL='SCIENTIFIC_FAIL_SCOPED_ITER057AJ_S3_PARITY_SECTOR_CERTIFICATE_NOT_UNIQUE_AS_PREREGISTERED'
BLOCKED='BLOCKED_ITER057AJ_SYMMETRY_SECTOR_UNIQUENESS_NOT_TECHNICALLY_REALIZED'
INVALID='INVALID_ITER057AJ_FROZEN_AF_AG_AH_AI_AUTHORITY_OR_EXACTNESS_CONTRADICTION'
ROOT=Path(__file__).resolve().parents[1]
AG_DATA=ROOT/'data'/'ITER057AG_CANONICAL_DUAL_WITNESS.json'
AH_DATA=ROOT/'data'/'ITER057AH_DUAL_WITNESS_LOCALIZATION.json'
AI_DATA=ROOT/'data'/'ITER057AI_SINGLE_GENERATOR_COMPRESSION.json'
AG_SHA='5ecb962af9a1265a8846a6d8de4cd0885c2b53bea630a5729a8c069aae9fd9da'
AH_SHA='8e7c74aa9d5c154f5be7fb8bcc8f0db8937e5a605d983ea20bf9fad067b9d661'
AI_SHA='7ffe4d285b366959568a1e4c6503b209710ee15044a8dd363db896c396e2fa24'
NROWS=1456; NCOLS=1114


def qrat(v):
    v=ag.ff(v)
    return sp.Rational(v.numerator,v.denominator)


def primitive_integer(vec):
    vals=[sp.Rational(x) for x in vec]
    den=1
    for x in vals:
        if x: den=math.lcm(den,int(x.q))
    ints=[int(x*den) for x in vals]
    g=0
    for x in ints: g=math.gcd(g,abs(x))
    g=max(g,1); ints=[x//g for x in ints]
    first=next((x for x in ints if x),1)
    if first<0: ints=[-x for x in ints]
    return ints


def sector_and_orbits():
    a11=z.alphas(11); n=len(a11)
    sector=[j for j,a in enumerate(a11) if (a[0]%2,a[1]%2,a[2]%2,a[3]%2)==(1,0,0,0)]
    pos={a11[j]:k for k,j in enumerate(sector)}
    seen=set(); orbits=[]
    for j in sector:
        a=a11[j]
        if a in seen: continue
        orb=sorted(set((a[0],)+p for p in itertools.permutations(a[1:])))
        orb=[q for q in orb if q in pos]
        for q in orb: seen.add(q)
        orbits.append(orb)
    P=sp.MutableSparseMatrix(len(sector),len(orbits),{})
    for c,orb in enumerate(orbits):
        for q in orb: P[pos[q],c]=1
    return a11,sector,pos,orbits,P


def matrix_for_sector(cols,sector):
    loc={idx:k for k,idx in enumerate(sector)}
    data={}
    for branch,d in cols.items():
        for idx,v in d.items():
            k=loc.get(idx)
            if k is not None and v:
                data[(branch,k)]=qrat(v)
    return sp.MutableSparseMatrix(NCOLS,len(sector),data)


def normalized_kernel(Cs,P,sector,O0):
    ns=Cs.nullspace()
    if len(ns)!=1:
        return None,None,None,None
    s=ns[0]
    ysector=P*s
    y=[F(0)]*NROWS
    for k,idx in enumerate(sector): y[idx]=ag.ff(ysector[k])
    norm=sum((ag.ff(O0[i])*y[i] for i in range(NROWS)),F(0))
    if norm==0:
        return y,norm,None,primitive_integer(ysector)
    yn=[v/norm for v in y]
    return y,norm,yn,primitive_integer(ysector)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old-root',required=True);ap.add_argument('--af-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    agd=json.loads(AG_DATA.read_text()); ahd=json.loads(AH_DATA.read_text()); aid=json.loads(AI_DATA.read_text())
    provenance=(agd.get('scientific_payload_sha256')==AG_SHA and ahd.get('scientific_payload_sha256')==AH_SHA and aid.get('scientific_payload_sha256')==AI_SHA and agd.get('classification')==ag.PASS and ahd.get('y_b_support')==[0] and ahd.get('y_parity_support')==[[1,0,0,0]] and ahd.get('spatial_stabilizer_order')==6 and aid.get('classification')=='PASS_SCOPED_ITER057AI_DUAL_CERTIFICATE_COMPRESSES_TO_SINGLE_S3_SCALAR_BIANCHI_GENERATOR')
    recs,cols,lane_controls,coverage,dup=ag.assemble(Path(a.old_root),Path(a.af_root))
    M14,rows14,L,r0,O0,lowerprov,inv,ann=ag.canonical_object(); o0nz=sum(x!=0 for x in O0)
    a11,sector,pos,orbits,P=sector_and_orbits(); C=matrix_for_sector(cols,sector); Cs=C*P
    rankC=DomainMatrix.from_Matrix(C).to_field().rank(); rankS=DomainMatrix.from_Matrix(Cs).to_field().rank()
    nullC=C.cols-rankC; nullS=Cs.cols-rankS
    yraw,norm,yn,primitive=normalized_kernel(Cs,P,sector,O0)
    canon=[F(0)]*NROWS
    for r in agd.get('canonical_y',[]): canon[int(r['compatibility_index'])]=F(r['value'])
    compare=(yn is not None and yn==canon)
    bt=[]
    if yn is not None:
        for j in range(NCOLS):
            s=F(0)
            for i,v in cols[j].items(): s += v*yn[i]
            bt.append(s)
    norm_replay=sum((ag.ff(O0[i])*yn[i] for i in range(NROWS)),F(0)) if yn is not None else None
    sector_support_exact=(set(i for i,v in enumerate(canon) if v)==set(sector))
    orbit_cover=(sum(len(o) for o in orbits)==len(sector) and len({q for o in orbits for q in o})==len(sector))
    # Stronger-than-required diagnostic: uniqueness already in the full parity sector.
    controls={
      'A_frozen_AF_AG_AH_AI_provenance':provenance,
      'A_lane_payload_controls_exact':lane_controls,
      'A_complete_unique_B_coverage':coverage and not dup and len(cols)==NCOLS,
      'A_original_canonical_object_exact':lowerprov and inv and ann and M14.shape==(6790,6800) and L.shape==(1456,6790) and o0nz==223,
      'B_S_parity_exactly_56':len(sector)==56,
      'B_AG_support_equals_full_S_parity':sector_support_exact,
      'C_parity_rank_55_nullity_1':rankC==55 and nullC==1,
      'D_S3_orbit_basis_complete':orbit_cover and P.rows==56,
      'D_S3_orbit_basis_dimension_16':P.cols==16,
      'D_S3_rank_15_nullity_1':rankS==15 and nullS==1,
      'E_independent_kernel_O0_functional_nonzero':norm not in (None,F(0)),
      'E_normalized_generator_equals_AG_AI_exactly':compare,
      'F_BT_y_exact_zero_1114':bool(bt) and all(x==0 for x in bt),
      'F_O0T_y_exact_one':norm_replay==1,
      'G_no_numerical_tolerance':True,
    }
    passed=all(controls.values())
    structural_ready=(provenance and lane_controls and coverage and not dup and lowerprov and inv and ann)
    cls=PASS if passed else (FAIL if structural_ready and (nullS!=1 or (yn is not None and not compare)) else (INVALID if not provenance else BLOCKED))
    payload={
      'gate':'ITER057AJ-SYMMETRY-SECTOR-UNIQUENESS','preregistration':PREREG,'classification':cls,'controls':controls,
      'S_parity_coordinate_count':len(sector),'S_parity_indices':sector,'C_parity_shape':list(C.shape),'C_parity_nnz':len(C.todok()),'rank_C_parity':rankC,'nullity_C_parity':nullC,
      'S3_orbit_basis_dimension':len(orbits),'S3_orbit_sizes':[len(o) for o in orbits],'S3_orbit_representatives':[list(o[0]) for o in orbits],
      'C_S3_shape':list(Cs.shape),'C_S3_nnz':len(Cs.todok()),'rank_C_S3':rankS,'nullity_C_S3':nullS,
      'independent_primitive_sector_generator':primitive,'independent_kernel_O0_value_before_normalization':str(norm) if norm is not None else None,
      'normalized_generator_matches_AG':compare,'BT_y_nonzero_count':sum(x!=0 for x in bt),'O0T_y':str(norm_replay) if norm_replay is not None else None,
      'stronger_structural_observation':'The complete 56-dimensional b=0 odd-time/even-spatial parity sector already has one-dimensional exact dual kernel before imposing S3 invariance.' if nullC==1 else None,
      'exact_zero_uses_tolerance':False,'scope':'uniqueness only inside the frozen finite-dimensional AH parity/S3 compatibility sector; no global/all-orders/physical symmetry claim'
    }
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k not in ('S_parity_indices','independent_primitive_sector_generator')},indent=2,sort_keys=True));return 0 if passed else 2

if __name__=='__main__': raise SystemExit(main())
