# L6 — The Pick-kernel criterion for RH (proved equivalence)

**Tag:** PROVED (modulo one standard textbook citation, flagged below; hostile re-read
wanted per docs/07 Stage 4). ⚠️ This is a docs/03-style **equivalent formulation** of
RH: attack surface if proved as an inequality, circularity hazard if ever assumed.

## Statement

Fix any `X > ½`. Let `Q(x) := ξ'(½+x)/ξ(½+x)` for `x > 0` (well defined by L2). Then

```
RH  ⟺  for every N ≥ 1, x_1,…,x_N ∈ (X,∞), c ∈ ℝ^N:
        Σ_{j,k} c_j c_k (Q(x_j)+Q(x_k))/(x_j+x_k) ≥ 0.
```

(Equivalently: the kernel `K(x,y) = (Q(x)+Q(y))/(x+y)` is positive semidefinite on
`(X,∞)`.) This is a Loewner-coordinates form of Lagarias's criterion [Lagarias1999,
with 2005 Correction]; the proof below is self-contained apart from the two standard
citations noted.

## Setup

`F(z) := ξ(½ − iz)`. `F` is entire of order 1, even (`F(−z) = ξ(½+iz) = ξ(½−iz)` by the
functional equation), real on ℝ (ξ real on the critical line, docs/02), `F(0) = ξ(½) ≠ 0`
(L2), and satisfies `F(z̄) = conj F(z)`. Zeros of `F`: `ρ = β+iγ` nontrivial zero of ζ ⟺
`F` vanishes at `z_ρ = γ + i(β−½)`; unconditionally all zeros of `F` lie in
`|Im z| < ½` (docs/02 §3). Define `M(z) := −F'(z)/F(z)`, meromorphic on ℂ, with poles
exactly at the zeros of `F`; `M(ix) = i·Q(x)` for real `x` (chain rule:
`F'(z) = −i·ξ'(½−iz)`, so `M(ix) = i·ξ'(½+x)/ξ(½+x)`).

RH ⟺ all zeros of `F` are real.

## Proof of ⟹ (RH implies PSD)

Assume all zeros of `F` real. Hadamard factorization for the even, order-1 function `F`
with `F(0) ≠ 0` [docs/02 §2; Titchmarsh]:
`F(z) = F(0)·Π_k (1 − z/γ_k) e^{z/γ_k}` over the real zeros `γ_k ≠ 0` (with
multiplicity; evenness forces the exponential factor `e^{bz}` to have `b = 0`, and
zeros to pair as `±γ`), with `Σ 1/γ_k² < ∞` (Riemann–von Mangoldt). Termwise
logarithmic differentiation (locally uniformly convergent after pairing `±γ`) gives

```
M(z) = Σ_k [ 1/(γ_k − z) − 1/γ_k ],
```

absolutely convergent in the paired grouping. For nodes `z_1,…,z_N ∈ ℂ₊` the Pick
kernel splits termwise: for a single term `1/(γ − z)` (any real γ, including negative),

```
( 1/(γ−z_j) − conj(1/(γ−z_k)) ) / (z_j − conj z_k) = v_j · conj(v_k),
v_j := 1/(γ − z_j),
```

a rank-one PSD kernel; real constants (`−1/γ_k`) contribute 0. Summing (locally
uniformly convergent sum of PSD kernels) shows the full Pick kernel of `M` is PSD on
ℂ₊. Restrict to `z_j = i x_j`, `x_j > X`: using `M(ix) = iQ(x)`,

```
( iQ(x_j) − conj(iQ(x_k)) ) / ( ix_j − conj(ix_k) ) = (Q(x_j)+Q(x_k))/(x_j+x_k). ∎
```

## Proof of ⟸ (PSD implies RH)

Assume all finite Pick matrices at nodes in `i(X,∞)` are PSD. Note the `1×1` case gives
`Q(x) ≥ 0` on `(X,∞)`.

**Step 1 (interpolant).** Choose a countable dense `{x_n} ⊂ (X,∞)`. By the classical
Nevanlinna–Pick theorem for the upper half-plane (finite node version: distinct
`z_1..z_N ∈ ℂ₊`, targets `w_1..w_N`; PSD of `[(w_j − conj w_k)/(z_j − conj z_k)]` ⟹
∃ H in the Pick/Herglotz class with `H(z_j) = w_j`; degenerate-rank cases yield real
rational interpolants, still Herglotz) — **citation: standard, e.g. Donoghue,
*Monotone Matrix Functions and Analytic Continuation*, Springer 1974 (flagged: page/
theorem number to be pinned when the volume is at hand)** — there are Herglotz `H_N`
with `H_N(ix_j) = iQ(x_j)` for `j ≤ N`.

