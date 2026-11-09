"""Licensed, checksum-verified dataset loading.

    tsds.data.list_datasets()          # names in the registry
    tsds.data.info("wine")             # licence, citation, notes
    X, y = tsds.data.load("wine")      # bundled datasets -> (DataFrame, Series)
    df = tsds.data.load("air_quality") # downloaded datasets -> DataFrame (raw, sentinels kept)

No Google Drive mount and no Kaggle token is ever needed.
"""
import hashlib
import io
import os
import urllib.request
import zipfile
from importlib import resources
from pathlib import Path

import pandas as pd
import yaml

_REGISTRY = None


def registry() -> dict:
    global _REGISTRY
    if _REGISTRY is None:
        _REGISTRY = yaml.safe_load(resources.files("tsds").joinpath("registry.yaml").read_text(encoding="utf-8"))
    return _REGISTRY


def list_datasets() -> list:
    return sorted(registry())


def info(name: str) -> dict:
    entry = _entry(name)
    print(f"{entry['title']} | licence: {entry['licence']} | {entry['citation']}")
    return entry


def cache_dir() -> Path:
    d = Path(os.environ.get("TSDS_DATA", Path.home() / ".cache" / "tsds"))
    d.mkdir(parents=True, exist_ok=True)
    return d


def _entry(name: str) -> dict:
    try:
        return registry()[name]
    except KeyError:
        raise KeyError(f"Unknown dataset {name!r}. Available: {list_datasets()}") from None


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _download(entry: dict) -> bytes:
    path = cache_dir() / Path(entry["url"]).name
    if path.exists():
        data = path.read_bytes()
        if _sha256(data) == entry["sha256"]:
            return data
        path.unlink()  # corrupted or changed cache: fetch again
    req = urllib.request.Request(entry["url"], headers={"User-Agent": "tsds-course"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    digest = _sha256(data)
    if digest != entry["sha256"]:
        raise ValueError(f"Checksum mismatch for {entry['url']}: got {digest}, expected {entry['sha256']}. "
                         "The source file has changed; do not use it until the registry is updated.")
    path.write_bytes(data)
    return data


def load(name: str):
    """Load a registry dataset. Bundled datasets return (X, y); downloaded ones return a DataFrame."""
    entry = _entry(name)
    if entry["kind"] == "sklearn":
        import sklearn.datasets as skd
        bunch = getattr(skd, entry["loader"])(as_frame=True)
        X = bunch.data.copy()
        y = bunch.target.copy()
        if hasattr(bunch, "target_names"):
            y = pd.Series(pd.Categorical.from_codes(y, list(map(str, bunch.target_names))), name="target") \
                if name != "digits" else y.rename("digit")
        return X, y
    if entry["kind"] == "url_zip_csv":
        data = _download(entry)
        with zipfile.ZipFile(io.BytesIO(data)) as z, z.open(entry["member"]) as f:
            return pd.read_csv(f, **entry.get("read_csv", {}))
    raise ValueError(f"Unsupported dataset kind {entry['kind']!r}")
