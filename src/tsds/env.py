"""Environment check printed at the top of every lab.

The ranges below are the package versions the course notebooks are tested against in CI
(see environment/). A version outside a range is not necessarily broken, but results and
APIs are not guaranteed: report the printed table if something fails.
"""
import platform
import sys
import warnings
from importlib import metadata

# minimum inclusive, maximum exclusive (major.minor)
TESTED = {
    "numpy": ("2.2", "2.6"),
    "pandas": ("2.2", "3.2"),
    "scipy": ("1.14", "1.19"),
    "scikit-learn": ("1.6", "1.10"),
    "matplotlib": ("3.10", "3.12"),
}


def _mm(v: str) -> tuple:
    parts = []
    for p in v.split(".")[:2]:
        digits = "".join(ch for ch in p if ch.isdigit())
        parts.append(int(digits) if digits else 0)
    return tuple(parts)


def in_colab() -> bool:
    return "google.colab" in sys.modules or "COLAB_RELEASE_TAG" in __import__("os").environ


def check(verbose: bool = True) -> dict:
    """Print Python and package versions; warn for packages outside the tested ranges."""
    info = {"python": platform.python_version(), "runtime": "Google Colab" if in_colab() else "local"}
    outside = []
    for pkg, (lo, hi) in TESTED.items():
        try:
            v = metadata.version(pkg)
        except metadata.PackageNotFoundError:
            v = "not installed"
            outside.append(pkg)
        else:
            if not (_mm(lo) <= _mm(v) < _mm(hi)):
                outside.append(pkg)
        info[pkg] = v
    if verbose:
        print(f"Runtime: {info['runtime']} | Python {info['python']}")
        for pkg in TESTED:
            flag = "  <-- outside tested range" if pkg in outside else ""
            print(f"  {pkg:<13} {info[pkg]:<14} tested {TESTED[pkg][0]} to <{TESTED[pkg][1]}{flag}")
    if outside:
        warnings.warn(f"Untested package versions: {outside}. The lab may still work; if it fails, report this table.",
                      stacklevel=2)
    info["outside_tested_range"] = outside
    return info
