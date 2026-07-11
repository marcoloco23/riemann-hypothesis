# PROGRESS LOG — Riemann Hypothesis

> **This file is the source of truth and must survive context loss.** Update it at the end
> of every work session. A fresh agent should be able to read only this file (plus the
> linked attempt `STATUS.md` files) and know exactly where things stand and what to do next.
> Newest entries on top.

## Current status

**Phase:** Four attempts open; systematic verification pass over externally-supplied
research notes completed. **RH is NOT solved; no claim of solution exists in this
repository.**
**Headline (2026-07-11):** User-supplied `notes.md` (two batches, ~4300 lines) was
decomposed into three new attempts + one lemma + a dead-end ledger, then **adversarially
verified by parallel agents**. Outcome: all checkable algebra in the notes was correct,
but two of its three "live targets" were **refuted** (finite theta-strip conjecture —
explicit strip zero of `Ξ_3` found; divisor-packet positivity — fails for every k), one
was shown RH-empty (Pick 2×2 layer — Davenport–Heilbronn passes it too), and the pass
uncovered **an apparent error in a refereed RH-criterion paper**: [DimitrovXu2019,
Thm 1.1] is false as printed (sign error in its Lemma 3.3; unconditional counterexample
from the paper's own Cor. 4.3 b; corrected form = Jensen's criterion `𝒞(x+iy) > 0`;
record in `scratch/dimitrov-xu-boundary/dx-erratum/`, pending one independent
re-derivation before external use). Net: strong negative knowledge, sharp new
sub-targets, zero progress at any actual wall — recorded honestly below.

## Definition of done (from docs/01)

A complete rigorous proof (or disproof) of the docs/00 statement, every step proved or
cited, passing all docs/06 litmus tests and the docs/07 protocol, ideally formalized in
Lean (`formal/`). Anything less is **progress, not a solution**, and is recorded as such.

## Active threads

