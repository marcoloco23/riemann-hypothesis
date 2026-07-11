# explicit-formula-check — numeric anchor for lemma L8a

**Purpose:** end-to-end sign/constant check of the Riemann–Weil explicit formula in
the exact L8 normalization (`lemmas/L8-explicit-formula-crystalline-pair.md` §2):

```
Σ_ρ ĝ(z_ρ) = ĝ(i/2)+ĝ(−i/2) − 2ΣΛ(n)n^{−1/2}g(log n)
             + (1/2π)∫ ĝ(t)[Re ψ₀(¼+it/2) − log π] dt .
```

Motivational only (docs/01 B1) — this is a bug-catcher for the derivation's signs and
constants (the Dimitrov–Xu affair, `../dimitrov-xu-boundary/dx-erratum/`, is exactly
why such checks are mandatory before enshrining an identity), not part of any proof.

## Files

- `check_ef.py` — two test functions against the first 1000 zero pairs:
  - **T1** `g = (1−(u/3)²)³·𝟙_{[−3,3]}` (all four terms active; prime comb through
    n = 20). `ĝ` in closed Bessel form `A√π·6·(2/Az)^{7/2}J_{7/2}(Az)` — do NOT
    compute ĝ by naive quadrature at large t (oscillatory; that error mode produced a
    +24 phantom in the archimedean term in the first run, since fixed).
  - **T2** `g = e^{−u²/2}` (zero sum ≈ 0; checks the pole/prime/archimedean balance
    as an exact cancellation).
- `run-output.txt` — results:
  - T1: LHS `6.98913e−5` vs RHS `6.98876e−5` (residual `3.7e−9`; the analytic
    zero-tail envelope gives `7.6e−10`, the rest is arch-integral truncation at
    t = 2000, consistent with `∫_{2000}^∞ t^{−4}log t`-size).
  - T2: RHS cancels to `5.4e−17` against LHS ≈ 0 — seventeen-digit confirmation of
    the constants `ĝ(±i/2)`, `−2Λ(n)n^{−1/2}`, `Re ψ₀(¼+it/2) − log π`.
- Deps: mpmath 1.3.0, python3, dps 25. Deterministic.

## Caveats

- Zero heights from `mp.zetazero` (first 1000), treated as real — numerically
  verified territory ([PlattTrudgian2021] far beyond), fine for a motivational check.
- T1's tail envelope uses the asymptotic `|J_{7/2}(x)| ≲ √(2/πx)`, not a certified
  bound.
