# Attempt: pick-kernel-positivity

**Approach family (docs/05):** §3 Weil positivity / explicit formula, in Herglotz–Pick
(Loewner) clothing; adjacent to §5 (de Branges) and to the localized-Weil-form work of
Suzuki. Sibling of `attempts/li-positivity/` — same positivity wall, different coordinates.

**The idea (one paragraph).** RH is equivalent to `M(z) = i·(ξ'/ξ)(½ − iz)` being a
Herglotz (Pick) function on the upper half-plane (this is Lagarias's positivity criterion
in Cayley-rotated form). Restricting the Pick kernel of `M` to the positive imaginary
axis `z = ix`, `x > ½`, where everything is **real** and where `ζ'/ζ` still has its
absolutely convergent prime representation, RH becomes: the explicit real kernel

```
K(x,y) = (Q(x) + Q(y)) / (x + y),      Q(x) := ξ'(½+x) / ξ(½+x),
```

is positive semidefinite on `(X, ∞)` for one (any) fixed `X > ½`. The converse direction
is a Nevanlinna–Pick interpolation + identity-theorem argument (PROOF.md §2). The **new
input** relative to li-positivity: (i) the criterion lives entirely at real points
`s = ½ + x`, `x > ½`, inside the Euler-product half-plane, so the prime side is an
absolutely convergent series with positive coefficients `Λ(n)`; (ii) small principal
minors are claimed provable *unconditionally* (all 1×1 and 2×2), so the obstruction to RH
is intrinsically ≥ 3-point — a structural fact not visible in the `λ_n` coordinates;
(iii) an isolated off-line zero quartet is detected by an explicit *sign* of a 3×3
determinant, giving a concrete finite-dimensional shape to what must be excluded.

**What would close it.** A dilation / sum-of-squares factorization of the quadratic form
`𝒜 − 𝒫` (archimedean part minus prime-shift part, PROOF.md §5) making `K` manifestly PSD —
i.e., Weil positivity for the specific cone of test functions `B(u) = Σ c_j e^{−x_j u}`,
`x_j > ½`.

**Origin.** Distilled from `notes.md` (2026-07-11 session); see
`workspace/scratch/notes-triage.md` for the full mapping.
