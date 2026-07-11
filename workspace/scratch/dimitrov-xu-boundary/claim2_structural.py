"""Claim 2: structural identity  L(x) = (1/4) FT[C](x)  for real x, where
  C(p) = int_R q^2 Phi_c((p+q)/2) Phi_c((p-q)/2) dq,
  Xi(x) = int_R Phi_c(u) e^{-ixu} du   (OUR convention; Phi_c = 2*Phi_classical,
  pinned numerically in sanity.py: Xi(x) = 4 int_0^inf Phi_classical cos(xu) du).

Stage A: Gaussian test kernel Phi_g(u)=e^{-u^2}, f(x)=sqrt(pi) e^{-x^2/4}:
  check f'^2 - f f'' = (1/4) int C_g(p) e^{-ixp} dp to 15 digits, x in {0.7, 2.1},
  with C_g computed by NUMERICAL inner integration (no analytic shortcut).
Stage B: Riemann kernel spot check at x=5, dps 50: L(5) (from zeta machinery)
  vs (1/4) * nested numerical double integral.
Stage C: C(p) > 0 at p in {0,1,3};  C''(0) < 0 (central differences + Richardson).
"""
import mpmath as mp
import common as C


# ------------------------------------------------------------ Stage A: Gaussian
def stage_A():
    mp.mp.dps = 35
    print("=== Stage A: Gaussian kernel Phi_g(u) = e^{-u^2} ===")
    L = mp.mpf(13)  # e^{-p^2/2} < 1e-36 for |p| > 12.9

    def C_g(p):
        return mp.quad(lambda q: q**2 * mp.exp(-((p + q) / 2)**2 - ((p - q) / 2)**2),
                       [-L, 0, L])

    for x in [mp.mpf('0.7'), mp.mpf('2.1')]:
        f = mp.sqrt(mp.pi) * mp.exp(-x**2 / 4)
        fp = -x / 2 * f
        fpp = (x**2 / 4 - mp.mpf(1) / 2) * f
        lhs = fp**2 - f * fpp
        # FT of even real C_g: int_R C_g e^{-ixp} dp = 2 int_0^inf C_g cos(xp) dp
        rhs = mp.mpf(1) / 4 * 2 * mp.quad(lambda p: C_g(p) * mp.cos(x * p), [0, 3, 7, L])
        print(f"x={mp.nstr(x,3)}: LHS f'^2-ff''      = {mp.nstr(lhs, 20)}")
        print(f"        (1/4) FT[C_g](x) = {mp.nstr(rhs, 20)}")
        print(f"        rel diff = {mp.nstr(abs(lhs - rhs) / abs(lhs), 3)}   (need <= 1e-15)")


# ---------------------------------------------------- Stage B: Riemann kernel x=5
def stage_B():
    mp.mp.dps = 50
    print("\n=== Stage B: Riemann kernel, x = 5, dps 50 ===")
    # L(5) = xi(s) xi''(s) - xi'(s)^2 at s = 1/2 + 5i, via zeta machinery
    lhs = C.L_of_z(mp.mpf(5))
    print("L(5) via zeta machinery  =", mp.nstr(lhs, 25), " (imag part =", mp.nstr(mp.im(lhs), 3), ")")

    UCUT = mp.mpf('2.4')   # Phi(u) < 1e-100 beyond; integrand support |p|,|q| <= 2*UCUT

    def C_R(p):
        # inner integrand supported where |p+q|/2, |p-q|/2 <= UCUT
        qmax = 2 * UCUT
        return mp.quad(lambda q: q**2 * C.Phi_conv((p + q) / 2) * C.Phi_conv((p - q) / 2),
                       [-qmax, -2, 0, 2, qmax])

    x = mp.mpf(5)
    pmax = 2 * UCUT
    rhs = mp.mpf(1) / 4 * 2 * mp.quad(lambda p: C_R(p) * mp.cos(x * p), [0, 1, 2, 3, 4, pmax])
    print("(1/4) FT[C](5) numerical =", mp.nstr(rhs, 25))
    print("rel diff =", mp.nstr(abs(mp.re(lhs) - rhs) / abs(rhs), 3))
    return C_R


# ------------------------------------- Stage C: positivity / concavity of C(p)
def stage_C(C_R):
    mp.mp.dps = 50
    print("\n=== Stage C: C(p) > 0 at p in {0,1,3};  C''(0) < 0 ===")
    vals = {}
    for p in [mp.mpf(0), mp.mpf(1), mp.mpf(3)]:
        vals[p] = C_R(p)
        print(f"C({mp.nstr(p,2)}) = {mp.nstr(vals[p], 20)}   positive: {vals[p] > 0}")
    c0 = vals[mp.mpf(0)]
    # C even => C''(0) ~ 2(C(h)-C(0))/h^2; Richardson with h, h/2
    h = mp.mpf('0.1')
    D  = 2 * (C_R(h) - c0) / h**2
    D2 = 2 * (C_R(h / 2) - c0) / (h / 2)**2
    rich = (4 * D2 - D) / 3
    print(f"C''(0) fd estimates: D(h=0.1) = {mp.nstr(D, 12)}, D(h=0.05) = {mp.nstr(D2, 12)},"
          f" Richardson = {mp.nstr(rich, 12)}   negative: {rich < 0}")


if __name__ == '__main__':
    stage_A()
    C_R = stage_B()
    stage_C(C_R)
