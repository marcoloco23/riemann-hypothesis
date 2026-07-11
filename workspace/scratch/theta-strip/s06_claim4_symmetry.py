"""Stage 6 (Claim 4): symmetries of Xi_N.

  (i)  Xi_N(-conj(z)) = conj(Xi_N(z))   (reality on the imaginary direction)
  (ii) Xi_N(-z) = Xi_N(z)               (even)
  (iii) Xi_N real on the real axis.
Consequence: zeros are symmetric under z -> -z and z -> conj(z), so scanning
the closed first quadrant suffices.
"""
from mpmath import mp, mpf, mpc
from xi_common import Xi_N

mp.dps = 40
print("=== Stage 6: claim 4, symmetry spot checks ===")
pts = [mpc(3, 1), mpc(17, mpf(1) / 4), mpc(41, 5), mpc(mpf(7) / 10, mpf(29) / 10)]
for N in (1, 2, 3, 4):
    w1 = w2 = w3 = mpf(0)
    for z in pts:
        v = Xi_N(z, N)
        w1 = max(w1, abs(Xi_N(-mp.conj(z), N) - mp.conj(v)) / abs(v))
        w2 = max(w2, abs(Xi_N(-z, N) - v) / abs(v))
    for x in (mpf(5), mpf(23), mpf(61)):
        v = Xi_N(mpc(x, 0), N)
        w3 = max(w3, abs(mp.im(v)) / abs(v))
    print(f"  N={N}: max rel |Xi(-conj z)-conj Xi(z)| = {w1:.3e}, "
          f"max rel |Xi(-z)-Xi(z)| = {w2:.3e}, max rel |Im Xi(x real)| = {w3:.3e}")

# The closed form is symmetric by construction; also confirm via the direct
# Fourier integral (independent implementation) at one point per symmetry.
from xi_common import Xi_N_direct
z = mpc(11, mpf(7) / 5)
for N in (1, 3):
    v = Xi_N_direct(z, N)
    d1 = abs(Xi_N_direct(-mp.conj(z), N) - mp.conj(v)) / abs(v)
    d2 = abs(Xi_N_direct(-z, N) - v) / abs(v)
    print(f"  [direct integral] N={N} z={z}: rel conj-sym = {d1:.3e}, rel even-sym = {d2:.3e}")
