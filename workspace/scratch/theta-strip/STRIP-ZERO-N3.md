# REFUTATION RECORD — finite theta-strip conjecture fails at N = 3

**Date:** 2026-07-11. **Status tag:** NUMERICAL (high-confidence; two independent
implementations; not interval-certified).

## The zero

With `Ξ_N(z) = 4∫₀^∞ Σ_{n≤N} φ_n(u) cos(zu) du` (normalization pinned in
`xi_common.py`; `Ξ_N → Ξ = ξ(½+i·)`):

```
Ξ_3(z₀) = 0   at   z₀ = 67.8801896551476196444591034891
                        + 0.477343841770822985689697858444 i
```

- Inside the strip `0 < Im z < ½`: margin `½ − Im z₀ = 0.0226561582292`.
- Found: argument-principle phase count = 1.000…(1e−31-close) over
  `[34.5, 69.5] × [0.02, 0.48]` (`out_s05_N234.txt`), then grid + `findroot`.
- Verified: closed-form (incomplete-gamma) implementation gives `|Ξ_3(z₀)| ≈ 4e−51`
  at dps 50; **independent direct quadrature** of the defining integral gives
  `|Ξ_3(z₀)| ≈ 9e−66` at dps 60, against local scale `|Ξ_3| ~ 4e−21` (ratio ~1e−45).
- Consistency: near-real boxes confirm all 15 real zeros of `Ξ_3` are genuinely real
  (max |Im| after polish 2.4e−47); the strip zero is not a perturbed real zero.

## Context

- `R_3` (largest real zero of `Ξ_3`) ≈ 65.032 — the strip zero sits just past the
  real-zero front, consistent with front-attached complex zeros bending toward the
  axis. Min-Im of nonreal zeros by N: N=1: 2.697, N=2: 3.281, **N=3: 0.4773**,
  N=4: 0.73 (scan to Re ≤ 200) — NOT monotone, and NOT bounded below by ½.
- Haglund's Conjecture 1 / Remark-1 form is NOT contradicted: `Re z₀ = 67.88 > R_3`.
  The claim in notes.md that "nonreal zeros of Ξ_N for N ≤ 10 have Im ≳ 2.7" is FALSE.

## Consequence

The per-N strip statement `Ξ_N ≠ 0` in `0 < |Im z| < ½` (attempts/theta-strip PROOF.md
§2) is FALSE at N = 3, so it cannot be the route to RH. The Hurwitz argument only needs
the weaker **moving-window form** (every compact subset of the open strip is eventually
zero-free), which is consistent with all data — see the attempt's revised §2.

## Reproduce

```
cd workspace/scratch/theta-strip && ./venv/bin/python - <<'EOF'
from mpmath import mp, mpc
import xi_common as xc
mp.dps = 50
r = mp.findroot(lambda z: xc.Xi_N(z, 3), mpc('67.8801896551','0.4773438418'))
print(r, abs(xc.Xi_N(r, 3)))
EOF
```
