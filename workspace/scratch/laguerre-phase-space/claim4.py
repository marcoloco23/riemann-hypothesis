"""Claim 4: phase-space identity for C_f(z) := |f'(z)|^2 - Re( f(z) conj(f''(z)) ),
where f(z) = int psi(u) e^{izu} du, psi even positive rapidly decreasing, and
W(p,x) := int_R psi((p+q)/2) psi((p-q)/2) cos(xq) dq.

(i)  C_f(x+iy) = (1/2) d^2/dy^2 |f(x+iy)|^2  -- symbolic, via y-Taylor series.
(ii) candidate identities:
       (A)  C_f = (1/2) int_0^inf p^2 cosh(p y) W(p,x) dp
       (B)  C_f = (1/4) int_R    p^2 e^{-p y}  W(p,x) dp
     Gaussian test psi(u)=e^{-u^2}  =>  f(z) = sqrt(pi) e^{-z^2/4}, checked to
     ~20 digits at (x,y) in {(0.5,0.3), (2,1), (3,0.2)}.
"""
import sympy as sp
import mpmath as mp

print("=" * 72)
print("CLAIM 4 -- C_f and the Wigner-type representation")
print("=" * 72)

# ---------------- (i) symbolic ----------------
print("\n[i] Symbolic: C_f(x+iy) vs (1/2) d^2/dy^2 |f(x+iy)|^2, through y^6")
y = sp.symbols('y', real=True)
f = sp.symbols('f0:16', real=True)  # f[k] = f^(k)(x), real (f real entire)
K = 9  # truncation: C and |f|^2 coefficients exact for y^m, m <= 8, hence
       # d^2/dy^2 |f|^2 coefficients exact for m <= 6 (needs |f|^2 at y^{m+2})


def ser(d, sign):
    """Taylor series of f^(d)(x + sign*i*y) in y, truncated at y^(K-1)."""
    return sum((sign * sp.I * y) ** k * f[k + d] / sp.factorial(k) for k in range(K))


# f real entire => conj(f^(d)(x+iy)) = f^(d)(x-iy) for real x,y.
# |f'|^2 = f'(z) f'(zbar);  Re(f(z) conj(f''(z))) = [f(z)f''(zbar) + f(zbar)f''(z)]/2
C = sp.expand(ser(1, +1) * ser(1, -1)
              - (ser(0, +1) * ser(2, -1) + ser(0, -1) * ser(2, +1)) / 2)

absf2 = sp.expand(ser(0, +1) * ser(0, -1))
half_dyy = sp.expand(sp.diff(absf2, y, 2) / 2)


def L_sym(nn):
    return sp.expand(sp.Rational(1, sp.factorial(2 * nn)) *
                     sum((-1) ** (j + nn) * sp.binomial(2 * nn, j) * f[j] * f[2 * nn - j]
                         for j in range(2 * nn + 1)))


ok = True
for m in range(7):  # coefficients of y^0..y^6 (exact given truncation K=7)
    cC = sp.expand(C.coeff(y, m))
    cD = sp.expand(half_dyy.coeff(y, m))
    d1 = sp.simplify(cC - cD)
    if m % 2 == 1:
        good = (cC == 0 and cD == 0)
        print(f"    y^{m}: both coefficients zero? {'PASS' if good else 'FAIL'}")
    else:
        nn = m // 2 + 1
        target = sp.expand(nn * (2 * nn - 1) * L_sym(nn))  # n(2n-1) L_n y^{2n-2}
        d2 = sp.simplify(cC - target)
        good = (d1 == 0 and d2 == 0)
        print(f"    y^{m}: C_f == (1/2)|f|^2_yy coeff? {d1 == 0};  == {nn}*(2*{nn}-1)*L_{nn}? {d2 == 0}"
              f"   {'PASS' if good else 'FAIL'}")
    ok = ok and good
print(f"    n=1 term of C_f (coeff of y^0) = {sp.expand(C.coeff(y, 0))}   [expect L_1 = f1**2 - f0*f2]")
print(f"  [i] result: {'PASS -- C_f = (1/2) d_y^2 |f|^2 = sum_(n>=1) n(2n-1) L_n y^(2n-2)' if ok else 'FAIL'}")

# ---------------- (ii) Gaussian test ----------------
print("\n[ii] Gaussian test psi(u) = e^{-u^2}, f(z) = sqrt(pi) e^{-z^2/4}, dps = 30")
mp.mp.dps = 30
PLIM = mp.mpf('60')  # e^{-p^2/2} * cosh(2p) negligible beyond ~ p=40 at dps 30
QLIM = mp.mpf('12')


def psi(w):
    return mp.exp(-w ** 2)


def W(p, xv):
    return mp.quad(lambda q: psi((p + q) / 2) * psi((p - q) / 2) * mp.cos(xv * q), [-QLIM, 0, QLIM])


def C_direct(xv, yv):
    z = mp.mpc(xv, yv)
    F = mp.sqrt(mp.pi) * mp.exp(-z ** 2 / 4)
    F1 = -z / 2 * F
    F2 = (-mp.mpf(1) / 2 + z ** 2 / 4) * F
    return abs(F1) ** 2 - (F * mp.conj(F2)).real


for (xv, yv) in [(mp.mpf('0.5'), mp.mpf('0.3')), (mp.mpf(2), mp.mpf(1)), (mp.mpf(3), mp.mpf('0.2'))]:
    lhs = C_direct(xv, yv)
    rhsA = mp.quad(lambda p: p ** 2 * mp.cosh(p * yv) * W(p, xv), [0, 5, PLIM]) / 2
    rhsB = mp.quad(lambda p: p ** 2 * mp.exp(-p * yv) * W(p, xv), [-PLIM, -5, 0, 5, PLIM]) / 4
    relA = abs(rhsA - lhs) / abs(lhs)
    relB = abs(rhsB - lhs) / abs(lhs)
    print(f"    (x,y)=({mp.nstr(xv, 3)},{mp.nstr(yv, 3)}):")
    print(f"      C_f direct                          = {mp.nstr(lhs, 22)}")
    print(f"      (1/2) int_0^inf p^2 cosh(py) W dp   = {mp.nstr(rhsA, 22)}   rel.diff {mp.nstr(relA, 3)}")
    print(f"      (1/4) int_R     p^2 e^(-py)  W dp   = {mp.nstr(rhsB, 22)}   rel.diff {mp.nstr(relB, 3)}")
    print(f"      {'PASS (both)' if max(relA, relB) < mp.mpf('1e-20') else 'CHECK'}")

print("""
[ii] analysis (proved by hand, confirmed above): substituting f(z)=int psi e^{izu}du,
  C_f(x,y) = (1/2) iint (u+v)^2 psi(u)psi(v) cos(x(u-v)) e^{-y(u+v)} du dv.
  With p=u+v, q=u-v (du dv = dp dq / 2) this is exactly
  (B):  C_f = (1/4) int_R p^2 e^{-py} W(p,x) dp.
  Since psi is even, W(-p,x) = W(p,x), so folding p -> -p gives exactly
  (A):  C_f = (1/2) int_0^inf p^2 cosh(py) W(p,x) dp.
  Both forms are correct and equal; equivalence NEEDS psi even (W even in p).""")
