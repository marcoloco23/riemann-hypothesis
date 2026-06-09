# 07 — Verification Protocol

How a claimed result is checked **before** it is announced as a solution. No result leaves
`workspace/` as "solved" until it has passed this protocol. Treat verification as adversarial:
the goal of this phase is to **break** the argument, not to confirm it.

## Stage 0 — Statement check

- [ ] The theorem actually proved is **verbatim** the doc‑00 statement (or a doc‑03
      equivalent, with the equivalence itself proved/cited). Guard against proving a weaker,
      stronger, or subtly different proposition.
- [ ] If formalized: the Lean statement is confirmed by inspection to be RH, not a vacuous
      or mis‑typed proposition (a kernel‑checked proof of the wrong statement is worthless).

## Stage 1 — Self audit against doc 06

- [ ] Every item in [06-pitfalls-and-litmus-tests.md](06-pitfalls-and-litmus-tests.md)
      Part 2 explicitly checked against the argument, with a one‑line note on why each does
      not apply.
- [ ] **LITMUS‑1 (Davenport–Heilbronn)**: the exact place where the method uses a property
      `f(s)` lacks (Euler product/multiplicativity) is identified, and it is shown the
      argument *fails* for `f`. Mandatory.
- [ ] **LITMUS‑2..5** addressed (Epstein; proves‑too‑much in `σ>1`; consistency with
      `Λ ≥ 0`; Selberg‑class sanity).

## Stage 2 — Dependency / circularity audit

- [ ] Build the lemma dependency graph (what uses what). Confirm it is a DAG with no path
      that assumes RH, a doc‑03 equivalent, Lindelöf, or any open conjecture.
- [ ] Every external citation resolved to a specific theorem in
      [references/bibliography.md](references/bibliography.md), with statement matching use.
- [ ] Every in‑repo lemma proved to acceptance‑criteria standard (doc 01 B2–B4).

## Stage 3 — Step‑level rigour pass

- [ ] Every interchange of limit/sum/integral justified (state the convergence theorem and
      check its hypotheses).
- [ ] Every identity used only within its domain of validity; analytic continuations
      explicit.
- [ ] Every contour/argument‑principle/Rouché count has the contour, the bound on the
      relevant arcs, and the winding number written out.
- [ ] Constants and `ε`‑management consistent; quantifier order checked (doc 06 §11).

## Stage 4 — Independent re‑derivation of load‑bearing lemmas

- [ ] Identify the 1–3 lemmas the whole proof rests on ("if any one is false, RH does not
      follow"). For each, produce an **independent** re‑proof or a second route to the same
      conclusion, ideally by a separate agent/reviewer who has not seen the first proof.
- [ ] A dedicated **red‑team pass**: an agent whose only instruction is "find the fatal
      error; assume one exists." Record what it tried and why the argument survived.

## Stage 5 — Formalization (gold standard)

- [ ] Definitions (`ζ`, `ξ`, zeros, critical line) in Lean 4 match doc 00 — checked against
      mathlib's existing `ζ` to avoid a divergent redefinition.
- [ ] Load‑bearing lemmas formalized and kernel‑checked.
- [ ] Main theorem formalized; `#print axioms` shows no `sorry` and no unexpected axioms
      (only standard mathlib axioms: `propext`, `Classical.choice`, `Quot.sound`).
- [ ] Build is reproducible from `formal/` per its README (toolchain pinned).
- [ ] Any step **not** formalized is listed explicitly with the residual human‑review risk.

## Stage 6 — Reproducibility & provenance

- [ ] All numerics (motivational or, for a disproof, certified‑interval) scripted, seeded,
      tool/version pinned, re‑runnable from the repo.
- [ ] For a **disproof**: the off‑line zero is certified by validated interval arithmetic
      (e.g. `arb`/ball arithmetic + argument principle), not floating point (doc 01 D).
- [ ] `workspace/PROGRESS.md` updated to reflect verified status honestly.

## Stage 7 — Decision

A result is announced as a **solution** only when:

- Stages 0–4 and 6 are complete with no open item, **and**
- Stage 5 is complete (full formalization) — **or**, if not, the residual unformalized steps
  are explicitly enumerated, each independently re‑derived (Stage 4) and reviewed, with the
  remaining risk stated plainly to the user.

Otherwise the result is recorded as **progress** (partial / conditional / unverified) with
its exact status in `PROGRESS.md`. When in doubt, it is progress, not a solution.

---

### Reviewer mindset (read before each verification)

> Assume the proof is wrong and your job is to locate the flaw. A proof of RH is an
> extraordinary claim; the default outcome of this protocol is "found the error." Only after
> a genuine, hostile attempt to break it has failed across all stages is the result
> credible. Confirmation bias is the enemy — reward finding the bug, not confirming the
> theorem.
