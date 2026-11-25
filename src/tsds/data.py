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


def _load_rda(entry: dict) -> pd.DataFrame:
    """An R data file (.rda) holding one data frame, read with the pure-Python `rdata` package.

    Parsing takes about 20 s for the flights file, so the parsed frame is cached next to the
    download, keyed by the file's SHA-256 and the pandas version (a changed source file or pandas never
    reuses an old cache)."""
    parsed = cache_dir() / f"{entry['sha256'][:16]}-pandas{pd.__version__}.pkl"
    if parsed.exists():
        try:
            return pd.read_pickle(parsed)
        except Exception:  # unreadable cache: parse the download again
            parsed.unlink()
    data = _download(entry)
    import warnings
    import rdata
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # rdata warns about R classes (tibble, POSIXct) it maps to plain columns
        path = cache_dir() / Path(entry["url"]).name
        df = rdata.read_rda(str(path))[entry["object"]]
    df = df.reset_index(drop=True)
    df.columns = [str(c) for c in df.columns]
    for col in df.columns:
        if str(df[col].dtype).startswith(("string", "str")):
            df[col] = df[col].astype(object)
    df.to_pickle(parsed)
    return df


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
    if entry["kind"] == "url_rda":
        return _load_rda(entry)
    raise ValueError(f"Unsupported dataset kind {entry['kind']!r}")
