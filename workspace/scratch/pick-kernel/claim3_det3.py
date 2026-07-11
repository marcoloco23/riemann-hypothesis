"""CLAIM 3 (symbolic, sympy): single-quartet 3x3 Pick determinant.

Kernel of one off-line quartet, c = alpha^2 = u + i v (u < 0, v != 0):
    K_alpha(x,y) = 2(xy - c)/((x^2-c)(y^2-c)) + 2(xy - cbar)/((x^2-cbar)(y^2-cbar)).

Checks:
 (3a) K_alpha(x,y) == (Q_alpha(x) + Q_alpha(y))/(x + y),  Q_alpha(x) = 2x/(x^2-c) + 2x/(x^2-cbar)
      (fully symbolic in x, y, u, v; note Q_alpha here agrees with claim 1's 4xA/(A^2+B^2)).
 (3b) Real form: K_alpha(x,y) = 4[(xy-u)(A_x A_y - v^2) + v^2 (A_x + A_y)] / (D_x D_y),
      A_t = t^2 - u, D_t = A_t^2 + v^2 = |t^2 - c|^2.
 (3c) det[K_alpha(x_j,x_k)]_{3x3}
        ?= [64 v^2 prod_{j<k}(x_j - x_k)^2 / prod_j D_j^2] * [ -Re( cbar * prod_j (c - x_j^2) ) ].
      Verified two ways: (i) fully symbolically via polynomial cancellation,
      (ii) at exact rational sample points (deterministic seed).
 (3d) Sign: for u < 0, |v/u| < 0.072, x_j > 1/2 distinct:  Re(cbar prod(c - x_j^2)) > 0,
      hence det < 0.  Phase argument + numeric grid; also locate the true failure
      threshold (|v/u| up to tan(pi/8) ~ 0.4142 still works; test beyond).
"""

import itertools
import random
from fractions import Fraction

import sympy as sp

x, y, u, v = sp.symbols("x y u v", real=True)
x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)

c = u + sp.I * v
cb = u - sp.I * v

ok_all = True


def report(label, ok, extra=""):
    global ok_all
    ok_all = ok_all and ok
    print(f"  [{ 'PASS' if ok else 'FAIL' }] {label}{(': ' + extra) if extra else ''}")


def K_complex(s, t):
    return 2 * (s * t - c) / ((s**2 - c) * (t**2 - c)) + \
           2 * (s * t - cb) / ((s**2 - cb) * (t**2 - cb))


def Q_alpha(s):
    return 2 * s / (s**2 - c) + 2 * s / (s**2 - cb)


print("=" * 78)
print("CLAIM 3: single-quartet 3x3 Pick determinant (exact sympy)")
print("=" * 78)

# ---- (3a) K = (Q(x)+Q(y))/(x+y) ---------------------------------------------
d = sp.cancel(sp.together(K_complex(x, y) - (Q_alpha(x) + Q_alpha(y)) / (x + y)))
report("(3a) K_alpha(x,y) = (Q_alpha(x)+Q_alpha(y))/(x+y)", d == 0, f"cancel -> {d}")

# consistency with claim 1's Q_alpha = 4xA/(A^2+B^2)
A_x = x**2 - u
d = sp.cancel(sp.together(Q_alpha(x) - 4 * x * A_x / (A_x**2 + v**2)))
report("(3a') Q_alpha(x) = 4xA/(A^2+v^2)", d == 0, f"cancel -> {d}")

# ---- (3b) real form -----------------------------------------------------------
def A_of(t):
    return t**2 - u


def D_of(t):
    return A_of(t) ** 2 + v**2


def K_real(s, t):
    return 4 * ((s * t - u) * (A_of(s) * A_of(t) - v**2) + v**2 * (A_of(s) + A_of(t))) / (D_of(s) * D_of(t))


d = sp.cancel(sp.together(K_complex(x, y) - K_real(x, y)))
report("(3b) real form of K_alpha", d == 0, f"cancel -> {d}")

# ---- (3c) the 3x3 determinant identity ---------------------------------------
xs = [x1, x2, x3]
M = sp.Matrix(3, 3, lambda j, k: K_real(xs[j], xs[k]))

# det = det(N) / prod D_j^2 where N_jk = numerator polynomial (each entry has D_j D_k)
N = sp.Matrix(3, 3, lambda j, k: sp.expand(
    4 * ((xs[j] * xs[k] - u) * (A_of(xs[j]) * A_of(xs[k]) - v**2)
         + v**2 * (A_of(xs[j]) + A_of(xs[k])))))
detN = sp.expand(N.det())          # polynomial in x1,x2,x3,u,v
prodD2 = sp.prod(D_of(t) for t in xs) ** 2

# claimed RHS
vandermonde2 = ((x1 - x2) * (x1 - x3) * (x2 - x3)) ** 2
bracket = -sp.re(sp.expand(cb * sp.prod((c - t**2) for t in xs)))  # -Re(cbar prod(c - x_j^2))
claimed_num = sp.expand(64 * v**2 * vandermonde2 * bracket)

diff_poly = sp.expand(detN - claimed_num)
report("(3c) det identity, FULLY SYMBOLIC: det(N) == 64 v^2 Vdm^2 * (-Re(cbar prod(c-x_j^2)))",
       diff_poly == 0, f"expanded difference = {diff_poly if diff_poly != 0 else 0}")

