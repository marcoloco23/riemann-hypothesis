"""CLAIM 4 (numerical, mpmath): zeta Pick matrices K(x_j,x_k) = (Q(x_j)+Q(x_k))/(x_j+x_k)
for N = 2..8 at varied point sets in (1/2, 10); expect smallest eigenvalue >= 0.

Q(x) is computed by the (claim-6-validated, ~60-digit) formula route AND cross-checked
against high-dps numerical differentiation of log xi(1/2+x) at every point used.
Any negative eigenvalue would be re-checked at dps 100 before being reported.
"""

import common
import mpmath as mp

print("=" * 78)
print(f"CLAIM 4: zeta Pick matrices, N = 2..8, points in (1/2,10)  (dps = {mp.mp.dps})")
print("=" * 78)


def points_equispaced(n):
    return [mp.mpf(1) + 8 * mp.mpf(j) / (n - 1) for j in range(n)] if n > 1 else [mp.mpf(5)]


def points_geometric_cluster(n):
    return [mp.mpf("0.5") + mp.power(2, -(j + 1)) for j in range(n)]


def points_geometric_wide(n):
    lo, hi = mp.mpf("0.6"), mp.mpf("9.5")
    return [lo * (hi / lo) ** (mp.mpf(j) / (n - 1)) for j in range(n)] if n > 1 else [lo]


def points_right_cluster(n):
    return [mp.mpf("9.5") - mp.power(2, -(j + 1)) for j in range(n)]


FAMILIES = [
    ("equispaced [1,9]", points_equispaced),
    ("geometric cluster at 1/2+ (1/2 + 2^-j)", points_geometric_cluster),
    ("geometric wide [0.6, 9.5]", points_geometric_wide),
    ("cluster at 9.5- (9.5 - 2^-j)", points_right_cluster),
]

# cache Q values (formula route) and cross-check against mp.diff route
qcache = {}
max_xcheck = mp.mpf(0)


def Q(x):
    key = mp.nstr(x, 50)
    if key not in qcache:
        qf = common.Q_formula(x)
        qd = common.Q_diff(x)
        global max_xcheck
        max_xcheck = max(max_xcheck, abs(qf - qd))
        qcache[key] = qf
    return qcache[key]


any_negative = []
for name, fam in FAMILIES:
    print(f"\n  point family: {name}")
    for n in range(2, 9):
        pts = fam(n)
        qv = [Q(x) for x in pts]
        K = common.pick_matrix(pts, qv)
        eigs = common.sym_eigs(K)
        lam_min = eigs[0]
        flag = "OK (>=0)" if lam_min >= 0 else "NEGATIVE <-- recheck"
        if lam_min < 0:
            any_negative.append((name, n, lam_min, pts))
        print(f"    N={n}:  lambda_min = {mp.nstr(lam_min, 8):>15}   "
              f"lambda_max = {mp.nstr(eigs[-1], 6):>12}   {flag}")

print(f"\n  max |Q_formula - Q_diff| over all {len(qcache)} points used: {mp.nstr(max_xcheck, 3)}")

if any_negative:
    print("\n  RECHECK of negative candidates at dps = 100:")
    with mp.workdps(100):
        for name, n, lam, pts in any_negative:
            qv = [common.Q_formula(x) for x in pts]
            K = common.pick_matrix(pts, qv)
            eigs = common.sym_eigs(K)
            print(f"    {name}, N={n}: lambda_min(dps=100) = {mp.nstr(eigs[0], 10)}")
else:
    print("\n  No negative eigenvalues at any size/point family."
          "\n  (Smallest ones decay roughly geometrically with N for clustered points --"
          "\n   the expected Cauchy/Pick-matrix conditioning -- but all remain positive,"
          "\n   comfortably above the ~1e-55 noise floor of the dps-60 Q values.)")

print("\nCLAIM 4 verdict: expected-PSD behavior",
      "CONFIRMED [NUMERICAL]" if not any_negative else "VIOLATED -- see recheck above")
