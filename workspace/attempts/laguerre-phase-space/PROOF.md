# laguerre-phase-space — developing argument

> TAGS: PROVED / CONDITIONAL(on …) / CONJECTURED / NUMERICAL / FALSE / CLAIMED
> (= from notes.md, verification pending in `scratch/laguerre-phase-space/`).
> Not a solution; the wall is §4.

## §0. Objects

`Ξ(z) = ξ(½+iz)`, real entire, even, order 1. Heat flow (de Bruijn–Newman, docs/03 §12):
`H_t(x) = ∫_ℝ e^{tu²}φ(u)e^{ixu}du`, `φ` the positive even theta kernel normalized so
`H_0 = Ξ` (constant being pinned in scratch). Rodgers–Tao: `Λ ≥ 0`; RH ⟺ `Λ = 0`
[docs/04 §F].

## §1. The Laguerre chain of equivalences

For real entire `f`:
`L_n[f](x) = (1/(2n)!) Σ_{j=0}^{2n} (−1)^{j+n} C(2n,j) f^{(j)}(x) f^{(2n−j)}(x)`
(`L_0 = f²`, `L_1 = f'² − ff''`), and the generating identity

```
|f(x+iy)|² = Σ_{n≥0} L_n[f](x) y^{2n}.                                   (G)
```

TAG (G): **VERIFIED** (2026-07-11, scratch: symbolic through `y⁶` + numeric for Ξ with
discrepancy = first omitted term to 4 s.f.) — exact identity, two-line proof from
`|f|² = f(z)·f(z̄)`; write-up = candidate lemma L7.

Chain (each link needs its exact citation/hypotheses — literature agent):

```
RH ⟺ Ξ ∈ LP ⟺ L_n[Ξ](x) ≥ 0 ∀n,x ⟺ 𝒞(z) := |Ξ'(z)|² − Re(Ξ(z)conj(Ξ''(z))) ≥ 0 ∀z∈ℂ
```

- `RH ⟺ Ξ ∈ LP`: standard (Ξ has order 1 < 2, genus fits; real zeros ⟺ LP for such f
  given the Hadamard structure). Needs a written lemma with the exact genus hypotheses —
  **exposition item E1**.
- `LP ⟺ L_n ≥ 0 ∀n`: [CsordasVarga1990, Thm 2.9] (restated [CsordasEscassut2005, Thm
  2.2]); necessity direction [Patrick1973]. **Hypothesis for ⟸:** `f ∈ 𝔖(A)` — Hadamard
  form `Ce^{−az²+bz}z^m Π(1−z/z_k)e^{z/z_k}`, `a ≥ 0`, `b ∈ ℝ`, `Σ|z_k|^{−2} < ∞`, and
  **zeros confined to a horizontal strip** `|Im z_k| ≤ A`. **Key check (this session):**
  `Ξ ∈ 𝔖(½)` holds UNCONDITIONALLY — order 1 (so `a = 0`), even/real, `Σ1/|z_k|² < ∞`
  (from `N(T) ~ (T/2π)log T`), and all zeros in `|Im z| < ½` by `0 < β < 1` [docs/02 §3].
  So the criterion applies to Ξ with no RH input. TAG: usable; write the `Ξ ∈ 𝔖(½)`
  verification as part of E1.
- `LP ⟺ 𝒞 ≥ 0 on ℂ`: complex Laguerre inequality, [CsordasVarga1990, Thm 2.10/2.12]
  (restated [CsordasEscassut2005, Thm 2.4]), same `𝔖(A)` hypothesis — same unconditional
  applicability to Ξ. Also version I: `f ∈ LP ⟺ (1/y)·Im{−f'(z)conj(f(z))} ≥ 0, y ≠ 0`.
  Note `𝒞(x+iy) = ½∂_y²|Ξ(x+iy)|²` (CLAIMED; consistent with (G):
  `½∂_y²|f|² = Σ_{n≥1} n(2n−1)L_n y^{2n−2}`, whose `y=0` value is `L_1` ✓ — but the
  full-plane equivalence needs the literature hypotheses, not just `y=0`).

## §2. Exact hierarchy and the ultrahyperbolic obstruction

