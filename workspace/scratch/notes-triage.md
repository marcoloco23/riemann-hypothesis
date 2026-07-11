# Triage of notes.md (user-supplied research notes, absorbed 2026-07-11)

The root-level `notes.md` (4320 lines after a second batch was added mid-session;
appears to be a transcript of an extended AI-assisted exploration) was decomposed into
the structures below and then removed.
This file is the map. Nothing in the notes claimed a proof of RH; the notes' own verdict
("rigorous compressions + one identifiable target per route, no proof") was accurate.

## Where each thread went

| notes.md thread | Destination | One-line content |
|---|---|---|
| Li coefficients: RH ⟺ `limsup|λ_n|^{1/n} ≤ 1` ⟺ subexponential `λ_n`; circularity of the naive coefficient bound (Euler-product disk `|z−½|<½` tangent to, not covering, 𝔻) | `attempts/li-positivity/` already covers Li; the radius-of-convergence framing + the tangent-disk circularity note added below (§A) | Compression, no new wall |
| Herglotz/Pick: RH ⟺ `M_ξ` Herglotz; Schur `Θ_ξ`; high-strip anchoring via Suzuki-style finite Weil operators; shift-parameter contamination as missing lemma | `attempts/pick-kernel-positivity/` (background §; the operator-limit route noted in its PROOF.md §7 T3 comparisons) | The Suzuki-limit route's own missing lemma (shift normalization) recorded there |
| Pick-kernel criterion on the real axis; unconditional 1×1/2×2; 3×3 quartet detection; prime-shift inequality 𝒜−𝒫 ≥ 0 | `attempts/pick-kernel-positivity/` (main content) | The attempt's core |
| Lee–Yang / Brownian-bridge route | Parked here, §B below | Includes its own recorded counterexample |
| Haglund theta truncations: real-rootedness FALSE; real-zero front `R_N ≈ 4(N+1)²`; finite theta-strip target; tanh multiplier; atom ordering; τ-interpolation leak | `attempts/theta-strip/` | The attempt's core |
| de Bruijn–Newman collision program; block-energy identity failure; backward instability; Laguerre hierarchy; ultrahyperbolic PDE; phase-space inequality (9) | `attempts/laguerre-phase-space/` (live target §3–4; dead ends §5) | The attempt's core + two exact dead ends |
| **Batch 2 (lines 2776–4320):** Dimitrov–Xu correlation criterion; `ν̂₂ = 2𝓛`; `L₁[Ξ] ≥ 0` open; Pólya-convexity dead end (`C''(0)<0`); diagonal packets not the mechanism; boundary `Re s=1` route + its numerical refutation (`B(110.5)<0`) and endpoint-integrability diagnosis; divisor-packet grouping `k=mn`; interior-line nonvanishing program | `attempts/laguerre-phase-space/` PROOF.md §8 (supersedes its §3–4 framing) | Three new dead ends + two live targets |

## §A. Li-thread additions (for attempts/li-positivity, do not lose)

