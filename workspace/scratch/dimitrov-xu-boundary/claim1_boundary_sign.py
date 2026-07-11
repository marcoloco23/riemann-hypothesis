"""Claim 1: B(t) = Re[xi(1+it) xi''(1+it) - xi'(1+it)^2] allegedly changes
sign near t ~ 110.3-110.5 (B(110) ~ +8.3383e-68, B(110.5) ~ -2.2846e-69,
B(111) ~ -5.8294e-69).

Method: analytic xi-derivatives (see common.py; validated against mp.diff),
computed via the cancellation-free form h^2 (A' zeta^2 + zeta zeta'' - zeta'^2)
with mpmath.zeta(s, derivative=k).  NO finite differencing of xi anywhere.
dps-invariance: every reported value computed at dps 130 AND dps 170; scan
sign changes re-confirmed at dps 170 (and dps 210 at the sign-change bracket).
"""
import mpmath as mp
import common as C


def B(t):
    return C.B_boundary(mp.mpf(t))


def xi_abs2(t):
    s = mp.mpc(1, t)
    return abs(C.xi(s)) ** 2


def main():
    ts = ['100', '105', '108', '109', '110', '110.25', '110.5', '111', '112', '115', '120']
    print("=== Claim 1: requested values at dps 130 and dps 170 ===")
    print(f"{'t':>8} {'B(t) dps130':>24} {'B(t) dps170':>24} {'rel diff':>10} {'B/|xi|^2 (norm)':>24}")
    for tstr in ts:
        mp.mp.dps = 130
        b130 = B(tstr)
        n130 = b130 / xi_abs2(mp.mpf(tstr))
        mp.mp.dps = 170
        b170 = B(tstr)
        rel = abs(b130 - b170) / abs(b170) if b170 != 0 else mp.inf
        print(f"{tstr:>8} {mp.nstr(b130, 12):>24} {mp.nstr(b170, 12):>24} {mp.nstr(rel, 3):>10} {mp.nstr(n130, 12):>24}")

    print()
    print("=== Scan B(t) on [50, 130], step 0.5, dps 130; record sign changes ===")
    mp.mp.dps = 130
    grid = [mp.mpf(50) + mp.mpf('0.5') * k for k in range(161)]
    vals = []
    for t in grid:
        vals.append(B(t))
    changes = []
    for i in range(len(grid) - 1):
        if vals[i] * vals[i + 1] < 0:
            changes.append((grid[i], grid[i + 1]))
    print("sign-change brackets:", [(mp.nstr(a, 6), mp.nstr(b, 6)) for a, b in changes])
    print("first few / last few scan values (t, B, B/|xi|^2):")
    for i in list(range(0, 4)) + list(range(118, 126)) + list(range(157, 161)):
        t = grid[i]
        print(f"  t={mp.nstr(t,6):>7}  B={mp.nstr(vals[i],10):>18}  norm={mp.nstr(vals[i]/xi_abs2(t),10):>18}")

    print()
    print("=== Bisection of each sign change (dps 130), re-verified at dps 170 & 210 ===")
    roots = []
    for a, b in changes:
        mp.mp.dps = 130
        r130 = mp.findroot(B, (a, b), solver='bisect', tol=mp.mpf(10) ** (-30))
        mp.mp.dps = 170
        r170 = mp.findroot(B, (a, b), solver='bisect', tol=mp.mpf(10) ** (-30))
        mp.mp.dps = 210
        sa, sb = mp.sign(B(a)), mp.sign(B(b))
        roots.append(r130)
        print(f"  bracket ({mp.nstr(a,6)},{mp.nstr(b,6)}): root dps130 = {mp.nstr(r130, 25)}")
        print(f"      root dps170 = {mp.nstr(r170, 25)}   |diff| = {mp.nstr(abs(r130-r170), 3)}")
        print(f"      signs at bracket ends re-checked at dps 210: ({sa}, {sb})")
    if roots:
        print(f"\nFIRST sign change of B on [50,130]: t* = {mp.nstr(roots[0], 20)}")
    else:
        print("\nNO sign change of B found on [50,130].")


if __name__ == '__main__':
    main()
