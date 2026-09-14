# QGR automation runner failure pattern and mitigation

Date: 2026-09-14

## Observed failure pattern

Several scheduled QGR automation runs ended in the ChatGPT task UI with the generic message `Hmm...something seems to have gone wrong.` The repository evidence does **not** identify this as a scientific or GitHub Actions failure.

The task metadata showed the same operational pattern for both QGR lanes: the scheduled run started, useful GitHub work could occur, and the automation was then left disabled roughly one minute later. The same approximately one-minute failure envelope was also observed on other long research automations. The internal task-runner error payload is not exposed here, so an exact platform timeout code cannot be asserted, but the repeated timing pattern is strongly consistent with a scheduled-session execution/finalization timeout or equivalent task-runner boundary rather than a repository failure.

Important consequence: a generic task UI failure must **not** be interpreted as a scientific FAIL, GitHub Actions FAIL, or absence of durable work. Always recover from GitHub main first.

## Mitigation applied

Both `QGR Theory Constructor` and `QGR Adversarial Referee` were changed to short-orchestrator mode:

- read only `recovery/CURRENT_FRONT.md`, `recovery/state.json`, and the latest small commit window at run start;
- inspect only the active gate/run named by recovery;
- do not enumerate the full repository, all historical Actions, or all artifacts on every run;
- do not wait for long GitHub Actions workflows;
- put heavy symbolic/numerical work into GitHub Actions matrices;
- one scheduled run performs one bounded action: launch, terminalize, or review one gate;
- target small tool-call budgets and finish with a durable checkpoint rather than a broad unfinished investigation.

## Scientific firewall

This is an operational mitigation only. It changes no frozen scientific criterion, no historical result, no claim lock, and no QGR model object.
