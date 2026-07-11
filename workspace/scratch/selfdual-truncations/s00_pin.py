"""s00: pin the kernel H before anything else.

(1) theta functional equation  y H(y) = H(1/y)  at y = 1.3, 2.0  (target 30 digits)
(2) Mellin identity  2 xi(s) = Int_0^inf y^{s-1} H(y) dy  at s = 2, 3
    (H by the full series; integral split at y=1; tail truncated where
     e^{-pi y^2} < 10^-(dps+10)).
(3) term-wise complete-gamma Mellin:  Int_0^inf y^{s-1} h_n(y) dy
    = s(s-1) (pi n^2)^{-s/2} Gamma(s/2)  at s = 2, 3, 0.3+2i, n = 1, 2.
"""
import sys, time
from mpmath import mp, mpf, mpc, pi, gamma, quad, log, sqrt, exp
import sd_common as sd

out = open("run-output.txt", "a", buffering=1)
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n")

P("=" * 78)
P("s00_pin.py  --  pin H(y);", time.strftime("%Y-%m-%d %H:%M:%S"))
mp.dps = 45
P("mp.dps =", mp.dps)

# (1) functional equation
P("\n(1) y*H(y) - H(1/y)  (series both sides, full H):")
for yv in [mpf("1.3"), mpf(2)]:
    lhs = yv * sd.H_series(yv)
    rhs = sd.H_series(1 / yv, N=40)   # series at small argument needs many terms
    P(f"  y = {yv}:  yH(y) = {mp.nstr(lhs, 35)}")
    P(f"            H(1/y) = {mp.nstr(rhs, 35)}")
    P(f"            |diff| = {mp.nstr(abs(lhs - rhs), 5)}   rel = {mp.nstr(abs(lhs-rhs)/abs(lhs),5)}")

# (2) Mellin identity at s = 2, 3
P("\n(2) Int_0^inf y^{s-1} H(y) dy  vs  2 xi(s):")
Ymax = sqrt((mp.dps + 15) * log(10) / pi) + 1
for sv in [mpf(2), mpf(3)]:
    f = lambda y: y ** (sv - 1) * sd.H_series(y)
    val = quad(f, [0.05, 0.3, 1, 2, Ymax])
    # 0 < y < 0.05 tail: use reflection H(y) = H(1/y)/y, sub y->1/y:
    # Int_0^0.05 y^{s-1} H(y) dy = Int_{20}^inf y^{-s} H(y) dy  (doubly-exp small)
    tail = quad(lambda y: y ** (-sv) * sd.H_series(y), [20, 22])
    val += tail
    ref = 2 * sd.xi_true(sv)
    P(f"  s = {sv}:  integral = {mp.nstr(val, 32)}")
    P(f"           2 xi(s)  = {mp.nstr(ref, 32)}")
    P(f"           rel diff = {mp.nstr(abs(val - ref) / abs(ref), 5)}")

# (3) term-wise complete-gamma Mellin
P("\n(3) Int_0^inf y^{s-1} h_n(y) dy  vs  s(s-1)(pi n^2)^{-s/2} Gamma(s/2):")
for sv in [mpf(2), mpf(3), mpc("0.3", "2")]:
    for n in [1, 2]:
        f = lambda y: y ** (sv - 1) * sd.h_n(y, n)
        val = quad(f, [0, 0.5, 1, 2, Ymax / n + 1])
        ref = sv * (sv - 1) * (pi * n * n) ** (-sv / 2) * gamma(sv / 2)
        P(f"  s = {sv}, n = {n}:  rel diff = {mp.nstr(abs(val - ref) / abs(ref), 5)}")

P("\ns00 done.")
