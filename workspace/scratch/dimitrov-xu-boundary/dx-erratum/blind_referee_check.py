"""Referee verification of arXiv:1606.05011 (Dimitrov-Xu, Wronskians of Fourier
and Laplace transforms). All computations at 50 dps with mpmath."""
import mpmath as mp
mp.mp.dps = 50

print("=" * 72)
print("A. Theorem 2.5(1) factor check, n=2, f = chi_[-1,1]")
print("=" * 72)
# nu_2(f;t) = int (t-2s)^2 f(s) f(t-s) ds ; paper says = (1/3)(2-|t|)^3
def nu2_chi(t):
    t = mp.mpf(t)
    if abs(t) > 2: return mp.mpf(0)
    a, b = max(-1, t - 1), min(1, t + 1)
    return mp.quad(lambda s: (t - 2*s)**2, [a, b])
for t in [0, 0.5, 1.3]:
    print(f"  nu2({t}) direct = {nu2_chi(t)},  (1/3)(2-|t|)^3 = {(mp.mpf(2)-abs(mp.mpf(t)))**3/3}")

# W2(Ff;x) vs F(nu2)(x):  paper claims W2 = -F(nu2); I claim W2 = -(1/2) F(nu2)
def Fchi(x): return 2*mp.sin(x)/x
def W2_of(g, x, h=None):
    g0 = g(x); g1 = mp.diff(g, x, 1); g2 = mp.diff(g, x, 2)
    return g0*g2 - g1**2
def FT_nu2_chi(x):
    return 2*mp.quad(lambda t: nu2_chi(t)*mp.cos(x*t), [0, 2])
for x in [0.7, 2.3]:
    w2 = W2_of(Fchi, mp.mpf(x))
    ft = FT_nu2_chi(mp.mpf(x))
    print(f"  x={x}: W2(Ff)={mp.nstr(w2,12)}  F(nu2)={mp.nstr(ft,12)}  ratio W2/F(nu2) = {mp.nstr(w2/ft,12)}")
print("  -> paper predicts ratio -1 ; correct value is -1/2")

print()
print("=" * 72)
print("B. Proposition 2.9 constant (Gaussian), n=2 and n=3; and sign for n=3")
print("=" * 72)
g = lambda s: mp.e**(-s**2/2)
# n=2 direct: nu2(0) = int (2s)^2 g(s)g(-s) ds
nu2_gauss_0 = mp.quad(lambda s: (2*s)**2 * g(s)*g(-s), [-mp.inf, mp.inf])
print(f"  nu2(gauss;0) direct = {mp.nstr(nu2_gauss_0,12)}")
print(f"  paper a_2           = {mp.nstr(mp.sqrt(mp.pi),12)}   (sqrt(pi))")
print(f"  2*sqrt(pi)          = {mp.nstr(2*mp.sqrt(mp.pi),12)}   <- n! * paper value")
# n=3 direct: nu3(t) = int int prod (s_i-s_j)^2 g g g ds1 ds2, s3 = t-s1-s2 ; at t=0
def nu3_gauss(t):
    t = mp.mpf(t)
    def inner(s1, s2):
        s3 = t - s1 - s2
        return ((s1-s2)*(s1-s3)*(s2-s3))**2 * g(s1)*g(s2)*g(s3)
    return mp.quad(inner, [-8, 8], [-8, 8])
n3 = nu3_gauss(0)
a3_paper = (1/mp.sqrt(3))*(2*mp.pi)**1 * (mp.factorial(1)*mp.factorial(2))
print(f"  nu3(gauss;0) direct = {mp.nstr(n3,12)}")
print(f"  paper a_3           = {mp.nstr(a3_paper,12)}")
print(f"  ratio direct/paper  = {mp.nstr(n3/a3_paper,12)}   (should be 3! = 6 if factor n! missing)")
# n=3 sign check: W3(Fg;x) vs F(nu3)(x). paper sign (-1)^{n(n+1)/2}=+1; mine (-1)^{n(n-1)/2}=-1, factor 1/6
def Fgauss(x): return mp.sqrt(2*mp.pi)*mp.e**(-x**2/2)
def W3_of(gg, x):
    d = [mp.diff(gg, x, k) for k in range(5)]
    M = mp.matrix([[d[0], d[1], d[2]], [d[1], d[2], d[3]], [d[2], d[3], d[4]]])
    return mp.det(M)
x0 = mp.mpf('0.9')
w3 = W3_of(Fgauss, x0)
# nu3 is a_true * exp(-t^2/6); a_true from direct at 0
FTnu3 = 2*mp.quad(lambda t: n3*mp.e**(-t**2/6)*mp.cos(x0*t), [0, mp.inf])
print(f"  x=0.9: W3(Fgauss) = {mp.nstr(w3,12)},  F(nu3) = {mp.nstr(FTnu3,12)}")
print(f"  ratio = {mp.nstr(w3/FTnu3,12)}   (paper: +1 ; my derivation: -1/6)")

print()
print("=" * 72)
print("C. DECISIVE: Corollary 4.3(b): FT of cosh(yt)(2-|t|)^3 on [-2,2]")
print("   Paper claims translates dense in L1 for EVERY y  <=>  FT has NO real zero")
print("=" * 72)
def FT_printed_kernel(x, y):
    # 2 * int_0^2 cosh(yt) (2-t)^3 cos(xt) dt   (evenness)
    return 2*mp.quad(lambda t: mp.cosh(y*t)*(2-t)**3*mp.cos(x*t), [0, 2])
