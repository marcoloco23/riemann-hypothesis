"""Deterministic numerical checks for L8-L10; not interval certificates.

The compact test exp(1-1/(1-(u/3)^2))*cos(14*u), extended by zero,
is genuinely C_c^infinity. Compare 40/80 zero pairs and doubled quadrature
resolution, using (W) for the archimedean term. Also check the DH completion,
its exact negative b(3), and the exponential-test normalization in L9.
Only prints output; never changes stored research data.
"""

import argparse
import platform

import mpmath as mp


def primes_and_powers(limit):
    for p in range(2, limit + 1):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            n = p
            while n <= limit:
                yield n, mp.log(p)
                n *= p


def smooth_anchor(zeros, resolution):
    width = mp.mpf(3)

    def g(u):
        if abs(u) >= width:
            return mp.mpf(0)
        return mp.exp(1 - 1 / (1 - (u / width) ** 2)) * mp.cos(14 * u)

    def transform(z):
        panels = resolution * max(12, int(mp.ceil(width * (abs(z) + 14) / 10)))
        points = [width * j / panels for j in range(panels + 1)]
        return 2 * mp.quadgl(lambda u: g(u) * mp.cos(z * u), points, maxdegree=4)

    pole = mp.re(2 * transform(mp.j / 2))
    comb = -2 * mp.fsum(lam * g(mp.log(n)) / mp.sqrt(n)
                        for n, lam in primes_and_powers(20))

    def integrand(v):
        if not v:
            return -mp.mpf(3) / 2
        return (1 - mp.exp(3 * v / 2) * g(v)) * 2 * mp.exp(-2 * v) / (-mp.expm1(-2 * v))

    arch = -(mp.euler + mp.log(mp.pi)) + mp.quad(
        integrand, [mp.mpf(j) / 4 for j in range(13)] + [4, 8, mp.inf])
    terms = [2 * mp.re(transform(t)) for t in zeros]
    rhs = pole + comb + arch
    print(f"smooth: dps={mp.mp.dps}, quadrature multiplier={resolution}", flush=True)
    print("  pole, comb, arch:", *(mp.nstr(v, 18) for v in (pole, comb, arch)), flush=True)
    for count in (40, 80):
        lhs = mp.fsum(terms[:count])
        print(f"  {count} pairs: lhs={mp.nstr(lhs,18)}, residual={mp.nstr(lhs-rhs,8)}", flush=True)
    print("  last 40 terms absolute sum:", mp.nstr(mp.fsum(abs(v) for v in terms[40:]), 8), flush=True)
    return mp.fsum(terms), rhs


