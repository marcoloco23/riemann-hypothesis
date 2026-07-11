# theta-strip — developing argument

> TAGS: PROVED / CONDITIONAL(on …) / CONJECTURED / NUMERICAL / FALSE / CLAIMED
> (= from notes.md, in-repo verification pending). Not a solution; the wall is §4.

## §0. Objects

`Ξ(z) := ξ(½+iz)`, real entire, even. Classical kernel representation
(Titchmarsh §10.1 — normalization being re-pinned numerically in
`scratch/theta-strip/`):

```
Ξ(z) = 2∫₀^∞ Φ(u) cos(zu) du,   Φ(u) = Σ_{n≥1} φ_n(u),
φ_n(u) = (2π²n⁴e^{9u/2} − 3πn²e^{5u/2}) e^{−πn²e^{2u}}.
```

`Φ > 0`, even (via `θ(1/u) = √u θ(u)`), super-exponentially decaying. Truncation:
`Ξ_N(z) := 2∫₀^∞ (Σ_{n≤N} φ_n(u)) cos(zu) du` — an explicit finite combination of
incomplete gamma functions [Haglund2011, eqs. (12)–(14)]. `Ξ_N → Ξ` locally uniformly:
**asserted** in [Haglund2011] from Riemann's uniformly convergent expansion, not proved
standalone there ⟹ must be proved in-repo (candidate lemma L5, easy dominated
convergence) before the §2 route is tagged.

**Zero geography of Ξ (unconditional):** nontrivial zero `ρ = β+iγ` ⟺ `Ξ(z)=0` at
`z = γ − i(β−½)`; since `0<β<1`, ALL zeros of `Ξ` lie in `|Im z| < ½`. RH ⟺ all real.

## §1. Recorded dead end: truncations are not real-rooted (FALSE target)

`Ξ₁` has complex zeros ≈ `20.62534601 + 2.69715184i`, `26.05616693 + 7.12535971i`;
`Ξ₂` first nonreal ≈ `43.13890807 + 3.28097100i` (NUMERICAL, Haglund + independent
reproduction pending in scratch). Mechanism understood: a finite one-sided theta sum has
`K_N'(0) = d_N ≠ 0` (the full kernel's odd derivatives vanish at 0 only by modularity,
i.e. by the *infinite* sum), and two integrations by parts give
`Ξ_N(x) = −d_N/x² + O(x⁻⁴)`, so `Ξ_N` stops oscillating ⟹ finitely many real zeros ⟹
complex zeros necessarily appear. `d_N ≍ N⁶e^{−π(N+1)²}` tiny ⟹ front at
`e^{−πx/4} ~ e^{−π(N+1)²}` ⟹ `R_N ≈ 4(N+1)²` (matches Haglund's table: 39.53 vs 36 at
N=2, 489.39 vs 484 at N=10). **Do not retry real-rootedness of Ξ_N.**

## §2. The target — ORIGINAL FORM REFUTED (2026-07-11); weakened moving-window form

**Finite theta-strip theorem — FALSE.** The per-N statement "`Ξ_N(z) ≠ 0` for
`0 < |Im z| < ½`" fails at `N = 3`:

```
Ξ_3(67.88018965514762… + 0.47734384177082…i) = 0        (margin to ½: 0.0227)
```

TAG: NUMERICAL-REFUTATION, high confidence — argument-principle count exactly 1 in the
box, root polished to `|Ξ_3| ~ 1e−51`, independently confirmed by direct quadrature
(`~1e−66` vs local scale `1e−21`); full record `scratch/theta-strip/STRIP-ZERO-N3.md`.
The zero sits just past the real-zero front `R_3 ≈ 65.03`. Min-Im of nonreal zeros is
NOT monotone in N and NOT bounded below by ½ (N=1: 2.697, N=2: 3.281, N=3: 0.477,
N=4: 0.73 up to Re ≤ 200). The notes' claim "Im ≳ 2.7 for N ≤ 10" is FALSE — Haglund's
zero lists evidently did not include front-attached near-real zeros.

