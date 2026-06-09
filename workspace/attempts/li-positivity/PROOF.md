# li-positivity — developing argument

> **Status banner (keep honest, doc 01 E12):** RH is NOT proved here. Everything below
> is either PROVED scaffolding, CITED established results, or clearly-labelled
> NUMERICAL/CONJECTURED/TODO material. The target inequality (§2) is open and is
> equivalent to RH.

## 1. Target statement

With `ξ(s) = ½ s(s−1) π^(−s/2) Γ(s/2) ζ(s)` and the Li coefficients `λ_n` defined as
the Taylor coefficients at `0` of `G(z) = (d/dz) log ξ(1/(1−z)) = h'(z)/h(z)`,
`h(z) = ξ(1/(1−z))` (definition as in [lemmas/L3](../../lemmas/L3-li-converse-pringsheim.md);
equivalent to Li's original definition and to the paired zero-sum
`λ_n = Σ_ρ [1 − (1−1/ρ)^n]`, [Li1997, Thm 1], [BombieriLagarias1999, Thm 1]):

> **Target (equivalent to RH, [Li1997]).** `λ_n ≥ 0` for every `n ≥ 1`.

Direction status:

- **(⟸ of the criterion) PROVED in-repo:** if `λ_n ≥ 0` for all sufficiently large `n`,
  then RH — [lemmas/L3](../../lemmas/L3-li-converse-pringsheim.md) (self-contained,
  Pringsheim route; strengthens the needed direction: only eventual non-negativity is
  required).
- **(⟹, "RH ⟹ λ_n ≥ 0") CITED, not needed for the attack:** [Li1997]. (On RH every
  zero-quadruple contributes `2(1 − cos nθ_ρ) ≥ 0`; the content is convergence/pairing.)
- **The open problem is the unconditional proof of the Target.** That is this attempt.

## 2. Why this is the docs/05 §3 wall, precisely

[BombieriLagarias1999] exhibit `λ_n = W(g_n)` — the Weil explicit-formula functional
evaluated at a specific test-function sequence `g_n`. Two structural facts matter:

1. **The arithmetic side.** The explicit formula renders `λ_n` as
   `(archimedean/Γ-and-pole part, explicit and smooth, growing like (n/2)·log n)`
   **minus** `(a weighted sum over prime powers with non-negative weights Λ(m) ≥ 0)`.
   ⚠️ Exact constants/normalization to be transcribed verbatim from
   [BombieriLagarias1999, Thm 2] before any quantitative use — **TODO, do not quote
   from memory** (doc 01 B2).
