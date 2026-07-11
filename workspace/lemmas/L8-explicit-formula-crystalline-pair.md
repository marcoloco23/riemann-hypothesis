# L8 — The Weil explicit formula as an unconditional crystalline-pair statement

**Tag:** L8a PROVED — hostile re-read PASSED 2026-07-12 (independent agent: every
sign/constant re-derived, its own numerics to 1e−29; plus the repo numeric anchor,
17-digit constant cancellation). L8b PROVED — hostile re-read 2026-07-12 found one
fixable gap in Step C's shifted-anchor stage (collision-avoidance + `|h|<¼`), both
repairs applied same-day; **the repaired subsection wants one more independent
re-read** before load-bearing use. L8c PROVED — re-read PASSED (one operator-sign
typo fixed). §3's density remark: factor-2 error found by review, FIXED. §6
definitions + conjecture (R′) are NOT results. Numerical cross-check (motivational
only, docs/01 B1): `scratch/explicit-formula-check/`.

This is Rung 0 of `attempts/fourier-rigidity/` (ROADMAP §A, §D). Everything here is
unconditional: **RH is never assumed**, no docs/03 equivalent is assumed, and the zero
multiset is allowed complex atoms throughout.

## 1. Setup and conventions

Let `ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)` (entire, order 1, `ξ(s)=ξ(1−s)`,
`ξ(s̄) = conj ξ(s)`; docs/02 §1). Nontrivial zeros `ρ = β+iγ`, `0<β<1`, counted with
multiplicity.

**z-map.** `z(ρ) := −i(ρ−½)`, so `ρ = ½+iz(ρ)` and `z(ρ) = γ − i(β−½)`. Define the
zero multiset

```
Z_ζ := { z(ρ) : ρ nontrivial zero of ζ }  ⊂  S := { z : |Im z| < ½ }.
```

- `Z_ζ ⊂ S` strictly (all zeros have `0<β<1`; docs/02 §3).
- `Z_ζ` is closed under `z ↦ −z` (from `ρ ↦ 1−ρ`) and under `z ↦ z̄`
  (from `ρ ↦ 1−ρ̄`, using both symmetries). RH ⟺ `Z_ζ ⊂ ℝ`.
- Counting: `N_{Z_ζ}(T) := #{z ∈ Z_ζ : |Re z| ≤ T} = (T/π)log(T/2π) − T/π + O(log T)`
  (Riemann–von Mangoldt, both signs of γ; docs/02 §3, [Titchmarsh §9.4]).

**Test class.** `𝒯 := { g ∈ C_c^∞(ℝ) : g even, real-valued }`, and
`ĝ(z) := ∫_ℝ g(u)e^{−izu}du` (entire; even; real on `ℝ ∪ iℝ`).

**(PW) bound.** If `supp g ⊂ [−A,A]`, then for every integer `m ≥ 0`

```
|ĝ(x+iy)| ≤ C_m(g) · e^{A|y|} · (1+|x|)^{−m},     C_m(g) := 2^m max(‖g‖₁, ‖g^{(m)}‖₁).
```

*Proof:* `|ĝ| ≤ ‖g‖₁e^{A|y|}` directly; integrating by parts m times,
`|ĝ(z)| ≤ ‖g^{(m)}‖₁e^{A|y|}/|z|^m ≤ ‖g^{(m)}‖₁e^{A|y|}(2/(1+|x|))^m` for `|x| ≥ 1`
(and the first bound covers `|x| ≤ 1`). ∎

**Convergence of zero sums.** For any multiset `Z ⊂ S` with `N_Z(T) = O(T log T)` and
any `g ∈ 𝒯`: `Σ_{z∈Z}|ĝ(z)| ≤ C_3(g)e^{A/2}Σ_{z}(1+|Re z|)^{−3} < ∞` by partial
summation against `N_Z`. All zero sums below converge absolutely; no ordering is needed.

## 2. L8a — the explicit formula

> **Lemma L8a.** For every `g ∈ 𝒯`:
>
> ```
> Σ_{z∈Z_ζ} ĝ(z)  =  ĝ(i/2) + ĝ(−i/2)                                (pole term)
>                    − 2 Σ_{n≥2} Λ(n) n^{−1/2} g(log n)               (prime comb)
>                    + (1/2π) ∫_ℝ ĝ(t) [ Re ψ₀(¼+it/2) − log π ] dt   (archimedean)
> ```
>
> with `ψ₀ = Γ'/Γ`, every term absolutely convergent (the comb is a finite sum since
> `g` has compact support).

