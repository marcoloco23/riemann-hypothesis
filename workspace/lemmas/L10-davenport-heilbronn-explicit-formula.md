# L10 — Davenport–Heilbronn calibration with exact constants

**Tag: PROVED (written derivation, same-agent audit, 2026-09-05).
Not independently reviewed or formalized.** Numerical checks are separate in
`scratch/explicit-formula-check/check_smooth_and_dh.py`.

## 1. Completion and a zero-free starting half-plane

Let `χ` be the primitive odd character modulo 5 with `χ(2)=i`, and let

```
κ = (√(10-2√5)-2)/(√5-1),     A=(1-iκ)/2,
f(s)=A L(s,χ)+conj(A)L(s,conj(χ)).
```

Its real Dirichlet coefficients, indexed by residue modulo 5, are
`a(0),…,a(4) = 0,1,κ,-κ,-1`, with `0<κ<1`.
Define the completion

```
H(s)=(5/π)^((s+1)/2) Γ((s+1)/2) f(s).
```

For an odd primitive character the completed functional equation has root
number `ω=τ(χ)/(i√5)` ([KMP2010] p. 464; [DLMF25.15] equations 5–6).
The finite Gauss sum here is

```
τ(χ)=-2 sin(π/5)+2i sin(2π/5),
ω=[2 sin(2π/5)+2i sin(π/5)]/√5.
```

The half-angle identities give `κ=Im(ω)/(1+Re(ω))`, hence
`(1-iκ)ω=1+iκ`. The conjugate-character root number is `conj(ω)`.
Combining the two functional equations therefore gives **`H(s)=H(1-s)`**.
Also `H(conj(s))=conj(H(s))`. Nonprincipal character L-functions are entire;
their odd trivial zeros cancel the simple gamma poles ([DLMF25.15],
entireness statement and equation 8). Hence H is entire.

Its finite order can be checked directly. Since a(n) is periodic with mean
zero, `A(x)=Σ_{n≤x}a(n)` is bounded by a constant C. Partial summation gives
`f(s)=s∫_1^∞ A(x)x^{-s-1}dx` for `Re s>0`, first in the Dirichlet-series
domain and then by analytic continuation of the absolutely convergent integral.
For `Re s≥1/2`, this gives `|f(s)|≤2C|s|`. If `|s|≤R` in that half-plane,
the gamma integral gives `|Γ((s+1)/2)|≤Γ((Re s+1)/2)`; real Stirling bounds
the latter by `exp(O(R log(2+R)))`. The conductor factor adds only `exp(O(R))`.
Reflect the other half of the disc using `H(s)=H(1-s)` and radius R+1.
Thus `max_{|s|≤R}|H(s)|≤exp(O(R log(2+R)))`, proving order at most 1.

For `Re s≥2`,

```
|f(s)-1| ≤ Σ_{n≥2} n^{-2} = ζ(2)-1 < 1.
```

For example `Σ_{n≥2}n^{-2}≤1/4+∫_2^∞t^{-2}dt=3/4` is enough.
Thus H has no zeros there. By the functional equation all zeros of H lie
in `-1<Re s<2`, or `|Im z|<3/2` under `z=-i(s-1/2)`.
The elementary bound is deliberately wider than the classical critical strip;
there is no claim that all DH zeros lie in `0<Re s<1`.

## 2. Exact signed comb

For `Re s≥2`, expand `(1+(f-1))^{-1}` geometrically in the Banach algebra
of absolutely convergent Dirichlet series. Its norm ratio is at most `3/4`.
The derivative series also converges absolutely there, so

```
-f'(s)/f(s)=Σ_{n≥2} b(n)n^{-s},
b(n)=a(n)log n - Σ_{d|n, 2≤d<n} b(d)a(n/d).
```

All coefficients are **real**, not generically complex for this specific f.
In particular

```
b(2)=κ log2 >0,
b(3)=-κ log3 <0,
b(6)=(1+κ²)log6 >0.
```

The last identity follows by using the proper divisors 2 and 3 in the
recursion and `a(6)=1`. It also gives an explicit non-prime-power coefficient.
These are exact algebraic identities, not signs inferred from a finite scan.

## 3. Explicit formula

Let `Z_H` be the zero multiset of H in the z-plane. For every even real
`g∈C_c^∞(R)` with `ĝ(z)=∫g(u)e^{-izu}du`,

