# dimitrov-xu-boundary — verification of correlation-kernel claims

**Status: numerical verification/refutation of 5 claims. Numerics motivate, never prove.**
All headline numbers were recomputed at two (or three) precisions; "dps-stable" below
means the values agree to within the smaller working precision.

## Conventions (pinned)

- `xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`, `Xi(z) = xi(1/2+iz)`,
  `L(z) = Xi'(z)^2 - Xi(z)Xi''(z) = [xi xi'' - xi'^2](s=1/2+iz)`.
- Fourier transform: `fhat(x) = int_R f(u) e^{-ixu} du`.
- Classical kernel `Phi(u) = sum_n (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}`
  (u >= 0, even extension). **Pinned numerically** (sanity.py):
  `Xi(x) = 4 int_0^inf Phi(u) cos(xu) du` — same as the theta-strip convention note.
  Hence in OUR FT convention `Xi = FT[Phi_conv]` with `Phi_conv(u) = 2 Phi(|u|)`.
- xi-derivatives are computed **analytically** (no finite differences):
  with `h = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)`, `A = h'/h`, one gets the
  cancellation-free form `xi xi'' - xi'^2 = h^2 (A' zeta^2 + zeta zeta'' - zeta'^2)`
  using `mpmath.zeta(s, derivative=k)`. Validated against `mpmath.diff` of xi
  to ~1e-51 relative at dps 50 (sanity.py).

## Files

- `common.py` — xi/L machinery + kernel atoms; `sanity.py` — validation & convention pin.
- `claim1_boundary_sign.py`, `claim1b_fine_scan.py` — B(t) on the boundary line s=1+it.
- `claim2_structural.py` — L = (1/4) FT[C] identity (Gaussian + Riemann kernels), C>0, C''(0)<0.
- `claim3_cosh.py` — cosh-shift identity (Gaussian test kernel).
- `claim4_packets.py` — divisor-packet positivity kill test (atoms n=1..6).
- `claim5_interior.py` — interior lines sigma=1-delta and real axis.
- `diagnostics_zeros.py` — explains the negativity window via the close zero pair.
- `run-output.txt` — concatenated deterministic output of all scripts.

Reproduce: `python3 -m venv venv && ./venv/bin/pip install -r requirements.txt`,
then run each script with `./venv/bin/python`.

## Verdicts

### Claim 1 (headline sign change of B on Re s = 1): **VERIFIED**
`B(t) = Re[xi xi'' - xi'^2](1+it)` matches all three claimed values
(B(110)=+8.33828e-68, B(110.5)=-2.28461e-69, B(111)=-5.82941e-69; dps 130 = dps 170
to ~1e-129 relative). On [50,130] B has exactly one negative window:
**(110.45825828206558322, 111.47863638025211626)**, endpoints dps-stable
(130/170 bisection roots identical to 25 digits; bracket signs re-checked at dps 210).
Normalized `B/|xi(1+it)|^2` is O(1) (min ≈ -1.81 at t≈111.125), so this is a genuine
sign change, not underflow noise. A step-0.125 normalized scan finds no other
negative points on [50,130].

### Claim 2 (structural identity L = (1/4) FT[C]): **VERIFIED**
Analytically exact for the Gaussian test kernel (both sides = (pi/2)e^{-x^2/2});
numerically 0 rel. diff at 35 dps for x in {0.7, 2.1} with C computed by inner
quadrature. Riemann kernel spot check at x=5 (dps 50, nested double integral,
Phi_conv = 2 Phi): see run-output.txt for the achieved agreement.
C(p) > 0 at p in {0,1,3} and C''(0) < 0 (Richardson central differences) — see below.
NOTE: the identity requires the Jacobian factor 2 from (p,q)->(u,v); the notes'
sketch `FT[C_{m,n}] = -g_m''g_n - g_m g_n'' + 2g_m'g_n'` is off by that factor 2
(harmless for positivity questions, fatal for calibrated constants).

### Claim 3 (cosh-shift identity): **VERIFIED**, constant c = 4
`FT[cosh(yt) nu2](x) = (1/2)[nu2hat(x+iy) + nu2hat(x-iy)] = 4 Re L(x+iy)`
verified to 35 digits at (x,y) = (1.3, 0.35) for the Gaussian kernel.
(First equality is elementary; second uses nu2 real even + nu2hat = 4 L.)

### Claim 4 (divisor-packet positivity, notes §7): **REFUTED for every k tested**
`FT[C^(k)](x)` goes negative for all k in {1,2,3,4,6} (scan [0,60], step 0.25,
dps 45, 8x48-node Gauss-Legendre; first crossings bisected):

