import mpmath as mp
mp.mp.dps = 30

# Example: w = chi_(-1,1), phi(z) = F w (z) = 2 sin z / z  (LP class, real simple zeros at k*pi)
def phi(z):  return 2*mp.sin(z)/z if z != 0 else mp.mpf(2)
def phip(z): return 2*(z*mp.cos(z)-mp.sin(z))/z**2
def phipp(z):return 2*(-z**2*mp.sin(z)-2*z*mp.cos(z)+2*mp.sin(z))/z**3

# nu2(w;t) = int (2s-t)^2 w(s) w(t-s) ds = (1/3)(2-|t|)^3 on [-2,2]  (paper, after Cor 2.12)
def nu2(t):
    a = abs(t)
    return (2-a)**3/mp.mpf(3) if a < 2 else mp.mpf(0)

# candidate 1 (paper / "outside" weight): F[cosh(y t) nu2(t)](x)
def FT_outside(x, y):
    f = lambda t: mp.cosh(y*t)*nu2(t)*mp.cos(x*t)   # even integrand
    return 2*mp.quad(f, [0, 2])

# corrected kernel ("inside" weight cosh(y*(t-2s))):
# Ktil(t) = int (t-2s)^2 cosh(y(t-2s)) w(t-s) w(s) ds , w=chi_(-1,1)
def Ktil(t, y):
    lo, hi = max(-1, t-1), min(1, t+1)
    if lo >= hi: return mp.mpf(0)
    f = lambda s: (t-2*s)**2*mp.cosh(y*(t-2*s))
    return mp.quad(f, [lo, hi])

def FT_inside(x, y):
    f = lambda t: Ktil(t, y)*mp.cos(x*t)   # Ktil even in t
    return 2*mp.quad(f, [0, 2])

def L(z):   # Landau-type: phi'^2 - phi*phi''
    return phip(z)**2 - phi(z)*phipp(z)
def C(z):   # Jensen quantity: |phi'|^2 - Re(phi * conj(phi''))
    return abs(phip(z))**2 - mp.re(phi(z)*mp.conj(phipp(z)))

y = mp.mpf('0.8')
print("x      FT_out          2ReL           FT_in           2C")
for x in ['0.5','2.0','3.5','6.0']:
    x = mp.mpf(x); z = x + 1j*y
    print(x, mp.nstr(FT_outside(x,y),12), mp.nstr(2*mp.re(L(z)),12),
             mp.nstr(FT_inside(x,y),12),  mp.nstr(2*C(z),12))

# Scan for negativity of 2 Re L(x+iy) (i.e., FT of the PAPER's kernel) for larger y
for yv in ['2','3','5']:
    y = mp.mpf(yv)
    neg = None
    x = mp.mpf('0.1')
    while x < 40:
        v = mp.re(L(x+1j*y))
        if v < 0: neg = (x, v); break
        x += mp.mpf('0.1')
    print("y =", yv, "first negativity of Re L(x+iy):", neg and (mp.nstr(neg[0],6), mp.nstr(neg[1],6)))
    # C should stay positive (phi in LP, simple real zeros => Jensen strict for y!=0)
    minC = min(C(mp.mpf(x0)/10 + 1j*y) for x0 in range(1, 400))
    print("      min of C on scan:", mp.nstr(minC, 6))
