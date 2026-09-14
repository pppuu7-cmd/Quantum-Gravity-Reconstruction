#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from pathlib import Path
import sympy as sp

GATE = 'ITER054G-WEYL3-DYNAMICAL-TREATMENT-SELECTION-AUTHORITY'
PREREG = 'b4730d02f66b9378c41313bb833e2fdedd62daae'
SOURCE_LOCK = '3398cd5a195d3d6b05fad01715ab5b79a880c4f1'

CLASS_EXACT = 'ITER054G_EXACT_DYNAMICAL_TREATMENT_SELECTED_READY_FOR_PROSPECTIVE_EXACT_EVOLUTION_REDUCTION'
CLASS_REDUCED = 'ITER054G_ORDER_REDUCED_DYNAMICAL_TREATMENT_SELECTED_READY_FOR_PROSPECTIVE_REDUCED_EVOLUTION_CONSTRUCTION'
CLASS_BOTH = 'BLOCKED_OBJECT_DEFINITION_ITER054G_MULTIPLE_DYNAMICAL_TREATMENTS_AUTHORIZED_WITHOUT_SELECTION_RULE'
CLASS_NEITHER = 'BLOCKED_OBJECT_DEFINITION_ITER054G_WEYL3_DYNAMICAL_TREATMENT_NOT_SELECTED'
CLASS_REVIEW = 'REQUIRES_SOURCE_AUTHORITY_REVIEW_ITER054G'
CLASS_INVALID = 'INVALID_IMPLEMENTATION_OR_PROVENANCE_ITER054G'

CORE = [
    'docs/CONSTITUTION.md',
    'iterations/ITERATION_006.md',
    'iterations/ITERATION_010.md',
    'iterations/ITERATION_011.md',
    'status/ITERATION_047.md',
    'preregistration/ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION.md',
    'results/ITER054A_TERMINAL_RESULT.md',
    'results/ITER054E_TERMINAL_RESULT.md',
    'results/ITER054F_TERMINAL_RESULT.md',
    'recovery/CURRENT_FRONT.md',
    'recovery/state.json',
]

AUTH_PREFIXES = ('docs/','iterations/','status/','results/','recovery/','prereg/','preregistration/')
TEXT_EXT = ('.md','.json','.txt','.yaml','.yml')

# Narrow selector-relevant census terms. Generic words such as "solution space" by
# themselves are intentionally excluded to avoid false source-completeness claims.
CENSUS_PATTERNS = [
    re.compile(r'order[- ]reduc', re.I),
    re.compile(r'effective field theory', re.I),
    re.compile(r'\bEFT\b'),
    re.compile(r'\bcutoff\b', re.I),
    re.compile(r'validity domain', re.I),
    re.compile(r'matching scale', re.I),
    re.compile(r'finite[- ]?c6', re.I),
    re.compile(r'exact (?:finite[- ]?coupling |higher[- ]derivative |fourth[- ]order )?(?:dynamics|solution space|evolution)', re.I),
    re.compile(r'physical (?:branch|solution)[- ]selection', re.I),
]

# Files already explicitly included in the frozen A0/A1 semantic mapping.
REVIEWED_SELECTOR_PATHS = set(CORE)


def git_show(path):
    return subprocess.check_output(['git','show',f'{SOURCE_LOCK}:{path}'], text=True)


def list_locked_paths():
    out = subprocess.check_output(['git','ls-tree','-r','--name-only',SOURCE_LOCK], text=True)
    return [x.strip() for x in out.splitlines() if x.strip()]


def load_core():
    texts = {}
    errors = []
    for p in CORE:
        try:
            texts[p] = git_show(p)
        except Exception as ex:
            errors.append(f'{p}:{type(ex).__name__}:{ex}')
    return texts, errors


def line_excerpt(line, n=260):
    x = ' '.join(line.strip().split())
    return x if len(x) <= n else x[:n-3] + '...'


