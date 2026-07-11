"""Claim 4: divisor-packet kill test for the notes' section-7 grouping proposal.

Atom-level even extension (RECORDED CHOICE): phi~_n(u) := phi_n(|u|) with
  phi_n(u) = (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}},  u >= 0.
The analytic formula for phi_n is NOT even; only the full sum Phi is.  We use
UNSCALED classical atoms; packet positivity is invariant under Phi -> lambda*Phi
(lambda > 0) because C_{m,n} scales by lambda^2 > 0.

Atom transforms (real, even in x, since phi~_n is real even):
  g_n(x)   = int_R phi~_n(u) e^{-ixu} du = 2 int_0^inf phi_n(u) cos(xu) du
  g_n'(x)  = -2 int_0^inf u   phi_n(u) sin(xu) du
  g_n''(x) = -2 int_0^inf u^2 phi_n(u) cos(xu) du

Derivation of the packet transform (INCLUDES the Jacobian factor 2 that the
notes' sketch omits):  C_{m,n}(p) = int q^2 phi~_m((p+q)/2) phi~_n((p-q)/2) dq;
substituting u=(p+q)/2, v=(p-q)/2 (so p=u+v, q=u-v, |Jacobian d(p,q)/d(u,v)|=2),
  FT[C_{m,n}](x) = 2 * iint (u-v)^2 phi~_m(u) phi~_n(v) e^{-ix(u+v)} du dv
                 = 2 * [ -g_m'' g_n - g_m g_n'' + 2 g_m' g_n' ].
(For m=n this is 4(g'^2 - g g''), consistent with claim 2's L = (1/4) FT[C].)
Verified below against a direct nested double integral at (m,n)=(1,1), x=3.

Divisor packets: C^(k) = sum_{mn=k} C_{m,n}.  TEST: FT[C^(k)](x) >= 0 for all
real x, k in {1,2,3,4,6}?  Scan x in [0,60] step 0.25, bisect sign changes.

Quadrature: composite Gauss-Legendre, 8 panels on [0,4], 48 nodes each
(panel error ~1e-42 even for cos(60u)); phi_n(4) ~ e^{-pi n^2 e^8} == 0.
"""
import mpmath as mp
from mpmath.calculus.quadrature import GaussLegendre
import common as C

mp.mp.dps = 45
NS = [1, 2, 3, 4, 6]
PACKETS = {1: [(1, 1)],
           2: [(1, 2), (2, 1)],
           3: [(1, 3), (3, 1)],
           4: [(1, 4), (2, 2), (4, 1)],
           6: [(1, 6), (2, 3), (3, 2), (6, 1)]}

# ---------------------------------------------------------------- fixed nodes
gl = GaussLegendre(mp.mp)
NODES = []
for i in range(8):
    a, b = mp.mpf(i) / 2, mp.mpf(i + 1) / 2
    NODES.extend(gl.get_nodes(a, b, degree=5, prec=mp.mp.prec))
U = [x for x, w in NODES]
W = [w for x, w in NODES]
PHIW = {n: [w * C.phi_atom(n, u) for u, w in NODES] for n in NS}   # w_i phi_n(u_i)


def g_trip(x):
    """Return {n: (g_n, g_n', g_n'')} at real x, sharing cos/sin tables."""
    cos = [mp.cos(x * u) for u in U]
    sin = [mp.sin(x * u) for u in U]
    out = {}
    for n in NS:
        pw = PHIW[n]
        g0 = 2 * mp.fsum(pw[i] * cos[i] for i in range(len(U)))
        g1 = -2 * mp.fsum(pw[i] * U[i] * sin[i] for i in range(len(U)))
        g2 = -2 * mp.fsum(pw[i] * U[i] ** 2 * cos[i] for i in range(len(U)))
        out[n] = (g0, g1, g2)
    return out


def ftc(trip, m, n):
    gm, gm1, gm2 = trip[m]
    gn, gn1, gn2 = trip[n]
    return 2 * (-gm2 * gn - gm * gn2 + 2 * gm1 * gn1)


def packet(x, k):
    trip = g_trip(mp.mpf(x))
    return mp.fsum(ftc(trip, m, n) for m, n in PACKETS[k])


