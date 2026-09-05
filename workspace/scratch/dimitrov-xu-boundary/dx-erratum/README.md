# Erratum finding — Dimitrov–Xu, Trans. AMS 372 (2019) 4107–4125 (arXiv:1606.05011)

**Date:** 2026-07-11. **Tag:** CONFIRMED — independently re-derived 2026-07-12 by a
**blind second reader** (agent given only the PDF, no access to this record, tasked as
hostile referee). The blind pass reproduced every element independently: the Lemma 3.3
dropped-`i` (FT of odd `sinh(sy)K(s)` purely imaginary; `(−i)² = −1` flips the
`ν₂(sinh)` term), the corrected kernel `cosh((t−2s)y)` INSIDE the integral, the Jensen
identity `ℱ[K̃_{2,y}] = 2[|φ'|² − Re(φ·conj(φ''))]` (51-digit agreement on the
Gaussian, where printed vs corrected kernels give `cos(2xy)` vs `(1+2y²)` — qualitatively
different), the Cor. 4.3(b) counterexample (real zeros of the printed kernel's FT at
`x ≈ 2.8964132, 4.0153412` for `y = 2`, 50 dps, kernel `‖·‖₁ ≈ 13.73` so Wiener
applies), AND both side errata (missing `1/n!` in Lemma 2.1/Thm 2.5/Props 2.9–2.10 —
constants off by `n!`, verified ratios `−0.5`, `−1/6`, `6.000…`; sign exponent
`(−1)^{n(n+1)/2}` → `(−1)^{n(n−1)/2}`, wrong for odd n, contradicting the paper's own
p. 5 derivation and eq. (2.3)). Blind verdict: "ERROR FOUND — FATAL TO PRINTED
THEOREM"; proof architecture survives with the corrected kernel. Script preserved:
`blind_referee_check.py` (mp.dps = 50). One nuance from the blind pass: for ζ itself
the printed criterion is *unproven* rather than directly falsified at feasible heights
in ITS scan range (y = 0.4, x ≤ 40; y = 0.49, x ≤ 100 — no sign change there); the
refutation for ζ at `(x, y) = (111.1, 0.45)` from `check_riemann.py` (forced by the
γ₃₄/γ₃₅ close pair) stands and is outside that scan range — the two computations are
consistent. Docs/07 Stage-4 second-reader requirement: **SATISFIED.**

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

- [arXiv:1606.05011v1](https://arxiv.org/abs/1606.05011v1) — authoritative source
  page for the reviewed 17-page version. The PDF is linked rather than redistributed
  from this repository because its arXiv license grants distribution rights to arXiv.
- `check_dx.py` — sin-counterexample numerics (`ℱ[cosh ν₂] = 2Re𝓛`, sign change;
  `ℱ[K̃] = 2𝒞`).
- `check_riemann.py` — Riemann Ξ values at the γ₃₄/γ₃₅ window.
- Context: parent dir `../` (claims 1–5 verification), and
  `attempts/laguerre-phase-space/PROOF.md` §8.9.

## Follow-ups

1. ~~Independent re-derivation of the Lemma 3.3 sign analysis by a second reader~~
   **DONE 2026-07-12** (blind referee pass, see Tag above). The finding may now be
   treated as established in-repo.
2. ~~Check citing literature for propagation~~ **DONE 2026-07-12** (web agent):
   only 3 citing works exist (Panzone PEMS 2021 — background citation in
   Nyman–Beurling context, full text paywalled/UNCONFIRMED but abstract+refs show no
   density-criterion use; Polson arXiv:1804.10043 — passing list citation, DROPPED in
   its current v8; Whitehead–Pereira figshare 2026 preprint — passing pointer with
   garbled bibliographic data). **No paper uses Thm 1.1 as a logical ingredient; the
   error has not propagated.** zbMATH review (Zbl 1476.11117, by M. Balazard) does not
   restate the kernel formula and endorses only the architecture.
3. ~~No published erratum as of 2026-07-11~~ **CONFIRMED 2026-07-12**: no erratum/
   corrigendum on arXiv, AMS/TAMS, Crossref, zbMATH, Semantic Scholar. arXiv has ONE
   version (v1, 2016-06-16, never updated); published version (received 2017-07-28,
   revised 2018-07-31, DOI 10.1090/tran/7809) has **Theorem 1.1 verbatim identical to
   v1** (cosh(ty) OUTSIDE the integral in both); only substantive v1→print change is
   the LP-class definition typo fix in the introduction. Diff artifacts + saved PDFs
   recorded by the agent (tams.pdf vs arxiv.pdf).
4. Whether to contact the authors: **user decision, pending** (finding is now
   double-checked, so the prerequisite is met).
5. Extra blind-pass detail worth keeping: the printed Thm 3.2's x=0 positivity step
   (p. 14) is only justified for `K ≥ 0`, not for arbitrary signed even Schwartz K
   that its hypotheses allow — a further (minor) gap independent of the kernel error.
