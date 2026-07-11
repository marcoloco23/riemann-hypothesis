"""Front-law study, per-N driver.

Usage: run_front.py N

Enumerates ALL zeros of Xi_N in [0, X_N] x (0, ~12], X_N = 6(N+1)^2 + 100:
  1. real-zero scan on the axis (step 0.2 bulk / 0.05 front window) + polish
     + reality check (findroot from x + 0.01i must return to the axis);
  2. per ~10-wide column [x0,x1] (edges shifted >= 0.4 away from real zeros):
       C_sym  = winding count on [x0,x1] x [-ys, +ys]   (ys ~ 0.5)
       C_high = winding count on [x0,x1] x [ ys, ~12  ]
     By conjugate symmetry C_sym = nr + 2*n_low with nr = #real zeros in the
     column and n_low = #zeros with 0 < Im < ys (a zero exactly on the
     imaginary axis would make C_sym - nr odd; that case is flagged and
     resolved by a direct upper-half count).  When n_low > 0 a near-real box
     [x0,x1] x [-ylo, ylo] (ylo = 0.011, then 0.0005) certifies no zeros with
     0 < Im <= ylo and pins the enumeration window; the axis is also rescanned
     at step 0.01 if the near-real count disagrees with nr (missed real pair).
     Nonzero counts are located by count-guided bisection (fl_common.isolate),
     deduplicated at 1e-6, and polished at dps ~ floor_digits + 70.
  3. front fine scan: [R_N - 10, R_N + 40] x [0.011, 0.5] in 5-wide boxes
     (independent recount of the strip window where front zeros live);
  4. tracked front zero: Muller from seed 4.24*(N+1)^2 + 0.4i.

Everything is appended (line-buffered) to run-output.txt and the full result
set is written to zeros_N<N>.json.
"""
import json
import sys
import time

from mpmath import mp, mpf, mpc

import fl_common as fl
from fl_common import (BadContour, Eval, count_box, dedup, isolate,
                       polish_zero, real_scan, reality_check)
import xi_common as xc

HERE = "/Users/marcsperzel/code/research/riemann-hypothesis/workspace/scratch/theta-strip/front-law"
RUNOUT = HERE + "/run-output.txt"

_logf = None   # per-N progress file (survives crashes)
_lines = []    # accumulated; appended to run-output.txt in one write at the end


def init_log(N):
    global _logf
    _logf = open(f"{HERE}/out_N{N}.txt", "a", buffering=1)


def say(msg=""):
    print(msg, flush=True)
    _logf.write(msg + "\n")
    _lines.append(msg)


def flush_runout():
    with open(RUNOUT, "a") as f:
        f.write("\n".join(_lines) + "\n")


def build_edges(X, rz):
    """Column edges ~10 apart, each >= 0.4 from every real zero."""
    edges = [mpf('-0.5')]
    x = mpf(10)
    while x < X - 5:
        e = x
        while any(abs(e - r) < mpf('0.4') for r in rz):
            e += mpf('0.13')
        edges.append(e)
        x += 10
    edges.append(mpf(X))
    return edges


def sym_count(ev, x0, x1):
    """Symmetric-box count with edge shifting; returns (count, ys_used)."""
    last = None
    for ys in (mpf('0.5'), mpf('0.469'), mpf('0.531'), mpf('0.437'), mpf('0.563')):
        try:
            return count_box(ev, x0, x1, -ys, ys), ys
        except BadContour as e:
            last = e
    raise last


def high_count(ev, x0, x1, ys):
    """Upper-box count [ys, ytop] with top-edge shifting; returns (count, ytop)."""
    last = None
    for yt in (mpf('12.001'), mpf('12.043'), mpf('11.957'), mpf('12.101')):
        try:
            return count_box(ev, x0, x1, ys, yt, max_step=mpf('0.5')), yt
        except BadContour as e:
            last = e
    raise last


