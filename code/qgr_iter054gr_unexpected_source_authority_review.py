#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from pathlib import Path

GATE = 'ITER054G-R-UNEXPECTED-DYNAMICAL-TREATMENT-SOURCE-AUTHORITY-REVIEW'
PREREG = 'f9973884ce8e994c347f0ee5412fdc25206875ee'
SOURCE_LOCK = '3398cd5a195d3d6b05fad01715ab5b79a880c4f1'
PARENT_RUN = 34818484127
PARENT_CLASS = 'REQUIRES_SOURCE_AUTHORITY_REVIEW_ITER054G'
PARENT_EXACT = 'EXACT_NOT_SELECTED'
PARENT_REDUCED = 'ORDER_REDUCED_NOT_SELECTED'

CLASS_BLOCKED = 'BLOCKED_OBJECT_DEFINITION_ITER054G_WEYL3_DYNAMICAL_TREATMENT_NOT_SELECTED_AFTER_SOURCE_REVIEW'
CLASS_EXACT = 'ITER054G_EXACT_DYNAMICAL_TREATMENT_SELECTED_AFTER_SOURCE_REVIEW'
CLASS_REDUCED = 'ITER054G_ORDER_REDUCED_DYNAMICAL_TREATMENT_SELECTED_AFTER_SOURCE_REVIEW'
CLASS_BOTH = 'BLOCKED_OBJECT_DEFINITION_ITER054G_MULTIPLE_DYNAMICAL_TREATMENTS_AUTHORIZED_WITHOUT_SELECTION_RULE'
CLASS_AMBIG = 'BLOCKED_SOURCE_AUTHORITY_ITER054G_UNEXPECTED_TREATMENT_SOURCE_AMBIGUOUS'
CLASS_INVALID = 'INVALID_IMPLEMENTATION_OR_PROVENANCE_ITER054G_R'

PATHS = [
    'docs/KMQGB_HANDOFF.md',
    'iterations/ITERATION_007.md',
    'iterations/ITERATION_012.md',
    'preregistration/ITER054B_WEYL3_PRINCIPAL_HESSIAN_AND_WELLPOSEDNESS_OBLIGATION.md',
    'results/ITER007_G6E_G6H_CURVED_BROADBAND_OBSERVABLE_CLOSURE.md',
    'results/ITER007_G7B_G7D_SCALE_BOUNDARY.md',
    'results/ITER032_G32_PROJECTIVE_REFINEMENT_LIMIT_ACTION_PHASE.md',
    'results/ITER053U_TERMINAL_RESULT.md',
]

# Exact frozen context witnesses established prospectively for the eight-source panel.
# They are not scientific selector criteria; they ensure each lane is reviewing the
# intended source/context rather than silently accepting a renamed or different file.
CONTEXT_WITNESSES = {
    0: ['Ordinary cutoff divergence does not equal a no-go', 'QGR response: distinguish'],
    1: ['no arbitrary UV momentum cutoff enters this normalized comparator', 'no derived nonzero refinement stop scale'],
    2: ['MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY', 'BACKGROUND METHODOLOGY — NOT QGR AUTHORITY'],
    3: ['insufficient to authorize well-posed exact higher-derivative dynamics', 'does **not** establish the gauge-fixed covariant metric principal symbol'],
    4: ['no arbitrary UV momentum cutoff enters the normalized comparator', 'absolute physical cell scale `h`'],
    5: ['no current nonzero refinement stop scale', 'No current authoritative QGR rule fixes `g=1`'],
    6: ['without adding a regulator or cutoff', '`c6` fixed = **NO**'],
    7: ['derive a QGR-specific Weyl^3 dynamical-treatment authority', '`c6` remains symbolic/unfixed'],
}

# Phrases that would be sufficiently close to a positive treatment authority to force
# AMBIGUOUS rather than allowing NON_SELECTOR. The frozen manual review then must not
# silently discard them.
POSITIVE_EXACT_MARKERS = [
    r'exact finite[- ]?c6 .* (?:physical|dynamics|evolution)',
    r'complete higher[- ]derivative .* solution space .* (?:physical|admissible)',
    r'additional initial[- ]data .* (?:qgr|state|measure|composition)',
    r'exact higher[- ]derivative validity domain',
]
POSITIVE_REDUCED_MARKERS = [
    r'qgr[- ]derived .* (?:cutoff|validity domain|matching scale)',
    r'order[- ]reduction prescription',
    r'eliminat(?:e|ing) higher derivatives .* lower[- ]order equations',
    r'singular branch .* outside .* (?:derived|qgr) .* (?:domain|cutoff)',
    r'order[- ]reduced .* (?:qgr microscopic|state|composition)',
]

