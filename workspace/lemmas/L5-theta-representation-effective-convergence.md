# L5 — Theta representation of Ξ and effective uniform convergence of the truncations

**Tag:** PROVED (full derivation below; independent hostile re-read wanted per docs/07
Stage 4; the final numeric anchors are cross-checks, not part of the proof).

## Statement

Let `Ξ(z) := ξ(½+iz)` and, for `n ≥ 1`,

```
φ_n(u) := (2π²n⁴ e^{9u/2} − 3πn² e^{5u/2}) e^{−πn² e^{2u}}     (u ≥ 0),
Ξ_N(z) := 4 ∫₀^∞ Σ_{n≤N} φ_n(u) cos(zu) du.
```

Then:

**(a) Exact representation.** For every `z ∈ ℂ`:
`Ξ(z) = 4∫₀^∞ Σ_{n≥1} φ_n(u) cos(zu) du`, the integral converging absolutely.

**(b) Positivity.** `φ_n(u) > 0` for all `u ≥ 0, n ≥ 1` (since `2πn²e^{2u} ≥ 2π > 3`).

**(c) Effective tail bound.** For every `N ≥ 1` and every `z` with `|Im z| ≤ ½`:

```
|Ξ(z) − Ξ_N(z)| ≤ ε_N := 8.01·π·(N+1)² e^{−π(N+1)²}.
```

(More generally, for `|Im z| ≤ Y` with any fixed `Y ≥ ½` the same proof gives
`|Ξ−Ξ_N| ≤ 8.01π(N+1)²e^{−π(N+1)²}` provided `π(N+1)² ≥ 2(5/4 + Y/2)` — satisfied for
all `N ≥ 1` when `Y ≤ 5.03`.) In particular `Ξ_N → Ξ` uniformly on the closed strip
`|Im z| ≤ ½`, hence locally uniformly on `ℂ`.

## Proof

