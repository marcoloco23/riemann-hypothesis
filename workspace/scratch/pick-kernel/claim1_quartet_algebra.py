"""CLAIM 1 (symbolic, sympy): quartet contribution to Q(x) and derivative identities.

Setup: centered zero alpha = a + i b (alpha = rho - 1/2), c = alpha^2 = u + i v,
u = a^2 - b^2, v = 2ab, A = x^2 - u, B = v.

Checks:
 (1a) Q_alpha(x) := d/dx log[(1 - x^2/alpha^2)(1 - x^2/conj(alpha)^2)] == 4 x A / (A^2 + B^2).
 (1b) Q_alpha(x) - x Q_alpha'(x) == 8 x^3 (A^2 - B^2) / (A^2 + B^2)^2.
 (1c) Q_alpha(x) + x Q_alpha'(x) == 8 x (-u (A^2 - B^2) + 2 A B^2) / (A^2 + B^2)^2.
 (1d) Positivity logic: under x > 1/2 (in fact x > 0), |a| < 1/2, |b| >= 14:
        A - B = x^2 + (a - b)^2 - 2 a^2  and  A + B = x^2 + (a + b)^2 - 2 a^2
      (verified symbolically), hence A > |B| > 0 is impossible to violate:
      (a -+ b)^2 >= (14 - 1/2)^2 = 182.25 > 2 a^2 <= 1/2, so A -+ B > 0, i.e. A^2 > B^2;
      also u = a^2 - b^2 <= 1/4 - 196 < 0. Both RHS of (1b),(1c) are then > 0.
 (1e) Critical-line pair a = 0, alpha = i b: derive d/dx log(1 - x^2/alpha^2) == 2x/(x^2+b^2),
      and the analogous identities
        q - x q' == 4 x^3 / (x^2 + b^2)^2,   q + x q' == 4 x b^2 / (x^2 + b^2)^2  (both > 0).

All checks are exact sympy simplifications (no numerics needed).
"""

import sympy as sp

x, a, b, u, v = sp.symbols("x a b u v", real=True)

ok_all = True


def check(label, expr_diff):
    global ok_all
    d = sp.simplify(expr_diff)
    ok = (d == 0)
    ok_all = ok_all and ok
    print(f"  [{ 'PASS' if ok else 'FAIL' }] {label}: simplify(lhs - rhs) = {d}")
    return ok


print("=" * 78)
print("CLAIM 1: quartet contribution and derivative identities (exact sympy)")
print("=" * 78)

# ---- (1a) quartet contribution ----------------------------------------------
alpha = a + sp.I * b
c_expr = alpha**2  # = (a^2 - b^2) + 2ab i
A_ab = x**2 - (a**2 - b**2)
B_ab = 2 * a * b

Q_from_log = sp.diff(
    sp.log(1 - x**2 / alpha**2) + sp.log(1 - x**2 / sp.conjugate(alpha) ** 2), x
)
Q_claimed_ab = 4 * x * A_ab / (A_ab**2 + B_ab**2)
check("(1a) Q_alpha = 4xA/(A^2+B^2) from d/dx log of quartet factors",
      Q_from_log - Q_claimed_ab)

# Sanity: c = u + iv with u = a^2 - b^2, v = 2ab
check("(1a') Re(alpha^2) = a^2 - b^2, Im(alpha^2) = 2ab",
      sp.expand(c_expr) - ((a**2 - b**2) + sp.I * 2 * a * b))

# ---- (1b), (1c) in the (u, v) variables --------------------------------------
A = x**2 - u
B = v
Qa = 4 * x * A / (A**2 + B**2)
Qa_p = sp.diff(Qa, x)

check("(1b) Q - xQ' = 8x^3 (A^2-B^2)/(A^2+B^2)^2",
      (Qa - x * Qa_p) - 8 * x**3 * (A**2 - B**2) / (A**2 + B**2) ** 2)
check("(1c) Q + xQ' = 8x (-u(A^2-B^2)+2AB^2)/(A^2+B^2)^2",
      (Qa + x * Qa_p) - 8 * x * (-u * (A**2 - B**2) + 2 * A * B**2) / (A**2 + B**2) ** 2)

# ---- (1d) positivity logic ---------------------------------------------------
check("(1d) A - B = x^2 + (a-b)^2 - 2a^2  (with A,B in terms of a,b)",
      (A_ab - B_ab) - (x**2 + (a - b) ** 2 - 2 * a**2))
