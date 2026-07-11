# selfdual-truncations: self-dual theta truncations of Ξ

**Numerics motivate; they prove nothing.** All results are floating-point
evidence at stated precisions over stated finite regions.

## Setup

```
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt   # mpmath==1.4.1
./venv/bin/python s00_pin.py         # pin H(y)
./venv/bin/python s01_closedform.py  # closed form + identity with one-sided family
./venv/bin/python s02_corner.py      # corner jump J_N, tail -J_N/x^2
./venv/bin/python s03_laguerre.py    # L1 scans N=1..6 (slowest, ~15 min)
./venv/bin/python s04_coshsinh.py    # cosh/sinh split identities
./venv/bin/python s05_p2const.py     # P2 tail constants N=1..8
```

Full console log: `run-output.txt` (appended incrementally).

## Pinned definitions (s00, verified to 44+ digits)

    H(y)  = 4y^2 Σ_{n≥1} (2π²n⁴y² − 3πn²) e^{−πn²y²}     (series, all y > 0)
    yH(y) = H(1/y)                                          (theta functional eq.)
    2ξ(s) = ∫₀^∞ y^{s−1} H(y) dy,  ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)

The task's H is exactly right (no constant fix needed). Self-dual truncation:

    H_N(y) = Σ_{n≤N} h_n(y)  (y ≥ 1),   H_N(y) = H_N(1/y)/y  (0 < y < 1),
    ξ_N^sd(s) = ½∫₀^∞ y^{s−1} H_N(y) dy,   Ξ_N^sd(z) = ξ_N^sd(½+iz).

Closed form (s ↔ 1−s manifestly symmetric; a = πn²):

    ξ_N^sd(s) = ½ Σ_{n≤N} [T_n(s) + T_n(1−s)],
    T_n(s)    = a^{−s/2} [ 4Γ(s/2+2, a) − 6Γ(s/2+1, a) ].

## MAIN FINDING (s01e): the self-dual family IS the one-sided family

    Ξ_N^sd(z) ≡ Ξ_N(z)   (theta-strip xi_common.py, same normalization),

verified to 61 digits (relative, dps 100) and exact by algebra: applying
Γ(c+1,a) = cΓ(c,a) + a^c e^{−a} twice collapses the symmetric closed form to
`C_N + (s(s−1)/2) I_N(s)`, which is theta-strip `Xi_N` verbatim.

Why it had to happen: in log coordinates u = log y, the Mellin integral is
½∫_ℝ e^{u/2}H_N(e^u)e^{izu}du, and the y→1/y gluing H_N(y):=H_N(1/y)/y is
exactly evenness of Φ_N^sd(u) := ½e^{u/2}H_N(e^u). The "one-sided" family
4∫₀^∞ Φ_N(u)cos(zu)du is the Fourier transform of the **even extension** of
Φ_N — the same function (Φ_N^sd = 2Φ_N on u ≥ 0). The strip zero of Ξ_3 at
z ≈ 67.880 + 0.477i is therefore inherited verbatim; there is no better/worse
family — there is one family, and it was already self-dual (its closed form
was s↔1−s symmetric all along).

## Corner at u = 0 (s02): NOT C¹ — no free lunch

    J_N := Φ'(0⁺) − Φ'(0⁻) = ½H_N(1) + H_N'(1)
         = −2π Σ_{n≤N} n²(8π²n⁴ − 30πn² + 15) e^{−πn²}
         = +2π Σ_{n>N} (same)          [theta identity ⇒ full sum = 0]
         ~ 16π³ (N+1)⁶ e^{−π(N+1)²} > 0.

J_1 ≈ 7.8998e−2, J_2 ≈ 1.6531e−7, J_3 ≈ 2.7835e−16, J_4 ≈ 5.7395e−28,
J_5 ≈ 1.7075e−42, J_6 ≈ 7.9623e−60. Same exponential order as the one-sided
defect d_N ≍ N⁶e^{−π(N+1)²}. Consequence (verified, ratio → 1 like 1 − c/x²):

    Ξ_N^sd(x) = −J_N/x² + O(x⁻⁴)  as x → +∞  (eventually strictly negative).

## Laguerre scans (s03), cosh/sinh split (s04), P2 constants (s05)

See run-output.txt. Headlines: L1[Ξ_N] = Ξ_N'² − Ξ_N Ξ_N'' ≥ 0 holds on the
whole bulk [0, R_N]; the first violation sits a few units PAST the largest
real zero R_N (front region), then a few negative windows (front-attached
complex zero pairs), then a final L1 < 0 tail (forced: Ξ ~ −J_N/x² gives
L1 ~ −2J_N²/x⁶ < 0). Scan step 0.25, endpoints bisected to 1e−8:

| N | #real zeros | R_N            | first L1<0    | first−R_N | permanent tail L1<0 from |
|---|------------|----------------|---------------|-----------|--------------------------|
| 1 | 1          | 14.0454395823  | 18.7861134224 | +4.74     | 27.5701912977            |
| 2 | 7          | 39.5324810781  | 42.7156971730 | +3.18     | 55.6487691812            |
| 3 | 15         | 65.0320737697  | 67.4332616888 | +2.40     | 101.181083318            |
| 4 | 31         | 103.367988009  | 105.164417911 | +1.80     | 157.673183527            |
| 5 | 53         | 149.002699491  | 151.003065247 | +2.00     | 226.758686516            |
| 6 | 79         | 197.957595576  | 200.932683233 | +2.98     | 308.422694127            |

(N=6 windows between first-neg and the permanent tail: see run-output.txt.)
The cosh/sinh split holds with the two-sided positive even weight
w_N^sd(u;r) = 2Φ_N^sd(u)cosh(ru) and tanh(ru) multiplier (s04, ≤1e−42 abs).
P2 constants (s05, exact symbolic atom derivatives, tail-route cross-checked):
d_N = J_N/4 (verified), K_N'''(0), M4_N → 161.89788029 (stabilizes by N=3),
T_N = sqrt((|K_N'''(0)|+M4_N)/d_N) = 90.6, 6.26e4, 1.53e9, 1.06e15, 1.95e22,
9.02e30, 1.03e41, 2.85e52 for N = 1..8.
