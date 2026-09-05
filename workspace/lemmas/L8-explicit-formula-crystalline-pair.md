# L8 — The Weil explicit formula and uniqueness of its strip-atom functional

**2026-09-05 update:** [L9](L9-positive-comb-singleton.md) proves that the
unchanged relaxed class in §6 is also a singleton (written proof, same-agent
audit; independent review pending). Thus `(R′) ⇔ RH`, with no distinct system
to search for. [L10](L10-davenport-heilbronn-explicit-formula.md) supplies the
DH constants and exclusions. The [audit](../attempts/fourier-rigidity/AUDIT-2026-09-05.md)
records a recheck of Step C and a second, resolvent-based derivation of L8b.
The review history below refers to the earlier 2026-07-12 session.

**Tag:** L8a PROVED — hostile re-read PASSED 2026-07-12 (independent agent: every
sign/constant re-derived, its own numerics to 1e−29; plus the repo numeric anchor,
17-digit constant cancellation). L8b PROVED — hostile re-read 2026-07-12 found one
fixable gap in Step C's shifted-anchor stage (collision-avoidance + `|h|<¼`), both
repairs applied same-day; **the repaired subsection wants one more independent
re-read** before load-bearing use. L8c PROVED — re-read PASSED (one operator-sign
typo fixed). §3's density remark: factor-2 error found by review, FIXED. §6
definitions + conjecture (R′) are NOT results. Numerical cross-check (motivational
only, docs/01 B1): `scratch/explicit-formula-check/`.

This was Rung 0 of `attempts/fourier-rigidity/` (archived
`ROADMAP-2026-07-12.md` §A, §D). Everything here is
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

**Remark (wider test classes).** Compact smooth tests remain the default.
Decay of g alone does not justify every contour shift or a convergent zero sum;
in particular an arbitrary Schwartz function need not have a transform defined
at nonreal points. The Gaussian extension used by L8b is proved below, and
the nonsmooth exponential extension is proved in L9 §2. Other extensions require
their own checked hypotheses.

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
`x = e^{−2v}`, and checking the `v→0` cancellation (`integrand → −(3/2)g(0)`;
detail: `[g(0)−e^{3v/2}g(v)] = −(3/2)g(0)v + O(v²)` and `2e^{−2v}/(1−e^{−2v}) = 1/v +
O(1)`). For the interchange, first cut the v integral off at ε>0. Near 0,
`|1-e^{3v/2}e^{itv}|≤C v(1+|t|)`, and ĝ is Schwartz on R;
this gives an integrable majorant after division by v. At infinity use
`e^{-2v}+e^{-v/2}` times `|ĝ(t)|`. Dominated convergence removes ε.

**Reading.** The explicit-formula functional is **minus** an atomic comb with
nonnegative weights, plus the pole background and the archimedean distribution.
The last distribution is singular at 0, not globally a smooth background.
Off-axis atoms act by evaluation on entire transforms; this is not an ordinary
Fourier transform of a measure on R. Even under RH the computed right-hand side
is not purely atomic, so the standard Fourier-quasicrystal classification cannot
be applied to it as stated. “Crystalline pair” is historical program terminology,
not a claim that this object meets that classification's hypotheses.

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
of the archived roadmap §A (atoms in `S`, symmetries, ζ-density, satisfying L8a's identity with the
exact right-hand side) is the singleton `{Z_ζ}`. Hence the naive Rigidity Conjecture
(R) is **equivalent to RH but vacuous as a rigidity target** (no room for any tool to
act: the hypotheses already pin the object). The kill-criterion K1's "fake zero set
with the exact ζ comb" **cannot exist**. The program's content is therefore entirely
in the choice of relaxation (§6), as anticipated in the archived roadmap §E-K1.

**Corollary ((R) ⟺ RH, both directions, unconditional).** If (R) holds, apply
it to `Z_ζ` using L8a to obtain RH. Conversely, if RH holds, L8b identifies
every system in the naive class with `Z_ζ ⊂ ℝ`, so (R) holds.

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

Split ψ into its even and odd parts. The odd transform is odd, so its
absolutely convergent sum over the symmetric multiset cancels pairwise
(and is zero at the possible atom 0). The real and imaginary parts of the
even part belong to 𝒯; (H0) annihilates both. Thus `S=0` in `𝒟′(ℝ)`.

**Step B (extension to Gaussian tests).** Let `W` be the little-o space of
`ψ ∈ C^∞(ℝ)` with

```
‖ψ‖_W := max_{m≤3} sup_u (1+|u|)² |ψ^{(m)}(u)| e^{|u|/2} < ∞ .
```

