# The Riemann Hypothesis — Research Repository

> **Mission.** Produce a complete, rigorous, and ideally machine‑verifiable resolution
> of the Riemann Hypothesis (RH): a *proof* that every non‑trivial zero of the Riemann
> zeta function lies on the critical line `Re(s) = 1/2`, **or** a *disproof* exhibiting a
> non‑trivial zero with `Re(s) ≠ 1/2`.

This repository is a structured workspace prepared for an autonomous agent to attempt
RH. It contains the precise problem statement, the acceptance criteria a solution must
meet, the mathematical background, a survey of known results and failed approaches, a
catalogue of pitfalls, and a verification protocol. **No attempt at a solution is made
in these docs** — they exist so that the solving agent starts fully oriented.

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

Reference material: [references/bibliography.md](references/bibliography.md).

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
