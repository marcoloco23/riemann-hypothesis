# Bibliography

Citation keys used across `docs/` and `workspace/`. Add an entry whenever you rely on an
external result (docs/01 §E9). Keep statements precise enough that a reviewer can check the
use matches the source. (Page/edition details to be filled in as sources are consulted.)

## Primary sources & monographs

- **[Riemann1859]** B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen
  Größe*, Monatsberichte der Berliner Akademie, 1859. The original memoir.
- **[Titchmarsh]** E. C. Titchmarsh (rev. D. R. Heath‑Brown), *The Theory of the
  Riemann Zeta‑Function*, 2nd ed., Oxford, 1986. Standard analytic reference.
- **[IK]** H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloquium Publ. 53, 2004.
- **[Edwards]** H. M. Edwards, *Riemann's Zeta Function*, Academic Press, 1974 (Dover repr.).
- **[MontgomeryVaughan]** H. Montgomery, R. Vaughan, *Multiplicative Number Theory I*, 2007.
- **[Conrey2003]** J. B. Conrey, *The Riemann Hypothesis*, Notices AMS 50(3), 2003 — survey.
- **[Bombieri-CMI]** E. Bombieri, *Problems of the Millennium: The Riemann Hypothesis*,
  Clay Mathematics Institute official problem description.
- **[Mazur-Stein]** B. Mazur, W. Stein, *Prime Numbers and the Riemann Hypothesis*, 2016.

## Zeros on the line / proportion

- **[Hardy1914]** G. H. Hardy, *Sur les zéros de la fonction ζ(s) de Riemann*, C. R. Acad.
  Sci. Paris 158 (1914), 1012–1014.
- **[Selberg1942]** A. Selberg, *On the zeros of Riemann's zeta‑function*, 1942.
- **[Levinson1974]** N. Levinson, *More than one third of zeros of Riemann's zeta‑function
  are on σ=1/2*, Adv. Math. 13 (1974).
- **[Conrey1989]** J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta
  function are on the critical line*, J. Reine Angew. Math. 399 (1989).

## Zero‑free regions / density

- **[Hadamard1896]**, **[dlVP1896]** Hadamard; de la Vallée Poussin — PNT and first
  zero‑free region (1896).
- **[VK58]** Vinogradov (1958), Korobov (1958) — the widest known zero‑free region.
- **[GuthMaynard2024]** L. Guth, J. Maynard, *New large value estimates for Dirichlet
  polynomials*, 2024 — improved zero‑density near σ=3/4.

## Equivalent formulations

- **[Robin1984]** G. Robin, *Grandes valeurs de la fonction somme des diviseurs et
  hypothèse de Riemann*, J. Math. Pures Appl. 63 (1984).
- **[Lagarias2002]** J. Lagarias, *An elementary problem equivalent to the Riemann
  hypothesis*, Amer. Math. Monthly 109 (2002).
- **[Li1997]** X.‑J. Li, *The positivity of a sequence of numbers and the Riemann
  hypothesis*, J. Number Theory 65 (1997), 325–333. Defines `λ_n`; RH ⇔ `λ_n ≥ 0 ∀n`.
- **[BombieriLagarias1999]** E. Bombieri, J. C. Lagarias, *Complements to Li's criterion
  for the Riemann hypothesis*, J. Number Theory 77 (1999), 274–287. Li's criterion as a
  case of Weil positivity; arithmetic (explicit‑formula) expression for `λ_n`.
- **[Maslanka2004]** K. Maślanka, *Li's criterion for the Riemann hypothesis — numerical
  approach*, Opuscula Math. 24 (2004). Numerical computation of `λ_n`. (Evidence only.)
- **[Baez-Duarte2003]** L. Báez‑Duarte, *A strengthening of the Nyman–Beurling criterion
  for the Riemann hypothesis*, 2003.
- **[OdlyzkoteRiele1985]** A. Odlyzko, H. te Riele, *Disproof of the Mertens conjecture*,
  J. Reine Angew. Math. 357 (1985). ⚠️ Cautionary: numerically‑overwhelming ⇏ true.

## Spectral / NCG / positivity / function field

- **[Montgomery1973]** H. Montgomery, *The pair correlation of zeros of the zeta function*,
  Proc. Sympos. Pure Math. 24 (1973).
- **[BerryKeating1999]** M. Berry, J. Keating, *The Riemann zeros and eigenvalue
  asymptotics*, SIAM Review 41 (1999).
