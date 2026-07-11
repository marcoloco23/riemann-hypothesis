"""Stage 7 (Claim 5): the load-bearing finite-N identity.

Derived (see xi_common.py; no theta functional equation used for finite N —
only the substitution w = pi n^2 e^{2u} and Gamma(c+1,a) = c Gamma(c,a) + a^c e^{-a}):

    Xi_N(z) = C_N + (s(s-1)/2) * I_N(s),      s = 1/2 + i z,
    C_N = sum_{n<=N} (4 pi n^2 - 1) e^{-pi n^2},
    I_N(s) = Int_1^inf theta_N(u) (u^{s/2-1} + u^{(1-s)/2-1}) du   (NO extra 1/2),
    theta_N(u) = sum_{n<=N} e^{-pi n^2 u},

with Xi_N in the PINNED normalization Xi_N = 4 Int_0^inf (sum phi_n) cos(zu) du.
(In the task's 2*Int normalization both constants would instead be 1/2.)
C_N replaces the classical 1/2 and C_N -> 1/2 as N -> inf (stage 1).

Verification here, to >= 20 digits at several z in the strip:
  (A) I_N via direct quadrature of Int_1^inf theta_N (...) du  vs  the
      incomplete-gamma sum  sum_n [a_n^{-s/2}Gamma(s/2,a_n)+a_n^{-(1-s)/2}Gamma((1-s)/2,a_n)].
  (B) C_N + (s(s-1)/2)*I_N(quadrature)  vs  4*Int_0^inf sum phi_n cos(zu) du (direct Fourier).
  (C) Solve for unknown constants (k1, k2) in  Xi_N = k1*C_N + k2*(s(s-1)/2)*I_N
      from two z-values and confirm k1 = k2 = 1 (and residual at a third z).
"""
from mpmath import mp, mpf, mpc, exp, pi
from xi_common import Xi_N, Xi_N_direct, C_N, I_N, a_n, I

mp.dps = 45
print("=== Stage 7: claim 5, load-bearing identity ===")


def theta(u, N):
    return sum(exp(-pi * n * n * u) for n in range(1, N + 1))


def I_N_quad(s, N):
    U = mpf(60)  # e^{-pi*60} ~ 1e-82
    nseg = int(max(30, abs(mp.im(s)))) + 1
    pts = [1 + (U - 1) * k / nseg for k in range(nseg + 1)]
    return mp.quad(lambda u: theta(u, N) * (u ** (s / 2 - 1) + u ** ((1 - s) / 2 - 1)), pts)


test = [(1, mpc(3, mpf(1) / 10)), (2, mpc(10, mpf(4) / 10)), (3, mpc(25, mpf(1) / 4)),
        (4, mpc(40, mpf(45) / 100))]
print("(A)+(B): identity residuals at strip points (target < 1e-20 relative):")
for N, z in test:
    s = mpf(1) / 2 + I * z
    iq = I_N_quad(s, N)
    ig = I_N(s, N)
    relA = abs(iq - ig) / abs(ig)
    lhs = Xi_N_direct(z, N)
    rhs = C_N(N) + s * (s - 1) / 2 * iq
    relB = abs(lhs - rhs) / abs(lhs)
    print(f"  N={N} z={z}:  |I_quad-I_gamma|/|I| = {relA:.3e},  "
          f"|4*Fourier - (C_N+(s(s-1)/2)I_N)|/|Xi| = {relB:.3e}")

print()
print("(C): solve for constants k1, k2 in Xi_N = k1*C_N + k2*(s(s-1)/2) I_N:")
for N in (1, 3):
    zs = [mpc(2, mpf(1) / 5), mpc(9, mpf(3) / 10), mpc(21, mpf(1) / 10)]
    rows = []
    for z in zs:
        s = mpf(1) / 2 + I * z
        rows.append((C_N(N), s * (s - 1) / 2 * I_N(s, N), Xi_N_direct(z, N)))
    (A1, B1, P1), (A2, B2, P2), (A3, B3, P3) = rows
    det = A1 * B2 - A2 * B1
    k1 = (P1 * B2 - P2 * B1) / det
    k2 = (A1 * P2 - A2 * P1) / det
    resid = abs(k1 * A3 + k2 * B3 - P3) / abs(P3)
    print(f"  N={N}: k1 = {mp.nstr(k1, 25)}")
    print(f"        k2 = {mp.nstr(k2, 25)}")
    print(f"        |k1-1| = {abs(k1 - 1):.3e}, |k2-1| = {abs(k2 - 1):.3e}, rel resid@z3 = {resid:.3e}")
