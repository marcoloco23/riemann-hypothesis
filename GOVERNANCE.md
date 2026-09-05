# Governance

## Purpose

This is a community research record. Its maintainers preserve accurate mathematical
status, reproducibility, attribution, and a useful record of failed approaches. The
repository does not presently claim a proof or disproof of the Riemann hypothesis.

## Roles

- **Contributors** propose corrections, reviews, computations, formalizations, or new
  work through issues and pull requests.
- **Reviewers** evaluate a claim independently and document the scope and limits of
  their review. Authors cannot serve as the sole independent reviewer of their work.
- **Maintainers** merge changes, apply evidence states, protect releases, and enforce
  the contribution and conduct rules.

[`@marcoloco23`](https://github.com/marcoloco23) is the initial maintainer. Additional maintainers may be appointed after
sustained, constructive contributions and agreement from the existing maintainers.
The goal is shared stewardship rather than permanent control by one account.

## Decisions

Routine documentation, code, and reproduction changes require one maintainer review.
Adding or upgrading a mathematical result requires an independent mathematical review
whose scope is recorded in the repository. A status upgrade to `MACHINE-CHECKED`
requires a pinned, reproducible build of the exact advertised statement.

Material disagreements are recorded in the relevant claim file or issue. Maintainers
may merge a correction or downgrade immediately when a reproducible counterexample or
fatal proof gap is established. A disputed claim remains at the weaker evidence state
until the dispute is resolved.

No maintainer may announce an RH solution on behalf of the project unless all stages in
[`docs/07-verification-protocol.md`](docs/07-verification-protocol.md) have passed and
the public record contains the proof, review history, and remaining limitations.

## Machine assistance

Machine-assisted work is welcome when disclosed. The human submitter is responsible
for understanding the diff, checking citations against primary sources, reproducing
computations, and assigning the evidence state honestly. AI review does not count as
independent human review.

## Project continuity

Tagged releases are immutable research snapshots. If the initial maintainer becomes
inactive for six months, two established contributors may propose a stewardship
transfer in a public issue. Repository ownership should move to a neutral organization
when there are at least two active maintainers who can administer it.