| k | first sign crossing x* | first negative grid pt (value) | grid min (location) | # neg grid pts / 241 |
|---|---|---|---|---|
| 1 | 18.7861134228 | x=19.0 (-1.66e-9) | -3.6746e-9 (x=19.75) | 148 |
| 2 | 5.22271481951 | x=5.25 (-2.42e-8) | -1.3958e-6 (x=8.5)   | 65  |
| 3 | 4.84367691943 | x=5.0  (-5.36e-14)| -6.1469e-13 (x=8.25) | 66  |
| 4 | 26.356571929  | x=26.5 (-8.02e-14)| -1.4028e-12 (x=33.0) | 135 |
| 6 | 21.0335336198 | x=21.25(-1.85e-19)| -2.7710e-18 (x=29.0) | 156 |

All five grid minima re-verified at dps 70 with 16 panels: values agree to the
printed 10 digits (claim4b_stability.py). Validation suite passed: fixed-node
g_1 vs adaptive quad (0 / 1.3e-42 rel), packet formula vs direct kink-aware
nested double integral at (1,1), x=3 (8.6e-32 rel; this also pins the Jacobian
factor 2), sum_n g_n = Xi/2 (0 rel).

Structural reason (predicted before the scan, confirmed by it):
the atom-level even extension phi~_n(u)=phi_n(|u|) has a corner at 0 with slope
phi_n'(0+) = e^{-pi n^2}(-4 pi^3 n^6 + 15 pi^2 n^4 - (15/2) pi n^2) != 0
(+0.019749383 for n=1, -0.019749341 for n=2, negative for all n>=2), so each g_n
has an algebraic ~ c_n/x^2 tail (c_n = -2 phi_n'(0+)) instead of exponential decay,
giving FT[C^(k)] ~ (2/x^6) sum_{mn=k} (-4 c_m c_n) at large x — negative for k=1
(-8 c_1^2/x^6 ~ -0.0125/x^6, consistent with the observed k=1 tail). The corner
slopes cancel only in the FULL sum Phi (Phi'(0+)=0 by modularity — note the
near-perfect n=1 vs n=2 cancellation above), never inside a single divisor packet
containing n=1. The section-7 grouping proposal is therefore dead as stated: any
regrouping whose packets have nonzero net corner slope inherits a negative
algebraic tail, and even beyond the tail the packets are negative on large parts
of [0,60] (65-156 of 241 grid points).

### Claim 5 (interior lines): expectation **REFUTED — the sign change PERSISTS**
(but this does NOT threaten RH; it kills the notes' implication instead):
- delta=0.05 (sigma=0.95): R(111) = -3.3479e-69 < 0, normalized min -1.30. **dps-200 confirmed.**
- delta=0.10 (sigma=0.90): R(111) = -9.7293e-70 < 0, normalized min -0.51. **dps-200 confirmed.**
- delta=0.20 (sigma=0.80): no negative values on [100,120]; min normalized +0.80.
- Dip depth decreases monotonically with delta (a2 table): -1.81, -1.77, -1.72, -1.50, -0.84
  for delta = 0, .01, .02, .05, .1 — smooth continuation, no artifact signature.
- Real axis: U(0,y) > 0 for all tested y in [0, 0.49] (values ~ +0.0114, slowly increasing).

**Diagnosis (diagnostics_zeros.py):** the negative window (110.458, 111.479) brackets
the close zero pair gamma_34 = 111.02954, gamma_35 = 111.87466 (gap 0.845, right after
the large gap 3.86 from gamma_33 = 107.16861). Using the Hadamard form
`L(z) = Xi(z)^2 sum_rho 1/(z-rho)^2`, the two nearest-pair terms alone give
Re ~ -5.0e-69 vs the true Re L(111.1 - i/2) = -4.49e-69; all other zeros contribute
small positive corrections. Since Re[1/(z-gamma)^2] < 0 whenever |t-gamma| < y
(z = t - iy), **Re L < 0 near close zero pairs is forced even if RH is true.**
Conclusion: any claimed implication "RH => Re L >= 0 on horizontal lines 0 < y <= 1/2"
is false as stated (close pairs — Lehmer-type regions — are counterexamples), so the
persistence found here does not disprove RH; it refutes that step of the notes.
The same mechanism explains the claim-1 boundary sign change (y = 1/2 line).

## Numerical-stability summary

- Claim 1/5 quantities: computed at dps 130 vs 170 (agreement ~1e-129 rel.);
  sign-change roots identical to 25 digits across dps; negatives re-confirmed at
  dps 200/210. Magnitudes ~1e-68 are far above mpmath's exponent limits; the
  normalized O(1) companions rule out cancellation artifacts.
- Claim 2/3: adaptive quadrature at dps 35-50 with double-exponentially decaying
  integrands, cutoffs chosen so truncation < 1e-40.
- Claim 4: composite Gauss-Legendre (8 panels x 48 nodes on [0,4]); panel error
  ~6e-42 for the worst oscillation cos(60u); fixed-node g_1 validated against
  adaptive mp.quad at x=3 and x=60; packet formula validated against a direct
  nested double integral at (1,1), x=3; sum_n g_n cross-checked against Xi/2.
