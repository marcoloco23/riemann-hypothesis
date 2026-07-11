"""Front-law analysis over zeros_N*.json (run after run_front.py N for N=3..8).

Produces (appended to run-output.txt and stdout):
  - master table: #real zeros, R_N, all strip zeros (0 < Im < 0.5) to 12+
    digits, 5 lowest-Im nonreal zeros, min nonreal Im;
  - front-law tests: Re(strip zero) > R_N?  bulk-freeness Re <= 0.9 R_N?
  - tracked near-axis front-zero family (nearest zero to (4.24(N+1)^2, 0.4));
  - least-squares fit Re(front zero) ~ a (N+1)^2 + b with residuals;
  - Im-of-lowest-nonreal-zero trend;
  - coverage statement.
"""
import glob
import json
import os

HERE = "/Users/marcsperzel/code/research/riemann-hypothesis/workspace/scratch/theta-strip/front-law"
lines = []


def say(msg=""):
    print(msg, flush=True)
    lines.append(msg)


def main():
    data = {}
    for fn in sorted(glob.glob(f"{HERE}/zeros_N*.json")):
        with open(fn) as f:
            d = json.load(f)
        bad = [p for p in d["complex_zeros"] if not p["ok"]]
        if bad:
            say(f"WARNING N={d['N']}: {len(bad)} zero(s) failed polish "
                f"verification and are EXCLUDED: "
                + ", ".join(f"{p['re']}+{p['im']}i" for p in bad))
            d["complex_zeros"] = [p for p in d["complex_zeros"] if p["ok"]]
        data[d["N"]] = d
    if not data:
        say("no zeros_N*.json found")
        return
    Ns = sorted(data)
    say("")
    say("#" * 78)
    say("### FRONT-LAW ANALYSIS (theta truncations Xi_N, upper half plane)")
    say(f"### N available: {Ns}")

    # ---------------- master table ----------------
    say("")
    say("MASTER TABLE")
    say(f"{'N':>2} {'#real':>6} {'R_N':>18} {'4(N+1)^2':>9} {'#nonreal':>9} "
        f"{'#strip(0<Im<.5)':>16} {'min nonreal Im':>16}")
    strip_all = []   # (N, re, im)
    for N in Ns:
        d = data[N]
        cz = [(float(p["re"]), float(p["im"]), p) for p in d["complex_zeros"]]
        strips = [(re, im, p) for re, im, p in cz if 0 < im < 0.5]
        minim = min((im for _, im, _ in cz), default=float("nan"))
        say(f"{N:>2} {d['n_real']:>6} {float(d['R_N']):>18.10f} "
            f"{4*(N+1)**2:>9} {len(cz):>9} {len(strips):>16} {minim:>16.10f}")
        for re, im, p in strips:
            strip_all.append((N, re, im, p))
    say("")
    say("ALL STRIP ZEROS (0 < Im < 1/2), 12+ digits:")
    if not strip_all:
        say("  (none)")
    for N, re, im, p in strip_all:
        say(f"  N={N}:  z = {p['re']} + {p['im']} i")
    say("")
    say("5 LOWEST-Im NONREAL ZEROS PER N:")
    for N in Ns:
        d = data[N]
        cz = sorted(((float(p["re"]), float(p["im"])) for p in d["complex_zeros"]),
                    key=lambda t: t[1])
        say(f"  N={N}: " + ";  ".join(f"{re:.6f}+{im:.6f}i" for re, im in cz[:5]))

    # ---------------- front law ----------------
    say("")
    say("FRONT-LAW TEST  (conjecture: every strip zero has Re z > R_N;")
    say("                 bulk-freeness: none with Re z <= 0.9 R_N)")
    violations = 0
    for N, re, im, p in strip_all:
        RN = float(data[N]["R_N"])
        r1 = re / (4 * (N + 1) ** 2)
        r2 = re / RN
        verdict = "PAST FRONT (Re > R_N)" if re > RN else "*** VIOLATION: Re <= R_N ***"
        if re <= 0.9 * RN:
            verdict = "*** BULK STRIP ZERO -- KILLS MOVING-WINDOW PROGRAM ***"
            violations += 1
        elif re <= RN:
            violations += 1
        say(f"  N={N}: Re={re:.6f} Im={im:.6f}  Re/4(N+1)^2={r1:.6f}  "
            f"Re/R_N={r2:.6f}   {verdict}")
    if strip_all and violations == 0:
        say("  => SUPPORTED on all data: strip zeros occur only past the "
            "real-zero front (Re > R_N > 0.9 R_N).")
    elif not strip_all:
        say("  => vacuously supported (no strip zeros found at these N).")
    else:
        say(f"  => {violations} VIOLATION(S) -- SEE ABOVE, REPORT LOUDLY.")

    # ---------------- tracked family ----------------
    say("")
    say("TRACKED NEAR-AXIS FRONT ZERO (seed 4.24(N+1)^2 + 0.4i -> Muller):")
    fam = []
    for N in Ns:
        d = data[N]
        t = d.get("tracked")
        if t and t["ok"]:
            say(f"  N={N}: converged to {t['re']} + {t['im']} i (verified)")
        else:
            say(f"  N={N}: no verified zero from the tracking seed"
                + (f" (Muller wandered to {t['re']}+{t['im']}i, rejected)"
                   if t else ""))
        # nearest enumerated zero (incl. real) to the seed
        seed = (4.24 * (N + 1) ** 2, 0.4)
        cands = [(float(p["re"]), float(p["im"])) for p in d["complex_zeros"]]
        cands += [(float(r), 0.0) for r in d["real_zeros"]]
        if cands:
            best = min(cands, key=lambda c: (c[0]-seed[0])**2 + (c[1]-seed[1])**2)
            say(f"        nearest enumerated zero to seed ({seed[0]:.1f},0.4): "
                f"{best[0]:.10f} + {best[1]:.10f} i")
        # lowest-Im nonreal zero = front-zero proxy for the fit
        cz = [(float(p["re"]), float(p["im"])) for p in d["complex_zeros"]]
        if cz:
            lo = min(cz, key=lambda t: t[1])
            fam.append((N, lo[0], lo[1]))

    # ---------------- fits ----------------
    say("")
    say("FIT Re(lowest-Im nonreal zero) ~ a*(N+1)^2 + b  (least squares):")
    if len(fam) >= 2:
        xs = [(N + 1) ** 2 for N, _, _ in fam]
        ys = [re for _, re, _ in fam]
        n = len(xs)
        sx, sy = sum(xs), sum(ys)
        sxx = sum(x * x for x in xs)
        sxy = sum(x * y for x, y in zip(xs, ys))
        a = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        b = (sy - a * sx) / n
        say(f"  a = {a:.8f}   b = {b:.6f}")
        for (N, re, im), x in zip(fam, xs):
            say(f"    N={N}: Re={re:.8f}  fit={a*x+b:.8f}  resid={re-(a*x+b):+.6f}"
                f"   (Im={im:.8f})")
    say("")
    say("Im of lowest nonreal zero vs N:")
    for N, re, im in fam:
        say(f"  N={N}: min nonreal Im = {im:.10f}   at Re = {re:.8f}")

    # strip-zero fit if there are >= 2 strip zeros
    if len(strip_all) >= 2:
        say("")
        say("FIT over STRIP zeros only: Re ~ a*(N+1)^2 + b:")
        xs = [(N + 1) ** 2 for N, _, _, _ in strip_all]
        ys = [re for _, re, _, _ in strip_all]
        n = len(xs)
        sx, sy = sum(xs), sum(ys)
        sxx = sum(x * x for x in xs)
        sxy = sum(x * y for x, y in zip(xs, ys))
        den = n * sxx - sx * sx
        if den != 0:
            a = (n * sxy - sx * sy) / den
            b = (sy - a * sx) / n
            say(f"  a = {a:.8f}   b = {b:.6f}")
            for (N, re, im, _), x in zip(strip_all, xs):
                say(f"    N={N}: Re={re:.8f}  fit={a*x+b:.8f}  "
                    f"resid={re-(a*x+b):+.6f}")

    # ---------------- coverage ----------------
    say("")
    say("COVERAGE:")
    for N in Ns:
        d = data[N]
        yts = sorted({c["ytop"] for c in d["columns"]})
        yss = sorted({c["ys"] for c in d["columns"]})
        say(f"  N={N}: [-0.5, {d['X_N']}] x (0, {min(yts)}] fully enumerated "
            f"(per-column ytop in {yts}, ys in {yss}); "
            f"{d['seconds']:.0f}s, {d['evals']} evals")
    say("Nothing is asserted for Re z > X_N or Im z above the recorded ytop.")

    with open(f"{HERE}/run-output.txt", "a") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