This is the classical Riemann–Weil formula ([IK] Thm 5.12 specialized to ζ; [Weil-EF
framework as in BombieriLagarias1999]); we give a self-contained derivation because the
program lives or dies on its exact constants and test classes.

### Proof

Write `H(s) := ĝ(−i(s−½)) = ∫_ℝ g(u)e^{−(s−½)u}du`, entire, with `H(ρ) = ĝ(z(ρ))`,
and (from (PW)) `|H(σ+it)| ≤ C_m e^{A|σ−½|}(1+|t|)^{−m}` on every vertical strip.
Also set `f(u) := g(u)e^{u/2} ∈ C_c^∞`, so `H` is the two-sided Laplace transform
`H(s) = ∫ f(u)e^{−su}du`, and Fourier inversion on any vertical line gives

```
(1/2πi) ∫_{(σ)} H(s) e^{sv} ds = f(v)          for every σ ∈ ℝ, v ∈ ℝ.        (INV)
```

*(Proof of (INV): `H(σ+it) = FT_t[f e^{−σ·}](t)` with `f e^{−σ·} ∈ C_c^∞`; apply
classical Fourier inversion and multiply by `e^{σv}`.)*

**Step 1 (contour).** `ξ'/ξ` is meromorphic with poles exactly at the zeros of `ξ`
(all in `0<σ<1`), simple with residue = multiplicity. Fix `δ ∈ (0,½)`. There is a
sequence `T_j ↑ ∞` with `T_j ∈ [j, j+1]` and `|T_j − γ| ≫ 1/log T_j` for all zero
ordinates γ, because `N(T+1)−N(T) = O(log T)` ([Titchmarsh Thm 9.2]). For
`−1 ≤ σ ≤ 2`, `|t| ≥ 2`:

```
ζ'/ζ(σ+it) = Σ_{|t−γ|≤1} 1/(σ+it−ρ) + O(log|t|)      ([Titchmarsh Thm 9.6(A)])
```

so on the horizontal segments `t = ±T_j`, `−δ ≤ σ ≤ 1+δ`: each of the `O(log T_j)`
terms is `O(log T_j)`, giving `ζ'/ζ = O(log²T_j)`; and
`ξ'/ξ = ζ'/ζ + 1/s + 1/(s−1) − ½log π + ½ψ₀(s/2)` adds `O(log T_j)` (Stirling).
With `|H| ≤ C_3(1+T_j)^{−3}` on those segments, the horizontal contributions to

```
(1/2πi) ∮_{∂R_j} H(s) (ξ'/ξ)(s) ds ,      R_j := [−δ, 1+δ] × [−T_j, T_j],
```

are `O(T_j^{−3}log²T_j) → 0`. The residue theorem and absolute convergence of the
zero sum (§1) give

```
Σ_{z∈Z_ζ} ĝ(z) = (1/2πi) [ ∫_{(1+δ)} − ∫_{(−δ)} ] H(s)(ξ'/ξ)(s) ds,
```

both vertical integrals absolutely convergent (`ξ'/ξ` grows logarithmically on each
line — on `Re s = 1+δ` from the absolutely convergent Dirichlet series plus Stirling,
on `Re s = −δ` via the functional equation — while `H` decays cubically).

**Step 2 (fold the left line onto the right).** From `ξ(s)=ξ(1−s)`:
`(ξ'/ξ)(s) = −(ξ'/ξ)(1−s)`. Substituting `s = 1−w` in the left-line integral
(upward `Re s = −δ` becomes downward `Re w = 1+δ`, `ds = −dw`):

```
(1/2πi)∫_{(−δ)} H(s)(ξ'/ξ)(s)ds = −(1/2πi)∫_{(1+δ)} H(1−w)(ξ'/ξ)(w)dw .
```

Since `g` is even, `H(1−s) = ∫g(u)e^{(s−½)u}du = H(s)`. Hence

```
Σ_{z∈Z_ζ} ĝ(z) = 2 · (1/2πi) ∫_{(1+δ)} H(s)(ξ'/ξ)(s) ds .                    (FOLD)
```

**Step 3 (expand on `Re s = 1+δ`).** Insert
`ξ'/ξ = [1/s] + [1/(s−1)] + [−½log π] + [½ψ₀(s/2)] + [ζ'/ζ]` into (FOLD) and evaluate
the five pieces. Each piece is separately absolutely integrable against `H` on the line.

*(i) Prime piece.* `ζ'/ζ(s) = −Σ_{n≥2}Λ(n)n^{−s}` absolutely on `Re s = 1+δ`
(docs/02 §2); Fubini is justified by `Σ_nΛ(n)n^{−1−δ}∫|H(1+δ+it)|dt < ∞`. By (INV)
with `e^{sv} = n^{−s}` (i.e. `v = −log n`):
`(1/2πi)∫_{(1+δ)}H(s)n^{−s}ds = f(−log n) = g(log n)n^{−1/2}` (g even). Total, after
the factor 2 from (FOLD): `−2Σ_{n≥2}Λ(n)n^{−1/2}g(log n)`.

