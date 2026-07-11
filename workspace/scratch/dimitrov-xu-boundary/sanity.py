import time
import mpmath as mp
import common as C

# 1) xi functional-equation + known value sanity at dps 50
mp.mp.dps = 50
print("xi(1/2)             =", C.xi(mp.mpf(1)/2))
print("xi(2)               =", C.xi(2), " (should equal xi(-1))", C.xi(-1))
print("Xi(0) real?         =", C.xi(mp.mpf(1)/2))

# 2) analytic-derivative composition vs mpmath.diff of xi directly
s0 = mp.mpc(1, 30)
x0, x1, x2 = C.xi_derivs(s0)
d1 = mp.diff(C.xi, s0, 1)
d2 = mp.diff(C.xi, s0, 2)
print("xi'  rel err vs diff:", mp.nstr(abs(x1-d1)/abs(d1), 5))
print("xi'' rel err vs diff:", mp.nstr(abs(x2-d2)/abs(d2), 5))
w_direct = x0*x2 - x1*x1
w_form   = C.wronskian_s(s0)
print("wronskian form rel err:", mp.nstr(abs(w_direct-w_form)/abs(w_form), 5))

# 3) Fourier normalization pin: Xi(x) vs 2 int_0^inf Phi(u) cos(xu) du at x = 2
mp.mp.dps = 40
for x in [0, 2]:
    lhs = C.xi(mp.mpf(1)/2 + mp.mpc(0,1)*x)
    rhs = 2*mp.quad(lambda u: C.Phi(u)*mp.cos(x*u), [0, 1, 2, 3.5])
    print(f"x={x}: Xi(x)={mp.nstr(lhs,20)}  2*int Phi cos={mp.nstr(rhs,20)}  ratio={mp.nstr(lhs/rhs,20)}")

# 4) timing of one zeta triple at dps 130 and 170 at t=110
for dps in (130, 170):
    mp.mp.dps = dps
    t0 = time.time()
    b = C.B_boundary(mp.mpf(110))
    print(f"dps={dps}: B(110) = {mp.nstr(b, 12)}   ({time.time()-t0:.2f}s)")
