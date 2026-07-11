# pick-kernel-positivity — developing argument

> Status tags per workspace/README.md: PROVED / CONDITIONAL(on …) / CONJECTURED /
> NUMERICAL / FALSE / **CLAIMED** (= asserted in notes.md, in-repo verification pending).
> Nothing in this file is a solution of RH. The wall is §5.

## §0. Setup and normalization

`ξ(s) = ½s(s−1)π^(−s/2)Γ(s/2)ζ(s)`, entire, `ξ(s)=ξ(1−s)` [docs/02].
`F(z) := ξ(½ − iz)`; zeros of `F` are `z_ρ = i(ρ − ½)`… **pinned convention:**
`ρ = β+iγ` a nontrivial zero ⟺ `F(z)=0` at `z = γ + i(β − ½)`
(check: `½ − iz = ½ − iγ + (β−½) = β + i(−γ)`… ξ zeros closed under conjugation, fine).
So RH ⟺ all zeros of `F` real. Since `0<β<1` unconditionally, **all** zeros of `F` lie in
`|Im z| < ½` [docs/02 §3].

```
M(z) := −F'(z)/F(z) = i·(ξ'/ξ)(½ − iz).
Q(x) := (ξ'/ξ)(½ + x),  x > ½  real   ⇒   M(ix) = i·Q(x).
```

`Q` is well defined on `(0,∞)` since `ξ` has no real zeros (lemma L2). `Q(x) > 0` for
`x > 0` — from the Hadamard product, `Q(x) = Σ_ρ` (paired) of positive terms; TAG:
CLAIMED, being verified in `scratch/pick-kernel/` (claim 6 also gives the prime form).

## §1. The criterion (statement)

**Criterion (Pick-kernel form of RH).** Fix any `X > ½`. TAG: CLAIMED (audit in §2 found
no gap; independent hostile read still wanted, docs/07 Stage 4).

```
RH  ⟺  for every N, every x_1,…,x_N ∈ (X,∞), every c ∈ ℝ^N:
        Σ_{j,k} c_j c_k · (Q(x_j)+Q(x_k))/(x_j+x_k)  ≥ 0.
```