def stream_s0():
    try:
        paths = list_locked_paths()
    except Exception as ex:
        return {'stream':'S0','gate':GATE,'valid':False,'errors':[f'ls-tree:{ex}']}
    hits=[]; read_errors=[]
    for p in paths:
        if not p.startswith(AUTH_PREFIXES) or not p.endswith(TEXT_EXT):
            continue
        try:
            txt=git_show(p)
        except Exception as ex:
            read_errors.append(f'{p}:{type(ex).__name__}:{ex}')
            continue
        for i,line in enumerate(txt.splitlines(),1):
            pats=[pat.pattern for pat in CENSUS_PATTERNS if pat.search(line)]
            if pats:
                hits.append({'path':p,'line':i,'patterns':pats,'excerpt':line_excerpt(line)})
    hit_paths=sorted({h['path'] for h in hits})
    unexpected=sorted(set(hit_paths)-REVIEWED_SELECTOR_PATHS)
    return {
        'stream':'S0','gate':GATE,'valid':not read_errors,
        'source_lock':SOURCE_LOCK,
        'authority_file_count':sum(1 for p in paths if p.startswith(AUTH_PREFIXES) and p.endswith(TEXT_EXT)),
        'hit_count':len(hits),'hit_paths':hit_paths,'hits':hits,
        'unexpected_candidate_paths':unexpected,
        'read_errors':read_errors,
        'interpretation':'keyword census only; keyword hits are not selectors'
    }


def stream_a0():
    texts, errors = load_core()
    if errors:
        return {'stream':'A0','gate':GATE,'valid':False,'outcome':'INVALID_PROVENANCE','errors':errors}
    con=texts['docs/CONSTITUTION.md'].lower()
    i6=texts['iterations/ITERATION_006.md'].lower()
    i10=texts['iterations/ITERATION_010.md'].lower()
    a_pre=texts['preregistration/ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION.md'].lower()
    a_res=texts['results/ITER054A_TERMINAL_RESULT.md'].lower()
    f_res=texts['results/ITER054F_TERMINAL_RESULT.md'].lower()
    state=json.loads(texts['recovery/state.json'])

    # These booleans test whether the frozen sources provide the positive authority
    # required by the preregistration. They deliberately do not infer authority from
    # the mere existence of an action term.
    exact_finite_c6_rule = any(k in '\n'.join(t.lower() for t in texts.values()) for k in [
        'take exact finite-c6', 'exact finite-c6 dynamics is physical',
        'full higher-derivative solution space is physical'
    ])
    full_solution_space_mapped = (
        'complete higher-derivative euler-lagrange solution space' in i6
        or 'additional initial-data' in i6
    ) and 'weyl' in i6
    extra_state_mapped = (
        state.get('claim_locks',{}).get('strong_hyperbolicity_evolution_object_defined') is True
        and 'additional initial' in '\n'.join(t.lower() for t in texts.values())
    )
    exact_validity_domain = any(k in '\n'.join(t.lower() for t in texts.values()) for k in [
        'exact finite-c6 validity domain', 'exact higher-derivative validity domain'
    ])
    anti_posthoc = ('post' in con and 'branch' in con) or ('branch selection' in con) or ('overfit' in con)

    obligations={
        'finite_nonzero_c6_exact_dynamical_rule':bool(exact_finite_c6_rule),
        'complete_higher_derivative_solution_space_physical_and_mapped':bool(full_solution_space_mapped),
        'additional_initial_data_mapped_to_qgr_state_measure':bool(extra_state_mapped),
        'exact_use_validity_domain_defined':bool(exact_validity_domain),
        'selection_independent_of_later_stability_outcome':bool(anti_posthoc and exact_finite_c6_rule),
    }
    selected=all(obligations.values())
    # Frozen negative evidence is reported, not treated as a proof of candidate failure.
    negative_evidence={
        'iter010_c6_unfixed_and_phase_composition_compatible_with_arbitrary_real_c6':('arbitrary real `c6`' in texts['iterations/ITERATION_010.md'] or 'arbitrary real c6' in i10) and ('unfixed' in i10),
        'iter054a_regimes_distinguished_not_selected':('exact and perturbative/order-reduced dynamical regimes must remain distinct' in a_pre) and ('does **not** establish a physical extra-mode count' in a_res),
        'iter054f_evolution_object_blocked':('blocked_object_definition_iter054f' in f_res) and ('does not' in f_res),
    }
    return {
        'stream':'A0','gate':GATE,'valid':True,
        'outcome':'EXACT_SELECTED' if selected else 'EXACT_NOT_SELECTED',
        'obligations':obligations,'negative_evidence':negative_evidence,
        'source_paths':CORE,'source_lock':SOURCE_LOCK,
        'interpretation':'authority audit; absence of selector is an object-definition blocker, not candidate inconsistency'
    }


