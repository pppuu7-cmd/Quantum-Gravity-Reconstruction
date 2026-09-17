#!/usr/bin/env python3
"""Iter057AS target-blind source-basis cardinality audit."""
import hashlib, json, math
from itertools import product
from pathlib import Path

PREREG='6c08691e0a00e6176531c1d07c01f50fc4758ab8'
ROOT=Path(__file__).resolve().parents[1]


def sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def enum_homogeneous(n,vars_=4):
    return sorted(a for a in product(range(n+1),repeat=vars_) if sum(a)==n)


def main():
    w=(ROOT/'code'/'qgr_iter057w_decic_einstein_seed_sparse.py').read_text()
    ar=(ROOT/'code'/'qgr_iter057ar_corrected_degree6_source.py').read_text()
    pre=(ROOT/'preregistration'/'ITER057AR_CORRECTED_DEGREE6_WEYL3_SOURCE_AUTHORITY.md').read_text()

    hom=enum_homogeneous(6,4)
    cumulative=[a for d in range(7) for a in enum_homogeneous(d,4)]
    pairs=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
    census={
      'variables':4,
      'symmetric_pairs':len(pairs),
      'homogeneous_degree6_monomials_enum':len(hom),
      'homogeneous_degree6_monomials_closed':math.comb(9,3),
      'homogeneous_degree6_source_slots':len(pairs)*len(hom),
      'cumulative_degree0_through6_monomials_enum':len(cumulative),
      'cumulative_degree0_through6_monomials_closed':math.comb(10,4),
      'cumulative_degree0_through6_source_slots':len(pairs)*len(cumulative),
    }
    source_checks={
      'iter057w_alphas_is_exact_homogeneous_four_tuple':
        'def alphas(n): return sorted(a for a in product(range(n+1),repeat=4) if sum(a)==n)' in w,
      'iter057ar_loops_pairs_then_alphas6':
        'for a,bb in PAIRS:' in ar and 'for alpha in b.alphas(6):' in ar,
      'iter057ar_prereg_says_2100': '2100-slot' in pre,
      'iter057ar_prereg_says_degree_six': 'degree-six' in pre,
      'historical_target_coefficients_loaded':False,
    }
    exact=(census['homogeneous_degree6_monomials_enum']==census['homogeneous_degree6_monomials_closed']==84 and
           census['homogeneous_degree6_source_slots']==840 and
           census['cumulative_degree0_through6_monomials_enum']==census['cumulative_degree0_through6_monomials_closed']==210 and
           census['cumulative_degree0_through6_source_slots']==2100)
    controls={
      'independent_enumeration_and_closed_form_agree':exact,
      'source_interface_checks_pass':all(v for k,v in source_checks.items() if k!='historical_target_coefficients_loaded'),
      'historical_target_coefficients_not_loaded':not source_checks['historical_target_coefficients_loaded'],
      'no_tolerance_or_fit':True,
      'c6_status_unchanged_symbolic_unfixed':True,
    }
    classification=('PASS_SCOPED_ITER057AS_AR_CARDINALITY_INCONSISTENCY_ESTABLISHED'
                    if all(controls.values()) else 'BLOCKED_ITER057AS_SOURCE_OBJECT_DEFINITION_UNRESOLVED')
    payload={'gate':'ITER057AS_SOURCE_BASIS_CARDINALITY_AUDIT','preregistration_commit':PREREG,
             'classification':classification,'census':census,'source_checks':source_checks,'controls':controls,
             'interpretation':'840 is the homogeneous degree-six slice; 2100 is the cumulative degree-0-through-6 tensor-source space under the inherited four-variable/ten-pair representation. Iter057AR remains BLOCKED; no post-hoc embedding is authorized.',
             'c6':'SYMBOLIC_UNFIXED'}
    payload['scientific_payload_sha256']=sha(payload)
    print(json.dumps(payload,sort_keys=True,indent=2))
    Path('iter057as_cardinality_audit.json').write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
    if not all(controls.values()): raise SystemExit(2)

if __name__=='__main__': main()