Require additionally that the weighted expression tends to 0 as `|u|→∞`
for each `m≤3`. This condition, satisfied by all Gaussian tests below,
is needed for cutoff convergence in this norm.

For `ψ ∈ W` the transform `ψ̂(z) = ∫ψ(u)e^{−izu}du` is defined on the closed strip
`|Im z| ≤ ½` (the weight dominates `e^{yu}`), and three integrations by parts —
boundary terms vanish by the decay — give `|ψ̂(x+iy)| ≤ C‖ψ‖_W (1+|x|)^{−3}`
uniformly on the strip. Hence `⟨S,ψ⟩ := Σ_j c_j ψ̂(z_j)` converges absolutely for
every `ψ ∈ W`, with `|⟨S,ψ⟩| ≤ C′‖ψ‖_W` (density `O(T log T)`; only `|y_j| ≤ ½` is
used, valid on the closure of the strip). Now `S = 0` extends from `C_c^∞` to `W`
by cutoff: with `χ_R` smooth, `= 1` on `[−R,R]`, supported in `[−2R,2R]`, derivatives
bounded uniformly in R, we have `ψχ_R ∈ C_c^∞` and `‖ψ − ψχ_R‖_W → 0` as `R → ∞`
(by the product rule, `‖ψ(1−χ_R)‖_W ≤ C sup_{|u|≥R}
(1+|u|)²max_{m≤3}|ψ^{(m)}(u)|e^{|u|/2} → 0` by the little-o condition).
Hence `⟨S,ψ⟩ = lim_R ⟨S, ψχ_R⟩ = 0` for all such ψ.

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

**Corollary (distinct members).** Any admissible system in §6 **distinct from
`Z_ζ`** must differ from it in infinitely many atoms. This does not exclude
`Z_ζ` itself being nonreal if RH is false. The original “any non-real system”
wording was incorrect. L9 now excludes distinct members altogether using
the unchanged S1–S3 assumptions; L8c alone establishes only the finite-defect claim.

## 6. The relaxed class and (R′) — definition unchanged, class now identified by L9

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

**Current result (2026-09-05):** L9 identifies this exact class with
`{(Z_ζ,(Λ(n)/√n))}`. Positivity first gives `Σ_{n≤X}w_n=O(√X)`;
the explicit formula reconstructs a Dirichlet series with ζ's completion;
Hamburger's theorem identifies it with ζ. Prime-power support is consequently
a derived property, although it was not an axiom. Thus `(R′) ⇔ RH`, not an
established Grand-RH-strength generalization. L10 proves the DH exclusions
with real signed coefficients and exact background data.

## 7. DH analogue — constants supplied by L10

L10 gives the full derivation for
`H(s)=(5/π)^((s+1)/2)Γ((s+1)/2)f(s)=H(1-s)`.
Its zero set lies in `|Im z|<3/2` by a direct zero-free bound for `Re s≥2`.
Its explicit formula has no pole background, a negative signed comb
`-2Σ b(n)n^{-1/2}g(log n)`, and gamma integrand
`Re ψ₀(3/4+it/2)+log(5/π)`. The log-derivative series converges absolutely
for `Re s≥2`. Its coefficients are real, with `b(3)=-κlog3<0` and
`b(6)=(1+κ²)log6>0`. Thus “supported on ALL integers” is replaced by the
precise statement that support is not restricted to prime powers.

## 8. Litmus & circularity audit (docs/06, mandatory)

- Nothing above assumes RH or any docs/03 equivalent; L8a–L8c are unconditional and
  the zero atoms are allowed complex throughout. (R′) is CONJECTURED and clearly
  labeled; it is never used.
- LITMUS-1: L10 proves the DH signed-comb and background exclusions separately.
  L8b/L8c make no reality claim, so their uniqueness mechanisms also work
  harmlessly for appropriate DH analogues. No blanket claim about every Epstein
  function's coefficient signs is needed for these results.
- LITMUS-3: the nonvanishing reconstruction on `Re s>1` is now justified in
  L9 using positivity, strip containment and the exact background, not positivity alone.
- LITMUS-4: (R′) demands `Z ⊂ ℝ` exactly (no zero-free strip of positive width) —
  consistent with `Λ_dBN ≥ 0`.

## 9. References

[Titchmarsh] §4.42, Thm 9.2, §9.4, Thm 9.6(A); [IK] Thm 5.12 (statement shape
cross-check); [BombieriLagarias1999] (framework; multiset theorem — see bibliography);
[DavenportHeilbronn1936], [BombieriHejhal1995] (DH facts); [Remmert1991] (ψ₀ integral
representation, Morera/Fubini standards). Program context:
`attempts/fourier-rigidity/ROADMAP.md`; numerics `scratch/explicit-formula-check/`.
