# Fourier-rigidity research cycle — completion record

**Completed: 2026-09-05.** This records execution of the plan selected in
the conversation: audit the foundation, test the relaxed class with converse
theorems, calibrate against DH, and decide the next direction. All three
work packages were performed in this cycle; the proposed “three sessions”
were an effort bound, not a requirement to invent separate dates or logs.

## Deliverables and evidence

| Agreed item | Completed work | Evidence |
|---|---|---|
| Recheck L8b, its cutoff and shifted-anchor argument | Rechecked each rate and tail condition; corrected the weighted space; supplied a separate resolvent derivation | [Audit](AUDIT-2026-09-05.md), L8 §4 |
| Correct the finite-defect corollary | Replaced “non-real member” with “distinct member”; retained the possibility RH is false | L8 §5 |
| Synchronize signs, distributions and research status | Corrected the negative comb and singular background terminology; archived the old roadmap without losing its body | [README](README.md), [roadmap](ROADMAP.md), L8 §3 |
| Keep S1–S3 unchanged | No axiom added; weaker count suffices for the resulting theorem | L8 §6, L9 statement |
| Match converse-theorem hypotheses | Recorded all reconstruction requirements; distinguished Booker positivity and missing A1 bounds from comb positivity | Audit hypothesis table |
| Reconstruct divisor, completion and Dirichlet series | Proved the weight estimate, exponential-test extension, product convergence, finite order, normalization and functional equation | [L9](../../lemmas/L9-positive-comb-singleton.md) §§1–4 |
| Deliver a structural result or precise obstruction | Written proof that the exact relaxed class is a singleton; also direct PNT asymptotics for its weights | L9 |
| Pin DH constants and coefficient signs | Derived the mod-5 odd completion, root-number identity, zero-free starting half-plane, explicit formula, negative b(3) and non-prime-power b(6) | [L10](../../lemmas/L10-davenport-heilbronn-explicit-formula.md) |
| Distinguish background and positivity exclusions | Proved an explicit background mismatch on the comb-free interval, independent of coefficient signs | L10 §4 |
| Reproduce old anchors and add a smooth compact test | Ran the existing scripts, added the actual C_c^∞ test and precision/quadrature doubling; documented the wide-Gaussian cutoff residual | [Numerical record](../../scratch/explicit-formula-check/audit-output-2026-09-05.txt) |
| Check circularity, domains, multiplicities and limiting steps | Written audit plus finite toy-divisor calibration with nonreal quartets, repeated atoms and both central parities | Audit; L9 §2; new calibration script |
| Choose the outcome branch | Singleton branch: retire the fixed-background counterexample hunt and fixed-data deformations; RH remains open | STATUS and roadmap |
| Update durable state | Updated the progress log, bibliography, lemma records and attempt documents | [Progress log](../../PROGRESS.md) |

## Verification performed

- Written derivation and same-agent adversarial audit of L9 and L10.
- Second analytic derivation of L8b using resolvents instead of Gaussian
  localization. “Separate derivation” does not mean a separate reviewer.
- Direct derivation of the weight PNT in L9 §1, independent of Hamburger.
- Numerical regressions, including the exact smooth test: residual about
  `9.7e-12` with 80 zero pairs and quadrature/precision stability `2.7e-17`.
- Python syntax, local document links, archived-roadmap preservation and
  whitespace checks. No certified infinite tails are claimed.

## Completion boundary

This cycle's result is a **written characterization proof**, not an RH proof.
Independent review and machine verification are distinct, higher evidence
levels and have not been completed. Lean setup was explicitly deferred in
the accepted plan. The roadmap's future independent-review gate concerns
using or publishing the new result; it is not an unfinished reconstruction
step or a claim that a second reviewer has already checked it.

The other four research approaches remain parked for this cycle. No successor
class, external outreach, publication, repository-management work or Lean
installation was added to this task. Concurrent community/governance changes
belong to their separate workflow.