*(ii)+(iii) Pole pieces.* For `Re s = 1+δ`: `1/(s−1) = ∫_0^∞ e^{−(s−1)v}dv` and
`1/s = ∫_0^∞ e^{−sv}dv`, both with Fubini justified by `e^{−δv}`- resp.
`e^{−(1+δ)v}`-damping against `∫|H| < ∞`. By (INV):

```
(1/2πi)∫ H(s)/(s−1) ds = ∫_0^∞ e^{v} f(−v)dv = ∫_0^∞ g(v)e^{v/2}dv,
(1/2πi)∫ H(s)/s     ds = ∫_0^∞ f(−v)dv     = ∫_0^∞ g(v)e^{−v/2}dv .
```

Sum: `∫_0^∞ g(v)·2cosh(v/2)dv = ∫_ℝ g(u)cosh(u/2)du = ½[ĝ(i/2)+ĝ(−i/2)]`
(evenness; `ĝ(±i/2) = ∫g(u)e^{±u/2}du`). Doubled by (FOLD): `ĝ(i/2)+ĝ(−i/2)`.

*(iv) `−½log π` piece.* `H` is entire with uniform cubic decay on the strip
`½ ≤ Re s ≤ 1+δ`, so the line of integration shifts to `Re s = ½` (Cauchy on tall
rectangles, horizontal parts → 0), where `H(½+it) = ĝ(t)`:
`(1/2πi)∫_{(1+δ)}H(s)ds = (1/2π)∫_ℝ ĝ(t)dt = g(0)`. Contribution doubled:
`−g(0)log π = −(1/2π)∫ĝ(t)dt·log π` — absorbed into the archimedean integral.

*(v) Gamma piece.* `ψ₀(s/2)` is analytic on `½ ≤ Re s ≤ 1+δ` (nearest pole `s=0`)
with `ψ₀(s/2) = O(log(2+|t|))` there, so the same contour shift is valid:
`(1/2πi)∫_{(1+δ)}H(s)·½ψ₀(s/2)ds = (1/4π)∫_ℝ ĝ(t)ψ₀(¼+it/2)dt`. Doubled:
`(1/2π)∫ĝ(t)ψ₀(¼+it/2)dt`. Since `ĝ(t)` is real and even and
`ψ₀(¼−it/2) = conj ψ₀(¼+it/2)`, the substitution `t ↦ −t` symmetrizes this to
`(1/2π)∫ĝ(t)·Re ψ₀(¼+it/2)dt`.

Collecting (i)–(v) yields L8a. ∎

**Numerical anchor (motivational, not part of the proof).**
`scratch/explicit-formula-check/check_ef.py` verifies the identity end-to-end (all
four terms active) for a compactly supported bump and a Gaussian against the first
1000 zero pairs; see `run-output.txt` there.

**Remark (wider test classes).** L8a extends by standard approximation to the Weil
class (g even, continuous, of bounded variation with `g(u)e^{(½+ε)|u|} ∈ L¹`), and to
even Schwartz g with `ĝ` sub-cubic-decaying on `|Im z| ≤ ½` — the proof is identical
except (PW) is replaced by the assumed decay. We fix `𝒯` because it is closed under
the modulations used in L8b and large enough for uniqueness.

## 3. The crystalline-pair reading (unconditional)

Define the **zero measure** `μ_ζ := Σ_{z∈Z_ζ} δ_z` — an atomic measure on the strip
`S ⊂ ℂ`, real-supported iff RH. For `g ∈ 𝒯` the pairing `⟨μ_ζ, ĝ⟩ := Σ_{Z_ζ}ĝ(z)`
is well defined (§1), so `μ_ζ` acts on the Paley–Wiener space `𝒯̂ := {ĝ : g ∈ 𝒯}`.
Define its Fourier transform as a functional on `𝒯` by `⟨μ̂_ζ, g⟩ := ⟨μ_ζ, ĝ⟩`.
L8a computes it exactly:

```
μ̂_ζ  =  2cosh(u/2)du                                   (pole background, positive)
        −  Σ_{n≥2} (Λ(n)/√n) (δ_{log n} + δ_{−log n})    (prime comb, weights ≥ 0)
        +  W_∞                                          (archimedean distribution)
```

where `W_∞` is the even tempered distribution given for `g ∈ 𝒯` by

