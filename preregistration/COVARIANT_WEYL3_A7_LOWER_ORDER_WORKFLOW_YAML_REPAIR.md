# Prospective execution-only repair — A7 lower-order workflow YAML fallback

Date: 2026-09-19

Scope: execution/workflow syntax only.

## Frozen defect observed before scientific execution

Execution-only PR #33 was opened from the frozen lower-order execution authority, but no GitHub Actions run was created. Inspection of the frozen workflow identified an invalid YAML literal-block indentation in the terminal missing-artifact fallback: the Python heredoc body was emitted at column zero, outside the `run: |` block.

No source-lock job, Researcher job, Critic job, terminal comparator, or scientific production executed. Therefore there is no scientific result to classify or repair.

## Authorized repair

Modify only `.github/workflows/qgr-weyl3-a7-lower-order-localization.yml` to replace the malformed heredoc fallback with YAML-valid shell/Python syntax.

Then prospectively refresh only the workflow identity in `preregistration/COVARIANT_WEYL3_A7_LOWER_ORDER_EXECUTION_BINDING.json`.

## Frozen invariants

Do not modify:
- preregistration `a8c7bd1bd5280f18aa50955b4cd847b707c178ab`;
- decomposition binding `f0081e60056106b0eac916b6f207ad03fc113233`;
- Researcher blob `321e37073c33c279e11de79c201a63922718e418`;
- Critic blob `5bad4bd0362e2eabf7df1906d1cf6308f67a4a64`;
- terminal comparator blob `728952715cec8de1e95575157149739d3974b044`;
- source-lock blob `4d5b64f0421c243cdafb067ef2e1e3645cfcbba6`;
- frozen witness `OFFSHELL_A / d=7`;
- parent discrepancy;
- exact arithmetic;
- class semantics/order;
- terminal taxonomy;
- `c6=SYMBOLIC_UNFIXED`;
- corrected Q10 lock.

After repair, trigger the same execution-only PR by a sentinel-only synchronization commit. The first actual Actions run is the scientific production authority.