- **[Connes1999]** A. Connes, *Trace formula in noncommutative geometry and the zeros of
  the Riemann zeta function*, Selecta Math. 5 (1999).
- **[ConnesConsani2021]** A. Connes, C. Consani, *Weil positivity and trace formula, the
  archimedean place*, Selecta Math. 27 (2021), no. 77. Weil positivity proved for test
  functions of restricted scaling support (the prime‑free window); the frontier is
  crossing the first prime.
- **[ConreyLi2000]** J. B. Conrey, X.‑J. Li, *A note on some positivity conditions related
  to zeta and L‑functions*, IMRN 2000 — obstruction to the de Branges approach.
- **[Weil1948]** A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*,
  1948 — RH for curves over finite fields.
- **[Deligne1974]** P. Deligne, *La conjecture de Weil I*, Publ. IHÉS 43 (1974);
  **[Deligne1980]** *…II*, Publ. IHÉS 52 (1980).
- **[Selberg1992]** A. Selberg, *Old and new conjectures and results about a class of
  Dirichlet series*, 1992 — the Selberg class axioms.

## Herglotz / Pick / Weil‑positivity (attempt pick-kernel-positivity)

- **[Lagarias1999]** J. C. Lagarias, *On a positivity property of the Riemann ξ‑function*,
  Acta Arith. 89 (1999), no. 3, 217–234; **with published Correction**, Acta Arith. 116
  (2005), 293–294 (fixes Lemma 3.1; main result stands — cite both together).
  Statement: RH ⇔ `Re(ξ'/ξ(s)) > 0` for all `Re(s) > 1/2`. (Positivity for `Re(s) ≥ 1` is
  unconditional, due to Hinkkanen.)
- **[Suzuki2023]** M. Suzuki, *Aspects of the screw function corresponding to the Riemann
  zeta‑function*, J. London Math. Soc. 108 (2023), 1448–1487, arXiv:2206.03682.
- **[Suzuki2023-Weil]** M. Suzuki, *On the Hilbert space derived from the Weil
  distribution*, arXiv:2301.00421; DOI 10.4153/S0008414X25101739 (Canad. J. Math., 2025 —
  venue string UNCONFIRMED). Completion of `C_c^∞` under the Weil form; RH equivalences.
- **[Suzuki2026]** M. Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096 (June 2026, preprint). Unifies Yoshida/Bombieri/Connes–Consani(–
  Moscovici) treatments of the Weil form without assuming RH; conjectures a self‑adjoint
  operator with eigenvalues = imaginary parts of zeros as an `a → ∞` limit of finite
  self‑adjoint operators on `[−a,a]`.
- **[Connes2026]** A. Connes, *The Riemann Hypothesis: Past, Present and a Letter Through
  Time*, arXiv:2602.04022 (Feb 2026) — survey; RH remains open as of this survey.
- **[ConnesMoscovici2022]** A. Connes, H. Moscovici, *The UV prolate spectrum matches the
  zeros of zeta*, PNAS 119 (2022), e2123174119.
- **[CCM2024]** A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave
  operators*, Ann. Funct. Anal. 15 (2024), no. 87, arXiv:2310.18423.
- **[CCM2025]** A. Connes, C. Consani, H. Moscovici, *Zeta Spectral Triples*,
  arXiv:2511.22755 (Nov 2025, preprint). Rank‑one perturbations of the scaling spectral
  triple using Euler factors `p ≤ λ²`; a rigorous `N, λ → ∞` convergence proof would
  establish RH (explicitly a proposed strategy, not a proof).

## Theta approximants / Laguerre–Pólya (attempts theta-strip, laguerre-phase-space)

- **[Haglund2011]** J. Haglund, *Some conjectures on the zeros of approximates to the
  Riemann Ξ‑function and incomplete gamma functions*, Cent. Eur. J. Math. 9 (2011),
  302–318, arXiv:0910.5228. Defines `Ξ_N` via incomplete gamma functions; **Conjecture 1**
  (monotonic zeros in the first quadrant; weaker Remark‑1 form: nonreal zeros lie to the
  right of the largest real zero, verified numerically for N ≤ 10); **Proposition 1**:
  Conjecture 1 for all N ⟹ RH. Locally‑uniform convergence `Ξ_N → Ξ` is asserted from
  Riemann's uniformly convergent expansion (not separately proved there).
