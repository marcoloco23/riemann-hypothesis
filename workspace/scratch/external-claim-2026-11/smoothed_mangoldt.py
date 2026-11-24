#!/usr/bin/env python3
"""Numerical regression for the smoothed von Mangoldt statistic

    F(X) = sum_{n<=X} Lambda(n) (X/n - 1)  -  X log X  +  (1 + gamma) X

and its explicit formula

    F(X) = sum_rho X^rho / (rho (1 - rho)) + log(2 pi) - sum_{k>=1} X^(-2k) / (2k (2k+1)).

This is evidence for a standard identity, not a proof, and it certifies no infinite
tail. It assumes nothing about the location of zeros beyond the first NZ, which
mpmath locates on the critical line.

Usage: python smoothed_mangoldt.py [NZ]      (default 400 zeros; about two minutes)
"""
from __future__ import annotations

import math
import sys

import mpmath as mp

EULER = 0.57721566490153286
C_RH = 2 + EULER - math.log(4 * math.pi)  # sum over all rho of 1/(rho(1-rho))


def mangoldt_terms(limit: int):
    """Yield (n, Lambda(n)) for prime powers n <= limit."""
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = bytearray(len(range(p * p, limit + 1, p)))
    for p in range(2, limit + 1):
        if sieve[p]:
            logp = math.log(p)
            q = p
            while q <= limit:
                yield q, logp
                q *= p


def prime_side(x: float, terms) -> float:
    total = math.fsum(lam * (x / n - 1.0) for n, lam in terms if n <= x)
    return total - x * math.log(x) + (1 + EULER) * x


def zero_side(x: float, gammas) -> float:
    lx = math.log(x)
    zeros = math.sqrt(x) * math.fsum(2 * math.cos(g * lx) / (0.25 + g * g) for g in gammas)
    trivial = math.fsum(x ** (-2 * k) / (2 * k * (2 * k + 1)) for k in range(1, 60))
    return zeros + math.log(2 * math.pi) - trivial


def main() -> int:
    nz = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    mp.mp.dps = 20
    gammas = [float(mp.zetazero(k).imag) for k in range(1, nz + 1)]
    partial = math.fsum(2 / (0.25 + g * g) for g in gammas)
    tail = C_RH - partial  # what the omitted zeros contribute at most, per sqrt(X)
    print(f"zeros used: {nz}, last ordinate {gammas[-1]:.4f}")
    print(f"sum over used zeros of 2/(1/4+g^2) = {partial:.8f}")
    print(f"2 + gamma - log(4 pi)              = {C_RH:.8f}   (omitted tail {tail:.2e})")
    if not 0 < tail < 0.01:
        print("FAIL: partial sum of 1/(rho(1-rho)) inconsistent with the closed form")
        return 1

    xs = [10.5, 100.5, 1000.5, 10000.5, 100000.5, 1000000.5, 2000000.5]
    terms = list(mangoldt_terms(int(max(xs))))
    ok = True
    print("\n        X      F(X) primes       F(X) zeros     |diff|/sqrt(X)   (F-log 2pi)/sqrt(X)")
    for x in xs:
        fp, fz = prime_side(x, terms), zero_side(x, gammas)
        diff = abs(fp - fz) / math.sqrt(x)
        ratio = (fp - math.log(2 * math.pi)) / math.sqrt(x)
        good = diff <= tail * 1.001 + 1e-9 * x / math.sqrt(x) and abs(ratio) <= C_RH + 1e-6
        ok &= good
        print(f"{x:11.1f} {fp:16.8f} {fz:16.8f} {diff:16.3e} {ratio:20.6f}  {'ok' if good else 'FAIL'}")
    print(f"\nbound checked: |diff|/sqrt(X) <= omitted tail; |(F - log 2pi)/sqrt(X)| <= {C_RH:.6f}")
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
