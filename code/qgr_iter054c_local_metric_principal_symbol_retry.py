#!/usr/bin/env python3
import sympy as sp
import qgr_iter054c_local_metric_principal_symbol as core

# Implementation-only prereg-compliance fix:
# the initial implementation accidentally included one null covector [3,2,1,2].
# Replace only that witness with a non-null exact-rational/integer covector.
def corrected_k_panel():
    return [
        [sp.Integer(2),sp.Integer(1),sp.Integer(3),sp.Integer(1)],
        [sp.Integer(3),sp.Integer(2),sp.Integer(1),sp.Integer(3)],
        [sp.Integer(4),sp.Integer(1),sp.Integer(2),sp.Integer(3)],
        [sp.Integer(5),sp.Integer(2),sp.Integer(3),sp.Integer(1)],
    ]

core.k_panel = corrected_k_panel

if __name__ == '__main__':
    core.main()