```
⟨W_∞, g⟩ = −(γ_E + log π) g(0)
           + ∫_0^∞ [ g(0) − e^{3v/2} g(v) ] · 2e^{−2v}/(1−e^{−2v}) dv           (W)
```

(`γ_E` = Euler's constant). Away from `u = 0`, `W_∞` is the smooth density
`−e^{−|u|/2}/(1−e^{−2|u|})du = −Σ_{k≥0} e^{−(2k+½)|u|}du` — the trivial-zero comb in
exponential clothing (factor pinned by the hostile-review numeric check: a test g
supported near `|u|=2` gives `⟨W_∞,g⟩ = −0.475253` matching this density exactly);
the two pieces of (W) diverge separately and only the combination is defined
(Hadamard-type regularization at 0). Formula (W) follows from
the archimedean term of L8a by inserting `ψ₀(z) = −γ_E + ∫_0^1 (1−x^{z−1})/(1−x)dx`
(`Re z > 0`; [Titchmarsh §4.42-standard], [Remmert1991]) at `z = ¼+it/2`, using
`(1/2π)∫ĝ(t)x^{it/2}dt = g(−(log x)/2)` (Fourier inversion), substituting
`x = e^{−2v}`, and checking the `v→0` cancellation (`integrand → (3/2−¼·…)`-finite;
detail: `[g(0)−e^{3v/2}g(v)] = −(3/2)g(0)v + O(v²)` and `2e^{−2v}/(1−e^{−2v}) = 1/v +
O(1)`). Fubini is justified by the same absolute bounds as in L8a(v).

**Reading.** `(supp μ_ζ, supp μ̂_ζ)` is the program's crystalline pair: the "Fourier
transform" of the zero measure is a **nonnegative atomic comb on ±log(prime powers)
plus one positive smooth background plus one explicit archimedean distribution** —
unconditionally. If RH is false, `μ_ζ` has non-real atoms (complex defects) but the
right-hand side is unchanged: `μ_ζ` is an "almost-real quasicrystal with complex
defects" whose diffraction data is exactly the prime comb. This object is NOT a
Fourier quasicrystal in the technical sense of the literature (its FT has a continuous
part; cf. Kurasov–Sarnak's remark on Guinand's measure) — the program's language must
therefore be "crystalline pair modulo explicit smooth background".

**Equivalent divisor form.** With `D(s) := π^{−s/2}Γ(s/2)ζ(s)` (zeros = nontrivial
zeros, simple poles at `s = 0,1`), the divisor measure `μ̃ := μ_ζ − δ_{i/2} − δ_{−i/2}`
(zeros minus poles in the z-plane) satisfies the cleaner
`μ̃̂ = −comb + W_∞` — the pole background is the FT of the two pole atoms:
`ĝ(i/2)+ĝ(−i/2) = ⟨δ_{i/2}+δ_{−i/2}, ĝ⟩`.

## 4. L8b — the pinning (uniqueness) lemma

> **Lemma L8b.** Let `Z, Z′ ⊂ S = {|Im z| < ½}` be multisets, each locally finite,
> closed under `z ↦ −z`, with `N_Z(T) + N_{Z′}(T) = O(T log T)`. If
>
> ```
> Σ_{z∈Z} ĝ(z) = Σ_{z∈Z′} ĝ(z)      for all g ∈ 𝒯,
> ```
>
> then `Z = Z′` as multisets.

**Corollary (K1, naive class — settled).** The class of "ζ-type crystalline systems"
of ROADMAP §A (atoms in `S`, symmetries, ζ-density, satisfying L8a's identity with the
exact right-hand side) is the singleton `{Z_ζ}`. Hence the naive Rigidity Conjecture
(R) is **equivalent to RH but vacuous as a rigidity target** (no room for any tool to
act: the hypotheses already pin the object). The kill-criterion K1's "fake zero set
with the exact ζ comb" **cannot exist**. The program's content is therefore entirely
in the choice of relaxation (§6), as anticipated in ROADMAP §E-K1.

**Corollary ((R) ⟺ RH, both directions, unconditional).** (⟸ was trivial;) (⟹): if
RH holds, then by L8b the only system in the naive class is `Z_ζ ⊂ ℝ`, so (R) holds.

### Proof of L8b

Let `ν := Z − Z′` denote the (formal) difference: a countable family of atoms
`z_j ∈ S` with weights `c_j ∈ ℤ∖{0}` (multiplicity differences), `Σ_j` locally
finite, `Σ_{|Re z_j|≤T}|c_j| = O(T log T)`, symmetric under `z ↦ −z` (both multisets
are), and

```
Σ_j c_j ĝ(z_j) = 0   for all g ∈ 𝒯,   absolutely convergent (§1).        (H0)
```

We must show all `c_j = 0`.

**Step A (upgrade to all test functions, not just even).** For `ψ ∈ C_c^∞(ℝ)`
(complex, not necessarily even) define `ψ̂(z) := ∫ψ(u)e^{−izu}du`; the (PW) bound of
§1 holds verbatim, so `⟨S, ψ⟩ := Σ_j c_j ψ̂(z_j)` converges absolutely and defines a
distribution `S ∈ 𝒟′(ℝ)` (continuity: `|⟨S,ψ⟩| ≤ C_3(ψ)e^{A/2}Σ_j|c_j|(1+|x_j|)^{−3}`,
and `C_3` is a finite sum of seminorms on any fixed support interval). We claim
`S = 0`.

For even `φ ∈ C_c^∞` and `x₀ ∈ ℝ`, the function `g(u) := φ(u)cos(x₀u)` is in `𝒯`
(complexify: it suffices to treat real φ; general φ by linearity) and
`ĝ(z) = ½[φ̂(z−x₀) + φ̂(z+x₀)]`. Define `G(x₀) := Σ_j c_j φ̂(z_j−x₀)`
(absolutely convergent by (PW)). By the `z↦−z` symmetry of ν and evenness of `φ̂`,
`Σ_j c_j φ̂(z_j+x₀) = Σ_j c_j φ̂(−z_j+x₀)·…` — explicitly, replacing `z_j` by `−z_j`
reindexes ν onto itself and `φ̂(−z_j+x₀) = φ̂(z_j−x₀)` — so both halves are equal and
(H0) gives `G(x₀) = 0` for all `x₀ ∈ ℝ` and all even φ.

Now let `ψ ∈ C_c^∞` be arbitrary and pick even `φ ∈ C_c^∞` with `φ ≡ 1` on
`supp ψ ∪ (−supp ψ)`. Then `ψ = φψ` and, by Fourier synthesis
`ψ(u) = (1/2π)∫ψ̂₀(x₀)e^{ix₀u}dx₀` (`ψ̂₀` = FT of ψ on ℝ, Schwartz):

```
⟨S, ψ⟩ = Σ_j c_j (φψ)^(z_j) = (1/2π)∫ ψ̂₀(x₀) Σ_j c_j φ̂(z_j−x₀) dx₀
       = (1/2π)∫ ψ̂₀(x₀) G(x₀) dx₀ = 0,
```

the interchange justified by
`Σ_j |c_j| ∫|ψ̂₀(x₀)||φ̂(z_j−x₀)|dx₀ ≤ C Σ_j |c_j|(1+|x_j|)^{−3} < ∞`
(convolving the cubic decay of `φ̂` on the strip with the Schwartz decay of `ψ̂₀`).
So `S = 0` in `𝒟′(ℝ)`.

**Step B (extension to Gaussian tests).** Let `W` be the space of `ψ ∈ C^∞(ℝ)` with

```
‖ψ‖_W := max_{m≤3} sup_u (1+|u|)² |ψ^{(m)}(u)| e^{|u|/2} < ∞ .
```

For `ψ ∈ W` the transform `ψ̂(z) = ∫ψ(u)e^{−izu}du` is defined on the closed strip
`|Im z| ≤ ½` (the weight dominates `e^{yu}`), and three integrations by parts —
boundary terms vanish by the decay — give `|ψ̂(x+iy)| ≤ C‖ψ‖_W (1+|x|)^{−3}`
uniformly on the strip. Hence `⟨S,ψ⟩ := Σ_j c_j ψ̂(z_j)` converges absolutely for
every `ψ ∈ W`, with `|⟨S,ψ⟩| ≤ C′‖ψ‖_W` (density `O(T log T)`; only `|y_j| ≤ ½` is
used, valid on the closure of the strip). Now `S = 0` extends from `C_c^∞` to `W`
by cutoff: with `χ_R` smooth, `= 1` on `[−R,R]`, supported in `[−2R,2R]`, derivatives
bounded uniformly in R, we have `ψχ_R ∈ C_c^∞` and `‖ψ − ψχ_R‖_W → 0` as `R → ∞`
(the `(1+|u|)²`-weight of the norm ‖ψ‖ with one extra order of decay beats the
uniformly bounded cutoff derivatives — concretely `‖ψ(1−χ_R)‖_W ≤ C sup_{|u|≥R}
(1+|u|)²max_m|ψ^{(m)}|e^{|u|/2} → 0` for ψ Gaussian-type; for general ψ ∈ W replace
the norm by the corresponding "little-o" subspace, which contains all functions used
below). Hence `⟨S,ψ⟩ = lim_R ⟨S, ψχ_R⟩ = 0` for all such ψ.

Apply this to the family `ψ_{τ,a}(u) := e^{−u²/(2τ)} e^{iau}` (`τ > 0`, `a ∈ ℝ`;
real and imaginary parts lie in the little-o subspace of `W`), whose transform is
`ψ̂_{τ,a}(z) = √(2πτ)·exp(−τ(z−a)²/2)`. Dividing by `√(2πτ)`:

```
A(a, τ) := Σ_j c_j exp( −τ (z_j−a)²/2 ) = 0     for all τ > 0, a ∈ ℝ.      (GAUSS)
```

(Absolute convergence: `|exp(−τ(z_j−a)²/2)| = exp(−τ[(x_j−a)²−y_j²]/2) ≤
e^{τ/8}exp(−τ(x_j−a)²/2)`, summable against the `O(T log T)` density.)

**Step C (localization and extraction).** Suppose some `c ≠ 0`; fix such an atom
`z₀ = ξ₀ + iy₀`. Let `h ∈ ℝ` with `|h| < ¼` (chosen below; `h = 0` allowed) and set
the anchor `a := ξ₀ + h`. Split `(GAUSS)` at this anchor:
`A(a,τ) = A_win(τ) + A_tail(τ)` with window `J := { j : |x_j − ξ₀| ≤ ¾ }`.

*J is finite:* the atoms of ν with `|Re z| ≤ |ξ₀| + 1` number at most
`N_Z(|ξ₀|+1) + N_{Z′}(|ξ₀|+1) < ∞`.

*Tail vanishes:* for `j ∉ J`, `|x_j − a| ≥ ¾ − |h| > ½`, so
`Re[(z_j−a)²] = (x_j−a)² − y_j² ≥ (x_j−a)² − ¼ ≥ (¾−|h|)² − ¼ > 0`. Each term of
`A_tail` thus tends to 0 as `τ → ∞`, and is dominated by its `τ = 1` value, whose sum
converges (Gaussian decay in `x_j` against `O(T log T)` density). By dominated
convergence `A_tail(τ) → 0`.

*Extraction principle:* write the finite window sum as
`A_win(τ) = Σ_{λ ∈ Λ} d_λ e^{−τλ}` where `λ_j := (z_j−a)²/2`, `Λ` the (finite) set of
distinct rate values, `d_λ := Σ_{j∈J: λ_j=λ} c_j`. **Claim: `d_λ = 0` for every
`λ ∈ Λ` with `Re λ ≤ 0`.** Induct over the distinct values of `Re λ ≤ 0` in
increasing order; at the stage of value `r ≤ 0`, multiply `A_win + A_tail ≡ 0` by
`e^{τr}`:

- groups with `Re λ < r`: coefficients already shown to be 0;
- groups with `Re λ = r`: contribute `P(τ) := Σ_{Reλ=r} d_λ e^{−iτ·Imλ}`,
  a trigonometric polynomial with distinct real frequencies;
- groups with `Re λ > r`: their terms `→ 0` as `τ → ∞`;
- `e^{τr}A_tail(τ) → 0` since `r ≤ 0` and `A_tail → 0`.

Hence `P(τ) → 0` as `τ → ∞`; Cesàro means
`d_λ = lim_{U→∞}(1/U)∫_U^{2U} P(τ)e^{iτ·Imλ}dτ` then give `d_λ = 0` for every group
at this stage (distinct frequencies; the finitely many cross terms average out).
Induction complete. *(Groups with `Re λ > 0` are never extracted and never need to
be — the anchor rates below all have `Re ≤ 0`.)*

*Conclusion, case `y₀ = 0`:* take `h = 0`. The rate of `z₀` is `λ = 0`, and its
group is `{z : (z−ξ₀)² = 0} = {z₀}` alone. The claim gives `c(z₀) = d_0 = 0` —
contradiction.

*Conclusion, case `y₀ ≠ 0`:* the rate of `z₀` at anchor `ξ₀+h` is
`λ₀(h) = (iy₀−h)²/2 = (h²−y₀²)/2 − ihy₀`, with `Re λ₀(h) < 0` whenever
`|h| < |y₀|`. Another window atom `z_k ≠ z₀` shares this rate iff
`(z_k−a)² = (iy₀−h)²`, i.e. (factoring the difference of squares)
`z_k = ξ₀ + iy₀ = z₀` — excluded — or `z_k = ξ₀ + 2h − iy₀`, i.e.
`h = (z_k − ξ₀ + iy₀)/2`: at most ONE bad value of h per window atom (and only real
values matter). So choose `h` real with `0 < |h| < min(¼, |y₀|)` avoiding the
finitely many bad values. Then the group of `λ₀(h)` is the singleton `{z₀}`,
`Re λ₀(h) < 0`, and the claim gives `c(z₀) = 0` — contradiction. ∎

**Honest flag.** Hostile re-read PASSED 2026-07-12 for Steps A and B and the
unshifted extraction; the reviewer found the original shifted-anchor stage
incomplete (no collision-avoidance in h, wrong smallness condition on h) — the
version above incorporates both repairs (generic `h` avoiding finitely many
collisions; `|h| < ¼` for tail positivity). The repaired Step C has NOT itself been
independently re-read; a second hostile pass on this subsection is wanted before
L8b is consumed by anything load-bearing. The same reviewer failed to construct a
counterexample to the statement (Gaussian separation of symmetric strip multisets).

## 5. L8c — finite-defect rigidity

> **Lemma L8c.** Let `Z′` be a multiset in `ℂ`, closed under `z ↦ −z`, with
> `Z′ = (Z_ζ ∖ A) ∪ B` for finite multisets `A ⊂ Z_ζ`, `B` (arbitrary atoms in ℂ,
> `A ∩ B = ∅` as multisets). Suppose there exist real weights `(w_n)_{n≥2}` of at most
> polynomial growth — **any signs allowed** — such that for all `g ∈ 𝒯`:
>
> ```
> Σ_{z∈Z′} ĝ(z) = ĝ(i/2)+ĝ(−i/2) − 2Σ_{n≥2} w_n g(log n) + ⟨W_∞, g⟩ .
> ```
>
> Then `A = B = ∅` (so `Z′ = Z_ζ`) and `w_n = Λ(n)/√n` for all n.

*Proof.* Subtract L8a: with `ν := Σ_B δ − Σ_A δ` (finite, `z↦−z`-symmetric — A and B
are separately symmetric since `Z_ζ` and `Z′` are and A = Z_ζ∖Z′-part… precisely:
symmetry of `Z_ζ` and `Z′` forces the finite difference to be symmetric) and
`d_n := 2(Λ(n)/√n − w_n)`:

```
Σ_{finite ν} c_j ĝ(z_j) = Σ_{n≥2} d_n g(log n)      for all g ∈ 𝒯.
```

The left side equals `∫ g(u) h(u) du` with `h(u) := Σ_j c_j e^{−iz_j u}` — a FINITE
sum, so h is real-analytic on ℝ, and even (ν symmetric). The right side is the
pairing of g with the atomic measure `Σ d_n δ_{log n}`, whose even symmetrization is
`½Σ d_n(δ_{log n}+δ_{−log n})`. Both sides are even distributions tested against all
even `g ∈ C_c^∞`, hence equal as distributions on ℝ:
`h(u)du = ½Σ_n d_n (δ_{log n}+δ_{−log n})`. Testing with bumps `ψ_ε` at `log n`
(`ψ_ε(log n)=1`, `0≤ψ_ε≤1`, width ε): left side `≤ sup_{loc}|h|·2ε → 0`, right side
`→ d_n/2` (the points `log n` are isolated). So all `d_n = 0`, hence `h ≡ 0` as a
distribution, hence identically. A finite sum `Σ c_j e^{−iz_j u} ≡ 0` with distinct
`z_j` forces all `c_j = 0` (all derivatives at 0 vanish ⟹ `Σ_j c_j z_j^m = 0` for all
m ⟹ Vandermonde; equivalently apply `∏_{k≠j}(i·d/du − z_k)` and evaluate at 0).
So ν = 0 and `d_n ≡ 0`. ∎

**Corollary (shape of any (R′)-counterexample).** Any non-real system in the relaxed
positive-comb class (§6) must differ from `Z_ζ` in **infinitely many atoms**. In
particular there is no "move one zero off the line and re-tune the comb" counterexample:
K1's hunt (and Rung 3's deformation theory) is intrinsically infinite-dimensional.
Consistent with LITMUS-1: Davenport–Heilbronn's zero set differs from any
L-function zero set in infinitely many atoms.

