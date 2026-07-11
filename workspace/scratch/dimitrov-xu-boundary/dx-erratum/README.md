# Erratum finding — Dimitrov–Xu, Trans. AMS 372 (2019) 4107–4125 (arXiv:1606.05011)

**Date:** 2026-07-11. **Tag:** NUMERICAL + hand-derivation (agent-verified; not yet
independently re-derived by a second reader — do that before any external
communication).

## Finding

Theorem 1.1 / Theorem 3.2 of [DimitrovXu2019] — "RH ⟺ translates of
`Φ_{2,y}(t) = cosh(ty)·ν₂(Φ;t)` dense in `L¹(ℝ)` for each `y ∈ (−½,½)\{0}`" — is
**false as printed**, in both the arXiv v1 and the published TAMS version (kernel
wording identical; weight OUTSIDE the correlation integral).

- **The error:** their Lemma 3.3 asserts `ψ(x,y) = ℱ[sinh(·y)K](x)`; but
  `sinh(sy)K(s)` is odd, so its FT is **purely imaginary** (`±i·ψ`). The dropped `i`
  enters the quadratic Wronskian as `i² = −1`, flipping the sign of the
  `ν₂(sinh(·y)K)` term; the cosh/sinh addition formula then produces
  `cosh(y(t−2s))` **inside** the integral, not `cosh(yt)` outside.
- **Unconditional counterexample to the printed theorem** (from their own Cor. 4.3 b):
  `φ = 2sin(z)/z ∈ 𝓛𝓟` (real simple zeros), `ν₂ = ⅓(2−|t|)³`;
  `ℱ[cosh(yt)ν₂](x) = 2Re𝓛(x+iy)` changes sign (`+2.79` at `(0.5, 0.8)`;
  `−0.0011` at `(2.9, 2)`; `−0.495` at `(1.3, 5)`) ⟹ real zero of the FT ⟹ translates
  NOT dense (Wiener), contradicting the claimed density for every `y ∈ ℝ`.
- **For Riemann Ξ:** `Re𝓛(111.1+0.45i) = −2.77e−69 < 0` (forced by the close pair
  `γ₃₄, γ₃₅`), while the corrected quantity `𝒞(111.1+0.45i) = +2.44e−68 > 0`. The
  printed theorem is refuted at `y = 0.45` modulo only the certified reality/simplicity
  of ζ's zeros near height 111; the corrected version is untouched.

## Corrected statement (proof architecture of DX goes through verbatim)

```
K̃_{2,y}(t) = ∫ (t−2s)² cosh(y(t−2s)) Φ(t−s)Φ(s) ds
ℱ[K̃_{2,y}](x) = 2𝒞(x+iy) = 2[|Ξ'(x+iy)|² − Re(Ξ(x+iy)·conj(Ξ''(x+iy)))]
RH ⟺ ∀y ∈ (−½,½)\{0}: translates of K̃_{2,y} dense in L¹ ⟺ 𝒞(x+iy) > 0 ∀x.
```

This corrected criterion is Jensen's classical convexity criterion (their Theorem A)
repackaged through Wiener density — the DX-specific `Re𝓛` formulation does not
survive. Two harmless side errata: missing `1/n!` in their Lemma 2.1 (Andreief), and
the exponent `n(n+1)/2` vs `n(n−1)/2` typo (coincide for even n).

## Files

- `dx1606.pdf` — arXiv v1 (17 pp.).
- `check_dx.py` — sin-counterexample numerics (`ℱ[cosh ν₂] = 2Re𝓛`, sign change;
  `ℱ[K̃] = 2𝒞`).
- `check_riemann.py` — Riemann Ξ values at the γ₃₄/γ₃₅ window.
- Context: parent dir `../` (claims 1–5 verification), and
  `attempts/laguerre-phase-space/PROOF.md` §8.9.

## Follow-ups

1. Independent re-derivation of the Lemma 3.3 sign analysis by a second reader
   (docs/07 Stage 4 discipline) before treating this as established or contacting the
   authors.
2. Check citing literature for propagation of the erroneous form.
3. No published erratum found as of 2026-07-11.
