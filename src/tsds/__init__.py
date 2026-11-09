"""Course helpers for 040563107 Tools for Statistical Data Science.

Import in the first cell of every lab:

    import tsds
    tsds.env.check()        # print versions; warn if outside the CI-tested ranges
    rng = tsds.rng()        # NumPy Generator seeded with the course seed
    X, y = tsds.data.load("wine")
"""
from . import data, env
from .seed import SEED, rng, seed_everything

__all__ = ["SEED", "rng", "seed_everything", "data", "env"]
__version__ = "0.1.0"
