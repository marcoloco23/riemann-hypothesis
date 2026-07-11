# Attempt: laguerre-phase-space

**Approach family (docs/05):** de Bruijn–Newman deformation (docs/03 §12) crossed with
Laguerre–Pólya class theory; the recurring positivity crux (docs/05 cross-cutting) in
phase-space coordinates.

**The idea (one paragraph).** RH ⟺ `Ξ ∈ LP` (Laguerre–Pólya) ⟺ the generalized Laguerre
quantities `L_n[Ξ](x) ≥ 0` for all `n ≥ 0, x ∈ ℝ` (Csordas–Varga circle; cite pending) ⟺
a single scalar inequality over the plane: `|Ξ'(z)|² ≥ Re(Ξ(z)·conj(Ξ''(z)))` for all
`z ∈ ℂ` (complex Laguerre inequality). Under the heat flow `H_t` (de Bruijn–Newman), the
`L_n` satisfy an **exact hierarchy** `∂_t L_n = −½∂_x²L_n + (n+1)(2n+1)L_{n+1}`, which
sums to an **ultrahyperbolic** PDE `∂_t G = −½∂_x²G + ½∂_y²G` for `G_t = |H_t(x+iy)|²` —
the structural explanation for why maximum-principle arguments fail here. The live
target: a phase-space (Wigner-type) representation writes the master quantity as
`C(x,y) = ½∫₀^∞ p² cosh(py) W(p,x) dp` with `W` the Wigner transform of the theta
kernel; RH becomes **nonnegativity of hyperbolic-weighted moments of `W`** — `W` itself
may go negative, only its `cosh`-moments must not. **New input:** the inequality lives at
`t = 0` directly (no unstable backward flow), is one explicit integral inequality with
every component in closed form, and admits an atom decomposition `W = Σ_{m,n} W_{m,n}`
over theta atoms where modularity and the integer lattice enter *before* oscillatory
cancellation.

**What would close it.** A blockwise positivity theorem for theta-atom packets:
`∫p²cosh(py)(W_{n,n} + W_{m,m} + 2W_{m,n})dp ≥ 0` after suitable arithmetic grouping,
summable absolutely.

**Also recorded here (dead ends, from notes.md):** the raw block-energy/collision route
for the backward heat flow fails *exactly* (the environment term equals the dissipation
term already in the clock configuration — it is not a perturbation), and backward
evolution amplifies alternating perturbations by `exp(τπ²/Δ²)` — faster than any power
of height — so zero-counting inputs can never control it. See PROOF.md §5.

**Origin.** notes.md (2026-07-11); mapping in `workspace/scratch/notes-triage.md`.
