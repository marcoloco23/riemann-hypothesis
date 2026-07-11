"""Stage 1: pin the normalization.

(a) Verify Xi(z) = 2 Int_0^inf Phi(u) cos(zu) du (Titchmarsh 10.1) against
    xi(1/2+iz) computed from mpmath zeta, at z = 0 and z = 2 (and z = 1+0.3i).
    The full Phi is approximated by N = 8 terms (e^{-pi*81} ~ 10^-111 truncation).
(b) Verify C_N -> 1/2 (equivalently sum_{n>=1} (4 pi n^2 - 1) e^{-pi n^2} = 1/2).
(c) Verify the classical identity
    xi(s) = 1/2 + (s(s-1)/2) Int_1^inf psi(u) (u^{s/2-1} + u^{(1-s)/2-1}) du
    numerically at s = 1/2 + 2i and s = 0.3 + 5i.
"""
from mpmath import mp, mpf, mpc, exp, pi
from xi_common import Xi_true, Xi_N_direct, Xi_N, C_N, I_N, xi_from_zeta, I

mp.dps = 40
print("=== Stage 1: normalization ===")
print(f"mp.dps = {mp.dps}")

NFULL = 8  # e^{-pi n^2 e^{2u}} <= e^{-81 pi} ~ 1e-111 for n = 9: full series to 40 dps

print("Testing claimed 'Xi(z) = 2 * Int_0^inf Phi(u) cos(zu) du' (Titchmarsh form as")
print("given in the task) against xi(1/2+iz) from mpmath zeta:")
for z in (mpf(0), mpf(2), mpc(1, mpf(3) / 10)):
    raw = Xi_N_direct(z, NFULL) / 4  # raw = Int_0^inf Phi(u) cos(zu) du
    truth = Xi_true(z)
    closed = Xi_N(z, NFULL)
    print(f"z = {z}")
    print(f"  Int Phi cos(zu) du (N={NFULL})   = {raw}")
    print(f"  claimed 2*Int                  = {2 * raw}")
    print(f"  xi(1/2+iz) via mpmath zeta     = {truth}")
    print(f"  ratio (2*Int)/xi = {2 * raw / truth}   <-- 1/2, NOT 1")
    print(f"  ratio (4*Int)/xi = {4 * raw / truth}   <-- pinned factor is 4")
    print(f"  closed form C_N+(s(s-1)/2)I_N  = {closed},  |closed-xi| = {abs(closed - truth):.3e}")
print()
print("PINNED: Xi(z) = 4 * Int_0^inf Phi(u) cos(zu) du  with the task's Phi")
print("        (the task's Phi is half of Titchmarsh's Phi).")
print("        Xi_N(z) := 4 * Int_0^inf sum_(n<=N) phi_n(u) cos(zu) du,  so Xi_N -> Xi.")

print()
print("C_N and its limit (claim: C_inf = 1/2):")
for N in (1, 2, 3, 4, 8):
    print(f"  C_{N} = {C_N(N)}")
print(f"  C_8 - 1/2 = {C_N(8) - mpf(1) / 2:.3e}")

print()
print("Classical identity xi(s) = 1/2 + (s(s-1)/2) I_inf(s):")
for s in (mpf(1) / 2 + 2 * I, mpc(3, 0) / 10 + 5 * I):
    rhs = mpf(1) / 2 + s * (s - 1) / 2 * I_N(s, NFULL)
    lhs = xi_from_zeta(s)
    print(f"  s = {s}: |lhs - rhs| = {abs(lhs - rhs):.3e}  (lhs = {lhs})")
