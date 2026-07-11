"""Hostile numeric verification of L8a, formula (W), and the density remark in Sec 3.

Conventions from the file:
  ghat(z) = int g(u) e^{-izu} du,  g even real.
  L8a:  sum_{z in Z_zeta} ghat(z) = ghat(i/2)+ghat(-i/2)
        - 2 sum_{n>=2} Lambda(n) n^{-1/2} g(log n)
        + (1/2pi) int ghat(t) [Re psi0(1/4+it/2) - log pi] dt
  (W):  <W_inf, g> = -(gamma_E + log pi) g(0)
        + int_0^inf [g(0) - e^{3v/2} g(v)] * 2 e^{-2v}/(1-e^{-2v}) dv
        and W_inf should equal  (1/2pi) int ghat(t)[Re psi0(1/4+it/2) - log pi] dt.
  Density claim: away from 0, W_inf = -2 e^{-|u|/2}/(1-e^{-2|u|}) du.
"""
import mpmath as mp

mp.mp.dps = 30

# ---------- Lambda(n) sieve ----------
NMAX = 200000
def lambda_list(nmax):
    """return list of (n, Lambda(n)) for n<=nmax with Lambda(n)!=0"""
    sieve = bytearray([1]) * (nmax + 1)
    sieve[0] = sieve[1] = 0
    out = []
    import math
    for p in range(2, nmax + 1):
        if sieve[p]:
            for q in range(p * p, nmax + 1, p):
                sieve[q] = 0
            lp = mp.log(p)
            pk = p
            while pk <= nmax:
                out.append((pk, lp))
                pk *= p
    out.sort()
    return out

LAM = lambda_list(NMAX)

def gaussian_pair(a, b):
    """g(u)=exp(-u^2/(2a)) cos(b u); ghat(z)=0.5 sqrt(2 pi a)[e^{-a(z-b)^2/2}+e^{-a(z+b)^2/2}]"""
    a = mp.mpf(a); b = mp.mpf(b)
    def g(u):
        return mp.e**(-u * u / (2 * a)) * mp.cos(b * u)
    c = mp.mpf(1) / 2 * mp.sqrt(2 * mp.pi * a)
    def ghat(z):
        return c * (mp.e**(-a * (z - b) ** 2 / 2) + mp.e**(-a * (z + b) ** 2 / 2))
    return g, ghat

def comb_term(g, a, b):
    # -2 sum Lambda(n) n^{-1/2} g(log n); truncate when envelope < 1e-30
    s = mp.mpf(0)
    for n, lam in LAM:
        ln = mp.log(n)
        if ln * ln / (2 * mp.mpf(a)) > 80:   # e^{-80} envelope cutoff
            break
        s += lam / mp.sqrt(n) * g(ln)
    return -2 * s

def arch_term(ghat, pts):
    # (1/2pi) int_R ghat(t)[Re psi(1/4+it/2) - log pi] dt ; integrand even
    def f(t):
        return ghat(t) * (mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * t / 2)) - mp.log(mp.pi))
    return (mp.quad(f, pts)) / mp.pi   # = (1/2pi)*2*int_0^inf

def zero_term(ghat, K):
    s = mp.mpf(0)
    for k in range(1, K + 1):
        gam = mp.im(mp.zetazero(k))
        s += 2 * ghat(gam)   # both signs
    return s

def check_L8a(a, b, K, pts):
    g, ghat = gaussian_pair(a, b)
    Z = zero_term(ghat, K)
    P = ghat(mp.mpc(0, 0.5)) + ghat(mp.mpc(0, -0.5))
    C = comb_term(g, a, b)
    A = arch_term(ghat, pts)
    print(f"  a={a}, b={b}:")
    print(f"    zeros LHS      = {mp.nstr(Z, 20)}")
    print(f"    pole term      = {mp.nstr(P, 20)}")
    print(f"    prime comb     = {mp.nstr(C, 20)}")
    print(f"    archimedean    = {mp.nstr(A, 20)}")
    print(f"    RHS total      = {mp.nstr(P + C + A, 20)}")
    print(f"    LHS - RHS      = {mp.nstr(Z - (P + C + A), 5)}")
    print()

print("=== L8a full explicit-formula check ===")
# test 1: modulated gaussian, zero sum O(1), all four terms active
check_L8a(1, 14, 40, [0, 8, 12, 14, 16, 20, 30, 60])
# test 2: wide unmodulated gaussian, zero term ~0, tests pole/comb/arch balance
check_L8a(4, 0, 40, [0, 3, 8, 20, 60])
# test 3: narrow-ish, everything moderate
check_L8a(0.2, 0, 60, [0, 5, 15, 40, 100])

print("=== (W) formula check: direct arch integral vs (W) ===")
def W_formula(g):
    g0 = g(mp.mpf(0))
    def integrand(v):
        if v == 0:
            return -mp.mpf(3) / 2 * g0  # limit value
        return (g0 - mp.e**(3 * v / 2) * g(v)) * 2 * mp.e**(-2 * v) / (1 - mp.e**(-2 * v))
    return -(mp.euler + mp.log(mp.pi)) * g0 + mp.quad(integrand, [0, 1, 5, 20, 80])

for (a, b, pts) in [(1, 0, [0, 3, 10, 40]), (4, 0, [0, 3, 8, 20, 60]), (1, 14, [0, 8, 14, 20, 40])]:
    g, ghat = gaussian_pair(a, b)
    direct = arch_term(ghat, pts)
    viaW = W_formula(g)
    print(f"  a={a}, b={b}: direct={mp.nstr(direct,20)}  viaW={mp.nstr(viaW,20)}  diff={mp.nstr(direct-viaW,5)}")

print()
print("=== density claim check (g supported away from 0) ===")
# g2(u) = e^{-8(u-2)^2} + e^{-8(u+2)^2}; ghat2(t) = 2 cos(2t) sqrt(pi/8) e^{-t^2/32}
def g2(u):
    return mp.e**(-8 * (u - 2) ** 2) + mp.e**(-8 * (u + 2) ** 2)
def ghat2(t):
    return 2 * mp.cos(2 * t) * mp.sqrt(mp.pi / 8) * mp.e**(-t * t / 32)

direct2 = arch_term(ghat2, [0, 5, 15, 40, 100])
viaW2 = W_formula(g2)
# claimed density -2 e^{-|u|/2}/(1-e^{-2|u|}):
D_claimed = 2 * mp.quad(lambda u: g2(u) * (-2 * mp.e**(-u / 2) / (1 - mp.e**(-2 * u))), [0.5, 2, 4])
D_half = D_claimed / 2
print(f"  direct arch    = {mp.nstr(direct2, 20)}")
print(f"  via (W)        = {mp.nstr(viaW2, 20)}")
print(f"  claimed density -2e^-|u|/2/(1-e^-2|u|): {mp.nstr(D_claimed, 20)}")
print(f"  half density    -e^-|u|/2/(1-e^-2|u|): {mp.nstr(D_half, 20)}")
