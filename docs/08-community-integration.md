# Connecting this repository to Tao-led open collaboration

**Research date:** 2026-09-05  
**Audience:** Maintainers and prospective contributors to this repository

## Finding

The project that best matches the requested shared network is the **Integrated
Explicit Analytic Number Theory Network (IEANTN)**, led by Terence Tao and hosted
at [`teorth/IEANTN`](https://github.com/teorth/IEANTN). It records explicit
analytic-number-theory claims as a dependency graph and tracks the evidence for
each claim. A node may be supported by a Lean proof, a computation, or a literature
citation. Tao's launch post describes it as a collaborative formalization and
bound-propagation project, coordinated through GitHub and the Lean Zulip
`#PrimeNumberTheorem+` channel. The project also has institutional support through
IPAM. Sources: [IEANTN repository](https://github.com/teorth/IEANTN),
[Tao's launch post](https://terrytao.wordpress.com/2026/01/15/the-integrated-explicit-analytic-number-theory-network/),
[IPAM project page](https://www.ipam.ucla.edu/news-research/special-projects/integrated-explicit-analytic-number-theory-network/).

IEANTN is a good destination for **selected modular claims** from this repository.
It is not designed as a general notebook for every RH experiment. The durable
structure should therefore have two connected layers:

1. This repository becomes the open, complete research record: proofs, failed
   approaches, computations, audits, provenance, and reproducibility material.
2. Claims that fall within explicit analytic number theory are proposed as focused
   IEANTN nodes, with links back to the detailed record here.

This conclusion is partly an inference from IEANTN's current subject matter and
contribution format. Its maintainers should decide the final scope of any proposed
node.

## Which public projects fit

| Project | Current purpose | Fit for this repository |
|---|---|---|
| [IEANTN](https://github.com/teorth/IEANTN) | A graph of explicit analytic-number-theory claims, dependencies, and evidence; contributions arrive through pull requests and discussion on [Lean Zulip](https://leanprover.zulipchat.com/#narrow/channel/423402-PrimeNumberTheorem.2B). | **Best bridge.** Propose individual explicit-formula or zeta-analysis claims. |
| [PrimeNumberTheoremAnd (PNT+)](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) | The broader Lean formalization project from which IEANTN developed. | Useful formal foundation and community, especially for shared zeta infrastructure. |
| [Zeta Lab](https://github.com/teal-sea/zeta-lab) | A current public computational and formal workbench for zeta, with explicit formulas, negative controls, Davenport-Heilbronn work, Lean proofs, failures, and evidence grades. It is not Tao-led. | **Closest peer repository.** Compare results and coordinate to avoid duplicate work; do not assume it is a community home without asking its maintainer. |
| [Polymath15 / de Bruijn-Newman upper bound](https://github.com/km-git-acc/dbn_upper_bound) | A computational project for upper-bounding the de Bruijn-Newman constant. Tao's 2019 thread described itself as the presumably final Polymath15 thread. | Suitable only for a concrete new de Bruijn-Newman computation or bound. It is not a general RH repository. See [Tao's Polymath archive](https://terrytao.wordpress.com/category/question/polymath/). |
| [ANTEDB / expdb](https://github.com/teorth/expdb) | A database for analytic-number-theory exponents and derived bounds. | Potentially relevant only when a result improves or composes one of its supported bounds. |
| [General Polymath](https://polymathprojects.org/about/) | Infrastructure and norms for open, massively collaborative mathematics. | A later option for a sharply posed, parallelizable subproblem. A proposal framed as solving RH in full would be too broad; the [proposal discussion](https://mathoverflow.net/questions/219638/proposals-for-polymath-projects) favors concrete problems with a credible starting idea. |
| [Palomar](https://palomar-registry.org/) | A registry for immutable snapshots of externally hosted Lean-verified mathematics. | A future discovery and preservation route after this repository has a reproducible Lean build. It is not a substitute for peer review. See [Tao's announcement](https://terrytao.wordpress.com/2026/08/). |

## Contribution mechanics in IEANTN

IEANTN's [contribution guide](https://github.com/teorth/IEANTN/blob/main/CONTRIBUTING.md)
allows nodes based on papers, reusable pipelines, folklore, or computations. A new
node can begin with a literature justification or with no completed proof. Each node
separates its conclusions, proof challenge, and formalization metadata. Work is
claimed through the project's GitHub board, and ordinary pull requests carry the
changes.

AI assistance is allowed, but the pull-request author must disclose it and understand
the submitted diff. That policy matters here: every exported claim should identify
its human author or maintainer, its machine-assisted steps, its independent review
status, and the exact reproducible evidence.

## Fit of the current findings

| Local result | IEANTN fit | Recommended treatment |
|---|---|---|
| `L8a`, the Riemann-Weil explicit formula in the repository's chosen normalization and test class | **High** | First scope proposal. Frame it as a standard literature-backed `folklore` or reusable `pipeline` node, with no novelty claim. Ask whether IEANTN wants the full formula or smaller prerequisite nodes. |
| `L10`, the Davenport-Heilbronn completion and signed-comb explicit formula | **Medium, with overlap to check** | Zeta Lab already has a Palomar-registered Lean theorem on a Davenport-Heilbronn analytic domain and broader DH computation. Compare exact statements and normalizations first. L10's signed-comb explicit formula may still be complementary; propose it after L8a only if IEANTN maintainers want the comparison function. |
| `L8b`, `L8c`, and `L9`, the rigidity and singleton results | **Possible later** | Keep public here first. Obtain independent mathematical review before proposing them as network claims. L9 currently has same-agent adversarial review only. |
| The Dimitrov-Xu theorem correction and reproducible counterexample | **Different publication route first** | Prepare a concise erratum note and contact the authors and journal. Once there is a stable public correction, IEANTN can link it if the corrected claim supports an explicit-number-theory node. |
| Failed approaches, counterexamples, and numerical scripts | **Low as standalone IEANTN nodes** | Preserve them in this repository with stable links and releases. Link them from relevant network-node notes where they prevent a known error or validate a boundary case. |

The current IEANTN graph already covers zeta-function ingredients such as zero counts,
verified low zeros, zero-free regions, and logarithmic-derivative facts. During this
research, no existing node specifically named for the Riemann-Weil explicit formula or
the Davenport-Heilbronn explicit formula was found. That makes L8a a plausible gap,
but absence by keyword is not proof that the mathematics is absent under another node.
A short Zulip scope discussion should precede implementation.

Zeta Lab materially changes the surrounding landscape. Its public record says that its
Davenport-Heilbronn analytic theorem has already been registered with Palomar, and it
publishes an explicit-formula implementation plus structure-matched negative controls.
Its registered declaration is not described as the signed-comb formula proved in L10,
so direct statement comparison is required before drawing a novelty conclusion. See
[its Palomar surface](https://github.com/teal-sea/zeta-lab/blob/main/lean/PALOMAR.md).

## Publication readiness of this repository

The repository is organized as a public research record: it separates acceptance
criteria, lemmas, attempts, scratch computations, and a status log that explicitly says
RH remains unsolved. The local release candidate now includes a claim index, an
Apache-2.0 license, citation metadata, governance, issue forms, reproducibility CI,
machine-assistance disclosure, and prepared outreach. The remaining issues are
account-level or external:

1. A public GitHub lookup for `marcoloco23/riemann-hypothesis` returned `404` on
   2026-09-05. Outsiders therefore cannot currently rely on the configured origin as
   a public home; it may be private or absent at that address.
2. The release candidate must be committed and pushed after its third-party PDF is
   removed from reachable public history. The paper remains available through its
   authoritative arXiv link.
3. The GitHub repository still needs its public description, topics, labels,
   Discussions, merge settings, initial passing workflow, tag, and release.
4. The Lean project is not initialized. The prose and computations can be published
   now, but evidence levels must distinguish written proof, same-author audit,
   independent review, numerical check, and machine-checked proof.

The release audit scanned 316 current and historical blobs for common private-key,
credential, and token formats without finding a match. It also compiled every Python
source and checked every detected local Markdown link. This focused audit reduces the
risk of accidental publication but cannot prove that no sensitive information exists.

## Recommended community structure

Use a neutral GitHub organization if the intention is that the work outlive one
person's account. GitHub repository transfer preserves issues, pull requests, and
redirects; organization roles allow maintenance responsibility to be shared. Sources:
[transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository),
[organization repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).

The release candidate now provides:

- Apache-2.0 for the repository's original code, research records, and documentation,
  while cited third-party material keeps its own terms;
- `CONTRIBUTING.md`, including evidence labels and the rule that no unreviewed work is
  presented as an RH proof;
- `GOVERNANCE.md`, naming maintainers and explaining review and status changes;
- `CODE_OF_CONDUCT.md`, pull-request and issue templates, and GitHub Discussions;
- `CITATION.cff` so GitHub exposes citation metadata, following
  [GitHub's citation-file guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files);
- reproducibility CI for deterministic scripts and, once initialized, the Lean build;
- tagged archival releases connected to Zenodo for a DOI, following
  [Zenodo's GitHub integration guide](https://help.zenodo.org/docs/github/archive-software/github-upload/).

## Execution sequence

1. Create a clean public history without the bundled third-party PDF and commit the
   internally consistent release candidate using the maintainer's public GitHub identity.
2. Push it, make the GitHub repository public, apply the prepared settings, and wait for
   the verification workflow to pass.
3. Publish the `v0.1.0` tagged release and archive it with a DOI. This gives outside discussions
   stable references even while `main` continues to change.
4. Post the short IEANTN scope proposal below on the `#PrimeNumberTheorem+` Zulip
   channel. Incorporate maintainer feedback before writing a node.
5. Compare L8a and L10 line by line with Zeta Lab's explicit-formula and
   Davenport-Heilbronn surfaces, then submit one small IEANTN pull request for L8a,
   disclosing machine assistance and linking the exact repository release. Treat L10
   and the rigidity results as later, separate proposals.
6. Initialize Lean around the smallest reusable prerequisite selected with IEANTN.
   Reuse mathlib and PNT+ definitions instead of creating a parallel zeta foundation.

## Draft IEANTN scope proposal

> We maintain a reproducible, explicitly non-solution-claiming research repository on
> the Riemann hypothesis. Our first possible IEANTN contribution is a precise
> Riemann-Weil explicit formula for zeta in a fixed normalization and test-function
> class, with literature support, a complete written derivation, and numerical
> regression checks. Would a `ZetaExplicitFormula.v1` node fit best as `folklore` or as
> a reusable `pipeline`? We would start with a small conclusions interface and
> literature justification, link the stable source release, disclose AI assistance,
> and treat Lean formalization as follow-up work. We make no novelty or RH-solution
> claim. If the full formula is too broad, which prerequisite split would compose best
> with the existing zeta and zero-count nodes?

No issue, message, repository transfer, visibility change, or pull request was made as
part of this research. Those actions affect an external public project and should use
the reviewed snapshot and agreed authorship information.
