"""Li coefficients for zeta and for the Davenport-Heilbronn function (NUMERICAL ONLY).

Purpose (doc 01 B1 / E10): motivation and litmus grounding for
``workspace/attempts/li-positivity/``. Nothing computed here enters any proof.

What it does
------------
1.  Computes the Li coefficients ``lambda_n``, n = 1..N, of the completed zeta
    ``xi(s) = 1/2 s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`` via the Taylor expansion of
    ``G(z) = h'(z)/h(z)``, ``h(z) = xi(1/(1-z))`` (the definition in
    ``workspace/lemmas/L3-li-converse-pringsheim.md``).

    Method: Taylor coefficients ``c_k`` of ``h`` at 0 by Cauchy integrals on the
    circle ``|z| = r`` (trapezoidal rule = exponentially accurate for periodic
    analytic integrands), then the power-series identity ``h' = G h`` solved
    recursively for the coefficients of ``G``:

        (k+1) c_{k+1} = sum_{j<=k} g_j c_{k-j}   =>   g_k,   lambda_n = g_{n-1}.

    The contour ``|z| = r < 1`` maps to a compact disk strictly inside
    ``Re(s) > 1/2`` (lemma L1(4)), where xi is holomorphic and tame.

2.  Convention/correctness checks:
      - lambda_1 against the closed form  1 + gamma/2 - (1/2) log(4 pi)
        (sum over zeros of 1/rho; classical, e.g. [Edwards]).
      - internal cross-check of lambda_n for small n via direct high-order
        numerical differentiation of G (independent route).

3.  Davenport-Heilbronn litmus function (doc 06 LITMUS-1):
        f(s) = (1-i kappa)/2 * L(s,chi) + (1+i kappa)/2 * L(s,conj(chi)),
    chi the character mod 5 with chi(2) = i,
    kappa = (sqrt(10 - 2 sqrt(5)) - 2)/(sqrt(5) - 1).
      - verifies numerically the self-dual functional equation
        Xi_f(s) = Xi_f(1-s), Xi_f(s) = (pi/5)^(-(s+1)/2) Gamma((s+1)/2) f(s);
      - refines the classical off-line zero near 0.8085 + 85.699i ([Spira1968])
        and reports it;
      - computes lambda_n(f) and the single-zero prediction for where the first
        negative Li coefficient of f must appear (criterion signature, lemma L3).

Run:  .venv/bin/python li_coefficients.py        (mpmath pinned in requirements.txt)
"""

from __future__ import annotations

import mpmath as mp

# ----------------------------- configuration ---------------------------------

DPS = 60          # working precision (decimal digits)
N_COEFFS = 40     # compute lambda_1 .. lambda_N_COEFFS
M_POINTS = 256    # contour sample count (aliasing error ~ r^(M - n), negligible)

# Precision must be set BEFORE any module-level constant is evaluated, otherwise
# constants like KAPPA freeze at mpmath's default 15 digits and poison everything.
mp.mp.dps = DPS

RADIUS = mp.mpf(1) / 2


# ----------------------------- generic machinery -----------------------------

def taylor_coeffs_cauchy(func, n_max: int, r=RADIUS, m_points: int = M_POINTS):
    """Taylor coefficients c_0..c_n_max of `func` at 0 by trapezoidal Cauchy integrals."""
    samples = []
    for j in range(m_points):
        theta = mp.mpf(2) * mp.pi * j / m_points
        samples.append(func(r * mp.e ** (1j * theta)))
    coeffs = []
    for n in range(n_max + 1):
        acc = mp.mpc(0)
        for j, val in enumerate(samples):
            theta = mp.mpf(2) * mp.pi * j / m_points
            acc += val * mp.e ** (-1j * n * theta)
        coeffs.append(acc / (m_points * r ** n))
    return coeffs


