"""Stage 5 (Claim 3, KEY): Xi_N(z) != 0 for 0 < Im z < 1/2, tested for N = 1..4.

Coverage per N (X_N = 1.5 * 4(N+1)^2 + 50):
  (a) STRIP boxes  [x0,x1] x [0.02, 0.48], x in [-0.5, X_N] in widths <= 35:
      zero count by numerical contour integration of Xi_N'/Xi_N (mp.quad,
      derivative by central difference) AND independently by adaptive
      phase-tracking winding number.  Distance from nearest integer reported.
  (b) NEAR-REAL boxes [x0,x1] x [-0.02, 0.02]: count must equal the number of
      real zeros found in stage 4 (zeros come in conjugate pairs, so equality
      excludes complex zeros with 0 < |Im z| < 0.02).
  (c) GAP+UPPER box [-0.5, X_N] x [0.48, 12.03]: phase-tracking count, then all
      zeros located by |Xi_N| grid minima + findroot; located count must match.
      Covers the gap Im in [0.48, 0.5) and gives min Im of complex zeros.
  (d) Reality check: findroot from x_k + 0.01i for every stage-4 real zero;
      report max |Im| of the converged roots.

Evaluations are cancellation-aware: Xi_N(z) = C_N + (s(s-1)/2)I_N has scale
~0.5, so when |Xi_N(z)| ~ 1e-k the working precision is raised to k + 30.
"""
import sys
import time
from mpmath import mp, mpf, mpc, pi, arg, ceil
from xi_common import Xi_N

I = mpc(0, 1)
BASE_DPS = 30


def xi_eval(z, N):
    v = Xi_N(z, N)
    if abs(v) > 0:
        needed = int(mp.log10(mpf(1) / abs(v))) + 30
    else:
        needed = mp.dps + 30
    if needed > mp.dps:
        old = mp.dps
        mp.dps = needed
        v = Xi_N(z, N)
        mp.dps = old
    return v


def dxi_eval(z, N, h=mpf(10) ** -8):
    return (xi_eval(z + h, N) - xi_eval(z - h, N)) / (2 * h)


# ---------- adaptive phase-tracking winding number ----------
class PhaseTracker:
    def __init__(self, N, tol=mpf(8) / 10, maxdepth=48):
        self.N, self.tol, self.maxdepth = N, tol, maxdepth
        self.evals = 0
        self.minabs = mp.inf
        self.depth_hit = False

    def f(self, z):
        self.evals += 1
        v = xi_eval(z, self.N)
        if abs(v) < self.minabs:
            self.minabs = abs(v)
        return v

    def seg(self, p0, v0, p1, v1, depth):
        d = arg(v1 / v0)
        if abs(d) <= self.tol:
            return d
        if depth >= self.maxdepth:
            self.depth_hit = True
            return d
        pm = (p0 + p1) / 2
        vm = self.f(pm)
        return self.seg(p0, v0, pm, vm, depth + 1) + self.seg(pm, vm, p1, v1, depth + 1)

    def edge(self, za, zb, max_step):
        n = max(1, int(ceil(abs(zb - za) / max_step)))
        pts = [za + (zb - za) * k / n for k in range(n + 1)]
        vals = [self.f(p) for p in pts]
        return sum(self.seg(pts[k], vals[k], pts[k + 1], vals[k + 1], 0)
                   for k in range(n))


def count_phase(N, x0, x1, y0, y1, max_step=mpf(1) / 4):
    tr = PhaseTracker(N)
    corners = [mpc(x0, y0), mpc(x1, y0), mpc(x1, y1), mpc(x0, y1), mpc(x0, y0)]
    tot = sum(tr.edge(corners[k], corners[k + 1], max_step) for k in range(4))
    return tot / (2 * pi), tr


# ---------- quadrature of Xi'/Xi ----------
def count_quad(N, x0, x1, y0, y1, zero_xs):
    corners = [mpc(x0, y0), mpc(x1, y0), mpc(x1, y1), mpc(x0, y1), mpc(x0, y0)]
    tot = mpc(0)
    for k in range(4):
        za, zb = corners[k], corners[k + 1]
        L = zb - za
        ts = [mpf(0), mpf(1)]
        if k in (0, 2):  # horizontal edges: divide at real-zero abscissas
            lo, hi = (x0, x1) if k == 0 else (x1, x0)
            for x in zero_xs:
                t = (x - lo) / (hi - lo)
                if 0 < t < 1:
                    ts.append(t)
        ts = sorted(set(ts))
        tot += mp.quad(lambda t: dxi_eval(za + t * L, N) * L / xi_eval(za + t * L, N),
                       ts, maxdegree=7)
    val = tot / (2 * pi * I)
    return val


def nearest_int_info(x):
    n = int(mp.nint(x))
    return n, abs(x - n)


