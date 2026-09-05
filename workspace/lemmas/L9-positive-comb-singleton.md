# L9 — The fixed-background positive-comb class is a singleton

**Tag: PROVED (written proof; same-agent adversarial audit, 2026-09-05).
Not independently reviewed or formalized.** No novelty claim is made: this is an
application of Hamburger's classical converse theorem to the class defined in L8.

## Statement

Let `(Z,w)` satisfy **exactly** L8 §6 (S1)–(S3), including `w_n ≥ 0`.
Then `Z = Z_ζ` with multiplicities and `w_n = Λ(n)/√n` for every `n ≥ 2`.
Consequently `(R′) ⇔ RH`, and the proposed relaxation supplies no distinct systems.
This theorem neither assumes nor proves that the atoms of `Z_ζ` are real.

In fact, only `N_Z(T)=O(T log(2+T))` from (S2) is needed. Constants below can
depend on the given system. Use L8's Fourier convention throughout.

## 1. Positivity supplies the missing coefficient estimate

Fix a nonnegative even `φ ∈ C_c^∞(R)`, supported in `[-1,1]`, with `φ≥1` on
`[-1/2,1/2]`. For `U≥2` set `g_U(u)=φ(u-U)+φ(u+U)`.
Its transform is `2 cos(Uz) φ̂(z)`. The strip bound and L8's Paley–Wiener estimate give

```
|Σ_Z ĝ_U(z)| ≤ C e^{U/2} Σ_Z (1+|Re z|)^(-3) ≤ C_Z e^{U/2}.
```

The pole term is `O(e^{U/2})`. Since `g_U(0)=0`, L8 (W) gives
`|W_∞(g_U)|=O(e^{-U/2})`. Rearranging (S3), with positivity on the comb side,

```
Σ_{|log n-U|≤1/2} w_n ≤ Σ_n w_n g_U(log n) ≤ C_Z e^{U/2}.
```

The finitely many small indices cause no problem. Covering the log axis by
unit intervals and summing a geometric progression proves

```
M_w(X) := Σ_{2≤n≤X} w_n = O_Z(√X).                         (1)
```

Thus, for every real `a>1/2`, `Σ w_n n^{-a}<∞`. All corresponding series
converge normally on closed right half-planes with boundary `a>1/2`.
No individual Ramanujan bound or prime-power support has been assumed.

### Independent normalization check: a PNT for the comb weights

Before any reconstruction or use of Hamburger, the same assumptions imply

```
M_w(X) ~ 2√X,       Ψ_w(X):=Σ_{2≤n≤X}w_n√n ~ X.          (1a)
```

Here strict strip containment matters: every individual atom satisfies
`|Im z|<1/2`, although there need not be a uniform gap from the boundary.
Fix any real `φ∈C_c^∞(R)`, not necessarily even, supported in `[-B,B]`.
For `U>B+1`, use the legal even test

```
g_U(u)=φ(u-U)+φ(-u-U),
ĝ_U(z)=e^{-iUz}φ̂(z)+e^{iUz}φ̂(-z).
```

For each atom z, `e^{-U/2}ĝ_U(z)→0`. Uniformly in U its absolute value is
at most `C_φ(1+|Re z|)^{-3}` by Paley–Wiener and the closed-strip bound.
This summable majorant proves `e^{-U/2}Σ_Z ĝ_U(z)→0` by dominated convergence.
It does not assume that Im z=0 or that the atoms stay uniformly away from
the edges. Since the supports avoid 0, `W_∞(g_U)=O_φ(e^{-U/2})`.
The pole term is exactly

```
2e^{U/2}∫φ(v)e^{v/2}dv + 2e^{-U/2}∫φ(v)e^{-v/2}dv.
```

Only the first translated bump contributes at positive log n. Dividing
(S3) by `2e^{U/2}` therefore gives

```
e^{-U/2}Σ_n w_n φ(log n-U) → ∫φ(v)e^{v/2}dv.             (1b)
```

To pass from local tests to the cumulative sum, fix K>0. The positive
measures `ν_U=Σ_n e^{-U/2}w_n δ_{log n-U}` converge on compact smooth
tests to the measure `e^{v/2}dv`. Sandwich the indicator of `[-K,0]`
between nonnegative compact smooth functions differing only in arbitrarily
small neighborhoods of its endpoints. The limiting measure has no mass
at those endpoints, so

```
ν_U([-K,0]) → ∫_{-K}^0 e^{v/2}dv = 2(1-e^{-K/2}).
```

The discarded lower tail obeys, by (1),
`ν_U((-∞,-K))≤C e^{-K/2}` for sufficiently large U. Combining this bound
with the preceding limit, first letting U→∞ and then K→∞, proves
`e^{-U/2}M_w(e^U)→2`. This is the first assertion of (1a).
Partial summation then gives

