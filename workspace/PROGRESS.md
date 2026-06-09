# PROGRESS LOG — Riemann Hypothesis

> **This file is the source of truth and must survive context loss.** Update it at the end
> of every work session. A fresh agent should be able to read only this file (plus the
> linked attempt `STATUS.md` files) and know exactly where things stand and what to do next.
> Newest entries on top.

## Current status

**Phase:** First attempt opened and scaffolded. **RH is NOT solved; no claim of solution
exists in this repository.**
**Headline:** Attempt `li-positivity` (Weil positivity via Li's criterion, docs/05 §3 /
docs/03 §8) is OPEN with proved scaffolding (lemmas L1–L3), a completed litmus audit of
the frame, reproducible numerics, and one scoped sub-target (Q1). The actual wall —
proving `λ_n ≥ 0` unconditionally — is untouched, as recorded honestly in the attempt.

## Definition of done (from docs/01)

A complete rigorous proof (or disproof) of the docs/00 statement, every step proved or
cited, passing all docs/06 litmus tests and the docs/07 protocol, ideally formalized in Lean
(`formal/`). Anything less is **progress, not a solution**, and is recorded as such.

## Active threads

| Thread | Approach family (docs/05) | Status | Current blocker (one sentence) |
|--------|---------------------------|--------|--------------------------------|
| [`attempts/li-positivity/`](attempts/li-positivity/STATUS.md) | §3 Weil positivity / explicit formula (Li's criterion) | OPEN | No mechanism converts `Λ(m) ≥ 0` (entering the explicit formula with a **negative** sign) into `λ_n ≥ 0` for all large `n`; positivity is proved only for test functions whose support excludes every prime ([ConnesConsani2021]). |

**Next actions for thread (in order, from its STATUS.md):**
1. Transcribe [BombieriLagarias1999, Thm 2] verbatim; re-verify against the numerics.
2. Execute sub-target **Q1**: explicit `N₀(T₀)` with full proof that `λ_n > 0` for
   `n ≤ N₀`, from cited rigorously-verified zeros ([Platt-Trudgian]); main work item is
   the lower bound `Σ_{|γ|≤T₀}(1 − cos nθ_ρ) ≫ n` (sketch in PROOF.md §6).
3. Function-field Li-positivity analogue in `notes/` to localize the missing `Spec ℤ`
   object (PROOF.md §7).
4. Initialize `formal/` (elan/lake not yet installed on this machine) and formalize L1,
   L2 as first targets; then L3 (needs Pringsheim — check mathlib availability).

## Proved lemmas (in `lemmas/`)

| Lemma | Statement (one line) | Tag |
|---|---|---|
| [L1](lemmas/L1-cayley-map-critical-line.md) | `w(s)=1−1/s` maps `{Re>1/2}↔𝔻` biholomorphically; `ρ↦1−ρ` ↔ `w↦1/w`; sublevel sets `{|w|≤r}` compact in `{Re>1/2}` | PROVED |
| [L2](lemmas/L2-zeta-xi-real-axis.md) | `ζ(σ)>1` for real `σ>1`; `ζ<0` on `(0,1)`; `ξ(0)=ξ(1)=½`; `ξ` nowhere zero on `ℝ` | PROVED |
| [L3](lemmas/L3-li-converse-pringsheim.md) | RH false ⟹ `λ_n<0` infinitely often with `limsup|λ_n|^{1/n}>1` (so: `λ_n≥0` eventually ⟹ RH); self-contained Pringsheim proof | PROVED (standard result, [Li1997]; proof in-repo for formalization-readiness) |

All three passed an adversarial re-read this session (one exposition defect found and
fixed in L2 (2b); no mathematical gaps found — a hostile second reader is still wanted,
docs/07 Stage 4).

## Numerics (motivational only, doc 01 B1)

`scratch/li-coefficients/` (Python 3.14.3, mpmath 1.3.0 pinned, dps 60, deterministic;
output `run-output.txt`): `λ_n(ζ) > 0` for `n ≤ 40`, convention pinned to closed-form
`λ₁` at `1.8e−61`; Davenport–Heilbronn `Ξ_f(s)=Ξ_f(1−s)` confirmed to `~1e−60` with the
root-number identity `(1+iκ)/(1−iκ)=τ(χ)/(i√5)` exact to `1.1e−61`; Spira's off-line
zero `0.80851718…+85.69934849…i` reproduced; predicted first negative `λ_n(f)` at
`n ~ 3.5e5` (single-zero heuristic) — calibrates how little low-`n` positivity means.

## Dead ends recorded (in `scratch/` or attempt `STATUS.md`)

- **Failure modes pre-recorded for li-positivity** (PROOF.md §4): termwise positivity of
  the zero-sum; positivity from the functional equation alone (dies on LITMUS-1);
  archimedean-only convexity bounds. Do not retry.
- **Numerics pitfall** (scratch/li-coefficients/README.md): module-level constants
  materialized before setting precision froze κ at 15 digits and faked a `1e−17` FE
  violation; always set precision first and keep an exact cross-check identity.

## Session history

- **2026-06-09 (session 1 of solving agent).** Read docs/00–07 in full. Opened
  `attempts/li-positivity/` (family docs/05 §3; open step: the positivity wall;
  litmus audit of the frame passed — no positivity claim made anywhere). Proved and
  audited lemmas L1–L3. Built reproducible Li-coefficient numerics for ζ and
  Davenport–Heilbronn; pinned conventions against exact identities. Scoped sub-target
  Q1 (finite-range unconditional positivity from verified zeros). Added bibliography
  entries (Bombieri–Lagarias, Connes–Consani, Maślanka, Remmert, Apostol, Spira).
  **No progress at the actual wall; RH remains open.** Lean toolchain absent —
  formalization deferred to next session (action 4 above).
- **(setup)** Repository scaffolded: problem statement, acceptance criteria, background,
  equivalent formulations, known results, approaches/dead‑ends, pitfalls/litmus tests,
  verification protocol, workspace + formal + references structure, root CLAUDE.md. No
  mathematical attempt made yet.
