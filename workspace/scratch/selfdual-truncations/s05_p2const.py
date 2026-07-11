"""s05: explicit P2 constants for the far-tail zero-free zone of Xi_N, N = 1..8.

Kernel (theta-strip normalization, Xi_N = 4 Int_0^inf K_N(u) cos(xu) du):
    K_N(u) = sum_{n<=N} phi_n(u),
    phi_n(u) = 2 pi^2 n^4 e^{9u/2} e^{-a e^{2u}} - 3 pi n^2 e^{5u/2} e^{-a e^{2u}},  a = pi n^2.

Exact symbolic derivatives: an atom c e^{alpha u} e^{-a e^{2u}} differentiates to
alpha*c at alpha  and  -2ac at alpha+2 (same a).  All derivatives below are exact
finite sums of such atoms (no numerical differentiation except cross-checks).

Constants (10 digits):
    d_N      = K_N'(0)      [= -sum_{n>N} phi_n'(0) via theta identity; both routes]
    K_N'''(0)               [both routes]
    M4_N     = Int_0^inf |K_N''''(u)| e^{u/2} du     [piecewise quad, split at
                                                      sign changes of K_N'''']
    T_N      = sqrt( (|K_N'''(0)| + M4_N) / d_N )
Sanity: 4 d_N = J_N (s02) and Xi_N(x) x^2 / (-4 d_N) -> 1 (x = 400, 800; N = 1, 2).
"""
import time
from mpmath import mp, mpf, pi, exp, quad, sqrt, fabs
import sd_common as sd

out = open("run-output.txt", "a", buffering=1)
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.write(s + "\n")

P("=" * 78)
P("s05_p2const.py --", time.strftime("%Y-%m-%d %H:%M:%S"))


def atom_dicts(n, order):
    """Exact k-th derivative of phi_n as {alpha: coeff}, k = 0..order; a = pi n^2."""
    a = pi * n * n
    d = {mpf(9) / 2: 2 * pi ** 2 * n ** 4, mpf(5) / 2: -3 * pi * n * n}
    seq = [d]
    for _ in range(order):
        nd = {}
        for al, c in seq[-1].items():
            nd[al] = nd.get(al, mpf(0)) + al * c
            nd[al + 2] = nd.get(al + 2, mpf(0)) - 2 * a * c
        seq.append(nd)
    return seq, a


def eval_atoms(d, a, u):
    e2u = exp(2 * u)
    return sum(c * exp(al * u) for al, c in d.items()) * exp(-a * e2u)


def eval_at0(d, a):
    return sum(d.values()) * exp(-a)


def K_deriv_at0(N, k, tail=False):
    """K_N^{(k)}(0) via finite sum (tail=False) or -sum_{n>N} (tail=True)."""
    rng = range(N + 1, N + 80) if tail else range(1, N + 1)
    tot = mpf(0)
    for n in rng:
        seq, a = atom_dicts(n, k)
        tot += eval_at0(seq[k], a)
    return -tot if tail else tot


P("\ncross-checks:")
mp.dps = 40
# symbolic 4th derivative vs numeric diff at u = 0.5, N = 2
seqs = [atom_dicts(n, 4) for n in [1, 2]]
sym = sum(eval_atoms(seq[4], a, mpf("0.5")) for seq, a in seqs)
num = mp.diff(lambda u: sum(eval_atoms(seq[0], a, u) for seq, a in seqs), mpf("0.5"), 4)
P(f"  K_2''''(0.5): symbolic = {mp.nstr(sym, 20)}, numeric diff = {mp.nstr(num, 20)}, "
  f"rel = {mp.nstr(abs(sym-num)/abs(sym), 3)}")
# 4 d_N = J_N
with mp.workdps(140):
    for N in [1, 3, 6, 8]:
        d = K_deriv_at0(N, 1)
        J = sd.J_closed(N)
        P(f"  N={N}: 4 d_N / J_N - 1 = {mp.nstr(4*d/J - 1, 3)}")

P(f"\n{'N':>2} {'d_N':>17} {'K_N\'\'\'(0)':>17} {'tailA/B-1':>10} {'M4_N':>17} {'T_N':>14}")
results = {}
for N in range(1, 9):
    with mp.workdps(140):
        dN = K_deriv_at0(N, 1)
        dN_t = K_deriv_at0(N, 1, tail=True)
        K3 = K_deriv_at0(N, 3)
        K3_t = K_deriv_at0(N, 3, tail=True)
        chk = max(abs(dN_t / dN - 1), abs(K3_t / K3 - 1))
    # M4: sign changes of K'''' on [0, 3], then piecewise integrals
    mp.dps = 40
    seqs = [atom_dicts(n, 4) for n in range(1, N + 1)]
    K4 = lambda u: sum(eval_atoms(seq[4], a, u) for seq, a in seqs)
    U = mpf(3)
    grid = [U * k / 600 for k in range(601)]
    vals = [K4(u) for u in grid]
    brk = [mpf(0)]
    for i in range(600):
        if (vals[i] > 0) != (vals[i + 1] > 0):
            lo, hi = grid[i], grid[i + 1]
            sgn = vals[i] > 0
            for _ in range(60):
                mid = (lo + hi) / 2
                if (K4(mid) > 0) == sgn:
                    lo = mid
                else:
                    hi = mid
            brk.append((lo + hi) / 2)
    brk.append(U)
    M4 = mpf(0)
    for i in range(len(brk) - 1):
        M4 += fabs(quad(lambda u: K4(u) * exp(u / 2), [brk[i], (brk[i]+brk[i+1])/2, brk[i + 1]]))
    with mp.workdps(60):
        T = sqrt((abs(K3) + M4) / dN)
    results[N] = (dN, K3, M4, T)
    P(f"{N:>2} {mp.nstr(dN, 11):>17} {mp.nstr(K3, 11):>17} {mp.nstr(chk, 3):>10} "
      f"{mp.nstr(M4, 11):>17} {mp.nstr(T, 10):>14}  (sign changes of K'''': {len(brk)-2})")

P("\nasymptotic check  Xi_N(x) x^2 / (-4 d_N):")
mp.dps = 60
for N in [1, 2]:
    dN = results[N][0]
    for x in [mpf(400), mpf(800)]:
        v = sd.Xi_sd_real(x, N)
        P(f"  N={N}, x={int(x)}: {mp.nstr(x*x*v/(-4*dN), 12)}")

P("\ns05 done.")
