# scratch/pick-kernel — verification of the "Pick-kernel criterion" claims

**Tag: SYMBOLIC + NUMERICAL.** Claims 1–3 are verified *exactly* (sympy, rational
arithmetic); claims 4–6 are mpmath numerics (dps = 60), motivation/litmus only (doc 01
B1/E10) — nothing here is a proof of anything about ζ beyond exact algebraic identities.

Setting: `ξ(s) = ½s(s−1)π^(−s/2)Γ(s/2)ζ(s)`, `Q(x) = ξ'(½+x)/ξ(½+x)` for real `x > ½`,
Pick kernel `K(x,y) = (Q(x)+Q(y))/(x+y)`. Zero quartet: `α = ρ−½ = a+ib`, `c = α² = u+iv`.

## Provenance / reproduce

Python 3.13.11, mpmath 1.3.0 + sympy 1.14.0 (pinned in `requirements.txt`), dps = 60
(set in `common.py` **before** any constant — see the κ lesson in
`../li-coefficients/README.md`). All scripts deterministic (fixed seeds).

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
for f in claim1_quartet_algebra claim2_2x2 claim3_det3 claim6_prime_rep claim4_zeta_pick claim5_dh_litmus; do
  .venv/bin/python $f.py
done          # full output: run-output.txt (~40 s total)
```

## Scripts

- `common.py` — shared numerics: ξ, Q via the exact `Q_inf + ζ'/ζ` formula, an
  independent Cauchy-integral log-derivative, the Davenport–Heilbronn `f`, `ξ_f`
  (conventions copied from `../li-coefficients/`), Pick/quartet matrix builders,
  symmetric eigensolver wrapper.
- `claim1_quartet_algebra.py` — quartet contribution `Q_α = 4xA/(A²+B²)` derived from
  `d/dx log[(1−x²/α²)(1−x²/ᾱ²)]`; the identities for `Q_α ∓ xQ_α'`; positivity via the
  factorizations `A∓B = x²+(a∓b)²−2a²`; critical-pair (`a=0`) analogues. All exact.
- `claim2_2x2.py` — exact factorization
  `det·xy(x+y)² = (Q_y x − Q_x y)(Q_x x − Q_y y)`, sum of factors `= (Q_x+Q_y)(x−y)`,
  hence the claimed equivalence; 2000-sample exact-rational boolean cross-check.
- `claim3_det3.py` — `K_α = (Q_α(x)+Q_α(y))/(x+y)` exactly; the 3×3 determinant
  identity **fully symbolically** (polynomial difference expands to 0) plus 8 exact
  rational sample points; corrected phase analysis for the sign (see below).
- `claim4_zeta_pick.py` — ζ Pick matrices, N = 2..8, four point families in (½,10);
  `Q` cross-checked formula-vs-finite-difference at every point (≤ 1.6e−59).
- `claim5_dh_litmus.py` — the Davenport–Heilbronn litmus (LITMUS-1): functional
  equation, real-segment zero scan, Q_f validation (two independent routes),
  Spira zero refinement, Pick matrices for 11 patterns up to N = 20 and x ≤ 205,
  exhaustive 3-point search (2600 triples), quartet-vs-background diagnostics,
  dps-100 recheck of any negative candidate.
- `claim6_prime_rep.py` — structural identity `Q = Q_inf + ζ'/ζ(½+x)` (three
  independent routes, ~60 digits); prime-power sum with a **rigorous tail bound**
  (`Σ_{n>N} Λ(n)n^(−σ) ≤ N^(1−σ)[log N/(σ−1) + 1/(σ−1)²]`); `Q > 0` scan on (½,50].

## Verdicts (details in run-output.txt and PROGRESS notes)

1. **VERIFIED (exact)** — all five identities hold; positivity of both `Q_α ∓ xQ_α'`
   needs only `|a| < ½`, `|b| ≥ 14`, `x > 0`. **Consequence: −Q ≤ xQ' ≤ Q is
   UNCONDITIONAL** (true with off-line zeros too, since `0 < Re ρ < 1` and
   `|Im ρ| > 14` are known facts) — it carries **no RH content**. DH numerics agree:
   the same inequality holds for the RH-violating `Q_f` (11 026 pairs, 0 violations).
2. **VERIFIED (exact)** — the 2×2 equivalence is pure algebra given `Q > 0`;
   key factorization above. (By 1, it is also unconditional — content starts at 3×3.)
3. **VERIFIED (exact + sharpened)** — determinant identity confirmed fully
   symbolically. Sign claim confirmed, but the stated window `|v/u| < 0.072` is very
   conservative: the correct phase bound is `|arg| ≤ 2·arctan|v/u|` (the `|u|+iv` and
   `A_j−iv` phases *oppose*), so `Re(c̄Π(c−x_j²)) > 0` — hence det < 0 — for **all**
   `|v/u| < 1`; it genuinely fails just past 1 (numerically: flips between 1.0
   and 1.01 in the worst configuration).
4. **CONFIRMED [numerical]** — all ζ Pick matrices PSD; λ_min decays geometrically
   with N for clustered points (Cauchy-type conditioning, down to ~1.5e−42 at N=8)
   but stays positive, far above the ~1e−55 noise floor.
5. **NEGATIVE EIGENVALUE NOT FOUND [numerical litmus]** — DH: FE holds to ~1e−59;
   no real-segment zeros (Q_f pole-free and > 0 on the range used); the single-quartet
   kernel of the Spira zero (`c ≈ −7344.28 + 52.88i`, `|v/u| ≈ 0.0072`) is indefinite
   exactly as claim 3 predicts (every 3×3 det < 0, formula matches to 1e−53), yet the
   full `K_f` stayed PSD in every probed configuration. The best "deficit ratio"
   (background quadratic form ÷ quartet negativity, same direction) was ≈ 3.2e6,
   roughly scale-independent over x ∈ [30, 200]; two −1e−62-ish candidates re-checked
   **positive** at dps 100. So the off-line signature is buried ~6–7 orders below the
   on-line background in every direction tried — a structural gap, not a precision
   one. **Whether the DH Pick kernel is actually PSD (which would kill the converse
   'K PSD ⇒ RH') is NOT decided.** Until a DH negative eigenvalue is exhibited, the
   criterion FAILS the doc-06 LITMUS-1 gate in the operational sense: nothing in the
   verified algebra (claims 1–3 use only `|a|<½`, `|b|≥14`, `u<0`) distinguishes ζ
   from DH, and where ζ's Euler product/multiplicativity enters has not been shown.
6. **VERIFIED [numerical]** — `Q_inf` term-reconciliation is exact (`s = ½+x` ⇒
   `1/s = 1/(x+½)`, `ψ(s/2) = ψ(x/2+¼)`); identity to ~1e−61 at x = 1.5, 2.5, 5, 10;
   prime sum certified to ~26 digits at x = 5, ~11 at x = 2.5, only ~4–5 at x = 1.5
   (20+ digits at x = 1.5 would need N ~ 10^21 — infeasible by direct truncation;
   reported honestly). `Q > 0` on (½, 50], increasing, with infimum at the boundary:
   `Q(½⁺) = ξ'(1)/ξ(1) = 1 + γ/2 − ½log(4π) ≈ 0.0231` (matches closed form to 2.6e−61).

## Lesson learned (recorded)

A first version of the claim-5 point pattern "cluster at 85.7, spacing 30" generated
a point x = −4.3 < ½ (outside the domain), which silently produced `Q_f < 0` (Q_f is
odd) and a bogus "negative" diagnostic. Every point-set generator now asserts
`x > ½`. Moral: domain guards on generated test points, always.
