# L11 — The smoothed von Mangoldt statistic `F(X)` and its sharp RH-equivalent bound

**Tag:** `PROVED-WRITTEN` (2026-11-21). Standard material, written out because the
2026-11-20 announcement ([record](../../docs/10-external-claim-2026-11.md), step 5) names
this statistic as the object its argument works with. Numeric anchor:
[`scratch/external-claim-2026-11`](../scratch/external-claim-2026-11/README.md). No
independent human review; machine-assisted.

**⚠️ Scope note:** part (c) is an *equivalence* with RH. It is a reformulation in the
sense of docs/03, as hard as RH, and proves nothing about zeros.

## Statement

For `X ≥ 1` put

```
F(X) := Σ_{n≤X} Λ(n)(X/n − 1) − X log X + (1+γ)X          (γ = Euler's constant).
```

**(a) Explicit formula.** For every `X > 1`, with the sum over nontrivial zeros `ρ`
counted with multiplicity and absolutely convergent,

```
F(X) = Σ_ρ X^ρ / (ρ(1−ρ)) + log 2π − Σ_{k≥1} X^{−2k} / (2k(2k+1)).
```

**(b) Sharp bound under RH.** If RH holds then for all `X > 1`

```
| F(X) − log 2π + Σ_{k≥1} X^{−2k}/(2k(2k+1)) |  ≤  (2 + γ − log 4π) √X ,
```

and `F(X) = √X · Σ_{γ_ρ>0} 2cos(γ_ρ log X)/(¼+γ_ρ²) + O(1)`: an almost periodic
function of `log X` whose coefficients are all positive. `2+γ−log 4π = 0.046191…`.

**(c) Converse.** If `F(X) = O_ε(X^{1/2+ε})` for every `ε > 0`, then RH holds.

## Proof

**(a)** For `y > 0` and `c > 1`, `(1/2πi)∫_{(c)} y^s/(s(s−1)) ds = (y−1)_+`: the integrand
is `O(|s|^{−2})`; for `y ≤ 1` close the contour to the right (no poles), for `y > 1` to
the left (residues `y` at `s=1` and `−1` at `s=0`). Since `−ζ'/ζ(s) = ΣΛ(n)n^{−s}`
converges absolutely on `Re s = c` and the kernel is absolutely integrable there,

```
Σ_{n≤X} Λ(n)(X/n − 1) = (1/2πi) ∫_{(c)} (−ζ'/ζ)(s) · X^s/(s(s−1)) ds .
```

Move the line to `Re s = −U`, `U` odd, through horizontal segments at heights `±T_j`
chosen as in [MontgomeryVaughan, §12.1] so that `ζ'/ζ(σ±iT_j) ≪ log² T_j` uniformly
for `−1 ≤ σ ≤ 2`, and using `ζ'/ζ(s) ≪ log(2|s|)` for `σ ≤ −1` away from the trivial
zeros [MontgomeryVaughan, §12.1] (exact lemma numbers to be pinned on review). Against the kernel `X^σ/|s|²` the horizontal
segments tend to 0 as `T_j → ∞`, and the left line tends to 0 as `U → ∞` because
`X > 1`. The residues are:

- `s = 1` (double pole; `−ζ'/ζ(s) = 1/(s−1) − γ + O(s−1)` and
  `X^s/s = X[1 + (log X − 1)(s−1) + …]`): `X log X − (1+γ)X`;
- `s = 0`: `(−ζ'/ζ)(0)·X⁰/(0−1) = log 2π`, since `ζ'/ζ(0) = log 2π`;
- `s = ρ`: `−X^ρ/(ρ(ρ−1)) = X^ρ/(ρ(1−ρ))`, with multiplicity;
- `s = −2k`: `−X^{−2k}/((−2k)(−2k−1)) = −X^{−2k}/(2k(2k+1))`.

Absolute convergence of the `ρ`-sum is `Σ|ρ|^{−2} < ∞` (order 1), so no symmetric
pairing is needed and the limit along the `T_j` is the full sum. ∎

**(b)** Under RH, `ρ = ½+iγ_ρ`, `ρ(1−ρ) = ¼+γ_ρ² > 0` and `|X^ρ| = √X`, so the zero sum
is at most `√X · Σ_ρ 1/(ρ(1−ρ))` in absolute value. Unconditionally
`Σ_ρ 1/(ρ(1−ρ)) = Σ_ρ (1/ρ + 1/(1−ρ)) = 2 Σ_ρ Re(1/ρ) = 2 + γ − log 4π`
[Davenport, Ch. 12: `B = −γ/2 − 1 + ½ log 4π = −Σ_ρ Re(1/ρ)`]. Pairing `ρ, ρ̄`
gives the cosine form. ∎

**(c)** For `Re s > 1`, by (a)'s Mellin pair and `∫_1^∞ X^{−s}(log X) dX = (s−1)^{−2}`,

```
∫_1^∞ F(X) X^{−s−1} dX = (−ζ'/ζ)(s)/(s(s−1)) − 1/(s−1)² + (1+γ)/(s−1).
```

If `F(X) ≪ X^{1/2+ε}` the left side is holomorphic in `Re s > ½+ε`, so `ζ'/ζ` has no
pole there except `s = 1`: no zeros with `Re ρ > ½`, and by the functional equation
none with `Re ρ < ½`. ∎

## Remarks

- **Where the Euler product enters.** Only in `−ζ'/ζ = ΣΛ(n)n^{−s}` with `Λ ≥ 0`
  supported on prime powers. The same contour argument applied to the
  Davenport–Heilbronn function gives the analogue of (a) with signed coefficients
  (cf. [L10](L10-davenport-heilbronn-explicit-formula.md)), and (b) fails there because
  its off-line zeros contribute terms of size `X^{β}`, `β > ½` (LITMUS-1).
- **Why this statistic.** The kernel `1/(s(1−s))` is positive on the critical line and
  integrable, so under RH the zero side is a positive combination of characters of
  `log X`. In Weil's language it is the explicit formula for a test function whose
  transform is `1/(¼+t²)`; the announcement's remark that "Guinand–Weil had the sign"
  is read here as this positivity (our reading, not the author's statement).
- Nothing here bears on whether the announced proof is correct.
