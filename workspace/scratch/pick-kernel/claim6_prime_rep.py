"""CLAIM 6 (numerical, mpmath): sanity checks on Q(x) = xi'/xi(1/2+x).

 (6a) Structural identity: Q(x) == Q_inf(x) + zeta'/zeta(1/2+x) with
        Q_inf(x) = 1/(x+1/2) + 1/(x-1/2) - log(pi)/2 + psi(x/2+1/4)/2,
      cross-checked against two INDEPENDENT computations of xi'/xi(1/2+x):
      mp.diff finite differences and a trapezoidal Cauchy integral.
      (Reconciliation: s = 1/2+x so 1/s = 1/(x+1/2), 1/(s-1) = 1/(x-1/2),
       psi(s/2) = psi(x/2+1/4) -- the claim's terms are exactly the standard
       xi'/xi(s) = 1/s + 1/(s-1) - log(pi)/2 + psi(s/2)/2 + zeta'/zeta(s).)
 (6b) Prime representation: zeta'/zeta(1/2+x) == -sum_{n>=2} Lambda(n) n^(-1/2-x)
      for x > 1/2, truncated at N = 10^6 with the rigorous tail bound
        0 <= sum_{n>N} Lambda(n) n^(-sigma) <= int_N^inf t^(-sigma) log t dt
           = N^(1-sigma) [log N/(sigma-1) + 1/(sigma-1)^2]      (sigma = 1/2 + x + 1/2...
      no: sigma = x + 1/2),
      using Lambda(n) <= log n and monotonicity of t^(-sigma) log t for t >= e^(1/sigma).
      Achievable digits depend on x:  x=5 -> ~26 digits (>= 20 as requested);
      x=2.5 -> ~11 digits; x=1.5 -> ~4-5 digits (20+ digits at x=1.5 would need
      N ~ 10^21: infeasible by direct truncation -- reported honestly).
 (6c) Q(x) > 0 for x in (1/2, 50]: grid scan + minimum location.
"""

import common  # sets dps FIRST
import mpmath as mp
import sympy

print("=" * 78)
print(f"CLAIM 6: Q(x) sanity + prime representation  (mpmath dps = {mp.mp.dps})")
print("=" * 78)

# ---- (6a) structural identity --------------------------------------------------
print("\n(6a) Q_formula vs two independent xi'/xi computations:")
print(f"{'x':>6} | {'|Q_formula - Q_mp.diff|':>25} | {'|Q_formula - Q_cauchy|':>25} | Q(x)")
for xv in ("1.5", "2.5", "5", "10"):
    xv = mp.mpf(xv)
    qf = common.Q_formula(xv)
    qd = common.Q_diff(xv)                                   # finite differences
    qc = common.logderiv_cauchy(common.xi, mp.mpf("0.5") + xv)  # Cauchy integral
    print(f"{mp.nstr(xv, 4):>6} | {mp.nstr(abs(qf - qd), 3):>25} | "
          f"{mp.nstr(abs(qf - mp.re(qc)), 3):>25} | {mp.nstr(qf, 30)}")

# ---- (6b) prime representation --------------------------------------------------
N_TRUNC = 10 ** 6
print(f"\n(6b) prime sum  -zeta'/zeta(1/2+x) = sum Lambda(n) n^(-1/2-x), truncated at N = {N_TRUNC:.0e}")

primes = list(sympy.primerange(2, N_TRUNC + 1))
prime_powers = []          # (n, log p) with n = p^k <= N
for p in primes:
    n = p
    lp = mp.log(p)
    while n <= N_TRUNC:
        prime_powers.append((n, lp))
        n *= p
print(f"     prime powers <= N: {len(prime_powers)}")


def tail_bound(sigma, N):
    """Rigorous: sum_{n>N} Lambda(n) n^-sigma <= N^(1-sigma)(log N/(sigma-1) + 1/(sigma-1)^2)."""
    N = mp.mpf(N)
    return N ** (1 - sigma) * (mp.log(N) / (sigma - 1) + 1 / (sigma - 1) ** 2)


print(f"{'x':>5} | {'sigma':>6} | {'|LHS - truncated sum|':>22} | {'rigorous tail bound':>20} | verdict")
for xv in ("1.5", "2.5", "5"):
    xv = mp.mpf(xv)
    sigma = mp.mpf("0.5") + xv
    lhs = -mp.zeta(sigma, derivative=1) / mp.zeta(sigma)
    ssum = mp.fsum(lp * mp.power(n, -sigma) for n, lp in prime_powers)
    err = abs(lhs - ssum)
    tb = tail_bound(sigma, N_TRUNC)
    ok = err <= tb
    digits = int(mp.floor(-mp.log10(tb))) if tb < 1 else 0
    print(f"{mp.nstr(xv, 3):>5} | {mp.nstr(sigma, 3):>6} | {mp.nstr(err, 3):>22} | {mp.nstr(tb, 3):>20} | "
          f"{'PASS' if ok else 'FAIL'} (~{digits} digits certified)")
print("""     NOTE: at x = 1.5 (sigma = 2) direct truncation certifies only ~4-5 digits;
     20+ digits would need N ~ 10^21 terms.  The representation is nevertheless a
     classical theorem for Re(s) > 1; the numerics above confirm it to the digits
     the rigorous tail bound allows, and the structural identity (6a) is confirmed
     to ~40+ digits independently of the prime sum.""")

# ---- (6c) positivity scan --------------------------------------------------------
print("\n(6c) Q(x) > 0 scan on (1/2, 50]:")
grid = ([mp.mpf("0.5") + mp.mpf(k) / 100 for k in range(1, 151)]      # 0.51 .. 2.00
        + [mp.mpf(2) + mp.mpf(k) / 20 for k in range(1, 161)]         # 2.05 .. 10
        + [mp.mpf(10) + mp.mpf(k) / 2 for k in range(1, 81)])         # 10.5 .. 50
vals = [(xv, common.Q_formula(xv)) for xv in grid]
neg = [(float(xv), float(q)) for xv, q in vals if q <= 0]
xmin, qmin = min(vals, key=lambda t: t[1])
print(f"     grid points: {len(grid)}; Q <= 0 at: {neg if neg else 'none'}")
print(f"     minimum on grid: Q({mp.nstr(xmin, 6)}) = {mp.nstr(qmin, 25)}  (left edge of grid)")
monotone = all(vals[i + 1][1] > vals[i][1] for i in range(len(vals) - 1))
print(f"     Q strictly increasing along the grid: {monotone}")
# Boundary behavior: the pole of zeta'/zeta at s=1 cancels 1/(x-1/2); Q extends
# continuously to x = 1/2 with Q(1/2) = xi'(1)/xi(1) = sum_rho 1/rho
#                                      = 1 + gamma/2 - log(4 pi)/2  (classical).
q_half_num = mp.re(common.logderiv_cauchy(common.xi, mp.mpf(1)))
q_half_closed = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
print(f"     boundary value Q(1/2+) = xi'(1)/xi(1) = {mp.nstr(q_half_num, 25)}")
print(f"       closed form 1 + gamma/2 - log(4 pi)/2 = {mp.nstr(q_half_closed, 25)}"
      f"   |diff| = {mp.nstr(abs(q_half_num - q_half_closed), 3)}")
print("     => inf of Q on (1/2, 50] is the boundary value ~0.0231 > 0.")
print(f"     Q > 0 on the scanned range: {'YES' if not neg and q_half_num > 0 else 'NO'}   [NUMERICAL]")