## 6. The relaxed class and (R′) — definitions only (NOT results)

> **Definition (positive-comb crystalline system).** A pair `(Z, w)`:
> `Z ⊂ S = {|Im z| < ½}` a multiset, `w = (w_n)_{n≥2}`, `w_n ≥ 0`, such that
>
> - **(S1)** Z locally finite, closed under `z ↦ −z` and `z ↦ z̄`;
> - **(S2)** `N_Z(T) = (T/π)log(T/2π) − T/π + O(log T)` (two-sided count, ζ's law);
> - **(S3)** for every `g ∈ 𝒯`, `Σ_{z∈Z}ĝ(z)` converges absolutely and
>
>   `Σ_{z∈Z} ĝ(z) = ĝ(i/2)+ĝ(−i/2) − 2Σ_{n≥2} w_n g(log n) + ⟨W_∞, g⟩`
>
>   with the SAME pole atoms and the SAME archimedean `W_∞` (formula (W)) as ζ.
>
> **(R′)** Every positive-comb crystalline system has `Z ⊂ ℝ`.

Facts already in hand: `(Z_ζ, (Λ(n)/√n))` is in the class (L8a); for FIXED w the
multiset is unique if it exists (L8b applies verbatim — fixed combs cancel in the
difference), so the class injects into `{w ≥ 0 admissible}`; any non-real member is
an infinite defect (L8c). **K1 is now a theorem-or-counterexample question:** exhibit
an admissible `w ≥ 0` whose (unique) multiset is non-real — killing (R′) and refocusing
on ζ-local rigidity (Rung 3) — or prove no such w exists, which IS (R′) ⟹ RH-hard.
Litmus: DH is excluded by `w_n ≥ 0` (its log-derivative coefficients are complex /
sign-indefinite, and its archimedean datum differs — conductor 5, odd gamma factor);
Epstein likewise. Where multiplicativity enters: nothing in (S1)–(S3) forces w to be
supported on prime powers — the class is deliberately larger than "Selberg-like", and
the degree-1 Selberg classification (Kaczorowski–Perelli — pin citation before use;
UNCONFIRMED here) suggests the multiplicative sub-class is just ζ and shifts of
Dirichlet L. The K1 hunt lives exactly in the non-multiplicative freedom of w.

## 7. DH analogue (statement shape; constants UNCONFIRMED pending source pass)

For the Davenport–Heilbronn function `f` (docs/06 LITMUS-1; [DavenportHeilbronn1936],
[BombieriHejhal1995]): f is entire, order 1, satisfies an exact functional equation
with the odd mod-5 gamma factor, is nonzero in some half-plane `Re s > σ₀` (leading
Dirichlet coefficient 1), and `−f'/f = Σ b_f(n)n^{−s}` converges there with complex,
sign-indefinite `b_f(n)` supported on ALL integers (no Euler product ⟹ no
prime-power support, no positivity, no multiplicativity). Running the L8a contour
argument with lines `Re s = σ₀+δ` and `1−σ₀−δ` produces an (EF) of the same shape:
zero measure on one side; a comb with weights `b_f(n)`-derived (complex,
sign-indefinite) plus f's own archimedean density on the other. DH's zero system is
thus a genuine crystalline-pair-with-complex-defects whose comb FAILS positivity —
and its zeros are indeed off-line in abundance. This is the standing
counterexample-generator for calibrating (R′)-type hypotheses (ROADMAP §F). The
precise DH functional-equation constants and the exact strip `|Im z| < σ₀−½` must be
pinned from the sources before this section is upgraded from SHAPE to PROVED.

## 8. Litmus & circularity audit (docs/06, mandatory)

- Nothing above assumes RH or any docs/03 equivalent; L8a–L8c are unconditional and
  the zero atoms are allowed complex throughout. (R′) is CONJECTURED and clearly
  labeled; it is never used.
- LITMUS-1/2: the DH/Epstein systems satisfy (EF)-analogues but violate (S3)'s comb
  positivity (and archimedean datum) — any future rigidity proof must use `w ≥ 0`
  as a load-bearing hypothesis (§7). L8b/L8c are litmus-safe because they make no
  reality claim: they are Fourier-uniqueness statements, valid for DH-type systems
  too (uniqueness/finite-rigidity of DH's own pair — true and harmless).
- LITMUS-3: `w_n ≥ 0` + (S3) encodes nonvanishing analogues on `σ>1` exactly as the
  Euler product does for ζ — recorded, not yet used.
- LITMUS-4: (R′) demands `Z ⊂ ℝ` exactly (no zero-free strip of positive width) —
  consistent with `Λ_dBN ≥ 0`.

## 9. References

[Titchmarsh] §4.42, Thm 9.2, §9.4, Thm 9.6(A); [IK] Thm 5.12 (statement shape
cross-check); [BombieriLagarias1999] (framework; multiset theorem — see bibliography);
[DavenportHeilbronn1936], [BombieriHejhal1995] (DH facts); [Remmert1991] (ψ₀ integral
representation, Morera/Fubini standards). Program context:
`attempts/fourier-rigidity/ROADMAP.md`; numerics `scratch/explicit-formula-check/`.