```
Ψ_w(X)=√X M_w(X) - (1/2)∫_1^X M_w(t)t^{-1/2}dt = X+o(X).
```

The integrated error is o(X) by splitting the integral at a fixed large
threshold and using the little-o bound above it. This proves (1a) directly
from S1–S3. It is an asymptotic normalization check, not an RH-strength
error estimate, and it is not needed for the reconstruction below. ∎

## 2. Extend (S3) to the resolvent test

Fix real `a>1/2` and put `g_a(u)=e^{-a|u|}`. This function is not smooth at 0;
the extension must be justified, not asserted.

Choose a nonnegative even smooth approximate identity `η_ε` supported in
`[-ε,ε]`, `0<ε<1`, of integral 1. Let `h_ε=g_a*η_ε`, and then
`h_{ε,R}=h_ε χ(u/R)`, where `χ` is even, smooth, equals 1 on `[-1,1]`,
vanishes outside `[-2,2]`, satisfies `0≤χ≤1`, and `R≥1`. These are legal tests.

Uniformly in `ε,R`, the weighted L1 norms of `h_{ε,R}` and its second
derivative, with weight `e^{|u|/2}`, are bounded. To check the only delicate
term, use the distributional identity

```
g_a'' = a² g_a du - 2a δ_0.
```

Its weighted total variation is finite; convolution multiplies the bound by
at most `e^{1/2}`, and the cutoff product terms are bounded by the weighted
L1 norms of `h_ε,h_ε'` and uniformly bounded cutoff derivatives. Hence, by
two integrations by parts and the direct L1 bound,

```
|ĥ_{ε,R}(x+iy)| ≤ C_a (1+|x|)^(-2),   |y|≤1/2.             (2)
```

This is summable against the counting measure of Z. First let `R→∞`, then
`ε→0`; transforms converge pointwise by weighted L1 convergence, so dominated
convergence applies to the zero sum. The same limits apply to the pole term.
For the comb, `|h_{ε,R}(u)|≤C_a e^{-a|u|}` and (1) give domination.

For (W), the approximants are uniformly bounded and Lipschitz near 0.
Consequently `h(0)-e^{3v/2}h(v)=O(v)` uniformly for `0<v≤1`; the singular
factor in (W) is `O(1/v)`. At infinity the integrands are dominated by a
constant times `e^{-2v}+e^{-(a+1/2)v}`. This proves convergence of (W),
including its regularization at the origin.

Now `ĝ_a(z)=2a/(a²+z²)`. Direct substitution in (W), followed by `t=2v`
and the digamma integral used in L8, gives

```
W_∞(g_a) = ψ₀((a+1/2)/2)-log π.
```

The extended identity is therefore

```
Σ_{z∈Z} 2a/(a²+z²)
 = 2/(a-1/2)+2/(a+1/2)
   + ψ₀((a+1/2)/2)-log π - 2Σ_{n≥2} w_n n^{-a}.           (3)
```

## 3. Reconstruct a finite-order entire numerator

Let `m_0` be the multiplicity of 0 in Z. Select one representative of each
nonzero pair `{z,-z}`, with its multiplicity, and form

```
E(x) = x^{m_0} Π_{pairs {z,-z}} (1+x²/z²).
```

The count assumption implies `Σ_{z≠0}|z|^{-2}<∞`; local finiteness and
the finite count in bounded real windows exclude accumulation at 0.
The product converges normally on compact sets and has exactly the zeros
`x=iz`, with the required multiplicities. It is independent of representative
choice. Its parity is `E(-x)=(-1)^{m_0}E(x)`; evenness is **not** presumed.

For completeness its finite order follows directly: if
`n(t)=#{z≠0: |z|≤t}=O(t log(2+t))`, then

```
log |E(x)| ≤ m_0 log r + 1/2 ∫ log(1+r²/t²) dn(t)
           = O(r log(2+r)),     |x|=r≥2.
```

Integration by parts bounds the integral by a constant times
`r²∫_{t_0}^∞ log(2+t)/(t²+r²) dt = O(r log(2+r))`, where `t_0>0`
is smaller than all nonzero atom moduli. This also handles finitely many
small atoms. The entire function has order at most 1.

On `x=a>1/2` there are no zeros: a zero there would require an atom
with imaginary part of magnitude `a`. Logarithmic differentiation yields

```
E'(a)/E(a) = m_0/a + Σ_pairs 2a/(a²+z²)
           = (1/2) Σ_{z∈Z} 2a/(a²+z²).                  (4)
```

Define initially as a meromorphic function on C

```
F_0(s) = π^{s/2} E(s-1/2) / [s(s-1) Γ(s/2)].
```

