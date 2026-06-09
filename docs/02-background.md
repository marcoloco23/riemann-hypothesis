# 02 — Mathematical Background

Standard facts you may use **without re‑proving them**, with enough precision to cite.
Everything here is classical and appears in Titchmarsh, *The Theory of the Riemann
Zeta‑Function*, or Iwaniec–Kowalski, *Analytic Number Theory*. When you rely on any of
these in a proof, cite the source (doc 04 / bibliography), don't just gesture at it.

## 1. Definitions

- **`s = σ + it`**: complex variable; `σ = Re(s)`, `t = Im(s)`.
- **Critical strip**: `0 < σ < 1`. **Critical line**: `σ = 1/2`.
- **`ζ(s)`**: Riemann zeta function (doc 00 §1). Dirichlet series for `σ>1`, Euler product
  for `σ>1`, meromorphic on `ℂ` with one simple pole at `s=1`, residue `1`.
- **`ξ(s) = ½ s(s−1) π^(−s/2) Γ(s/2) ζ(s)`**: completed zeta, **entire**, order 1,
  `ξ(s)=ξ(1−s)`, real on the critical line and on the real axis.
- **`Γ(s)`**: gamma function; poles at `s = 0, −1, −2, …`; `Γ(s)Γ(1−s)=π/sin(πs)`.
- **`Λ(n)`**: von Mangoldt function; `Λ(n)=log p` if `n=p^k`, else `0`.
- **`ψ(x) = Σ_{n≤x} Λ(n)`**: second Chebyshev function.
- **`θ(x) = Σ_{p≤x} log p`**: first Chebyshev function.
- **`π(x)`**: prime‑counting function. **`Li(x) = ∫₀^x dt/log t`** (principal value):
  logarithmic integral.
- **`μ(n)`**: Möbius function. **`M(x) = Σ_{n≤x} μ(n)`**: Mertens function.
- **`σ_a(n) = Σ_{d|n} d^a`**; write `σ(n)=σ_1(n)` (sum of divisors). **`H_n = Σ_{k≤n} 1/k`**.

## 2. Key identities (valid where stated)

- **Euler product**: `ζ(s) = ∏_p (1−p^(−s))^(−1)`, `σ>1`. Hence `ζ(s)≠0` for `σ>1`.
- **Logarithmic derivative**: `−ζ'(s)/ζ(s) = Σ_{n≥1} Λ(n) n^(−s)`, `σ>1`.
- **Reciprocal**: `1/ζ(s) = Σ_{n≥1} μ(n) n^(−s)`, `σ>1`.
- **Functional equations**: doc 00 §1 (symmetric `ξ(s)=ξ(1−s)` and asymmetric forms).
- **Hadamard product** for the entire order‑1 function `ξ`:
  `ξ(s) = ξ(0) ∏_ρ (1 − s/ρ)` over non‑trivial zeros `ρ` (paired with `1−ρ` for
  convergence). Equivalently
  `ζ'(s)/ζ(s) = B − 1/(s−1) + ½ log π − ½ ψ₀(s/2+1) + Σ_ρ (1/(s−ρ) + 1/ρ)`
  with `ψ₀=Γ'/Γ`. The sum over zeros is the bridge between zeros and primes.

## 3. Zeros: what is unconditional

- All non‑trivial zeros lie in `0<σ<1`, symmetric about `σ=1/2` and about `t=0`.
- **`ζ(1+it) ≠ 0` for all real `t`** (de la Vallée Poussin / Hadamard, 1896) — equivalent
  to the Prime Number Theorem.
- **Classical zero‑free region**: there is `c>0` with `ζ(σ+it)≠0` whenever
  `σ ≥ 1 − c/log(|t|+2)`. **Vinogradov–Korobov** widens this to
  `σ ≥ 1 − c/((log|t|)^(2/3)(log log|t|)^(1/3))`. These are the best known and are *far*
  from the critical line.
- **Counting (Riemann–von Mangoldt)**: the number `N(T)` of zeros with `0<t≤T` satisfies
  `N(T) = (T/2π) log(T/2π) − T/2π + (7/8) + S(T) + O(1/T)`, where
  `S(T)=π^(−1) arg ζ(1/2+iT) = O(log T)`.

## 4. The explicit formula (zeros ↔ primes)

For `x>1` not a prime power (von Mangoldt's explicit formula):

```
ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − ½ log(1 − x^(−2)),
```

the sum over non‑trivial zeros `ρ` (symmetric pairing). The real parts of the `ρ` control
the size of the error `ψ(x)−x`. This identity is the reason RH is equivalent to a sharp
prime‑counting error term (doc 03). Weil's explicit formula is the general distributional
version and underlies the "positivity" approaches (doc 05).

## 5. On the critical line — partial progress (unconditional)

- **Hardy (1914)**: infinitely many zeros lie *on* `σ=1/2`.
- **Hardy–Littlewood, Selberg, Levinson, Conrey, …**: a positive *proportion* of zeros lie
  on the line; the current record is **> 41%** (Conrey 1989: 40.9%; later refinements
  ~41.5%). This does **not** approach 100% with present methods.
- **Numerical**: the first ~`1.3×10^13` zeros (Platt, Gourdon, et al.) all lie exactly on
  the line, and verification extends to enormous heights in sampled ranges. Evidence only —
  see doc 01 item B1.

## 6. Useful analytic tools (standard, citable)

- **Argument principle / Rouché** for counting zeros in a region.
- **Phragmén–Lindelöf** for bounding analytic functions in strips.
- **Hadamard factorization** for functions of finite order.
- **Jensen's formula**, **Borel–Carathéodory**, **Littlewood's lemma**.
- **Convexity / subconvexity** bounds for `ζ` on vertical lines; the **Lindelöf
  hypothesis** (`ζ(1/2+it)=O(t^ε)`) is implied by RH but is itself open — do not assume it.
- **Mellin transform / Perron's formula** linking Dirichlet series to summatory functions.

## 7. Generalizations (scope awareness, not targets)

- **Dirichlet L‑functions `L(s,χ)`** → **Generalized RH (GRH)**.
- **Dedekind zeta of number fields**, **Hecke L‑functions** → **Extended RH (ERH)**.
- **Automorphic L‑functions** → **Grand RH (GRH, Selberg class)**.
- **Function‑field analogue**: for curves/varieties over finite fields the analogue of RH
  is a **theorem** (Hasse, Weil; Deligne for higher dimensions). The proof uses algebraic
  geometry (étale cohomology, positivity) with **no known transfer** to the number field
  ζ. The structural lessons of this proof are a major source of strategy ideas (doc 05).

A proof of GRH/ERH/Grand‑RH implies RH and is acceptable (doc 00 §0), but the required
deliverable is RH for ζ.