- **[CSV1994]** G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de
  Bruijn–Newman constant Λ, and the Riemann Hypothesis*, Constr. Approx. 10 (1994),
  107–129. Origin of the heat‑flow zero dynamics `ẋ_k = 2Σ_{j≠k} 1/(x_k−x_j)` (restated
  precisely as [RodgersTao2020] Thm 11; hypotheses: zeros real, simple, distinct;
  principal‑value sums).
- **[CsordasVarga1990]** G. Csordas, R. S. Varga, *Necessary and sufficient conditions and
  the Riemann Hypothesis*, Adv. Appl. Math. 11 (1990), 328–357. Thm 2.9: for
  `f ∈ 𝔖(A)` (order ≤ 2 Hadamard form `Ce^{−az²+bz}z^m Π(1−z/z_k)e^{z/z_k}`, `a ≥ 0`,
  `b ∈ ℝ`, zeros in `|Im z| ≤ A`, `Σ|z_k|^{−2} < ∞`): `f ∈ LP ⇔ L_n[f](x) ≥ 0 ∀n,x`.
  Thm 2.10/2.12: the complex Laguerre inequality `|f'(z)|² ≥ Re(f(z)·conj(f''(z)))` on ℂ
  ⇔ `f ∈ LP`, same `𝔖(A)` hypothesis. ⚠️ The strip confinement of zeros is a genuine
  hypothesis — satisfied by `Ξ` **unconditionally** (`|Im z| < ½`).
- **[Patrick1973]** M. L. Patrick, *Extensions of inequalities of the Laguerre and Turán
  type*, Pacific J. Math. 44 (1973), 675–682 — necessity direction (`LP ⟹ L_n ≥ 0`).
- **[CsordasEscassut2005]** G. Csordas, A. Escassut, *The Laguerre inequality and the
  distribution of zeros of entire functions*, Ann. Math. Blaise Pascal 12 (2005), 331–345
  — clean restatements (Thms 2.2, 2.3, 2.4) of the above.
- **[CsordasVishnyakova2013]** G. Csordas, A. Vishnyakova, *The generalized Laguerre
  inequalities and functions in the Laguerre–Pólya class*, Cent. Eur. J. Math. 11 (2013),
  1643–1650 — drops a‑priori order/type assumptions.
- **[Michalowski2026]** W. Michałowski, *On the Pólya Frequency Order of the de
  Bruijn–Newman Kernel: Certified Failure at Order Five and the Toeplitz Threshold
  Phenomenon*, arXiv:2602.20313 (Feb 2026, **unrefereed preprint**). The kernel
  `K(u) = Φ(|u|)` is not PF₅ (certified 5×5 Toeplitz minor, interval arithmetic); PF₄
  left open.
- **[BianePitmanYor2001]** P. Biane, J. Pitman, M. Yor, *Probability laws related to the
  Jacobi theta and Riemann zeta functions, and Brownian excursions*, Bull. AMS 38 (2001),
  435–465, arXiv:math/9912170. Eqs. (1.4)–(1.5): `Y = √(2/π)·(range of Brownian bridge)`
  satisfies `E[Y^s] = 2ξ(s)` for all `s ∈ ℂ`.
- **[DimitrovXu2019]** D. K. Dimitrov, **Yuan** Xu, *Wronskians of Fourier and Laplace
  transforms*, Trans. AMS 372 (2019), 4107–4125, arXiv:1606.05011.
  **⚠️ ERRATUM FOUND IN-REPO (2026-07-11, needs independent re-derivation before
  external use):** Thm 1.1/3.2 as printed — kernel `Φ_{2,y}(t) =
  cosh(ty)∫(t−2s)²Φ(t−s)Φ(s)ds`, weight OUTSIDE — is **false** (sign error in their
  Lemma 3.3: `ℱ[sinh(·y)K]` is purely imaginary; dropped `i` squares to `−1`);
  unconditional counterexample from their own Cor. 4.3 b) (`φ = 2sin z/z`). **Corrected
  form:** `K̃_{2,y}(t) = ∫(t−2s)²cosh(y(t−2s))Φ(t−s)Φ(s)ds` (weight INSIDE, on the
  difference variable), `ℱ[K̃_{2,y}] = 2𝒞(x+iy)` (Jensen quantity); RH ⇔ translates of
  `K̃_{2,y}` dense in `L¹` for each `y ∈ (−½,½)\{0}` ⇔ `𝒞(x+iy) > 0`; all-y version ⇔
  real and simple zeros. The corrected criterion = Jensen's convexity criterion via
  Wiener density. Side errata: missing `1/n!` in their Lemma 2.1; exponent
  `n(n+1)/2` vs `n(n−1)/2` typo (coincide for even n). Record:
  `workspace/scratch/dimitrov-xu-boundary/dx-erratum/`. Cite only in corrected form.
