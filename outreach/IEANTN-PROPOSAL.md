# Draft scope proposal for IEANTN

**Destination:** Lean Zulip, `#PrimeNumberTheorem+`  
**Purpose:** Ask maintainers to choose the correct node scope before implementation.  
**Status:** Ready for human review and posting after the repository is public.

## Proposed message

We maintain an open, reproducible, explicitly non-solution-claiming research repository
on the Riemann hypothesis:

<https://github.com/marcoloco23/riemann-hypothesis>

Our first possible IEANTN contribution is a precise Riemann-Weil explicit formula for
ζ in a fixed normalization and test-function class. The repository contains a complete
written derivation, a hypothesis audit, and deterministic numerical regression checks.
It makes no novelty claim and remains `PROVED-WRITTEN` pending independent human review.

Would a `ZetaExplicitFormula.v1` node fit IEANTN best as `folklore` or as a reusable
`pipeline`? We would begin with a small conclusions interface and literature
justification, link a tagged repository snapshot, disclose substantial AI assistance,
and treat Lean formalization as follow-up work. If the full formula is too broad, which
prerequisite split would compose best with the existing zeta, logarithmic-derivative,
and zero-count nodes?

We also have a Davenport-Heilbronn signed-comb calibration, but we plan to compare its
exact statement with Zeta Lab's existing formal work before proposing it separately.

## Material to link

- [Claim index](../CLAIMS.md)
- [L8](../workspace/lemmas/L8-explicit-formula-crystalline-pair.md)
- [L8–L10 audit](../workspace/attempts/fourier-rigidity/AUDIT-2026-09-05.md)
- [Community integration research](../docs/08-community-integration.md)
- [Reproduction instructions](../REPRODUCIBILITY.md)

## Required disclosure

The research notes, derivations, tests, and repository preparation received substantial
assistance from AI coding and reasoning systems. The submitting human must understand
and approve the exact IEANTN diff, verify citations against the cited sources, and
describe the assistance in the pull-request body.
