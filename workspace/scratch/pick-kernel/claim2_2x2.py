"""CLAIM 2 (symbolic, sympy): the 2x2 Pick-determinant equivalence.

Claim: for x > y > 1/2 and Q(x), Q(y) > 0,
    y/x <= Q(x)/Q(y) <= x/y
  <=>
    det [[Q(x)/x, K(x,y)], [K(x,y), Q(y)/y]] >= 0,   K(x,y) = (Q(x)+Q(y))/(x+y).

Method: treat Q(x), Q(y) as free positive symbols Qx, Qy (the equivalence is claimed
pointwise, i.e. as an algebraic statement about the four numbers x, y, Qx, Qy).

Key factorization (verified exactly):
    det * x*y*(x+y)^2 = (Qy*x - Qx*y) * (Qx*x - Qy*y)
Then:
    Qx/Qy <= x/y  <=>  Qy*x - Qx*y >= 0
    Qx/Qy >= y/x  <=>  Qx*x - Qy*y >= 0
so both inequalities => both factors >= 0 => det >= 0.
Converse: det >= 0 means the factors have equal sign (or one vanishes); both negative
is impossible since their SUM is (Qx+Qy)(x-y) > 0 for x > y, Qx,Qy > 0.  Hence
det >= 0 => both factors >= 0 => both inequalities.  Equivalence HOLDS.
"""

import sympy as sp

x, y, Qx, Qy = sp.symbols("x y Q_x Q_y", positive=True)

K = (Qx + Qy) / (x + y)
det = (Qx / x) * (Qy / y) - K**2

ok_all = True


def check(label, d):
    global ok_all
    d = sp.simplify(d)
    ok = (d == 0)
    ok_all = ok_all and ok
    print(f"  [{ 'PASS' if ok else 'FAIL' }] {label}: {d}")


print("=" * 78)
print("CLAIM 2: 2x2 determinant <=> two-sided ratio bound (exact sympy)")
print("=" * 78)

check("diagonal consistency K(x,x) = Q(x)/x",
      K.subs(y, x).subs(Qy, Qx) - Qx / x)

factored = (Qy * x - Qx * y) * (Qx * x - Qy * y)
check("det * xy(x+y)^2 = (Qy x - Qx y)(Qx x - Qy y)",
      sp.expand(det * x * y * (x + y) ** 2) - sp.expand(factored))

check("sum of factors = (Qx+Qy)(x-y)",
      sp.expand((Qy * x - Qx * y) + (Qx * x - Qy * y)) - sp.expand((Qx + Qy) * (x - y)))

print("""
  Logic (using the two verified identities, with x > y > 1/2, Qx, Qy > 0):
    (=>)  y/x <= Qx/Qy <= x/y  <=>  Qx*x - Qy*y >= 0  and  Qy*x - Qx*y >= 0
          => product >= 0 => det >= 0  (xy(x+y)^2 > 0).
    (<=)  det >= 0 => (Qy x - Qx y)(Qx x - Qy y) >= 0.  If both factors were < 0,
          their sum (Qx+Qy)(x-y) would be < 0, contradicting x > y, Q > 0.  So both
          are >= 0, giving y/x <= Qx/Qy <= x/y.
  EQUIVALENCE VERIFIED (it is a pure algebra fact about positive numbers; the only
  inputs used are Q(x), Q(y) > 0 and x > y > 0 - the value 1/2 is irrelevant).
""")

# Randomized sanity check of the equivalence as a boolean statement (exact rationals)
import fractions as fr
import random
random.seed(20260711)
mismatch = 0
for _ in range(2000):
    xv = fr.Fraction(random.randint(2, 400), random.randint(1, 40)) + fr.Fraction(1, 2)
    yv = fr.Fraction(random.randint(1, 399), random.randint(1, 40)) + fr.Fraction(1, 2)
    if xv == yv:
        continue
    if xv < yv:
        xv, yv = yv, xv
    qxv = fr.Fraction(random.randint(1, 500), random.randint(1, 100))
    qyv = fr.Fraction(random.randint(1, 500), random.randint(1, 100))
    ineq = (yv * qyv <= xv * qxv) and (yv * qxv <= xv * qyv)   # y/x <= qx/qy <= x/y
    detv = qxv * qyv / (xv * yv) - ((qxv + qyv) / (xv + yv)) ** 2
    if ineq != (detv >= 0):
        mismatch += 1
print(f"  exact-rational boolean check, 2000 random samples: mismatches = {mismatch}")
print()
print("CLAIM 2 overall:", "VERIFIED" if ok_all and mismatch == 0 else "FAILED")