def stream_a1():
    texts, errors = load_core()
    if errors:
        return {'stream':'A1','gate':GATE,'valid':False,'outcome':'INVALID_PROVENANCE','errors':errors}
    alltxt='\n'.join(texts.values()).lower()
    a_pre=texts['preregistration/ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION.md'].lower()
    a_res=texts['results/ITER054A_TERMINAL_RESULT.md'].lower()
    e_res=texts['results/ITER054E_TERMINAL_RESULT.md'].lower()
    f_res=texts['results/ITER054F_TERMINAL_RESULT.md'].lower()
    state=json.loads(texts['recovery/state.json'])

    controlled_expansion = any(k in alltxt for k in [
        'qgr-derived order-reduction expansion parameter',
        'controlled weyl3 effective field theory expansion'
    ])
    derived_domain = any(k in alltxt for k in [
        'weyl3 eft cutoff', 'order-reduced validity domain', 'qgr-derived cutoff for weyl3',
        'qgr-derived matching scale for weyl3'
    ])
    explicit_reduction = any(k in alltxt for k in [
        'eliminate higher derivatives order by order using the lower-order equations',
        'order-reduction prescription for weyl3'
    ])
    branch_excluded_by_domain = any(k in alltxt for k in [
        'singular branch lies outside the derived validity domain',
        'non-analytic branch lies above the derived cutoff'
    ])
    mapped_to_micro = any(k in alltxt for k in [
        'order-reduced equations map to the qgr microscopic',
        'microscopic derivation of the order-reduced'
    ])
    predates = controlled_expansion and derived_domain and explicit_reduction and branch_excluded_by_domain and mapped_to_micro

    obligations={
        'controlled_small_expansion_defined_for_weyl3':bool(controlled_expansion),
        'qgr_derived_validity_domain_or_cutoff':bool(derived_domain),
        'explicit_order_reduction_prescription':bool(explicit_reduction),
        'singular_branch_excluded_by_preexisting_domain_rule':bool(branch_excluded_by_domain),
        'reduced_equations_mapped_to_microscopic_state_composition_and_gr_limit':bool(mapped_to_micro),
        'selection_independent_of_later_stability_outcome':bool(predates),
    }
    selected=all(obligations.values())
    negative_evidence={
        'iter054a_only_says_singular_root_outside_finite_taylor_unless_separately_justified':('outside a finite-order perturbative/order-reduced branch unless separately justified' in a_pre),
        'iter054a_terminal_is_regime_separation_only':('regime separation only' in a_res),
        'iter054e_does_not_assign_physical_branch_weights':('does **not** establish' in e_res or 'does not establish' in e_res),
        'iter054f_treatment_not_defined_by_evolution_object':('exact-vs-order-reduced treatment' in f_res and 'no preferred' in f_res),
        'current_state_treatment_not_authorized':state.get('claim_locks',{}).get('weyl3_dynamical_treatment_authorized') is False,
    }
    return {
        'stream':'A1','gate':GATE,'valid':True,
        'outcome':'ORDER_REDUCED_SELECTED' if selected else 'ORDER_REDUCED_NOT_SELECTED',
        'obligations':obligations,'negative_evidence':negative_evidence,
        'source_paths':CORE,'source_lock':SOURCE_LOCK,
        'interpretation':'authority audit; mention of perturbative/order-reduced bookkeeping is not a physical selector'
    }


def stream_b0():
    z,eps,lam=sp.symbols('z eps lam', nonzero=True)
    expr=sp.expand(z+eps*lam*z**2)
    factor=sp.factor(expr)
    exact_factor=sp.simplify(expr-z*(1+eps*lam*z))==0
    r0=sp.Integer(0); rhs=-1/(eps*lam)
    roots_ok=sp.simplify(expr.subs(z,r0))==0 and sp.simplify(expr.subs(z,rhs))==0
    singular=sp.limit(rhs,eps,0,dir='+') in (sp.oo,-sp.oo) or rhs.has(1/eps)
    # A finite polynomial in eps cannot equal a function with a simple pole at eps=0.
    c=sp.symbols('c0:5')
    taylor=sum(c[n]*eps**n for n in range(5))
    pole_witness=sp.simplify(sp.limit(eps*(taylor-rhs),eps,0))
    finite_taylor_cannot_equal = sp.simplify(pole_witness-1/lam)==0
    gr_only=sp.expand(expr.subs(eps,0))==z
    valid=bool(exact_factor and roots_ok and singular and finite_taylor_cannot_equal and gr_only)
    return {
        'stream':'B0','gate':GATE,'valid':valid,
        'factorized':str(factor),'exact_factorization':bool(exact_factor),
        'roots':['0',str(rhs)],'roots_annihilate':bool(roots_ok),
        'singular_branch_nonanalytic':bool(singular),
        'finite_taylor_cannot_equal_singular_branch':bool(finite_taylor_cannot_equal),
        'eps_zero_leaves_gr_factor_only':bool(gr_only),
        'interpretation':'exact mathematical control only; no QGR treatment selected'
    }