# independent confirmation at exact rational points (deterministic)
random.seed(42)
mism = 0
for trial in range(8):
    subs = {
        x1: Fraction(random.randint(1, 200), random.randint(1, 20)) + Fraction(1, 2),
        x2: Fraction(random.randint(1, 200), random.randint(1, 20)) + Fraction(3, 2),
        x3: Fraction(random.randint(1, 200), random.randint(1, 20)) + Fraction(5, 2),
        u: -Fraction(random.randint(1, 5000), random.randint(1, 10)),
        v: Fraction(random.randint(1, 300), random.randint(1, 10)),
    }
    subs_sp = {k: sp.Rational(f.numerator, f.denominator) for k, f in subs.items()}
    lhs = M.subs(subs_sp).det()
    rhs = (64 * v**2 * vandermonde2 / prodD2 * bracket).subs(subs_sp)
    if sp.simplify(lhs - rhs) != 0:
        mism += 1
report("(3c') det identity at 8 exact rational sample points", mism == 0,
       f"mismatches = {mism}")

# ---- (3d) sign of the bracket -------------------------------------------------
print("""
  (3d) Phase argument for Re(cbar * prod_j(c - x_j^2)) with u < 0 (take v > 0 wlog;
       v -> -v conjugates the product, leaving Re unchanged):
    c - x_j^2 = -(A_j - iv), A_j = x_j^2 - u > |u| > 0, so
    cbar * prod_{j=1..3}(c - x_j^2) = -(u - iv)*(-1)^3 prod(A_j - iv)
                                    = (|u| + iv) * prod_j (A_j - iv).
    arg(|u|+iv) = +arctan(v/|u|); arg(A_j - iv) = -arctan(v/A_j), and
    0 < arctan(v/A_j) < arctan(v/|u|) since A_j > |u|.  The signs OPPOSE, so
    total arg T = arctan(v/|u|) - sum_j arctan(v/A_j) lies in (-2*arctan(v/|u|), arctan(v/|u|)),
    hence |T| < 2*arctan(|v/u|) < pi/2 whenever |v/u| < tan(pi/4) = 1.
    => Re = |...|*cos(T) > 0 STRICTLY for ALL |v/u| < 1 (and can genuinely fail
    only for |v/u| > 1).  The claimed 0.072 window is therefore correct but very
    conservative; 0.072 is what zeta-zero constraints give:
    |v/u| = 2|a||b|/(b^2-a^2) < 1/|b| <= 1/14 = 0.0714 for |a| < 1/2, |b| >= 14.
""")

import mpmath as mp
mp.mp.dps = 40

def bracket_num(uu, vv, pts):
    cc = mp.mpc(uu, vv)
    return mp.re(mp.conj(cc) * mp.fprod([cc - t**2 for t in pts]))

fails_below = []
grid_u = [mp.mpf(s) for s in ("-0.1", "-1", "-10", "-196", "-7344.3", "-1e5")]
grid_r = [mp.mpf(s) for s in ("0.001", "0.01", "0.0714", "0.07199")]
pt_sets = [
    (mp.mpf("0.51"), mp.mpf("0.52"), mp.mpf("0.53")),
    (mp.mpf("0.6"), mp.mpf("1.7"), mp.mpf("9.4")),
    (mp.mpf("1"), mp.mpf("10"), mp.mpf("100")),
    (mp.mpf("50"), mp.mpf("85.7"), mp.mpf("120")),
    (mp.mpf("200"), mp.mpf("500"), mp.mpf("1000")),
]
count = 0
for uu in grid_u:
    for r in grid_r:
        for sgn in (1, -1):
            vv = sgn * r * abs(uu)
            for pts in pt_sets:
                count += 1
                val = bracket_num(uu, vv, pts)
                if val <= 0:
                    fails_below.append((float(uu), float(vv), tuple(map(float, pts)), float(val)))
report(f"(3d) Re(cbar prod(c-x_j^2)) > 0 on grid |v/u| <= 0.072, u<0 ({count} cases)",
       not fails_below, f"violations = {fails_below if fails_below else 'none'}")

# where DOES it fail?  the corrected phase bound predicts safety up to |v/u| = 1,
# with worst case A_j ~ |u| (x_j^2 << |u|), and genuine failure for |v/u| > 1.
thresh_examples = []
for r in ("0.30", "0.4142", "0.9", "0.999", "1.0", "1.01", "1.5"):
    uu = mp.mpf("-1e6")
    vv = mp.mpf(r) * abs(uu)
    pts = (mp.mpf("0.51"), mp.mpf("0.6"), mp.mpf("0.7"))  # x_j^2 << |u| -> worst case
    val = bracket_num(uu, vv, pts)
    thresh_examples.append((r, float(val)))
print("  (3d) threshold exploration, u = -1e6, x_j ~ 0.5 (worst case A_j ~ |u|):")
for r, val in thresh_examples:
    print(f"        |v/u| = {r:>7}: Re(cbar prod(c - x_j^2)) = {val:+.4e}  "
          f"({'>0' if val > 0 else '<0  <-- fails only past |v/u| = 1'})")

print()
print("CLAIM 3 overall:", "IDENTITY + SIGN CLAIM VERIFIED" if ok_all else "FAILED")
print("""  Consequence (as claimed): for ANY 3 distinct points x_j > 1/2 and any c = u+iv
  with u < 0, 0 < |v/u| < 0.072, the single-quartet 3x3 Pick matrix has det < 0,
  i.e. an odd number of negative eigenvalues (in fact signature (2,1): the kernel has
  rank 4 with at most 1 negative square among {Re g, Im g, Re h, Im h} coordinates...
  -- signature checked numerically in claim 5's script).  NOTE this concerns the
  SINGLE-QUARTET kernel alone; it does NOT by itself make the FULL Pick matrix
  (quartet + on-line background) indefinite.  That gap is probed in claim 5.""")