- **[Csordas2015]** G. Csordas, *Fourier transforms of positive definite kernels and the
  Riemann ξ-function*, Comput. Methods Funct. Theory 15 (2015), 373–391, arXiv:1309.0055.
  **Open Problem 4.7:** `L₁[Ξ](x) ≥ 0 ∀x` is OPEN unconditionally; Remark 4.8:
  follows from RH; failure would disprove RH; strict `>` gives simplicity; known
  unconditionally for `|x| < 1.09×10⁹`. Thm 4.5: Φ is a strictly log-concave admissible
  kernel.
- **[CsordasVarga1988]** G. Csordas, R. S. Varga, *Moment inequalities and the Riemann
  hypothesis*, Constr. Approx. 4 (1988), 175–198. Thm 2.1: `log Φ(√t)` strictly concave
  (⟹ strict log-concavity of Φ on `ℝ\{0}`, cf. [Csordas2015, Rmk 4.3(a)]; NOT proved in
  CNV 1986, which concerns `log K_Φ`).
- **[CsordasRuttanVarga1991]** G. Csordas, A. Ruttan, R. S. Varga, *The Laguerre
  inequalities with applications to a problem associated with the Riemann hypothesis*,
  Numer. Algorithms 1 (1991), 305–329 — numerical `L₁` study near Lehmer pairs.

## Litmus‑test functions (counterexamples sharing ζ's functional equation)

- **[DavenportHeilbronn1936]** H. Davenport, H. Heilbronn, *On the zeros of certain
  Dirichlet series*, J. London Math. Soc. 11 (1936) — functional equation, zeros off the
  line; Epstein zeta with class number > 1.
- **[BombieriHejhal1995]** E. Bombieri, D. Hejhal, *On the distribution of zeros of linear
  combinations of Euler products*, Duke Math. J. 80 (1995) — positive proportion of
  Davenport–Heilbronn zeros off the critical line.

## de Bruijn–Newman

- **[RodgersTao2020]** B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non‑negative*,
  Forum Math. Pi 8 (2020), e6, arXiv:1801.05914. Zero dynamics = their Thm 11 (originally
  [CSV1994]).
- **[Polymath15-2019]** D.H.J. Polymath, *Effective approximation of heat flow evolution
  of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*,
  Res. Math. Sci. 6 (2019), no. 31, arXiv:1904.12438. `Λ ≤ 0.22` unconditional; `Λ ≤ 0.2`
  combining with [PlattTrudgian2021]. No better bound known as of 2026‑07.
- **[PlattTrudgian2021]** D. Platt, T. Trudgian, *The Riemann hypothesis is true up to
  3·10¹²*, Bull. LMS 53 (2021), 792–797, arXiv:2004.09765.

## Numerical verification

- **[Gourdon2004]** X. Gourdon, *The 10^13 first zeros of the Riemann zeta function …*,
  2004 (preprint).
- **[Platt-Trudgian]** D. Platt, T. Trudgian — rigorous verification of RH to large height;
  rigorous `ζ` computation via interval arithmetic.
- **[OdlyzkoZeros]** A. Odlyzko — tables and statistics of zeros at height ~10^20–10^22.

## Classical analysis (textbook theorems cited by name)

- **[Remmert1991]** R. Remmert, *Theory of Complex Functions*, GTM 122, Springer, 1991.
  Used for: **Pringsheim's theorem** (a power series with non‑negative coefficients and
  finite radius of convergence `R` has a singularity at `z = R`), Cauchy–Hadamard.
- **[Apostol1976]** T. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.
  Used for: Dirichlet‑series convergence (Abel summation), `η(s) = (1−2^{1−s})ζ(s)`,
  alternating‑series bounds.
- **[Spira1968]** R. Spira, *Some zeros of the Titchmarsh counterexample*, Math. Comp. 22
  (1968). Numerical location of off‑line zeros of the Davenport–Heilbronn function.

## Formalization

- **[mathlib]** The mathlib4 library (Lean 4). Modules: `NumberTheory.LSeries.*`,
  `NumberTheory.ZetaFunction`, `NumberTheory.PrimeCounting`, PNT formalization. Pin the
  exact revision used in `formal/`.
