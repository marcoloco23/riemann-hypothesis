# theta-strip: numerical verification of finite theta truncations of Ξ

Skeptical numerical verification of claims about Haglund-style finite theta
approximants Ξ_N of the Riemann Ξ-function. **Numerics motivate; they prove
nothing.** All results below are floating-point evidence at the stated
precisions, over the stated finite regions only.

## Setup

```
python3 -m venv venv
./venv/bin/pip install -r requirements.txt   # mpmath==1.4.1
./venv/bin/python s01_normalization.py
./venv/bin/python s02_crosscheck.py
./venv/bin/python s03_claim1_zeros.py
./venv/bin/python s04_claim2_realzeros.py    # writes realzeros_N.txt used by s05
./venv/bin/python s05_claim3_strip.py        # slow part; args select N, e.g. "1 2"
./venv/bin/python s06_claim4_symmetry.py
./venv/bin/python s07_claim5_identity.py
```

All scripts are deterministic (mpmath, fixed dps ≥ 30, raised adaptively where
cancellation demands it). Full console output: `run-output.txt`.

## Pinned normalization (CORRECTION found here)

Ξ(z) := ξ(1/2 + iz), ξ(s) = (1/2)s(s−1)π^{−s/2}Γ(s/2)ζ(s).
With the task's atoms

    φ_n(u) = (2π²n⁴e^{9u/2} − 3πn²e^{5u/2}) e^{−πn² e^{2u}},   Φ = Σ_{n≥1} φ_n,

stage 1 shows numerically (42 digits, at z = 0, 2, 1+0.3i):

    2∫₀^∞ Φ(u)cos(zu)du = (1/2)·Ξ(z)      — factor 2 off.

The task's Φ is **half** of Titchmarsh §10.1's Φ (whose coefficients are
4π²n⁴ and 6πn²). Pinned:

    Ξ(z) = 4∫₀^∞ Φ(u)cos(zu)du,
    Ξ_N(z) := 4∫₀^∞ Σ_{n≤N} φ_n(u)cos(zu)du   (so Ξ_N → Ξ as N → ∞).

Zero locations are unaffected by the overall constant, so Haglund's zero
values need no rescaling.

## Validated closed forms (exact identities, verified to ≥ 20 digits)

Substitution w = πn²e^{2u} gives (verified, stage 2, worst rel. diff 7.9e−26
over N=1..4 and 8 z-values incl. |Re z| up to 150, after raising dps where
|Ξ_N| ~ 1e−31 causes cancellation in the *direct* integral):

    ∫₀^∞ e^{βu} e^{−πn²e^{2u}} e^{izu} du = (1/2)(πn²)^{−(β+iz)/2} Γ((β+iz)/2, πn²).

With a_n = πn², s = 1/2+iz, Γ(c+1,a) = cΓ(c,a) + a^c e^{−a}:

    Φ_n(z) := ∫₀^∞ φ_n(u)cos(zu)du
            = (1/4)(4a_n−1)e^{−a_n}
              + (s(s−1)/2)·(1/4)·[a_n^{−s/2}Γ(s/2,a_n) + a_n^{−(1−s)/2}Γ((1−s)/2,a_n)].

**The constants in the claimed alternative form are 1/4, NOT 1/2** (stage 2
solves for them numerically: 0.25 to 47 digits). The 1/2 would be correct for
Titchmarsh's Φ atoms (twice the task's).

Load-bearing identity (claim 5), in the pinned normalization — verified exact
(stage 7, constants recovered as 1 to 46 digits; residuals ≤ 1e−36 relative,
limited only by quadrature at the tiny-|Ξ_4| test point):

    Ξ_N(z) = C_N + (s(s−1)/2)·I_N(s),
    C_N = Σ_{n≤N} (4πn²−1)e^{−πn²},
    I_N(s) = ∫₁^∞ θ_N(u)(u^{s/2−1} + u^{(1−s)/2−1})du            (NO extra 1/2)
           = Σ_{n≤N} [a_n^{−s/2}Γ(s/2,a_n) + a_n^{−(1−s)/2}Γ((1−s)/2,a_n)],
    θ_N(u) = Σ_{n≤N} e^{−πn²u}.

C_N replaces the classical 1/2: C_N → 1/2 (C_3 already agrees to 19 digits;
analytically Σ(4πn²−1)e^{−πn²} = −ψ(1) − 4ψ'(1) = 1/2 by differentiating the
theta functional equation at u = 1 — but the finite-N identity itself is
derived WITHOUT the theta functional equation, only via the w-substitution
and the Γ recurrence, so it is exactly true for every N; numerics confirm).
In the task's 2∫ normalization both constants would be 1/2 instead of 1.

Consequence (why Ξ_N decays and is eventually negative): repeated integration
by parts of I_N gives Ξ_N(x) → C_N + θ_N(1) + 4θ_N'(1) + O(x^{−2}) on the real
axis, and C_N + θ_N(1) + 4θ_N'(1) = Σ(4πn²−1+1−4πn²)e^{−πn²} = 0 identically,
leaving Ξ_N(x) = O(x^{−2}).

## Claim-by-claim results

See run-output.txt for full numbers; summary in the final report of the
verification session. Scripts ↔ claims: s01/s02 = normalization & closed
forms, s03 = claim 1, s04 = claim 2, s05 = claim 3, s06 = claim 4,
s07 = claim 5.

## Honest coverage statement (claim 3)

The strip check Ξ_N ≠ 0 on 0 < Im z < 1/2 was established numerically ONLY on
Re z ∈ [−0.5, X_N], X_N = 1.5·4(N+1)² + 50 (74, 104, 146, 200 for N = 1..4),
via rectangles [x0,x1]×[0.02,0.48] (widths ≤ 35), closed by:
near-real boxes [x0,x1]×[−0.02,0.02] whose counts equal the number of real
zeros (excluding complex zeros with 0 < |Im| < 0.02, using conjugate
symmetry), an upper box ×[0.48,12.03] (covers the gap [0.48,0.5)), and a
reality-polish of every real zero from seed x_k + 0.01i. By evenness and
Ξ_N(−z̄) = conj Ξ_N(z) (claim 4), the first quadrant suffices. Nothing is
asserted for Re z > X_N or Im z > 12.03 beyond the (numerically observed,
not proved) x^{−2} tail behaviour.
