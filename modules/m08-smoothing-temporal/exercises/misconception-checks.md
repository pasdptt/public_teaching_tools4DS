# Misconception checks — module m08 (formative, in lecture)

Use these with a show of hands or a polling tool (for example a Microsoft Forms quiz in the class team). Students answer individually, discuss in pairs for one minute, then re-vote. Each item names the misconception it targets. Answers and discussion notes are kept with the instructor material.

**MC1 — Sentinels** (lecture §1). A sensor file codes missing readings as −200. An analyst computes a 24-hour moving average of temperature without recoding. What is most likely?
A. nothing: averaging removes outliers · B. the average drops far below any real temperature around each outage · C. the code fails with an error · D. only the variance changes

**MC2 — Centred windows** (lecture §2). True or false: *"A centred 7-day moving average is a better forecast of tomorrow than a trailing one, because it is not lagged."* Explain in one sentence.

**MC3 — Leave-one-out bandwidth** (lecture §3). Leave-one-out cross-validation picks the smallest bandwidth for a daily pollution series. The most likely reason is:
A. the series has no noise · B. neighbouring days are correlated, so they predict the left-out day too well · C. the kernel is wrong · D. the series is too short

**MC4 — α close to 1** (lecture §4). Simple exponential smoothing fitted to a series estimates α = 0.97. What does that mean?
A. the series is very smooth, so SES works well · B. the forecast is almost "tomorrow = today" · C. the model failed to converge · D. the series has a strong trend

**MC5 — Shuffled K-fold** (lecture §6). True or false: *"Shuffled 5-fold cross-validation is fine for a forecasting model, as long as the features are computed correctly."* Explain.

**MC6 — The random walk** (lecture §5). A random walk $y_t = y_{t-1} + \varepsilon_t$ is best described as:
A. a smoothing method · B. a stochastic process whose best one-step forecast is the last value · C. a trend model · D. a way to remove outliers
