"""Claim 2: Laguerre inequalities for Xi (necessary for RH):
  L_1[Xi](x) = Xi'(x)^2 - Xi(x) Xi''(x) >= 0
  L_2[Xi](x) = (1/12)(Xi Xi'''' - 4 Xi' Xi''' + 3 Xi''^2)  (from claim-1 formula, n=2) >= 0
on x in {0,...,30} and x = 14.134725, 21.022040 (near first two zeros).
"""
import mpmath as mp
from common import Xi, Xi_derivs_real, laguerre_Ln

mp.mp.dps = 40
print("=" * 72)
print("CLAIM 2 -- L_1[Xi] >= 0 and L_2[Xi] >= 0 on grid (dps = 40)")
print("=" * 72)

xs = [mp.mpf(k) for k in range(31)] + [mp.mpf('14.134725'), mp.mpf('21.022040')]
viol = []
print(f"{'x':>12}  {'L_1[Xi](x)':>28}  {'L_2[Xi](x)':>28}")
for x in xs:
    d = Xi_derivs_real(x, 4, radius=1.5)
    L1 = laguerre_Ln(d, 1)
    L2 = laguerre_Ln(d, 2)
    print(f"{mp.nstr(x, 10):>12}  {mp.nstr(L1, 15):>28}  {mp.nstr(L2, 15):>28}")
    if L1 < 0:
        viol.append(('L1', x, L1))
    if L2 < 0:
        viol.append(('L2', x, L2))

print("\nAt the first two zeros (L_1 should reduce to Xi'^2 > 0):")
for x in [mp.mpf('14.134725'), mp.mpf('21.022040')]:
    d = Xi_derivs_real(x, 2, radius=1.0)
    L1 = laguerre_Ln(d, 1)
    print(f"  x={mp.nstr(x, 10)}: Xi = {mp.nstr(d[0], 6)},  Xi'^2 = {mp.nstr(d[1] ** 2, 15)},"
          f"  L_1 = {mp.nstr(L1, 15)},  L_1 - Xi'^2 = {mp.nstr(L1 - d[1] ** 2, 4)}")

if viol:
    print("\nVIOLATIONS FOUND (almost certainly a bug -- investigate!):")
    for tag, x, val in viol:
        print(f"  {tag} at x={mp.nstr(x, 12)}: {mp.nstr(val, 20)}")
else:
    print("\nNo violations: L_1[Xi] >= 0 and L_2[Xi] >= 0 at all grid points. PASS")