# ------------------------------------------------------------------ validation
def validate():
    print("=== Validation ===")
    x = mp.mpf(3)
    # fixed-node g_1 vs adaptive mp.quad at x=3 and x=60
    for xx in [mp.mpf(3), mp.mpf(60)]:
        gq = 2 * mp.quad(lambda u: C.phi_atom(1, u) * mp.cos(xx * u), [0, 1, 2, 3, 4])
        gf = g_trip(xx)[1][0]
        print(f"g_1({mp.nstr(xx,3)}): fixed-node = {mp.nstr(gf, 18)},  mp.quad = {mp.nstr(gq, 18)},"
              f"  rel diff = {mp.nstr(abs(gf - gq) / abs(gq), 3)}")
    # formula vs direct nested double integral for (1,1) at x=3.
    # NB: phi~_1 has a corner at 0, so the inner integrand has kinks at q = +-p;
    # we put quadrature breakpoints there and run this validation at dps 30
    # (15+ digit agreement amply pins the structure incl. the Jacobian factor 2).
    dps_save = mp.mp.dps
    mp.mp.dps = 30
    def C11(p):
        pts = sorted({-mp.mpf(8), -abs(p), mp.mpf(0), abs(p), mp.mpf(8)})
        return mp.quad(lambda q: q**2 * C.phi_atom_even(1, (p + q) / 2)
                       * C.phi_atom_even(1, (p - q) / 2), pts)
    direct = 2 * mp.quad(lambda p: C11(p) * mp.cos(x * p), [0, 2, 4, 6, 8])  # C even
    mp.mp.dps = dps_save
    trip = g_trip(x)
    formula = ftc(trip, 1, 1)
    print(f"FT[C_11](3): direct double integral = {mp.nstr(direct, 18)}")
    print(f"             2(-2 g g'' + 2 g'^2)   = {mp.nstr(formula, 18)}")
    print(f"             rel diff = {mp.nstr(abs(direct - formula) / abs(direct), 3)}")
    # sanity: sum_n g_n = Xi/2 in the unscaled-atom convention (PHI_SCALE = 2)
    xs = mp.mpf('2.5')
    gs = mp.fsum(2 * mp.quad(lambda u: C.phi_atom(n, u) * mp.cos(xs * u), [0, 2, 4])
                 for n in range(1, 8))
    Xi = C.xi(mp.mpf(1) / 2 + mp.mpc(0, 1) * xs)
    print(f"sum_n g_n(2.5) = {mp.nstr(gs, 18)} vs Xi(2.5)/2 = {mp.nstr(mp.re(Xi) / 2, 18)},"
          f" rel diff = {mp.nstr(abs(gs - mp.re(Xi) / 2) / abs(gs), 3)}")
    # evenness/reality: g_n from cos formula is manifestly real and even (analytic note)
    print("g_n real & even in x: manifest from g_n(x) = 2 int_0^inf phi_n cos(xu) du.")
    # diagnostic: atom kink slopes phi_n'(0+) (nonzero => algebraic 1/x^2 tails)
    for n in NS:
        slope = mp.exp(-mp.pi * n**2) * (-4 * mp.pi**3 * n**6 + 15 * mp.pi**2 * n**4
                                         - mp.mpf(15) / 2 * mp.pi * n**2)
        print(f"phi_{n}'(0+) = {mp.nstr(slope, 8)}")


# ----------------------------------------------------------------------- scan
def scan():
    print("\n=== Packet scan: FT[C^(k)](x), x in [0,60], step 0.25 ===")
    xs = [mp.mpf(j) / 4 for j in range(0, 241)]
    vals = {k: [] for k in PACKETS}
    for x in xs:
        trip = g_trip(x)
        for k in PACKETS:
            vals[k].append(mp.fsum(ftc(trip, m, n) for m, n in PACKETS[k]))
    for k in PACKETS:
        v = vals[k]
        neg_idx = [i for i, y in enumerate(v) if y < 0]
        print(f"\n-- k = {k}:  value at x=0: {mp.nstr(v[0], 10)};  min over grid: "
              f"{mp.nstr(min(v), 10)} at x = {mp.nstr(xs[v.index(min(v))], 6)}")
        if not neg_idx:
            print(f"   no negative grid value on [0,60] (grid step 0.25)")
            continue
        i0 = neg_idx[0]
        a, b = xs[i0 - 1], xs[i0]
        root = mp.findroot(lambda x: packet(x, k), (a, b), solver='bisect',
                           tol=mp.mpf(10) ** (-25))
        print(f"   FIRST negative grid point: x = {mp.nstr(xs[i0], 6)}, value {mp.nstr(v[i0], 8)}")
        print(f"   first sign crossing (bisected): x* = {mp.nstr(root, 12)}")
        # sample a few negative values
        for i in neg_idx[:3]:
            print(f"     x={mp.nstr(xs[i],6)}: {mp.nstr(v[i], 8)}")
        print(f"   number of negative grid points on [0,60]: {len(neg_idx)}")


if __name__ == '__main__':
    validate()
    scan()
