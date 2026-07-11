# STATUS — laguerre-phase-space

**State:** OPEN. Batch-2's two live targets both DIED under verification (divisor
packets REFUTED ∀k, §8.6; interior-line `Re𝓛` positivity REFUTED as premise, §8.7);
boundary route dead (`B` sign change at t* = 110.458…). **§8.9 RESOLVED:** the
inconsistency traced to a sign error in [DimitrovXu2019] itself (Lemma 3.3; theorem
false as printed, unconditional counterexample from their own Cor. 4.3 b); the
corrected criterion is `𝒞(x+iy) > 0` (Jensen quantity) with positive-kernel
representation `ℱ[K̃_{2,y}] = 2𝒞` — record + scripts in
`scratch/dimitrov-xu-boundary/dx-erratum/`. Needs one independent re-derivation
(docs/07 Stage 4) before external use.

**Precise current blocker (one sentence):** The surviving live objects are the open
first Laguerre inequality `L₁[Ξ] ≥ 0` [Csordas2015, OP 4.7] and its off-axis extension
`𝒞(x+iy) > 0` (⟺ RH, corrected DX / Jensen) via the positive correlation kernel
`K̃_{2,y}` — and no non-circular positivity mechanism for either is known; any packet
decomposition of `K̃_{2,y}` must avoid the §8.6 corner defect (use the self-dual
completion, not `|u|`-reflection).

**Verification complete for the original batch (2026-07-11,
`scratch/laguerre-phase-space/`):** (G) VERIFIED (exact identity); (H) VERIFIED at
integrand level (E2: differentiation-under-integral remains as stated hypothesis);
(W) VERIFIED — both notes variants are exactly equal (ψ even); `L₁, L₂ > 0` on 33-point
grid incl. Lehmer region (`1.23e−4765 > 0` at x = 7005.063, two independent methods).
⚠️ Tooling pitfall found and recorded: `mpmath diff(method='quad')` is silently wrong
(~1.4% rel.) for tiny-magnitude functions — use explicit trapezoid Cauchy with
N-doubling validation (see scratch README).
**Still in flight:** `scratch/dimitrov-xu-boundary/` — B(t) sign change near t≈110.5,
C''(0)<0, divisor-packet kill test, interior-line scans.

**Citations pinned (2026-07-11):** LP ⟺ L_n ≥ 0 is [CsordasVarga1990, Thm 2.9]; complex
Laguerre inequality is [CsordasVarga1990, Thm 2.10] / [CsordasEscassut2005, Thm 2.4];
both need `f ∈ 𝔖(A)` (zeros in a horizontal strip) — and `Ξ ∈ 𝔖(½)` holds
**unconditionally**, so the chain is usable with no RH input (PROOF.md §1).

**Depends on:** candidate lemmas L6 (phase-space identity), L7 (hierarchy + generating
identity); E1 (`Ξ ∈ 𝔖(½)` write-up).

**Honest assessment:** the equivalence chain is now fully cited and applicable; the
dead-end recordings (§5) are solid and independently valuable; the live target (9) is
untouched analytically.

**Next actions:**
1. Incorporate scratch results; settle the exact (W) constant; retag.
2. Run V1 (packet positivity scan) and V2 (DH failure) — either can kill or
   substantially de-risk the attempt cheaply.
3. If V1/V2 pass: T3 diagonal-packet closed forms.
