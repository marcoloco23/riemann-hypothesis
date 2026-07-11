# front-law: complex-zero geography of Ξ_N near the real axis, N = 3..8

Tests the **moving front law** for strip zeros of the theta truncations
Ξ_N(z) = 4∫₀^∞ Σ_{n≤N} φ_n(u) cos(zu) du (normalization pinned in
`../xi_common.py`, which is reused unchanged): *nonreal zeros with
0 < Im z < 1/2 occur only just past the real-zero front R_N ≈ 4(N+1)², never
in the bulk Re z ≤ 0.9·R_N*. A bulk strip zero would kill the moving-window
program of `attempts/theta-strip`.

**Status: NUMERICAL evidence only** (mpmath, adaptive precision, deterministic;
not interval-certified). Nothing here is a proof.

## Region and method

For each N = 3..8, all zeros of Ξ_N in `[0, X_N] × (0, ~12]`,
X_N = 6(N+1)² + 100, are enumerated:

- **Adaptive precision** (`fl_common.Eval`): in the bulk |Ξ_N(x+iy)| ~ e^{−πx/4}
  (it tracks Ξ), past the front it sits on a floor ~ e^{−π(N+1)²} (for N = 8
  that is ~1e−108), while the constituent terms are of size ~|z|². Every value
  is recomputed at higher dps until it clears the cancellation error bound
  `10·(2+|z|²)·10^{5−dps}` by 8 digits (cap π(N+1)²/ln10 + 45).
- **Counting** = argument principle: adaptive phase-tracking winding number
  (equals ∮ Ξ_N′/Ξ_N dz / 2πi; counts verified to be within 0.02 of an
  integer). A contour point that cannot be resolved above the error bound
  (zero on the contour) aborts the box and the edge is shifted.
- **Column bookkeeping**: per ~10-wide column, the symmetric box
  [x0,x1]×[−ys,ys] (ys ≈ 0.5) gives C_sym = #real + 2·#{0<Im<ys} by conjugate
  symmetry, with contour edges kept ≥ 0.4 from the axis zeros. Any excess
  triggers near-real boxes at ±0.011 and ±0.0005 (certifying no zeros with
  0 < Im ≤ ylo) plus a fine axis rescan. The upper box [ys, ~12] is counted
  directly.
- **Location** = count-guided bisection (`fl_common.isolate`): boxes are split,
  with child counts re-verified to sum to the parent, until each holds one
  zero; Muller locates it; a polish at dps ≈ π(N+1)²/ln10 + 70 verifies the
  residual is < 1e−15 × the local scale |Ξ_N| at distance ~0.013. Roots are
  deduplicated by clustering at 1e−6. **Located count = counted count by
  construction** — this removes the false-accept/dedup failure of the earlier
  locator (absolute residual threshold on a function of local scale 1e−30
  accepted 640 non-zeros; `../out_s05_N234.txt`, N=4).
- **Real zeros**: certified-sign scan (step 0.2 bulk, 0.05 in the front window),
  Anderson polish, and a reality check (Muller from x + 0.01i must return to
  the axis). Column counts cross-validate completeness of the scan.
- **Front fine scan**: [R_N−10, R_N+40] × [0.011, 0.5] recounted independently
  in 5-wide boxes. **Tracked zero**: Muller from seed 4.24(N+1)² + 0.4i.

## Files

- `fl_common.py` — evaluator/winding/isolate/polish machinery (docstring has
  the numerical details).
- `run_front.py N` — full enumeration for one N → `zeros_N<N>.json`,
  progress in `out_N<N>.txt`, appended to `run-output.txt` on completion.
- `analyze.py` — master table, front-law verdict, tracked family, fits
  (appends to `run-output.txt`).
- `run-output.txt` — assembled output of the whole campaign.

## Reproduce

```
cd workspace/scratch/theta-strip/front-law
for N in 3 4 5 6 7 8; do ../venv/bin/python run_front.py $N; done
../venv/bin/python analyze.py
```

Validation anchors reproduced before the campaign (see run-output.txt): the
known N=3 strip zero 67.8801896551476 + 0.4773438417708i, R_3 = 65.032…,
15 real zeros for N=3, and the N=3 upper-arc zeros 71.894+2.804i,
75.694+5.102i, 79.461+7.225i.
