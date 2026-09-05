# 04 — Known Results (cite, do not re‑derive)

These are established theorems. Use them freely **with citation**; do not spend effort
re‑proving them. Full references: [references/bibliography.md](../references/bibliography.md).
This is also the boundary line of doc 01 item B2: anything here is "established"; anything
not here (and not standard textbook material from doc 02) must be proved in‑repo.

## A. Foundational (1859–1900)

- **Riemann (1859)**: analytic continuation, functional equation, the explicit formula
  program, and the hypothesis itself.
- **Hadamard; de la Vallée Poussin (1896)**: `ζ(1+it) ≠ 0` ⟹ **Prime Number Theorem**,
  `π(x) ∼ Li(x)`. First nontrivial zero‑free region.
- **von Mangoldt**: rigorous proof of the explicit formula; `N(T)` asymptotics.

## B. Zeros on the line

- **Hardy (1914)**: infinitely many zeros on `σ=1/2`.
- **Hardy–Littlewood (1921)**: `≫ T` zeros up to height `T` on the line.
- **Selberg (1942)**: a *positive proportion* of zeros lie on the line.
- **Levinson (1974)**: ≥ 1/3 of zeros on the line (mollifier method).
- **Conrey (1989)**: ≥ 2/5 (40.9%); subsequent work (Bui–Conrey–Young, Pratt–Robles–…,
  ~2020) pushes to ≈ 41.7%. **Still bounded well below 100%.**

## C. Zero‑free regions and density

- **de la Vallée Poussin**: `ζ(σ+it)≠0` for `σ ≥ 1 − c/log(|t|+2)`.
- **Vinogradov–Korobov (1958)**: `σ ≥ 1 − c/((log|t|)^(2/3)(loglog|t|)^(1/3))`.
- **Zero‑density theorems** (Ingham, Huxley, Bourgain, Guth–Maynard 2024): bounds on
  `N(σ,T)` = number of zeros with `Re≥σ`, height `≤T`. Guth–Maynard (2024) improved the
  long‑standing Ingham exponent near `σ=3/4`. These constrain how zeros *could* lie off the
  line; they do not prove RH.

## D. Numerical verification (evidence only — see doc 01 B1)

- **Turing; Lehmer; van de Lune–te Riele–Winter; Odlyzko; Gourdon (2004); Platt**: the
  first `~1.3×10^13` non‑trivial zeros lie on the critical line; high‑height sampled
  blocks (Odlyzko, near `10^22`) confirm GUE pair‑correlation statistics.

## E. Statistics / random matrix theory

- **Montgomery (1973)**: pair‑correlation of zeros matches the GUE (random Hermitian)
  ensemble (pair‑correlation conjecture, partially proven).
- **Odlyzko**: numerical confirmation of GUE spacing.
- **Keating–Snaith**: random‑matrix predictions for moments of `ζ` on the line.
  Suggestive of Hilbert–Pólya; not a proof.

## F. The de Bruijn–Newman constant

- **Newman (1976)** conjectured `Λ ≥ 0`; **Rodgers–Tao (2020)** proved `Λ ≥ 0`.
  Upper bounds (Polymath 15, 2019): `Λ < 0.2`. RH ⇔ `Λ = 0` (doc 03 §12).

## G. The function‑field / arithmetic‑geometry analogue (proven RH analogues)

- **Hasse (1930s)**: RH for elliptic curves over finite fields.
- **Weil (1948)**: RH for all curves over finite fields; the "Riemann hypothesis for
  function fields."
- **Deligne (1974, 1980)**: the **Weil conjectures**, including RH for varieties over
  finite fields, via étale cohomology and a positivity/monodromy argument.
  → Studied intensively for transferable ideas; **no transfer to `ℚ`/ζ is known**.

## H. Conditional landscape (what RH would give / relations)

- RH ⟹ Lindelöf hypothesis ⟹ subconvexity (converse open).
- RH ⟹ tightest prime gaps consistent with current heuristics, sharp `π(x)` error (doc 03).
- **GRH** has many independent consequences (Miller–Rabin determinism, Artin's primitive
  root conjecture under GRH, class number bounds, …) — context for why the problem matters.

## I. Selberg class (axiomatic framework)

- **Selberg (1992)**: axioms (Dirichlet series, analytic continuation, functional
  equation, Euler product, Ramanujan bound) isolating L‑functions expected to satisfy RH.
  Key axiom: the **Euler product**. Functions with a functional equation but **no** Euler
  product (Davenport–Heilbronn, Epstein) are **outside** the class and **violate** RH — the
  formal statement of the litmus test in doc 06.

---

**Rule of use.** When an argument leans on any result above, cite it inline by name and
bibliography key (e.g. "[VK58]"). When it leans on something *not* above and not in doc 02,
that something must be proved in `workspace/lemmas/` to acceptance‑criteria standard.
