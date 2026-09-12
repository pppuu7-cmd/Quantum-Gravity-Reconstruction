#!/usr/bin/env python3
import json

# For unitary conjugation channels Ad_U and Ad_V and any system+ancilla trace-class X,
# ||(U⊗I)X(U†⊗I)-(V⊗I)X(V†⊗I)||_1
# <= ||(U-V)⊗I|| ||X||_1 + ||(U†-V†)⊗I|| ||X||_1
# <= 2 ||U-V||_op ||X||_1.
# Hence ||Ad_U-Ad_V||_diamond <= 2||U-V||_op.
# The same convex bound applies to equal-weight mixtures branchwise.
# If sup_a ||U_a(h_{n+1})-U_a(h_n)|| <= C h_n^p with dyadic h_n=2^-n and p>0,
# the channel increments are summable. QGR currently has scalar/RMS O(h^4) evidence,
# not this uniform operator-sup hypothesis.

for p in [1,2,4]:
    partial=sum(2.0*(2.0**(-n))**p for n in range(1,80))
    exact=2.0*(2.0**(-p))/(1.0-2.0**(-p))
    assert abs(partial-exact)<1e-12

out={
    "gate":"ITER009-G4-CHANNEL-CONVERGENCE-BOUND",
    "unitary_channel_bound":"||Ad_U-Ad_V||_diamond <= 2||U-V||_op",
    "mixture_bound":"equal-weight branch mixture bounded by average/sup of branch unitary differences",
    "sufficient_dyadic_condition":"sup_alpha ||U_alpha(h_{n+1})-U_alpha(h_n)||_op <= C h_n^p for any p>0",
    "current_QGR_evidence":"specified scalar/RMS comparator scaling near O(h^4), not a uniform branch operator-norm bound on a full state domain",
    "classification":"BLOCKED_SCOPED_A_CLEAR_SUMMABLE_OPERATOR_CRITERION_EXISTS_BUT_CURRENT_QGR_DATA_DO_NOT_ESTABLISH_THE_REQUIRED_UNIFORM_BRANCH_OPERATOR_BOUND",
    "guard":"Observable or RMS convergence cannot be substituted for a diamond/strong operator convergence theorem."
}
print(json.dumps(out,sort_keys=True))
