# Draft author correspondence: Dimitrov–Xu correction

**Status:** Ready for human review after the repository has a stable public release.  
**Paper:** Dimitar K. Dimitrov and Yuan Xu, *Wronskians of Fourier and Laplace
Transforms*, Transactions of the AMS 372 (2019), 4107–4125,
DOI [10.1090/tran/7809](https://doi.org/10.1090/tran/7809),
[arXiv:1606.05011](https://arxiv.org/abs/1606.05011).

## Draft email

**Subject:** Possible correction to Theorems 1.1 and 3.2 of “Wronskians of Fourier and Laplace Transforms”

Dear Professors Dimitrov and Xu,

While checking the density criterion in your 2019 paper *Wronskians of Fourier and
Laplace Transforms*, we found what appears to be a sign error in Lemma 3.3 that changes
the kernel in Theorems 1.1 and 3.2.

The Fourier transform of the odd function `sinh(sy)K(s)` is purely imaginary. Retaining
the resulting factor of `i` flips the sign of the corresponding quadratic term. The
addition formula then gives a factor `cosh(y(t−2s))` inside the correlation integral,
rather than `cosh(yt)` outside it. In our notation the corrected kernel is

```text
K̃_{2,y}(t) = ∫ (t−2s)² cosh(y(t−2s)) Φ(t−s)Φ(s) ds,
```

and its Fourier transform is

```text
ℱ[K̃_{2,y}](x)
  = 2[|Ξ′(x+iy)|² − Re(Ξ(x+iy) conjugate(Ξ″(x+iy)))].
```

The printed form is contradicted by the paper's example `φ(z)=2 sin(z)/z`: for `y=2`,
the printed kernel's Fourier transform changes sign and has real zeros near
`x=2.8964132` and `x=4.0153412`. We also found two smaller apparent typographical
issues: a missing `1/n!` in the Andreief normalization and the exponent
`n(n+1)/2` where `n(n−1)/2` matches the derivation.

We have published the derivation, scripts, exact source references, and limitations at:

<https://github.com/marcoloco23/riemann-hypothesis/tree/v0.1.0/workspace/scratch/dimitrov-xu-boundary/dx-erratum>

The work was substantially machine-assisted. A separate blind machine-assisted
re-derivation reproduced the algebra and numerical counterexample, but it has not yet
received independent human peer review. We are contacting you first so you can check
the finding and advise whether we have misunderstood a convention or whether an erratum
would be appropriate.

We would be grateful for any correction or guidance.

Best regards,

marcoloco (`@marcoloco23`)  
Riemann Hypothesis Research Community

## Before sending

- Replace the release link if the public tag differs from `v0.1.0`.
- Attach no third-party paper; link the DOI and arXiv record.
- Re-run `check_dx.py` and `blind_referee_check.py` from the tagged commit.
- Add an independent human review link if one becomes available.
- Send privately to both authors before opening a public journal issue.