**Corrected target (moving-window strip theorem, CONJECTURED).** For every compact
`K ⊂ {0 < |Im z| < ½}` there is `N_K` with `Ξ_N ≠ 0` on `K` for all `N ≥ N_K`.
Consistent with all data if strip zeros occur only near the moving front
(`Re z ≍ 4(N+1)² → ∞`). Plausible sharp form: `Ξ_N(z) ≠ 0` for
`0 < |Im z| < ½, |Re z| ≤ c·N²` (some explicit `c`; data: front-attached strip zero at
`Re ≈ 67.9 ≈ 1.06·4(N+1)²` for N=3).

**Theorem (conditional route to RH), REVISED.** Moving-window theorem + locally uniform
convergence ⟹ RH. TAG: PROVED-modulo-citations. Argument: suppose `Ξ(z₀) = 0` with
`0 < Im z₀ < ½`. Take a closed disc `K ⊂` strip around `z₀`; by Hurwitz (local form:
zeros of locally-uniform limits are limits of zeros), `Ξ_N` has a zero in `K` for all
large `N` — contradicting the moving-window theorem for `N ≥ N_K`. Mirror strip by
reality/evenness; §0 geography finishes. ✓ (This is exactly what the FALSE per-N form
was providing; the weakening costs nothing in the implication.)

Relation to [Haglund2011]: his Conjecture 1 / Remark-1 form (nonreal zeros right of the
largest real zero) is NOT contradicted by the N=3 strip zero (`67.88 > R_3`), and his
Proposition 1 route to RH is intact. The moving-window form is morally the
strip-shadow of his conjecture: both say complex zeros are confined to the escaping
front region.

## §2b. Structural results (2026-07-11 night session)

**(1) The moving-window statement is EQUIVALENT to RH** (docs/03-style; hence also a
circularity tripwire). ⟸ was §2's Hurwitz argument. ⟹: assume RH; let
`K ⊂ {0<|Im z|<½}` be compact; under RH, `Ξ ≠ 0` on `K` (all zeros real), so
`m_K := min_K |Ξ| > 0`; by [L5(c)], for `N ≥ N_K` with `ε_N < m_K`,
`|Ξ_N| ≥ m_K − ε_N > 0` on `K`. ∎ Consequence: the *qualitative* moving-window form
carries the full difficulty of RH; only the *quantitative* front form (explicit window
`|Re z| ≤ c N²`) is a stronger, potentially-falsifiable per-N statement — the campaign
data bear on that one.

