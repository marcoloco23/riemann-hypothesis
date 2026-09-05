# Contributor and agent operating rules

This repository is an open research project on the Riemann hypothesis. Human and
machine-assisted contributors follow the same mathematical status and provenance rules.

Read [`docs/00`–`07`](docs/) in order, then read [`CLAIMS.md`](CLAIMS.md),
[`workspace/PROGRESS.md`](workspace/PROGRESS.md), and the status file for the attempt you
will change.

## Non-negotiable rules

1. Do not claim that RH is solved unless the complete acceptance and verification
   protocols pass. Partial results remain partial results.
2. Never assume RH, an equivalent statement, Lindelöf, pair correlation, an open
   zero-density conjecture, or the desired conclusion inside a lemma.
3. Treat numerics as motivation or regression evidence unless a rigorous interval
   certificate covers every needed error and tail.
4. State domains of convergence and justify every interchange, continuation, contour
   shift, and limit.
5. Run structure-matched negative controls, especially Davenport-Heilbronn, early.
6. Prove each nontrivial step or cite a primary source with an exact statement match.
7. Preserve refutations and failed approaches. Downgrade a claim immediately when a
   counterexample or load-bearing gap is found.
8. Disclose substantial machine assistance. An AI audit does not count as independent
   human review.

## Repository discipline

- Update `workspace/PROGRESS.md` and affected status files with every research change.
- Put one serious strategy in each `workspace/attempts/<slug>/` directory.
- Promote stable, self-contained subresults to `workspace/lemmas/`.
- Keep exploratory programs and negative results in `workspace/scratch/` with exact
  dependency versions, commands, and selected output.
- Reuse mathlib's standard zeta definitions in Lean and pin the toolchain and dependency
  revisions.
- Run `python3 scripts/verify.py --quick` before submitting a pull request.

Contribution mechanics, evidence states, and governance are defined in
[`CONTRIBUTING.md`](CONTRIBUTING.md) and [`GOVERNANCE.md`](GOVERNANCE.md).