def stream_b1():
    texts, errors = load_core()
    if errors:
        return {'stream':'B1','gate':GATE,'valid':False,'errors':errors}
    con=texts['docs/CONSTITUTION.md'].lower()
    state=json.loads(texts['recovery/state.json'])
    locks=state.get('claim_locks',{})
    anti_posthoc=('branch' in con and ('overfit' in con or 'post' in con))
    required={
        'anti_posthoc_branch_selection_rule_present':bool(anti_posthoc),
        'c6_unfixed':not state.get('candidate',{}).get('six_derivative_coefficient_fixed',False),
        'beta_equal_one_not_authorized':locks.get('beta_set_to_one_authorized') is False,
        'theory_established_zero':state.get('readiness',{}).get('theory_established_pct')==0,
        'strong_hyperbolicity_not_established':locks.get('weyl3_well_posedness_established') is False,
        'treatment_not_pre_authorized_in_state':locks.get('weyl3_dynamical_treatment_authorized') is False,
        'quantum_transition_not_authorized':locks.get('quantum_amplitude_measure_transition_authorized') is False,
    }
    valid=all(required.values())
    return {
        'stream':'B1','gate':GATE,'valid':bool(valid),'required_firewall':required,
        'interpretation':'missing selector is BLOCKED_OBJECT_DEFINITION, not candidate failure; no ghost/mode/unitarity claim'
    }


def run_stream(s):
    return {'S0':stream_s0,'A0':stream_a0,'A1':stream_a1,'B0':stream_b0,'B1':stream_b1}[s]()


def aggregate(root):
    rows=[]; errors=[]
    for p in sorted(Path(root).rglob('*.json')):
        try: rows.append(json.loads(p.read_text()))
        except Exception as ex: errors.append(f'{p}:{type(ex).__name__}:{ex}')
    expected={'S0','A0','A1','B0','B1'}
    by={r.get('stream'):r for r in rows if r.get('stream') in expected}
    missing=sorted(expected-set(by))
    valid=not missing and not errors and all(by[s].get('valid') is True for s in expected)
    if not valid:
        cls=CLASS_INVALID; terminal=False
    elif by['S0'].get('unexpected_candidate_paths'):
        cls=CLASS_REVIEW; terminal=True
    else:
        exact=by['A0'].get('outcome')=='EXACT_SELECTED'
        reduced=by['A1'].get('outcome')=='ORDER_REDUCED_SELECTED'
        if exact and not reduced: cls=CLASS_EXACT
        elif reduced and not exact: cls=CLASS_REDUCED
        elif exact and reduced: cls=CLASS_BOTH
        else: cls=CLASS_NEITHER
        terminal=True
    return {
        'gate':GATE,'classification':cls,'terminal_valid':bool(terminal),'scientific_pass':False,
        'source_lock':SOURCE_LOCK,'preregistration_commit':PREREG,
        'found_streams':sorted(by),'missing_streams':missing,'parse_errors':errors,
        'stream_valid':{s:by[s].get('valid') for s in by},
        'exact_outcome':by.get('A0',{}).get('outcome'),
        'order_reduced_outcome':by.get('A1',{}).get('outcome'),
        'unexpected_candidate_paths':by.get('S0',{}).get('unexpected_candidate_paths',[]),
        'interpretation_lock':'DYNAMICAL-TREATMENT SELECTION AUTHORITY ONLY; NO HYPERBOLICITY, PHYSICAL MODE/GHOST, UNITARITY OR QUANTUM CLAIM'
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',choices=['S0','A0','A1','B0','B1'])
    ap.add_argument('--aggregate')
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    data=aggregate(a.aggregate) if a.aggregate else run_stream(a.stream)
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(data,indent=2,sort_keys=True))
    print(json.dumps(data,sort_keys=True))
    if a.aggregate and not data.get('terminal_valid',False): raise SystemExit(2)
    if not a.aggregate and not data.get('valid',False): raise SystemExit(2)

if __name__=='__main__': main()