With `L_n(t,x)` the double-integral (Fourier-side) form,
`L_n(t,x) = (1/(2n)!)∬(u−v)^{2n} e^{t(u²+v²)}e^{ix(u+v)}φ(u)φ(v)dudv`:

```
∂_t L_n = −½ ∂_x² L_n + (n+1)(2n+1) L_{n+1}       (H)
∂_t G   = −½ ∂_x² G + ½ ∂_y² G,  G_t(x,y) = |H_t(x+iy)|²   (sums (H) against y^{2n})
```

TAG: **VERIFIED at integrand level** (2026-07-11, scratch: kernel identity + coefficient
identity symbolic in `n`; residual vanishes numerically for n ≤ 3). Remaining hypothesis
for a PROVED tag: differentiation under the integral (standard for rapidly decreasing φ,
subcritical t) — exposition item E2.
**Structural finding worth keeping regardless of the attempt's fate:** the `(x,y)`
evolution of `G` is ultrahyperbolic (diffusion in `x`, anti-diffusion in `y` under
forward `t`) — no parabolic maximum principle exists for it, which is a clean a-priori
explanation of why naive PDE approaches to dBN fail. Also shows exactly how
real-rootedness is lost backward: the `−(n+1)(2n+1)L_{n+1}` term (in reversed time) can
drive `L_n` negative — loss of LP is a *cascade down the hierarchy*, not a single event.

## §3. Phase-space representation (the live target)

`ψ_t(u) = e^{tu²}φ(u)`, Wigner-type transform
`W_t(p,x) = ∫_ℝ ψ_t((p+q)/2)ψ_t((p−q)/2)cos(xq)dq` (even in `p`):

```
𝒞_t(x,y) = ½ ∫₀^∞ p² cosh(py) W_t(p,x) dp                                (W)
```

TAG: **VERIFIED** — both notes variants are EXACTLY EQUAL (`¼∫_ℝ p²e^{−py}W dp =
½∫₀^∞ p²cosh(py)W dp`, using evenness of ψ ⟹ `W(−p,x) = W(p,x)`; hand proof via
`p = u+v, q = u−v` + Gaussian closed-form agreement to ~30 digits, 2026-07-11). Candidate
lemma L6. **RH target (at t=0):**

```
∫₀^∞ p² cosh(py) W_0(p,x) dp ≥ 0    ∀ x,y ∈ ℝ.                           (9)
```

Not pointwise `W_0 ≥ 0` (far stronger, almost surely false — Wigner transforms of
non-Gaussians go negative); only hyperbolic-weighted `p`-moments must be ≥ 0.

## §4. The wall

Prove (9) unconditionally. Proposed program: decompose `φ = Σφ_n` (theta atoms) ⟹
`W_0 = Σ_{m,n} W_{m,n}`; prove packet positivity
`∫p²cosh(py)(W_{n,n} + W_{m,m} + 2W_{m,n})dp ≥ 0` for an arithmetic grouping into
packets, with absolute summability. Nothing beyond the program exists yet. Failure modes
to check FIRST (litmus §6 + these): (a) does packet positivity already fail numerically
for small `(m,n)`? — cheap kill test, action V1; (b) diagonal terms `W_{n,n}` are Wigner
transforms of single positive atoms — positive-definite in a weak sense but NOT pointwise
positive; the cross terms `W_{m,n}` carry the arithmetic (`log m − log n` shifts) — if
packet positivity holds trivially without arithmetic input, LITMUS-1 fails and the
grouping is wrong.

## §5. Dead ends recorded exactly (do not retry)

1. **Block-energy / collision-prevention under backward dBN flow.** Exact identity
   (verified algebra: triple-cancellation `Σ_{cyc} 1/((a−b)(a−c)) = 0`):
   `d𝓗_K/dt = −4ℰ_K + 2Σ_{ℓ∉K}Σ_{j<k∈K} 1/((x_ℓ−x_j)(x_ℓ−x_k))`. In the clock
   (equally-spaced) configuration the external term EQUALS `4ℰ_K` — the environment is
   not a perturbation, it is what holds equilibrium; no inequality
   `d𝓗/dt ≤ −cℰ + small` can exist. This is why Rodgers–Tao renormalize against expected
   locations; their machinery propagates nothing backward from `t > 0`.