def resolve_low(ev, N, x0, x1, nr, ys, csym, rz):
    """Locate the (csym - nr)/2 zeros with 0 < Im < ys in the column.
    Returns (roots, notes)."""
    notes = []
    n2 = csym - nr
    if n2 == 0:
        return [], notes
    say(f"    LOUD: column [{mp.nstr(x0,8)},{mp.nstr(x1,8)}] has C_sym={csym} "
        f"vs {nr} real zeros -> {n2} nonreal zero(s) with |Im|<{mp.nstr(ys,4)}")
    if n2 < 0:
        notes.append(f"NEGATIVE excess {n2}: impossible; real scan overcounted?")
        say("    !! " + notes[-1])
        return [], notes
    # near-real certification, shrinking ylo until the extra zeros are above it
    for ylo in (mpf('0.011'), mpf('0.0005')):
        try:
            nrb = count_box(ev, x0, x1, -ylo, ylo)
        except BadContour as e:
            notes.append(f"near-real box ylo={float(ylo)} failed: {e}")
            say("    !! " + notes[-1])
            continue
        if nrb == nr:
            notes.append(f"near-real box [{float(ylo)}]: count {nrb} == nr {nr}; "
                         f"no zeros with 0 < Im <= {float(ylo)}")
            say("    " + notes[-1])
            k = n2 // 2
            if n2 % 2 == 1:
                notes.append("ODD excess -> possible imaginary-axis zero; "
                             "direct upper-half count used")
                say("    !! " + notes[-1])
                k = count_box(ev, x0, x1, ylo, ys)
            roots = isolate(ev, N, x0, x1, ylo, ys, k, log=say)
            return roots, notes
        notes.append(f"near-real box [{float(ylo)}]: count {nrb} != nr {nr} "
                     f"-> zeros below {float(ylo)} or missed real zeros")
        say("    !! " + notes[-1])
    # disambiguate: rescan axis finely
    extra_real = []
    x = x0
    evr = Eval(N, real=True)
    vprev = evr(x)[0]
    while x < x1:
        xn = x + mpf('0.01')
        vnext = evr(xn)[0]
        if vprev * vnext < 0:
            extra_real.append((x + xn) / 2)
        x, vprev = xn, vnext
    known = [r for r in rz if x0 < r < x1]
    missed = [m for m in extra_real
              if all(abs(m - r) > mpf('0.02') for r in known)]
    notes.append(f"fine axis rescan: {len(extra_real)} sign changes, "
                 f"{len(missed)} not in the real-zero list: "
                 + ", ".join(mp.nstr(m, 10) for m in missed))
    say("    !! " + notes[-1])
    # last resort: enumerate the upper half directly from a tiny offset
    k = count_box(ev, x0, x1, mpf('0.00002'), ys)
    roots = isolate(ev, N, x0, x1, mpf('0.00002'), ys, k, log=say)
    return roots, notes