check("(1d) A + B = x^2 + (a+b)^2 - 2a^2",
      (A_ab + B_ab) - (x**2 + (a + b) ** 2 - 2 * a**2))

print("""
  Positivity conclusion (logic, using the verified identities):
    Under |a| < 1/2, |b| >= 14, x > 0:
      (a-b)^2 and (a+b)^2 >= (14 - 1/2)^2 = 182.25, while 2a^2 <= 1/2,
      so A - B > 0 and A + B > 0  =>  A > |B|  =>  A^2 - B^2 > 0;  A > 0.
      u = a^2 - b^2 <= 1/4 - 196 < 0  =>  -u > 0.
    Hence RHS of (1b) = 8x^3(A^2-B^2)/(A^2+B^2)^2 > 0
      and RHS of (1c) = 8x(-u(A^2-B^2) + 2AB^2)/(A^2+B^2)^2 > 0 (both terms >= 0, first > 0).
    NOTE: this needs only x > 0, not x > 1/2, and does NOT need a = 0:
    it holds for EVERY zero allowed by known facts (0 < Re(rho) < 1, |Im rho| > 14),
    on or off the critical line.""")

# Numeric spot grid for the positivity of both RHS (belt and braces)
import itertools
viol = []
for av in [-0.499, -0.25, 0.0, 0.25, 0.499]:
    for bv in [14, 14.13, 50, 1000]:
        for xv in [0.51, 1, 5, 100, 10000]:
            uu, vv = av**2 - bv**2, 2 * av * bv
            AA, BB = xv**2 - uu, vv
            r1 = 8 * xv**3 * (AA**2 - BB**2) / (AA**2 + BB**2) ** 2
            r2 = 8 * xv * (-uu * (AA**2 - BB**2) + 2 * AA * BB**2) / (AA**2 + BB**2) ** 2
            if r1 <= 0 or r2 <= 0:
                viol.append((av, bv, xv, r1, r2))
print(f"  grid check of positivity (100 points): violations = {viol if viol else 'none'}")

# ---- (1e) critical-line pair -------------------------------------------------
q_from_log = sp.diff(sp.log(1 - x**2 / (sp.I * b) ** 2), x)
q = 2 * x / (x**2 + b**2)
check("(1e) pair contribution: d/dx log(1 - x^2/(ib)^2) = 2x/(x^2+b^2)",
      q_from_log - q)
qp = sp.diff(q, x)
check("(1e) q - xq' = 4x^3/(x^2+b^2)^2", (q - x * qp) - 4 * x**3 / (x**2 + b**2) ** 2)
check("(1e) q + xq' = 4x b^2/(x^2+b^2)^2", (q + x * qp) - 4 * x * b**2 / (x**2 + b**2) ** 2)

print()
print("CLAIM 1 overall:", "ALL IDENTITIES PASS" if ok_all else "SOME CHECK FAILED")
print("""
Conclusion target (-Q <= xQ' <= Q for x > 1/2):
  Each pair/quartet term t satisfies t - x t' > 0 and t + x t' > 0 (verified above),
  so IF Q(x) = sum of these terms and xQ'(x) = sum of x t'(x) termwise, then
  -Q(x) < xQ'(x) < Q(x) follows.  Analytic justification (standard, not re-proved here):
  xi(s) = xi(0) prod_rho (1 - s/rho) with zeros paired (rho, 1-rho) makes the product
  absolutely convergent when grouped; centering at 1/2 and grouping {alpha,-alpha,
  conj(alpha),-conj(alpha)} gives xi(1/2+x)/xi(1/2) = prod (1 - x^2/alpha^2)... ;
  on any compact subset of the real ray x > 1/2 (where xi(1/2+x) != 0, since
  zeta(s) != 0 for real s > 1 by the Euler product), sum_rho 1/|rho|^2 < infinity
  gives locally uniform convergence of the term series and of its derivative series,
  so termwise differentiation is valid.
  *** IMPORTANT CAVEAT: the inequality is therefore UNCONDITIONAL - it holds whether
  or not RH is true, because the quartet terms are positive for off-line zeros too
  (only |a| < 1/2 and |b| >= 14 were used, both known facts).  So -Q <= xQ' <= Q
  carries NO RH content: it can never serve as an RH criterion. ***
""")
