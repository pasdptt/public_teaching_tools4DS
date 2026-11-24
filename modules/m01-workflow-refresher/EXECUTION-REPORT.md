# Execution report — module m01 (week 1)

**Date:** 24 November 2026. Every result below comes from running the code **[V]**.

## 1. Environments

The two pinned environments are those of the [m04 execution report](../m04-pca/EXECUTION-REPORT.md#1-environments), with **DuckDB** added for this module:

| Environment | DuckDB | Other pins (unchanged) |
|---|---|---|
| `environment/requirements-local.txt` (pinned local) | 2.0.1 | numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, scikit-learn 1.9.1, Matplotlib 3.11.2 |
| `environment/requirements-colab-proxy.txt` (Colab proxy) | 1.2.2 | numpy 2.2.6, pandas 2.2.3, scipy 1.16.3, scikit-learn 1.6.1, Matplotlib 3.10.9 |

The Colab-proxy DuckDB version is an **assumption** (a 1.x release, as preinstalled in Colab), not a measured Colab snapshot. The lab's DuckDB cell installs DuckDB if a runtime does not have it, so the lab does not depend on the assumption.

## 2. Results

| Check | Pinned local | Colab proxy |
|---|---|---|
| Student notebook: valid, no outputs, badge and setup cell, every task raises `NotImplementedError` | pass | pass |
| Student notebook: given cells run top to bottom with every task and self-check removed | pass | pass |
| Solution notebook (private): runs top to bottom, all 7 self-checks print `OK`, ids match the student notebook | pass | pass |
| Mutation test (private): 9 typical mistakes injected, one at a time | 9/9 caught | 9/9 caught |
| Answer-key numbers (`key_numbers.py`, private) | identical output | identical output |

The Air Quality file is downloaded from UCI and its SHA-256 checksum verified on every fresh run (`tsds.data.load`).

**The nine injected mistakes**, each caught by the self-check of its task: a reordered notebook that still overwrites its input (T1); the population divisor for a sample standard deviation, the arithmetic mean used as a growth rate, and the arithmetic mean of speeds (T2); the −200 sentinel left in the data (T3); missing shares sorted the wrong way (T4); `COUNT(*)` for valid hours (T5); pandas `rolling` without `min_periods` (T6); and the AI's day-of-month grouping kept in the "fix" (T7).

## 3. Numbers quoted in the lecture outline and the lab

| Quantity | Value |
|---|---|
| Air Quality rows after removing empty lines; time span | 9,357 consecutive hours, 2004-03-10 18:00 to 2005-04-04 14:00 (no gaps) |
| Temperatures coded −200 | 366 |
| Mean temperature, raw / recoded | 9.78 °C / 18.32 °C (minimum −200 / −1.9 °C) |
| Missing share after recoding | NMHC 90.2%, CO 18.0%, NO₂ 17.5%, NOₓ 17.5%, other columns 3.9% |
| Calendar days; days without any valid CO | 391; 36 |
| AI answer (`groupby(aq.index.day)`) | 31 values |
| Returns 10%, −5%, 20%, −15%, 8%: arithmetic / geometric mean | 3.60% / 2.86% (total factor 1.1512) |
| Average speed over three 60 km legs at 30, 60, 90 km/h | 49.09 km/h |
| `np.std` / `pd.Series.std` of (52, 61, 70, 85, 47) | 13.5204 / 15.1162 |
| Hidden-state example: orders 0-2-1 / 0-1-2 / 0-2-2-1 | mean 0.63 / `NameError` / mean 0.0063 |

## 4. Limitations

* **Not yet run in a real Colab runtime.** The Colab proxy is an approximation. Before the lab session, open the lab from its badge in Colab and run *Restart session and run all* once.
* The Colab badge points to the `main` branch, so it works once this module is merged into `main`.
* The download needs `archive.ics.uci.edu` to be reachable. If UCI is down during the lab, Part 3 onward cannot run; keep a copy of `air+quality.zip` to share in Microsoft Teams. Students upload it to `~/.cache/tsds/` in their runtime (or to the folder named by the environment variable `TSDS_DATA`); the loader uses that copy only if its SHA-256 checksum matches.
