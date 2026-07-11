import mpmath as mp
mp.mp.dps = 40

def xi(s):
    return s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)
def Xi(z):
    return xi(mp.mpf('0.5') + 1j*z)

def L(z):
    Xp  = mp.diff(Xi, z, 1)
    Xpp = mp.diff(Xi, z, 2)
    return Xp**2 - Xi(z)*Xpp

def C(z):  # Jensen quantity
    Xp  = mp.diff(Xi, z, 1)
    Xpp = mp.diff(Xi, z, 2)
    return abs(Xp)**2 - mp.re(Xi(z)*mp.conj(Xpp))

for xv, yv in [('111.1','0.45'), ('111.1','0.5'), ('110.9','0.40'), ('50','0.45')]:
    z = mp.mpf(xv) + 1j*mp.mpf(yv)
    print(f"z = {xv}+{yv}i   Re L = {mp.nstr(mp.re(L(z)), 8):>15}   C = {mp.nstr(C(z), 8):>15}")
