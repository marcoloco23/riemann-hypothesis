"""
Self-dual theta truncations of the Riemann xi function.

PINNED DEFINITIONS (verified numerically in s00_pin.py)
--------------------------------------------------------
Kernel (task's H, series converges for all y > 0):

    H(y)   = 4 y^2 sum_{n>=1} (2 pi^2 n^4 y^2 - 3 pi n^2) e^{-pi n^2 y^2}
           = sum_{n>=1} h_n(y),
    h_n(y) = (8 pi^2 n^4 y^4 - 12 pi n^2 y^2) e^{-pi n^2 y^2}.

Verified identities (s00):
    (I1)  y H(y) = H(1/y)                      (theta functional equation),
    (I2)  2 xi(s) = Integral_0^inf y^{s-1} H(y) dy,
          xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s).
Term-wise Mellin transform on (0,inf) (complete gamma; used in s00):
    Integral_0^inf y^{s-1} h_n(y) dy = s(s-1) (pi n^2)^{-s/2} Gamma(s/2)
for Re s > 0 -- summing over n gives (I2) for Re s > 1, both sides entire.

SELF-DUAL TRUNCATION
--------------------
    H_N(y) = sum_{n<=N} h_n(y)                 for y >= 1,
    H_N(y) = H_N(1/y)/y                        for 0 < y < 1,
    xi_N^sd(s)  = (1/2) Integral_0^inf y^{s-1} H_N(y) dy,
    Xi_N^sd(z)  = xi_N^sd(1/2 + i z).

CLOSED FORM (derived by t = pi n^2 y^2 on the y>=1 piece; the 0<y<1 piece is
the y -> 1/y substitute of the y>=1 piece with s -> 1-s):

    Integral_1^inf y^{b-1} e^{-a y^2} dy = (1/2) a^{-b/2} Gamma(b/2, a),
    T_n(s) := Integral_1^inf y^{s-1} h_n(y) dy
            = a^{-s/2} [ 4 Gamma(s/2 + 2, a) - 6 Gamma(s/2 + 1, a) ],  a = pi n^2,
    xi_N^sd(s) = (1/2) sum_{n<=N} [ T_n(s) + T_n(1-s) ].          (*)

Manifestly symmetric under s <-> 1-s.  Via Gamma(c+1,a) = c Gamma(c,a) + a^c e^{-a}
(applied twice), (*) collapses ALGEBRAICALLY to

    xi_N^sd(s) = C_N + (s(s-1)/2) I_N(s),
    C_N  = sum_{n<=N} (4 pi n^2 - 1) e^{-pi n^2},
    I_N(s) = sum_{n<=N} [ a_n^{-s/2} Gamma(s/2, a_n) + a_n^{-(1-s)/2} Gamma((1-s)/2, a_n) ],

which is EXACTLY the one-sided (cosine-transform) truncation of
workspace/scratch/theta-strip/xi_common.py, same normalization:

    Xi_N^sd(z) === Xi_N^{one-sided}(z)   identically.

Reason: the one-sided family is 4 Int_0^inf Phi_N(u) cos(zu) du, i.e. the Fourier
transform of the EVEN extension of Phi_N(u) = sum_{n<=N} phi_n(u) from u >= 0;
and evenness in u = log y is precisely the y -> 1/y gluing H_N(y) := H_N(1/y)/y.
Numerical confirmation in s01.

LOG COORDINATES / FOURIER FORM
------------------------------
    Phi_N^sd(u) := (1/2) e^{u/2} H_N(e^u)      (even in u by construction),
    Xi_N^sd(z) = Integral_R Phi_N^sd(u) e^{izu} du = 2 Int_0^inf Phi_N^sd(u) cos(zu) du.
For u >= 0:  Phi_N^sd(u) = sum_{n<=N} (4 pi^2 n^4 e^{9u/2} - 6 pi n^2 e^{5u/2})
                            e^{-pi n^2 e^{2u}}  > 0   (since 2 pi n^2 e^{2u} > 3).

Corner at u = 0:
    J_N := Phi'(0+) - Phi'(0-) = 2 Phi'(0+) = (1/2) H_N(1) + H_N'(1)
         = (1/2) sum_{n<=N} [h_n(1) + 2 h_n'(1)]
         = -2 pi sum_{n<=N} n^2 (8 pi^2 n^4 - 30 pi n^2 + 15) e^{-pi n^2}.
Full series sums to 0 (differentiate y H(y) = H(1/y) at y=1), so
    J_N = +2 pi sum_{n>N} n^2 (8 pi^2 n^4 - 30 pi n^2 + 15) e^{-pi n^2}
        ~ 16 pi^3 (N+1)^6 e^{-pi (N+1)^2}  > 0,
and Xi_N^sd(x) ~ -J_N / x^2 as x -> +infinity (Fourier corner asymptotics).

All functions deterministic; precision controlled by mp.dps set by caller.
"""