2. **The sign problem.** `Λ(m) ≥ 0` — the Euler-product positivity that distinguishes
   `ζ` from the litmus counterexamples — enters with a **minus sign**. Naive
   term-positivity therefore proves nothing; `λ_n ≥ 0` asserts that the prime sum never
   overshoots the smooth archimedean growth, for any `n`. That assertion is *equivalent*
   to RH, so no generic inequality (Cauchy–Schwarz, convexity, term domination…) can
   suffice: any proof must exploit fine cancellation in the distribution of primes.
   This is the recurring positivity crux of docs/05 ("Positivity is the recurring
   crux"), in its most explicit form.

**Effective support obstruction (why current technology stops):** the `n`-th Li test
function samples the multiplicative axis up to scale `≍ log n` (the kernel
`1 − (1−1/ρ)^n` resolves zeros to height `≍ n`, dually the test function reaches
prime powers `m ≲ e^{c·log n}`-ish; sharp version TODO with §1's transcription).
Positivity of the Weil functional is *proved* only for test functions whose support
excludes all primes ([ConnesConsani2021]: the archimedean window, support inside
`(−log 2, log 2)` in the additive normalization). All `n ≥ some small n₀` exit that
window. There is no proved positivity statement covering any infinite tail of the Li
sequence. Filling *any* infinite tail would finish (L3 needs only "eventually ≥ 0").

## 3. What is established in-repo so far

| Piece | File | Tag |
|---|---|---|
| Möbius dictionary `w(s)=1−1/s`: half-plane ↔ disk, `ρ↦1−ρ` ↔ `w↦1/w`, compact sublevels | [L1](../../lemmas/L1-cayley-map-critical-line.md) | PROVED |
| `ζ(σ)>1` for real `σ>1`; `ζ<0` on `(0,1)`; `ξ` non-vanishing on `ℝ`, `ξ(0)=ξ(1)=½` | [L2](../../lemmas/L2-zeta-xi-real-axis.md) | PROVED |
| RH false ⟹ `λ_n<0` infinitely often, with `limsup|λ_n|^{1/n}=1/r₀>1` | [L3](../../lemmas/L3-li-converse-pringsheim.md) | PROVED |
| `λ_n > 0` for `1 ≤ n ≤ 40` (ζ), convention check `λ₁ = 1+γ/2−½log 4π` to ~60 digits | `scratch/li-coefficients/` | NUMERICAL |
| Davenport–Heilbronn grounding (functional equation verified numerically; off-line zero region) | `scratch/li-coefficients/` | NUMERICAL |

## 4. Failure modes already understood (do not retry blindly)

- **Termwise positivity of the zero-sum.** Off-line zero quadruples contribute
  `4 − 2(r^n + r^{−n})cos nθ`, which is negative for many `n`; positivity of the *sum*
  is global, not termwise. (This is just L3 read in reverse.)
- **Positivity from the functional equation alone.** Impossible — Davenport–Heilbronn
  shares the FE shape and has `λ_n(f) < 0` for some `n` (it has off-line zeros, apply
  L3's argument scheme to `ξ_f`). Any candidate proof must visibly break for `f`. See §5.
- **Convexity/moment bounds on the archimedean term alone.** The archimedean part grows
  `~(n/2)log n` for *every* function with the right Γ-factor, including `f`. Cannot
  decide positivity by itself.

## 5. Litmus analysis (doc 06, mandatory — run BEFORE believing any idea)

- **LITMUS-1 (Davenport–Heilbronn `f`).** `f` has the same FE shape, no Euler product,
  zeros off the line ([DavenportHeilbronn1936], [BombieriHejhal1995], [Spira1968]).
  Consequently some `λ_n(f) < 0`. *Gate applied to this attempt:* any claimed proof of
  `λ_n(ζ) ≥ 0` must use an input **false for `f`**. Available such inputs: the Euler
  product / `Λ(m) ≥ 0` on the arithmetic side (the coefficients of `−f'/f` are not
  non-negative — `f` has zeros in `σ>1`, so `−f'/f` even has poles there); positivity
  `f(σ) > 0` on `(1,∞)` may *fail* for `f`. A draft that never invokes these is dead on
  arrival. **Checkpoint passes today:** no positivity claim is made yet; L3 makes no
  such claim (see its scope notes).
- **LITMUS-2 (Epstein).** Same gate, same conclusion: class-number `>1` Epstein zetas
  have off-line zeros; their Li coefficients go negative; a valid method must
  distinguish via multiplicativity.
- **LITMUS-3 (proves too much in `σ>1`?).** The only `σ>1` non-vanishing used anywhere
  is [L2] (1) for `ζ` via series positivity — a property `f` genuinely lacks (signed
  coefficients), so no overreach.
- **LITMUS-4 (`Λ_dBN ≥ 0`, no slack).** Consistent: Li positivity is an *equality-edge*
  statement — on RH, `λ_n` grows only logarithmically faster than `n` while single
  off-line zeros would force exponential excursions; nothing here manufactures a
  positive-width zero-free strip.
- **LITMUS-5 (Selberg-class sanity).** The attack surface (arithmetic side of the
  explicit formula) is exactly where the Euler-product axiom enters. Compliant by
  construction; must be re-checked for every concrete draft.

## 6. Concrete next sub-target (scoped, believed completable — partial progress only)

> **Sub-target Q1 (quantitative finite-range positivity).** From the cited rigorous
> verification that all zeros with `|Im ρ| ≤ T₀` lie on the line ([Platt-Trudgian],
> `T₀ ≈ 3·10^12`), derive an explicit `N₀ = N₀(T₀)` with a full proof that
> `λ_n > 0` for all `n ≤ N₀`.

Sketch (to be executed carefully; all bounds to be made explicit):

1. Pair zeros into quadruples `{ρ, ρ̄, 1−ρ, 1−ρ̄}`; by [L1] (3) the quadruple
   contribution to `λ_n` is `Q_ρ(n) = 4 − 2(r^n + r^{−n})cos nθ` where
   `w(ρ) = re^{iθ}` (on-line zeros: `r = 1`, `Q_ρ(n) = 4(1 − cos nθ) ≥ 0`).
2. Verified region `|γ| ≤ T₀`: zeros on the line ⟹ contribution `Σ 4(1−cos nθ_ρ) ≥ 0`;
   moreover a *lower bound growing in `n`* should follow from `N(T)` asymptotics
   (docs/02 §3) — the angles `θ_ρ ≈ 1/γ` (hmm: `θ_ρ = arg(1−1/ρ)`, for `ρ = ½+iγ`,
   `θ_ρ ~ 1/γ`) equidistribute enough that `Σ_{|γ|≤T₀}(1−cos nθ_ρ) ≫ n` for
   `n ≤ c·T₀` — **needs a real proof, this is the main work item**.
3. Unverified tail `|γ| > T₀` (zeros may be anywhere in the strip): with
   `β ∈ (0,1)`, `r² = 1 − (2β−1)/|ρ|²` gives `r^n + r^{−n} ≤ 2cosh(n/(2γ²)·c)`, so
   `Q_ρ(n) ≥ 4 − 2(2 + (cn/γ²)²)·1 = −2(cn/γ²)²` for `n ≪ γ²`; summing against the
   zero-counting density `dN(γ) ≍ log γ · dγ` gives
   `tail ≥ −C n² (log T₀)/T₀³`.
4. Conclude `λ_n ≥ (growth from 2) − C n² log T₀ / T₀³ > 0` for `n ≤ N₀(T₀)`.
   Expected shape: `N₀ ≍ T₀` at least (possibly `≍ T₀²` with sharper step-2 input).

Honest framing: Q1 is **not** progress toward removing the wall (it is conditional on
finite verification and inherently finite-range); its value is (a) a fully rigorous,
checkable, formalizable quantitative lemma where most "λ_n positivity" statements in
circulation are numerical, and (b) forcing the explicit-formula machinery of §2 to be
set up to acceptance standard, which any real attack on the wall needs anyway.

## 7. Candidate directions at the actual wall (unranked; none currently has a plan)

- Squeeze the [ConnesConsani2021] archimedean-window positivity past `log 2`
  (include `p = 2` only): even the single-prime extension is open and would be a
  structural breakthrough far beyond Q1.
- Reformulate the §2 sign problem as a moment problem / Hamburger-type positivity for
  the measure behind `(λ_n)` and look for arithmetic input making the Hankel forms PSD.
  (Same wall in different clothing — Hankel positivity of `(λ_n)` is *not* implied by
  `λ_n ≥ 0` and is not equivalent to RH; check equivalences carefully before investing.)
- Mine the function-field proof (docs/05 §4): in Weil's proof positivity comes from the
  Hodge index theorem; the Li-coefficient analogue over function fields is provable —
  write it out (notes/) to see exactly which object has no `Spec ℤ` counterpart.

## 8. Session log

- **2026-06-09:** Attempt opened. L1–L3 proved and audited; litmus §5 run on the frame
  (passes; no positivity claim made). Numerics (60 dps): `λ_n(ζ) > 0` for `n ≤ 40`,
  convention pinned against closed-form `λ₁` to `1.8e−61`; D–H functional equation
  verified to `~1e−60` (root-number identity exact to `1.1e−61`), Spira's off-line zero
  reproduced, `λ_n(f)` negativity onset estimated `n ~ 3.5e5`. Q1 scoped (§6). No
  progress at the wall itself (§7) — recorded plainly.
