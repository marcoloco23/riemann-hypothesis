# Workspace

Where the actual work happens. Conventions below keep the effort organized and, crucially,
**recoverable after context loss** (per the continuity principle: long‑running work must
survive compaction).

## Layout

```
workspace/
  PROGRESS.md     Running log + state of every thread. THE source of truth. Update often.
  attempts/       One subdirectory per serious strategy (see template below).
  lemmas/         Proved supporting results, each self-contained and independently checkable.
  scratch/        Exploration, numerics, dead ends. KEEP these — a recorded dead end saves
                  the next pass from repeating it.
```

## The discipline (non‑negotiable)

1. **Update [PROGRESS.md](PROGRESS.md) at the end of every work session** — what you tried,
   what you proved, what broke, what's next. Assume your context will be wiped; write so a
   fresh instance can resume in five minutes.
2. **One idea per `attempts/<slug>/`.** Self‑contained: its own `README.md` (the idea, in
   one paragraph), `PROOF.md` (the developing argument), `STATUS.md` (open/dead/promising +
   the precise current blocker).
3. **Promote, don't inline.** When a sub‑result is solid, move it to `lemmas/<name>.md` as a
   standalone statement+proof, and cite it from attempts. Each lemma must be checkable on its
   own against doc 01.
4. **Label honestly.** Every claim is tagged `PROVED` / `CONDITIONAL(on …)` /
   `CONJECTURED` / `NUMERICAL` / `FALSE`. Never silently upgrade a tag (doc 01 E12).
5. **Litmus before celebration.** No attempt is marked "promising → solution" until it has
   been run through doc 06 litmus tests and doc 07. Most ideas die at LITMUS‑1; that's the
   point.

## Attempt template

```
attempts/<slug>/
  README.md   One-paragraph idea. Which approach family (doc 05)? What's the new input?
  PROOF.md    The argument as it develops: statement → lemmas → main steps → conclusion.
  STATUS.md   open | dead | promising. The single precise sentence of "what is blocking this
              right now." Updated every session. Link the lemmas it depends on.
  notes/      Scratch specific to this attempt.
```

## Lemma template

```
lemmas/<name>.md
  Statement   Precise, with all hypotheses.
  Tag         PROVED | CONDITIONAL(on X) | CONJECTURED
  Proof       Complete, every step justified or cited (doc 04 / bibliography).
  Used by     Which attempts depend on it.
  Checks      Which doc-06 pitfalls were audited for this lemma.
```

## Numerics

Anything computational goes in `scratch/` (or an attempt's `notes/`), scripted and
reproducible (tool + version + seed). Numerics **motivate**; they never appear in a proof's
logical chain (doc 01 B1) — except certified interval arithmetic in a disproof (doc 01 D).
