"""Claim 3: hierarchy for H_t(x) = int e^{t u^2} phi(u) e^{ixu} du.

L_n(t,x) := (1/(2n)!) iint (u-v)^{2n} e^{t(u^2+v^2)} e^{ix(u+v)} phi(u)phi(v) du dv

Claim A: L_n(t,x) = L_n[H_t](x)  (claim-1 operator applied to H_t)
Claim B: d/dt L_n = -(1/2) d^2/dx^2 L_n + (n+1)(2n+1) L_{n+1}

Part A: integrand-level algebra with sympy.
Part B: numeric check of Claim A at t=0, n=0,1, x=3, phi(u)=e^{-u^2-u^4}.
"""
import sympy as sp
import mpmath as mp

print("=" * 72)
print("CLAIM 3 -- phase-space hierarchy for H_t")
print("=" * 72)

u, v, x, t = sp.symbols('u v x t', real=True)
n = sp.symbols('n', integer=True, nonnegative=True)

# --- (a) u^2+v^2 = (1/2)(u+v)^2 + (1/2)(u-v)^2 ---
idA = sp.expand(u ** 2 + v ** 2 - (sp.Rational(1, 2) * (u + v) ** 2 + sp.Rational(1, 2) * (u - v) ** 2))
print(f"\n[a] u^2+v^2 - [ (u+v)^2/2 + (u-v)^2/2 ] = {idA}   {'PASS' if idA == 0 else 'FAIL'}")

# --- (b) Claim A at integrand level ---
# L_n[H_t](x) inserts H_t^(j)(x) = int (iu)^j e^{tu^2} phi e^{ixu} du.  The double
# integrand's polynomial part is sum_j (-1)^{j+n} C(2n,j) (iu)^j (iv)^{2n-j},
# which must equal (u-v)^{2n}.
print("\n[b] Claim A kernel: sum_j (-1)^(j+n) C(2n,j) (iu)^j (iv)^(2n-j) == (u-v)^(2n)")
okA = True
for nn in range(5):
    S = sp.expand(sum((-1) ** (j + nn) * sp.binomial(2 * nn, j) * (sp.I * u) ** j * (sp.I * v) ** (2 * nn - j)
                      for j in range(2 * nn + 1)))
    d = sp.expand(S - (u - v) ** (2 * nn))
    print(f"    n={nn}: difference = {d}   {'PASS' if d == 0 else 'FAIL'}")
    okA = okA and (d == 0)
print("    (differentiation under the integral is justified by rapid decrease of phi,")
print("     for t below the Gaussian threshold; noted as hypothesis, not checked here)")

# --- (c) coefficient bookkeeping for Claim B, symbolic in n ---
# (1/2)(u-v)^2 * (u-v)^{2n}/(2n)!  ==  (n+1)(2n+1) * (u-v)^{2n+2}/(2n+2)!
coeff = sp.simplify(sp.Rational(1, 2) / sp.factorial(2 * n) - (n + 1) * (2 * n + 1) / sp.factorial(2 * n + 2))
print(f"\n[c] 1/(2(2n)!) - (n+1)(2n+1)/(2n+2)! = {coeff}   {'PASS' if coeff == 0 else 'FAIL'}")

# --- (d) full integrand identity for Claim B, concrete n = 0..3 ---
# G_n = (u-v)^{2n}/(2n)! * e^{t(u^2+v^2)} * e^{ix(u+v)}   (phi(u)phi(v) is a
# constant w.r.t. t and x, so it can be dropped).
print("\n[d] d/dt G_n + (1/2) d^2/dx^2 G_n - (n+1)(2n+1) G_{n+1} == 0")
E = sp.exp(t * (u ** 2 + v ** 2)) * sp.exp(sp.I * x * (u + v))
okB = True
for nn in range(4):
    Gn = (u - v) ** (2 * nn) / sp.factorial(2 * nn) * E
    Gn1 = (u - v) ** (2 * nn + 2) / sp.factorial(2 * nn + 2) * E
    resid = sp.simplify(sp.diff(Gn, t) + sp.Rational(1, 2) * sp.diff(Gn, x, 2) - (nn + 1) * (2 * nn + 1) * Gn1)
    print(f"    n={nn}: residual = {resid}   {'PASS' if resid == 0 else 'FAIL'}")
    okB = okB and (resid == 0)
print("    (i.e. d/dt L_n = -(1/2) d^2/dx^2 L_n + (n+1)(2n+1) L_{n+1} at integrand level)")

# --- (e) numeric Claim A: t=0, n=0,1, x=3, phi = e^{-u^2-u^4} ---
print("\n[e] Numeric Claim A at t=0, x=3, phi(u)=exp(-u^2-u^4), dps=30")
mp.mp.dps = 30
LIM = mp.mpf('3.8')  # exp(-3.8^4) ~ 1e-91 << 1e-30


def phi(w):
    return mp.exp(-w ** 2 - w ** 4)


def f(z):  # H_0(z), entire in z since phi decays like e^{-u^4}
    z = mp.mpc(z)
    return mp.quad(lambda w: phi(w) * mp.exp(1j * z * w), [-LIM, 0, LIM])


xv = mp.mpf(3)
for nn in [0, 1]:
    # double integral (real part; imaginary part vanishes by u,v -> -u,-v)
    dbl = mp.quad(lambda uu, vv: (uu - vv) ** (2 * nn) * phi(uu) * phi(vv) * mp.cos(xv * (uu + vv)),
                  [-LIM, 0, LIM], [-LIM, 0, LIM]) / mp.factorial(2 * nn)
    # derivative formula
    ders = [mp.mpc(mp.diff(f, xv, k, method='quad', radius=0.5)).real if k else mp.mpc(f(xv)).real
            for k in range(2 * nn + 1)]
    Ln = sum((-1) ** (j + nn) * mp.binomial(2 * nn, j) * ders[j] * ders[2 * nn - j]
             for j in range(2 * nn + 1)) / mp.factorial(2 * nn)
    rel = abs(dbl - Ln) / max(abs(dbl), abs(Ln))
    print(f"    n={nn}:  double integral = {mp.nstr(dbl, 20)}")
    print(f"           L_n[f](3)       = {mp.nstr(Ln, 20)}")
    print(f"           rel. difference = {mp.nstr(rel, 4)}   {'PASS' if rel < mp.mpf('1e-20') else 'FAIL'}")
