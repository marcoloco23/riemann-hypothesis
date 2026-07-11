"""Numerical sign-check of the Riemann-Weil explicit formula in the L8 normalization.

    sum_rho  ghat(z_rho) = ghat(i/2) + ghat(-i/2)
                           - 2 sum_{n>=2} Lambda(n) n^{-1/2} g(log n)
                           + (1/2pi) int ghat(t) [Re psi0(1/4+it/2) - log pi] dt

with ghat(z) = int g(u) e^{-izu} du, g even real, z_rho = -i(rho-1/2)
(so z_rho = gamma for an on-line zero rho = 1/2 + i*gamma).

Motivational check only (docs/01 B1): uses the first NZEROS zeros (numerically
on the line) + a density-based tail estimate for the zero sum.

Two test functions:
  T1: g(u) = (1 - (u/3)^2)^3 on [-3,3]   (compactly supported, C^2; all four
      terms active: primes n <= 20 contribute)
  T2: g(u) = exp(-u^2/2)                  (Gaussian; zero-sum negligible,
      checks pole/prime/archimedean balance)

Deps: mpmath 1.3.0.  Deterministic.
"""
import mpmath as mp

mp.mp.dps = 25

NZEROS = 1000

def vonmangoldt_table(N):
    """Lambda(n) for 2..N."""
    lam = {}
    for p in range(2, N + 1):
        # p prime?
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            pk = p
            while pk <= N:
                lam[pk] = mp.log(p)
                pk *= p
    return lam

ZEROS = None
def zero_heights(n):
    global ZEROS
    if ZEROS is None:
        ZEROS = [mp.im(mp.zetazero(k)) for k in range(1, n + 1)]
    return ZEROS

def run_check(name, g, ghat, support, envelope=None):
    print(f"--- {name} ---")
    # pole term
    pole = ghat(mp.mpc(0, '0.5')) + ghat(mp.mpc(0, '-0.5'))
    pole = mp.re(pole)
    # prime term: g(log n) nonzero for log n < support
    N = int(mp.e ** support) + 1
    lam = vonmangoldt_table(N)
    primes = -2 * mp.fsum(lam[n] / mp.sqrt(n) * g(mp.log(n)) for n in sorted(lam))
    # archimedean term (integrand even in t)
    def arch_integrand(t):
        return mp.re(ghat(t)) * (mp.re(mp.digamma(mp.mpf('0.25') + 0.5j * t)) - mp.log(mp.pi))
    arch = (1 / mp.pi) * mp.quad(arch_integrand, [0, 5, 20, 100, 500, 2000])
    rhs = pole + primes + arch
    # zero sum (first NZEROS zeros, using gamma real = numerically verified heights)
    hs = zero_heights(NZEROS)
    zs = mp.fsum(2 * mp.re(ghat(h)) for h in hs)
    gamma_last = hs[-1]
    # tail estimate: |ghat(t)| * density (1/pi) log(t/2pi) dt, via analytic envelope
    env = envelope if envelope is not None else (lambda t: abs(ghat(t)))
    tail = (1 / mp.pi) * mp.quad(lambda t: env(t) * mp.log(t / (2 * mp.pi)),
                                 [gamma_last, 2 * gamma_last, 100 * gamma_last, mp.inf])
    print(f"  pole   = {mp.nstr(pole, 12)}")
    print(f"  primes = {mp.nstr(primes, 12)}")
    print(f"  arch   = {mp.nstr(arch, 12)}")
    print(f"  RHS    = {mp.nstr(rhs, 12)}")
    print(f"  LHS (sum over {NZEROS} zero pairs) = {mp.nstr(zs, 12)}")
    print(f"  LHS - RHS = {mp.nstr(zs - rhs, 6)}   (zero-sum tail bound ~ {mp.nstr(tail, 4)})")
    ok = abs(zs - rhs) <= tail + mp.mpf('1e-8')
    print(f"  MATCH within tail: {ok}")
    return ok

# T1: compact bump, support [-3,3]
A = mp.mpf(3)
def g1(u):
    u = mp.mpf(u) if not isinstance(u, mp.mpc) else u
    if abs(mp.re(u)) >= A:
        return mp.mpf(0)
    return (1 - (u / A) ** 2) ** 3

def ghat1(z):
    # closed form: int_{-1}^{1} (1-x^2)^3 e^{-iax} dx = sqrt(pi)*Gamma(4)*(2/a)^{7/2} J_{7/2}(a)
    # with u = A x, a = A z:  ghat(z) = A * sqrt(pi)*6*(2/(Az))^{7/2} * J_{7/2}(Az).
    # Entire in z; mpmath besselj handles small/complex arguments accurately.
    a = A * mp.mpc(z) if not isinstance(z, mp.mpc) else A * z
    if abs(a) < mp.mpf('1e-8'):
        return mp.mpf(2) * A * mp.mpf(16) / 35  # ghat(0) = 2*A*16/35
    val = A * mp.sqrt(mp.pi) * 6 * (2 / a) ** mp.mpf('3.5') * mp.besselj(mp.mpf('3.5'), a)
    return val

def ghat1_envelope(t):
    # |J_{7/2}(x)| <~ sqrt(2/(pi x)) for large x  =>  |ghat(t)| <= C * t^{-4}
    a = A * t
    return A * mp.sqrt(mp.pi) * 6 * (2 / a) ** mp.mpf('3.5') * mp.sqrt(2 / (mp.pi * a))

# T2: Gaussian
def g2(u):
    return mp.e ** (-mp.mpf(u) ** 2 / 2) if not isinstance(u, mp.mpc) else mp.exp(-u ** 2 / 2)

def ghat2(z):
    return mp.sqrt(2 * mp.pi) * mp.exp(-z ** 2 / 2)

ok1 = run_check("T1: bump (1-(u/3)^2)^3", g1, ghat1, 3, envelope=ghat1_envelope)
# Gaussian support cutoff: g2(log n) < 1e-30 for log n > 12  => n <= e^12; use 9 => 1e-17
ok2 = run_check("T2: Gaussian exp(-u^2/2)", g2, ghat2, 9)
print()
print("OVERALL:", "PASS" if (ok1 and ok2) else "FAIL")
