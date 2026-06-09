# L3 — If RH fails, infinitely many Li coefficients are negative (Pringsheim route)

**Tag:** PROVED. (The result is standard — it is the "easy" direction of Li's criterion
[Li1997]; the self-contained proof below is recorded to acceptance-criteria standard
because the attempt `attempts/li-positivity/` is built on it and because it is a clean
first formalization target. Nothing here is claimed as new.)

## Setting and definition

Work with `ξ(s) = ½ s(s−1) π^(−s/2) Γ(s/2) ζ(s)`: entire, `ξ(s) = ξ(1−s)`, zeros of `ξ`
= non-trivial zeros of `ζ`, all in the open strip `0 < Re(s) < 1` (docs/00, docs/02).
Let `𝔻 = {|z| < 1}` and define

```
h : 𝔻 → ℂ,        h(z) = ξ( 1/(1−z) ),
G : 𝔻 ⇢ ℂ,        G(z) = h'(z)/h(z)        (meromorphic on 𝔻).
```

`h` is holomorphic on `𝔻` (composition of `z ↦ 1/(1−z)`, holomorphic on `ℂ∖{1}`, with
the entire `ξ`), and `h(0) = ξ(1) = ½ ≠ 0` ([L2] (3)), so `G` is holomorphic in a
neighborhood of `0`.

**Definition (Li coefficients).** `λ_n` (`n ≥ 1`) are the Taylor coefficients of `G`
at `0`:

```
G(z) = Σ_{n≥1} λ_n z^(n−1)        (|z| small).
```

> **Remark (convention).** This agrees with Li's original definition
> `λ_n = (1/(n−1)!) (d/ds)^n [ s^(n−1) log ξ(s) ] |_{s=1}` and with the zero-sum form
> `λ_n = Σ_ρ [1 − (1 − 1/ρ)^n]` (symmetrically paired) — see [Li1997, Thm 1] and
> [BombieriLagarias1999, Thm 1]. **The equivalence is cited context, not used below**;
> everything in this lemma refers to the Taylor-coefficient definition. (Numerical
> cross-check of the convention: `scratch/li-coefficients/`, which confirms
> `λ₁ = 1 + γ/2 − ½log(4π)` to ~60 digits.) Working with `G = h'/h` rather than `log h`
> avoids any branch choice (doc 06 §7).

## Statement

Suppose RH is false. Then:

1. `r₀ := min { |1 − 1/ρ| : ξ(ρ) = 0, Re(ρ) > 1/2 }` exists and `0 < r₀ < 1`;
2. the Taylor series of `G` at `0` has radius of convergence exactly `r₀`; consequently
   `limsup_{n→∞} |λ_n|^(1/n) = 1/r₀ > 1`;
3. `λ_n < 0` for **infinitely many** `n`.

Contrapositive: **if `λ_n ≥ 0` for all sufficiently large `n`, then RH holds.**

## Proof

**Step 1 (zeros of `h` in `𝔻`).** By [L1] (2), `s(z) = 1/(1−z)` is a bijection
`𝔻 → {Re(s) > 1/2}` with inverse `w(s) = 1 − 1/s`. Hence

```
Z := {z ∈ 𝔻 : h(z) = 0} = { w(ρ) : ξ(ρ) = 0, Re(ρ) > 1/2 }.
```

**Step 2 (RH false ⟹ `Z ≠ ∅`).** If some non-trivial zero has `Re(ρ) ≠ 1/2`, then
either `Re(ρ) > 1/2`, or `Re(1−ρ) > 1/2` and `1−ρ` is also a zero by the functional
equation (docs/00 §2). Either way `Z` contains `w(ρ★)` for some zero `ρ★` with
`Re(ρ★) > 1/2`, and `r★ := |w(ρ★)| < 1` by [L1] (1).

**Step 3 (the minimum `r₀` is attained; conclusion 1).** Fix `r := (1+r★)/2 < 1`. By
[L1] (4), `{z : |z| ≤ r} ∩ Z` corresponds to the zeros of `ξ` in the compact set
`K_r ⊂ {Re(s) > 1/2}`. Since `ξ` is entire and `ξ ≢ 0` (`ξ(1) = ½`), its zeros are
isolated with no accumulation point in `ℂ`, so `K_r` contains finitely many of them.
The set `{|z| ≤ r} ∩ Z` is thus finite and non-empty (it contains `w(ρ★)`), so
`r₀ = min{|z| : z ∈ Z}` is attained at some `w₀ ∈ Z`. Moreover `r₀ > 0` because
`h(0) = ½ ≠ 0`, and `r₀ ≤ r★ < 1`. ∎(1)

**Step 4 (singularities of `G` in `𝔻`).** `G = h'/h` is holomorphic at every `z ∈ 𝔻`
with `h(z) ≠ 0`. At a zero `z₀ ∈ Z` of multiplicity `m ≥ 1`, write
`h(z) = (z−z₀)^m u(z)` with `u` holomorphic, `u(z₀) ≠ 0`; then
`G(z) = m/(z−z₀) + u'(z)/u(z)` has a simple pole at `z₀` (residue `m ≠ 0`), in
particular `|G(z)| → ∞` as `z → z₀`. So the singularities of `G` in `𝔻` are **exactly**
the points of `Z`, and each is a pole.

