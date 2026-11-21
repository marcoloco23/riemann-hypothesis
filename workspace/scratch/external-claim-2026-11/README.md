# external-claim-2026-11 — numeric anchor for lemma L11

**Purpose:** regression check of the explicit formula in
[`lemmas/L11`](../../lemmas/L11-smoothed-mangoldt-statistic.md) for the smoothed von
Mangoldt statistic named in step 5 of the 2026-11-20 announcement
([record](../../../docs/10-external-claim-2026-11.md)).

Motivational only (docs/01 B1): it catches sign and constant errors. It certifies no
infinite tail and says nothing about zeros beyond the ones used.

```sh
python workspace/scratch/external-claim-2026-11/smoothed_mangoldt.py 400
```

Environment: Python 3, `mpmath==1.3.0`. About 25 seconds, under 0.1 GB.
Selected output is in [`run-output.txt`](run-output.txt): with 400 zeros the two sides
agree to within the omitted tail (`2.66e-3` per `√X`; observed `≤ 6.1e-5`) for seven
values of `X` up to `2×10⁶`, and `|F(X) − log 2π|/√X ≤ 0.0139`, inside the bound
`2 + γ − log 4π = 0.04619…` that L11 derives from RH.
