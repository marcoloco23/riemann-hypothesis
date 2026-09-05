# Fourier rigidity — revised roadmap, 2026-09-05

**The agreed bounded research cycle is complete.** Its deliverables and
verification are mapped in [COMPLETION.md](COMPLETION.md). The review gate
below is the next phase; formalization was explicitly deferred in the plan.

## Current conclusion

The first structural test of the relaxed class returns a **singleton**, not
a family of systems to rigidify. [L9](../../lemmas/L9-positive-comb-singleton.md)
derives a Dirichlet series from the unchanged S1–S3 assumptions and applies
Hamburger's converse theorem. It follows that `(R′) ⇔ RH`. This is a written
characterization proof with same-agent audit; independent review remains open.

RH remains open. The result constrains this research program, not the real
parts of ζ's zeros. The [original roadmap](ROADMAP-2026-07-12.md) is archived
with its historical assertions explicitly superseded.

## Completed research cycle

1. Audited L8b's repaired Gaussian argument and supplied a second resolvent
   derivation; corrected its weighted-space definition and simplified evenization.
2. Corrected the finite-defect corollary, comb sign, and Fourier terminology.
3. Proved `Σ_{n≤X}w_n=O(√X)`, extended the explicit formula to exponential
   tests, reconstructed the canonical numerator and Dirichlet series, and checked
   every hypothesis of Hamburger's two-function theorem (L9).
4. Completed the DH comparison, including exact completion, a convergence
   half-plane, a negative coefficient and a separate background exclusion (L10).
5. Reproduced the old numerical anchors and added a smooth compact test with
   precision and quadrature doubling. Numerical tails are not certified.
6. Proved the weight asymptotics `Σw_n~2√X` and `Σw_n√n~X` directly
   from S1–S3, independently of the reconstruction/Hamburger route.

Details and hypothesis table: [AUDIT-2026-09-05.md](AUDIT-2026-09-05.md).

## Next gate: independent review

Before treating L9 as independently verified, obtain a fresh review of:

- The translated-test estimate and the passage from log intervals to `O(√X)`.
- The weighted second-derivative bound for mollified exponential tests,
  including convergence of W_∞ at its singular origin.
- The paired canonical product, its finite order and the factor of two in
  its logarithmic derivative.
- The gamma cancellation at s=0, normalization at +∞, and handling of an
  odd central multiplicity with the two-function Hamburger theorem.

Acceptance: each step proved or cited with matching hypotheses, and no use
of RH, a zero-reality assumption, or an unstated coefficient axiom. A gap
changes L9's tag and reopens only that precise step. A confirming review
retains the singleton conclusion and the retired targets below.

## Retired targets and conditions for a successor

- Retire the K1 hunt for distinct systems satisfying this exact S1–S3.
- Retire Rung 3's fixed-comb perturbation target. Fixed data already determine
  the divisor; “ζ-local rigidity” does not fix this issue.
- Park broad Lee–Yang classification and interpolation investment. Before
  adopting a successor, define the altered background or approximate identity,
  construct at least one genuinely distinct admissible example, and state which
  additional theorem would constrain its zero locations. These are prerequisites,
  not a claim that such a successor exists.
- Keep the existing theta finite-model research available as a separate,
  bounded project; it has not been reopened during this cycle.

No large search, author correspondence, or Lean installation is part of
this cycle. Formalization remains a later verification layer.