**Step 1 (Riemann's formula).** For `σ > 1`, `π^{−s/2}Γ(s/2)ζ(s) = ∫₀^∞ y^{s/2−1}ψ(y)dy`
with `ψ(y) = Σ_{n≥1}e^{−πn²y}` (termwise Mellin, Tonelli — all terms positive). Split at
`y = 1` and apply the theta functional equation `ψ(1/y) = −½ + ½√y + √y·ψ(y)`
(Jacobi; [Titchmarsh §2.6]) to the `(0,1)` part via `y ↦ 1/y`:

```
∫₀^1 y^{s/2−1}ψ(y)dy = −1/s + 1/(s−1) + ∫₁^∞ y^{(1−s)/2−1}ψ(y)dy,
```

(using `σ > 1` for convergence of the two elementary integrals). Since
`−1/s + 1/(s−1) = 1/(s(s−1))`:

```
ξ(s) = ½ + (s(s−1)/2) ∫₁^∞ ψ(y)(y^{s/2−1} + y^{(1−s)/2−1}) dy.        (R)
```

Both sides of (R) are entire in `s` (the integral converges absolutely for every
`s ∈ ℂ` because `ψ(y) = O(e^{−πy})`, and defines an entire function by
Morera/dominated convergence), so (R) holds for all `s` by the identity theorem.

**Step 2 (logarithmic substitution).** Put `s = ½ + iz`, `y = e^{2u}`. Then
`y^{s/2−1}dy = 2e^{su}du`, `y^{(1−s)/2−1}dy = 2e^{(1−s)u}du`, and
`e^{su} + e^{(1−s)u} = 2e^{u/2}cos(zu)`. With `w(u) := e^{u/2}ψ(e^{2u})` and
`s(s−1) = −(z²+¼)`:

```
Ξ(z) = ½ − 2(z²+¼) ∫₀^∞ w(u) cos(zu) du.                              (*)
```

**Step 3 (two integrations by parts).** `w` and all its derivatives are
`O(e^{−πe^{2u}+O(u)})` as `u → ∞` (termwise differentiation of the series defining `w`
is justified by locally uniform convergence of each differentiated series — each term
is smooth and the series of `k`-th derivatives is dominated on `[0,U]` by
`Σ_n poly(n)e^{−πn²}` type bounds). For `z ∈ ℝ` first:

```
z²∫₀^∞ w cos(zu)du = −w'(0) − ∫₀^∞ w''(u)cos(zu)du
```

(boundary terms at `∞` vanish; at `0`, `sin(0) = 0` kills one and the other gives
`−w'(0)`). Substituting into (*):

```
Ξ(z) = ½ + 2w'(0) + ∫₀^∞ (2w''(u) − ½w(u)) cos(zu) du.
```

**Step 4 (the constant vanishes).** `w'(0) = ½ψ(1) + 2ψ'(1)`. Differentiating the theta
functional equation at `y = 1`: `−ψ'(1) = ¼ + ½ψ(1) + ψ'(1)`, i.e.
`ψ'(1) = −⅛ − ¼ψ(1)`. Hence `w'(0) = ½ψ(1) − ¼ − ½ψ(1) = −¼` and `½ + 2w'(0) = 0`.

**Step 5 (the integrand is `4Σφ_n`).** Termwise, with `q = πn²e^{2u}` and
`h_n(u) = e^{u/2}e^{−q}`:

```
h_n'' = e^{u/2}(4q² − 6q + ¼)e^{−q}   ⟹   2h_n'' − ½h_n = 4q(2q−3)e^{u/2}e^{−q}
      = 4(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}} = 4φ_n(u).
```

Summation over `n` (locally uniform) gives `2w'' − ½w = 4Σφ_n`, proving (a) for real
`z`; both sides are entire in `z` (dominated convergence for the integral — see Step 6
bound), so (a) holds on `ℂ`. (b) is immediate from `2πn²e^{2u} ≥ 2π > 3`.

**Step 6 (tail bound).** For `|Im z| ≤ Y`, `|cos(zu)| ≤ e^{Yu}`. Substituting
`ω = πn²e^{2u}` (so `e^{u} = (ω/πn²)^{1/2}`, `du = dω/2ω`):

```
∫₀^∞ φ_n(u)e^{Yu}du = ½(πn²)^{−1/4−Y/2} ∫_{πn²}^∞ ω^{1/4+Y/2}(2ω−3)e^{−ω}dω
                    ≤ (πn²)^{−1/4−Y/2} Γ(9/4 + Y/2, πn²).
```

For `a ≥ 2(c−1)` one has `Γ(c,a) = e^{−a}∫₀^∞(a+t)^{c−1}e^{−t}dt ≤
a^{c−1}e^{−a}·(1−(c−1)/a)^{−1} ≤ 2a^{c−1}e^{−a}` (using `(1+t/a)^{c−1} ≤ e^{(c−1)t/a}`).
With `c = 9/4 + Y/2` and `a = πn²`: valid for all `n ≥ 1` iff `πn² ≥ 5/2 + Y` — true
for `Y ≤ ½` and `n ≥ 1`. Hence `∫φ_n e^{Yu}du ≤ 2πn²e^{−πn²}` and

```
|Ξ(z) − Ξ_N(z)| ≤ 4Σ_{n>N} ∫φ_n e^{u/2}du ≤ 8π Σ_{n>N} n²e^{−πn²}.
```

Consecutive-term ratio: `a_{n+1}/a_n = ((n+1)/n)² e^{−π(2n+1)} ≤ 4e^{−3π} < 3.3×10⁻⁴`
for `n ≥ 1`, so `Σ_{n>N} n²e^{−πn²} ≤ (N+1)²e^{−π(N+1)²}/(1 − 3.3×10⁻⁴)`, giving (c). ∎

## Numeric anchors (cross-checks only, not part of the proof)

- Normalization: `Ξ(2) = 4∫₀^∞Φ(u)cos(2u)du` verified to 42 digits
  (`scratch/theta-strip/out_s01.txt`).
- `ε_1 ≈ 8.01π·4·e^{−4π} ≈ 3.5×10⁻⁴`; `ε_3 ≈ 1.6×10⁻²⁰`; `ε_5 ≈ 3.6×10⁻⁴⁸` —
  consistent with observed `|Ξ−Ξ_N|` in scratch.

## Used by

- `attempts/theta-strip/` (§2 revised: moving-window route; effective Hurwitz).
- Any future effective zero-transfer argument (`Ξ_N ≠ 0` on `K` + `min_K|Ξ_N| > ε_N` ⟹
  `Ξ ≠ 0` on `K` — NOTE the direction: transferring zero-freeness from `Ξ_N` to `Ξ`
  needs the lower bound on `Ξ_N`, which is checkable per-N; the reverse transfer needs
  `min_K|Ξ| > ε_N`, which presumes knowledge of `Ξ`'s zeros — keep the asymmetry
  straight to avoid circularity).

## Checks (docs/06 audit)

- Part 2 §2 (interchanges): Tonelli for positive terms (Steps 1, 5, 6); termwise
  differentiation justified by locally uniform convergence (Step 3); boundary terms
  computed (Steps 3–4). No conditionally convergent rearrangements.
- Part 2 §3 (domain): Dirichlet series used only at `σ > 1` (Step 1); everything else
  extended by the identity theorem with entire-ness established first.
- Circularity: none — no zero information about ζ is used anywhere.
- LITMUS-1: the derivation uses the Jacobi theta functional equation (Poisson summation
  over ℤ, unit coefficients) — exactly the structure Davenport–Heilbronn's kernel lacks
  in positive form; the POSITIVITY (b) is specific to ζ's kernel.
