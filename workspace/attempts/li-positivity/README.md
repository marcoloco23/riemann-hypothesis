# Attempt: `li-positivity` — Li's criterion inside the Weil-positivity program

**Approach family (docs/05):** §3 *Weil positivity / explicit-formula programs*, in the
concrete specialization of **Li's criterion** (docs/03 §8): RH ⟺ `λ_n ≥ 0` for all
`n ≥ 1`. By [BombieriLagarias1999], the `λ_n` are values of the Weil functional at a
specific sequence of test functions, so this is the positivity crux of docs/05 in its
most concrete clothing: a single explicit sequence of real numbers, with both a
zero-sum side and an arithmetic (prime) side.

**Open step being attacked (per docs/05 §3):** the positivity wall — convert the
arithmetic structure of `ζ` (Euler product; `Λ(n) ≥ 0`) into `λ_n ≥ 0` for *all* `n`.
Positivity is known only for restricted test-function classes (support not reaching the
first prime, [ConnesConsani2021]); the Li test functions have effective support growing
like `log n`, so *every* prime eventually enters — exactly the regime nothing covers.

**New input claimed for this session:** none at the wall itself — and that is recorded
honestly. This session establishes the attack surface to acceptance-criteria standard:
proved scaffolding lemmas ([L1], [L2], [L3]), the mandatory litmus analysis (PROOF.md
§5), reproducible numerics grounding the criterion on both `ζ` and the
Davenport–Heilbronn counterexample (`scratch/li-coefficients/`), and one *scoped,
plausibly-completable* sub-target: unconditional positivity `λ_n > 0` for an explicit
finite range `n ≤ N₀` derived from cited rigorously-verified zeros (PROOF.md §6) —
genuine partial progress per docs/05 ("partial credit is real"), not RH.

**Files:** [PROOF.md](PROOF.md) (the developing argument), [STATUS.md](STATUS.md)
(blocker, one sentence), `notes/` (attempt-local scratch).
