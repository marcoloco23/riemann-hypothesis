"""s02: corner of Phi_N^sd at u = 0 and its Fourier consequence.

Phi_N^sd(u) = (1/2) e^{u/2} H_N^sd(e^u), even by construction, and
Xi_N^sd(z) = Int_R Phi_N^sd(u) e^{izu} du = 2 Int_0^inf Phi_N^sd(u) cos(zu) du
(normalization verified in s01 via the closed form; re-verified here at z=2, N=2).

Corner jump  J_N = Phi'(0+) - Phi'(0-) = 2 Phi'(0+) = (1/2)H_N(1) + H_N'(1).
Three routes:
  (A) finite-sum closed form: J_N = -2 pi sum_{n<=N} n^2 (8 pi^2 n^4 - 30 pi n^2 + 15) e^{-pi n^2}
      [cancellation route; dps 120]
  (B) tail form (uses theta functional eq. sum_{n>=1} = 0):
      J_N = +2 pi sum_{n>N} n^2 (8 pi^2 n^4 - 30 pi n^2 + 15) e^{-pi n^2}
      [no cancellation; agreement with (A) also re-verifies the theta identity]
  (C) one-sided numeric derivative of Phi at 0+ (Richardson), resolves N <= 3.
Comparison scale: one-sided defect d_N = N^6 e^{-pi(N+1)^2}, and the leading
model 16 pi^3 (N+1)^6 e^{-pi(N+1)^2}.

Consequence: Xi_N^sd(x) = -J_N/x^2 + O(x^-4)  as x -> +inf.
Verified at x = 200, 400 (N = 1, 2): tabulate x^2 Xi_N(x) / (-J_N).
"""
import time
from mpmath import mp, mpf, mpc, pi, exp, quad, cos
import sd_common as sd

out = open("run-output.txt", "a", buffering=1)
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n")

P("=" * 78)
P("s02_corner.py --", time.strftime("%Y-%m-%d %H:%M:%S"))

mp.dps = 40
P("\nPhi even + Fourier normalization spot checks (dps 40):")
for uv in [mpf("0.37"), mpf("1.1")]:
    d = sd.Phi_sd(uv, 3) - sd.Phi_sd(-uv, 3)
    P(f"  N=3, u={uv}: |Phi(u)-Phi(-u)| = {mp.nstr(abs(d),4)}")
val = 2 * quad(lambda u: sd.Phi_sd(u, 2) * cos(2 * u), [0, 1, 3])
P(f"  N=2: 2 Int_0^3 Phi cos(2u) du = {mp.nstr(val, 25)}")
P(f"       Xi_2^sd(2) closed form  = {mp.nstr(sd.Xi_sd(mpf(2), 2), 25)}")

mp.dps = 120
P("\nJ_N table (dps 120):  [d_N = N^6 e^{-pi(N+1)^2},  model = 16 pi^3 (N+1)^6 e^{-pi(N+1)^2}]")
def term(n):
    return -2 * pi * n * n * (8 * pi * pi * n ** 4 - 30 * pi * n * n + 15) * exp(-pi * n * n)
P(f"{'N':>3} {'J_N (A: finite sum)':>28} {'J_N (B: tail)':>28} {'B/A - 1':>12} {'d_N':>12} {'model/J_N':>12}")
for N in range(1, 7):
    JA = sum(term(n) for n in range(1, N + 1))
    JB = -sum(term(n) for n in range(N + 1, N + 60))
    dN = mpf(N) ** 6 * exp(-pi * (N + 1) ** 2)
    model = 16 * pi ** 3 * (N + 1) ** 6 * exp(-pi * (N + 1) ** 2)
    P(f"{N:>3} {mp.nstr(JA, 20):>28} {mp.nstr(JB, 20):>28} {mp.nstr(JB/JA - 1, 4):>12} {mp.nstr(dN, 4):>12} {mp.nstr(model/JA, 4):>12}")
P("  (B/A - 1 ~ 0 confirms both routes AND the theta identity sum_{n>=1} = 0;")
P("   J_N > 0 for every N: the gluing is C^0 but NOT C^1 -- no free lunch;")
P("   J_N ~ 16 pi^3 (N+1)^6 e^{-pi(N+1)^2}: same exponential order as the")
P("   one-sided defect d_N = N^6 e^{-pi(N+1)^2}, ratio J_N/d_N -> 16 pi^3 e^{stuff} poly.)")

P("\n(C) numeric one-sided derivative check, J_N = 2 Phi'(0+):")
mp.dps = 60
for N in [1, 2, 3]:
    h = mpf(10) ** (-15)
    p0 = sd.Phi_sd(mpf(0), N)
    d1 = (4 * sd.Phi_sd(h, N) - sd.Phi_sd(2 * h, N) - 3 * p0) / (2 * h)
    Jnum = 2 * d1
    Jcf = sd.J_closed(N)
    P(f"  N={N}: J numeric = {mp.nstr(Jnum, 18)}   closed = {mp.nstr(Jcf, 18)}   rel diff = {mp.nstr(abs(Jnum-Jcf)/abs(Jcf), 3)}")

P("\nTail asymptotics  x^2 Xi_N^sd(x) / (-J_N)  (should -> 1):")
mp.dps = 60
for N in [1, 2]:
    JN = sd.J_closed(N)
    for x in [mpf(200), mpf(400), mpf(800)]:
        v = sd.Xi_sd_real(x, N)
        P(f"  N={N}, x={int(x)}: Xi = {mp.nstr(v, 12)}   x^2 Xi/(-J_N) = {mp.nstr(x*x*v/(-JN), 12)}")
P("  (sign: Xi_N^sd(x) < 0 for large x since J_N > 0.)")
P("\ns02 done.")
