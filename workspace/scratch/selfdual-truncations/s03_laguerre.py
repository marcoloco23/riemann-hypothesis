"""s03: Laguerre inequality scan for Xi_N^sd, N = 1..6.

    L1[Xi_N](x) = Xi_N'(x)^2 - Xi_N(x) Xi_N''(x)

L1 >= 0 on R is necessary for Xi_N to be in the Laguerre-Polya class (only real
zeros); L1 < 0 flags nearby nonreal zeros.  Far-tail prediction: with
Xi_N(x) ~ -J_N/x^2 one gets L1 ~ -2 J_N^2 / x^6 < 0, so L1 MUST go negative
past the real-zero front; the question is where it first fails vs R_N.

Method: R_N by sign scan + bisection (step 0.25); L1 on [0, R_N + 80] step 0.25,
central differences with h = 10^{-dps/4} at x-adaptive dps
    dps(x) = 30 + 2*min(ceil(0.3413 x) + 2, digits(J_N) + 8)
(0.3413 = pi/(4 ln 10) matches the e^{-pi x/4} decay of Xi; J_N/x^2 is the
truncation floor).  Error budget: |err L1| ~ 10^{-dps/2} << |Xi(x)|^2-scale.
Sign changes bisected to 8 digits.  Every negative interval is reported.
"""
import time
from mpmath import mp, mpf, pi, log, ceil
import sd_common as sd

out = open("run-output.txt", "a", buffering=1)
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n")

P("=" * 78)
P("s03_laguerre.py --", time.strftime("%Y-%m-%d %H:%M:%S"))

with mp.workdps(140):
    DIGJ = {N: int(-mp.log(sd.J_closed(N), 10)) + 1 for N in range(1, 7)}
P("digits of cancellation floor J_N:", DIGJ)

def dps_for(x, N, mult):
    return 30 + mult * min(int(0.3413 * x) + 3, DIGJ[N] + 8)

def Xi_at(x, N):
    with mp.workdps(dps_for(x, N, 1)):
        return sd.Xi_sd_real(mpf(x), N)

def L1_at(x, N):
    d = dps_for(x, N, 2)
    with mp.workdps(d):
        x = mpf(x)
        h = mpf(10) ** (-(d // 4))
        fm = sd.Xi_sd_real(x - h, N)
        f0 = sd.Xi_sd_real(x, N)
        fp = sd.Xi_sd_real(x + h, N)
        d1 = (fp - fm) / (2 * h)
        d2 = (fp - 2 * f0 + fm) / (h * h)
        return d1 * d1 - f0 * d2, f0

def bisect(fun, a, b, fa_sign, tol=mpf("1e-8")):
    a, b = mpf(a), mpf(b)
    while b - a > tol:
        m = (a + b) / 2
        if (fun(m) > 0) == (fa_sign > 0):
            a = m
        else:
            b = m
    return (a + b) / 2

for N in range(1, 7):
    t0 = time.time()
    # ---- R_N by sign scan of Xi on [0, 4(N+1)^2 + 70] ----
    xmax_r = 4 * (N + 1) ** 2 + 70
    step = mpf("0.25")
    xs = mpf(0)
    prev = Xi_at(0, N)
    changes = []
    x = step
    while x <= xmax_r:
        cur = Xi_at(x, N)
        if (cur > 0) != (prev > 0):
            changes.append((x - step, x))
        prev = cur
        x += step
    R = bisect(lambda t: Xi_at(t, N), *changes[-1], fa_sign=(1 if Xi_at(changes[-1][0], N) > 0 else -1))
    with mp.workdps(60):
        J = sd.J_closed(N)
        tailchk = xmax_r * xmax_r * Xi_at(xmax_r, N) / (-J)
    P(f"\nN={N}: {len(changes)} real sign changes on [0,{xmax_r}], R_N = {mp.nstr(R, 14)} "
      f"(4(N+1)^2 = {4*(N+1)**2}); tail check x^2 Xi/(-J_N) at {xmax_r} = {mp.nstr(tailchk, 8)}")

    # ---- L1 scan on [0, R_N + 80] ----
    xmax = float(R) + 80
    xg = mpf(0)
    l1prev, _ = L1_at(0, N)
    neg_intervals = []
    cur_start = None if l1prev >= 0 else mpf(0)
    x = step
    nswitch = 0
    while x <= xmax:
        l1, _ = L1_at(x, N)
        if (l1 < 0) != (l1prev < 0):
            nswitch += 1
            xc = bisect(lambda t: L1_at(t, N)[0], x - step, x,
                        fa_sign=(1 if l1prev > 0 else -1))
            if l1 < 0:
                cur_start = xc
            else:
                neg_intervals.append((cur_start, xc))
                cur_start = None
        l1prev = l1
        x += step
    if cur_start is not None:
        neg_intervals.append((cur_start, None))
    P(f"  L1 scan [0, {mp.nstr(mpf(xmax),8)}] step 0.25: {nswitch} sign switches")
    if not neg_intervals:
        P("  L1 >= 0 on the whole scanned range")
    for (a, b) in neg_intervals:
        bs = mp.nstr(b, 12) if b is not None else f">= {mp.nstr(mpf(xmax),8)} (scan end; far tail L1<0 persists)"
        P(f"  L1 < 0 interval: [{mp.nstr(a, 12)}, {bs}]")
    first_neg = neg_intervals[0][0] if neg_intervals else None
    if first_neg is not None:
        P(f"  first L1<0 at x = {mp.nstr(first_neg, 12)};  R_N = {mp.nstr(R, 12)};  "
          f"first_neg - R_N = {mp.nstr(first_neg - R, 6)};  first_neg/4(N+1)^2 = {mp.nstr(first_neg/(4*(N+1)**2), 8)}")
    P(f"  ({time.time()-t0:.0f}s)")

P("\ns03 done.")
