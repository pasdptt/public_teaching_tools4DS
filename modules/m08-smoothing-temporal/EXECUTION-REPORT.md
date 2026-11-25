# Execution report — module m08

**Date:** 25 November 2026. Every result below comes from running the code **[V]**.

## 1. Environments

The two pinned environments of the [m04 execution report](../m04-pca/EXECUTION-REPORT.md#1-environments), with `statsmodels` added to both pins: 0.15.0 locally and 0.14.6 in the Colab proxy (the proxy pin assumes Colab's 0.14 series).

## 2. Results

| Check | Pinned local | Colab proxy |
|---|---|---|
| Student notebook: valid, no outputs, badge and setup cell, every task raises `NotImplementedError` | pass | pass |
| Student notebook: given cells run top to bottom with every task and self-check removed | pass (2.9 s) | pass (2.3 s) |
| Solution notebook (private): runs top to bottom, all 4 self-checks print `OK`, ids match the student notebook; no warnings printed | pass (5.6 s) | pass (4.8 s) |
| Mutation test (private): 4 typical mistakes injected, one at a time | 4/4 caught | 4/4 caught |
| Auto-checker for G5 (private): solution scores 3/3 and 1/1 (23/23 hidden-test points); each mutant loses correctness on its own task; a blank notebook scores 0 | pass | pass |
| Answer-key numbers (`key_numbers.py`, private) | identical | identical |

**The four injected mistakes:** the −200 sentinel not recoded (T1); the centred window computed as a trailing one (T2); a forecaster that sees the day it forecasts (T3); a "trailing" mean that includes the target day (T4).

## 3. Numbers quoted in the lecture outline and the lab

All identical in both environments, despite the different statsmodels versions.

| Quantity | Value |
|---|---|
| Hourly rows; sentinel hours in temperature | 9,357; 366 |
| EWMA (α = 0.1) of temperature with sentinels: minimum; largest distortion | −199.9 °C; 224.7 °C |
| Gaps after dropping sentinel hours; longest | 16; 3 days 5 hours |
| Benzene: calendar days; below the 18-hour rule; filled inside; dropped at the ends; kept | 391; 20; 18; 2; 389 |
| Benzene: mean (min, max); lag-1 and lag-7 autocorrelation | 10.09 (1.42, 23.84); 0.614, 0.356 |
| Weekday means, Monday to Sunday | 9.9, 11.7, 11.3, 11.5, 11.6, 8.6, 6.1 |
| Kernel bandwidth: leave-one-out choice (MSE); leave-a-week-out choice (MSE) | 1 (7.33); 21 (14.76) |
| Rolling origin (291-day initial window, 98 forecasts), MAE: naive / seasonal naive / SES / Holt–Winters weekly | 2.617 / 3.794 / 2.661 / 2.330 |
| SES α (first 291 days); Holt–Winters level parameter | 0.966; 0.780 |
| MASE scale (in-sample naive MAE); MASE of Holt–Winters | 2.775; 0.840 |
| AI-generated evaluation MAE; honest rolling-origin regression MAE | 0.535; 2.552 |
| Simulated random walk (400 steps): SES α; MAE naive / SES | 0.972; 0.764 / 0.765 |

## 4. Limitations

* **Not yet run in a real Colab runtime.** Before the session, open Lab 8 from its badge in Colab and run *Restart session and run all* once.
* The Colab badge points to the `main` branch, so it works once this module is merged into `main`.
* The Holt–Winters fit estimates a weekly pattern that does not change over the year (seasonal smoothing parameter 0); a changing pattern is not examined.
