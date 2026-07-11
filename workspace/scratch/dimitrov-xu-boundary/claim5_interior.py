"""Claim 5: interior-line behavior.
(a) R(t, delta) = Re[xi xi'' - xi'^2](sigma + it), sigma = 1 - delta,
    delta in {0.05, 0.1, 0.2}, t in [100, 120] step 0.5, dps 130.
    Question: does the delta=0 sign change (t ~ 110.46-111.48) persist?
    Expected NO (persistence would contradict RH per the notes' reading of
    Dimitrov-Xu, and would then almost certainly be a numerical artifact).
    Any negative value found is re-verified at dps 200.
(b) U(0, y) = Re L(iy) = [xi xi'' - xi'^2](sigma) at sigma = 1/2 + y (real),
    y in {0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.49}: report signs.
"""
import mpmath as mp
import common as C


def R(t, delta):
    return mp.re(C.wronskian_s(mp.mpc(1 - delta, t)))


def main():
    print("=== (a) R(t, delta) on t in [100,120], step 0.5, dps 130 ===")
    for dstr in ['0.05', '0.1', '0.2']:
        mp.mp.dps = 130
        delta = mp.mpf(dstr)
        neg = []
        minval, mint = mp.inf, None
        rows = []
        t = mp.mpf(100)
        while t <= 120:
            v = R(t, delta)
            s = mp.mpc(1 - delta, t)
            norm = v / abs(C.xi(s)) ** 2
            rows.append((t, v, norm))
            if norm < minval:
                minval, mint = norm, t
            if v < 0:
                neg.append((t, v))
            t += mp.mpf('0.5')
        print(f"\n-- delta = {dstr} (sigma = {mp.nstr(1-delta,4)}):")
        print(f"   negative points: {[(mp.nstr(a,6), mp.nstr(b,6)) for a, b in neg] or 'NONE'}")
        print(f"   min normalized R/|xi|^2 = {mp.nstr(minval, 8)} at t = {mp.nstr(mint, 6)}")
        for t, v, norm in rows[::8]:
            print(f"     t={mp.nstr(t,6):>7}  R={mp.nstr(v,8):>16}  R/|xi|^2={mp.nstr(norm,8):>14}")
        if neg:
            print("   !!! negatives found on interior line -- recheck at dps 200:")
            mp.mp.dps = 200
            for t, _ in neg:
                print(f"     dps200: R({mp.nstr(t,6)}, {dstr}) = {mp.nstr(R(t, delta), 10)}")

    print("\n=== (a2) finer: does the dip shrink continuously? min of R/|xi|^2 near t~111 ===")
    mp.mp.dps = 100
    for dstr in ['0', '0.01', '0.02', '0.05', '0.1']:
        delta = mp.mpf(dstr)
        best, bt = mp.inf, None
        t = mp.mpf(109)
        while t <= 113:
            v = R(t, delta) / abs(C.xi(mp.mpc(1 - delta, t))) ** 2
            if v < best:
                best, bt = v, t
            t += mp.mpf('0.125')
        print(f"   delta={dstr:>5}: min R/|xi|^2 on [109,113] = {mp.nstr(best, 8)} at t={mp.nstr(bt,6)}")

    print("\n=== (b) U(0,y) = [xi xi'' - xi'^2](1/2 + y), real axis, dps 60 ===")
    mp.mp.dps = 60
    for ystr in ['0', '0.1', '0.2', '0.3', '0.4', '0.45', '0.49']:
        sigma = mp.mpf(1) / 2 + mp.mpf(ystr)
        v = C.wronskian_s(sigma)
        print(f"   y={ystr:>5} (sigma={mp.nstr(sigma,4)}): U = {mp.nstr(mp.re(v), 12)}"
              f"   sign: {'+' if mp.re(v) > 0 else '-'}   (imag part {mp.nstr(mp.im(v),3)})")


if __name__ == '__main__':
    main()
