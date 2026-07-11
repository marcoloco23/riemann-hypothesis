# L4 — Unconditional two-sided bound `−Q ≤ xQ' ≤ Q` for `Q = ξ'/ξ(½+x)`

**Tag:** PROVED (symbolic verification 2026-07-11, `scratch/pick-kernel/` claims 1–2;
prose proof below; hostile second read still wanted per docs/07 Stage 4).

**⚠️ Scope note (important):** this lemma is *unconditional and RH-empty*. Its
hypotheses admit off-line zeros, and the Davenport–Heilbronn analogue `Q_f` satisfies
the same bounds (numerically: 11,026 sampled pairs, 0 violations). It proves that the
Pick-kernel obstruction to RH is intrinsically ≥ 3-point; it cannot by itself
distinguish ζ from RH-violating functions.

## Statement

Let `Q(x) := ξ'(½+x)/ξ(½+x)` for real `x > ½` (well-defined by L2: `ξ ≠ 0` on ℝ). Then
for all `x > ½`:

```
Q(x) > 0   and   −Q(x) ≤ x·Q'(x) ≤ Q(x),
```

equivalently `x·Q(x)` is nondecreasing and `Q(x)/x` is nonincreasing on `(½, ∞)`;
equivalently every 1×1 and 2×2 principal minor of the Pick kernel
`K(x,y) = (Q(x)+Q(y))/(x+y)` is PSD (2×2 equivalence: exact factorization
`det·xy(x+y)² = (Q(y)x − Q(x)y)(Q(x)x − Q(y)y)`, whose factors cannot both be negative
since their sum is `(Q(x)+Q(y))(x−y) > 0` for `x > y`).

More generally the same holds for any entire order-1 function `Ξ*` real and nonvanishing
on `(½,∞)+½`, even under `s ↦ 1−s`, whose zeros `ρ = β+iγ` all satisfy `|β−½| < ½` and
`|γ| > 14` (only these two facts about the zero set are used).

## Proof

`ξ` is entire of order 1, genus 1, with Hadamard product `ξ(s) = ξ(0)Π_ρ(1−s/ρ)` under
symmetric pairing [docs/02 §2]. Grouping zeros as symmetric quartets
`{ρ, 1−ρ, ρ̄, 1−ρ̄}` (off-line) and pairs `{ρ, ρ̄} = {½±ib}` (on-line), the centered
variable `α = ρ−½ = a+ib` gives, for `s = ½+x`:

- **Quartet contribution.** With `c = α² = u+iv`, `u = a²−b² < 0` (since `|a|<½<14<|b|`),
  `v = 2ab`, `A = x²−u`, `B = v`:
  `Q_α(x) = d/dx log[(1−x²/α²)(1−x²/ᾱ²)] = 4xA/(A²+B²)`, and exactly

  ```
  Q_α − xQ_α' = 8x³(A²−B²)/(A²+B²)²
  Q_α + xQ_α' = 8x(−u(A²−B²) + 2AB²)/(A²+B²)²
  ```

  (verified by exact symbolic simplification). Positivity: the key factorization is

  ```
  A − B = x² + (a−b)² − 2a²,     A + B = x² + (a+b)² − 2a²,
  ```

  both `> 0` since `(|b|−|a|)² ≥ (14−½)²` dwarfs `2a² < ½` — hence `A > |B| > 0`,
  giving `A²−B² > 0`; with `u < 0` both displayed numerators are positive. So
  `−Q_α < xQ_α' < Q_α` and `Q_α > 0`.

- **Pair contribution** (`a = 0`): `Q_ib(x) = 2x/(x²+b²) > 0` with
  `Q − xQ' = 4x³/(x²+b²)²> 0` and `Q + xQ' = 4xb²/(x²+b²)² > 0`.

- **Summation.** `Σ_ρ 1/|ρ|² < ∞` (Riemann–von Mangoldt, docs/02 §3) gives locally
  uniform absolute convergence of the grouped log-derivative series and of its termwise
  derivative on compact subsets of `(½,∞)` (each term is `O(x/|ρ|²)`, `O(1/|ρ|²)`
  uniformly); termwise differentiation is legitimate, and the inequalities—each holding
  termwise—sum. ∎

**Boundary value** (numerical anchor): `Q(½⁺) = ξ'(1)/ξ(1) = 1 + γ/2 − ½log 4π ≈
0.0231049931`, matched to 2.6e−61 in scratch.

## Used by

`attempts/pick-kernel-positivity/` (PROOF.md §3).

## Checks (docs/06 audit)

- Circularity (Part 2 §1): none — hypotheses allow off-line zeros; RH nowhere assumed.
- Interchange (Part 2 §2): summation step justified via `Σ1/|ρ|² < ∞`; the only
  analytic input.
- Domain (Part 2 §3): everything on the real segment `x > ½`; no series used outside
  `σ > 1`… (no Dirichlet series used at all).
- LITMUS-1: the lemma *itself* holds for Davenport–Heilbronn (verified numerically) —
  consistent, because the lemma claims nothing RH-flavored. Any use of it in an RH
  argument must add Euler-product input elsewhere.
