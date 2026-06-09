# 05 — Major Approaches and Where They Stall

A survey of the serious programs aimed at RH, what each buys, and the **specific obstacle**
that has stopped it. Purpose: don't restart a known dead end at the same wall; if you pick
one of these, know exactly which step is the open one and aim your novelty there.

None of these is "wrong" — each has produced real mathematics. They are *unfinished*, and
each has a precise sticking point.

## 1. Hilbert–Pólya / spectral

**Idea.** Find a self‑adjoint operator `H` whose eigenvalues are the `t` with `1/2+it` a
zero. Self‑adjoint ⟹ real spectrum ⟹ RH.

**Status / wall.** No such operator is known. The **Berry–Keating** heuristic identifies a
candidate classical Hamiltonian `H = xp` whose semiclassical density matches `N(T)`, but no
rigorous quantum operator with the exact spectrum exists; boundary conditions and the
"missing" arithmetic content are unresolved. Random‑matrix agreement (GUE) is strong
evidence the spectrum is "random‑matrix‑like" but proves nothing.

**Open step to target.** Construct the operator *and* prove its spectrum is exactly the
zero set — not merely density‑matching.

## 2. Connes / noncommutative geometry & trace formulas

**Idea.** Realize the zeros as an absorption spectrum on a noncommutative space (adèle
classes); RH ⇔ a **positivity** (Weil positivity, doc 03 §9) in a trace formula.

**Status / wall.** Connes reduces RH to a trace‑formula positivity statement, but proving
that positivity is exactly as hard as RH; the geometric side has not been made to yield it
unconditionally. Recent Connes–Consani work on the "Riemann–Weil explicit formula as a
trace" and prolate/semilocal analysis is active but has not closed the gap.

## 3. Weil positivity / explicit‑formula programs

**Idea.** RH ⇔ `Σ_ρ \hat f(ρ) ≥ 0` for all admissible `f` (doc 03 §9). Try to prove the
quadratic form is positive‑definite directly.

**Status / wall.** Reduces to controlling an infinite sum of local terms; positivity is
known for restricted test‑function classes only. Bombieri and others formalized the
program; the general positivity is open. Li's criterion (doc 03 §8) is the same wall in
"`λ_n ≥ 0`" clothing — the `λ_n` are positive numerically but no proof of universal
positivity exists.

## 4. Function‑field analogy / arithmetic geometry

**Idea.** RH is a *theorem* over function fields (Weil, Deligne; doc 04 §G). Transport the
proof — positivity of intersection numbers / cohomological weights — to `Spec ℤ`.

**Status / wall.** There is no working cohomology theory over `Spec ℤ` playing the role of
étale cohomology over a curve. Programs: **Arakelov geometry**, **the field with one
element `𝔽₁`**, Connes–Consani, Deninger's conjectural dynamical/cohomological framework.
All are frameworks in search of the missing object; none yields the positivity
unconditionally. This is widely seen as the "deepest" direction and the least complete.

## 5. de Branges (Hilbert spaces of entire functions)

**Idea.** Use de Branges spaces `H(E)` and their structure theory to force zeros onto the
line via a positivity condition on a reproducing kernel.

**Status / wall.** de Branges announced proofs multiple times; **gaps were found** (notably
Conrey–Li 2000 exhibited a counterexample to a key positivity hypothesis as applied). The
machinery is real and powerful but the specific RH application has not survived scrutiny.
⚠️ A high‑profile cautionary case: structurally elaborate, repeatedly believed, repeatedly
refuted. If you go here, the Conrey–Li obstruction is the first thing to clear.

## 6. Moments, mollifiers, and proportion‑on‑line

**Idea (Levinson–Conrey, doc 04 §B).** Mollify `ζ` and count sign changes / use the
argument principle to bound the proportion of zeros on the line from below.

**Status / wall.** Genuinely unconditional and improving, but the method is **structurally
capped below 100%** — it counts a positive proportion, and pushing to "all" appears to need
a fundamentally new input. Good for partial results; not a path to full RH as‑is.

## 7. Probabilistic / statistical‑physics

**Idea.** Model `ζ` via random multiplicative functions, branching random walk, log‑correlated
fields (Fyodorov–Hiary–Keating maxima), statistical‑mechanics analogies.

**Status / wall.** Predicts fine statistics of `ζ` on the line spectacularly well, but these
are *distributional* statements; none constrains *every* zero's real part. Evidence‑generating,
not proof‑generating.

## 8. Elementary‑criterion attacks (Robin, Lagarias, Nicolas)

**Idea.** Prove the elementary inequalities of doc 03 §6–7 directly by analytic number
theory on `σ(n)`, superabundant/colossally abundant numbers, etc.

**Status / wall.** The inequalities are *equivalent* to RH — equally hard. Nicolas/Robin
results pin the extremal numbers but the inequality for all large `n` is open. These are the
richest source of **plausible‑looking false proofs** (doc 06): short arguments that secretly
need RH.

---

## Cross‑cutting lessons for any new attempt

- **The Euler product must enter.** Every serious program eventually needs the
  multiplicative structure (primes), because the functional equation alone is shared by
  functions that violate RH (doc 06). If your argument never uses primes/the Euler product,
  be very suspicious.
- **Positivity is the recurring crux.** Weil positivity, Li's `λ_n≥0`, de Branges kernels,
  intersection positivity — RH keeps reducing to "a certain quadratic form is ≥ 0," and
  *that* is the wall. Novelty is most valuable aimed there.
- **`Λ ≥ 0` (doc 03 §12) says there is no slack.** A proof must be tight, not produce a
  zero‑free region of positive width around the line "for free" — that would prove too much.
- **Partial credit is real.** Improving the proportion on the line, narrowing the
  zero‑free region, proving new conditional implications, or formalizing existing results in
  Lean are all worthwhile deliverables to record even if full RH is not reached.