1. **Radius-of-convergence form.** RH ⟺ `limsup|λ_n|^{1/n} ≤ 1` via
   `log ξ(1/(1−z)) = −log2 + Σ(λ_n/n)zⁿ` and Cauchy–Hadamard; so ANY subexponential
   bound `|λ_n| ≤ C_ε e^{εn}` (even `O(n^100)`) proves RH. TAG: CLAIMED (consistent with
   L3's Pringsheim converse already in `lemmas/`).
2. **Why the obvious bound is circular (recorded wall):** the Euler-product-controlled
   region `Re s > 1` maps under `s = 1/(1−z)` to the disk `|z−½| < ½` — tangent to the
   unit circle at `z=1`, not covering 𝔻. Extending coefficient control to all of 𝔻 needs
   `ξ'/ξ` control on `Re s > ½`, i.e. RH. Do not retry naive Cauchy-estimate routes.
3. **Detection-scale heuristic (NUMERICAL/heuristic only):** an off-line zero at height
   `γ`, offset `δ`, first affects `λ_n` at `n ~ γ²/δ` (scale `exp(δn/γ²)`), matching the
   li-positivity scratch estimate (first negative `λ_n` for DH at `n ~ 3.5e5`).

## §B. Parked route: Lee–Yang / ferromagnetic approximation (do not reopen without new input)

- Facts ([BianePitmanYor2001], eqs. (1.4)–(1.5), pinned 2026-07-11): ∃ positive r.v. `Y`
  (`= √(2/π)·`range of Brownian bridge, `Y² =_d (1/π)ΣΓ_{2,n}/n²`) with `E[Y^s] = 2ξ(s)`
  for ALL `s ∈ ℂ`; size-biasing + `X = log Y`
  gives `Z(z) = E_*[e^{zX}] = ξ(½+z)/ξ(½)`, so RH ⟺ `X` has the Lee–Yang property
  (zeros of `Z` purely imaginary).
- Sufficient (unproved) theorem: realize the size-biased law as a locally-uniform limit
  of ferromagnetic magnetization laws ⟹ Lee–Yang theorem + Hurwitz ⟹ RH.
- **Recorded counterexample (why parked):** the symmetrized gamma truncation
  `F_1(s) = ½[π^{−s/2}Γ(2+s/2) + π^{−(1−s)/2}Γ(2+(1−s)/2)]` satisfies the functional
  equation and positivity yet has noncritical zeros (NUMERICAL, from notes; not
  independently re-verified — re-verify before citing). Moral: functional symmetry +
  positivity is nowhere near sufficient; an approximation must carry genuine
  Hermite–Biehler / Lee–Yang structure. The better truncation (positive, self-dual
  `H_N` with `yH_N(y) = H_N(1/y)`) feeds the theta-strip attempt instead.

## §C. Global dead-end list contributed by the notes (cross-attempt)

1. Naive Li coefficient bound — circular (§A.2).
2. Real-rootedness of finite theta truncations — FALSE (theta-strip PROOF.md §1).
3. Total positivity / PF-∞ of the Riemann kernel — FALSE at PF order 5
   ([Michalowski2026], unrefereed preprint w/ certified interval arithmetic; PF₄ open;
   theta-strip §5, laguerre-phase-space litmus).
4. Continuous-τ atom interpolation strip-preservation — leaks (theta-strip §3.4).
5. Symmetrized probabilistic truncations — fail Hermite–Biehler at N=1 (§B).
6. Raw block-energy collision prevention under backward dBN — exact failure
   (laguerre-phase-space §5.1).
7. Zero-counting inputs into backward dBN flow — killed by `exp((τ/16)log²T)`
   amplification (laguerre-phase-space §5.2).
8. Pólya convexity of the correlation kernel — `C''(0) < 0` by log-concavity of Φ
   [CsordasVarga1988] (laguerre-phase-space §8.2).
9. Boundary `Re s = 1` positivity + minimum principle — `B(t)` changes sign at
   `t* = 110.4582…` (VERIFIED dps 130/170/210) + endpoint non-integrability
   (laguerre-phase-space §8.4).
10. Divisor-packet (`k = mn`) Fourier positivity — REFUTED for every tested k;
    corner defect of `φ_n(|u|)` extension (laguerre-phase-space §8.6).
11. Pointwise `Re𝓛 ≥ 0` on interior horizontal lines — FALSE even under RH near
    close zero pairs (`Re(z−γ)^{−2} < 0` for `|x−γ| < y`); persists to σ = 0.90
    (laguerre-phase-space §8.7). NOTE: exposed an open inconsistency with
    [DimitrovXu2019] as quoted — see §8.9 there.
12. **Finite theta-strip conjecture (per-N) — REFUTED**: `Ξ_3` vanishes at
    `67.8802 + 0.4773i`, inside `0<Im z<½` (margin 0.023), just past the front
    `R_3 ≈ 65.03` (`scratch/theta-strip/STRIP-ZERO-N3.md`). The notes' "Im ≳ 2.7
    for N ≤ 10" claim is FALSE. Attempt reframed to the moving-window form
    (theta-strip PROOF.md §2 revised).

## §D. Notes' claims deliberately NOT absorbed as fact

- "Connes's 2026 survey concludes …" — CONFIRMED: [Connes2026] = arXiv:2602.04022
  (Feb 2026); RH open as of that survey.
- All specific numerics (Haglund zeros, `R_N` table, `0.072` bound, `Λ < 0.2`) —
  under independent verification in `scratch/pick-kernel/`, `scratch/theta-strip/`,
  `scratch/laguerre-phase-space/`.
- The notes' equivalence arguments — re-audited in each attempt's PROOF.md; exposition
  items (E1/E2 per attempt) must be written before any PROVED tag.