```
Σ_{z∈Z_H} ĝ(z)
 = -2Σ_{n≥2} b(n)n^{-1/2}g(log n)
   +(1/2π)∫_R ĝ(t)[Re ψ₀(3/4+it/2)+log(5/π)]dt.          (DH-EF)
```

There is **no pole background**: H is entire and its logarithmic derivative
has poles only at its zeros. The prime-side sum is finite for these tests.

Here is the contour justification without importing ζ-specific zero-spacing
bounds. Entire order ≤1 implies `N_H(R)=O(R^{3/2})` by Jensen's formula;
this deliberately loose bound suffices. Choose heights `T_j∈[j,j+1]`
at distance at least `c j^{-3/2}` from every zero ordinate. Such heights exist
by excluding intervals around the `O(j^{3/2})` ordinates in a bounded
neighborhood of that interval, and taking c small enough. Reflection gives
the negative heights as well.

The genus-one Hadamard logarithmic derivative on the bounded horizontal
segments at these heights is `O(T_j^3)`: zeros of modulus `≤2T_j` contribute
at most their count times `O(T_j^{3/2})`, plus the `1/ρ` terms; the far tail
is bounded by `C T_j Σ_{|ρ|>2T_j}|ρ|^{-2}=O(T_j^{1/2})`.
Possible finitely many small zeros and the constant exponential factor cause
only lower-order terms. Compact smooth tests decay to every polynomial order
uniformly across the fixed vertical strip, so horizontal integrals vanish.
The zero sums converge absolutely by the same count and decay.

Run the L8 contour proof with right line `Re s=2+δ` and left line
`Re s=-1-δ`, `δ>0`. On the right line

```
H'/H(s)=1/2 log(5/π)+1/2 ψ₀((s+1)/2)-Σ b(n)n^{-s}.
```

The left line folds by `H(s)=H(1-s)`. Absolute Dirichlet convergence justifies
the comb evaluation. The gamma term shifts to `Re s=1/2` without crossing
a pole (its nearest one is at -1). Fourier inversion then yields (DH-EF).

Equivalently, the DH archimedean distribution is

```
W_H(g)=(log(5/π)-γ_E)g(0)
       +∫_0^∞ 2[e^{-2v}g(0)-e^{-3v/2}g(v)]/(1-e^{-2v}) dv.
```

The numerator is `O(v)` at 0 and the tail is integrable. Away from 0 its
density is `-e^{-3|u|/2}/(1-e^{-2|u|})`. As in L8, the gamma-integral
derivation can be justified first with a lower v cutoff and then by
dominated convergence; cancellation at 0 must be retained.

## 4. Three distinct exclusions from L8's class

1. The actual DH comb has negative coefficient `b(3)/√3`.
2. The completion has conductor 5 and odd gamma factor, and has no pole
   background. These differ from the *fixed* data in (S3).
3. Even arbitrarily reweighting its integer-log comb cannot repair this
   background mismatch. Test inside `0<|u|<log2`, away from 0, where both
   combs vanish. The difference between the DH smooth density and ζ's
   pole-plus-archimedean density is

   `1/[2cosh(u/2)] - 2cosh(u/2) < 0`.

   A nonzero nonnegative even bump in that interval detects the difference.
   Thus `Z_H` cannot satisfy (S3) for any weights, irrespective of signs.

The last point establishes exclusion independently of zero location. None
of these facts is a theorem forcing real zeros from comb positivity for
variable backgrounds. The L9 singleton theorem is specific to ζ's background.

## References and verification

- [KMP2010], pp. 463–464, DOI 10.4171/CMH/202:
  https://ems.press/content/serial-article-files/43234
- [DLMF25.15], Dirichlet series, Hurwitz representation, functional equation
  and Gauss sum: https://dlmf.nist.gov/25.15
- [Titchmarsh], [IK]: classical finite-order factorization and real Stirling
  bounds, as already used in the repository's background. The finite order
  of H itself is proved in §1 using bounded periodic partial sums.
- The coefficient recursion, Gauss sum algebra, strip bound, contour estimate,
  and background exclusion are derived above. No cited off-line zero is needed.
- Numerical checks reproduce the root-number identity, three functional-equation
  values, and b(3), b(6); they do not enter the proof.

**Used by:** L8 §7 and the Fourier-rigidity audit.