**Step 5 (radius of convergence; conclusion 2).** Let `R` be the radius of convergence
of `Σ λ_n z^(n−1)`.

- `R ≥ r₀`: on `{|z| < r₀}` there are no points of `Z` (minimality of `r₀`), so `G` is
  holomorphic there; the Taylor series of a function holomorphic on a disk converges on
  that disk.
- `R ≤ r₀`: otherwise the series defines a holomorphic function `g̃` on `{|z| < R}` with
  `R > r₀`, agreeing with `G` on `{|z| < r₀}`. Then `g̃` is bounded near `w₀` (continuity
  at `w₀`, `|w₀| = r₀ < R`), while `G(z) → ∞` as `z → w₀` radially inside `{|z| < r₀}`
  (Step 4) and `G = g̃` along that approach — contradiction.

So `R = r₀`, and by Cauchy–Hadamard ([Remmert1991]) `limsup |λ_n|^(1/n) = 1/r₀ > 1`
(the index shift `z^(n−1)` vs `z^n` does not affect the limsup of `n`-th roots). ∎(2)

**Step 6 (Pringsheim; conclusion 3).** Suppose for contradiction that `λ_n ≥ 0` for all
`n > N`. Let `P(z) = Σ_{n≤N} λ_n z^(n−1)` (a polynomial) and `G_N = G − P`. Then `G_N`
has the same singularities in `𝔻` as `G` and its Taylor series `Σ_{n>N} λ_n z^(n−1)`
has the same radius `r₀ ∈ (0,1)` (subtracting a polynomial changes neither). Its
coefficients are non-negative, so by **Pringsheim's theorem** ([Remmert1991]: a power
series with non-negative coefficients and finite radius of convergence `R` has a
singular point at `z = R`), the point `z = r₀` is a singular point of `G_N`, hence
of `G`.

By Step 4 the singularities of `G` in `𝔻` are exactly `Z`, so `r₀ ∈ Z`, i.e.
`h(r₀) = ξ(1/(1−r₀)) = 0` with `σ₀ := 1/(1−r₀)` **real and `> 1`** (as `r₀ ∈ (0,1)`).
But for real `σ₀ > 1`,

```
ξ(σ₀) = ½ σ₀(σ₀−1) π^(−σ₀/2) Γ(σ₀/2) ζ(σ₀) ≠ 0,
```

since `σ₀(σ₀−1) > 0`, `π^(−σ₀/2) > 0`, `Γ(σ₀/2) > 0` for positive real argument
(docs/02 §1), and `ζ(σ₀) > 1` by [L2] (1). Contradiction. Hence `λ_n < 0` for
infinitely many `n`. ∎(3) ∎

## Scope notes (read before building on this)

- **This is the criterion direction, not progress toward proving RH.** It converts
  "RH false" into a concrete signature (`λ_n < 0` infinitely often, exponentially large
  in modulus along a subsequence). The open problem — the attempt's actual target — is
  the **positivity** `λ_n ≥ 0 ∀n`, which is equivalent to RH and remains untouched here.
- **Litmus behaviour (doc 06).** Applied to the Davenport–Heilbronn function (with its
  completed `ξ_f` in place of `ξ`), the argument needs `ξ_f ≠ 0` on real `(1,∞)` at
  Step 6 — for `ζ` this came from series positivity ([L2] (1)), which D–H's signed
  coefficients do not grant. And in any case the conclusion for D–H would only be "some
  `λ_n(f) < 0`" — exactly what its off-line zeros predict. The lemma cannot be misused
  to "prove RH" for D–H; it makes no positivity claim. See the litmus section of
  `attempts/li-positivity/PROOF.md`.

## Used by

- `attempts/li-positivity/` (frames the target; supplies the failure signature).

## Checks (doc 06 audit)

- **§1 circularity:** RH is *assumed false* (for the contrapositive); no equivalent of
  RH, Lindelöf, or any open conjecture is invoked. Inputs: [L1], [L2], docs/00 §2
  symmetry, entirety of `ξ`, Pringsheim + Cauchy–Hadamard [Remmert1991].
- **§2 interchanges:** none performed; all function-theoretic steps are cited theorems
  with hypotheses checked (Taylor convergence on disks, Pringsheim, Cauchy–Hadamard).
- **§3 domain discipline:** the Dirichlet series for `ζ` enters only via [L2] (1) at
  real `σ > 1`.
- **§5 functional-equation sleight of hand:** the FE is used only to replace a zero by
  its partner `1−ρ` (Step 2) — no symmetry-forces-onto-the-line claim.
- **§6 product convergence:** the Hadamard product is not used at all (that is *why*
  the `h'/h` route was chosen over the zero-sum form of `λ_n`).
- **§7 branches:** no `log ξ` is taken; `G = h'/h` is single-valued.
- **§11 quantifiers:** the conclusion is `∀N ∃n>N : λ_n<0`, proved by contradiction
  against `∃N ∀n>N : λ_n≥0` — order explicit in Step 6.
