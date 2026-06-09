# 01 — Acceptance Criteria

**Read this twice.** This is the bar. A result that does not clear every applicable item
here is not a solution, regardless of how compelling it looks.

The Riemann Hypothesis has stood since 1859 and is a Clay Millennium Prize Problem. The
prior probability that any given argument is correct is very low. Accordingly the bar is
set for an adversarial reviewer who *assumes the argument is flawed* and looks for the
flaw. Your job is not to convince a friendly reader; it is to leave a hostile expert with
nothing to attack.

## A. What is being delivered

Exactly one of:

- **(P) A proof** that every non‑trivial zero of `ζ` has real part `1/2`, or
- **(D) A disproof** establishing the existence of a non‑trivial zero with real part `≠ 1/2`.

A correct **conditional** result (e.g. "RH follows from conjecture X") is **not** a
solution, but is a valuable partial result — record it in `workspace/` and label it
clearly as conditional. It does not satisfy these criteria.

## B. Hard requirements for a proof (all mandatory)

1. **Rigour, not evidence.** Numerical verification of zeros, statistical/random‑matrix
   agreement, "every equivalent formulation looks true", and physical heuristics are
   **not** proof. They may motivate but cannot conclude. (The first ~10^13 zeros are
   already known to be on the line; adding more proves nothing — see doc 04.)

2. **Completeness.** Every nontrivial inference is either (a) proved in full within this
   repository, or (b) cited to a specific, established, peer‑reviewed result stated
   precisely enough to be checked (theorem name + reference, see doc 04 / bibliography).
   No "it is well known that…" for non‑standard claims. No gaps marked "clearly".

3. **No circularity.** The argument must not assume RH, any statement equivalent to RH
   (see doc 03), or any open conjecture that implies RH. Audit every lemma for hidden
   assumption of the conclusion. This is the single most common failure mode.

4. **Valid analysis.** Every interchange of limit/sum/integral, every contour
   deformation, every analytic continuation, every application of the functional
   equation, every convergence claim must be justified with explicit hypotheses checked.
   Uniform convergence, absolute convergence, and the domain of validity of each identity
   must be tracked. (See doc 06 for the specific traps.)

5. **Litmus tests passed (mandatory).** The argument must be checked against the
   counterexample functions in [06-pitfalls-and-litmus-tests.md](06-pitfalls-and-litmus-tests.md),
   above all the **Davenport–Heilbronn function**, which satisfies a ζ‑like functional
   equation yet has zeros off the critical line. **If your method, applied verbatim, would
   also prove "RH" for Davenport–Heilbronn, the method is wrong.** A correct proof must
   use a property that ζ has and these functions lack (in practice: the Euler product /
   multiplicativity). State explicitly where that property is used and why it fails for the
   counterexamples.

6. **Self‑contained final write‑up.** A single document (`workspace/attempts/<name>/PROOF.md`)
   presenting the complete chain: statement → lemmas → main argument → conclusion, readable
   linearly by an expert without reconstructing missing steps.

## C. Strongly required: machine verification

7. **Formalization.** The definitions, the key lemmas, and ultimately the main theorem
   should be formalized in **Lean 4 + mathlib** and checked by the kernel (`formal/`).
   Mathlib already contains `ζ`, its analytic continuation, the functional equation, and
   substantial analytic number theory; build on it. Full formalization is the gold
   standard of acceptance. If full formalization is not yet reached, every non‑formalized
   step must be flagged in the verification checklist (doc 07) as carrying human‑review
   risk.

   > Formalization is *sufficient* for the mathematical correctness of what is formalized,
   > but only if the **statement** formalized is exactly the RH statement of doc 00 — guard
   > against a vacuous or mis‑stated theorem (a formal proof of the wrong proposition).
   > The statement itself must be reviewed against doc 00 by the protocol in doc 07.

## D. For a disproof

8. A claimed off‑line zero `ρ₀` must be established rigorously. A *numerical* near‑zero is
   not enough: floating‑point evaluation cannot prove `ζ(ρ₀) = 0`. Acceptable routes:
   (a) an exact/interval‑arithmetic argument with certified error bounds proving a zero
   exists in a region off the line (rigorous numerics, e.g. validated `arb`/ball
   arithmetic with a winding‑number / argument‑principle count), or (b) a non‑constructive
   existence proof. Note this would contradict the ~10^13 verified on‑line zeros only
   outside that range, so the height must be enormous or the argument structural — treat
   extreme skepticism as the default.

## E. Process requirements (so a result is trustworthy and reproducible)

9. **Provenance.** Every external fact used carries a citation. Maintain
   [references/bibliography.md](references/bibliography.md).
10. **Reproducible numerics.** Any computation is scripted, seeded, and re‑runnable from
    the repo; state the tool and version. Numerics never appear in the proof's logical
    chain (item 1) — only in motivation or in certified‑interval disproof arguments.
11. **Adversarial review survived.** Before announcing, the argument passes the
    verification protocol of [07-verification-protocol.md](07-verification-protocol.md),
    including independent re‑derivation of the load‑bearing lemmas and a dedicated
    "find‑the‑error" pass.
12. **Honest status.** `workspace/PROGRESS.md` always reflects true state: what is proved,
    what is conjectural, what is unchecked. Never upgrade "plausible" to "proved" in the
    log.

## F. Definition of done

> **Done** = a complete proof (B) of the doc‑00 theorem, formalized in Lean and
> kernel‑checked with a statement confirmed to match doc 00 (C), passing all litmus tests
> (B5) and the full verification protocol (doc 07), with every step either formalized or
> cited — **or** a rigorous disproof (D) meeting the same verification bar.

Anything short of this is **progress, not a solution**, and must be labelled as such.