This is Lagarias's positivity criterion — RH ⟺ `Re(ξ'/ξ(s)) > 0` for `Re s > ½`
([Lagarias1999], **cite together with its 2005 published Correction**, Acta Arith. 116,
293–294; the main equivalence stands; positivity on `Re s ≥ 1` is unconditional,
Hinkkanen) — transported through Loewner/Nevanlinna–Pick theory. It is an *equivalent
formulation* in the sense of docs/03 — a circularity hazard if ever assumed, an attack
surface if proved. Adjacent operator-theoretic programs: [Suzuki2026], [CCM2025] (both
reduce RH to a limiting statement about finite self-adjoint objects; both explicitly
open — compare before investing in T3).

## §2. Audit of the equivalence (this session's adversarial read)

**(⟹)** If RH, all zeros of `F` real, `F` real entire of order 1 with Hadamard product
over real zeros ⟹ `M(z) = Σ_γ (paired) 1/(γ−z)` is Herglotz on `ℂ₊`. Herglotz ⟹ Pick
kernel `(M(z)−conj(M(w)))/(z−conj(w))` PSD [standard: Pick 1916 / Donoghue]. At `z=ix`,
`w=iy`: `(iQ(x)+iQ(y))/(ix+iy) = (Q(x)+Q(y))/(x+y)`. ✓ (Interchange/convergence of the
paired zero sum: standard for order-1 real-zero entire functions; needs a written lemma —
**open exposition item E1**.)

**(⟸)** Suppose all finite Pick matrices at points `{ix : x > X}` are PSD. Pick–Nevanlinna
solvability (countable dense subset `{ix_n}`, values `iQ(x_n)`; PSD of all finite Pick
matrices ⟹ ∃ Herglotz `H` on `ℂ₊` interpolating; normal-family limit of finite-point
solutions) gives `H` Herglotz with `H(ix_n) = M(ix_n)`. The set `{ix_n}` accumulates at
interior points of `{Im z > ½}`, where `M` is **holomorphic** (all poles of `M` have
`|Im| < ½` by §0 — this is the load-bearing geometric fact; it uses only the unconditional
strip bound `0<β<1`). Identity theorem on the connected open set `{Im z > ½}`: `H ≡ M`
there. Now `H` is holomorphic on all of `ℂ₊` and agrees with the meromorphic `M` on an
open set; if `M` had a pole `z₀ ∈ ℂ₊` (⟺ an off-line zero of ξ with `β > ½` after the
`z`-map, plus its mirror), then on a punctured disc around `z₀`, `M = H` by meromorphic
continuation of the identity, forcing `|M| → ∞ = |H(z₀)| < ∞`, contradiction. Hence `M`
pole-free on `ℂ₊` ⟹ no zero of `F` in `ℂ₊`; `F(conj z) = conj(F(z))` (F real on ℝ: ξ real
on the critical line, docs/02) kills `ℂ₋` too ⟹ RH. ✓

*Subtleties checked:* (a) need `Q(x)` finite at the interpolation nodes — yes, `ξ(½+x)≠0`
on ℝ (L2); (b) need values purely imaginary with positive imaginary part for Herglotz
consistency — `Q > 0` gives `M(ix) = iQ(x) ∈ iℝ₊` ✓ (1×1 PSD is exactly `Q≥0`);
(c) Pick–Nevanlinna with infinitely many nodes: take solutions `H_N` for the first `N`
nodes, Montel (Herglotz family is normal after harmless normalization) ⟹ subsequence →
`H`; **open exposition item E2**: write this compactness argument in full.

**No gap found**, but E1/E2 must be written before the criterion is tagged PROVED.

## §3. Unconditional small minors (the "obstruction is ≥ 3-point" phenomenon)

Via the Hadamard product, group zeros into critical pairs (`β=½`) and off-line quartets
`{ρ, 1−ρ, conj ρ, 1−conj ρ}`. Centered variable `α = ρ−½ = a+ib`, `c = α² = u+iv`,
`u = a²−b² < 0` (since `|a|<½ < 14 < |b|`, unconditional), `A = x²−u`, `B = v`:

```
quartet:  Q_α(x) = 4xA/(A²+B²) > 0
pair:     Q_ib(x) = 2x/(x²+b²) > 0
Q_α − xQ_α' = 8x³(A²−B²)/(A²+B²)²                       (>0 since A>|B|)
Q_α + xQ_α' = 8x(−u(A²−B²)+2AB²)/(A²+B²)²               (>0 since u<0, A>|B|)
```

Summing: `−Q ≤ xQ' ≤ Q` on `(½,∞)`, i.e. `xQ(x)` ↑ and `Q(x)/x` ↓, equivalent to every
2×2 Pick minor PSD (exact determinant factorization). TAG: **PROVED** — now lemma
**[L4]** (symbolic verification 2026-07-11, `scratch/pick-kernel/`; key factorization
`A ∓ B = x² + (a∓b)² − 2a²`).

**Consequence, sharpened by verification:** the 1×1/2×2 layer is not merely
unconditional — it is **RH-empty**: Davenport–Heilbronn's `Q_f` satisfies the identical
two-sided bound (11,026 sampled pairs, 0 violations). So (i) RH cannot fail in any way
visible to two-point comparisons of `ξ'/ξ`, AND (ii) nothing in §3 distinguishes ζ from
an RH-violating function — the Euler product has not yet entered. Any positivity proof
must inject it at the ≥ 3-point level or in the summed prime form (§5).

## §4. 3×3 detection of an off-line quartet

Single-quartet kernel `K_α(x,y) = (Q_α(x)+Q_α(y))/(x+y)`; claimed closed form

```
det[K_α(x_j,x_k)]₃ = [64v² Π_{j<k}(x_j−x_k)² / Π_j D_j²] · [−Re(c̄·Π_j(c−x_j²))],
```

