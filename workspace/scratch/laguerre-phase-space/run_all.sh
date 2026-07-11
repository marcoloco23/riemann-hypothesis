#!/bin/sh
# Deterministic full run; output captured in run-output.txt.
set -e
cd "$(dirname "$0")"
{
  echo "run_all.sh -- $(./venv/bin/python -c 'import sys,mpmath,sympy;print(f"python {sys.version.split()[0]}, mpmath {mpmath.__version__}, sympy {sympy.__version__}")')"
  ./venv/bin/python claim1.py
  echo
  ./venv/bin/python claim2.py
  echo
  ./venv/bin/python claim3.py
  echo
  ./venv/bin/python claim4.py
  echo
  ./venv/bin/python claim5.py
  echo
  ./venv/bin/python crosscheck.py
} 2>&1 | tee run-output.txt
