# Contributing

This repository welcomes corrections, independent reviews, formalizations,
reproducibility improvements, and carefully scoped research proposals. Read
[`docs/00`–`07`](docs/) and the current [`workspace/PROGRESS.md`](workspace/PROGRESS.md)
before starting mathematical work.

## Choose a contribution type

- **Independent review:** Audit a named claim without relying on its conclusion.
  Record every checked hypothesis, citation, and unresolved gap.
- **Reproduction:** Run an existing computation independently and report the exact
  environment, command, result, and discrepancy, including a zero discrepancy.
- **Correction:** Give the file and line, the smallest counterexample or failed
  inference, and a proposed status downgrade or repair.
- **Formalization:** State exactly which informal claim the Lean declaration models.
  Keep the statement surface small and report `#print axioms`.
- **New research:** Open an issue identifying the precise target, prior work, expected
  failure mode, and a litmus test before opening a large pull request.

Use the GitHub issue forms where possible. Small typo, citation, or code fixes may go
directly to a pull request.

## Evidence labels

Every substantive claim must carry one of these states:

| State | Meaning |
|---|---|
| `CONJECTURED` | A proposed statement with no complete proof. |
| `NUMERICAL` | Supported by computation without a rigorous infinite or interval certificate. |
| `PROVED-WRITTEN` | A complete written argument is present, but independent review is pending. |
| `REVIEWED` | A named independent reviewer checked the stated proof and hypotheses. |
| `MACHINE-CHECKED` | A pinned proof-assistant build checks the exact advertised statement and permitted axioms. |
| `REFUTED` | A proof or reproducible counterexample shows the claim is false. |

Do not infer `REVIEWED` from an author reviewing their own work. Numerical agreement
does not upgrade a statement to `PROVED-WRITTEN`.

## Pull requests

A pull request should:

1. state the exact claim or repository behavior that changes;
2. link the relevant issue or explain why none is needed;
3. identify assumptions and citations with precise locations;
4. include reproducible commands and selected output;
5. update `workspace/PROGRESS.md` and any affected status file;
6. disclose substantial use of AI systems, including which parts were generated or
   checked and what the human contributor verified;
7. avoid announcing progress on RH beyond the evidence state earned by the change.

Run the quick checks before submitting:

```sh
python3 -m pip install -r requirements-ci.txt
python3 scripts/verify.py --quick
```

For explicit-formula changes, also run:

```sh
python3 scripts/verify.py --explicit-formula
```

Pull requests that establish or materially change a mathematical result require an
independent review. A claimed proof or disproof of RH must satisfy the complete
[`docs/07-verification-protocol.md`](docs/07-verification-protocol.md); repository
maintainers will not publicize it before that process is complete.

## Authorship and license

Preserve the authorship and provenance of imported arguments, computations, and data.
Do not submit copyrighted material without permission. By submitting a contribution,
you agree that it may be distributed under the repository's
[Apache License 2.0](LICENSE), as described in section 5 of that license.

Community conduct and decision rules are defined in
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) and [`GOVERNANCE.md`](GOVERNANCE.md).
