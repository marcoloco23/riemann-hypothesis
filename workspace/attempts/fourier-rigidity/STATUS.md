# STATUS — fourier-rigidity (quasicrystal program)

**State:** OPEN — Rung 0 DELIVERED 2026-07-12 (`lemmas/L8`): (EF) as crystalline-pair
statement PROVED with exact test class (L8a, + numeric anchor in
`scratch/explicit-formula-check/`); pinning lemma PROVED (L8b — naive class is the
singleton {Z_ζ}: K1's "fake zero set with exact ζ comb" cannot exist, naive (R) ⟺ RH
but vacuous, exactly as the adoption-night analysis predicted); finite-defect rigidity
PROVED (L8c — any (R′)-counterexample must move infinitely many atoms); positive-comb
class 𝒫 and (R′) precisely defined (L8 §6). §C citations ALL PINNED
(bibliography "Fourier quasicrystals" section).

**Precise current blocker (one sentence):** the K1 counterexample hunt for (R′) is now
well-posed (find admissible `w ≥ 0` ≠ ζ's comb at infinitely many n whose unique
multiset is non-real, or prove none exists) but unstarted, and the DH analogue (L8 §7)
plus the Kaczorowski–Perelli degree-1 citation remain to be pinned before the hunt's
exclusion arguments are rigorous.

**Time horizon:** years-to-decades by design; rungs and kill criteria in ROADMAP §D–E.

**Literature reshaping (2026-07-12 pinning pass — details ROADMAP §C):** the 1-D
unit-mass FQ classification is COMPLETE in the literature ([OlevskiiUlanovskii2020] +
[AlonCohenVinzant2024]: all ℕ-valued FQs on ℝ come from Lee–Yang data) — Rung 4's
converse question is answered for finite-frequency systems; but ζ's pair is provably
OUTSIDE that class ([KurasovSarnak2020]: Guinand's measure is not an FQ even under
RH). Rung 4's real target is now sharp: extend the Lee–Yang classification to
infinite frequency sets with an explicit smooth background ("FQ modulo smooth
background"). Rung 1 absorption list: [KurasovSarnak2020] (reprove 1-variable),
[OlevskiiUlanovskii2020]+[AlonCohenVinzant2024] (the classification pair),
[Goncalves2026] (de Branges framing — likely the right language for the background),
[LevOlevskii2015] Thm 1 (reprove; extract exactly why u.d. is load-bearing).

**Depends on:** L5 (theta representation); L8 (NEW — the program's foundation);
pick-kernel §5b (moment form of the wall); front-law campaign data (Rung 2 raw
material).

**Honest assessment:** unchanged — (R′) is Grand-RH-hard; the bet is on the toolkit
trajectory. Rung 0 cost one session and produced two unconditional theorems (L8b,
L8c) that make the program falsifiable in a concrete direction. The cheap kill test
(K1 hunt) is next; if a positive-comb non-real system exists, the program refocuses
on ζ-local Rung 3 immediately.

**Next actions:**
1. K1 hunt, first probes (ROADMAP §E-K1 resolution block): (a) prove the
   conductor/W_∞ exclusion of DH-type combinations from 𝒫; (b) pin
   Kaczorowski–Perelli degree-1 classification; (c) attempt a constructive w ≥ 0
   perturbation at infinitely many n (what does the unique-multiset machinery say —
   does ANY w ≠ ζ's give a legal system at all? plausibly (S2)'s density already
   forces `Σw_n`-asymptotics = PNT-shape; make that a lemma — it would say members of
   𝒫 satisfy a PNT).
2. L8 hostile re-read (L8b Step C especially) — docs/07 Stage 4.
3. DH analogue L8 §7: pin FE constants from [DavenportHeilbronn1936]/[Spira1968]/
   [BombieriHejhal1995], upgrade SHAPE → PROVED.
4. Rung 2 start: defect-confinement note recasting the front-law campaign in
   program language.
5. Rung 1 absorption (reading list above), starting with [Goncalves2026].
