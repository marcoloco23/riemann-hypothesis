# Attempt: theta-strip

**Approach family (docs/05):** none of §1–8 exactly; closest to the Laguerre–Pólya /
Fourier-transform-with-real-zeros circle behind de Bruijn–Newman (docs/03 §12), via
Haglund's incomplete-gamma approximants. The *arithmetic* input is the modular theta
kernel — Euler product enters through `θ(1/u)=√u·θ(u)` (Poisson summation over ℤ), the
same identity that produces the functional equation.

**The idea (one paragraph).** Write `Ξ(z) = ξ(½+iz) = 2∫₀^∞ Φ(u)cos(zu)du` with
`Φ(u) = Σ_n φ_n(u)` the classical theta kernel, and truncate: `Ξ_N` keeps atoms `n ≤ N`.
Truncations are NOT real-rooted (recorded dead end — Ξ₁ already has complex zeros near
`20.63+2.70i`), so the naive Hurwitz plan fails. But **every nontrivial zeta zero maps
into the horizontal strip `|Im z| < ½`**, and numerically the nonreal zeros of `Ξ_N` sit
far above it (Im ≳ 2.7) and only to the right of the last real zero
(`R_N ≈ 4(N+1)²`, Haglund). The weakened finite target — the **finite theta-strip
theorem**: `Ξ_N(z) ≠ 0` for `0 < |Im z| < ½`, all `N` — would give RH by locally uniform
convergence + Hurwitz. **New inputs:** (i) the target is dramatically weaker than
real-rootedness of truncations (which is false); (ii) an exact structural identity: on
the line `Im z = r`, real and imaginary parts of `Ξ_N` are cosh/sinh transforms of the
SAME positive weight `w_N`, with universal monotone ratio `tanh(rv)` — so the question is
a Pólya-style common-zero exclusion for a cosine and a sine transform linked by a
monotone multiplier; (iii) strict likelihood-ratio ordering of theta atoms
(`φ_m/φ_n` ↓ for `m>n`, sign-regularity of order 2) — survives even though full total
positivity of Φ is FALSE (fails at Pólya-frequency order 5, ~2026 result — cite pending).

**What would close it.** A weighted Pólya–Hurwitz separation theorem: if `w > 0` is a
(finite theta) kernel and `0 < r < ½`, then `∫w(v)cosh(rv)cos(tv)dv` and
`∫w(v)sinh(rv)sin(tv)dv` have no common zero `t > 0`. Plus locally uniform convergence
`Ξ_N → Ξ` (Haglund, cite pending).

**Origin.** notes.md (2026-07-11); mapping in `workspace/scratch/notes-triage.md`.
