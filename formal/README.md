# Formal Verification (Lean 4 + mathlib)

Machine‑checked formalization is the gold standard of acceptance (docs/01 §C, docs/07
Stage 5). This directory will hold the Lean development: definitions matching docs/00,
load‑bearing lemmas, and ultimately the main theorem.

## Why Lean here

- The Lean kernel checks proofs mechanically — it does not get tired, fooled, or biased,
  which is exactly the failure mode that has sunk past RH "proofs" (docs/06).
- **mathlib already contains the relevant objects**, so you build on a verified foundation
  rather than re‑axiomatizing analysis. As of recent mathlib this includes (verify exact
  names against the installed version — the API moves):
  - `riemannZeta : ℂ → ℂ` — the Riemann zeta function (analytic continuation).
  - `riemannZeta_one_sub` / completed zeta `completedRiemannZeta` (`Λ`/`ξ`) and the
    **functional equation** `completedRiemannZeta_one_sub`.
  - The simple pole at `s = 1`, special values, the trivial zeros, and Dirichlet series
    machinery (`LSeries`, `ArithmeticFunction`, von Mangoldt, Möbius).
  - The **Prime Number Theorem** has been formalized in mathlib — its zero‑free‑line and
    analytic infrastructure is directly reusable.

> ⚠️ Do **not** redefine `ζ` from scratch. Reuse mathlib's `riemannZeta` so the statement
> you prove is provably the standard one (docs/07 Stage 0). A correct proof of a *divergent*
> definition proves nothing about RH.

## The statement to land

```lean
-- Target (informal rendering — pin exact form to mathlib's defs):
theorem riemann_hypothesis (s : ℂ) (hs : riemannZeta s = 0)
    (htriv : ∀ n : ℕ, 0 < n → s ≠ -2 * n) : s.re = 1 / 2

-- Cleaner via the completed zeta (entire; zeros = non-trivial zeros):
theorem riemann_hypothesis' (s : ℂ) (hs : completedRiemannZeta s = 0) : s.re = 1 / 2
```

Confirm the chosen form against mathlib's actual definitions before committing to it; the
two must be proved equivalent if both are used.

## Setup (to be initialized when formal work begins)

```bash
# Install elan (Lean toolchain manager), then:
lake +leanprover/lean4:stable new rh math      # or `lake init` in this dir
# add mathlib as a dependency in lakefile, then:
lake exe cache get                              # fetch prebuilt mathlib oleans
lake build
```

Pin the toolchain in `lean-toolchain` and the mathlib revision in `lake-manifest.json` so
the build is reproducible (docs/07 Stage 5). Record the exact versions here once set.

## Conventions

- Mirror the repository's lemma structure: each `workspace/lemmas/<name>.md` that is
  formalized gets a corresponding Lean lemma; cross‑reference both ways.
- Keep `sorry` out of anything claimed as proved. Before announcing, run `#print axioms` on
  the main theorem and confirm only standard axioms appear (`propext`, `Classical.choice`,
  `Quot.sound`) — no `sorryAx`, no extra axioms.
- If a step resists formalization, that is a signal: either the informal step is shakier
  than it looks, or it needs a missing mathlib lemma (which itself must then be proved).

## Status

Not yet initialized — set up the Lake project when the first lemma is ready to formalize.
Until then, this README is the spec.
