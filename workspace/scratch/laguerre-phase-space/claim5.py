"""Claim 5: C_Xi(x,y) = |Xi'(x+iy)|^2 - Re( Xi(x+iy) conj(Xi''(x+iy)) ) >= 0
on the grid x in {0, 5, 14.1347, 21.02, 25}, y in {0.1, 0.5, 1, 2},
plus x = 7005.063, y = 0.05 (near the Lehmer pair).

Derivatives at complex z via the trapezoidal Cauchy rule (common.cauchy_derivs,
with built-in N-doubling validation); at the Lehmer point additionally checked
against central differences with step halving.  We do NOT use mpmath's
diff(method='quad') here: it silently returns coarse radius-dependent values
for tiny-magnitude integrands (|Xi| ~ 1e-2385 at t ~ 7005) because quadts's
stopping rule is effectively absolute.  See run-output.txt.
"""
import time
import mpmath as mp
from common import Xi, cauchy_derivs

print("=" * 72)
print("CLAIM 5 -- C_Xi(x,y) on grid + Lehmer-pair point")
print("=" * 72)

mp.mp.dps = 40


def C_Xi_cauchy(z, radius, N=64):
    X0, X1, X2 = cauchy_derivs(Xi, z, 2, radius, N=N)
    return abs(X1) ** 2 - (X0 * mp.conj(X2)).real


print("\nGrid (dps = 40, trapezoid Cauchy derivatives, radius 0.5, N-doubling checked):")
print(f"{'x':>10} {'y':>6}  {'C_Xi(x,y)':>28}  sign")
neg = []
for xs in ['0', '5', '14.1347', '21.02', '25']:
    for ys in ['0.1', '0.5', '1', '2']:
        z = mp.mpc(mp.mpf(xs), mp.mpf(ys))
        c = C_Xi_cauchy(z, radius=0.5)
        print(f"{xs:>10} {ys:>6}  {mp.nstr(c, 15):>28}  {'>=0 OK' if c >= 0 else 'NEGATIVE!'}")
        if c < 0:
            neg.append((xs, ys, c))

print("\nLehmer-pair point x = 7005.063, y = 0.05 (dps = 45, central differences):")
mp.mp.dps = 45
t0 = time.time()
z = mp.mpc(mp.mpf('7005.063'), mp.mpf('0.05'))


def C_Xi_fd(z, h):
    fp, f0, fm = Xi(z + h), Xi(z), Xi(z - h)
    X1 = (fp - fm) / (2 * h)
    X2 = (fp - 2 * f0 + fm) / h ** 2
    return abs(X1) ** 2 - (f0 * mp.conj(X2)).real


h = mp.mpf('1e-8')
c1 = C_Xi_fd(z, h)
c2 = C_Xi_fd(z, h / 2)   # step-halving consistency check
c3 = C_Xi_cauchy(z, radius=0.05)   # independent method (trapezoid Cauchy)
elapsed = time.time() - t0
rel = abs(c1 - c2) / abs(c1)
relm = abs(c1 - c3) / abs(c1)
print(f"  C_Xi (central diff, h = 1e-8) = {mp.nstr(c1, 20)}")
print(f"  C_Xi (central diff, h = 5e-9) = {mp.nstr(c2, 20)}")
print(f"  C_Xi (trapezoid Cauchy r=.05) = {mp.nstr(c3, 20)}")
print(f"  step-halving rel. consistency = {mp.nstr(rel, 3)}")
print(f"  cross-method rel. consistency = {mp.nstr(relm, 3)}")
print(f"  |Xi(z)| = {mp.nstr(abs(Xi(z)), 6)}  (scale check; values are ~1e-3050 range)")
print(f"  sign: {'>= 0 OK' if c1 >= 0 else 'NEGATIVE!'}   [{elapsed:.1f} s]")
if c1 < 0:
    neg.append(('7005.063', '0.05', c1))

print()
if neg:
    print("NEGATIVE VALUES FOUND (debug before believing -- see instructions):")
    for xs, ys, c in neg:
        print(f"  x={xs}, y={ys}: {mp.nstr(c, 20)}")
else:
    print("All C_Xi values >= 0 (strictly positive). Consistent with RH-necessity. PASS")
