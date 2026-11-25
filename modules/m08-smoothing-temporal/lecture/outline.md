# Lecture outline — Smoothing, aggregation and temporal evaluation (module m08)

**Slides:** m08 lecture deck (link added when the deck is published). The deck and this outline match section for section; the slide numbers are given in each section heading. Change both together.

**Length:** 2 hours, delivered in Thai with English slides and terms. **Lab:** [Lab 8](../lab/lab8_smoothing_temporal.ipynb), **graded lab G5** with an AI-audit task (guided run-through in the session; each student then does the lab as homework, and the homework is marked).

Every number in this outline was produced by the Lab 8 code or the module's key-numbers script and is the same in both CI environments (see [`../EXECUTION-REPORT.md`](../EXECUTION-REPORT.md)). Data: Air Quality, hourly, March 2004 – April 2005 [registry `air_quality`]; the worked series is the **daily mean benzene concentration** (C6H6, µg/m³). Reference keys such as [Tas00] point to [`../references.md`](../references.md). The misconception checks (MC1–MC6) are in [`../exercises/misconception-checks.md`](../exercises/misconception-checks.md).

| Time | Section | Purpose |
|---|---|---|
| 0:00–0:15 | §1 Data before smoothing | Sentinels; aggregate to a regular grid with a coverage rule |
| 0:15–0:40 | §2 Smoothers as estimators | Trailing vs centred MA, EWMA, kernel and LOESS; bandwidth |
| 0:40–0:50 | §3 Choosing the bandwidth | Leave-one-out fails on autocorrelated data; leave a block out |
| 0:50–1:00 | Break | |
| 1:00–1:25 | §4 Exponential smoothing models | SES, Holt, Holt–Winters, with estimated parameters |
| 1:25–1:45 | §5 Temporal evaluation | Rolling origin; naive baselines; MAE, RMSE, MASE; the random walk |
| 1:45–1:55 | §6 Temporal leakage and the AI audit | A forecast that is too good |
| 1:55–2:00 | §7 Graded lab G5 and project M3 | This week's work |

---

## §1 Data before smoothing (15 min)

**1.1 Sentinels (audit M15).** The file codes missing values as −200 (366 hours of temperature, the same outages for benzene). The course's old notebook smoothed temperature with the sentinels in. An EWMA with α = 0.1 then falls to **−199.9 °C**, and differs from the correctly recoded EWMA by up to **224.7 °C** (Lab 8 Part 1; key numbers). Recode first, then look at the minimum and maximum.

**1.2 A regular grid.** Smoothers and forecasting models assume equally spaced observations. The raw file is a regular hourly grid (9,357 rows), but dropping the sentinel hours leaves 16 gaps, the longest 3 days 5 hours. Aggregate to **daily means** with a **coverage rule**: a day counts only with at least 18 valid hours. For benzene: 391 calendar days, 20 below the rule; 18 of them inside the series are filled by time interpolation, and the incomplete first and last days are dropped, leaving 389 days. State the rule and count what you filled.

> **MC1** (sentinels) here.

## §2 Smoothers as estimators (25 min)

A smoother estimates a slowly varying signal $m(t)$ in $y_t = m(t) + \varepsilon_t$.

| Smoother | Uses | Can forecast? |
|---|---|---|
| Trailing MA($k$): mean of $y_{t-k+1}, \dots, y_t$ | the past only | yes, but lags a trend by $(k-1)/2$ steps (3 days for $k = 7$) |
| Centred MA($k$): mean of $y_{t-(k-1)/2}, \dots, y_{t+(k-1)/2}$ | past and **future** | no |
| EWMA: $\ell_t = \alpha y_t + (1-\alpha)\ell_{t-1}$ | the past, weights $\alpha(1-\alpha)^j$ | yes |
| Kernel (Nadaraya–Watson) [Nad64] | all points, weights $K((t - t_j)/h)$ | no (two-sided) |
| LOESS [Cle79] | local weighted regression in a window | no (two-sided) |

**Bandwidth** ($k$, $\alpha$, $h$ or the LOESS span) trades bias against variance: small = follows the noise; large = flattens real changes. It must be **chosen by a stated criterion**, not by eye.

> **MC2** (a centred window for forecasting) here.

## §3 Choosing the bandwidth (10 min)

**Criterion:** predict each day from the other days and minimise the mean squared error (Lab 8 Part 2, Gaussian kernel, benzene):

