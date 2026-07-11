# STATUS — pick-kernel-positivity

**State:** OPEN (frame promising; the wall is the same Weil-positivity wall as
li-positivity, docs/05 §3).

**Precise current blocker (one sentence):** No non-circular mechanism to prove the
prime-shift correlation inequality (★) `𝒜[B] ≥ 2ΣΛ(n)n^{−1/2}⟨B, S_{log n}B⟩` for all
exponential sums `B(u)=Σc_j e^{−x_j u}`, `x_j > ½` — this is Weil positivity restricted to
a cone, and every known route to it is equivalent to RH.

**Verification complete (2026-07-11, `scratch/pick-kernel/`):** §3 identities PROVED
symbolically → promoted to lemma [L4]; 2×2 determinant equivalence PROVED; 3×3 quartet
determinant formula PROVED (sign threshold corrected: `|v/u| < 1`, notes' 0.072 was
conservative ×14); ζ Pick matrices PSD for N ≤ 8 (NUMERICAL); prime representation of
`Q` verified to 1e−61.

**Litmus finding (important):** the DH kernel's mandatory non-PSD direction was NOT
found numerically — quartet negativity is masked by the on-line background by a factor
≥ ~3.2e6 across all probed configurations (structural `(v/A)²` suppression, not
precision). AND lemma L4 holds for DH verbatim. Net: everything verified so far is
RH-empty; the Euler product enters nowhere yet. This quantifies T2 and lowers confidence
that finite-matrix arguments can be the mechanism.

**Depends on lemmas:** L2 (`Q` well-defined), **L4** (two-sided bound, PROVED,
RH-empty by design). E1/E2 exposition items still open for the criterion itself.

**Honest assessment:** frame fully verified; zero progress at the wall (★); the litmus
quantification is genuine negative knowledge steering effort toward the summed prime
form (T3) and away from finite-minor exclusion.

**Update 2026-07-11 (night):** E1/E2 written in full — the criterion is now **lemma
[L6] (PROVED)**, self-contained apart from one flagged textbook citation (finite
Nevanlinna–Pick, Donoghue — theorem/page to pin). The attempt now rests on proved
ground; the wall (★) is unchanged.

**Next actions:**
1. Pin the Donoghue citation (theorem/page) when the volume is at hand; hostile
   re-read of L6.
2. T3 (dilation of 𝒜−𝒫 on the exponential cone) — first compare against
   [ConnesConsani2021]/[Suzuki2026] walls before investing; the mechanism must inject
   `Λ(n) ≥ 0`/multiplicativity, which no verified piece yet does.
3. Optional T2': hunt the DH negative direction with structured (Vandermonde-like /
   large-N clustered) coefficient vectors to calibrate detectability — bounded effort.
