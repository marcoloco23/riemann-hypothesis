# Claim index

This index is the public entry point to the repository's mathematical status. It is
descriptive, not an additional source of proof; the linked files contain the exact
statements, assumptions, and arguments.

**Repository headline:** The Riemann hypothesis remains open. This repository contains
no claimed proof or disproof.

Evidence states follow [`CONTRIBUTING.md`](CONTRIBUTING.md). None of the written proofs
listed below has independent human review or Lean verification as of 2026-09-05.

| ID | Claim | State | Source and next review |
|---|---|---|---|
| RH | Every nontrivial zero of ζ has real part 1/2 | `CONJECTURED` | [Problem statement](docs/00-problem-statement.md); no solution claim. |
| L1 | Cayley-map geometry for the critical line | `PROVED-WRITTEN` | [L1](workspace/lemmas/L1-cayley-map-critical-line.md); independent review available. |
| L2 | ζ on the real axis and nonvanishing of ξ there | `PROVED-WRITTEN` | [L2](workspace/lemmas/L2-zeta-xi-real-axis.md); independent review available. |
| L3 | Eventual nonnegativity of Li coefficients implies RH | `PROVED-WRITTEN` | [L3](workspace/lemmas/L3-li-converse-pringsheim.md); review the Pringsheim step. |
| L4 | Two-sided logarithmic-derivative bound | `PROVED-WRITTEN` | [L4](workspace/lemmas/L4-logderiv-two-sided-bound.md); deliberately RH-empty and awaiting hostile review. |
| L5 | Theta representation with an effective truncation bound | `PROVED-WRITTEN` | [L5](workspace/lemmas/L5-theta-representation-effective-convergence.md); hostile review requested. |
| L6 | Pick-kernel criterion equivalent to RH | `PROVED-WRITTEN` | [L6](workspace/lemmas/L6-pick-kernel-criterion.md); pin and review the remaining textbook citation. |
| L8 | Riemann-Weil explicit formula, fixed-data uniqueness, and finite-defect rigidity | `PROVED-WRITTEN` | [L8](workspace/lemmas/L8-explicit-formula-crystalline-pair.md) and [audit](workspace/attempts/fourier-rigidity/AUDIT-2026-09-05.md); first candidate for IEANTN scoping. |
| L9 | Fixed-background positive-comb class is a singleton | `PROVED-WRITTEN` | [L9](workspace/lemmas/L9-positive-comb-singleton.md); independently review §§2–4 and the Hamburger theorem hypotheses. |
| L10 | Exact Davenport-Heilbronn completion and signed-comb explicit formula | `PROVED-WRITTEN` | [L10](workspace/lemmas/L10-davenport-heilbronn-explicit-formula.md); compare with Zeta Lab, then independently review. |
| DX-ERRATUM | The printed Dimitrov-Xu kernel statement contains a sign/factor error and has a corrected form | `PROVED-WRITTEN` + `NUMERICAL` | [Erratum record](workspace/scratch/dimitrov-xu-boundary/dx-erratum/README.md); prepare author/journal correspondence and external human review. |
| THETA-N3 | The third theta truncation has a reported off-axis zero near `67.8802+0.4773i` | `NUMERICAL` | [Computation record](workspace/scratch/theta-strip/STRIP-ZERO-N3.md); interval certification would be needed for a rigorous refutation. |

The complete activity and dependency record is in
[`workspace/PROGRESS.md`](workspace/PROGRESS.md). Failed approaches are retained under
[`workspace/scratch/`](workspace/scratch/) because reproducible negative results keep
future contributors from repeating known errors.