def log_derivative_coeffs(c, n_max: int):
    """Coefficients g_0..g_{n_max-1} of h'/h from Taylor coefficients c of h (c[0] != 0)."""
    g = []
    for k in range(n_max):
        acc = (k + 1) * c[k + 1]
        for j in range(k):
            acc -= g[j] * c[k - j]
        g.append(acc / c[0])
    return g


def li_coefficients(completed, n_max: int):
    """lambda_1..lambda_n_max for a completed function via h(z) = completed(1/(1-z))."""
    h = lambda z: completed(1 / (1 - z))
    c = taylor_coeffs_cauchy(h, n_max + 1)
    return log_derivative_coeffs(c, n_max)  # lambda_n = g[n-1]


# ----------------------------- zeta -------------------------------------------

def xi(s):
    s = mp.mpc(s)
    if s == 1:  # removable singularity: xi(1) = 1/2 (lemma L2 (3))
        return mp.mpc(mp.mpf("0.5"))
    return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


# ----------------------------- Davenport-Heilbronn ----------------------------

CHI = {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}  # character mod 5 with chi(2) = i


def dirichlet_l(s, conjugate: bool = False):
    """L(s, chi) (or L(s, conj chi)) via Hurwitz zeta: 5^-s sum_a chi(a) zeta(s, a/5)."""
    s = mp.mpc(s)
    total = mp.mpc(0)
    for a in range(1, 5):
        coeff = mp.conj(mp.mpc(CHI[a])) if conjugate else mp.mpc(CHI[a])
        total += coeff * mp.zeta(s, mp.mpf(a) / 5)
    return 5 ** (-s) * total


KAPPA = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)


def dh(s):
    """Davenport-Heilbronn f(s)."""
    return ((1 - 1j * KAPPA) * dirichlet_l(s) + (1 + 1j * KAPPA) * dirichlet_l(s, True)) / 2


def xi_dh(s):
    """Completed D-H function (odd character mod 5): (pi/5)^(-(s+1)/2) Gamma((s+1)/2) f(s)."""
    s = mp.mpc(s)
    return (mp.pi / 5) ** (-(s + 1) / 2) * mp.gamma((s + 1) / 2) * dh(s)


# ----------------------------- report -----------------------------------------