2. **Backward linear instability kills zero-counting inputs.** Linearizing around the
   clock: mode `e^{ikθ}` has eigenvalue `λ(θ) = −(2π|θ|−θ²)/Δ²`; backward time `τ`
   amplifies `θ=π` by `exp(π²τ/Δ²) ≈ exp((τ/16)log²(T/4π))` — superpolynomial in height
   `T`. Any approach feeding only density/counting estimates into backward dBN evolution
   is dead on arrival.
3. **Naive saddle/two-phase collision exclusion** (double zero ⟺ simultaneous
   destructive interference + stationarity): plausible program but reduces to Polymath15
   -style effective asymptotics; parked — only worth reopening with a new idea for the
   uniform two-saddle expansion.

## §6. Litmus audit (docs/06)

- **LITMUS-1 (DH).** The chain §1 applies to any real entire order-1 function; for DH's
  completed function `𝒞` must go negative somewhere (it has nonreal zeros of its
  `F`-form). A proof of (9) must therefore use the specific positive-atom lattice
  structure of `φ` (unit coefficients, `log n` shifts, modular symmetry `u ↦ −u` with
  `yH(y)=H(1/y)`). DH's kernel has character-twisted non-positive atoms — packet
  positivity must fail for it. **Kill-check V2:** verify numerically that the DH analogue
  of (9) FAILS (find explicit `(x,y)` with negative value) — if we cannot find a failure,
  the frame is suspect per LITMUS-1.
- **LITMUS-4.** (9) is an equivalence-grade target (⟸ RH via the chain); no extra
  zero-free width produced. ✓
- **Circularity.** The chain's ⟸ directions come from LP theory, not from assuming zeros
  real; but E1 and the two pending citations MUST be pinned before any use — flagged.
- **Domain discipline.** All integrals absolutely convergent (`φ` super-exponential);
  interchanges in (H)/(W) need one dominated-convergence lemma — exposition item E2.

## §7. Sub-targets (original batch)

- **V1:** numeric packet positivity scan for small `(m,n)` — cheap kill test for §4.
  **Superseded by §8.6:** diagonal packets are NOT the mechanism; test divisor packets.
- **V2:** DH failure exhibit (litmus, §6). Still live.
- **T1:** settle the exact form of (W) (Gaussian test, in flight) and prove it as a
  lemma (candidate L6) — pure Fourier algebra. Still live, but see §8.1: the canonical
  object is the Dimitrov–Xu kernel, not the raw Wigner form.
- **T2:** prove (H) and (G) rigorously (dominated convergence; candidate L7). Still live.
- **T3:** superseded by §8.

---

## §8. REVISION — second notes batch (2026-07-11): the Dimitrov–Xu correlation frame

The phase-space (Wigner) formulation of §3–4 is superseded: the canonical object it was
approximating is the **Dimitrov–Xu correlation kernel** (citation being pinned —
[DimitrovXu]):

```
ν₂(t) = ∫_ℝ (t−2s)² Φ(t−s)Φ(s) ds  (> 0),      Φ_{2,y}(t) = cosh(yt)·ν₂(t).
```

**Criterion [DimitrovXu2019, Thm 1.1] (pinned 2026-07-11):** RH ⟺ for each
`y ∈ (−½,½)\{0}`, translates of `Φ_{2,y}` dense in `L¹(ℝ)` ⟺ (Wiener Tauberian)
`FT[Φ_{2,y}]` has no real zero. Second part: density for *every* `y ∈ (−½,½)` incl. 0 ⟺
zeros of Ξ real **and simple**. **Correction to the notes' §4–6 wobble:** since
`FT[Φ_{2,y}](0) > 0` unconditionally [DX (3.9)–(3.10)], nonvanishing on each fixed line
⟺ **strict positivity** on that line — i.e. `U(0,y) > 0` for all `|y| < ½` is a theorem,
and the criterion IS positivity of `Re 𝓛(x+iy)` line-by-line in the open strip. The
boundary `|y| = ½` remains excluded for the integrability reason in §8.4. Also:
Wronskian sign relation carries a typo in DX (exponent `n(n−1)/2` is correct; harmless
at n = 2, where `W₂(𝓕f) = −𝓕(ν₂)` stands).