`(s-1)F_0(s)` is entire of finite order: `1/[sΓ(s/2)]` is entire,
including at 0. The reciprocal-gamma product gives logarithmic maximum
`O(r log(2+r))`: split its factors at `k=2r`, bound the finitely many
linear and exponential factors by `O(r log(2+r))`, and the remaining
logarithms by `O(r² Σ_{k>2r}k^{-2})=O(r)`. Thus it has order at most 1.
There are no other possible poles. Equations (3)–(4) imply, for
real `s>1`,

```
F_0'(s)/F_0(s) = -Σ_{n≥2} w_n √n n^{-s}.                 (5)
```

## 4. Recover a normalized Dirichlet series and its functional equation

Set `c_n=w_n√n/log n` and

```
F_D(s)=exp(Σ_{n≥2} c_n n^{-s}),     Re s>1.
```

The exponent and its derivative converge absolutely by (1); differentiating
gives (5). F_0 is holomorphic and nonzero for Re s>1, since all zeros of
its numerator have `0<Re s<1`. Thus `F_0/F_D` is a nonzero constant C on the real interval
`s>1`, and by holomorphic uniqueness throughout the right half-plane.
Set `F=F_0/C`, so `F=F_D` there and `F(σ)→1` as `σ→∞`.

Exponentiating the absolutely convergent series produces an ordinary
Dirichlet series `F(s)=Σ_{n≥1} A_n n^{-s}`, absolutely convergent for
`Re s>1`, with `A_1=1`. Indeed the total absolute sum of all convolution
terms on a line `Re s=σ>1` is at most
`exp(Σ c_n n^{-σ})<∞`; each coefficient receives finitely many terms
because all factors have index ≥2. This is not an Euler-product assumption.

Write `D(s)=π^{-s/2}Γ(s/2)F(s)`. The product parity gives the meromorphic identity

```
D(s)=ε D(1-s),       ε=(-1)^{m_0}.
```

Apply Hamburger's **two-function** converse theorem to `f=F` and `g=εF`:
both are ordinary Dirichlet series absolutely convergent for `Re s>1`;
both become entire functions of finite order after multiplication by `s-1`;
and their completed functions satisfy the required equation.
The theorem gives `f=g=cζ`. Since `A_1=1`, `c=1`; since F is nonzero,
`ε=1`. In particular a central atom of odd multiplicity cannot slip through
the argument. The theorem is stated in [KMP2010], introduction, p. 463.

It follows that `F=ζ`. Comparing the completed divisors yields `Z=Z_ζ`.
Equation (5) and uniqueness of absolutely convergent Dirichlet series yield
`w_n√n=Λ(n)` for all n. Alternatively, after identifying Z, subtract L8a
and isolate each comb atom with a smooth test. This completes the proof. ∎

## Audit and implications

- Logical chain: S1–S3 → translated-bump estimate → legal resolvent test →
  canonical product → Dirichlet series → Hamburger → singleton. Neither L8b
  nor RH occurs as an input. L8a supplies the known member of the class.
- The exact count asymptotic and conjugation symmetry are stronger than needed;
  retaining them leaves S1–S3 unchanged.
- Weight positivity is used at (1), to bound an entire interval of weights.
  Strip containment controls the exponential growth and fixes convergence at
  `Re s>1`. The prescribed background supplies precisely ζ's completion.
- DH has a different completion and signed logarithmic coefficients (L10).
  Uniqueness here says nothing about reality, so there is no DH contradiction.
- The preliminary estimate (1) by itself is not a PNT. The translated-test
  limit (1b), strict strip containment and positivity additionally prove
  the PNT asymptotics (1a) without singleton identification or Hamburger.
- Same-agent review checked the cusp, central multiplicity, sign, order,
  Dirichlet-series reconstruction and normalizing constant explicitly.
  External independent review and Lean verification remain outstanding.
- A further numerical calibration uses finite toy divisors with nonreal
  conjugate quartets, repeated real atoms, and central multiplicities 1 and 2.
  Direct Fourier integration agrees with differentiation of their explicit
  product; recompletion retains the expected parity. These toys do not
  satisfy S2–S3 and are not examples in the positive-comb class.

## References

- [KMP2010] J. Kaczorowski, G. Molteni, A. Perelli, *A converse theorem for
  Dirichlet L-functions*, Comment. Math. Helv. 85 (2010), 463–483,
  DOI 10.4171/CMH/202; Hamburger theorem stated on p. 463.
  https://ems.press/content/serial-article-files/43234
- L8 §§1–3: Fourier convention, convergence and regularized archimedean term.
- Classical reciprocal-gamma product: NIST DLMF 5.8.2,
  https://dlmf.nist.gov/5.8.E2 (used only for its entire finite-order property).
- Digamma integral: NIST DLMF 5.9.16,
  https://dlmf.nist.gov/5.9.E16, for the regularized evaluation in §2.

**Used by:** Fourier-rigidity attempt; replaces the proposed K1 search in the
fixed-background class. This is characterization progress, not progress on
the real-support conclusion of RH.
