"""Stage 3 (Claim 1): polish the specific claimed zeros of Xi_1 and Xi_2.

Claimed (Haglund):
  Xi_1: real zero ~ 14.04543958; complex zeros ~ 20.62534601+2.69715184i,
        26.05616693+7.12535971i.
  Xi_2: first nonreal zero ~ 43.13890807+3.28097100i.
Polish with mp.findroot (Muller), report 15 digits, and the residual |Xi_N|.
"""
from mpmath import mp, mpf, mpc
from xi_common import Xi_N

mp.dps = 40
print("=== Stage 3: claim 1 zero locations ===")

cases = [
    (1, mpc(14.04543958, 0), "Xi_1 real zero"),
    (1, mpc(20.62534601, 2.69715184), "Xi_1 first complex zero"),
    (1, mpc(26.05616693, 7.12535971), "Xi_1 second complex zero"),
    (2, mpc(43.13890807, 3.28097100), "Xi_2 first nonreal zero (claimed)"),
]
for N, seed, label in cases:
    seeds = (seed, seed + mpf(10) ** -4, seed + mpc(0, 1) * mpf(10) ** -4)
    root = mp.findroot(lambda z: Xi_N(z, N), seeds, solver="muller", tol=mpf(10) ** -50)
    resid = abs(Xi_N(root, N))
    print(f"  {label}:")
    print(f"    seed  = {seed}")
    print(f"    root  = {mp.nstr(root, 20)}")
    print(f"    |Xi_N(root)| = {resid:.3e},  |root - seed| = {abs(root - seed):.3e}")
