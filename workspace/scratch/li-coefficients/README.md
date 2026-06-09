# scratch/li-coefficients — numerics for `attempts/li-positivity`

**Tag: NUMERICAL.** Motivation and litmus grounding only (doc 01 B1/E10). Nothing here
enters any proof's logical chain.

## What and how

`li_coefficients.py` computes the Li coefficients `λ_n` (the Taylor coefficients of
`(d/dz) log ξ(1/(1−z))` at `0`, per the definition in
[`lemmas/L3`](../../lemmas/L3-li-converse-pringsheim.md)) for

1. the Riemann `ξ`, and
2. the completed **Davenport–Heilbronn** function `Ξ_f` (doc 06 LITMUS-1),

by trapezoidal Cauchy integrals for the Taylor coefficients of `h(z) = ξ(1/(1−z))` on
`|z| = 1/2` (exponentially accurate; the contour maps into a compact subset of
`{Re s > 1/2}` by lemma L1(4)), followed by exact power-series recursion for `h'/h`.

**Provenance:** Python 3.14.3, mpmath 1.3.0 (pinned in `requirements.txt`), dps = 60,
no randomness. Reproduce with:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python li_coefficients.py     # full output: run-output.txt (~50 s)
```

## Results (2026-06-09 run, `run-output.txt`)

- **Convention pinned:** computed `λ₁` agrees with the closed form
  `1 + γ/2 − ½log(4π)` to `1.8e−61`; independent differentiation route agrees for
  `n ∈ {1,2,3,5,8}` to `~1e−59`. So the `h'/h` Taylor definition used in L3 *is* the
  standard Li sequence (`λ₂ = 0.0923457352…` also matches the literature).
- **`λ_n(ζ) > 0` for `1 ≤ n ≤ 40`**, real to `1e−48`, ratio to the RH-conditional
  asymptote `(n/2)(log n + γ − 1 − log 2π)` decreasing toward `1` (1.067 at `n = 40`).
- **Davenport–Heilbronn (LITMUS-1):**
  - root-number identity `(1+iκ)/(1−iκ) = τ(χ)/(i√5)` verified to `1.1e−61` — the
    self-dual functional equation `Ξ_f(s) = Ξ_f(1−s)` is exact, and held numerically to
    `~1e−60` at test points;
  - the classical off-line zero refined to
    `ρ_f ≈ 0.80851718245663739 + 85.69934848537759217i` (`|f(ρ_f)| < 3e−60`),
    matching [Spira1968];
  - `|w(ρ_f)| = 0.999958…` puts the L3 negativity onset for `λ_n(f)` at
    `n ~ 3.5e5` (single-zero heuristic), consistent with `λ_n(f) > 0` for `n ≤ 40`:
    **the criterion's off-line signature is asymptotic, not low-`n`** — a useful
    calibration for what "numerically positive" is worth (nothing much; cf. Mertens,
    doc 03 §3);
  - `f(σ) ∈ [0.93, …]` on real `σ ∈ [1.05, 4)`: positive there *numerically*, but not
    structurally (signed coefficients) — the input `ζ(σ) > 1` of [L2] genuinely has no
    D–H analogue.

## Lesson learned (recorded so it isn't repeated)

A first version computed module-level constants (κ) **before** setting `mp.mp.dps`,
freezing them at 15 digits and producing a spurious `1e−17` functional-equation
"violation". Bisected via dps-60-vs-120 comparison; root-number identity isolated the
leak to κ. Moral for any future *certified* computation (doc 01 D): precision context
must be established before any constant is materialized, and every pipeline needs an
exact cross-check identity (here: `(1+iκ)/(1−iκ) = τ(χ)/(i√5)`).
