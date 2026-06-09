# STATUS — li-positivity

**State:** OPEN (active; first session 2026-06-09).

**Blocker (one sentence):** No known mechanism converts the Euler-product positivity
`Λ(m) ≥ 0` — which enters the explicit-formula expression for `λ_n` with a *negative*
sign — into the target inequality `λ_n ≥ 0` for all (or all large) `n`; this is the
Weil-positivity wall of docs/05 §3, unproven for every test-function class whose support
reaches the first prime.

**Depends on lemmas:**
[L1](../../lemmas/L1-cayley-map-critical-line.md) (PROVED),
[L2](../../lemmas/L2-zeta-xi-real-axis.md) (PROVED),
[L3](../../lemmas/L3-li-converse-pringsheim.md) (PROVED — criterion direction only).

**Litmus state:** frame audited against LITMUS-1..5 (PROOF.md §5); no positivity claim
exists yet to gate. Every future draft claiming positivity must identify the line where
`Λ(m) ≥ 0` / the Euler product is load-bearing and show the argument breaks for
Davenport–Heilbronn.

**Next actions (in order):**
1. Transcribe [BombieriLagarias1999, Thm 2] verbatim (arithmetic formula for `λ_n`);
   re-verify against `scratch/li-coefficients/` numerics before any use.
2. Execute sub-target Q1 (PROOF.md §6): explicit `N₀(T₀)` with proof `λ_n > 0` for
   `n ≤ N₀` from cited verified zeros — main work item: the lower bound
   `Σ_{|γ|≤T₀}(1 − cos nθ_ρ) ≫ n`.
3. Write the function-field Li-positivity analogue in `notes/` (PROOF.md §7, last item)
   to localize the missing `Spec ℤ` object.
4. Initialize `formal/` (Lean 4 + mathlib; toolchain currently absent on this machine)
   and formalize L1, L2 as first targets.

**Honest assessment:** scaffolding solid; distance to RH unchanged. This attempt's
realistic near-term value is Q1 plus a clean formalization seed — partial progress per
docs/05, not a path to a solution as currently understood.
