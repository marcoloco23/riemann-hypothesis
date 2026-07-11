"""Claim 1: |f(x+iy)|^2 = sum_{n>=0} L_n[f](x) y^{2n} for real entire f,
L_n[f](x) = (1/(2n)!) sum_{j=0}^{2n} (-1)^{j+n} C(2n,j) f^(j)(x) f^(2n-j)(x).

Part A: symbolic check with sympy, generic f, through order y^6.
Part B: numeric check for f = Xi at (x,y) = (2, 0.3) and (14, 0.2),
        partial sum n <= 6 vs |Xi(x+iy)|^2.
"""
import sympy as sp
import mpmath as mp
from common import Xi, Xi_derivs_real, laguerre_Ln

print("=" * 72)
print("CLAIM 1 -- |f(x+iy)|^2 = sum_n L_n[f](x) y^{2n}")
print("=" * 72)

# ---------------- Part A: symbolic ----------------
print("\n[A] Symbolic (sympy), generic real-entire f, orders y^0..y^6")
y = sp.symbols('y', real=True)
f = sp.symbols('f0:13', real=True)  # f[k] stands for f^(k)(x), real

# f(x +/- i y) = sum_k (+/- i y)^k f^(k)(x)/k!, truncated at k=6:
# the product's coefficients of y^m are then EXACT for m <= 6.
K = 7
A = sum((sp.I * y) ** k * f[k] / sp.factorial(k) for k in range(K))
B = sum((-sp.I * y) ** k * f[k] / sp.factorial(k) for k in range(K))
P = sp.expand(A * B)  # = f(x+iy) * conj(f(x+iy)) = |f(x+iy)|^2 (f real entire)


def L_sym(n):
    return sp.expand(sp.Rational(1, sp.factorial(2 * n)) *
                     sum((-1) ** (j + n) * sp.binomial(2 * n, j) * f[j] * f[2 * n - j]
                         for j in range(2 * n + 1)))


ok = True
for m in range(7):
    c = sp.expand(P.coeff(y, m))
    if m % 2 == 1:
        good = (c == 0)
        print(f"  coeff of y^{m}: {'0 as required' if good else 'NONZERO: ' + str(c)}")
    else:
        n = m // 2
        diff = sp.simplify(c - L_sym(n))
        good = (diff == 0)
        print(f"  coeff of y^{m} vs L_{n}[f]: {'MATCH' if good else 'MISMATCH: ' + str(diff)}")
    ok = ok and good
print(f"  [A] symbolic result: {'PASS' if ok else 'FAIL'}")
print(f"  (sanity) L_1 = {L_sym(1)}   [expect f1**2 - f0*f2]")

# ---------------- Part B: numeric for Xi ----------------
print("\n[B] Numeric for f = Xi, partial sums n <= 6, dps = 40")
mp.mp.dps = 40
for (x, ystr) in [(2, '0.3'), (14, '0.2')]:
    yv = mp.mpf(ystr)
    derivs = Xi_derivs_real(x, 12, radius=1.5)
    # check roundoff on derivatives: recompute order 12 with a different radius
    d12b = Xi_derivs_real(x, 12, radius=2.0)[12]
    rel12 = abs(d12b - derivs[12]) / abs(derivs[12])
    Ls = [laguerre_Ln(derivs, n) for n in range(7)]
    partial = sum(Ls[n] * yv ** (2 * n) for n in range(7))
    z = mp.mpc(x, yv)
    exact = abs(Xi(z)) ** 2
    err = abs(partial - exact)
    # size of first omitted term (n=7) as truncation estimate
    derivs14 = Xi_derivs_real(x, 14, radius=1.5)
    tail = abs(laguerre_Ln(derivs14, 7)) * yv ** 14
    print(f"  (x,y)=({x},{ystr}):")
    print(f"    |Xi(x+iy)|^2          = {mp.nstr(exact, 25)}")
    print(f"    sum_(n<=6) L_n y^(2n) = {mp.nstr(partial, 25)}")
    print(f"    |difference|          = {mp.nstr(err, 5)}")
    print(f"    |first omitted term|  = {mp.nstr(tail, 5)}   (n=7)")
    print(f"    rel. agreement        = {mp.nstr(err / exact, 5)}")
    print(f"    deriv x-check (order 12, radius 1.5 vs 2.0), rel diff = {mp.nstr(rel12, 3)}")
    print(f"    -> {'PASS' if err / exact < mp.mpf('1e-20') or err <= 10*tail else 'FAIL'}")
