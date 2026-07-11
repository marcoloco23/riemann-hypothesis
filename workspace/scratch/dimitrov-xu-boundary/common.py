"""Shared machinery for verifying Dimitrov-Xu correlation-kernel claims.

Conventions (pinned, stated in README):
  xi(s)  = (1/2) s (s-1) pi^(-s/2) Gamma(s/2) zeta(s)          (completed zeta)
  Xi(z)  = xi(1/2 + i z)                                        (real, even for real z)
  L(z)   = Xi'(z)^2 - Xi(z) Xi''(z)  (derivatives in z)
         = xi(s) xi''(s) - xi'(s)^2   at s = 1/2 + i z          (derivatives in s)
  Fourier convention:  fhat(x) = int_R f(u) e^{-i x u} du.
  Riemann kernel: Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2})
                            e^{-pi n^2 e^{2u}}   for u >= 0, extended evenly.
  Claimed/checked normalization:  Xi(x) = int_R Phi(u) e^{-i x u} du
                                        = 2 int_0^inf Phi(u) cos(xu) du.

Analytic derivatives of xi (avoids finite differencing of zeta):
  h(s)  = (1/2) s (s-1) pi^(-s/2) Gamma(s/2)
  A(s)  = h'/h = 1/s + 1/(s-1) - (ln pi)/2 + psi(s/2)/2
  A'(s) = -1/s^2 - 1/(s-1)^2 + psi'(s/2)/4
  xi   = h zeta
  xi'  = h (A zeta + zeta')
  xi'' = h ((A^2 + A') zeta + 2 A zeta' + zeta'')
  ==> xi xi'' - xi'^2 = h^2 * ( A' zeta^2 + zeta zeta'' - zeta'^2 )
mpmath.zeta(s, derivative=k) supplies zeta^{(k)} rigorously (Euler-Maclaurin);
we cross-validate the composition against mpmath.diff of xi itself in tests.
"""
import mpmath as mp


def h_factor(s):
    return mp.mpf(1) / 2 * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)


def xi(s):
    return h_factor(s) * mp.zeta(s)


def xi_derivs(s):
    """Return (xi, xi', xi'') at s via analytic composition."""
    h = h_factor(s)
    A = 1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2 + mp.digamma(s / 2) / 2
    Ap = -1 / s**2 - 1 / (s - 1) ** 2 + mp.polygamma(1, s / 2) / 4
    z0 = mp.zeta(s)
    z1 = mp.zeta(s, derivative=1)
    z2 = mp.zeta(s, derivative=2)
    xi0 = h * z0
    xi1 = h * (A * z0 + z1)
    xi2 = h * ((A * A + Ap) * z0 + 2 * A * z1 + z2)
    return xi0, xi1, xi2


def wronskian_s(s):
    """xi(s) xi''(s) - xi'(s)^2, computed via the cancellation-free form
    h^2 (A' zeta^2 + zeta zeta'' - zeta'^2)."""
    h = h_factor(s)
    Ap = -1 / s**2 - 1 / (s - 1) ** 2 + mp.polygamma(1, s / 2) / 4
    z0 = mp.zeta(s)
    z1 = mp.zeta(s, derivative=1)
    z2 = mp.zeta(s, derivative=2)
    return h * h * (Ap * z0 * z0 + z0 * z2 - z1 * z1)


def L_of_z(z):
    """L(z) = Xi'(z)^2 - Xi(z) Xi''(z) = [xi xi'' - xi'^2](s=1/2+iz)."""
    return wronskian_s(mp.mpf(1) / 2 + mp.mpc(0, 1) * z)


def B_boundary(t):
    """B(t) = Re[ xi(1+it) xi''(1+it) - xi'(1+it)^2 ]."""
    return mp.re(wronskian_s(mp.mpc(1, t)))


# ---------------------------------------------------------------- Riemann kernel
def phi_atom(n, u):
    """Theta atom phi_n(u) for u >= 0 (analytic formula)."""
    e2u = mp.exp(2 * u)
    return (2 * mp.pi**2 * n**4 * mp.exp(mp.mpf(9) / 2 * u)
            - 3 * mp.pi * n**2 * mp.exp(mp.mpf(5) / 2 * u)) * mp.exp(-mp.pi * n**2 * e2u)


def phi_atom_even(n, u):
    """Atom-level even extension phi~_n(u) := phi_n(|u|).  NOTE: this is a
    CHOICE -- the analytic formula for phi_n is NOT even; only the full sum
    Phi has the modular even symmetry."""
    return phi_atom(n, abs(u))


def Phi(u, nmax=None):
    """Even Riemann kernel Phi(|u|). nmax chosen from working precision:
    tail term n is ~ e^{-pi n^2}, so pi n^2 > ln(10) * (dps+10) suffices at u>=0
    (larger u only helps)."""
    if nmax is None:
        nmax = int(mp.ceil(mp.sqrt((mp.mp.dps + 12) * mp.log(10) / mp.pi))) + 2
    ua = abs(u)
    return mp.fsum(phi_atom(n, ua) for n in range(1, nmax + 1))


# Numerically pinned (sanity.py): Xi(x) = 4 * int_0^inf Phi(u) cos(xu) du.
# Hence with OUR FT convention  Xi(x) = int_R Phi_conv(u) e^{-ixu} du  we need
#   Phi_conv(u) = PHI_SCALE * Phi(|u|),  PHI_SCALE = 2.
PHI_SCALE = 2


def Phi_conv(u, nmax=None):
    return PHI_SCALE * Phi(u, nmax=nmax)