### §8.1 Exact identities (TAG: CLAIMED, verification in scratch/dimitrov-xu-boundary/)

- `ν̂₂(z) = 2𝓛(z)` where `𝓛(z) = Ξ'(z)² − Ξ(z)Ξ''(z)`; hence
  `FT[Φ_{2,y}](x) = 2·Re 𝓛(x+iy)`.
- In `s`-coordinates (`s = ½+iz`): `𝓛(z) = ξ(s)ξ''(s) − ξ'(s)²`. On `Im z = −½`:
  `s = 1+ix` — the boundary line is `Re s = 1`.
- `L₁ = ¼·Ĉ` with `C(p) = ∫q²Φ((p+q)/2)Φ((p−q)/2)dq > 0` — so even the FIRST Laguerre
  inequality `L₁[Ξ] ≥ 0` is the Fourier-positivity of an explicit positive kernel, and
  it is **OPEN unconditionally** — [Csordas2015, Open Problem 4.7] verbatim ("one of the
  simplest Laguerre inequalities for the Riemann ξ-function"), with Remark 4.8: known
  unconditionally only for `|x| < 1.09×10⁹`; failure anywhere would DISPROVE RH; strict
  positivity would additionally give simplicity of the real zeros. Numerical state
  (scratch): `L₁, L₂ > 0` at 33 grid points incl. the Lehmer region
  (`C_Ξ(7005.063, 0.05) = 1.23e−4765 > 0`, two independent methods).
- Infinitesimal Turán / probabilistic form: `L₁(x)/Ξ(x)² = Var_x(U)` under the
  complex-tilted measure `E_x[f(U)] = E[f(U)e^{ixU}]/E[e^{ixU}]` for
  `dμ ∝ Φ(u)du` — positivity of a complex-tilted variance, not automatic.

### §8.1b Dead end (added night 2026-07-11): truncation routes to OP 4.7

Every finite theta truncation satisfies `L₁[Ξ_N](x) ~ −2J_N²/x⁶ < 0` for large `x`
(`J_N = 4d_N > 0` is the endpoint defect — theta-strip §2b(2),(3d)), and numerically
`L₁[Ξ_N] ≥ 0` holds exactly on the bulk `[0, R_N]` with first failure just past the
front (N = 1..6 data in `scratch/selfdual-truncations/`). So `L₁[Ξ] ≥ 0` [Csordas2015,
OP 4.7] can NOT be proved by any unwindowed positive-truncation approximation; a
truncation-based attack must prove the windowed statement `L₁[Ξ_N] ≥ 0 on [0, R_N]`
(true numerically, front-scale-aware) and pass to the limit through a window growing
like `4(N+1)²`. Do not retry unwindowed variants.

### §8.2 Dead end: Pólya convexity of C (do not retry)

`C''(0) = 4∫r²[ΦΦ'' − Φ'²]dr = 4∫r²Φ²(log Φ)''dr < 0` by **strict log-concavity of Φ**
— [CsordasVarga1988, Thm 2.1] (`log Φ(√t)` strictly concave), packaged as
[Csordas2015, Thm 4.5]; NOT in CNV 1986 (that is `log K_Φ`) and NOT in Dimitrov–Xu.
`C` is concave at its max, so the classical "positive, decaying, convex ⟹ nonneg FT"
criterion is structurally unavailable, for `C` and for every `cosh(yp)C(p)` with small
`|y|`. TAG: cited + numeric check in flight (scratch/dimitrov-xu-boundary claim 2).

### §8.3 Dead end: diagonal theta-packet positivity (sharpens §4/§6)

`FT[C_{n,n}] ≥ 0` would say each single-atom transform satisfies its own Laguerre
inequality — but finite truncations develop nonreal zeros (theta-strip §1), so diagonal
positivity is NOT the mechanism. Confirms the litmus expectation: **arithmetic
interaction `m ≠ n` is essential.** Any grouping must exploit cross-index cancellation.

### §8.4 Dead end: the boundary (`Re s = 1`) minimum-principle route — REFUTED numerically

Attempt: `U(x,y) = Re 𝓛(x+iy)` is harmonic; `𝓛 → 0` in the strip as `|x| → ∞`; so
`U ≥ 0` on `|y| < ½` would follow from `U ≥ 0` on the boundary `y = ±½`, i.e. from
`B(t) := Re[ξ(1+it)ξ''(1+it) − ξ'(1+it)²] ≥ 0` — one real inequality on `Re s = 1`
where the Euler product converges. **This fails:** high-precision evaluation (notes;
independent verification in flight, magnitudes ~1e−68 so dps-stability is being checked)
gives `B(110) ≈ +8.34e−68` but `B(110.5) ≈ −2.28e−69`, `B(111) ≈ −5.83e−69` — `B`
changes sign. Moreover the failure has a precise structural reason: at `|y| = ½` the
kernel `cosh(yt)ν₂(t)` **loses `L¹` integrability** (critical exponential threshold), so
the formal analytic boundary value `𝓛(x ± i/2)` is not the `L¹`-Fourier boundary limit
governed by Wiener's theorem; sign changes there do not contradict open-strip
nonvanishing — and cannot be used for a minimum principle either. Both directions die:
no cheap proof, no cheap disproof, from the boundary line.

Consequently the **averaged boundary program is also dead as stated**: the "Boundary
correlation theorem" (∫h·B ≥ 0 for all `h ≥ 0` with `ĥ ≥ 0`) is FALSE — take `h` an
approximate identity at `t ≈ 110.5–111`.

### §8.5 Poisson/strip structure worth keeping

For interior lines the harmonic machinery is legitimate: `Û(ω,y) = [cosh(ωy)/cosh(ωa)]·
Û(ω,a)` for `|y| < a < ½`; the strip Poisson kernel `K_y > 0`; inward smoothing damps
frequency `ω` by `~e^{−(a−|y|)|ω|}`. The boundary ripples at `t ≈ 110.5` may be
high-frequency and killed by any positive smoothing depth — this is the mechanism the
interior-line program (§8.7) must quantify.

### §8.6 Dead end: divisor-packet positivity — REFUTED (kill test, 2026-07-11)

Under `p = u+v, q = u−v`, group atom pairs by product `k = mn`:
`C^(k) = Σ_{mn=k} C_{m,n}`. **Kill test result (scratch/dimitrov-xu-boundary claim 4):
`FT[C^(k)]` goes negative for EVERY tested `k`** — first crossings: k=1: x≈18.79,
k=2: x≈5.22, k=3: x≈4.84, k=4: x≈26.36, k=6: x≈21.03 (dps 45, minima re-verified dps
70). **Structural cause, predicted then confirmed:** the atom-level even extension
`φ_n(|u|)` has a corner (`φ_n'(0⁺) ≠ 0`), giving each atom transform an algebraic
`c_n/x²` tail and `FT[C^(1)] ~ −8c₁²/x⁶ < 0`. The corner slopes cancel only in the FULL
kernel (e.g. `φ₁'(0⁺) = +0.019749383` vs `φ₂'(0⁺) = −0.019749341` — near-cancellation
across CONSECUTIVE indices, not within divisor packets). **Dead as stated.** Two
salvage notes for any future grouping: (a) the near-cancellation pattern is between
adjacent `n`, echoing theta-strip §3.4's integer-endpoint completion phenomenon;
(b) a grouping built on properly symmetrized atoms (the batch-1 self-dual completion
`H_N(y), yH_N(y)=H_N(1/y)` instead of the naive `|u|`-reflection) would remove the
corner artifact and is the only variant worth one more test.

### §8.7 Live target B: interior-line nonvanishing — PREMISE CORRECTED (see §8.9)

Original target: for every `δ > 0`, `Re[ξ(1−δ+it)ξ'' − ξ'²] ≠ 0 ∀t`. **REFUTED as
stated (scratch claim 5):** the negativity window persists on interior lines
(σ = 0.95: normalized min ≈ −1.30; σ = 0.90: ≈ −0.51; confirmed dps 200; gone by
σ = 0.8), bracketing the close zero pair `γ₃₄ ≈ 111.0295, γ₃₅ ≈ 111.8747`. Structural:
`𝓛 = Ξ²Σ_ρ(z−ρ)^{−2}` and `Re(z−γ)^{−2} < 0` whenever `|x−γ| < y` — so **`Re𝓛 < 0`
near close (Lehmer-type) zero pairs is forced EVEN UNDER RH** whenever the line height
`y` exceeds half the local pair gap. "RH ⟹ Re𝓛 ≥ 0 on horizontal lines" is FALSE;
pointwise positivity of `Re𝓛` on interior lines can be neither a consequence of RH nor
a route to it.

### §8.8 Litmus addendum

The `B(t)` sign change is itself a litmus-consistent datum: had the boundary route
worked, it would have proved positivity `Re 𝓛 > 0` up to the strip edge with room to
spare — smelling of LITMUS-4 violation (no-slack). Its failure at finite `t` is what a
barely-true RH looks like.

### §8.10 NEW TARGET (night 2026-07-11): the Windowed Laguerre conjecture

**Conjecture WL.** For every `N ≥ 1`: `L₁[Ξ_N](x) ≥ 0` for all `x ∈ [0, R_N]`
(`R_N` = largest real zero of `Ξ_N`). TAG: CONJECTURED; NUMERICAL support N = 1..6
(scratch/selfdual-truncations: holds on the full bulk, first failure at `R_N + 1.8` to
`R_N + 4.8`).

**Theorem (WL ⟹ Csordas OP 4.7), PROVED.** WL implies `L₁[Ξ](x) ≥ 0` for all real x.
*Proof.* (i) `R_N → ∞`: by Hardy [docs/04 §B] Ξ has infinitely many real zeros; at a
zero `γ` of odd multiplicity (sign changes give these), take a small
conjugation-symmetric disc; by [L5] and Rouché, `Ξ_N` has the same (odd) zero count
there for large `N`; complex zeros pair by conjugation, so an odd count forces ≥ 1
REAL zero of `Ξ_N` near `γ`; hence `R_N ≥ γ − ε` eventually. (ii) Fix `x₀`; for large
`N`, `x₀ ≤ R_N`, so WL gives `L₁[Ξ_N](x₀) ≥ 0`. (iii) `Ξ_N → Ξ` uniformly on a strip
neighborhood of `[x₀−1, x₀+1]` [L5(c)] ⟹ `Ξ_N', Ξ_N'' → Ξ', Ξ''` uniformly near `x₀`
(Cauchy integral estimates) ⟹ `L₁[Ξ_N](x₀) → L₁[Ξ](x₀) ≥ 0`. ∎

**Why WL has the right shape:** it is windowed exactly at the front, as the
endpoint-defect principle demands (§8.1b: unwindowed versions are FALSE). Mechanism
sketch for a proof attempt: `Ξ_N` has order 1, so
`L₁[Ξ_N](x) = Ξ_N(x)²·Σ_k (x−z_k)^{−2}` (Hadamard, genus ≤ 1, the `e^{bz}` term dies
under two log-derivatives). Real zeros contribute positively; a complex pair `a±bi`
contributes negatively at `x` iff `|x−a| < b`. So WL is the statement that IN THE BULK
the real-zero repulsion `Σ_{γ≤R_N} (x−γ)^{−2}` (dense zeros, spacing `~2π/log x`)
dominates the attraction of the front-attached complex zeros (`a ≳ R_N`, so their
negativity reaches only `x > a − b ≈ R_N − 12`). The fight is localized to an `O(10)`
window below `R_N` — a per-N, quantitative, zero-geography inequality. Sub-target WL':
prove WL for `x ≤ R_N − 15` (away from the fight) using (a) Rouché bulk-tracking of
real zeros (theta-strip §2b(3)–(4)) and (b) an upper bound on complex zeros' influence
via P2-type integration by parts. Note: WL for all N ⟹ OP 4.7, which is NOT RH — but
failure of L₁[Ξ] ≥ 0 anywhere would DISPROVE RH, and WL is the first finite-N route to
OP 4.7 with the structurally correct windowing.

**Proposition sketch WL'' (bulk, height-capped — provable with effective constants).**
For `x ≤ min((1−δ)·4(N+1)², H_v)` with `H_v` the rigorously verified zero height:
`L₁[Ξ](x)/Ξ(x)² = Σ_γ(x−γ)^{−2} ≥ 8/g(x)²` (`g(x)` = local real-zero gap, controlled
by verified data below `H_v`), while `|L₁[Ξ_N] − L₁[Ξ]|(x) ≤ C·ε_N·e^{−πx/4}·poly`
([L5] + Cauchy estimates), and `ε_N e^{+πx/4} ≤ e^{−δπ(N+1)²}` in this range — so
`L₁[Ξ_N](x) > 0` there. Hence **the genuinely open content of WL is exactly (i) the
front window `[R_N − O(10), R_N]` and (ii) heights beyond verification** — the same
frontier every route hits, but here in a per-N, finite, zero-geography form.

**WL(N=1): complete proof skeleton (night 2026-07-11).** Zero geography of `Ξ_1`
(NUMERICAL, high precision): real zeros exactly `±γ`, `γ = 14.04543957883…`; complex
zeros form one regular family `±a_k ± i b_k`, `k ≥ 0`, with
`(a_0,b_0) = (20.6253, 2.6972)`, `a_k − b_k` **strictly increasing from 17.9282**
(traced to k = 19, `a−b = 61.0`; `da_k > db_k` throughout, `db_k ↓`). Since a conjugate
pair `a±bi` contributes `2((x−a)²−b²)/|x−z|⁴ > 0` at real `x` iff `|x−a| > b`, and
`inf_k(a_k − b_k) = 17.93 > R_1 = 14.05`, EVERY term of the Hadamard identity
`L₁[Ξ_1](x)/Ξ_1(x)² = Σ_{zeros}(x−z)^{−2}` is individually positive on
`[0, 17.92) ⊃ [0, R_1]`. Hence WL(N=1) — in fact strict positivity — holds **termwise**,
given three proof obligations:
- **(P-a)** `Ξ_1` has order 1 (⟹ genus ≤ 1 Hadamard; evenness kills `e^{bz}`):
  straightforward from the integral representation (`log|Ξ_1(z)| ≲ (|z|/2)log|z|`).
- **(P-b)** Certified completeness of the zero list in a disc `|z| ≤ D` (D ≈ 110
  suffices): argument-principle counts, currently floating-point (integer to 1e−25);
  needs interval arithmetic for a proof (same tooling gap as T1-cert).
- **(P-c)** Tail: no complex zeros with `a − b < 18` (and none with `b < ½`, which
  simultaneously completes the N=1 strip theorem) for `|z| > D`. **RESOLVED IN
  PRINCIPLE (night 2026-07-11) — reduced to effective Stirling bookkeeping:**

  *Key identity (numerically dissected at x = 300; residual matches `−4d_1/x²` to 3
  digits):* expanding the lower incomplete gammas `γ(c, π) = π^c e^{−π}[1/c +
  π/(c(c+1)) + …]` and multiplying by `s(s−1)/2`, the O(x)-terms cancel pairwise and
  the O(1)-terms sum to `−(4π−1)e^{−π} = −C_1` **exactly cancelling the constant**
  (`(s−1)/(s+2) + s/(s−3) → 2` gives `−e^{−π}(4π−1)`); hence

  ```
  Ξ_1(z) = 𝒢(s) + 𝒢(1−s) + E(z),   𝒢(s) := (s(s−1)/2)π^{−s/2}Γ(s/2),
  |E(z)| ≤ C_E/x   (effective, for x ≥ D₀, 0 ≤ y ≤ x/2; s = ½−y+ix).
  ```

  Zeros require `|𝒢(s)+𝒢(1−s)| ≤ C_E/x`. By effective Stirling, `|𝒢(1−s)| ≍
  x^{7/4+y/2}π^{−¼−y/2}√(2π)e^{−πx/4}` grows in `y` while `|𝒢(s)|` shrinks, so zeros
  are confined to an `O(1/log x)`-tube around the explicit balance curve
  `y(x) ≈ (πx/4 − (11/4)log x − O(1)) / (½ log(x/2π))` — i.e. `b ~ πa/(2 log a)`
  (checked against the traced family: predicts 41.5 vs observed 43.45 at a = 104.5;
  30.5 vs 29.07 at a = 68.8). Consequences, all effective for `x ≥ D₀` (D₀ ≈ 40): every
  complex zero has `b ≥ ½` (tail of the N=1 strip theorem) and `b ≤ a/2` ⟹ `a − b ≥
  a/2 ≥ 18` (tail of WL(N=1)); for `y > x/2` the `𝒢(1−s)` term alone dominates —
  no zeros. Remaining writing: explicit Stirling constants (σ ∈ [−2,2], |t| ≥ 10 —
  standard) and the γ-series remainder (geometric in `π/|c|` — easy). Then WL(N=1) and
  T1(N=1) are theorems modulo (P-b) certification on the FINITE disc `|z| ≤ D₀ ≈ 40`
  (only ±14.045 and the first ~4 quadruplets to certify).

**Scope warning for N ≥ 2 (recorded before anyone tries the induction):** the same
two-term balance for `Ξ_N` replaces `𝒢(s)` by `Σ_{n≤N}`-completed terms — a completed
**Dirichlet polynomial** whose own strip-zero geography is a hard classical problem
(Turán partial-sum territory; partial sums of ζ are known to have zeros off the line).
The N=1 case closes precisely because no Dirichlet sum is present. A general-N windowed
theorem via this route needs new input on partial-sum zeros — do not assume the N=1
template scales.

The same (P-b)+(P-c) close T1 (theta-strip §2b(3d)): the two N=1 theorems share one
certification. Files: zero-family trace + asymptotic dissection in this session's log;
enumeration data `scratch/theta-strip/`.

### §8.9 INCONSISTENCY RESOLVED (2026-07-11): the DX paper's Theorem 1.1 is erroneous as printed

The three-way inconsistency (numerics `Re𝓛(111.1+0.45i) < 0`; identity
`FT[cosh(yt)ν₂] = 2Re𝓛(x+iy)`; DX Thm 1.1 as printed) is resolved: **links 1 and 2 are
correct; the printed theorem is false.** Full record + paper + verification scripts:
`scratch/dimitrov-xu-boundary/dx-erratum/`.

- **The error located:** DX Lemma 3.3 claims `ψ(x,y) = ℱ[sinh(·y)K](x)`; the RHS is
  purely imaginary (odd integrand) — a dropped `i`, squared to `−1` in the Wronskian,
  flips a sign in §3.1 and converts the true inside-weight `cosh(y(t−2s))` into their
  printed outside-weight `cosh(yt)`.
- **Unconditional counterexample to the printed form** from their own Cor. 4.3 b):
  `φ = 2 sin z/z ∈ 𝓛𝓟`, `ν₂ = ⅓(2−|t|)³`, yet `ℱ[cosh(yt)ν₂]` changes sign (e.g.
  `−0.495` at `(1.3, 5)`). Independent of RH and of our Ξ numerics.
