# 10 — External claim of a proof (Alpöge with Claude, 2026-11-20)

**Status of this page:** a dated record of public sources, read on 2026-11-21. It is not
a review of the mathematics. Nothing here was reproduced in this repository except the
small check in [L11](../workspace/lemmas/L11-smoothed-mangoldt-statistic.md). This
record was prepared with substantial machine assistance and has had no independent human
review.

## 1. What was announced

On 2026-11-20 Levent Alpöge (Anthropic) posted a four-page note, `alpo.ge/remark.pdf`,
stating that he believes he has found, working with Anthropic's Claude, a proof of the
Riemann hypothesis and of the generalized Riemann hypothesis, and that the argument is
formalized in Lean without assumptions. No written proof was released: the note says
the argument is very long, that the author does not yet command all of it, and that he
chose to publish only the Lean source (14 archive parts on the same site). A proper
write-up is promised.

The five theorems, as restated by the community in a file that imports only Mathlib
([`src/Challenge.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/main/src/Challenge.lean)):

| Theorem | Statement |
|---|---|
| `riemannHypothesis` | Mathlib's `RiemannHypothesis` |
| `riemannZeta_eq_zero_re` | the same, written out |
| `LFunction_ne_zero_of_half_lt_re` | `L(χ,s) ≠ 0` for `Re s > ½`, every modulus and Dirichlet character (trivial character at `s=1` excepted) |
| `LFunction_eq_zero_re` | every zero of `L(χ,s)` in `0 < Re s < 1` has `Re s = ½` |
| `LFunction_eq_zero_re_of_isPrimitive` | the same for primitive characters |

"GRH" here means Dirichlet L-functions. Dedekind zeta functions and other L-functions
are not covered; the note expects them to follow with more work.

## 2. Verification status (as of 2026-11-21, about 09:30 UTC)

Sources: A. Sutherland's page <https://math.mit.edu/~drew/grh/> and the notes in
<https://github.com/leanprover-community/riemann-hypothesis> (`verification/NOTES.md`).

- **Size.** 175,187 Lean files, about 17.4 million lines, no comments; Lean v4.33.1 and
  Mathlib tag v4.33.1.
- **Builds.** All modules compile with zero errors.
- **Axioms.** The five theorems depend only on `propext`, `Classical.choice`,
  `Quot.sound`. A text scan finds no `sorry`, `axiom`, `native_decide` or `unsafe`.
- **Kernels.** Every module replays through the Lean kernel (`leanchecker`). Two
  independently written kernels, nanoda and con-leche, accept the full exported proof
  (about 62 GB unpacked). lean4lean accepts every module; five needed a raised step
  limit.
- **Statement matching.** con-leche's compare mode confirms the five theorems against
  the Mathlib-only challenge file. The statements were also read by hand by the
  community checkers.
- **Still running at that time.** The `lake comparator` kernel stages and the
  single-threaded Lean default and paranoid kernel replays of the export.
- **A check that avoids Mathlib's zeta.** Combined with an independent formalization of
  Robin's and Lagarias's criteria, the proof yields Robin's inequality
  `σ(n) < e^γ n log log n` for all `n > 5040`, with the same three axioms.
- **Caveats stated by the checkers.** The source uses custom tactics that hand terms to
  the kernel unchecked by the elaborator, so the kernel is the only check for those
  proofs (the reason for the independent kernels). Lean v4.33.1 predates some runtime
  fixes; the judging therefore uses v4.36.0 and kernels not built on the Lean runtime.
  The first build ran unsandboxed on cloud machines.

What this does and does not establish: if the kernels and Mathlib's definitions are
sound, the formal statements are theorems. It does not give a human-readable proof, and
no mathematician has yet reported understanding the argument end to end.

## 3. Reactions reported in the press

Read in secondary reports only (Scientific American, IBM, Nature's news page was not
accessible): J. Maynard called it a historic milestone if it checks out and expects it
to be correct; Y. Lamzouri expects understanding to take months or years; A. Granville
criticized releasing it without a clear write-up; K. Buzzard's first question was
whether the Lean statement is the real hypothesis. These are press paraphrases and are
not verified against the speakers.

## 4. The strategy, as far as the note discloses it

The note gives one paragraph and a 20-item timeline, which it says was compiled by
Claude and is partly a paraphrase the author does not vouch for in detail. What can be
said with that caveat:

1. **Stepanov's method** proves RH for curves over finite fields by building an
   auxiliary function that vanishes to high *multiplicity* at the rational points and
   comparing degrees. Over the integers there is no derivative with which to define
   multiplicity. The note calls its argument a descendant of Stepanov's.
2. **Substitute for multiplicity:** a chain of theta lifts between totally definite
   unitary groups, `U(X₀) → U(X₁) → … → U(X_m)`, each lift said to gain one unit of
   multiplicity. For a von Mangoldt sum of length `X` the chain has length about `√X`;
   the note credits this choice to Claude.
3. **The statistic** is the smoothed sum
   `Σ_{n≤X} Λ(n)(X/n − 1) − X log X + (1+γ)X` (see [L11](../workspace/lemmas/L11-smoothed-mangoldt-statistic.md)).
4. **Positivity** enters as Weil-form inequalities `W(·) ≥ 0` for special test functions,
   obtained from determinants and read as "Stepanov with multiplicity one"; the note
   says an a-priori accounting of the cost of each lift stops at 2/3 and that further
   devices are needed beyond it.
5. **Other named ingredients:** Gan–Gross–Prasad and Bessel periods, the seesaw
   identity and Rallis inner product, a relative trace formula, Chowla–Selberg and
   Siegel mass formulas for divisibility, an Iwasawa tower in place of the constant-field
   extension, Bost's slope inequality, a weakened form of Vandiver's conjecture for
   classes that twisting does not remove, and a toy model over finite fields giving a
   sign-only proof of the Weil and Deligne bounds.

We cannot judge any of this from the note. It is recorded so that the repository's own
map of approaches can be compared with it.

**Predecessor.** Alpöge–Furman, arXiv:2608.13637 (August 2026): at least 2/3 of the
zeros are simple and on the line, unconditionally, by a finite compression of Weil's
Hermitian form, Sylvester's law of inertia for off-line pairs, and a rank–trace
inequality fed by the unconditional pair-correlation second moment; formalized in Lean;
the paper states the argument was found by Claude. Lamzouri, arXiv:2609.02882, gave a
shorter proof by one Hilbert-space inequality. That method is explicitly insensitive to
`o(N)` off-line zeros and holds for Davenport–Heilbronn, so it could not by itself reach
RH. See docs/04 §B.

## 5. Against this repository's own gates

| Gate | Reading on 2026-11-21 |
|---|---|
| docs/07 Stage 0, statement check | Passed by outside checkers: Mathlib's `RiemannHypothesis`, hand-read, plus the Robin cross-check. |
| docs/06 LITMUS-1/2 (Davenport–Heilbronn, Epstein) | The theorems are stated only for ζ and Dirichlet `L(χ,s)`, which have Euler products. The sketch is automorphic throughout. Where exactly the Euler product is used cannot be read off without a written proof. |
| docs/06 LITMUS-4 (`Λ ≥ 0`, no slack) | Not assessable without the proof. |
| docs/01 B (human-checkable rigour) | Not met: no written proof exists yet. |
| docs/01 C, docs/07 Stage 5 (machine verification) | Met externally to a higher standard than this repository has applied to anything of its own; not reproduced here (it needs roughly 100 GB of memory). |
| docs/07 Stage 4 (independent re-derivation) | Not met. |

## 6. Consequences for this repository

- The headline changes from "RH remains open" to "a machine-checked proof has been
  announced and is under community verification". This repository still contains no
  proof of its own, and `RH` stays `CONJECTURED` in `CLAIMS.md` with a pointer here
  until the outside verification concludes and a maintainer decides.
- docs/05 gains the Stepanov route, which it did not list, and a correction: the
  proportion-on-the-line results are no longer capped near 41.7%.
- If the proof stands, the repository's remaining value is its audited explicit-formula
  lemmas (L8–L11), the Davenport–Heilbronn controls, the Dimitrov–Xu erratum, and
  possibly help with reading the Lean development. Suggested next steps are in
  `workspace/PROGRESS.md`.

## Sources

- Announcement: <https://alpo.ge/remark.pdf> (read in full).
- Verification: <https://math.mit.edu/~drew/grh/>;
  <https://github.com/leanprover-community/riemann-hypothesis>.
- Predecessors: arXiv:2608.13637; arXiv:2609.02882.
- Press: Scientific American, IBM Think, World Science Festival (video description
  only), 2026-11-20/21.
