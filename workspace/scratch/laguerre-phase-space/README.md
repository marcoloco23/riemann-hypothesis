# Generalized Laguerre inequalities and a phase-space representation for Ξ

Verification workspace (numerics motivate, never prove). `Ξ(z) := ξ(½+iz)`,
`ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)`; Ξ is real entire and even.

## Setup

    python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
    sh run_all.sh          # writes run-output.txt (deterministic)

## Files

- `common.py` — pole-free ξ (`½sΓ(s/2)=Γ(s/2+1)` form), Ξ, trapezoidal-Cauchy
  derivatives with N-doubling validation, `L_n` evaluator.
- `claim1.py` — `|f(x+iy)|² = Σ_n L_n[f](x) y^{2n}` with
  `L_n[f] = (1/(2n)!) Σ_j (−1)^{j+n} C(2n,j) f^{(j)} f^{(2n−j)}`:
  sympy through `y^6` + numerics for Ξ. **VERIFIED.**
- `claim2.py` — `L_1[Ξ] ≥ 0`, `L_2[Ξ] ≥ 0` on `x ∈ {0..30}` + first two zeros.
  **All positive** (dps 40). Necessary conditions for RH; no violation.
- `claim3.py` — hierarchy for `H_t`: Claim A (double-integral = operator form)
  and Claim B `∂_t L_n = −½∂_x²L_n + (n+1)(2n+1)L_{n+1}` at integrand level;
  sympy + numeric test with `φ = e^{−u²−u⁴}`. **VERIFIED** (differentiation
  under the integral assumed, justified by rapid decrease).
- `claim4.py` — `C_f = |f'|² − Re(f·conj(f''))`:
  (i) `C_f(x+iy) = ½∂_y²|f(x+iy)|² = Σ_{n≥1} n(2n−1)L_n y^{2n−2}` (sympy). **VERIFIED.**
  (ii) **Both** candidate forms are exactly right and equal (ψ even ⇒ W(·,x) even):
  `C_f = ½∫_0^∞ p² cosh(py) W(p,x) dp = ¼∫_ℝ p² e^{−py} W(p,x) dp`,
  `W(p,x) = ∫ψ((p+q)/2)ψ((p−q)/2)cos(xq)dq`. Proof: substitute
  `f = ∫ψe^{izu}du`, symmetrize, set `p=u+v, q=u−v` (Jacobian ½). Gaussian
  test agrees to ~30 digits.
- `claim5.py` — `C_Ξ(x,y) > 0` on the 5×4 grid and at the Lehmer-pair point
  `(7005.063, 0.05)` (`≈ 1.2333e−4765`). **All positive.**
- `crosscheck.py` — two independent methods agree per point; also documents the
  pitfall below.

## Numerical pitfall found (not a math error)

`mpmath.diff(..., method='quad')` is **unreliable for functions of tiny
absolute magnitude**: `quadts`'s stopping rule is effectively absolute, so with
`|Ξ| ~ 1e−2385` near `t ≈ 7005` it accepts the coarsest level and returns
radius-dependent values with up to ~1e−2 relative error (identical at dps 30
and 45). All Ξ-derivatives here therefore use an explicit N-point trapezoidal
Cauchy rule (spectrally accurate, validated by N-doubling and radius
independence) and, at the Lehmer point, central differences with step halving
as an independent method.