def closed_form(x, y):
    # should equal 3 * Re[ 8 (z^2 - sin^2 z)/z^4 ] at z = x+iy  (kernel = 3 * nu2)
    z = mp.mpc(x, y)
    return mp.re(3 * 8*(z**2 - mp.sin(z)**2)/z**4)
# consistency of closed form
for (x, y) in [(1.1, 0.7), (4.2, 2.0)]:
    print(f"  check closed form (x={x},y={y}): quad={mp.nstr(FT_printed_kernel(x,y),12)}  Re-formula={mp.nstr(closed_form(x,y),12)}")
# scan for sign changes
for y in [mp.mpf('0.5'), mp.mpf(1), mp.mpf(2), mp.mpf(3)]:
    prev_x, prev_v = None, None
    changes = []
    x = mp.mpf('0.05')
    while x < 25:
        v = closed_form(x, y)
        if prev_v is not None and v*prev_v < 0:
            root = mp.findroot(lambda xx: closed_form(xx, y), (prev_x + x)/2)
            changes.append(root)
        prev_x, prev_v = x, v
        x += mp.mpf('0.05')
    if changes:
        print(f"  y={y}: SIGN CHANGES of FT at x ~ {[mp.nstr(r,10) for r in changes[:6]]}")
        r = changes[0]
        for dx in [-0.3, 0.3]:
            print(f"      FT({mp.nstr(r+dx,8)},{y}) = {mp.nstr(FT_printed_kernel(r+dx,y),12)} (direct quadrature)")
    else:
        print(f"  y={y}: no sign change found on (0,25)")

print()
print("=" * 72)
print("D. Corrected kernel H_y(t) = int (t-2s)^2 cosh((t-2s)y) K(s)K(t-s) ds, K=chi")
print("   Claim: FT(H_y)(x) = 2[|phi'|^2 - Re(phi conj(phi''))] at z=x+iy > 0")
print("=" * 72)
def H_y(t, y):
    t = mp.mpf(t)
    if abs(t) > 2: return mp.mpf(0)
    t = abs(t)
    # = int_0^{2-t} u^2 cosh(u y) du
    return mp.quad(lambda u: u**2*mp.cosh(u*y), [0, 2-t])
def FT_H(x, y):
    return 2*mp.quad(lambda t: H_y(t, y)*mp.cos(x*t), [0, 2])
def jensen(x, y):
    z = mp.mpc(x, y)
    f = lambda w: 2*mp.sin(w)/w
    f1 = mp.diff(f, z, 1); f0 = f(z); f2 = mp.diff(f, z, 2)
    return 2*(abs(f1)**2 - mp.re(f0*mp.conj(f2)))
mins = []
for y in [mp.mpf(1), mp.mpf(2), mp.mpf(3)]:
    vals = []
    for xi in [0.5, 2.0, 4.0, 6.5, 9.0, 12.0, 15.0, 20.0]:
        ft = FT_H(xi, y); jn = jensen(xi, y)
        vals.append((xi, ft, jn))
    worst = min(v[1] for v in vals)
    agree = max(abs(v[1]-v[2])/abs(v[2]) for v in vals)
    print(f"  y={y}: min FT(H_y) over sample = {mp.nstr(worst,10)} (>0?), max rel-diff FT vs Jensen = {mp.nstr(agree,6)}")

print()
print("=" * 72)
print("E. Riemann Xi itself: printed kernel Phi_2y FT = 2*Re[(Xi')^2 - Xi Xi''](x+iy)")
print("   vs corrected 2[|Xi'|^2 - Re(Xi conj Xi'')]; y = 0.4, scan x")
print("=" * 72)
def Xi(z):
    s = mp.mpf('0.5') + 1j*z
    return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def printedXi(x, y):
    z = mp.mpc(x, y)
    X0 = Xi(z); X1 = mp.diff(Xi, z, 1); X2 = mp.diff(Xi, z, 2)
    return 2*mp.re(X1**2 - X0*X2)
def correctedXi(x, y):
    z = mp.mpc(x, y)
    X0 = Xi(z); X1 = mp.diff(Xi, z, 1); X2 = mp.diff(Xi, z, 2)
    return 2*(abs(X1)**2 - mp.re(X0*mp.conj(X2)))
y = mp.mpf('0.4')
prev = None; prev_x = None; found = []
x = mp.mpf('0.2')
while x <= 40:
    v = printedXi(x, y)
    if prev is not None and v*prev < 0:
        found.append(((prev_x+x)/2, prev, v))
    prev, prev_x = v, x
    x += mp.mpf('0.4')
if found:
    for (xr, a, b) in found[:8]:
        root = mp.findroot(lambda xx: printedXi(xx, y), xr)
        print(f"  printed-kernel FT sign change near x={mp.nstr(root,10)} (values {mp.nstr(a,6)} -> {mp.nstr(b,6)})")
        print(f"     corrected (Jensen) value there: {mp.nstr(correctedXi(root,y),8)}  (should be > 0)")
else:
    print("  no sign change of printed quantity found for y=0.4, x in (0,40)")
# also check corrected positivity on the scan
minc = min(correctedXi(mp.mpf(xx)/10, y) for xx in range(2, 401, 4))
print(f"  min of corrected Jensen quantity over scan = {mp.nstr(minc,8)}")
