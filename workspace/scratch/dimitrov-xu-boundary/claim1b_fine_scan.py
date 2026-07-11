"""Claim 1 supplement: finer scan to exclude narrow negative dips missed by
the 0.5 grid.  Normalized N(t) = B(t)/|xi(1+it)|^2 is O(1), so dps 100 is ample."""
import mpmath as mp
import common as C

mp.mp.dps = 100
def N(t):
    s = mp.mpc(1, t)
    return C.B_boundary(t) / abs(C.xi(s))**2

neg = []
minval, mint = mp.inf, None
t = mp.mpf(50)
step = mp.mpf('0.125')
while t <= 130:
    v = N(t)
    if v < minval:
        minval, mint = v, t
    if v < 0:
        neg.append(t)
    t += step
print("step 0.125 scan of N(t)=B/|xi|^2 on [50,130]:")
print("  negative points:", [mp.nstr(x,7) for x in neg])
print("  min value:", mp.nstr(minval,8), "at t =", mp.nstr(mint,7))
