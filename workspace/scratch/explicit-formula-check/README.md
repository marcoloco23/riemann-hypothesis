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
  - T1: LHS `6.98913e−5` vs RHS `6.98876e−5` (residual `3.7e−9`; the heuristic
    zero-tail envelope gives `7.6e−10`, the rest is arch-integral truncation at
    t = 2000, consistent with `∫_{2000}^∞ t^{−4}log t`-size).
  - T2: RHS cancels to `5.4e−17` against LHS ≈ 0 — seventeen-digit confirmation of
    the constants `ĝ(±i/2)`, `−2Λ(n)n^{−1/2}`, `Re ψ₀(¼+it/2) − log π`.
- Deps: mpmath 1.3.0, python3, dps 25. Deterministic.

## Caveats

- T1's polynomial cutoff is C², not C_c^∞. It is a numerical normalization
  check in a wider test class, not a smooth test as previously described in
  some summary text. The new script below supplies a genuinely smooth test.

- Zero heights from `mp.zetazero` (first 1000), treated as real — numerically
  verified territory ([PlattTrudgian2021] far beyond), fine for a motivational check.
- T1's tail envelope uses the asymptotic `|J_{7/2}(x)| ≲ √(2/πx)`, not a certified
  bound.

## 2026-09-05 audit checks

`check_smooth_and_dh.py` adds the even C_c^∞ test
`g(u)=exp(1-1/(1-(u/3)²))cos(14u)` for `|u|<3`, zero elsewhere. Its
transform is evaluated with composite Gauss–Legendre quadrature; all four
explicit-formula terms are active. The archimedean term uses regularized (W),
whose Fourier-side normalization is checked separately by the older script.

The smooth test compares 40/80 zero pairs and doubles quadrature panels while
raising precision from 35 to 50 digits. The reference zero ordinates retain
their original 35-digit precision. Residual with 80 pairs: `9.6807134e-12`;
quadrature/precision stability: `2.7189649e-17`. The last 40 retained terms
have absolute sum `1.4672341e-8`; that is **not** a bound for the omitted tail.

The same script checks L9's exponential-test gamma evaluation and L10's
DH Gauss-sum identity, functional equation and exact coefficients b(3), b(6).
It also checks direct Fourier integration against polynomial logarithmic
derivatives for finite toy divisors containing a nonreal quartet, repeated
real atoms, and odd/even central multiplicity. These are tests of the
reconstruction identities, not examples satisfying S1–S3.
It prints to stdout and does not overwrite stored data. Commands from the
repository root:

```sh
python3 workspace/scratch/explicit-formula-check/check_ef.py
python3 workspace/scratch/explicit-formula-check/hostile_review_check.py
python3 workspace/scratch/explicit-formula-check/check_smooth_and_dh.py
```

For just the fast DH/resolvent calibration, pass `--calibration-only` to
the last script. Tested with Python 3.14.6, mpmath 1.3.0; deterministic.
The new script asserts numerical agreement, not a rigorous tail certificate.
Selected output is recorded in `audit-output-2026-09-05.txt`.

**Existing-script limitation reproduced:** `hostile_review_check.py` with
Gaussian a=4 has residual `-2.7619e-6`; its prime table ends at 200000 before
the Gaussian tail is negligible. The direct archimedean-vs-(W) comparisons
still agree to approximately 30 digits. Its final factor-two comparison is
a historical error diagnostic using a Gaussian concentrated near ±2,
not literally supported away from 0. Neither diagnostic is a certificate.
