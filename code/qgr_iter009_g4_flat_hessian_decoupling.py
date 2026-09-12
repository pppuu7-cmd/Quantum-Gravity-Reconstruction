#!/usr/bin/env python3
import json

# Around the exact flat seed W0=0, write W(eps)=eps W1 + eps^2 W2 + ... .
# Any homogeneous cubic invariant I3(W) begins at eps^3. Therefore its first and
# second variations at eps=0 vanish exactly. No tensor-index choice can generate
# eps or eps^2 terms from a homogeneous cubic in W when W0=0.
orders = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            orders.append(a+b+c)
min_order = min(orders)
assert min_order == 3

out = {
    "gate": "ITER009-G4-FLAT-HESSIAN-DECOUPLING",
    "background_weyl": 0,
    "minimum_epsilon_order_of_Weyl_cubed": min_order,
    "first_variation_at_flat": 0,
    "second_variation_at_flat": 0,
    "classification": "PASS_SCOPED_C6_WEYL_CUBED_DOES_NOT_MODIFY_THE_FLAT_QGR_LINEARIZED_HESSIAN_OR_TREE_LEVEL_CHARACTERISTIC_CONE",
    "guard": "Cubic and higher interactions about flat space can still depend on c6; curved-background quadratic response is a separate question."
}
print(json.dumps(out, sort_keys=True))