| $h$ (days) | 1 | 2 | 3 | 5 | 7 | 10 | 14 | 21 | 30 |
|---|---|---|---|---|---|---|---|---|---|
| Leave one out | **7.33** | 10.27 | 11.83 | 12.60 | 12.99 | 13.43 | 13.69 | 13.90 | 14.19 |
| Leave out ±3 days | 24.13 | 21.40 | 18.32 | 15.86 | 15.36 | 15.20 | 14.97 | **14.76** | 14.83 |

Leave-one-out picks the smallest bandwidth: neighbouring days are correlated (lag-1 autocorrelation 0.614), so they "know" the left-out day, and following the noise looks good. Leaving out a block around each day removes that shortcut and picks $h = 21$, a smooth seasonal level. With correlated errors, ordinary cross-validation undersmooths [CM91; OWY01].

> **MC3** (leave-one-out) here.

## §4 Exponential smoothing models (25 min)

**SES:** $\hat y_{t+1} = \ell_t$, $\ell_t = \alpha y_t + (1-\alpha)\ell_{t-1}$. **Holt** adds a trend $b_t$ [Hol04]; **Holt–Winters** adds a seasonal component (here weekly, additive) [Win60]. The smoothing parameters and initial states are **estimated** by minimising the one-step squared errors on the training data, not fixed in advance (the old notebook fixed α = 0.6, audit M18).

On benzene's first 291 days: SES estimates α = **0.966**, so it puts almost all its weight on today and is almost the naive forecast. Holt–Winters estimates a level parameter of 0.780 and a fixed weekly pattern, matching the traffic cycle in the weekday means (Monday 9.9; Tuesday–Friday 11.3–11.7; Saturday 8.6; Sunday 6.1).

> **MC4** (α close to 1) here.

## §5 Temporal evaluation (20 min)

**Rolling origin** [Tas00]. At each origin $o$, fit on days $0, \dots, o-1$, forecast day $o$, move on one day. Here the first 75% (291 days) is the initial window: 98 one-step forecasts (Lab 8 Part 3).

| Method | MAE | MASE |
|---|---|---|
| Naive (tomorrow = today) | 2.617 | 0.943 |
| Seasonal naive (same weekday last week) | 3.794 | 1.367 |
| SES (α estimated) | 2.661 | 0.959 |
| **Holt–Winters, weekly** | **2.330** | **0.840** |
| Regression on lags (Part 4, honest) | 2.552 | 0.920 |

**Measures.** MAE is in the data's units; RMSE penalises large errors more; **MASE** divides by the in-sample MAE of the naive forecast (2.775 here), so MASE < 1 beats naive [HK06]. Always report a naive baseline.

**The random walk is a process, not a smoother (audit M14).** $y_t = y_{t-1} + \varepsilon_t$. Its best one-step forecast is the naive forecast. On a simulated random walk (400 steps, course seed) SES estimates α = 0.972 and matches naive (MAE 0.765 vs 0.764). The naive forecast is the baseline every method must beat.

> **MC6** (random walk) here.

## §6 Temporal leakage and the AI audit (10 min)

An AI-generated "forecast of tomorrow's benzene" (Lab 8 Part 4) reports **MAE 0.535**, far better than any method above. Three leaks:

1. **A same-day predictor:** the daily mean of the PT08.S2 sensor, which tracks benzene almost perfectly and is not known the evening before. This is a same-day estimate, not a forecast.
2. **A centred window:** `rolling(3, center=True)` puts days $t$ and $t+1$ into day $t$'s feature.
3. **Shuffled K-fold:** the model trains on later days.

The honest version uses only what is known the evening before (yesterday, the same weekday last week, the mean of the previous 7 days) and refits at each rolling origin: **MAE 2.552**, a small gain over naive. Other temporal leaks: scaling or imputing with full-series statistics; look-ahead features.

> **MC5** (shuffled K-fold) here.

## §7 Graded lab G5 and project M3 (5 min)

**Graded lab G5 (Lab 8).** Four parts: sentinels and daily aggregation; smoothers and the bandwidth criterion; rolling-origin evaluation of four methods; the AI audit. In the session we run through the ideas on another pollutant; each student then does the lab **on their own as homework** and uploads the `.ipynb` to the G5 assignment in Teams. The homework is what is marked (3 + 1 points auto-checked, 2 + 2 points written answers).

**Project M3** (method comparison) is due this week ([project brief](../../../course/project-brief.md)).

**Independent work this week (5 h):** Lab 8 and submit it (about 2 h); reading [Tas00] and the problem set (about 1 h); project M3 with your team (about 2 h).
