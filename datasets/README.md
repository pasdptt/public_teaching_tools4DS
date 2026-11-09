# Datasets

The dataset registry lives in [`src/tsds/registry.yaml`](../src/tsds/registry.yaml), so that the `tsds` helper package and the documentation share one source. Every entry records the source, DOI, creators, licence, how and when the licence was verified, and a citation. Downloaded files also record a SHA-256 checksum, and the loader refuses a file whose checksum does not match.

| Name | Licence | Delivery |
|---|---|---|
| `iris` | CC BY 4.0 (UCI 53) | bundled with scikit-learn |
| `wine` | CC BY 4.0 (UCI 109) | bundled with scikit-learn |
| `digits` | CC BY 4.0 (UCI 80) | bundled with scikit-learn |
| `air_quality` | CC BY 4.0 (UCI 360) | downloaded from UCI, SHA-256 verified |

Data files are not committed to this repository. Required work never needs a Google Drive mount or a Kaggle token.
