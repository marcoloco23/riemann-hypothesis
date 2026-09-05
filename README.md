# The Riemann Hypothesis — Research Repository

> **Current status:** RH remains open. This repository contains no claimed proof or
> disproof. See the public [`CLAIMS.md`](CLAIMS.md) ledger for the exact evidence state
> of every highlighted result.

This is an open, community-oriented research workspace for rigorous and reproducible
work around the Riemann hypothesis. It preserves written arguments, computations,
counterexamples, failed approaches, audits, and formalization plans so other researchers
can verify, correct, reuse, or continue them.

The long-term mission is a complete, rigorous, and preferably machine-verifiable proof
or disproof. Until that bar is met, the repository reports narrower results with explicit
evidence labels and review gaps. Substantial machine assistance is disclosed; it never
counts as independent human review.

## Current research snapshot

- L8 records a carefully normalized Riemann-Weil explicit formula and two uniqueness
  results.
- L9 gives a written proof that the fixed-background positive-comb class considered by
  the Fourier-rigidity attempt is a singleton. This characterizes the class; it does not
  establish zero reality.
- L10 derives a Davenport-Heilbronn completion and signed-comb explicit formula as a
  structure-matched negative control.
- The Dimitrov-Xu record identifies and reproduces an apparent error in a published
  theorem and derives a corrected kernel. Author and journal correspondence remains
  pending.
- Several tempting strategies are retained with explicit numerical or mathematical
  counterexamples.

L8–L10 are `PROVED-WRITTEN`: full arguments are present, but independent human review
and Lean verification remain open. The detailed status is in
[`workspace/PROGRESS.md`](workspace/PROGRESS.md).

---

## How to read this repository (start here)

Read the docs **in order**. They are designed to be read once, top to bottom, before any
work begins.

| # | Document | What it gives you |
|---|----------|-------------------|
| 00 | [docs/00-problem-statement.md](docs/00-problem-statement.md) | The exact statement to be proved or disproved, with all definitions. |
| 01 | [docs/01-acceptance-criteria.md](docs/01-acceptance-criteria.md) | What counts as a solution. Non‑negotiable bar. Read twice. |
| 02 | [docs/02-background.md](docs/02-background.md) | Definitions and standard facts you may use without proof. |
| 03 | [docs/03-equivalent-formulations.md](docs/03-equivalent-formulations.md) | Equivalent statements — alternative attack surfaces. |
| 04 | [docs/04-known-results.md](docs/04-known-results.md) | What is already proven. Do not re‑derive; cite. |
| 05 | [docs/05-approaches-and-deadends.md](docs/05-approaches-and-deadends.md) | Major strategies tried and where they stall. |
| 06 | [docs/06-pitfalls-and-litmus-tests.md](docs/06-pitfalls-and-litmus-tests.md) | Why most "proofs" are wrong. Mandatory sanity checks. |
| 07 | [docs/07-verification-protocol.md](docs/07-verification-protocol.md) | How a claimed result must be checked before it is announced. |
| 08 | [docs/08-community-integration.md](docs/08-community-integration.md) | How to publish this work openly and connect modular claims to Tao's IEANTN project. |
| 09 | [docs/09-publication-checklist.md](docs/09-publication-checklist.md) | Release readiness and remaining GitHub account actions. |

Reference material: [references/bibliography.md](references/bibliography.md).

Community and verification material:

- [Claim index](CLAIMS.md)
- [Contributing guide](CONTRIBUTING.md)
- [Governance](GOVERNANCE.md)
- [Reproducibility](REPRODUCIBILITY.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Community integration and IEANTN path](docs/08-community-integration.md)

## Where work happens

```
workspace/
  PROGRESS.md     <- running log; survives context loss. Update it constantly.
  attempts/       <- one subdir per serious strategy. Self-contained write-ups.
  lemmas/         <- proved supporting results, each independently checkable.
  scratch/        <- exploration, numerics, dead ends (kept, not deleted).
formal/           <- Lean 4 / mathlib formalization of definitions, lemmas, and the
                     final theorem. Machine verification lives here.
```

See [workspace/README.md](workspace/README.md) and [formal/README.md](formal/README.md)
for the conventions in each.

## Reproduce the maintained checks

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --requirement requirements-ci.txt
python scripts/verify.py --quick
```

The slower explicit-formula suite is `python scripts/verify.py --explicit-formula`.
Numerical agreement is regression evidence; it is not a proof of an infinite claim.

## The one-paragraph rules of engagement

1. A solution is a **proof**, not evidence. Numerics, heuristics, and "all approaches
   point to RH being true" do not count. See doc 01.
2. Every nontrivial step is either proved here or cited to an established result (doc 04).
3. Before claiming success, the argument must pass the **litmus tests** in doc 06 — in
   particular it must fail for the Davenport–Heilbronn function, which has the same
   functional equation as ζ but has zeros off the critical line. A method that cannot
   tell ζ apart from Davenport–Heilbronn is wrong.
4. Keep [workspace/PROGRESS.md](workspace/PROGRESS.md) current so progress survives
   context compaction.

## Participate

Corrections and hostile reviews are especially valuable. Open the matching issue form
for a mathematical review, computational reproduction, correction, or scoped research
proposal. Pull requests must state their evidence level, disclose substantial AI use,
and preserve contradictory evidence and failed attempts.

The project is connecting modular explicit-analytic-number-theory claims to Terence
Tao's [Integrated Explicit Analytic Number Theory Network](https://github.com/teorth/IEANTN).
The first proposed bridge is L8's Riemann-Weil explicit formula; the prepared scope
message is in [`outreach/IEANTN-PROPOSAL.md`](outreach/IEANTN-PROPOSAL.md).

## License and citation

The repository is available under the [Apache License 2.0](LICENSE). Cite the exact
tagged release and claim file you use; machine-readable metadata is in
[`CITATION.cff`](CITATION.cff).