def main():
    N = int(sys.argv[1])
    init_log(N)
    X = 6 * (N + 1) ** 2 + 100
    t0 = time.time()
    say("")
    say("=" * 78)
    say(f"### N = {N}: rectangle [0, {X}] x (0, ~12]   "
        f"(cap dps {fl.cap_dps(N)}, polish dps {fl.polish_dps(N)})")
    say(f"### started {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # ---- 1. real zeros ----
    t = time.time()
    rz, evr = real_scan(N, X, log=say)
    maxim = reality_check(N, rz, log=say)
    R_N = rz[-1] if rz else None
    say(f"[N={N}] real zeros: {len(rz)} in (0,{X}];  R_{N} = {mp.nstr(R_N, 15)};"
        f"  4(N+1)^2 = {4*(N+1)**2};  R_N/4(N+1)^2 = {mp.nstr(R_N/(4*(N+1)**2), 8)}")
    say(f"[N={N}] reality check: max |Im| after polish from x+0.01i = "
        f"{mp.nstr(maxim, 3)}  ({len(rz)} zeros, {evr.evals} axis evals, "
        f"{time.time()-t:.0f}s)")

    # ---- 2. columns ----
    ev = Eval(N)
    edges = build_edges(X, rz)
    columns = []
    complex_roots = []
    say(f"[N={N}] columns: {len(edges)-1} (edges shifted off real zeros)")
    for x0, x1 in zip(edges[:-1], edges[1:]):
        t = time.time()
        nr = sum(1 for r in rz if x0 < r < x1)
        csym, ys = sym_count(ev, x0, x1)
        chigh, yt = high_count(ev, x0, x1, ys)
        col = {"x0": float(x0), "x1": float(x1), "nr": nr, "C_sym": csym,
               "ys": float(ys), "C_high": chigh, "ytop": float(yt),
               "n_low": (csym - nr) / 2, "notes": []}
        low_roots = []
        if csym != nr:
            low_roots, notes = resolve_low(ev, N, x0, x1, nr, ys, csym, rz)
            col["notes"] += notes
        high_roots = []
        if chigh > 0:
            high_roots = isolate(ev, N, x0, x1, ys, yt, chigh, log=say)
        loc = low_roots + high_roots
        if len(low_roots) * 2 + (0 if (csym - nr) % 2 == 0 else 1) < csym - nr:
            col["notes"].append(f"LOCATED {len(low_roots)} low vs expected "
                                f"{(csym-nr)//2}")
        complex_roots += loc
        flag = ""
        if csym != nr:
            flag = "  <== NONREAL BELOW 0.5"
        elif chigh > 0:
            flag = f"  ({chigh} upper zeros)"
        say(f"  col [{float(x0):9.2f},{float(x1):9.2f}]: nr={nr:3d}  "
            f"C_sym={csym:3d} (ys={float(ys):.3f})  C_high={chigh:3d} "
            f"(top={float(yt):.3f})  located={len(loc)}  "
            f"[{time.time()-t:.0f}s, {ev.evals} evals total]{flag}")
        columns.append(col)

    # dedup + polish
    complex_roots = dedup(complex_roots)
    polished = []
    for r in complex_roots:
        rp, ok, res, locv = polish_zero(N, r, log=say)
        polished.append({"re": mp.nstr(rp.real, 20), "im": mp.nstr(rp.imag, 20),
                         "ok": ok, "residual": mp.nstr(res, 3),
                         "local": mp.nstr(locv, 3)})
    total_c = sum((c["C_sym"] - c["nr"]) // 2 + c["C_high"] for c in columns)
    say(f"[N={N}] complex zeros (Im>0) located: {len(polished)}; "
        f"argument-principle total: {total_c}  "
        f"[{'MATCH' if len(polished) == total_c else 'MISMATCH -- INVESTIGATE'}]")
    for p in sorted(polished, key=lambda p: float(p["im"])):
        tag = " <== STRIP ZERO (0<Im<0.5)" if 0 < float(p["im"]) < 0.5 else ""
        say(f"    zero: {p['re']} + {p['im']} i   "
            f"(res {p['residual']}, ok={p['ok']}){tag}")

    # ---- 3. front fine scan ----
    say(f"[N={N}] front fine scan [R_N-10, R_N+40] x [0.011, 0.5], "
        f"5-wide boxes:")
    f0, f1 = R_N - 10, R_N + 40
    fs_roots = []
    fs_counts = []
    xa = f0
    while xa < f1 - mpf('0.01'):
        xb = min(xa + 5, f1)
        # shift edges off real zeros
        while any(abs(xa - r) < mpf('0.25') for r in rz):
            xa -= mpf('0.07')
        while any(abs(xb - r) < mpf('0.25') for r in rz):
            xb += mpf('0.07')
        nr = sum(1 for r in rz if xa < r < xb)
        try:
            nrb = count_box(ev, xa, xb, mpf('-0.011'), mpf('0.011'))
            cst = count_box(ev, xa, xb, mpf('0.011'), mpf('0.5'))
        except BadContour as e:
            say(f"    !! front box [{mp.nstr(xa,8)},{mp.nstr(xb,8)}] failed: {e}")
            xa = xb
            continue
        fs_counts.append({"x0": float(xa), "x1": float(xb), "nr": nr,
                          "near_real": nrb, "strip": cst})
        note = "" if nrb == nr else "  !! near-real mismatch"
        say(f"    front box [{float(xa):8.2f},{float(xb):8.2f}]: near-real "
            f"{nrb} (nr={nr}){note}; strip count = {cst}"
            + ("  <== STRIP ZERO(S)" if cst else ""))
        if cst > 0:
            fs_roots += isolate(ev, N, xa, xb, mpf('0.011'), mpf('0.5'), cst,
                                log=say)
        xa = xb
    fs_roots = dedup(fs_roots)
    say(f"[N={N}] front fine scan strip zeros: "
        + (", ".join(mp.nstr(r, 15) for r in fs_roots) if fs_roots else "none"))

    # ---- 4. tracked front zero ----
    seed = mpc(mpf('4.24') * (N + 1) ** 2, mpf('0.4'))
    tracked = None
    for off in (mpc(0), mpc(mpf('1.5'), 0), mpc(mpf('-1.5'), 0),
                mpc(0, mpf('0.15'))):
        try:
            r = fl._findroot_muller(N, seed + off, mpf('0.05'),
                                    min(fl.pred_dps(N, seed.real) + 30,
                                        fl.cap_dps(N) + 25),
                                    fl.pred_dps(N, seed.real) + 15)
            rp, ok, res, locv = polish_zero(N, r, log=say)
            say(f"[N={N}] tracked zero from seed {mp.nstr(seed + off, 8)}: "
                f"converged to {mp.nstr(rp, 18)} (ok={ok})")
            if ok:
                tracked = {"re": mp.nstr(rp.real, 20), "im": mp.nstr(rp.imag, 20),
                           "ok": ok}
                break
        except Exception as e:
            say(f"[N={N}] tracked-zero findroot failed from offset "
                f"{mp.nstr(off, 4)}: {type(e).__name__} {e}")

    out = {
        "N": N, "X_N": X, "R_N": mp.nstr(R_N, 25),
        "n_real": len(rz),
        "real_zeros": [mp.nstr(r, 25) for r in rz],
        "reality_max_im": mp.nstr(maxim, 3),
        "columns": columns,
        "complex_zeros": polished,
        "front_scan_boxes": fs_counts,
        "front_scan_zeros": [[mp.nstr(r.real, 20), mp.nstr(r.imag, 20)]
                             for r in fs_roots],
        "tracked": tracked,
        "coverage": f"all zeros in [-0.5,{X}] x (0, ytop~12.0]; per-column ytop "
                    f"recorded; symmetric boxes certify counts for |Im|<ys",
        "seconds": round(time.time() - t0, 1),
        "evals": ev.evals + evr.evals,
    }
    with open(f"{HERE}/zeros_N{N}.json", "w") as f:
        json.dump(out, f, indent=1)
    say(f"[N={N}] DONE in {time.time()-t0:.0f}s; wrote zeros_N{N}.json")
    flush_runout()


if __name__ == "__main__":
    main()
