# Attempt: fourier-rigidity (the quasicrystal program)

**Approach family (docs/05):** none of §1–8. This is a deliberate left-field program:
RH as a **rigidity/classification theorem for crystalline measure pairs** (Dyson's
2009 "quasicrystal" proposal, made concrete with the modular-interpolation technology
of the Viazovska school and the Lee–Yang/quasicrystal bridge of Kurasov–Sarnak).

**The idea (one paragraph).** Under RH, the explicit formula says the zero measure
`μ = Σ_γ δ_γ` is a *crystalline measure*: a tempered atomic measure whose Fourier
transform is again atomic, supported on `±log(prime powers)` with weights
`Λ(n)/√n ≥ 0` plus an explicit archimedean density. Unconditionally, the same formula
holds but with `μ` replaced by a complex-atom object (atoms at `γ + i(β−½)`), i.e. a
"quasicrystal with possibly non-real support." RH is then EXACTLY the statement:

> the summation-formula constraints (spectrum in the log-prime set, positive
> multiplicative weights, ξ-symmetries, density `~(T/2π)log T`) **force the support
> onto the real line**.

That is a *Fourier-rigidity statement* — a genre in which real theorems exist and are
improving yearly (Lev–Olevskii rigidity for uniformly discrete pairs; Kurasov–Sarnak
Fourier quasicrystals from Lee–Yang varieties; Radchenko–Viazovska interpolation;
Bondarenko–Radchenko–Seip interpolation with ζ-zero nodes — citations to pin, see
ROADMAP §C). **The bet is about toolkit, not about a weaker statement:** the rigidity
target implies Weil positivity and is RH-hard; but rigidity theorems in harmonic
analysis are proved by uniqueness-pair and interpolation-basis arguments whose engines
(modular magic functions, stable/Lee–Yang polynomials) are NOT positivity arguments —
they construct the object instead of estimating it. That is precisely the missing move
everywhere else.

**Why this fits everything we verified in-repo:** the moment reformulation
(pick-kernel §5b) says the wall = "produce the measure"; the Lee–Yang route (triage §B)
reappears here as the *construction mechanism* (Kurasov–Sarnak build quasicrystals from
Lee–Yang objects — the converse traffic of what we tried); the theta truncations are
finite approximants of the crystalline pair, and the front-law campaign measured their
**defect confinement** (strip zeros = boundary defects of a growing quasicrystal,
confined to `[R_N, 1.07·4(N+1)²]` — the approximation theory of the program's central
object, gathered before we had its name).

**Origin:** night session 2026-07-11, direction chosen by explicit intuition bet after
the systematic mapping of all conventional walls. See `ROADMAP.md` for the program,
rungs, kill criteria, and litmus audit.
