"""Shared numerics for the Pick-kernel checks (mpmath; NUMERICAL, motivation only).

Precision is set here, BEFORE any constant is materialized (lesson recorded in
../li-coefficients/README.md).  Import this module first in every numeric script.
"""

import mpmath as mp

DPS = 60
mp.mp.dps = DPS

# ----------------------------- Riemann xi --------------------------------------

def xi(s):
    s = mp.mpc(s)
    if s == 1:
        return mp.mpc(mp.mpf("0.5"))
    return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Q_formula(x):
    """Q(x) = xi'/xi(1/2+x) via the exact decomposition
       1/(x+1/2) + 1/(x-1/2) - log(pi)/2 + psi(x/2+1/4)/2 + zeta'/zeta(1/2+x).
       (Valid for real x > 1/2; zeta(1/2+x) != 0 there.)"""
    x = mp.mpf(x)
    s = mp.mpf("0.5") + x
    return (1 / (x + mp.mpf("0.5")) + 1 / (x - mp.mpf("0.5"))
            - mp.log(mp.pi) / 2 + mp.digamma(x / 2 + mp.mpf("0.25")) / 2
            + mp.zeta(s, derivative=1) / mp.zeta(s))


def logderiv_cauchy(func, s0, r=mp.mpf("0.25"), m=64):
    """func'(s0)/func(s0) by a trapezoidal Cauchy integral for func' on |s-s0| = r.
       Exponentially accurate for entire func; independent of finite differences."""
    s0 = mp.mpc(s0)
    acc = mp.mpc(0)
    for j in range(m):
        th = 2 * mp.pi * mp.mpf(j) / m
        w = mp.e ** (1j * th)
        acc += func(s0 + r * w) / w
    return (acc / (m * r)) / func(s0)


def Q_diff(x, f=xi):
    """Q(x) via mp.diff of the completed function at s = 1/2 + x."""
    x = mp.mpf(x)
    s = mp.mpf("0.5") + x
    return mp.diff(f, s) / f(s)


# ----------------------------- Davenport-Heilbronn ------------------------------
# Conventions copied from ../li-coefficients/li_coefficients.py (verified there:
# root-number identity to 1e-61, functional equation to ~1e-60).

CHI = {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}  # character mod 5 with chi(2) = i


def dirichlet_l(s, conjugate=False):
    s = mp.mpc(s)
    total = mp.mpc(0)
    for a in range(1, 5):
        coeff = mp.conj(mp.mpc(CHI[a])) if conjugate else mp.mpc(CHI[a])
        total += coeff * mp.zeta(s, mp.mpf(a) / 5)
    return 5 ** (-s) * total


KAPPA = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)


def dh(s):
    return ((1 - 1j * KAPPA) * dirichlet_l(s) + (1 + 1j * KAPPA) * dirichlet_l(s, True)) / 2


def xi_dh(s):
    """Completed D-H: (5/pi)^((s+1)/2) Gamma((s+1)/2) f(s)  [= (pi/5)^(-(s+1)/2) ...]."""
    s = mp.mpc(s)
    return (mp.mpf(5) / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * dh(s)


# ----------------------------- Pick matrices ------------------------------------

def pick_matrix(points, qvals):
    """K[j,k] = (Q(x_j)+Q(x_k))/(x_j+x_k) from precomputed Q values."""
    n = len(points)
    K = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            K[j, k] = (qvals[j] + qvals[k]) / (points[j] + points[k])
    return K


def sym_eigs(K):
    """Eigenvalues of a real symmetric mpmath matrix, ascending."""
    E = mp.eigsy(K, eigvals_only=True)
    return sorted([E[i] for i in range(E.rows)])


def quartet_kernel(c):
    """K_alpha(x,y) for one quartet with c = alpha^2 (complex).  Returns callable."""
    cb = mp.conj(c)

    def K(x, y):
        return (2 * (x * y - c) / ((x**2 - c) * (y**2 - c))
                + 2 * (x * y - cb) / ((x**2 - cb) * (y**2 - cb))).real

    return K


def quartet_matrix(points, c):
    Kf = quartet_kernel(c)
    n = len(points)
    K = mp.matrix(n, n)
    for j in range(n):
        for k in range(j, n):
            K[j, k] = K[k, j] = Kf(points[j], points[k])
    return K