`D_j = |x_j²−c|²`; `= 0` iff on-line (`v=0`, kernel rank ≤ 2). TAG: **PROVED**
(full symbolic expansion to 0, + 8 exact rational points, 2026-07-11). Sign: the correct
phase argument is `c̄·Π(c−x_j²) = (|u|+iv)·Π(A_j−iv)` with **opposing** phases, giving
`det < 0` for all `|v/u| < 1` — the notes' `0.072` window was true but conservative by
a factor ~14 (actual ζ/DH-geometry bound: `|v/u| < 1/14`; failure only past `|v/u|=1`).
**Known limitation, now QUANTIFIED (scratch claim 5):** for the real DH quartet
(`ρ_f = 0.8085…+85.6993…i`, `|v/u| ≈ 0.0072`) the single-quartet kernel is indefinite at
*every* 3-point set (best `λ_min(K_q) ≈ −1.3e−9`), but the on-line background quadratic
form on the same direction stayed ≥ `~3.2e6 ×` the quartet negativity across all probes
(N ≤ 20, x ≤ 205, incl. resonance cluster `x ≈ √|c| ≈ 85.7`); no negative eigenvalue of
the full DH kernel was found at dps 100. The masking is *structural* (suppression
`(v/A)² ≈ 1.3e−5` on top of ~1% relative size), not a precision artifact. Detecting an
off-line zero through finite Pick matrices requires either a smarter direction than any
probed, or points/coefficients outside the probed families — this stiffness must be
solved by any finite-dimensional exclusion strategy, and equally afflicts sibling
criteria (Li: first DH negativity at `n ~ 3.5e5`).

## §5. The wall, in prime coordinates

For `x > ½` (absolutely convergent region — domain discipline, docs/06 §3):

```
Q(x) = Q_∞(x) − Σ_{n≥2} Λ(n) n^{−½−x},
Q_∞(x) = 1/(x+½) + 1/(x−½) − ½log π + ½ψ(x/2 + ¼)        [ψ = digamma]
```

(TAG: VERIFIED numerically to ~1e−61 by three independent routes at x ∈ {1.5, 2.5, 5,
10}; derivation is the standard ξ'/ξ decomposition at real s = ½+x — elementary to write
up. Boundary anchor: `Q(½⁺) = 1 + γ/2 − ½log 4π ≈ 0.0231`. Caveat from scratch: direct
prime-sum truncation certifies only ~4–5 digits at x = 1.5 — tail `~N^{−(x−½)}` is slow
near the boundary; any *proof* using the prime form near x = ½⁺ must handle this
analytically, not numerically.) Plugging into the quadratic form with
`B(u) = Σ_j c_j e^{−x_j u}` turns the criterion into a **prime-shift correlation
inequality**:

```
𝒜[B]  ≥  2 Σ_{n≥2} Λ(n) n^{−1/2} ∫_0^∞ B(u) B(u+log n) du        (★)
```

`𝒜` = explicit archimedean form from `Q_∞`. This is Weil positivity [docs/03 §9,
docs/05 §3] for the exponential-sum cone. **The wall is (★).** No mechanism known that
does not secretly assume RH. The candidate mechanism worth trying: a dilation /
sum-of-squares representation of `𝒜 − 𝒫` where `𝒫 = Σ_p Σ_k (log p) p^{−k/2}(S_{k log p}
+ S*_{k log p})` on `L²(0,∞)` — i.e. exhibit `𝒜 − 𝒫 = T*T` on the cone.

## §5b. Exact shape of the wall (night session 2026-07-11): the moment reformulation

**Characterization (proved; same NP machinery as [L6], record as L6-corollary).** For
`f : (a,∞) → ℝ`, the kernel `(f(x)+f(y))/(x+y)` is PSD on `(a,∞)` **iff** `f` extends
to the imaginary-axis trace of a Herglotz function whose Nevanlinna measure is
symmetric, i.e. iff

```
f(x) = βx + c/x + ∫₀^∞ 2x/(x²+t²) dμ(t)          (x > a)          (N)
```

for some `β, c ≥ 0` and a positive measure `μ` with `∫dμ/(1+t²) < ∞`. [⟸: each
`2x/(x²+t²) = 1/(x+it)+1/(x−it)`-pair contributes a rank-≤2 PSD kernel — same
computation as L6 ⟹-direction; `βx` gives the PSD kernel `β`; `c/x` gives
`c/(xy)·(x+y)/(x+y)`… check: `f=c/x` ⟹ `K = c(1/x+1/y)/(x+y) = c/(xy)` — rank-one PSD ✓.
⟹: L6's Step 1–2 verbatim give a Herglotz extension; its Nevanlinna representation
restricted to the imaginary axis must have vanishing real part, forcing the symmetric
form (N).]

