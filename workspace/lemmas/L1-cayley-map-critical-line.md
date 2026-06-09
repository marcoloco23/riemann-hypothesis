# L1 — The Cayley-type map `w(s) = 1 − 1/s` and the critical line

**Tag:** PROVED (elementary; self-contained).

## Statement

Let `w(s) = 1 − 1/s = (s−1)/s` for `s ∈ ℂ ∖ {0}`, and let `𝔻 = {z : |z| < 1}`.

1. **(Half-plane dictionary.)** For `s ≠ 0`:
   - `|w(s)| < 1 ⟺ Re(s) > 1/2`,
   - `|w(s)| = 1 ⟺ Re(s) = 1/2`,
   - `|w(s)| > 1 ⟺ Re(s) < 1/2`.
2. **(Biholomorphism.)** `w` is a bijection from `{Re(s) > 1/2}` onto `𝔻`, holomorphic with
   holomorphic inverse `s(z) = 1/(1−z)`.
3. **(Symmetries.)** For `s ≠ 0, 1`: `w(1−s) = 1/w(s)` and `w(s̄) = \overline{w(s)}`.
   Thus the functional-equation symmetry `ρ ↦ 1−ρ` becomes circle inversion `w ↦ 1/w`,
   and the critical line `Re(s)=1/2` becomes the unit circle.
4. **(Compact sublevel sets.)** For `0 < r < 1`, the set `K_r = {s : |w(s)| ≤ r}` is the
   closed disk with center `1/(1−r²)` and radius `r/(1−r²)`; it is a compact subset of
   `{Re(s) > 1/2}` (its leftmost point is `1/(1+r) > 1/2`).

## Proof

**(1)** Since `|w(s)| = |s−1|/|s|`, each comparison `|w(s)| ⋚ 1` is equivalent to
`|s−1|² ⋚ |s|²`. Expanding, `|s−1|² = |s|² − 2Re(s) + 1`, so `|s−1|² ⋚ |s|²` is
equivalent to `1 ⋚ 2Re(s)`, i.e. to `Re(s) ⋛ 1/2`. ∎(1)

**(2)** `w` is holomorphic on `ℂ∖{0}` and `s(z) = 1/(1−z)` is holomorphic on `ℂ∖{1}`,
in particular on `𝔻`. For `z ∈ 𝔻`: `s(z) ≠ 0` (a reciprocal is never `0`), and
`w(s(z)) = 1 − (1−z) = z`; moreover `|w(s(z))| = |z| < 1`, so `Re(s(z)) > 1/2` by (1).
Conversely for `Re(s) > 1/2`, `|w(s)| < 1` by (1) and `s(w(s)) = 1/(1 − (1 − 1/s)) = s`.
So `w` and `s(·)` are mutually inverse holomorphic bijections between `{Re(s) > 1/2}`
and `𝔻`. ∎(2)

**(3)** `w(1−s)·w(s) = [((1−s)−1)/(1−s)]·[(s−1)/s] = [(−s)(s−1)] / [(1−s)s] = 1`,
since `(−s)(s−1) = s(1−s)`. Conjugation: `w(s̄) = 1 − 1/s̄ = \overline{1 − 1/s}`. ∎(3)

**(4)** For `s ≠ 0`, `|w(s)| ≤ r ⟺ |s−1|² ≤ r²|s|² ⟺ (1−r²)|s|² − 2Re(s) + 1 ≤ 0`.
Dividing by `1−r² > 0` and completing the square:

```
|s|² − (2/(1−r²)) Re(s) + 1/(1−r²) ≤ 0
⟺ |s − 1/(1−r²)|² ≤ 1/(1−r²)² − 1/(1−r²) = r²/(1−r²)².
```

This is the stated closed disk (note `0 ∉ K_r` since `w` blows up at `0`; the disk indeed
excludes `0` because its leftmost point is `(1−r)/(1−r²) = 1/(1+r) > 0`). The leftmost
point `1/(1+r) > 1/2` for `r < 1`, so `K_r ⊂ {Re(s) > 1/2}`; closed + bounded = compact. ∎

## Used by

- [L3-li-converse-pringsheim.md](L3-li-converse-pringsheim.md)
- `attempts/li-positivity/`

## Checks (doc 06 audit)

- Pure algebra/geometry of Möbius maps; no zeta-specific input, no convergence issues, no
  branch choices, no conjectural input. Nothing to be circular about.
