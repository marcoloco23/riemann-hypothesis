# Publication checklist

This checklist separates local readiness from account-level publication actions.

## Completed in the release candidate

- [x] Prominent statement that RH is not solved.
- [x] Public claim index with evidence and review states.
- [x] Apache-2.0 license, notice, and citation metadata.
- [x] Contribution, governance, conduct, and security policies.
- [x] Review, correction, reproduction, and proposal issue forms.
- [x] Pull-request checklist with machine-assistance disclosure.
- [x] Reproduction entry point and GitHub Actions workflow.
- [x] Current-tree and Git-history secret-format scan.
- [x] Local Markdown-link validation.
- [x] Third-party paper removed from the release tree and replaced with its source link.
- [x] Draft IEANTN and Dimitrov–Xu correspondence.

## Account-level publication

- [x] Use the maintainer's existing public GitHub identity in citation and notice files.
- [x] Commit the complete release candidate on `main`.
- [x] Remove the third-party PDF from public Git history or publish a clean squashed
  history; retaining it in reachable history defeats its removal from the release tree.
- [ ] Push the cleaned history to GitHub.
- [ ] Make the repository public and apply the description, topics, labels, Discussions,
  and merge settings in `scripts/configure_github.sh`.
- [ ] Wait for the `Verify` workflow to pass on GitHub.
- [ ] Create signed or annotated tag `v0.1.0` and the GitHub release from
  `docs/releases/v0.1.0.md`.
- [ ] Connect the repository to Zenodo and archive the release for a DOI.
- [ ] Post `outreach/IEANTN-PROPOSAL.md` after checking the public links.
- [ ] Send the Dimitrov–Xu note privately after checking the tagged reproduction.

## Later community hardening

- [ ] Add at least one independent human reviewer for L9 §§2–4.
- [ ] Move ownership to a neutral organization after a second active maintainer joins.
- [ ] Protect `main` with required pull-request and passing-CI rules once the initial
  workflow has completed.
- [ ] Initialize the Lean project around the smallest claim selected with IEANTN.
