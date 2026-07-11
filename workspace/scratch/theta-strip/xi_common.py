"""
Common definitions for finite theta truncations of the Riemann Xi function.

NORMALIZATION (pinned):
    Xi(z) := xi(1/2 + i z),  xi(s) = (1/2) s (s-1) pi^(-s/2) Gamma(s/2) zeta(s).

Fourier representation.  With the atoms as specified in the task,
    phi_n(u) = (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}},
    Phi(u) = sum_{n>=1} phi_n(u),
numerical verification (stage 1) shows
    2 * Integral_0^inf Phi(u) cos(z u) du = (1/2) * Xi(z)      [ratio 0.5 to 42 digits],
i.e. this Phi is HALF of Titchmarsh's Phi (whose coefficients are 4 pi^2 n^4 and
6 pi n^2).  PINNED CORRECT NORMALIZATION:
    Xi(z) = 4 * Integral_0^inf Phi(u) cos(z u) du.

Truncations (pinned so that Xi_N -> Xi as N -> inf):
    Xi_N(z) := 4 * Integral_0^inf sum_{n<=N} phi_n(u) cos(z u) du.
(The task's "Xi_N = 2*Int..." equals half of this; zeros are unaffected.)

Closed form (derived by w = pi n^2 e^{2u}, verified numerically herein):
    Integral_0^inf e^{beta u} e^{-pi n^2 e^{2u}} e^{i z u} du
        = (1/2) (pi n^2)^{-(beta+iz)/2} Gamma((beta+iz)/2, pi n^2).
With a_n = pi n^2, s = 1/2 + i z (so s/2 = 1/4 + iz/2, (1-s)/2 = 1/4 - iz/2),
using Gamma(c+1,a) = c Gamma(c,a) + a^c e^{-a} twice, one gets exactly:

    Phi_n(z) := Integral_0^inf phi_n(u) cos(z u) du
             = (1/4)(4 a_n - 1) e^{-a_n}
               + (s(s-1)/2) * (1/4) [ a_n^{-s/2} Gamma(s/2, a_n)
                                     + a_n^{-(1-s)/2} Gamma((1-s)/2, a_n) ],
i.e. the constants in the claimed alternative form are 1/4, NOT 1/2.

    Xi_N(z) = 4 sum_{n<=N} Phi_n(z) = C_N + (s(s-1)/2) * I_N(s),
    C_N = sum_{n<=N} (4 pi n^2 - 1) e^{-pi n^2},
    I_N(s) = sum_{n<=N} [ a_n^{-s/2} Gamma(s/2, a_n) + a_n^{-(1-s)/2} Gamma((1-s)/2, a_n) ]
           = Integral_1^inf theta_N(u) (u^{s/2-1} + u^{(1-s)/2-1}) du,
    theta_N(u) = sum_{n<=N} e^{-pi n^2 u}.

All functions deterministic; precision controlled by mp.dps set by caller.
"""

from mpmath import mp, mpf, mpc, exp, cos, sin, pi, sqrt, gamma, zeta, arg, fabs

I = mpc(0, 1)


def a_n(n):
    return pi * n * n


def C_N(N):
    """C_N = sum_{n<=N} (4 pi n^2 - 1) e^{-pi n^2}."""
    return sum((4 * pi * n * n - 1) * exp(-pi * n * n) for n in range(1, N + 1))


def G(c, a):
    """G(c,a) = a^{-c} Gamma(c,a) = Integral_1^inf e^{-a u} u^{c-1} du."""
    return a ** (-c) * mp.gammainc(c, a)


def I_N(s, N):
    """I_N(s) = sum_{n<=N} [G(s/2, a_n) + G((1-s)/2, a_n)]."""
    tot = mpc(0)
    for n in range(1, N + 1):
        a = a_n(n)
        tot += G(s / 2, a) + G((1 - s) / 2, a)
    return tot


def xi_from_zeta(s):
    """xi(s) = (1/2) s (s-1) pi^(-s/2) Gamma(s/2) zeta(s), via mpmath zeta."""
    return mpf(1) / 2 * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def Xi_true(z):
    """Xi(z) = xi(1/2 + i z), via mpmath zeta."""
    return xi_from_zeta(mpf(1) / 2 + I * z)


def Xi_N(z, N):
    """Closed form via incomplete gamma: Xi_N(z) = C_N + (s(s-1)/2) I_N(s)."""
    s = mpf(1) / 2 + I * z
    return C_N(N) + s * (s - 1) / 2 * I_N(s, N)


def Xi_N_real(x, N):
    """Xi_N on the real axis, computed as an explicitly real quantity.

    For real x: s/2 and (1-s)/2 are conjugates, so I_N is 2*Re(sum of G(s/2,.)),
    and s(s-1)/2 = -(x^2+1/4)/2 is real.
    """
    s = mpf(1) / 2 + I * x
    tot = mpf(0)
    for n in range(1, N + 1):
        tot += 2 * G(s / 2, a_n(n)).real
    return C_N(N) - (x * x + mpf(1) / 4) / 2 * tot


def phi_n(u, n):
    e2u = exp(2 * u)
    return (2 * pi**2 * n**4 * exp(mpf(9) / 2 * u)
            - 3 * pi * n**2 * exp(mpf(5) / 2 * u)) * exp(-pi * n * n * e2u)


def Xi_N_direct(z, N, U=None, nseg=None):
    """Direct numerical integration: Xi_N(z) = 4 Int_0^U sum_{n<=N} phi_n(u) cos(zu) du
    (pinned normalization, see module docstring).

    Tail bound: for u >= U, |phi_n(u)| <= 2 pi^2 n^4 e^{9u/2} e^{-pi n^2 e^{2u}} and
    pi e^{2U} >= mp.dps*ln(10) + margin makes the tail utterly negligible. With
    U = 3, pi e^6 ~ 1267, e^{-1267} ~ 10^-550: negligible for dps <= 400.
    |cos(zu)| <= e^{|Im z| u}: harmless for |Im z| <= 40 at U = 3.
    For oscillation, split [0,U] into >= max(20, |Re z|) segments.
    """
    if U is None:
        U = mpf(3)
    if nseg is None:
        nseg = int(max(20, 2 * abs(mp.re(z)) * float(U) / 3.14)) + 1
    pts = [U * k / nseg for k in range(nseg + 1)]

    def f(u):
        tot = mpf(0)
        for n in range(1, N + 1):
            tot += phi_n(u, n)
        return tot * cos(z * u)

    return 4 * mp.quad(f, pts)


def dXi_N(z, N, h=None):
    """Numerical derivative of Xi_N via central difference (relative error ~ h^2)."""
    if h is None:
        h = mpf(10) ** (-(mp.dps // 3))
    return (Xi_N(z + h, N) - Xi_N(z - h, N)) / (2 * h)
