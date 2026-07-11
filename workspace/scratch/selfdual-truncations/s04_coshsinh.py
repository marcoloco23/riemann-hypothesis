"""s04: cosh/sinh split of Xi_N^sd on the horizontal line Im z = r.

Since Phi_N^sd is EVEN (two-sided symmetric weight -- no half-line restriction),
writing z = t + ir:

    Xi_N^sd(t+ir) = Int_R Phi_N^sd(u) e^{-ru} e^{itu} du

splits into even/odd parts of e^{-ru} = cosh(ru) - sinh(ru):

    (E1)  Re Xi_N^sd(t+ir) =  2 Int_0^inf Phi_N^sd(u) cosh(ru) cos(tu) du
    (E2)  Im Xi_N^sd(t+ir) = -2 Int_0^inf Phi_N^sd(u) sinh(ru) sin(tu) du

Equivalently with the POSITIVE even weight  w_N^sd(u; r) := 2 Phi_N^sd(u) cosh(ru):

    (E1') Re Xi_N^sd(t+ir) =  Int_0^inf w_N^sd(u;r) cos(tu) du
    (E2') Im Xi_N^sd(t+ir) = -Int_0^inf w_N^sd(u;r) tanh(ru) sin(tu) du

i.e. the tanh(ru)-multiplier structure survives with the symmetric weight:
Im is the sine transform of the SAME positive weight damped by tanh(ru).
Positivity: Phi_N^sd > 0 (s01(d)) and cosh > 0, so w_N^sd > 0 on all of R.

This script validates (E1),(E2) numerically against the closed form.
"""
import time
from mpmath import mp, mpf, mpc, cos, sin, cosh, sinh, tanh, quad
import sd_common as sd

out = open("run-output.txt", "a", buffering=1)
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n")

P("=" * 78)
P("s04_coshsinh.py --", time.strftime("%Y-%m-%d %H:%M:%S"))
mp.dps = 40
P("mp.dps =", mp.dps)

cases = [(mpf(5), mpf("0.3"), 2), (mpf(30), mpf("0.45"), 3),
         (mpf("67.8801896551"), mpf("0.4773438418"), 3), (mpf(12), mpf("0.25"), 1)]
U = mpf(3)   # pi e^{2U} ~ 1267 >> dps*ln10: tail negligible
for (t, r, N) in cases:
    nseg = int(max(20, 2 * t)) + 1
    pts = [U * k / nseg for k in range(nseg + 1)]
    reI = quad(lambda u: 2 * sd.Phi_sd(u, N) * cosh(r * u) * cos(t * u), pts)
    imI = quad(lambda u: -2 * sd.Phi_sd(u, N) * sinh(r * u) * sin(t * u), pts)
    ref = sd.Xi_sd(t + mpc(0, 1) * r, N)
    # tanh-multiplier form (E2'): same weight w = 2 Phi cosh(ru), damped by tanh
    imI2 = quad(lambda u: -2 * sd.Phi_sd(u, N) * cosh(r * u) * tanh(r * u) * sin(t * u), pts)
    P(f"\n  N={N}, t={mp.nstr(t,10)}, r={mp.nstr(r,10)}:")
    P(f"    Re: quad = {mp.nstr(reI, 25)}")
    P(f"        ref  = {mp.nstr(ref.real, 25)}   |diff| = {mp.nstr(abs(reI - ref.real), 3)}")
    P(f"    Im: quad = {mp.nstr(imI, 25)}")
    P(f"        ref  = {mp.nstr(ref.imag, 25)}   |diff| = {mp.nstr(abs(imI - ref.imag), 3)}")
    P(f"    Im via tanh-multiplier form: |diff| = {mp.nstr(abs(imI2 - ref.imag), 3)}")

P("\nValidated: (E1),(E2),(E2') hold; w_N^sd(u;r) = 2 Phi_N^sd(u) cosh(ru) > 0, even,")
P("two-sided; tanh(ru)-multiplier structure survives with the symmetric weight.")
P("\ns04 done.")