**Consequence.** (★) ⟺ the explicitly-computable function
`Q(x) = Q_∞(x) − Σ Λ(n)n^{−½−x}` admits representation (N). Under RH this holds with
`μ = Σ_γ δ_γ` (the zero measure), `β = c = 0` — so **the criterion asks us to produce
the Hilbert–Pólya measure `μ` directly from the prime/archimedean data**, and its
positivity IS the theorem. Stieltjes inversion identifies `μ` with the boundary measure
`(1/π) lim Im M(t+iε) dt`, i.e. with the phase increment of `ξ` along (the right edge
of) the critical line: the criterion is the classical "phase monotonicity" form of RH
in Loewner coordinates. **Verdict for T3:** a dilation `𝒜−𝒫 = T*T` is *equivalent* to
constructing `μ ≥ 0`; there is no cheaper algebraic identity hiding here — any
candidate `T` already encodes the zero measure. This sharpens where novelty must
enter: either (i) a construction of `μ` from primes with positivity visible (the
Hilbert–Pólya program, docs/05 §1–2, with its known walls), or (ii) positivity of
finitely many moments at a time (the ≥3-point minors) with an arithmetic input — for
which the L4 result says the first two layers are free and the DH-masking result says
naive finite tests cannot see the obstruction. Recorded as the attempt's honest state:
(★) is Weil positivity in yet another exact coordinate system; the coordinates clarify
but do not weaken it.

## §6. Litmus audit (docs/06, run at frame level BEFORE investment)

- **LITMUS-1 (Davenport–Heilbronn).** The *criterion* is per-function and DH violates its
  conclusion, so DH's Pick kernel must fail PSD — being probed numerically
  (scratch/pick-kernel claim 5; the failure may be exponentially small, which is itself
  informative for the masking question T2). Any future *proof* of (★) must break for DH at
  a specific line: DH's Dirichlet coefficients are **not** of the form `Λ(n) ≥ 0` with
  Euler product — the positive cone structure of the prime side is exactly what DH lacks.
  A proof of (★) that never uses `Λ(n) ≥ 0` / multiplicativity is wrong by LITMUS-1.
- **LITMUS-3 (σ>1 sanity).** DH has zeros with `Re s > 1`; the criterion correctly "sees"
  them (poles of `Q_f` on `(½,∞)` ⟹ kernel undefined/blows up there). ζ has none —
  because of the Euler product. Consistent.
- **LITMUS-4 (Λ ≥ 0, no slack).** The criterion is an exact equivalence; proving PSD gives
  RH with zero margin, no zero-free strip of positive width. Consistent with Rodgers–Tao.
- **Circularity tripwire.** §3's unconditional minors do NOT assume RH (checked: the
  hypotheses admit off-line zeros). The criterion itself is a docs/03-style equivalent:
  never *assume* it.

## §7. Current sub-targets

- **T1 (exposition, promotable):** write E1, E2 (§2) fully ⟹ criterion → PROVED; write §3
  fully ⟹ lemma L4.
- **T2 (masking quantification):** for one off-line quartet at height `γ` with offset
  `δ = β−½`, estimate the most-negative eigenvalue of the full 3×3 (quartet + all on-line
  zeros) over choices of `x_j`. Expected: detectability needs `x_j` scale ~ `γ`, negative
  eigenvalue scale ~ `δ/γ²` relative — quantify precisely. This tells us how "stiff" the
  criterion is and whether a finite-dimensional exclusion argument is even conceivable.
- **T3 (the real attack):** attempt an operator dilation for `𝒜 − 𝒫` (★). First step:
  compute `𝒜` explicitly as an integral operator kernel on the cone and identify what
  positive structure `Q_∞` has that survives subtracting the prime shifts for ζ but NOT
  for DH-type coefficient sequences.
