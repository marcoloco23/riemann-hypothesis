# PROGRESS LOG — Riemann Hypothesis

> **This file is the source of truth and must survive context loss.** Update it at the end
> of every work session. A fresh agent should be able to read only this file (plus the
> linked attempt `STATUS.md` files) and know exactly where things stand and what to do next.
> Newest entries on top.

## Current status

**Phase:** Repository prepared; no solution attempt started yet.
**Headline:** Scaffolding complete. Read `docs/00`–`07` in order, then open the first
attempt under `attempts/`.

## Definition of done (from docs/01)

A complete rigorous proof (or disproof) of the docs/00 statement, every step proved or
cited, passing all docs/06 litmus tests and the docs/07 protocol, ideally formalized in Lean
(`formal/`). Anything less is **progress, not a solution**, and is recorded as such.

## Active threads

| Thread | Approach family (docs/05) | Status | Current blocker (one sentence) |
|--------|---------------------------|--------|--------------------------------|
| _(none yet)_ | — | — | Start by choosing an approach and creating `attempts/<slug>/`. |

## Proved lemmas (in `lemmas/`)

_(none yet)_

## Dead ends recorded (in `scratch/` or attempt `STATUS.md`)

_(none yet — record every one so it isn't retried)_

## Suggested first moves for the solving agent

1. Read all of `docs/` in order. Internalize docs/01 (the bar), docs/06 (litmus tests), and
   docs/07 (verification) especially.
2. Skim mathlib's existing zeta development (`formal/README.md`) to know what is already
   formalized and reusable.
3. Pick **one** approach from docs/05 whose machinery you can control end‑to‑end, and write
   down *precisely which open step* you intend to attack (don't restart a known wall blindly).
4. Create `attempts/<slug>/` from the template; state the new input that gives you a chance
   where the approach previously stalled.
5. Before investing heavily, dry‑run your intended method against **LITMUS‑1
   (Davenport–Heilbronn)**: if the method would also "prove RH" for it, discard early.
6. Keep this log current.

## Session history

- **(setup)** Repository scaffolded: problem statement, acceptance criteria, background,
  equivalent formulations, known results, approaches/dead‑ends, pitfalls/litmus tests,
  verification protocol, workspace + formal + references structure, root CLAUDE.md. No
  mathematical attempt made yet.
