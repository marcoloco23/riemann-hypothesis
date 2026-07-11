"""Stage 2: cross-check the two independent implementations of Xi_N to 20 digits,
and verify the claimed alternative closed form for Phi_n with its constants.

(a) Xi_N closed form (incomplete gamma) vs direct u-integration, N in {1,2,3,4},
    at several complex z including large |Re z| and z in the strip.
(b) Claimed: Phi_n(z) = c1*(4 a_n - 1) e^{-a_n}
                      + (s(s-1)/2) * c2 * [a_n^{-s/2} Gamma(s/2, a_n)
                                          + a_n^{-(1-s)/2} Gamma((1-s)/2, a_n)]
    with a_n = pi n^2, s = 1/2 + iz.  Derivation (see xi_common.py docstring)
    gives c1 = c2 = 1/2.  Verify numerically: compute Phi_n by direct quadrature
    and solve/compare.
"""
from mpmath import mp, mpf, mpc, exp, pi, cos
from xi_common import Xi_N, Xi_N_direct, a_n, G, phi_n, I

mp.dps = 45  # target: agreement to >= 20 significant digits

print("=== Stage 2: cross-check closed form vs direct integration ===")
print(f"mp.dps = {mp.dps}")

test_z = [mpc(0, 0), mpf(2), mpc(14, 0), mpc(20, 3), mpc(50, mpf(1) / 4),
          mpc(100, mpf(45) / 100), mpc(150, 5), mpc(30, 10)]
worst = mpf(0)
for N in (1, 2, 3, 4):
    for z in test_z:
        v1 = Xi_N(z, N)
        v2 = Xi_N_direct(z, N)
        scale = max(abs(v1), abs(v2))
        rel = abs(v1 - v2) / scale if scale > 0 else mpf(0)
        note = ""
        if rel > mpf(10) ** -20:
            # |Xi_N(z)| is tiny; the direct oscillatory integral cancels from an
            # O(1) integrand, so raise precision until 20 digits are resolved.
            dps0 = mp.dps
            mp.dps = int(45 + max(0, -mp.log10(abs(v1))) + 10)
            v1 = Xi_N(z, N)
            v2 = Xi_N_direct(z, N)
            rel = abs(v1 - v2) / max(abs(v1), abs(v2))
            note = f"  [re-run at dps={mp.dps}]"
            mp.dps = dps0
        worst = max(worst, rel)
        print(f"  N={N} z={z}:  closed={mp.nstr(v1, 21)}  rel.diff={rel:.3e}{note}")
print(f"  WORST relative difference over all cases: {worst:.3e}"
      f"  ({'PASS >=20 digits' if worst < mpf(10) ** -20 else 'FAIL'})")

print()
print("Alternative closed form for Phi_n (claim: c1 = c2 = 1/2):")


def Phi_n_direct(z, n):
    U = mpf(3)
    nseg = int(max(20, 2 * abs(mp.re(z)))) + 1
    pts = [U * k / nseg for k in range(nseg + 1)]
    return mp.quad(lambda u: phi_n(u, n) * cos(z * u), pts)


def bracketA(n):
    return (4 * a_n(n) - 1) * exp(-a_n(n))


def bracketB(z, n):
    s = mpf(1) / 2 + I * z
    a = a_n(n)
    return s * (s - 1) / 2 * (G(s / 2, a) + G((1 - s) / 2, a))


# Solve for c1, c2 from two z-values (per n), then verify at a third.
for n in (1, 2, 3):
    z1, z2, z3 = mpc(1, mpf(1) / 5), mpc(7, 2), mpc(15, mpf(1) / 3)
    A = bracketA(n)
    rows = []
    for z in (z1, z2):
        rows.append((A, bracketB(z, n), Phi_n_direct(z, n)))
    # 2x2 solve: c1*A + c2*B_i = P_i  (A constant, B_i differ)
    (A1, B1, P1), (A2, B2, P2) = rows
    det = A1 * B2 - A2 * B1
    c1 = (P1 * B2 - P2 * B1) / det
    c2 = (A1 * P2 - A2 * P1) / det
    resid = abs(c1 * A + c2 * bracketB(z3, n) - Phi_n_direct(z3, n))
    print(f"  n={n}: c1 = {mp.nstr(c1, 25)}")
    print(f"        c2 = {mp.nstr(c2, 25)}")
    print(f"        |c1-1/2| = {abs(c1 - mpf(1) / 2):.3e}, "
          f"|c2-1/2| = {abs(c2 - mpf(1) / 2):.3e}, resid@z3 = {resid:.3e}")
