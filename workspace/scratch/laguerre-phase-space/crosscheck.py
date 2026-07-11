"""Independent cross-checks tying the claims together, plus documentation of
a numerical pitfall found during verification.

(1) C_Xi(x,y) computed two ways:
      direct:  |Xi'(z)|^2 - Re(Xi(z) conj(Xi''(z)))   (claim-5 method)
      series:  sum_{n=1}^{7} n(2n-1) L_n[Xi](x) y^{2n-2}   (claims 1 + 4(i))
    at (x,y) = (5, 0.1) and (14.1347, 0.5); also the smallest grid value (25, 0.1).

(2) Lehmer point x=7005.063, y=0.05: three-way method comparison, and a
    demonstration that mpmath's diff(method='quad') is UNRELIABLE there
    (quadts's stopping rule is effectively absolute, so for |Xi| ~ 1e-2385 it
    accepts the coarsest quadrature level and returns radius-dependent junk
    with up to ~1e-2 relative error, identical across dps 30/45).
"""
import mpmath as mp
from common import Xi, Xi_derivs_real, cauchy_derivs, laguerre_Ln

mp.mp.dps = 40
print("=" * 72)
print("CROSS-CHECKS")
print("=" * 72)

print("\n[1] C_Xi direct vs series sum_(n>=1) n(2n-1) L_n y^(2n-2):")
for xs, ys in [('5', '0.1'), ('14.1347', '0.5'), ('25', '0.1')]:
    x, yv = mp.mpf(xs), mp.mpf(ys)
    z = mp.mpc(x, yv)
    X0, X1, X2 = cauchy_derivs(Xi, z, 2, 0.5, N=64)
    direct = abs(X1) ** 2 - (X0 * mp.conj(X2)).real
    d = Xi_derivs_real(x, 14, radius=1.5)
    series = sum(n * (2 * n - 1) * laguerre_Ln(d, n) * yv ** (2 * n - 2) for n in range(1, 8))
    rel = abs(direct - series) / abs(direct)
    print(f"    (x,y)=({xs},{ys}): direct = {mp.nstr(direct, 20)}")
    print(f"                    series = {mp.nstr(series, 20)}   rel.diff = {mp.nstr(rel, 3)}"
          f"   {'PASS' if rel < mp.mpf('1e-10') else 'CHECK (truncation?)'}")

print("\n[2] Lehmer point x=7005.063, y=0.05: method comparison")
mp.mp.dps = 45
z = mp.mpc(mp.mpf('7005.063'), mp.mpf('0.05'))


def C_from(X0, X1, X2):
    return abs(X1) ** 2 - (X0 * mp.conj(X2)).real


X0 = Xi(z)
h = mp.mpf('1e-8')
fp, fm = Xi(z + h), Xi(z - h)
cd = C_from(X0, (fp - fm) / (2 * h), (fp - 2 * X0 + fm) / h ** 2)
tr = {}
for r in ('0.02', '0.05'):
    d0, d1, d2 = cauchy_derivs(Xi, z, 2, mp.mpf(r), N=64)
    tr[r] = C_from(d0, d1, d2)
print(f"    central diff h=1e-8:            {mp.nstr(cd, 20)}")
for r, c in tr.items():
    print(f"    trapezoid Cauchy r={r}, N=64:  {mp.nstr(c, 20)}   "
          f"rel.diff vs central = {mp.nstr(abs(c - cd) / cd, 3)}")

print("\n    pitfall demo -- mpmath diff(method='quad') at the same point:")
for r in (0.005, 0.02, 0.05):
    X1q = mp.diff(Xi, z, 1, method='quad', radius=r)
    X2q = mp.diff(Xi, z, 2, method='quad', radius=r)
    cq = C_from(X0, X1q, X2q)
    print(f"      radius={r}: C = {mp.nstr(cq, 15)}   rel.err vs true = {mp.nstr(abs(cq - cd) / cd, 3)}")
print("    -> radius-dependent, dps-independent bias: do NOT use diff(method='quad')")
print("       for functions of tiny absolute magnitude. (Trapezoid rule instead.)")
