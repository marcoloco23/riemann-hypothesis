"""Claim 3: cosh-shift identity.  With fhat(x) = int f(t) e^{-ixt} dt:
  FT[cosh(y t) nu2(t)](x)  ?=  (1/2)[nu2hat(x+iy) + nu2hat(x-iy)]  ?=  c * Re L(x+iy).
Test with the Gaussian kernel (Phi_g = e^{-u^2}, f = sqrt(pi) e^{-x^2/4}),
nu2 := C_g (the correlation of Stage A of claim 2), at (x, y) = (1.3, 0.35).

Analytic bookkeeping for the Gaussian:
  C_g(p) = sqrt(2 pi) e^{-p^2/2}          (we still integrate numerically),
  nu2hat(z) = 2 pi e^{-z^2/2},   L_g(z) = f'(z)^2 - f f'' = (pi/2) e^{-z^2/2},
  so the expected constant is c = 4.
"""
import mpmath as mp

mp.mp.dps = 35
x, y = mp.mpf('1.3'), mp.mpf('0.35')
L = mp.mpf(14)


def C_g(p):
    return mp.quad(lambda q: q**2 * mp.exp(-((p + q) / 2)**2 - ((p - q) / 2)**2),
                   [-L, 0, L])


def nu2hat(z):
    """nu2hat(z) = int C_g(t) e^{-izt} dt, numerically, complex z allowed."""
    return mp.quad(lambda t: C_g(t) * mp.exp(-mp.mpc(0, 1) * z * t), [-L, 0, L])


# LHS: FT[cosh(yt) nu2(t)](x)
lhs = mp.quad(lambda t: mp.cosh(y * t) * C_g(t) * mp.exp(-mp.mpc(0, 1) * x * t), [-L, 0, L])

# Middle: (1/2)[nu2hat(x+iy) + nu2hat(x-iy)]
mid = (nu2hat(x + mp.mpc(0, 1) * y) + nu2hat(x - mp.mpc(0, 1) * y)) / 2

# RHS: c * Re L_g(x+iy) with L_g(z) = (pi/2) e^{-z^2/2}; also compute L_g from f directly
z = x + mp.mpc(0, 1) * y
f  = mp.sqrt(mp.pi) * mp.exp(-z**2 / 4)
fp = -z / 2 * f
fpp = (z**2 / 4 - mp.mpf(1) / 2) * f
Lg = fp**2 - f * fpp
reL = mp.re(Lg)

print("(x, y) =", (mp.nstr(x, 4), mp.nstr(y, 4)))
print("LHS  FT[cosh(yt) nu2](x)            =", mp.nstr(lhs, 22))
print("MID  (1/2)[nu2hat(x+iy)+nu2hat(x-iy)] =", mp.nstr(mid, 22))
print("Re L_g(x+iy)                        =", mp.nstr(reL, 22))
print("LHS/MID rel diff  =", mp.nstr(abs(lhs - mid) / abs(mid), 3), "  (need <= 1e-15)")
print("LHS / Re L        =", mp.nstr(mp.re(lhs) / reL, 22), "  (claimed constant c; expect 4)")
print("|Im LHS| =", mp.nstr(abs(mp.im(lhs)), 3), " |Im MID| =", mp.nstr(abs(mp.im(mid)), 3))
c = mp.re(lhs) / reL
print("c - 4 =", mp.nstr(c - 4, 3))