from mpmath import mp, mpf, mpc, exp, cos, sin, pi, gamma, zeta

I = mpc(0, 1)


# ---------------------------------------------------------------- kernel H
def h_n(y, n):
    """One term of H: (8 pi^2 n^4 y^4 - 12 pi n^2 y^2) e^{-pi n^2 y^2}."""
    a = pi * n * n
    y2 = y * y
    return (8 * a * a * y2 * y2 - 12 * a * y2) * exp(-a * y2)


def H_series(y, N=None):
    """H(y) via the series (valid all y>0 for full H; this is sum n<=N)."""
    if N is None:
        # full: stop when terms negligible
        N = max(3, int(mp.sqrt((mp.dps + 10) * mp.log(10) / (pi * y * y))) + 2)
    return sum(h_n(y, n) for n in range(1, N + 1))


def H_N_sd(y, N):
    """Self-dual truncated kernel: series for y>=1, reflected for y<1."""
    y = mpf(y) if not isinstance(y, (mpf, mpc)) else y
    if y >= 1:
        return sum(h_n(y, n) for n in range(1, N + 1))
    return H_N_sd(1 / y, N) / y


# ------------------------------------------------- closed form, both routes
def T_n(s, n):
    """Integral_1^inf y^{s-1} h_n(y) dy = a^{-s/2}[4 G(s/2+2,a) - 6 G(s/2+1,a)]."""
    a = pi * n * n
    return a ** (-s / 2) * (4 * mp.gammainc(s / 2 + 2, a) - 6 * mp.gammainc(s / 2 + 1, a))


def xi_sd(s, N):
    """Self-dual truncation, primary closed form (manifestly s <-> 1-s symmetric)."""
    return sum(T_n(s, n) + T_n(1 - s, n) for n in range(1, N + 1)) / 2


def Xi_sd(z, N):
    """Xi_N^sd(z) = xi_N^sd(1/2 + iz)."""
    return xi_sd(mpf(1) / 2 + I * z, N)


def C_N(N):
    return sum((4 * pi * n * n - 1) * exp(-pi * n * n) for n in range(1, N + 1))


def G(c, a):
    """a^{-c} Gamma(c, a)."""
    return a ** (-c) * mp.gammainc(c, a)


def xi_sd_collapsed(s, N):
    """Equivalent collapsed form C_N + (s(s-1)/2) I_N(s) (= theta-strip Xi_N)."""
    tot = mpc(0)
    for n in range(1, N + 1):
        a = pi * n * n
        tot += G(s / 2, a) + G((1 - s) / 2, a)
    return C_N(N) + s * (s - 1) / 2 * tot


def Xi_sd_real(x, N):
    """Xi_N^sd on the real axis as an explicitly real quantity (fast, stable)."""
    s = mpf(1) / 2 + I * x
    tot = mpf(0)
    for n in range(1, N + 1):
        tot += 2 * G(s / 2, pi * n * n).real
    return C_N(N) - (x * x + mpf(1) / 4) / 2 * tot


# ------------------------------------------------------------- Fourier side
def Phi_sd(u, N):
    """Phi_N^sd(u) = (1/2) e^{u/2} H_N^sd(e^u); even in u."""
    return exp(u / 2) * H_N_sd(exp(u), N) / 2


def Xi_true(z):
    s = mpf(1) / 2 + I * z
    return mpf(1) / 2 * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def xi_true(s):
    return mpf(1) / 2 * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


# ------------------------------------------------------------------ corner
def J_closed(N):
    """J_N = -2 pi sum_{n<=N} n^2 (8 pi^2 n^4 - 30 pi n^2 + 15) e^{-pi n^2}."""
    return -2 * pi * sum(
        n * n * (8 * pi * pi * n ** 4 - 30 * pi * n * n + 15) * exp(-pi * n * n)
        for n in range(1, N + 1))


# ------------------------------------------------------------- derivatives
def dXi_sd_real(x, N, k=1, h=None):
    """k-th derivative (k=1,2) of Xi_N^sd on the real axis, central differences."""
    if h is None:
        h = mpf(10) ** (-max(6, mp.dps // 5))
    f = lambda t: Xi_sd_real(t, N)
    if k == 1:
        return (f(x + h) - f(x - h)) / (2 * h)
    if k == 2:
        return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)
    raise ValueError(k)
