# Problem set — module m08 (independent work)

This week's independent work is: **do Lab 8 (graded lab G5) on your own and submit it in Teams** (about 2 hours), the **reading and this problem set** (about 1 hour), and **project M3** with your team (about 2 hours). Not graded. Items marked **[hand]** are the kind that appear on the paper final (item 5).

**P1 [hand] — SES by hand.** A series is 10, 12, 11, 15. With α = 0.5 and initial level ℓ₀ = 10, compute the one-step forecasts for each of the four values and the forecast of the fifth. Then say what α = 1 and α = 0 would give.

**P2 [hand] — EWMA weights and trailing lag.** (a) Write the weights an EWMA with α = 0.3 puts on today and the four previous days. What share of the total weight falls on the last 7 days? (b) On a series that rises by one unit per day, by how many days does a trailing 7-day mean lag? A centred one?

**P3 [hand] — Accuracy measures.** Actual values 12, 15, 14, 18; forecasts 13, 13, 16, 17. Compute MAE and RMSE. If the in-sample MAE of the naive forecast is 2.0, what is the MASE, and is the method better than naive?

**P4 [hand] — Spot the leak.** For each, say whether it leaks the future and how to fix it: (a) standardising a series with its full-series mean and SD before rolling-origin evaluation; (b) a 7-day centred mean as a feature; (c) yesterday's value as a feature with a rolling-origin split; (d) a random 80/20 split of days.

**P5 — Another pollutant** *(optional)*. Repeat Lab 8 Parts 1–3 for `NO2(GT)` (more sentinel hours). How many days fail the coverage rule? Which bandwidth does each criterion choose, and does Holt–Winters still beat naive?

**P6 — LOESS** *(optional)*. Smooth the benzene series with `statsmodels.nonparametric.smoothers_lowess.lowess` and choose its span `frac` by the leave-a-week-out criterion of Lab 8. Compare with the kernel smoother.

**P7 — Reading.** Tashman (2000), on rolling-origin evaluation ([references](../references.md)). Which of its recommendations did Lab 8 follow, and which did it not?

**P8 — Project M3.** With your team, compare at least one dimension-reduction or feature method and one of network / smoothing / HPC / streaming against the baseline, every fitted step inside validation, with a failure-analysis section ([project brief](../../../course/project-brief.md)). One member uploads it to the M3 assignment in Teams.