def main():
    mp.dps = BASE_DPS
    print("=== Stage 5: claim 3 (finite theta-strip conjecture), N = 1..4 ===")
    print(f"base dps = {BASE_DPS}; cancellation-aware precision raising enabled")

    Ns = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4]
    for N in Ns:
        t0 = time.time()
        X_N = mpf(15) / 10 * 4 * (N + 1) ** 2 + 50
        zeros = [mp.mpf(l.strip()) for l in open(f"realzeros_{N}.txt")]
        print(f"\n--- N = {N}:  scan region Re in [-0.5, {float(X_N)}] ---")

        # strip boxes
        edges = [mpf(-1) / 2]
        while edges[-1] < X_N:
            edges.append(min(edges[-1] + 35, X_N))
        y0, y1 = mpf(2) / 100, mpf(48) / 100
        total_strip = 0
        for x0, x1 in zip(edges[:-1], edges[1:]):
            cq = count_quad(N, x0, x1, y0, y1, zeros)
            nq, dq = nearest_int_info(cq.real)
            cp, tr = count_phase(N, x0, x1, y0, y1)
            nph, dp = nearest_int_info(cp)
            total_strip += nq
            flag = "" if (nq == 0 and nph == 0) else "  <-- NONZERO COUNT"
            print(f"  strip [{float(x0)},{float(x1)}]x[0.02,0.48]: "
                  f"quad count = {mp.nstr(cq.real, 8)} (nearest {nq}, dist {dq:.1e}, "
                  f"|Im| {abs(cq.imag):.1e}); "
                  f"phase count = {mp.nstr(cp, 8)} (nearest {nph}, dist {dp:.1e}, "
                  f"{tr.evals} evals, min|Xi| {tr.minabs:.1e})"
                  f"{' [depth hit]' if tr.depth_hit else ''}{flag}")

        # near-real boxes
        print("  near-real boxes [x0,x1]x[-0.02,0.02] (count must equal # real zeros):")
        for x0, x1 in zip(edges[:-1], edges[1:]):
            nreal = sum(1 for x in zeros if x0 < x < x1)
            cp, tr = count_phase(N, x0, x1, mpf(-2) / 100, mpf(2) / 100)
            npc, dpc = nearest_int_info(cp)
            ok = "OK" if npc == nreal else "MISMATCH <-- possible near-real complex zeros"
            print(f"    [{float(x0)},{float(x1)}]: count = {mp.nstr(cp, 8)} "
                  f"(nearest {npc}, dist {dpc:.1e}), real zeros = {nreal}  [{ok}]")

        # reality of real zeros
        maxim = mpf(0)
        for x in zeros:
            seed = mpc(x, mpf(1) / 100)
            seeds = (seed, seed + mpf(10) ** -4, seed + I * mpf(10) ** -4)
            r = mp.findroot(lambda z: xi_eval(z, N), seeds, solver="muller",
                            tol=mpf(10) ** -40)
            maxim = max(maxim, abs(mp.im(r)))
        print(f"  reality check: max |Im| over {len(zeros)} polished 'real' zeros "
              f"(seeded x_k+0.01i) = {maxim:.3e}")

        # gap+upper box and complex-zero location
        yu0, yu1 = mpf(48) / 100, mpf(1203) / 100
        cp, tr = count_phase(N, mpf(-1) / 2, X_N, yu0, yu1)
        nup, dup = nearest_int_info(cp)
        print(f"  upper box [-0.5,{float(X_N)}]x[0.48,12.03]: phase count = "
              f"{mp.nstr(cp, 8)} (nearest {nup}, dist {dup:.1e}, {tr.evals} evals)")

        # grid search for zeros in the upper box
        gx, gy = mpf(1) / 2, mpf(1) / 4
        nx = int((X_N + mpf(1) / 2) / gx) + 1
        ny = int((yu1 - yu0) / gy) + 1
        vals = {}
        for i in range(nx + 1):
            for j in range(ny + 1):
                z = mpc(mpf(-1) / 2 + i * gx, yu0 + j * gy)
                vals[(i, j)] = abs(Xi_N(z, N))
        cands = []
        for i in range(1, nx):
            for j in range(1, ny):
                v = vals[(i, j)]
                if all(v <= vals[(i + di, j + dj)]
                       for di in (-1, 0, 1) for dj in (-1, 0, 1)
                       if (di, dj) != (0, 0)):
                    cands.append(mpc(mpf(-1) / 2 + i * gx, yu0 + j * gy))
        roots = []
        for c in cands:
            try:
                seeds = (c, c + mpf(10) ** -3, c + I * mpf(10) ** -3)
                r = mp.findroot(lambda z: xi_eval(z, N), seeds, solver="muller",
                                tol=mpf(10) ** -40)
            except Exception:
                continue
            if not (mpf(-1) / 2 < r.real < X_N and yu0 < r.imag < yu1):
                continue
            if abs(xi_eval(r, N)) > mpf(10) ** -20:
                continue
            if all(abs(r - r2) > mpf(10) ** -6 for r2 in roots):
                roots.append(r)
        roots.sort(key=lambda r: (r.real, r.imag))
        match = "MATCH" if len(roots) == nup else "MISMATCH (grid may have missed zeros)"
        print(f"  located {len(roots)} zeros in upper box vs count {nup}  [{match}]")
        for r in roots[:8]:
            print(f"    zero: {mp.nstr(r, 15)}")
        if len(roots) > 8:
            print(f"    ... ({len(roots) - 8} more)")
        if roots:
            minim = min(r.imag for r in roots)
            print(f"  MIN Im among located complex zeros (N={N}): {mp.nstr(minim, 12)}")
        print(f"  strip total count N={N}: {total_strip}   "
              f"[claim 3 {'SUPPORTED' if total_strip == 0 else 'VIOLATED'}"
              f" in scanned region]   ({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    main()