| Thread | Approach family (docs/05) | Status | Current blocker (one sentence) |
|--------|---------------------------|--------|--------------------------------|
| [`attempts/li-positivity/`](attempts/li-positivity/STATUS.md) | §3 Weil positivity (Li's criterion) | OPEN | No mechanism converts `Λ(m) ≥ 0` into `λ_n ≥ 0`; positivity proved only for prime-free test windows ([ConnesConsani2021]). |
| [`attempts/pick-kernel-positivity/`](attempts/pick-kernel-positivity/STATUS.md) | §3 Weil positivity (Herglotz/Pick form, [Lagarias1999]) | OPEN | Prime-shift inequality (★) `𝒜[B] ≥ 2ΣΛ(n)n^{−½}⟨B,S_{log n}B⟩` unproved; everything verified so far is RH-empty (DH passes it), so the Euler product has not yet entered. |
| [`attempts/theta-strip/`](attempts/theta-strip/STATUS.md) | Haglund theta approximants / LP-class | OPEN (reframed) | Original per-N strip conjecture **REFUTED** (`Ξ_3` zero at `67.8802+0.4773i`); the moving-window replacement needs a windowed Pólya separation theorem that degrades at the front scale `t ≍ 4N²`. |
| [`attempts/laguerre-phase-space/`](attempts/laguerre-phase-space/STATUS.md) | dBN / Laguerre–Pólya / Dimitrov–Xu correlation | OPEN | No non-circular positivity mechanism for `L₁[Ξ] ≥ 0` [Csordas2015, OP 4.7] or its RH-equivalent off-axis form `𝒞(x+iy) > 0` (corrected DX/Jensen; see §8.9-resolution) via the positive kernel `K̃_{2,y}`. |

| [`attempts/fourier-rigidity/`](attempts/fourier-rigidity/STATUS.md) | none of docs/05 §1–8 — designated left-field program (Dyson quasicrystal + Viazovska-school interpolation + Kurasov–Sarnak Lee–Yang bridge) | OPEN (program adopted 2026-07-11; ROADMAP.md has rungs + kill criteria) | Rung 0 (lemma L8: explicit formula as crystalline-pair statement) unwritten, and the K1 soundness check (does prime comb + density + symmetry pin the zero multiset, given Bombieri–Lagarias' arbitrary-multiset phenomenon?) not yet run — everything gates on these two. |

**Parked (do not reopen without new input):** Lee–Yang/ferromagnetic route —
`scratch/notes-triage.md` §B (note: its constructive converse is now Rung 4 of
`attempts/fourier-rigidity/`).

## Proved lemmas (in `lemmas/`)

| Lemma | Statement (one line) | Tag |
|---|---|---|
| [L1](lemmas/L1-cayley-map-critical-line.md) | Cayley map `w=1−1/s` geometry | PROVED |
| [L2](lemmas/L2-zeta-xi-real-axis.md) | `ζ(σ)>1` for `σ>1`; `ξ` nowhere zero on ℝ | PROVED |
| [L3](lemmas/L3-li-converse-pringsheim.md) | `λ_n ≥ 0` eventually ⟹ RH (Pringsheim) | PROVED |
| [L4](lemmas/L4-logderiv-two-sided-bound.md) | `−Q ≤ xQ' ≤ Q` for `Q=ξ'/ξ(½+x)`, `x>½` — unconditional, **RH-empty by design** (DH satisfies it too) | PROVED (symbolic verification; hostile re-read wanted) |
| [L5](lemmas/L5-theta-representation-effective-convergence.md) | `Ξ = 4∫₀^∞Σφ_n cos(zu)du` (full derivation) + `|Ξ−Ξ_N| ≤ 8.01π(N+1)²e^{−π(N+1)²}` on the strip | PROVED (hostile re-read wanted) |
| [L6](lemmas/L6-pick-kernel-criterion.md) | RH ⟺ Pick kernel `(Q(x)+Q(y))/(x+y)` PSD on `(X,∞)` — full equivalence proof | PROVED (one textbook citation to pin; hostile re-read wanted) |

Candidate lemmas queued: L7 (Laguerre generating identity), phase-space identity,
`Ξ ∈ 𝔖(½)` write-up, WL ⟹ OP 4.7 (proof written in laguerre-phase-space §8.10 —
promote after re-read); E-items per attempt STATUS files.

## Key verified facts & refutations from the 2026-07-11 verification pass

All scripted + reproducible; scratch dirs have README + run-output + pinned deps.
Numerics are motivational only (docs/01 B1).

1. **`scratch/pick-kernel/`**: notes' quartet identities + 2×2 factorization + 3×3
   determinant formula all PROVED symbolically (3×3 sign threshold is `|v/u| < 1`, not
   0.072). ζ Pick matrices PSD (N ≤ 8). **DH's mandatory negative direction not found:
   masked ≥ 3.2e6× by on-line background — structural, not precision.** Prime
   representation of Q verified to 1e−61; `Q(½⁺) = 1+γ/2−½log4π`.
2. **`scratch/theta-strip/`**: normalization pinned (`Ξ_N = 4∫₀^∞`, atom constants ¼);
   Haglund zeros reproduced; `R_N ≈ 4(N+1)²` confirmed (R₂ = 39.5325, R₃ = 65.0321);
   **REFUTATION: `Ξ_3(67.8801896551 + 0.4773438418 i) = 0`** — see
   `scratch/theta-strip/STRIP-ZERO-N3.md`; N=1,2 strip-free, N=4 strip-free to Re ≤ 200
   (min nonreal Im 0.73).
3. **`scratch/laguerre-phase-space/`**: Laguerre generating identity, hierarchy
   `∂_tL_n = −½∂_x²L_n + (n+1)(2n+1)L_{n+1}`, and phase-space identity all VERIFIED
   (the notes' two variants are exactly equal). `L₁, L₂ > 0` on grid incl. Lehmer point
   (`1.23e−4765 > 0` at `x=7005.063`). **Tooling pitfall: `mpmath diff(method='quad')`
   silently ~1.4% wrong for tiny-magnitude functions — use trapezoid Cauchy w/
   N-doubling.**
4. **`scratch/dimitrov-xu-boundary/`**: boundary sign change VERIFIED
   (`B(t) < 0` on `(110.458, 111.479)`, first crossing `t* = 110.45825828…`, robust to
   dps 210) — boundary minimum-principle route dead. `𝓛 = ¼·FT[C]` verified (Jacobian
   factor 2 correction to notes' packet sketch). **Divisor-packet positivity REFUTED for
   every k ∈ {1,2,3,4,6}** (corner defect of `φ_n(|u|)`). **Interior-line negativity
   persists (σ = 0.95, 0.90, dps 200)**, forced by the close pair `γ₃₄, γ₃₅ ≈ 111.03,
   111.87 — `Re𝓛 < 0` near close pairs even under RH. This exposed the §8.9
   inconsistency, RESOLVED by the paper-reader pass: **[DimitrovXu2019, Thm 1.1] is
   erroneous as printed** (Lemma 3.3 sign error; their own `2sin z/z` example refutes
   the printed form; corrected kernel `K̃_{2,y}` has `cosh(y(t−2s))` inside;
   `ℱ[K̃_{2,y}] = 2𝒞(x+iy)` — Jensen quantity, `+2.44e−68 > 0` exactly where
   `Re𝓛 < 0`). Record: `scratch/dimitrov-xu-boundary/dx-erratum/`.

## Numerics (motivational only, doc 01 B1)

- `scratch/li-coefficients/` (session 1): `λ_n(ζ) > 0` for `n ≤ 40`; DH calibration —
  first negative `λ_n(f)` predicted at `n ~ 3.5e5`.
- New scratch dirs (this session): `pick-kernel/`, `theta-strip/`,
  `laguerre-phase-space/`, `dimitrov-xu-boundary/` — each with README, deterministic
  scripts, pinned mpmath 1.3.0 / sympy 1.14.0, run-output.txt.

## Dead ends recorded (see `scratch/notes-triage.md` §C for the full 12-item ledger)

Highlights this session: naive Li Cauchy-estimate (circular, tangent-disk); per-N
real-rootedness AND per-N strip-freeness of theta truncations (both FALSE — explicit
zeros); PF₅ total positivity (FALSE, [Michalowski2026]); block-energy collision route
(exact failure at the clock configuration); backward-dBN + zero counting (superpolynomial
amplification); Pólya convexity of the correlation kernel (`C''(0) < 0`); boundary
`Re s = 1` positivity (sign change t* ≈ 110.458); divisor packets (corner defect);
pointwise `Re𝓛 ≥ 0` on interior lines (false even under RH near close pairs); mpmath
`diff(method='quad')` on tiny scales (tooling).

## Session history

- **2026-07-11 (session 2, night shift — attack pass).** New PROVED material:
  **[L5]** (self-contained analytic derivation of `Ξ = 4∫Σφ_n cos` + effective tail
  `ε_N = 8.01π(N+1)²e^{−π(N+1)²}` uniform on the strip — theta machinery no longer
  leans on uncited assertions); **[L6]** (Pick-kernel criterion RH-equivalence fully
  proved, E1/E2 closed; one textbook citation to pin); moving-window ⟺ RH; endpoint-
  defect principle (unifies all per-N refutations; extends to L₁: every truncation has
  `L₁ ~ −2J_N²/x⁶ < 0` eventually ⟹ no unwindowed truncation route to Csordas OP 4.7);
  Rouché reality lemma; defect sign lemma (`d_N > 0 ∀N`; `π` vs root `3.1559`
  near-miss); far-tail zone P2 with computed `T_N` (`T_1 = 90.6`: N=1 strip theorem
  reduced to a finite certifiable computation); (★) moment reformulation (kernel PSD ⟺
  Nevanlinna measure ≥ 0 — a dilation would BE the Hilbert–Pólya measure; no cheaper
  identity exists). **NEW CONJECTURE WL** (windowed Laguerre: `L₁[Ξ_N] ≥ 0` on
  `[0, R_N]`): PROVED WL ⟹ OP 4.7; NUMERICAL for N ≤ 6; bulk part provable
  height-capped (WL''); open content = front window + unverified heights. Campaign
  findings: `Ξ_N^{sd} ≡ Ξ_N` identically (self-dual family = one-sided family —
  closes the last packet-salvage idea); L₁-front tables N=1..6; P2 constants N=1..8.
  Late-night addition: **WL(N=1) and the N=1 strip theorem reduced to (i) effective
  Stirling bookkeeping (strategy complete: `Ξ_1 = 𝒢(s)+𝒢(1−s)+E`, `|E| ≤ C/x`, via the
  exact `C_1`-cancellation in the lower-gamma expansion; zero-tube around
  `b ~ πa/(2 log a)` verified against the traced 20-zero family) + (ii) interval
  certification on `|z| ≤ 40`** — two N=1 theorems one write-up + one certified
  computation away. Scope warning recorded: the N≥2 induction hits Dirichlet
  partial-sum zero geography (Turán territory), do not assume it scales. Front-law campaign
  verdict (N = 3..8 complete): **front law supported** — N=8: no strip zeros, min
  nonreal Im 0.566, `R_8 = 327.38 ≈ 4·81` (minor caveat: N=8 polish reality-check
  incomplete, symmetric-box counts cover it); — a second strip zero found
  at N=7 (`260.288+0.347i`, `Re/(4(N+1)²) = 1.017`, `Re > R_7`), bulk clean for all N,
  front-zero heights quasi-random (strip zeros recur sporadically, always
  front-confined) — table in theta-strip PROOF.md §2b(3e). **RH remains open; the
  walls are unchanged but now have exact shapes, and two N=1 theorems (T1 + WL(N=1))
  are one Stirling write-up + one certified computation from done.**
- **2026-07-11 (session 2).** Absorbed user `notes.md` (2 batches, 4320 lines) into
  `attempts/pick-kernel-positivity/`, `attempts/theta-strip/`,
  `attempts/laguerre-phase-space/` + `scratch/notes-triage.md`; ran 6 parallel
  verification agents (3 math, 2 literature, 1 paper-reader in flight) + direct root
  hunting. Results: L4 proved+promoted; theta-strip conjecture refuted at N=3 and
  attempt reframed (moving-window); divisor packets refuted; boundary route refuted;
  Pick 2×2 layer shown RH-empty w/ quantified DH masking (≥3.2e6×); bibliography +12
  entries all source-verified ([Lagarias1999]+correction, [Haglund2011],
  [DimitrovXu2019], [Csordas2015], [CsordasVarga1988/1990], [CSV1994], [RodgersTao2020],
  [Polymath15-2019]+[PlattTrudgian2021], [Michalowski2026], [BianePitmanYor2001],
  [Suzuki2023/2026], [Connes2026], [CCM2024/2025]). §8.9 DX-inconsistency RESOLVED
  in-session: [DimitrovXu2019] erroneous as printed, corrected criterion = Jensen
  (`dx-erratum/` record). Lean toolchain still absent.
  **No progress at any actual wall; RH remains open.**
- **2026-06-09 (session 1 of solving agent).** Read docs/00–07. Opened
  `attempts/li-positivity/` (docs/05 §3); proved L1–L3; Li-coefficient numerics for ζ
  and DH; scoped sub-target Q1. **No progress at the actual wall.**
- **(setup)** Repository scaffolded.

## Next-session priorities (in order)

1. **Independent re-derivation of the DX Lemma-3.3 sign analysis** (docs/07 Stage 4
   discipline; `dx-erratum/README.md` follow-ups) — the erratum finding is significant
   and must be double-checked before any external communication; then decide with the
   user whether to contact the authors.
2. theta-strip action 2: locate ALL strip zeros for N = 3..8 (fix the locator dedup
   bug), test the front law `Re ≥ c·4(N+1)²` — second clean kill test for the
   moving-window form.
3. Write L5 (loc-unif convergence), then E1/E2 items (pick-kernel criterion → PROVED;
   `Ξ ∈ 𝔖(½)` write-up).
4. li-positivity Q1 (unchanged from session 1) and the function-field analogue note.
5. Install Lean toolchain; formalize L1, L2 (then L3, L4).
