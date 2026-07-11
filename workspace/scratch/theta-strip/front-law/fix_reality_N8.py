"""Re-run the reality check for N=8 with the fixed x-appropriate precision
(fl_common.reality_check now uses dd = pred_dps(N,x)+30 instead of the full
polish precision, whose overtight step tolerance made Muller iterates collide
at the working ulp for small-x zeros).  Updates zeros_N8.json in place and
logs to out_N8.txt / run-output not needed (analyze reads the JSON)."""
import json

from mpmath import mp, mpf

from fl_common import reality_check

HERE = "/Users/marcsperzel/code/research/riemann-hypothesis/workspace/scratch/theta-strip/front-law"

with open(f"{HERE}/zeros_N8.json") as f:
    d = json.load(f)
zeros = [mpf(s) for s in d["real_zeros"]]
msgs = []
maxim = reality_check(8, zeros, log=msgs.append)
for m in msgs:
    print(m)
print(f"[N=8] reality check (fixed): max |Im| after polish from x+0.01i = "
      f"{mp.nstr(maxim, 3)} over {len(zeros)} zeros")
d["reality_max_im"] = mp.nstr(maxim, 3)
d["reality_note"] = ("recomputed with x-appropriate Muller precision after "
                     "ulp-collision failures at small x in the main run; "
                     "see fix_reality_N8.py")
with open(f"{HERE}/zeros_N8.json", "w") as f:
    json.dump(d, f, indent=1)
with open(f"{HERE}/out_N8.txt", "a") as f:
    f.write(f"[N=8] reality check (fixed rerun): max |Im| = {mp.nstr(maxim, 3)}\n")
