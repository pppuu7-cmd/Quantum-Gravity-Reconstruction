#!/usr/bin/env python3
import json

# If U_n -> U strongly and U_n^dagger -> U^dagger strongly with all U_n unitary,
# then U_n rho U_n^dagger -> U rho U^dagger in trace norm for every trace-class rho.
# Proof: exact on finite-rank rho by strong convergence on finitely many vectors; approximate
# arbitrary trace-class rho in trace norm by finite-rank rho_F and use unitary norm preservation.
# A finite convex sum (24 branches) preserves convergence termwise.
branches=24
out={
 'gate':'ITER009-G6-TRACE-CLASS-CHANNEL-LIMIT',
 'branch_count':branches,
 'input':'each branch unitary and adjoint converge strongly on the one-particle physical L2 space',
 'finite_rank_step':'trace-norm convergence follows from strong convergence on finitely many ket/bra vectors',
 'extension_step':'finite-rank operators are trace-norm dense and unitary conjugation is a trace-norm isometry',
 'mixture_step':'finite 24-branch convex sum converges termwise in trace norm',
 'classification':'PASS_SCOPED_STRONG_BRANCH_CONVERGENCE_IMPLIES_TRACE_NORM_CONVERGENCE_OF_THE_FINITE_24_HISTORY_CHANNEL_FOR_ALL_NORMAL_ONE_PARTICLE_STATES',
 'guard':'This does not by itself control a refinement in which the number of serial microscopic cells also diverges; that accumulation is audited separately.'
}
print(json.dumps(out,sort_keys=True))
