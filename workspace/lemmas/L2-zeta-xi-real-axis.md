# L2 — `ζ` and `ξ` on the real axis: signs and non-vanishing

**Tag:** PROVED (standard facts; proofs included in full for self-containment and as
formalization targets; cf. [Titchmarsh §2], [Apostol1976 Ch. 11–12]).

## Statement

Let `ζ` be the Riemann zeta function (docs/00 §1) and
`ξ(s) = ½ s(s−1) π^(−s/2) Γ(s/2) ζ(s)` the completed zeta.

1. For real `σ > 1`: `ζ(σ) > 1`. In particular `ζ(σ) ≠ 0`.
2. For real `s ∈ (0,1)`: `ζ(s) < 0`. In particular `ζ(s) ≠ 0`.
3. `ξ(1) = ξ(0) = 1/2`, and `ξ(σ) ≠ 0` for **all** real `σ`. Consequently every zero of
   `ξ` (equivalently, every non-trivial zero of `ζ`) is non-real.

## Proof

**(1)** For real `σ > 1` the Dirichlet series `ζ(σ) = Σ_{n≥1} n^(−σ)` converges
absolutely (docs/02 §1; we use it only in its domain `σ > 1`, per doc 06 §3). All terms
are positive and the `n=1` term is `1`, so `ζ(σ) ≥ 1 + 2^(−σ) > 1`. ∎(1)

**(2)** Define the Dirichlet eta function `η(s) = Σ_{n≥1} (−1)^(n−1) n^(−s)`.

*(2a) Convergence and positivity of `η` on real `s > 0`.* For fixed real `s > 0` the
sequence `a_n = n^(−s)` is strictly decreasing with limit `0`, so the alternating series
converges, and the alternating-series estimate places the sum strictly between
consecutive partial sums: `η(s) > 1 − 2^(−s) > 0` (the lower bound is the second partial
sum; strictness because the remainders are nonzero). ∎(2a)

*(2b) `η` is holomorphic on `{Re(s) > 0}`.* Let `A(x) = Σ_{n≤x} (−1)^(n−1) ∈ {0,1}`.
By Abel summation, for `N ≥ 1`,

```
Σ_{n≤N} (−1)^(n−1) n^(−s)  =  A(N) N^(−s) + s ∫₁^N A(x) x^(−s−1) dx.
```

For `s` in the compact set `{Re(s) ≥ δ, |s| ≤ 1/δ}` (any `δ > 0`): the boundary term
satisfies `|A(N) N^(−s)| ≤ N^(−δ) → 0` uniformly, and the integral tail is bounded by
`|s| ∫_N^∞ x^(−1−δ) dx ≤ N^(−δ)/δ² → 0` uniformly. Hence the partial sums converge
uniformly on each such compact set, with limit `η(s) = s ∫₁^∞ A(x) x^(−s−1) dx`. Every
compact subset of `{Re(s) > 0}` lies in such a set, and a locally uniform limit of
holomorphic functions is holomorphic (Weierstrass), so `η` is holomorphic on
`{Re(s) > 0}`. ∎(2b)

*(2c) The identity `η(s) = (1 − 2^(1−s)) ζ(s)` on `{Re(s) > 0}`.* For `Re(s) > 1` both
`Σ n^(−s)` and `Σ (2n)^(−s)` converge absolutely, and splitting the absolutely
convergent series for `η` into even and odd terms gives

```
η(s) = Σ_{n} n^(−s) − 2 Σ_{n} (2n)^(−s) = ζ(s) − 2·2^(−s) ζ(s) = (1 − 2^(1−s)) ζ(s),
```

the rearrangement justified by absolute convergence. The right-hand side, with `ζ` the
analytic continuation (docs/00 §1), is holomorphic on `{Re(s) > 0}`: the only pole of
`ζ` there is simple at `s = 1` with residue `1`, and `1 − 2^(1−s)` has a (simple) zero at
`s = 1`, so the product extends holomorphically across `s = 1`. Both sides are
holomorphic on the connected open set `{Re(s) > 0}` and agree on `{Re(s) > 1}`, which has
limit points; by the identity theorem they agree on all of `{Re(s) > 0}`. ∎(2c)

*(2d) Conclusion.* Fix real `s ∈ (0,1)`. Then `1 − s > 0`, so `2^(1−s) > 1`, i.e.
`1 − 2^(1−s) < 0`; and this factor is nonzero on `(0,1)` (its real zeros require
`2^(1−s) = 1`, i.e. `s = 1`). By (2a) and (2c),

```
ζ(s) = η(s) / (1 − 2^(1−s)) = (positive)/(negative) < 0.   ∎(2)
```

**(3)** *Value at `s=1`:* `ξ(1) = ½ · 1 · π^(−1/2) Γ(1/2) · lim_{s→1} (s−1)ζ(s)
= ½ · π^(−1/2) · √π · 1 = ½`, using the simple pole of `ζ` at `1` with residue `1`
(docs/00 §1) and `Γ(1/2) = √π` (docs/02 §1). By the functional equation `ξ(0) = ξ(1) = ½`
(docs/00 §1).

*Non-vanishing on the real axis:* the zeros of `ξ` are exactly the non-trivial zeros of
`ζ`, and all of these lie in the open strip `0 < Re(s) < 1` (docs/00 §2, [Titchmarsh §2]).
A real zero of `ξ` would therefore be a real `s ∈ (0,1)` with `ζ(s) = 0`, contradicting
(2). For real `σ ∉ (0,1)` there is nothing to check beyond `σ ∈ {0,1}`, where `ξ = ½ ≠ 0`.
Hence `ξ` never vanishes on `ℝ`, and every zero of `ξ` is non-real. ∎

## Used by

- [L3-li-converse-pringsheim.md](L3-li-converse-pringsheim.md)
- `attempts/li-positivity/`

## Checks (doc 06 audit)

- **§3 domain discipline:** the Dirichlet series for `ζ` and `η` are used only for
  `Re(s) > 1` resp. `Re(s) > 0` (where proved convergent); values on `(0,1)` come only
  through the continuation identity (2c), proved via the identity theorem.
- **§2 interchanges:** the only rearrangement (even/odd split) is inside an absolutely
  convergent series; uniform convergence for (2b) is established before passing to the
  limit (Weierstrass).
- **§4 pole handling:** the `s = 1` pole/zero cancellation in (2c) is explicit.
- **§1 circularity:** no statement about complex zeros is assumed; conclusions are about
  real `s` only. RH and its equivalents are not used.
- **§7 branches:** no logarithms or fractional powers of complex quantities are used
  (`2^(1−s) = e^((1−s)log 2)` with real `log 2`).
