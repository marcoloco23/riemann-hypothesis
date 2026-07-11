# STATUS — theta-strip

**State:** OPEN, reframed — **the original per-N strip conjecture was REFUTED this
session** (the clean-kill scenario): `Ξ_3` has a zero at `67.8802 + 0.4773i`, inside
the strip with margin 0.023 (`scratch/theta-strip/STRIP-ZERO-N3.md`). The attempt
continues with the weakened **moving-window strip target** (PROOF.md §2 revised), whose
conditional route to RH is equally valid and which all data support (strip zeros appear
only at the escaping front `Re ≍ 4(N+1)²`).

**Precise current blocker (one sentence):** No proof of the windowed common-zero
exclusion (PROOF.md §4 revised): the two transforms have no common zero for `0<r<½`,
`t ≤ c·N²` — and any proof must explicitly degrade at the front scale `t ≍ 4N²`, which
no classical Pólya-separation hypothesis encodes.

**Verification complete (2026-07-11, `scratch/theta-strip/`):** normalization pinned
(`Ξ_N = 4∫₀^∞…`, atom constants ¼); Haglund zeros reproduced to ~4e−9; `R_2, R_3`
confirmed; §3.1 identity validated (`C_N + (s(s−1)/2)I_N`, constants 1); strip scans:
N=1,2 zero-free (counts integer to ≤1e−25), **N=3 count 1 (the refuting zero)**, N=4
zero-free up to Re ≤ 200 (min-Im of nonreal zeros 0.73). Known bug: N=4 located-zero
enumeration produced spurious duplicates (640 vs count 7) — counts are the trustworthy
output; do not reuse the locator without fixing dedup.

**Depends on:** locally uniform convergence `Ξ_N → Ξ` (candidate lemma L5 — asserted in
[Haglund2011], must be proved in-repo); Hurwitz local form (cite [Remmert1991]).

**Honest assessment:** the session's main product here is a genuine refutation plus a
principled repair. The revised wall now has one more structural input (front scale).
The N=3 zero's 0.023 margin says the strip boundary ½ is NOT special for truncations —
only the limit function respects it; a correct proof must use convergence-to-Ξ, not
per-N structure alone. LITMUS audit of §6 unchanged (V1 still worth running).

**Night update (2026-07-11):** [L5] PROVED (action 1 done — representation +
effective ε_N, in `lemmas/`). Action 2 done for N ≤ 7 (PROOF.md §2b(3e)): front law
SUPPORTED — second strip zero found at N=7 (`260.288+0.347i`, ratio 1.017), bulk clean
everywhere, front-zero heights quasi-random ⟹ strip zeros recur but stay
front-confined. Additional structure proved: §2b(1)–(3d) (moving-window ⟺ RH;
endpoint-defect principle; Rouché reality; defect sign `d_N > 0`; far-tail P2 with
`T_1 = 90.6`). T1(N=1) has a complete proof strategy (shared with WL(N=1) — see
laguerre-phase-space §8.10): effective Stirling write-up + interval certification on
`|z| ≤ 40` remain.

**Next actions:**
1. Write the (P-c) Stirling bookkeeping for N=1 (constants explicit) → T1 + WL(N=1)
   theorems modulo certification.
2. Interval-arithmetic certification tooling (arb/flint) for (P-b) — shared
   infrastructure for T1-cert and future disproof-grade numerics (docs/01 D).
3. V1 (DH strip litmus) still open; the windowed separation theorem (§4) for general N
   remains the wall (Dirichlet partial-sum scope warning recorded).
