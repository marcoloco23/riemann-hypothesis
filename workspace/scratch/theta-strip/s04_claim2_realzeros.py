"""Stage 4 (Claim 2): real zeros of Xi_N, the largest real zero R_N, and the
tail behaviour Xi_N(x) ~ -d_N / x^2.

- Sign-change scan of Xi_N on the real axis, step 0.05, up to 1.5 * 4(N+1)^2,
  then a coarser scan (step 0.5) up to 1.5 * 4(N+1)^2 + 50 to confirm no
  further sign changes.  All sign changes polished with findroot (bisection
  seeds -> secant).
- Claimed: R_2 ~ 39.5325, R_3 ~ 65.0321, R_N ~ 4(N+1)^2.
- Tail: for N = 1, 2 evaluate x^2 * Xi_N(x) at x = 200, 400, 800; verify it
  approaches a (negative) constant -d_N.

Writes the polished real zeros to realzeros_N.txt for reuse by stage 5.
"""
from mpmath import mp, mpf
from xi_common import Xi_N_real

mp.dps = 40
print("=== Stage 4: claim 2, real zeros and tail sign ===")

all_zeros = {}
for N in (1, 2, 3, 4):
    bound1 = mpf(15) / 10 * 4 * (N + 1) ** 2
    bound2 = bound1 + 50
    step = mpf(5) / 100
    zeros = []
    x = mpf(0)
    fprev = Xi_N_real(x, N)
    while x < bound1:
        xn = x + step
        fnext = Xi_N_real(xn, N)
        if fprev * fnext < 0:
            r = mp.findroot(lambda t: Xi_N_real(t, N), (x, xn), solver="anderson",
                            tol=mpf(10) ** -60)
            zeros.append(r)
        x, fprev = xn, fnext
    # coarser confirmation scan beyond
    extra = []
    x = bound1
    fprev = Xi_N_real(x, N)
    while x < bound2:
        xn = x + mpf(1) / 2
        fnext = Xi_N_real(xn, N)
        if fprev * fnext < 0:
            extra.append((x, xn))
        x, fprev = xn, fnext
    all_zeros[N] = zeros
    print(f"N={N}: {len(zeros)} positive real zeros in (0, {float(bound1)}], "
          f"sign changes in ({float(bound1)}, {float(bound2)}]: {len(extra)}")
    print("   zeros:", ", ".join(mp.nstr(r, 12) for r in zeros))
    RN = zeros[-1]
    print(f"   R_{N} = {mp.nstr(RN, 15)},  4(N+1)^2 = {4 * (N + 1) ** 2},"
          f"  R_N/4(N+1)^2 = {mp.nstr(RN / (4 * (N + 1) ** 2), 8)}")
    with open(f"realzeros_{N}.txt", "w") as f:
        for r in zeros:
            f.write(mp.nstr(r, 35) + "\n")

print()
print("Claimed R_2 ~ 39.5325, R_3 ~ 65.0321:")
print(f"  R_2 = {mp.nstr(all_zeros[2][-1], 15)}")
print(f"  R_3 = {mp.nstr(all_zeros[3][-1], 15)}")

print()
print("Tail behaviour x^2 * Xi_N(x) at x = 200, 400, 800 (claim: -> -d_N < 0):")
for N in (1, 2):
    vals = []
    for x in (mpf(200), mpf(400), mpf(800)):
        v = Xi_N_real(x, N)
        vals.append(v)
        print(f"  N={N} x={int(x)}: Xi_N(x) = {mp.nstr(v, 12)},  x^2*Xi_N(x) = {mp.nstr(x * x * v, 12)}")
    print(f"  N={N}: ratio Xi(200)/Xi(400) = {mp.nstr(vals[0] / vals[1], 10)} (x^-2 predicts 4),"
          f" Xi(400)/Xi(800) = {mp.nstr(vals[1] / vals[2], 10)}")
