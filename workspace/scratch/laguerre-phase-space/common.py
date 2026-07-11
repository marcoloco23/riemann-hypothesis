"""Shared utilities: Xi function and Cauchy-integral derivatives (mpmath).

Xi(z) := xi(1/2 + i z),  xi(s) = (1/2) s (s-1) pi^(-s/2) Gamma(s/2) zeta(s).
Xi is real entire and even.

Derivatives are computed with an N-point trapezoidal rule for the Cauchy
integral over a circle |w - z| = r (spectrally accurate for periodic analytic
integrands), NOT with mpmath's diff(method='quad'):  mpmath's quadts stops on
an (effectively absolute) error criterion, so for integrands of tiny magnitude
(|Xi| ~ 1e-2385 at t ~ 7005) it "converges" at the coarsest level and returns
a radius-dependent coarse estimate.  We found this the hard way; see
run-output.txt cross-checks.  The trapezoid rule below is deterministic and is
validated by N-doubling inside cauchy_derivs.
"""
import mpmath as mp


def xi(s):
    """xi(s) = (1/2) s (s-1) pi^(-s/2) Gamma(s/2) zeta(s).

    Implemented as (s-1) pi^(-s/2) Gamma(s/2 + 1) zeta(s), identical via
    (1/2) s Gamma(s/2) = Gamma(s/2 + 1), but pole-free at s = 0 (needed on
    the imaginary z-axis, e.g. Xi at z = i/2 <=> s = 0).
    """
    s = mp.mpc(s)
    if s == 1:  # removable: (s-1) zeta(s) -> 1
        return mp.pi ** (-mp.mpf('0.5')) * mp.gamma(mp.mpf('1.5'))
    return (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2 + 1) * mp.zeta(s)


def Xi(z):
    return xi(mp.mpf('0.5') + mp.mpc(0, 1) * mp.mpc(z))


def cauchy_derivs(f, z, nmax, radius, N=128, check=True):
    """f^(k)(z) for k = 0..nmax via the trapezoidal Cauchy rule.

    f^(k)(z) = k!/(N r^k) sum_j f(z + r e^{i th_j}) e^{-i k th_j},  th_j = 2 pi j/N.
    Error is aliasing only: computed c_k = c_k + sum_{m>=1} c_{k+mN} r^{mN};
    with N >> nmax and moderate r this is negligible for our entire functions.
    If check=True, recompute with 2N nodes and raise if disagreement exceeds
    1e-(dps-15) relatively (the slack absorbs roundoff cancellation ~ r^-k in
    high orders; genuine quadrature failures are orders of magnitude larger).
    """
    z = mp.mpc(z)
    r = mp.mpf(radius)

    def derivs(NN):
        vals = [f(z + r * mp.expj(2 * mp.pi * j / NN)) for j in range(NN)]
        M = max(abs(vv) for vv in vals)  # roundoff floor scale
        out = []
        for k in range(nmax + 1):
            s = mp.mpc(0)
            for j in range(NN):
                s += vals[j] * mp.expj(-2 * mp.pi * j * k / NN)
            out.append(s * mp.factorial(k) / (NN * r ** k))
        return out, M

    d1, M1 = derivs(N)
    if check:
        d2, M2 = derivs(2 * N)
        tol = mp.mpf(10) ** (-(mp.mp.dps - 15))
        for k in range(nmax + 1):
            # roundoff floor: an order-k Cauchy coefficient carries absolute
            # noise ~ eps * M * k!/r^k, which dominates when the true
            # derivative vanishes (e.g. odd derivatives of even Xi at x=0)
            floor = max(M1, M2) * mp.factorial(k) / r ** k
            scale = max(abs(d1[k]), abs(d2[k]), floor)
            if abs(d1[k] - d2[k]) / scale > tol:
                raise ValueError(f"cauchy_derivs N-doubling check failed at order {k}: "
                                 f"{d1[k]} vs {d2[k]}")
        d1 = d2
    return d1


def Xi_derivs_real(x, kmax, radius=1.5, N=128):
    """Xi^(k)(x) for k=0..kmax at real x; returns real mpf values."""
    d = cauchy_derivs(Xi, mp.mpf(x), kmax, radius, N=N)
    return [dk.real for dk in d]


def laguerre_Ln(derivs, n):
    """L_n[f](x) = (1/(2n)!) sum_{j=0}^{2n} (-1)^(j+n) C(2n,j) f^(j) f^(2n-j)."""
    s = mp.mpf(0)
    for j in range(2 * n + 1):
        s += (-1) ** (j + n) * mp.binomial(2 * n, j) * derivs[j] * derivs[2 * n - j]
    return s / mp.factorial(2 * n)
