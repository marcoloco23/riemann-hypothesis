# 06 — Pitfalls and Mandatory Litmus Tests

Most claimed proofs of RH are wrong, and they tend to be wrong in the **same few ways**.
This document is the checklist a hostile reviewer will run. Run it on yourself first. Items
marked **LITMUS** are mandatory gates in the acceptance criteria (doc 01 B5).

---

## Part 1 — The litmus tests (a method must pass ALL of these)

The deepest trap: an argument that uses only properties **shared by functions known to
violate RH**. Such an argument cannot be valid, because it would "prove" a false statement.
Before believing any method, apply it to the following and confirm it **fails** for them.

### LITMUS‑1 — Davenport–Heilbronn function `f(s)` (the single most important test)

Construct `f(s) = ½(1 − iκ) L(s, χ) + ½(1 + iκ) L(s, χ̄)`, where `χ` is the character mod 5
with `χ(2) = i` and `κ = (√(10 − 2√5) − 2)/(√5 − 1)`. This function:

- has a **Dirichlet series** and **analytic continuation** to `ℂ`;
- satisfies a **functional equation of the same shape as `ζ`** (relating `s` and `1−s` with
  the same kind of gamma factor);
- but has **NO Euler product** (it is not multiplicative); and
- **has infinitely many zeros off the critical line** — including zeros with `Re(s) > 1`,
  and (Bombieri–Hejhal) a positive proportion of its critical‑strip zeros lie off the line.

> **Gate.** If your argument, applied to `f(s)`, would conclude "all zeros on `Re=1/2`,"
> your argument is **wrong** — `f` is a counterexample. A correct proof must use a property
> `ζ` has and `f` lacks. In practice that property is the **Euler product /
> multiplicativity**. State explicitly, in the proof, the line where Euler‑product structure
> is used and why the argument breaks for `f`.

### LITMUS‑2 — Epstein zeta functions `ζ_Q(s)`

For a positive‑definite binary quadratic form `Q` whose class number is `> 1`, the Epstein
zeta `ζ_Q(s) = Σ'_{(m,n)} Q(m,n)^(−s)` has a functional equation but (in general) no Euler
product, and is known to have **zeros off the critical line** (and in `σ>1`). Same gate as
LITMUS‑1: a method blind to the Euler product will wrongly "prove RH" for `ζ_Q`.

### LITMUS‑3 — Does it prove too much in `σ > 1`?

`f` and many `ζ_Q` have zeros with `Re(s) > 1`. `ζ` has none there — *but only because of
the Euler product*. If your argument establishes a zero‑free region for `Re(s) > 1/2`
without ever invoking the Euler product, it would also (falsely) clear `σ>1` for `f`. Red
flag.

### LITMUS‑4 — Consistency with `Λ ≥ 0`

The de Bruijn–Newman constant satisfies `Λ ≥ 0` (Rodgers–Tao; doc 03 §12), so RH, if true,
is true with **zero margin**. Any proof that would yield a zero‑free strip of *positive
width* around the line, or otherwise "extra room," contradicts `Λ ≥ 0` and is wrong.

### LITMUS‑5 — Selberg‑class sanity

The Selberg class includes the Euler product as an axiom precisely to exclude
Davenport–Heilbronn/Epstein. If your method would apply to every function with a Dirichlet
series + functional equation, it ignores the defining axiom and fails LITMUS‑1/2 by
construction.

---

## Part 2 — Recurring technical errors (audit every one)

1. **Circular reasoning / assuming the conclusion.** Using RH, an equivalent (doc 03),
   Lindelöf, a zero‑density hypothesis, or "the zeros are symmetric so…" in a way that
   presupposes them on the line. The most common fatal error. Grep every lemma.

2. **Illegitimate interchange of limits/sums/integrals.** Swapping `Σ` and `∫`, `lim` and
   `Σ`, differentiating under the integral, or rearranging a conditionally convergent
   series without absolute/uniform convergence justification. The zero‑sum
   `Σ_ρ x^ρ/ρ` is only **conditionally** convergent — order of summation matters.

3. **Using an identity outside its domain.** The Dirichlet series and Euler product hold
   **only for `σ>1`**; `−ζ'/ζ = ΣΛ(n)n^(−s)` and `1/ζ=Σμ(n)n^(−s)` likewise. Applying any
   of them on the critical line or in the strip is invalid without analytic continuation —
   and continuation does **not** carry the series representation with it.

4. **Mishandling the analytic continuation / the pole.** Forgetting the simple pole at
   `s=1`, or treating the continued `ζ` as if its defining series still converges.

5. **Functional‑equation sleight of hand.** Concluding "zeros symmetric about `1/2`,
   therefore on `1/2`." Symmetry gives pairs `ρ, 1−ρ`; it does **not** force `ρ=1−ρ`.
   `f` and `ζ_Q` have the same symmetry and off‑line zeros.

6. **Convergence/order errors in products.** Manipulating the Hadamard product without the
   convergence‑forcing pairing of `ρ` with `1−ρ`; ignoring the genus/`exp` factor.

7. **Branch‑cut / multivaluedness.** `log ζ`, `ζ^α`, `arg ζ` are multivalued; `S(T)` jumps
   at zeros. Errors hide in an unstated branch choice.

8. **Numerics masquerading as proof.** "Checked to `10^N`" proves nothing about all zeros
   (doc 01 B1; the Mertens conjecture died this way — doc 03 §3). Floating point cannot
   certify `ζ(ρ)=0` (doc 01 D).

9. **Real‑analysis on a complex problem.** Treating `ζ(σ+it)` as if positivity/monotonicity
   in one variable controls the complex zero set.

10. **Hidden use of an unproven conjecture.** Lindelöf, pair‑correlation, GUE, a moment
    conjecture, a subconvexity bound stronger than what is proven — all are open. Cite doc
    04 for what is actually established; anything beyond it must be proved in‑repo.

11. **Order‑of‑quantifiers slips.** "For every `ε` there is `T`…" vs "there is `T` for every
    `ε`…"; uniform vs pointwise bounds. RH is a statement about **all** zeros simultaneously.

12. **`ε`/exponent mismatches in equivalences.** Doc 03's equivalences are exponent‑precise;
    proving a near‑miss bound is not proving the equivalent statement.

---

## Part 3 — The "would an expert believe this in 5 minutes?" filter

If the proposed proof is **short and elementary**, prior probability it is correct is
extremely low — 165 years of effort by Hardy, Selberg, Levinson, Connes, Deligne‑adjacent
programs, etc. have not found a short proof. A short argument almost certainly (a) is
circular, (b) uses an identity out of domain, or (c) fails a litmus test. This is not proof
that short proofs can't exist — it is a calibration of where to look for your own error
**first**. Find the bug before claiming the theorem.
