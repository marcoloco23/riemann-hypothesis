# 03 — Equivalent Formulations

Each statement below is **provably equivalent to RH** (some to a quantitative form). They
are alternative attack surfaces: proving any one proves RH. They are also a **circularity
hazard** — assuming any of them (or anything that implies one) inside an argument for RH is
assuming the conclusion (doc 01 item B3). Know them so you can avoid accidentally using
them as hypotheses.

References are in [references/bibliography.md](references/bibliography.md).

## Analytic / prime‑counting

1. **Prime counting error.** `π(x) = Li(x) + O(√x · log x)` as `x→∞`.
   (RH ⇔ this bound. Unconditionally only much weaker bounds are known.)

2. **Chebyshev ψ error.** `ψ(x) = x + O(√x · (log x)²)`; equivalently
   `|ψ(x) − x| ≤ (1/8π) √x (log x)²` for `x ≥ 73.2` (Schoenfeld's explicit form).
   RH ⇔ `ψ(x) = x + O(x^(1/2+ε))` for every `ε>0`.

3. **Mertens function.** `M(x) = Σ_{n≤x} μ(n) = O(x^(1/2+ε))` for every `ε>0`. RH ⇔ this.
   ⚠️ The stronger **Mertens conjecture** `|M(x)| ≤ √x` is **FALSE** (Odlyzko–te Riele,
   1985) — a cautionary tale that "numerically overwhelming" ⇏ true. Do not confuse the two.

4. **Zero‑free half‑strip.** `ζ(s) ≠ 0` for `Re(s) > 1/2`. (Trivially equivalent by the
   `ρ ↦ 1−ρ` symmetry.)

5. **Farey / Franel–Landau.** A statement that the Farey fractions are "as equidistributed
   as possible": `Σ_{ν} |δ_ν|` is `O(x^(1/2+ε))`, where `δ_ν` are the deviations of Farey
   points from equally spaced points.

## Elementary‑number‑theory criteria (deceptively simple — beware)

6. **Robin's criterion (1984).** RH ⇔ for all `n > 5040`,
   `σ(n) < e^γ · n · log log n`, where `γ` is Euler–Mascheroni and `σ(n)=Σ_{d|n} d`.

7. **Lagarias's criterion (2002).** RH ⇔ for all `n ≥ 1`,
   `σ(n) ≤ H_n + exp(H_n)·log(H_n)`, with equality iff `n=1` (`H_n` the harmonic number).

   These look elementary but encode the full strength of RH. A short "elementary" proof of
   either is exactly the shape of argument most likely to be subtly wrong (doc 06).

## Spectral / positivity

8. **Li's criterion (1997).** RH ⇔ `λ_n ≥ 0` for all `n ≥ 1`, where
   `λ_n = Σ_ρ (1 − (1 − 1/ρ)^n)` (sum over non‑trivial zeros), equivalently
   `λ_n = (1/(n−1)!) d^n/ds^n [ s^(n−1) log ξ(s) ]|_{s=1}`.

9. **Weil's positivity criterion.** RH ⇔ a certain explicit‑formula Hermitian functional
   `W(f) = Σ_ρ \hat f(ρ)` is non‑negative for all admissible test functions `f`
   (positive‑definiteness of the Weil distribution). Basis of the trace‑formula programs.

10. **Nyman–Beurling criterion.** RH ⇔ the indicator `1_{(0,1)}` lies in the `L²(0,1)`
    closure of the span of the dilations `{ρ(θ/x) : 0<x≤1}` of the fractional‑part
    function `ρ(t)={1/t}` (Báez‑Duarte's refinement sharpens the approximation rate).

11. **Hilbert–Pólya (program, not a theorem).** If the numbers `t` with `1/2+it` a zero are
    the eigenvalues of a self‑adjoint operator, RH follows from reality of the spectrum. No
    such operator is known; this is a *direction*, not an equivalent statement (doc 05).

## De Bruijn–Newman

12. **De Bruijn–Newman constant `Λ`.** For the deformation `ξ_t` of `ξ`, there is a real
    constant `Λ` such that `ξ_t` has only real zeros iff `t ≥ Λ`. RH ⇔ `Λ ≤ 0`. It is a
    **theorem** that `Λ ≥ 0` (Rodgers–Tao, 2020) and `Λ < 0.2` (upper bounds). So RH ⇔
    `Λ = 0`, and RH is now known to be "barely true if true": there is *no room to spare*.
    Any proof must be consistent with `Λ ≥ 0`.

---

### How to use this list

- **As targets:** pick a formulation whose machinery you can actually control end‑to‑end.
- **As tripwires:** before finalizing, grep your argument for any step that silently uses
  one of these (or Lindelöf, or a zero‑density hypothesis). If found, it is circular.
- **Quantitative care:** some equivalences are with a specific exponent/`ε`. Match the
  exact form; an off‑by‑`ε` can turn an equivalence into a strictly weaker/stronger claim.
