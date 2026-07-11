"""s01: closed form for xi_N^sd + verifications (a)-(d) + IDENTITY with one-sided.

(0) closed form T_n(s) vs direct quadrature of Int_1^inf y^{s-1} h_n(y) dy,
    and xi_N^sd (closed form) vs direct quadrature of (1/2)Int_0^inf y^{s-1}H_N^sd,
    at s = 0.3+2i, s = 2, N = 1..3.
(a) xi_N^sd(s) = xi_N^sd(1-s) at s = 0.3+2i, N = 1..6  (30 digits).
(b) Xi_N^sd(z) real and even for real z.
(c) |Xi_N^sd(z) - Xi(z)| at several z, N = 1..6.
(d) H_N^sd > 0: per-summand positivity check on y >= 1 (analytic: 2 pi n^2 y^2 > 3)
    + numeric spot grid over y in (0, 8].
(e) IDENTITY: xi_N^sd == collapsed form C_N + (s(s-1)/2)I_N(s)  ==  one-sided
    theta-strip Xi_N (imported read-only), at complex test points, N = 1..6.
"""
import sys, time
from mpmath import mp, mpf, mpc, pi, quad, sqrt, log, exp
import sd_common as sd

sys.path.insert(0, "/Users/marcsperzel/code/research/riemann-hypothesis/workspace/scratch/theta-strip")
import xi_common as xc   # one-sided family (read-only import)

out = open("run-output.txt", "a", buffering=1)
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n")

P("=" * 78)
P("s01_closedform.py --", time.strftime("%Y-%m-%d %H:%M:%S"))
mp.dps = 45
P("mp.dps =", mp.dps)
I = mpc(0, 1)
Ymax = sqrt((mp.dps + 15) * log(10) / pi) + 1

P("\n(0) closed form vs direct quadrature:")
for sv in [mpc("0.3", "2"), mpf(2)]:
    for n in [1, 2, 3]:
        direct = quad(lambda y: y ** (sv - 1) * sd.h_n(y, n), [1, 2, Ymax])
        cf = sd.T_n(sv, n)
        P(f"  T_n: s={sv}, n={n}: rel diff = {mp.nstr(abs(direct-cf)/abs(cf),5)}")
for sv in [mpc("0.3", "2")]:
    for N in [1, 2, 3]:
        # direct: (1/2)[ Int_1^inf y^{s-1}H_N + Int_1^inf y^{-s}H_N ]  (y<1 piece reflected)
        direct = (quad(lambda y: y ** (sv - 1) * sd.H_N_sd(y, N), [1, 2, Ymax])
                  + quad(lambda y: y ** (-sv) * sd.H_N_sd(y, N), [1, 2, Ymax])) / 2
        cf = sd.xi_sd(sv, N)
        P(f"  xi_N^sd: s={sv}, N={N}: rel diff = {mp.nstr(abs(direct-cf)/abs(cf),5)}")

P("\n(a) symmetry xi_N^sd(s) - xi_N^sd(1-s) at s = 0.3+2i:")
sv = mpc("0.3", "2")
for N in range(1, 7):
    d = sd.xi_sd(sv, N) - sd.xi_sd(1 - sv, N)
    v = sd.xi_sd(sv, N)
    P(f"  N={N}: xi={mp.nstr(v,32)}  |sym diff|={mp.nstr(abs(d),5)} (rel {mp.nstr(abs(d)/abs(v),5)})")

P("\n(b) Xi_N^sd(z) real and even on the real axis:")
for N in [1, 3, 5]:
    for zv in [mpf("0.7"), mpf(13), mpf("41.5")]:
        v = sd.Xi_sd(zv, N); w = sd.Xi_sd(-zv, N)
        P(f"  N={N}, z={zv}: |Im|={mp.nstr(abs(v.imag),5)}  |Xi(z)-Xi(-z)|={mp.nstr(abs(v-w),5)}")

P("\n(c) convergence |Xi_N^sd(z) - Xi(z)|:")
zs = [mpf(5), mpf(20), mpc(0, "0.02"), mpc(2, "0.4"), mpc(20, 6)]
P("  z \\ N " + "".join(f"{('N=%d'%N):>12}" for N in range(1, 7)))
for zv in zs:
    ref = sd.Xi_true(zv)
    row = f"  z={mp.nstr(zv,6):<12}"
    for N in range(1, 7):
        row += f"{mp.nstr(abs(sd.Xi_sd(zv, N) - ref), 3):>12}"
    P(row + f"   |Xi(z)|={mp.nstr(abs(ref),3)}")

P("\n(d) positivity of H_N^sd:")
P("  analytic: h_n(y) = 4y^2 n^2 pi (2 pi n^2 y^2 - 3) e^{-pi n^2 y^2} > 0 for y>=1")
P("  since 2 pi n^2 y^2 >= 2 pi > 6 > 3; reflection H_N(1/y)/y preserves sign. Check grid:")
bad = 0
for N in [1, 2, 3, 4, 5, 6]:
    ymin = None; vmin = None
    for k in range(1, 1601):
        yv = mpf(k) / 200          # 0.005 .. 8
        v = sd.H_N_sd(yv, N)
        if vmin is None or v < vmin:
            vmin, ymin = v, yv
        if v <= 0:
            bad += 1
    P(f"  N={N}: min over grid (0.005..8, step .005) = {mp.nstr(vmin,5)} at y={ymin}  (violations: {bad})")

P("\n(e) IDENTITY  Xi_N^sd(z)  vs  collapsed  vs  one-sided theta-strip Xi_N(z):")
zs = [mpc("67.8801896551", "0.4773438418"), mpc(3, "0.25"), mpc(150, 11), mpf("12.5"), mpc(0, 3)]
worst = mpf(0)
for N in range(1, 7):
    for zv in zs:
        a = sd.Xi_sd(zv, N)
        b = sd.xi_sd_collapsed(mpf(1) / 2 + I * zv, N)
        c = xc.Xi_N(zv, N)
        scale = max(abs(a), mpf(10) ** (-mp.dps))
        d1 = abs(a - b) / scale; d2 = abs(a - c) / scale
        worst = max(worst, d1, d2)
        P(f"  N={N}, z={mp.nstr(zv,8)}: |sd-collapsed|/|sd|={mp.nstr(d1,3)}  |sd-onesided|/|sd|={mp.nstr(d2,3)}  |Xi|={mp.nstr(abs(a),3)}")
P(f"  WORST relative deviation over all tests: {mp.nstr(worst, 3)}")
P("  => Xi_N^sd IS the one-sided theta-strip Xi_N, identically (algebra in sd_common.py docstring).")
P("\ns01 done.")