def dh_checks():
    k = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    coeffs = [0, 1, k, -k, -1]

    def dh(s):
        return mp.fsum(coeffs[r] * mp.zeta(s, mp.mpf(r) / 5)
                       for r in range(1, 5)) / mp.power(5, s)

    def completed(s):
        return mp.power(5 / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * dh(s)

    chi = [0, 1, mp.j, -mp.j, -1]
    tau = mp.fsum(chi[r] * mp.exp(2 * mp.pi * mp.j * r / 5) for r in range(1, 5))
    omega = tau / (mp.j * mp.sqrt(5))
    root_error = abs((1 - mp.j * k) * omega - (1 + mp.j * k))
    print("DH root-number identity error:", mp.nstr(root_error, 6), flush=True)
    errors = []
    for s in (mp.mpc('0.3', '2.7'), mp.mpc('1.9', '-4.1'), mp.mpc('0.71', '33.3')):
        err = abs(completed(s) - completed(1 - s)) / abs(completed(s))
        errors.append(err)
        print("  DH functional equation:", mp.nstr(s, 8), mp.nstr(err, 6), flush=True)
    b = {}
    for n in range(2, 7):
        b[n] = coeffs[n % 5] * mp.log(n) - mp.fsum(
            b[d] * coeffs[(n // d) % 5] for d in range(2, n) if n % d == 0)
    print("  b(3) =", mp.nstr(b[3], 18), "; b(6) =", mp.nstr(b[6], 18), flush=True)
    assert b[3] < 0 and abs(b[3] + k * mp.log(3)) < mp.mpf('1e-30')
    assert abs(b[6] - (1 + k*k) * mp.log(6)) < mp.mpf('1e-30')
    assert root_error < mp.mpf('1e-30') and max(errors) < mp.mpf('1e-30')


def resolvent_check():
    for a in (mp.mpf('0.75'), mp.mpf('1.5'), mp.mpf(4)):
        # Directly evaluate regularized (W), including its cusp-dependent limit.
        def integrand(v):
            if not v:
                return a - mp.mpf('1.5')
            return 2 * (mp.exp(-2*v) - mp.exp(-(a+mp.mpf('0.5'))*v)) / (-mp.expm1(-2*v))
        numeric = -(mp.euler + mp.log(mp.pi)) + mp.quad(integrand, [0, 1, 4, mp.inf])
        closed = mp.digamma((a + mp.mpf('0.5')) / 2) - mp.log(mp.pi)
        error = abs(numeric - closed)
        print("resolvent arch:", a, "error", mp.nstr(error, 6), flush=True)
        assert error < mp.mpf('1e-30')


def complex_atom_checks():
    """Test the proof's transforms on finite toy divisors, NOT members of S1-S3.

    Integrate the Fourier transform directly and differentiate an explicit
    polynomial independently. Include a conjugate quartet, repeated real
    atoms, and both parities of the central multiplicity.
    """
    z = mp.mpc(2, '0.3')
    nonzero = [z, -z, mp.conj(z), -mp.conj(z), 3, -3, 3, -3]
    for central in (1, 2):
        atoms = [0] * central + nonzero

        def numerator(x):
            return (x**central * (1 + x*x/(z*z))
                    * (1 + x*x/mp.conj(z*z)) * (1 + x*x/9)**2)

        for a in (mp.mpf('0.75'), mp.mpf('1.5')):
            integral_sum = mp.fsum(
                2 * mp.quad(lambda u: mp.exp(-a*u) * mp.cos(atom*u),
                            [0, 4, 8, 16, 32, 64, 128, mp.inf])
                for atom in atoms)
            derivative = 2 * mp.diff(numerator, a) / numerator(a)
            error = abs(integral_sum - derivative)
            print(f"complex-atom integral/product: m0={central}, a={a}, error={mp.nstr(error,6)}", flush=True)
            assert error < mp.mpf('1e-25')

        def completed(s):
            # Deliberately use the gamma-removal and recompletion operations.
            f0 = (mp.power(mp.pi, s/2) * numerator(s-mp.mpf('0.5'))
                  / (s*(s-1)*mp.gamma(s/2)))
            return mp.power(mp.pi, -s/2) * mp.gamma(s/2) * f0

        s = mp.mpc('0.8', '0.2')
        parity_error = abs(completed(s) - (-1)**central * completed(1-s))
        print(f"  completion parity m0={central}: error={mp.nstr(parity_error,6)}", flush=True)
        assert parity_error < mp.mpf('1e-30')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--calibration-only', action='store_true', help='Skip the slower smooth zero sums.')
    args = parser.parse_args()
    mp.mp.dps = 35
    print(f"Python {platform.python_version()}, mpmath {mp.__version__}; deterministic", flush=True)
    dh_checks()
    resolvent_check()
    complex_atom_checks()
    if not args.calibration_only:
        print("Computing 80 reference zero ordinates...", flush=True)
        zeros = [mp.im(mp.zetazero(k)) for k in range(1, 81)]
        low = smooth_anchor(zeros, 1)
        mp.mp.dps = 50
        high = smooth_anchor(zeros, 2)
        # The reference ordinates retain their original 35-digit precision.
        stability = max(abs(x-y) for x, y in zip(low, high))
        residual = abs(high[0] - high[1])
        print("quadrature/precision stability:", mp.nstr(stability, 8), flush=True)
        assert stability < mp.mpf('1e-8'), 'Quadrature has not stabilized'
        assert residual < mp.mpf('1e-5'), 'Truncated smooth anchor mismatch'
    print("PASS (numerical calibration only; no certified infinite tails)", flush=True)


if __name__ == '__main__':
    main()