**(2) Endpoint-defect principle (unifies this session's three refutations).** Any
finite positive truncation of the theta kernel — one-sided (`K_N`), atom-reflected
(`φ_n(|u|)`), or self-dual-glued — has a nonvanishing odd-derivative defect at `u = 0`
(full modularity, an infinite-sum identity, is what kills all odd derivatives). Two
integrations by parts convert the defect into an algebraic `x^{−2}` tail of FIXED SIGN
in the cosine transform. Consequences: finitely many real zeros; complex zeros
necessarily appear at the balance point of `(oscillatory scale) ~ (defect scale)` — the
front; and every UNWINDOWED per-N positivity/zero-freeness target is generically FALSE
(per-N real-rootedness ✗, per-N strip theorem ✗ at N=3, divisor packets ✗ ∀k). Rule:
**every finite-truncation target must be windowed by the defect scale.**

**(3) Rouché reality lemma (proved; candidate L6').** Let `γ` be a simple real zero of
`Ξ`, `D` a conjugation-symmetric closed disc centred at `γ` containing no other zero of
`Ξ`, with `min_{∂D}|Ξ| > ε_N`. Then `Ξ_N` has exactly one zero in `D`, and it is
**real**. *Proof:* Rouché with [L5(c)] gives exactly one zero (counting multiplicity,
= that of `Ξ` in `D`, = 1). `Ξ_N(z̄) = conj(Ξ_N(z))` (real integrand), so nonreal zeros
come in conjugate pairs inside the symmetric `D`; a single zero must therefore be real. ∎

**(3b) Defect sign lemma (PROVED).** `φ_n'(0) = (a_n/2)(−8a_n² + 30a_n − 15)e^{−a_n}`,
`a_n = πn²`. The quadratic `−8a²+30a−15` has roots `(30±√420)/16 ≈ 0.5940, 3.1559`;
since `π ≈ 3.14159 < 3.1559 < 4π`, we get `φ_1'(0) > 0` (barely — the near-coincidence
of `π` with the root `3.1559` is why the defect is tiny, `≈ 0.01975`) and
`φ_n'(0) < 0` for all `n ≥ 2`. Hence the endpoint defect
`d_N := K_N'(0) = −Σ_{n>N} φ_n'(0) > 0` for **every** `N ≥ 1`, and
`Ξ_N(x) → 0⁻` like `−4d_N/x²` as `x → +∞`: all truncations are eventually negative.

**(3c) Far-tail zero-free zone (PROVED-modulo-writeup, P2).** Two integrations by
parts, twice (boundary terms at ∞ vanish for `|Im z| ≤ ½` by double-exponential decay
of `K_N` and derivatives; odd-derivative boundary terms at 0 survive):

```
Ξ_N(z) = −4d_N/z² + 4K_N'''(0)/z⁴ + (4/z⁴)∫₀^∞ K_N''''(u) cos(zu) du,
```

so with `T_N² := (|K_N'''(0)| + ∫₀^∞|K_N''''(u)|e^{u/2}du)/d_N` (explicit, computable):
`Ξ_N(z) ≠ 0` for `|Im z| ≤ ½, |z| ≥ T_N`. Caveat: `d_N` is doubly-exponentially small,
so `T_N ~ e^{π(N+1)²/2}` — far beyond the observed front `4(N+1)²`. P2 closes the
strip at infinity (per-N zero-freeness is now a FINITE-window question), but the
gap `[cN², T_N]` still needs the saddle-regime analysis (§4). 

**(3d) Night-campaign data + consequences (2026-07-11, `scratch/selfdual-truncations/`).**
- **Identity:** the batch-1 "self-dual truncation" is IDENTICALLY the one-sided
  truncation: `Ξ_N^{sd} ≡ Ξ_N` (algebraic proof via two applications of
  `Γ(c+1,a) = cΓ(c,a) + a^c e^{−a}`; 61-digit numeric confirmation). There is ONE
  truncation family and it was already self-dual. Corner: `J_N = 4d_N =
  −2πΣ_{n≤N}n²(8π²n⁴−30πn²+15)e^{−πn²} > 0` exactly (= `2π·(n>N tail)`).
- **P2 constants:** `T_N = 90.6, 6.26e4, 1.53e9, 1.06e15, …` for `N = 1..8`
  (`M4_N → 161.898` stable). So **for N=1 the strip question is a finite certified
  computation**: `Ξ_1 ≠ 0` in `0<|Im z|<½` reduces to (i) PROVED tail `|z| ≥ 90.6`
  (P2), (ii) certified argument-principle count 0 on `[0, 90.6]×[δ, ½]`, (iii)
  certified single-zero symmetric boxes around each real zero (reality by the parity
  trick of (3)). NUMERICAL status: all three hold in floating point; interval-certified
  versions are future work (needs arb-style ball arithmetic — flag as T1-cert).
  For `N = 2` (`T_2 ≈ 6.3e4`) still conceivable; `N ≥ 3` needs a sharper tail bound
  than P2 (the true front is `~4(N+1)²`; P2's `T_N` is exponentially wasteful).
- **L₁ front structure (NUMERICAL, N = 1..6):** `L₁[Ξ_N] ≥ 0 on the ENTIRE bulk
  `[0, R_N]`; first failure always just past the front (`first-neg − R_N ∈
  [1.8, 4.8]`); then bounded negative windows tracking the complex-zero abscissas
  (N=3's first window `[67.43, 68.34]` brackets the strip zero); then a PERMANENT
  negative tail from `x ≈ 27.6, 55.7, 101.2, 157.7, 226.8, 308.4` — analytically
  forced: `Ξ_N ~ −J_N/x²` gives `L₁[Ξ_N] ~ −2J_N²/x⁶ < 0`. **Consequence (proved, not
  just data): EVERY finite theta truncation eventually violates the first Laguerre
  inequality.** So Csordas OP 4.7 (`L₁[Ξ] ≥ 0`) cannot be attacked by unwindowed
  truncation-limit arguments — windowing by the front is mandatory there too
  (cross-referenced in laguerre-phase-space §8).

**(3e) Front-law campaign verdict (2026-07-11 night, `scratch/theta-strip/front-law/`,
N = 3..8 complete; N=8 caveat: its final polish-based reality check did not complete
(`reality_max_im = inf` in zeros_N8.json) — near-real counts are covered by the
symmetric-box certification instead, but re-run the polish check before citing N=8's
real-zero list at full weight):**

| N | R_N | #real | strip zeros (0<Im<½) | min nonreal Im | Re/(4(N+1)²) |
|---|-----|-------|----------------------|----------------|--------------|
| 3 | 65.032 | 15 | 67.8802 + 0.4773i | 0.477 | 1.0606 |
| 4 | 103.368 | 31 | none | 1.357 | — |
| 5 | 149.003 | 53 | none | 1.785 | — |
| 6 | 197.958 | 79 | none | 0.689 | — |
| 7 | 258.531 | 113 | **260.2881 + 0.3471i** | 0.347 | 1.0168 |
| 8 | 327.380 | 155 | none | 0.566 | — |

Interpretation: (i) **front law supported** — every strip zero found satisfies
`Re > R_N` with `Re/(4(N+1)²) ∈ [1.01, 1.07]`; the bulk is clean in all cases
(coverage: all zeros enumerated in `[0, 6(N+1)²+100] × (0, ~12]`, counts
argument-principle-certified in floating point). (ii) The lowest front-zero height
wanders non-monotonically (0.48, 1.36, 1.78, 0.69, 0.35 for N = 3..7) — the front
phase is quasi-random, so strip zeros should recur for infinitely many N (whenever the
phase dips below ½) while remaining front-confined. Per-N strip-freeness is dead for
good; the **quantitative front law** `strip zeros ⊂ [R_N, (1+δ)·4(N+1)²] × (0,½)` is
the empirically exact statement (CONJECTURED; NUMERICAL N ≤ 7).

**(4) Effective bulk confinement (proposition schema).** Fix `N` and a bulk window
`B = [0, X] × [0.001, 0.499]` with `X` below the front. Suppose (i) all zeros of `Ξ`
with `0 ≤ Re z ≤ X` are real and simple — a *theorem* for `X ≤ ~3·10¹²`
[PlattTrudgian2021]; (ii) discs `D_γ` as in (3) around each such zero, and
`|Ξ| > ε_N` on `B \ ∪D_γ` (certifiable per-N by interval evaluation — |Ξ| is
`≍ e^{−πx/4}` in the strip, so this holds whenever `X ≲ 4(N+1)² − C log N`, with
per-case certification of the minimum). Then `Ξ_N` has NO zeros in `B` off the real
axis. This *derives* the front law with constant 4: strip zeros of `Ξ_N` can live only
where `|Ξ| ≤ ε_N`, i.e. `Re z ≳ 4(N+1)²` (matching the observed N=3 zero at
`67.88 ≈ 1.06·4·16`). Missing for a clean closed-form theorem: an explicit
unconditional lower bound for `|Ξ(x+iy)|` off zero-discs in the strip (currently:
certifiable numerically per window, not a formula). **The wall in its sharpest form:**
beyond verification height, step (i) IS RH — the front law for all N is exactly as
hard as RH at the corresponding heights, as (1) predicts. New mathematics must
therefore target per-N zero-freeness WITHOUT routing through Ξ's zeros — the §4
windowed separation. The strip `|Im| < ½` has a ~5× safety margin —
but see LITMUS-4 discussion in §6: the margin must *shrink to zero* in the limit, and it
does (complex zeros march right and, along subsequences approaching genuine ζ zeros,
their imaginary parts must approach `±(β−½)`… no: if RH holds all limit zeros are real).

## §3. Exact finite structure (the tools)

With `s = ½+iz`, `a_n = πn²` (constants being re-validated):

1. **Incomplete-gamma / phase form.** `Ξ_N(z) = C_N + (s(s−1)/2)·I_N(s)` with
   `C_N = Σ_{n≤N}(4πn² − 1)e^{−πn²} > 0` and
   `I_N(s) = ∫₁^∞ θ_N(u)(u^{s/2−1} + u^{(1−s)/2−1})du`, `θ_N(u) = Σ_{n≤N}e^{−πn²u}`.
   TAG: CLAIMED (finite-N analogue of Riemann's classical formula; exact constants under
   numerical validation). A zero in the strip must satisfy the phase equation
   `I_N(s) = −2C_N/(s(s−1))`.

2. **cosh/sinh split with universal multiplier.** For `z = t + ir`, `0<r<½`, `t>0`,
   substituting `u = e^{2v}`: `I_N = A_N + iB_N` where

   ```
   A_N(r,t) = 4∫₀^∞ w_N(v) cosh(rv) cos(tv) dv,
   B_N(r,t) = 4∫₀^∞ w_N(v) sinh(rv) sin(tv) dv,
   w_N(v) = e^{v/2} θ_N(e^{2v}) > 0,
   ```

   and the two kernels satisfy `g/f = tanh(rv)`: strictly increasing in `v`, independent
   of `N`, range `[0,1)`. An off-line zero forces the **phase-matching equation**
   `B_N/A_N = 2rt/(t² + ¼ − r²)` with `A_N, B_N > 0` (★). TAG: CLAIMED.

3. **Atom ordering (sign-regularity of order 2).** For `m > n`, `φ_m/φ_n` strictly ↓ on
   `u ≥ 0` (proof via `h(q) = 5/2 + 4q/(2q−3) − 2q`, `h' < 0` — one-line calculus; TAG:
   CLAIMED, easy). NOTE the `−3` denominator: `2q−3 > 0` needs `q = πn²e^{2u} > 3/2`,
   true for all `n≥1, u≥0` since `π > 3/2` — check kept explicit. This survives even
   though full total positivity of `Φ` is FALSE at PF-order 5 ([Michalowski2026] —
   unrefereed preprint, certified interval arithmetic; re-verify before load-bearing
   use). The primes' locations `log n` and the coefficient-1 completions are essential,
   not decorative.

4. **Zero motion under adding an atom.** `F_{N,τ} = Ξ_N + τΦ_{N+1}`; at a simple zero,
   `dIm z/dτ = ∂_x W_N/|F'|²` with `W_N = Im[Ξ_N · conj(Φ_{N+1})]`, and `W_N` symmetrizes
   over `u>v` against the fixed-sign determinant `D_N(u,v) = K_N(v)φ_{N+1}(u) −
   K_N(u)φ_{N+1}(v) < 0`. **Recorded obstruction:** the other factor `H_{x,y}(u,v)`
   oscillates in `x` — the naive sign argument is INVALID, and interpolation in `τ` can
   leak zeros through the strip at interior `τ`; only integer endpoints `τ=1` (exact atom
   completion, cancelling the dominant odd-derivative defect at `u=0`) are special. Any
   proof must be discrete-in-N, not continuous-in-τ. TAG: analysis CLAIMED; the
   *obstruction* is the reliable part.

## §4. The wall (revised after the §2 refutation)

The unrestricted common-zero exclusion (★) is **FALSE** — the N=3 strip zero is exactly
a common zero of the two transforms at `(r,t) ≈ (0.477, 67.88)`. The wall is now the
**windowed** version: prove that for `0 < r < ½` and `t ≤ c·N²` (away from the front),
`∫w_N cosh(rv)cos(tv)dv` and `∫w_N sinh(rv)sin(tv)dv` have no common zero — i.e. the
Pólya-type separation must incorporate the front scale `4(N+1)²` (from the endpoint
defect `d_N ≍ N⁶e^{−π(N+1)²}`, §1) as an explicit hypothesis boundary. Tools unchanged:
(a) `tanh(rv)` multiplier identity, (b) atom ordering §3.3, (c) integer-endpoint
completion §3.4, plus now (d) the endpoint-defect asymptotics separating "bulk" from
"front" behavior. The refutation is informative: any candidate proof that does not
break down near `t ≍ 4N²` is wrong.

## §5. Failure modes pre-recorded (do not retry)

- Real-rootedness of `Ξ_N`: FALSE (§1).
- Total positivity / PF-∞ of `Φ`: FALSE at order 5 (cite pending).
- Continuous interpolation `τ ∈ (0,1)` strip-preservation: leaks (§3.4).
- Symmetrized probabilistic truncations (Brownian/gamma route): fails Hermite–Biehler
  already at first order — see `scratch/notes-triage.md` (Lee–Yang route, parked).

## §6. Litmus audit (docs/06)

- **LITMUS-1/2 (DH, Epstein).** Where does the method use what DH lacks? The kernel
  `w_N > 0` as a sum of *positive, identically-shaped, ℤ-translated* atoms comes from
  `θ(u) = Σe^{−πn²u}` — Poisson/modularity over the full integer lattice with
  **unit coefficients**. DH's completed function has a theta-like kernel with complex
  (character-twisted, non-positive) coefficients; `w_N^{DH}` is not positive and the
  cosh/sinh split with a *positive* common weight fails at §3.2. If a candidate proof of
  §4 never uses positivity/unit-coefficients of `w_N`, it would apply to DH and is wrong.
  Action item V1: numerically build the DH analogue of `Ξ_1` and confirm it has zeros
  INSIDE the strip (it must — DH's off-line zeros at height ~85 sit at `Im z ≈ ±0.31`).
- **LITMUS-3.** `Ξ_N ≠ 0` in `|Im z|<½` says nothing about `σ>1` zeros directly; the
  strip statement corresponds to `|β−½|<½`, exactly the nontrivial-zero region. No
  proves-too-much leak visible at frame level.
- **LITMUS-4 (no slack).** The theorem would give RH with zero margin — zeros of `Ξ`
  could still be dense on the real axis; consistent with `Λ = 0` barely-true. ✓
- **Circularity.** The conjecture is per-N about explicit incomplete-gamma sums; no RH
  input anywhere in §3 structure. ✓ Main risk is instead that (★)-exclusion is simply
  false for some `(N,r,t)` — hence the counterexample hunt V2.

## §7. Sub-targets

- **V1:** DH strip litmus (build `Ξ_1^{DH}`, find strip zeros). 
- **V2:** counterexample hunt: dense `(r,t)` scan of the phase equation for `N ≤ 6`,
  especially near the real-zero front `t ≈ R_N` where `A_N` changes sign.
- **T1:** prove the `N=1` case: `Ξ_1(z) ≠ 0` in `0<|Im z|<½` — single incomplete-gamma
  atom, fully explicit; a complete proof here would be a genuine new lemma and the
  template for induction.
- **T2:** make §3.1–3.3 PROVED (they're finite calculus + Mellin manipulations).
