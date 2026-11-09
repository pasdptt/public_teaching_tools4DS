"""One course-wide seed so that every stochastic result in a lab is reproducible."""
import os
import random

import numpy as np

SEED = 40563107  # the course code


def rng(seed: int = SEED) -> np.random.Generator:
    """Return a NumPy Generator. Pass `rng()` or `SEED` to every function that accepts `random_state`."""
    return np.random.default_rng(seed)


def seed_everything(seed: int = SEED) -> int:
    """Seed Python's `random` and NumPy's legacy global generator (used by some older libraries)."""
    random.seed(seed)
    np.random.seed(seed % 2**32)
    os.environ["PYTHONHASHSEED"] = str(seed)
    return seed
