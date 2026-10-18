"""Run from any working directory; no installation or network required."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if sys.version_info < (3, 10):
    raise SystemExit("Python 3.10 or newer is required.")

print(f"Python {sys.version.split()[0]} | {ROOT}", flush=True)
raise SystemExit(subprocess.call(
    [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=ROOT,
))