MATCH_TERMS = [
    re.compile(r'order[- ]reduc', re.I),
    re.compile(r'\bEFT\b'),
    re.compile(r'\bcutoff\b', re.I),
    re.compile(r'validity domain', re.I),
    re.compile(r'matching scale', re.I),
    re.compile(r'exact .*?(?:dynamics|evolution|solution space)', re.I),
    re.compile(r'branch selection', re.I),
    re.compile(r'dynamical treatment', re.I),
]


def locked_text(path):
    return subprocess.check_output(['git', 'show', f'{SOURCE_LOCK}:{path}'], text=True)


def excerpts(text):
    out=[]
    for n,line in enumerate(text.splitlines(),1):
        pats=[p.pattern for p in MATCH_TERMS if p.search(line)]
        if pats:
            s=' '.join(line.strip().split())
            out.append({'line':n,'patterns':pats,'excerpt':s[:320]})
    return out


def obligations_template(n_exact=5, n_reduced=6):
    return ({f'exact_obligation_{i+1}': False for i in range(n_exact)},
            {f'order_reduced_obligation_{i+1}': False for i in range(n_reduced)})


def source_status(index, text):
    low=text.lower()
    exact, reduced = obligations_template()
    witness_ok=all(w.lower() in low for w in CONTEXT_WITNESSES[index])
    positive_exact=[m for m in POSITIVE_EXACT_MARKERS if re.search(m,text,re.I|re.S)]
    positive_reduced=[m for m in POSITIVE_REDUCED_MARKERS if re.search(m,text,re.I|re.S)]

    # Source-specific frozen semantic checks. Every one is a negative-authority witness:
    # the file either concerns a different cutoff/scale question or explicitly states
    # that treatment authority is missing/future/not established.
    if index == 0:
        reason='KMQGB handoff discusses generic cutoff divergence versus no-go/renormalization burden; it gives no QGR Weyl3 treatment rule.'
        qgr_authority_context='benchmark-handoff methodology, not a Weyl3 dynamical-treatment construction'
    elif index == 1:
        reason='Iter007 cutoff language concerns a normalized broadband comparator and lack of a derived refinement stop scale; it predates and does not select Weyl3 exact/order-reduced dynamics.'
        qgr_authority_context='QGR result, but on observable normalization/refinement scale rather than Weyl3 treatment'
    elif index == 2:
        reason='Iter012 explicitly classifies MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY and marks external EFT literature BACKGROUND METHODOLOGY — NOT QGR AUTHORITY.'
        qgr_authority_context='QGR audit explicitly recording absence of selector'
    elif index == 3:
        reason='Iter054B explicitly says algebraic Hessian evidence is insufficient to authorize well-posed exact higher-derivative dynamics and does not supply an order-reduction rule.'
        qgr_authority_context='prospective QGR obligation/negative authority boundary'
    elif index == 4:
        reason='G6E-G6H cutoff language concerns analytic momentum integration in an observable comparator; no Weyl3 dynamical treatment is defined.'
        qgr_authority_context='QGR observable/readout result, unrelated cutoff meaning'
    elif index == 5:
        reason='G7B-G7D concerns absence of a physical refinement stop scale and an unfixed microscopic coupling; it supplies no Weyl3 order reduction or exact higher-derivative solution-space rule.'
        qgr_authority_context='QGR scale-identifiability result, not treatment selection'
    elif index == 6:
        reason='Iter032 forbids adding regulator/cutoff to repair a projective refinement regularity theorem and explicitly leaves c6/phase normalization unfixed; it is not a Weyl3 treatment selector.'
        qgr_authority_context='conditional refinement-limit result, not Weyl3 dynamics'
    else:
        reason='Iter053U explicitly makes derivation of a future QGR-specific Weyl3 dynamical-treatment authority the next gate; therefore it does not itself provide that authority.'
        qgr_authority_context='QGR terminal result explicitly deferring treatment selection'

    if not witness_ok:
        classification='AMBIGUOUS_SOURCE_AUTHORITY'
        reason='Frozen context witnesses were not all found; fail closed rather than classify a potentially changed source.'
    elif positive_exact or positive_reduced:
        classification='AMBIGUOUS_SOURCE_AUTHORITY'
        reason=('Potential positive selector-like wording was detected outside the frozen semantic expectation; '
                'manual authority adjudication is required. exact=%s reduced=%s' % (positive_exact,positive_reduced))
    else:
        classification='NON_SELECTOR'

    return {
        'classification':classification,
        'context_witnesses_valid':bool(witness_ok),
        'qgr_authority_context':qgr_authority_context,
        'exact_selector_obligations':exact,
        'order_reduced_selector_obligations':reduced,
        'potential_exact_markers':positive_exact,
        'potential_order_reduced_markers':positive_reduced,
        'reason':reason,
    }


