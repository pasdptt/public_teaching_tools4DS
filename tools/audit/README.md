# Audit harness

These scripts produced the results in [`docs/audit/02-execution-report.md`](../../docs/audit/02-execution-report.md).

| File | Purpose |
|---|---|
| `runnb.py` | Executes a notebook top to bottom in a fresh kernel and records per-cell errors in `<out>.report.json`. Usage: `runnb.py <in.ipynb> <out.ipynb> <working-dir> <mode-label>`. Shell lines (`!…`, `%pip`, `%%bash`) are replaced by logged no-ops. The kernel name comes from `AUDIT_KERNEL` (default `audit312`). |
| `colabstub/` | A minimal `google.colab.drive` stub (namespace package) for Colab-simulated runs. Put it on `PYTHONPATH`. |
| `compare.py` | Compares stored text outputs of an original notebook with a re-executed copy. |
| `checks.py` | Targeted checks C1–C8 that confirm individual audit findings. Takes a data directory. |
| `nb_summary.py` | Prints a compact, images-stripped view of a notebook's cells and outputs for review. |

The audited notebooks and data files belong to the course lecturer and are not part of this public repository.
