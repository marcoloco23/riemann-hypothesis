"""Diagnostic for the claim-1/claim-5 negativity window (110.458, 111.479):
locate nearby critical-line zeros and test the pair-sum explanation
  L(z) = Xi(z)^2 * sum_rho 1/(z - rho)^2   (Hadamard, degree-0 exponential factor
  since Xi is even of order 1 => genus 1 with pairing rho, -rho; sum over ALL
  zeros rho of Xi, paired symmetrically).
We check numerically whether Re L < 0 on s = 1+it near t ~ 111 is driven by the
two closest zeros (a close pair), by comparing Re[Xi^2/(z-rho)^2] terms.
Also: gap statistics of zeros gamma_n in [100, 120] to confirm the close pair.
"""
import mpmath as mp
import common as C

mp.mp.dps = 30
print("zeta zeros gamma_n in [95, 125] and consecutive gaps:")
zs = []
n = 1
# find index range by scanning; zetazero is monotone in n
# rough count N(95) ~ 27 -> start at 20
for n in range(20, 50):
    z = mp.zetazero(n)
    g = mp.im(z)
    if g > 125:
        break
    if g >= 95:
        zs.append((n, g))
prev = None
for n, g in zs:
    gap = (g - prev) if prev is not None else None
    print(f"  n={n:3d}  gamma={mp.nstr(g, 10):>14}  gap={mp.nstr(gap, 6) if gap else '--'}")
    prev = g

print("\nNegativity window of B(t): (110.4583, 111.4786) -- compare with zeros above.")

# Term-by-term: at z = t - i/2 (i.e. s = 1+it), t = 111.1:
mp.mp.dps = 40
t = mp.mpf('111.1')
z = t - mp.mpc(0, 1)/2
Ltrue = C.L_of_z(z)
Xi2 = C.xi(mp.mpc(1, t))**2 * (-1)  # Xi(z) = xi(s); Xi(z)^2 = xi(s)^2
Xi2 = C.xi(mp.mpc(1, t))**2
print("\nRe L at z = 111.1 - i/2:", mp.nstr(mp.re(Ltrue), 10))
acc = mp.mpc(0)
print("running partial sums of Xi^2 * sum 1/(z-rho)^2 over zeros nearest 111 (paired +/-gamma):")
order = sorted(range(20, 60), key=lambda n: abs(mp.im(mp.zetazero(n)) - t))
for i, n in enumerate(order[:12]):
    g = mp.im(mp.zetazero(n))
    for rho in (g, -g):
        acc += 1/(z - rho)**2
    term = Xi2*(1/(z - g)**2 + 1/(z + g)**2)
    print(f"  zero gamma={mp.nstr(g,8):>10}: term Re = {mp.nstr(mp.re(term), 6):>12}, "
          f"partial Re[Xi^2*sum] = {mp.nstr(mp.re(Xi2*acc), 8)}")
print("target Re L =", mp.nstr(mp.re(Ltrue), 8), " (partial sums converge slowly; trend is what matters)")