- **Corrected criterion** (DX's remaining architecture goes through verbatim):

  ```
  RH ⟺ ∀y ∈ (−½,½)\{0}:  ℱ[K̃_{2,y}](x) = 2𝒞(x+iy) > 0 ∀x,
  K̃_{2,y}(t) = ∫(t−2s)² cosh(y(t−2s)) Φ(t−s)Φ(s) ds,
  𝒞(z) = |Ξ'(z)|² − Re(Ξ(z)·conj(Ξ''(z)))         [the Jensen quantity]
  ```

  Verified numerically: `𝒞(111.1+0.45i) = +2.44e−68 > 0` exactly where
  `Re𝓛 = −2.77e−69 < 0`. Also `+ all-y version` ⟺ real AND simple zeros.
- **Consequence for this attempt:** the corrected criterion is Jensen's classical
  convexity criterion repackaged — identical in content to §1's complex-Laguerre chain
  ([CsordasVarga1990, Thm 2.10]). The DX-specific `Re𝓛` handle evaporates; what
  survives is a **positive-kernel correlation representation of 𝒞**
  (`ℱ[K̃_{2,y}] = 2𝒞`), which is the correct object on which any future packet/grouping
  strategy must act (with the §8.6 corner-defect caution). TAGS: agent-verified with
  hand derivation; **needs one independent re-derivation of the Lemma-3.3 sign analysis
  (docs/07 Stage 4) before external use or author contact.** Cite [DimitrovXu2019] only
  in corrected form; no published erratum found as of 2026-07-11.