def main() -> None:
    print("=" * 78)
    print("Li coefficients of zeta (NUMERICAL; motivation only)")
    print("=" * 78)
    lam = li_coefficients(xi, N_COEFFS)

    # Check 1: closed form for lambda_1 = 1 + gamma/2 - (1/2) log(4 pi).
    lam1_exact = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    err1 = abs(lam[0] - lam1_exact)
    print(f"lambda_1 computed = {mp.nstr(lam[0].real, 40)}")
    print(f"lambda_1 exact    = {mp.nstr(lam1_exact, 40)}")
    print(f"|difference|      = {mp.nstr(err1, 5)}   (convention pinned iff ~1e-{DPS - 20} or less)")

    # Check 2: independent route -- direct numerical differentiation of G at 0.
    def G(z):
        hh = lambda u: xi(1 / (1 - u))
        return mp.diff(hh, z) / hh(z)

    print("\nCross-check (independent route: direct differentiation of G):")
    for n in (1, 2, 3, 5, 8):
        direct = mp.diff(G, 0, n - 1) / mp.factorial(n - 1)
        print(f"  n={n:2d}  series={mp.nstr(lam[n - 1].real, 25):>30}  "
              f"direct={mp.nstr(direct.real, 25):>30}  "
              f"|diff|={mp.nstr(abs(lam[n - 1] - direct), 3)}")

    # Table with the RH-conditional asymptote (n/2)(log n + gamma - 1 - log 2pi).
    print("\n  n        lambda_n              lambda_n / asymptote     max|Im| (should be ~0)")
    max_imag = max(abs(l.imag) for l in lam)
    all_positive = True
    for n in range(1, N_COEFFS + 1):
        l_re = lam[n - 1].real
        if l_re <= 0:
            all_positive = False
        asym = mp.mpf(n) / 2 * (mp.log(n) + mp.euler - 1 - mp.log(2 * mp.pi)) if n > 1 else None
        ratio = mp.nstr(l_re / asym, 8) if asym not in (None, mp.mpf(0)) else "-"
        print(f"{n:4d}  {mp.nstr(l_re, 20):>24}  {ratio:>18}")
    print(f"\nmax |Im lambda_n| = {mp.nstr(max_imag, 3)}   (reality check)")
    print(f"all lambda_n > 0 for n <= {N_COEFFS}: {all_positive}   [NUMERICAL]")

    print()
    print("=" * 78)
    print("Davenport-Heilbronn litmus function (doc 06 LITMUS-1)  [NUMERICAL]")
    print("=" * 78)
    print(f"kappa = {mp.nstr(KAPPA, 30)}")

    # Functional equation check at arbitrary points.
    print("\nFunctional equation Xi_f(s) - Xi_f(1-s) at test points:")
    for s in (mp.mpc("0.3", "2.7"), mp.mpc("1.9", "-4.1"), mp.mpc("0.71", "33.3")):
        fe_err = abs(xi_dh(s) - xi_dh(1 - s)) / abs(xi_dh(s))
        print(f"  s = {mp.nstr(s, 6):>16}   relative error = {mp.nstr(fe_err, 3)}")

    # f on the real segment (1, 4): sign scan (Euler-product positivity is NOT available).
    real_vals = [(sigma, dh(sigma).real) for sigma in mp.arange(mp.mpf("1.05"), 4, mp.mpf("0.05"))]
    fmin = min(v for _, v in real_vals)
    print(f"\nmin of f(sigma) on real sigma in [1.05, 4): {mp.nstr(fmin, 10)} "
          f"(f real on the real axis; positivity NOT structural, unlike zeta)")

    # Refine the classical off-line zero ([Spira1968] seed).
    rho_f = mp.findroot(dh, mp.mpc("0.8085", "85.6993"))
    print(f"\nOff-critical-line zero of f (refined from [Spira1968] seed):")
    print(f"  rho_f      = {mp.nstr(rho_f, 30)}")
    print(f"  |f(rho_f)| = {mp.nstr(abs(dh(rho_f)), 3)}")
    print(f"  Re(rho_f)  = {mp.nstr(rho_f.real, 25)}   (!= 1/2: off-line; NUMERICAL evidence only)")

    # Criterion signature for f (lemma L3): r0 and the negativity onset estimate.
    w = 1 - 1 / rho_f
    r0 = abs(w)
    print(f"\n  |w(rho_f)| = {mp.nstr(r0, 20)}  (< 1, lemma L1: zero in Re > 1/2)")
    print(f"  -log r0    = {mp.nstr(-mp.log(r0), 6)}")
    print("  => single-zero estimate: |contribution| ~ r0^(-n) overtakes the ~(n/2)log n bulk")
    onset = mp.findroot(lambda n: -n * mp.log(r0) - mp.log(n / 2 * mp.log(n + 2) + 2), 1e5)
    print(f"     around n ~ {mp.nstr(onset, 4)}  (heuristic; other off-line zeros can only hasten it)")

    lam_f = li_coefficients(xi_dh, N_COEFFS)
    neg = [n for n in range(1, N_COEFFS + 1) if lam_f[n - 1].real <= 0]
    print(f"\nlambda_n(f), n = 1..{N_COEFFS}: first values "
          f"{[mp.nstr(lam_f[k].real, 8) for k in range(6)]}")
    print(f"negative lambda_n(f) for n <= {N_COEFFS}: {neg if neg else 'none'} "
          f"(consistent: onset estimated ~1e5; L3's signature is asymptotic)")

    print("\nDone. All values NUMERICAL (mpmath, dps = %d); nothing here is a proof." % DPS)


if __name__ == "__main__":
    main()
