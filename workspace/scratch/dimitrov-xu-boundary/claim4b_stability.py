"""Claim 4 stability check: recompute the reported negative packet values at
dps 70 with a finer panelization (16 panels x 48 nodes on [0,4]) and compare."""
import mpmath as mp
from mpmath.calculus.quadrature import GaussLegendre
import common as C

mp.mp.dps = 70
NS = [1, 2, 3, 4, 6]
PACKETS = {1: [(1,1)], 2: [(1,2),(2,1)], 3: [(1,3),(3,1)],
           4: [(1,4),(2,2),(4,1)], 6: [(1,6),(2,3),(3,2),(6,1)]}
gl = GaussLegendre(mp.mp)
NODES = []
for i in range(16):
    a, b = mp.mpf(i)/4, mp.mpf(i+1)/4
    NODES.extend(gl.get_nodes(a, b, degree=5, prec=mp.mp.prec))
U = [x for x, w in NODES]
PHIW = {n: [w * C.phi_atom(n, u) for u, w in NODES] for n in NS}

def packet(k, x):
    x = mp.mpf(x)
    cos = [mp.cos(x*u) for u in U]; sin = [mp.sin(x*u) for u in U]
    t = {}
    for n in NS:
        pw = PHIW[n]
        t[n] = (2*mp.fsum(pw[i]*cos[i] for i in range(len(U))),
                -2*mp.fsum(pw[i]*U[i]*sin[i] for i in range(len(U))),
                -2*mp.fsum(pw[i]*U[i]**2*cos[i] for i in range(len(U))))
    return mp.fsum(2*(-t[m][2]*t[n][0] - t[m][0]*t[n][2] + 2*t[m][1]*t[n][1])
                   for m, n in PACKETS[k])

checks = [(1, '19.75', '-3.674612558e-9'), (2, '8.5', '-1.395784649e-6'),
          (3, '8.25', '-6.146854177e-13'), (4, '33.0', '-1.402797315e-12'),
          (6, '29.0', '-2.771038793e-18')]
print("dps-70 / 16-panel recomputation of reported packet minima (dps-45/8-panel values in parens):")
for k, xs, ref in checks:
    v = packet(k, xs)
    print(f"  k={k}, x={xs}: {mp.nstr(v, 15)}   (was {ref});  rel diff = "
          f"{mp.nstr(abs(v - mp.mpf(ref))/abs(v), 3)}")