def lane(index):
    if index < 0 or index >= len(PATHS):
        raise ValueError('index out of range')
    path=PATHS[index]
    try:
        text=locked_text(path)
    except Exception as ex:
        return {'gate':GATE,'index':index,'path':path,'source_lock':SOURCE_LOCK,
                'valid':False,'classification':'INVALID_PROVENANCE','error':f'{type(ex).__name__}:{ex}'}
    stat=source_status(index,text)
    return {
        'gate':GATE,'index':index,'path':path,'source_lock':SOURCE_LOCK,'valid':True,
        'matching_excerpts':excerpts(text),
        **stat,
    }


def aggregate(root):
    rows=[]; errors=[]
    for p in sorted(Path(root).rglob('*.json')):
        try: rows.append(json.loads(p.read_text()))
        except Exception as ex: errors.append(f'{p}:{type(ex).__name__}:{ex}')
    by={r.get('index'):r for r in rows if isinstance(r.get('index'),int) and 0 <= r['index'] < 8}
    missing=sorted(set(range(8))-set(by))
    duplicate_count=len(rows)-len(by)
    valid=not missing and not errors and duplicate_count==0 and all(by[i].get('valid') is True for i in range(8))
    classes={i:by[i].get('classification') for i in by}

    if not valid or any(c=='INVALID_PROVENANCE' for c in classes.values()):
        cls=CLASS_INVALID; terminal=False
    elif any(c=='AMBIGUOUS_SOURCE_AUTHORITY' for c in classes.values()):
        cls=CLASS_AMBIG; terminal=True
    else:
        exact=any(c in ('EXACT_SELECTOR','BOTH_SELECTORS') for c in classes.values())
        reduced=any(c in ('ORDER_REDUCED_SELECTOR','BOTH_SELECTORS') for c in classes.values())
        if exact and reduced: cls=CLASS_BOTH
        elif exact: cls=CLASS_EXACT
        elif reduced: cls=CLASS_REDUCED
        elif all(c=='NON_SELECTOR' for c in classes.values()): cls=CLASS_BLOCKED
        else: cls=CLASS_INVALID
        terminal=cls != CLASS_INVALID

    return {
        'gate':GATE,
        'classification':cls,
        'terminal_valid':bool(terminal),
        'scientific_pass':False,
        'source_lock':SOURCE_LOCK,
        'preregistration_commit':PREREG,
        'parent_run':PARENT_RUN,
        'parent_classification':PARENT_CLASS,
        'parent_exact_outcome':PARENT_EXACT,
        'parent_order_reduced_outcome':PARENT_REDUCED,
        'found_indices':sorted(by),
        'missing_indices':missing,
        'parse_errors':errors,
        'duplicate_count':duplicate_count,
        'lane_classifications':{str(i):classes[i] for i in sorted(classes)},
        'paths':{str(i):by[i].get('path') for i in sorted(by)},
        'interpretation_lock':'SOURCE-AUTHORITY REVIEW ONLY; BLOCKED MEANS TREATMENT SELECTION MISSING, NOT QGR CANDIDATE FAILURE OR HYPERBOLICITY/PHYSICAL-SPECTRUM RESULT',
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--index',type=int)
    ap.add_argument('--aggregate')
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    data=aggregate(args.aggregate) if args.aggregate else lane(args.index)
    p=Path(args.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(data,indent=2,sort_keys=True))
    print(json.dumps(data,sort_keys=True))
    if args.aggregate and not data.get('terminal_valid',False): raise SystemExit(2)
    if not args.aggregate and not data.get('valid',False): raise SystemExit(2)

if __name__=='__main__':
    main()