**Step 2 (normality).** Let `c : ℂ₊ → 𝔻` be the Cayley map `c(w) = (w−i)/(w+i)`
(well-defined on the closed upper half-plane minus `{−i}`; Herglotz functions map ℂ₊
into `ℂ₊ ∪ ℝ`; if `H_N` is a real constant, it fails `Im H_N(ix_1) = Q(x_1) ≥ 0`…
handle the two cases: if `Q(x_1) > 0` the interpolants are non-real-constant, map into
open ℂ₊, and `c∘H_N : ℂ₊ → 𝔻` is a uniformly bounded family — normal by Montel. A
locally uniform limit `g` along a subsequence has `g(ix_1) = c(iQ(x_1)) ∈ 𝔻`, so by the
maximum principle `g` maps into `𝔻` (not a unimodular constant), and
`H := c^{-1}∘g` is Herglotz with `H(ix_j) = iQ(x_j)` for EVERY `j` (each node is exact
for all `N ≥ j`, hence in the limit). If instead `Q ≡ 0` on a dense subset of `(X,∞)`
then `ξ'/ξ` vanishes on a set with an accumulation point in `(½+X, ∞)` ⟹ `ξ'≡ 0` by
the identity theorem — false. So some node has `Q(x_1) > 0` after reindexing.)

**Step 3 (identification).** All poles of `M` lie in `|Im z| < ½` (Setup), so `M` is
holomorphic on the connected open set `Ω := {Im z > ½} ⊃ i(X,∞)`. `H − M` is
holomorphic on `Ω` and vanishes on `{ix_n}`, which accumulates at interior points of
`Ω`; by the identity theorem `H ≡ M` on `Ω`.

**Step 4 (no poles in ℂ₊).** `M` is meromorphic on ℂ₊ and agrees with the holomorphic
`H` on the open set `Ω`; hence `M = H` on ℂ₊ minus the poles of `M` (identity theorem
on the connected set `ℂ₊ ∖ {poles}`, which contains `Ω`). If `M` had a pole
`z₀ ∈ ℂ₊`, then `|M| → ∞` at `z₀` while `M = H` on a punctured neighbourhood and `H` is
continuous at `z₀` — contradiction. So `F` has no zeros in ℂ₊; by
`F(z̄) = conj F(z)`, none in ℂ₋ either; all zeros of `F` are real ⟹ RH. ∎

## Remarks

- The proof of ⟸ never uses any unproved zero information: the only geometric input is
  the **unconditional** strip bound `|Im z_ρ| < ½` (docs/02 §3), which is what makes
  `Ω = {Im z > ½}` pole-free. For Davenport–Heilbronn the same argument applies verbatim
  (DH's completed function also has its zeros in a horizontal strip after the analogous
  rotation, and no real zeros of `ξ_f(½+x)` on the relevant ray were found —
  scratch/pick-kernel claim 5), so DH's kernel must fail PSD at some finite set —
  numerically it is masked below ~1e−9·background (see attempt STATUS). The
  *criterion* passes the litmus tests as a criterion; any *proof of the PSD side* must
  use `Λ(n) ≥ 0`/Euler product (attempt PROOF.md §6).
- `1×1` PSD ⟺ `Q ≥ 0` on `(X,∞)`: already unconditional (L4). By L4 all `2×2` minors
  are unconditional too; RH content starts at `3×3`.

## Used by

`attempts/pick-kernel-positivity/` (criterion, §1–2).

## Checks (docs/06 audit)

- Circularity: ⟸ uses only the unconditional strip bound; ⟹ assumes RH by design
  (it is one side of an equivalence). ✓
- Interchanges: Hadamard termwise log-differentiation with `Σ1/γ² < ∞` (paired) —
  locally uniform on compacts avoiding zeros. ✓
- Domain discipline: no Dirichlet series used. ✓
- Open citation item: Donoghue theorem/page number (finite NP for ℂ₊) — flagged, to be
  pinned; the statement used is textbook-standard.
