# Reproducibility

## Supported quick check

Use Python 3.13 or newer in a fresh virtual environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --requirement requirements-ci.txt
python scripts/audit_repo.py --current-only
python scripts/verify.py --quick
```

The quick suite compiles all repository Python sources, validates local Markdown links,
and runs the deterministic Davenport-Heilbronn and resolvent calibration. It is the
required pull-request check and runs in GitHub Actions.

## Explicit-formula regression suite

```sh
python scripts/verify.py --explicit-formula
```

This slower suite recomputes zeta zeros and numerical integrals. It exercises the
Riemann-Weil normalization, the L8 hostile-review diagnostics, the smooth compact test,
and the Davenport-Heilbronn calibration. Selected reference output is stored in
[`workspace/scratch/explicit-formula-check/`](workspace/scratch/explicit-formula-check/).

These regressions are motivational numerical checks. They do not certify the omitted
infinite tails and are not part of a proof of RH.

## Older experiments

Each scratch directory has its own README, dependency pins, and recorded output. Follow
that directory's instructions rather than assuming the root CI environment is suitable.
In particular, older experiments currently use either `mpmath==1.3.0` or
`mpmath==1.4.1`; those environments are intentionally kept separate.

Generated virtual environments, bytecode, logs, and large scratch data are ignored by
Git. Do not commit them. Commit small reference outputs only when they are needed to
audit a published claim.

## Releasing a snapshot

Before tagging a release:

1. run `python scripts/audit_repo.py` to scan the current tree and Git history for
   common secret formats;
2. run `python scripts/verify.py --quick` and the suites affected by the release;
3. check that [`CLAIMS.md`](CLAIMS.md) and [`workspace/PROGRESS.md`](workspace/PROGRESS.md)
   agree;
4. record exact commands, versions, outputs, limitations, and machine assistance in
   the release notes;
5. tag the reviewed commit and archive the GitHub release with Zenodo when available.
