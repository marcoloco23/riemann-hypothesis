"""Front-law study: shared machinery for enumerating complex zeros of Xi_N.

Reuses the validated closed form in ../xi_common.py (normalization pinned there:
Xi_N(z) = 4 * Int_0^inf sum_{n<=N} phi_n(u) cos(zu) du = C_N + (s(s-1)/2) I_N(s),
s = 1/2 + iz).

KEY NUMERICAL FACT driving the design: in the bulk (x below the real-zero front
R_N ~ 4(N+1)^2) |Xi_N(x+iy)| ~ e^{-pi x/4} (it tracks Xi), and past the front it
sits on a floor ~ e^{-pi (N+1)^2} (truncation-tail scale).  Measured examples:
|Xi_8(300+0.5i)| ~ 3e-98, floor for N=8 ~ 1e-108.  Since Xi_N is assembled from
terms of size ~ |z|^2, evaluation suffers catastrophic cancellation and the
working precision must adapt: dps ~ 0.3413*x + 35, capped at
pi (N+1)^2 / ln 10 + 45.  The Eval class below does this per point, verifying
|value| >> (term scale) * 10^{5-dps} before trusting a phase or a sign.

Zero counting: adaptive phase-tracking winding number (exact argument principle,
(1/2pi) * total continuous change of arg Xi_N around the box; equals the contour
integral of Xi_N'/Xi_N / 2 pi i).  A contour point whose value cannot be
resolved above the error bound (zero on/near the contour) raises BadContour and
the caller shifts the offending edge.

Zero location: count-guided bisection (split a count-k box until count <= 1,
verifying child counts sum to the parent count), then Muller iteration in each
count-1 box, then a high-precision polish with residual verification against
the local scale.  Located count therefore equals the argument-principle count
by construction -- this removes the dedup/false-accept failure mode of the
earlier locator (absolute residual threshold 1e-20 on a function whose local
scale is ~1e-30 accepted 640 non-zeros; see ../out_s05_N234.txt N=4).

All computations deterministic (mpmath; fixed seeds/steps; no randomness).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mpmath import mp, mpf, mpc, pi, arg  # noqa: E402
import xi_common as xc  # noqa: E402

mp.dps = 60  # ambient precision for geometry (box corners, bisection points)

IU = mpc(0, 1)
LOG10 = mpf('2.302585092994045684017991454684364207601101488628772976033')


def floor_digits(N):
    """Digits of the past-front floor |Xi_N| ~ e^{-pi (N+1)^2}."""
    return float(pi) * (N + 1) ** 2 / 2.302585092994046


def cap_dps(N):
    return int(floor_digits(N)) + 45


def polish_dps(N):
    return int(floor_digits(N)) + 70


def pred_dps(N, x):
    """Predicted working precision at Re z = x: bulk |Xi_N| ~ e^{-pi x/4} until
    the front, then the floor.  0.3413 = (pi/4)/ln 10."""
    xe = min(abs(float(x)), 4.0 * (N + 1) ** 2)
    return min(cap_dps(N), max(30, int(0.3413 * xe) + 35))


class BadContour(Exception):
    """A contour point could not be resolved (zero on/near the contour) or the
    winding did not come out near-integer."""

    def __init__(self, msg, z=None):
        super().__init__(msg)
        self.z = z


class Eval:
    """Adaptive-precision cached evaluator.  __call__(z) -> (v, err) with
    |true - v| <= err (heuristic bound: term scale * 10^{5-dps}); precision is
    raised until |v| > 10^min_good * err or the per-N cap is hit."""

    MIN_GOOD = 8  # trusted phase/sign needs >= 8 clean digits

    def __init__(self, N, real=False):
        self.N = N
        self.real = real
        self.cap = cap_dps(N)
        self.cache = {}
        self.evals = 0
        self.hits = 0

    def scale(self, z):
        # order-of-magnitude bound on the terms whose cancellation forms Xi_N:
        # C_N ~ 0.5, |s(s-1)/2| ~ |z|^2/2, sum_n |G| = O(1) for |Im z| <= 12.
        return 10 * (2 + abs(z) ** 2)

    def raw(self, z, d):
        self.evals += 1
        old = mp.dps
        mp.dps = d
        try:
            if self.real:
                return xc.Xi_N_real(z, self.N)
            return xc.Xi_N(z, self.N)
        finally:
            mp.dps = old

    def __call__(self, z):
        if self.real:
            key = mp.nstr(z, 25)
        else:
            key = (mp.nstr(z.real, 25), mp.nstr(z.imag, 25))
        c = self.cache.get(key)
        if c is not None:
            v, err, d = c
            if abs(v) > 10 ** self.MIN_GOOD * err or d >= self.cap:
                self.hits += 1
                return v, err
        sc = self.scale(z)
        d = pred_dps(self.N, z if self.real else z.real)
        if c is not None:
            d = max(d, c[2] + 10)
        while True:
            v = self.raw(z, d)
            err = sc * mpf(10) ** (5 - d)
            if abs(v) > 10 ** self.MIN_GOOD * err or d >= self.cap:
                self.cache[key] = (v, err, d)
                return v, err
            if abs(v) > err:
                # need ~ digits to expose |v| above err with MIN_GOOD margin
                need = d + self.MIN_GOOD + 3 + int(mp.log10(err / abs(v)))
            else:
                need = d + 20
            d = min(self.cap, max(need, d + 10))


class Winding:
    """Adaptive phase-tracking winding number around a polygon."""

    def __init__(self, ev, tol=mpf('0.8'), maxdepth=44):
        self.ev = ev
        self.tol = mpf(tol)
        self.maxdepth = maxdepth
        self.minabs = mp.inf

    def f(self, z):
        v, err = self.ev(z)
        if abs(v) <= 10 ** 4 * err:
            raise BadContour(
                f"unresolvable contour point {mp.nstr(z, 15)} "
                f"|v|={mp.nstr(abs(v), 3)} err={mp.nstr(err, 3)}", z)
        a = abs(v)
        if a < self.minabs:
            self.minabs = a
        return v

    def seg(self, p0, v0, p1, v1, depth):
        d = arg(v1 / v0)
        if abs(d) <= self.tol:
            return d
        if depth >= self.maxdepth:
            raise BadContour(
                f"phase-refinement depth limit near {mp.nstr((p0 + p1) / 2, 15)}",
                (p0 + p1) / 2)
        pm = (p0 + p1) / 2
        vm = self.f(pm)
        return (self.seg(p0, v0, pm, vm, depth + 1)
                + self.seg(pm, vm, p1, v1, depth + 1))

    def edge(self, za, zb, max_step):
        n = max(1, int(mp.ceil(abs(zb - za) / max_step)))
        pts = [za + (zb - za) * k / n for k in range(n + 1)]
        vals = [self.f(p) for p in pts]
        return sum(self.seg(pts[k], vals[k], pts[k + 1], vals[k + 1], 0)
                   for k in range(n))

    def polygon(self, corners, max_step):
        tot = mpf(0)
        for k in range(len(corners) - 1):
            tot += self.edge(corners[k], corners[k + 1], max_step)
        return tot / (2 * pi)


def count_box(ev, x0, x1, y0, y1, max_step=mpf('0.25')):
    """Integer number of zeros in the open box (x0,x1) x (y0,y1).
    Raises BadContour (with the offending point when known) on failure."""
    last = None
    for tol, ms in ((mpf('0.8'), max_step),
                    (mpf('0.5'), max_step / 2),
                    (mpf('0.35'), max_step / 4)):
        try:
            w = Winding(ev, tol)
            c = w.polygon([mpc(x0, y0), mpc(x1, y0), mpc(x1, y1),
                           mpc(x0, y1), mpc(x0, y0)], ms)
        except BadContour as e:
            last = e
            continue
        n = int(mp.nint(c))
        if abs(c - n) < mpf('0.02') and n >= 0:
            return n
        last = BadContour(f"non-integer winding {mp.nstr(c, 10)} on "
                          f"[{mp.nstr(x0,8)},{mp.nstr(x1,8)}]x"
                          f"[{mp.nstr(y0,8)},{mp.nstr(y1,8)}]")
    raise last


# ---------------------------------------------------------------- location

def _findroot_muller(N, seed, spread, dd, tol_exp):
    def f(z):
        old = mp.dps
        mp.dps = dd
        try:
            return xc.Xi_N(z, N)
        finally:
            mp.dps = old
    last = None
    # retries: Muller can raise ZeroDivisionError when consecutive iterates
    # collide exactly AT the root before the step tolerance is met; a looser
    # tolerance / different seed spread then succeeds.
    for te, sp in ((tol_exp, spread),
                   (tol_exp - 8, spread * mpf('3.7')),
                   (tol_exp - 16, spread * mpf('0.23'))):
        seeds = (seed, seed + sp, seed + IU * sp)
        try:
            return mp.findroot(f, seeds, solver='muller', tol=mpf(10) ** (-te))
        except (ZeroDivisionError, ValueError) as e:
            last = e
    raise last


def locate_single(ev, N, x0, x1, y0, y1):
    """Find the unique zero in a count-1 box.  Returns the root or None."""
    w, h = x1 - x0, y1 - y0
    dd = min(pred_dps(N, (x0 + x1) / 2) + 30, cap_dps(N) + 25)
    spread = max(min(w, h) / 20, mpf('1e-6'))
    seeds = [mpc(x0 + w / 2, y0 + h / 2),
             mpc(x0 + w * mpf('0.37'), y0 + h * mpf('0.41')),
             mpc(x0 + w * mpf('0.63'), y0 + h * mpf('0.59'))]
    old = mp.dps
    for sd in seeds:
        try:
            r = _findroot_muller(N, sd, spread, dd, dd - 10)
        except Exception:
            continue
        if not (x0 < r.real < x1 and y0 < r.imag < y1):
            continue
        # verify it is a genuine zero, not a Muller stall point: the residual
        # must be far below the local scale (cf. the spurious 175.115+6.2505i
        # accepted for N=5 before this check existed)
        mp.dps = dd
        try:
            res = abs(xc.Xi_N(r, N))
            loc = abs(xc.Xi_N(r + spread / 3 + IU * spread / 5, N))
        finally:
            mp.dps = old
        if res < loc * mpf('1e-10'):
            return r
    return None


def isolate(ev, N, x0, x1, y0, y1, k, log=None, depth=0):
    """Return the k zeros in (x0,x1)x(y0,y1) by count-guided bisection.
    Child counts are recomputed and verified to sum to the parent count."""
    if k == 0:
        return []
    w, h = x1 - x0, y1 - y0
    if k == 1:
        r = locate_single(ev, N, x0, x1, y0, y1)
        if r is not None:
            return [r]
        if w < mpf('1e-4') and h < mpf('1e-4'):
            if log:
                log(f"    !! locate_single failed in tiny box "
                    f"[{mp.nstr(x0,12)},{mp.nstr(x1,12)}]x"
                    f"[{mp.nstr(y0,12)},{mp.nstr(y1,12)}] -- reporting center")
            return [mpc((x0 + x1) / 2, (y0 + y1) / 2)]
    if depth > 60:
        raise BadContour(f"isolate depth>60 with k={k} at "
                         f"[{mp.nstr(x0,10)},{mp.nstr(x1,10)}]x"
                         f"[{mp.nstr(y0,10)},{mp.nstr(y1,10)}]")
    ms = max(min(mpf('0.25'), max(w, h) / 4), mpf('1e-5'))
    last = None
    for frac in (mpf('0.5'), mpf('0.53'), mpf('0.461'), mpf('0.567')):
        if w >= h:
            xm = x0 + frac * w
            sub1, sub2 = (x0, xm, y0, y1), (xm, x1, y0, y1)
        else:
            ym = y0 + frac * h
            sub1, sub2 = (x0, x1, y0, ym), (x0, x1, ym, y1)
        try:
            k1 = count_box(ev, *sub1, max_step=ms)
            k2 = count_box(ev, *sub2, max_step=ms)
        except BadContour as e:
            last = e
            continue
        if k1 + k2 == k:
            return (isolate(ev, N, *sub1, k1, log, depth + 1)
                    + isolate(ev, N, *sub2, k2, log, depth + 1))
        last = BadContour(f"child counts {k1}+{k2} != parent {k}")
    raise last


def polish_zero(N, r, log=None):
    """High-precision polish + residual verification against the local scale.
    Returns (root, ok, residual, local_scale)."""
    pd = polish_dps(N)
    try:
        rp = _findroot_muller(N, r, mpf('1e-8'), pd, pd - 12)
    except Exception:
        rp = r
    old = mp.dps
    mp.dps = pd
    try:
        res = abs(xc.Xi_N(rp, N))
        loc = abs(xc.Xi_N(rp + mpf('0.011') + mpf('0.007') * IU, N))
    finally:
        mp.dps = old
    ok = bool(res < loc * mpf('1e-15') and abs(rp - r) < mpf('0.1'))
    if not ok and log:
        log(f"    !! polish verification FAILED at {mp.nstr(rp, 15)}: "
            f"res={mp.nstr(res, 3)} local={mp.nstr(loc, 3)}")
    return rp, ok, res, loc


def dedup(roots, eps=mpf('1e-6')):
    """Cluster roots within eps (the fix for the earlier dedup bug)."""
    out = []
    for r in sorted(roots, key=lambda t: (t.real, t.imag)):
        if all(abs(r - q) > eps for q in out):
            out.append(r)
    return out


# ---------------------------------------------------------------- real axis

def real_scan(N, X, log=None):
    """All real zeros of Xi_N in (0, X]: sign-change scan (step 0.2 globally,
    0.05 inside the front window [4(N+1)^2 - 60, X]), bisection bracket to 1e-3,
    then high-precision Anderson polish.  Signs are only trusted when the
    adaptive evaluator certifies them.  Returns list of mpf zeros."""
    evr = Eval(N, real=True)
    front_lo = mpf(4 * (N + 1) ** 2 - 60)
    front_hi = min(mpf(X), mpf('4.4') * (N + 1) ** 2 + 20)

    def step_at(x):
        return mpf('0.05') if front_lo <= x <= front_hi else mpf('0.2')

    def sgn(x):
        v, err = evr(x)
        if abs(v) <= 10 ** 4 * err:
            return 0  # unresolved: essentially ON a zero
        return 1 if v > 0 else -1

    pd = polish_dps(N)

    def polish(a, b):
        old = mp.dps
        mp.dps = pd
        try:
            def f(t):
                return xc.Xi_N_real(t, N)
            return mp.findroot(f, (a, b), solver='anderson',
                               tol=mpf(10) ** (-(pd - 15)))
        finally:
            mp.dps = old

    zeros = []
    x = mpf(0)
    sprev = sgn(x)
    while x < X:
        xn = min(x + step_at(x), mpf(X))
        snext = sgn(xn)
        if snext == 0:
            # scan point sits on a zero: bracket around it
            a, b = x, min(xn + step_at(xn), mpf(X))
            sb = sgn(b)
            if sprev != 0 and sb != 0 and sprev != sb:
                zeros.append(polish(a, b))
            else:
                zeros.append(xn)  # even-order or unresolved -- flag
                if log:
                    log(f"  !! sign scan hit unresolved point x={mp.nstr(xn, 12)}")
            x, sprev = b, sb
            continue
        if sprev != 0 and sprev != snext:
            a, b = x, xn
            for _ in range(8):  # bracket to ~1e-3
                m = (a + b) / 2
                sm = sgn(m)
                if sm == 0:
                    break
                if sm == sprev:
                    a = m
                else:
                    b = m
            zeros.append(polish(a, b))
        x, sprev = xn, snext
    return zeros, evr


def reality_check(N, zeros, log=None):
    """Polish each real zero from x + 0.01i; return max |Im| of results."""
    maxim = mpf(0)
    for x in zeros:
        # x-appropriate precision: at small x the local scale of Xi_N is far
        # above the floor, and an excessive step tolerance makes Muller
        # iterates collide at the working ulp before it is met.
        dd = min(pred_dps(N, x) + 30, polish_dps(N))
        got = None
        for h in (mpf('0.01'), mpf('0.003'), mpf('0.03')):
            try:
                got = _findroot_muller(N, mpc(x, h), mpf('1e-4'), dd, dd - 12)
                break
            except Exception:
                continue
        if got is None:
            if log:
                log(f"  !! reality check: findroot failed at x={mp.nstr(x, 15)}")
            maxim = mpf('inf')
        else:
            maxim = max(maxim, abs(got.imag))
    return maxim
