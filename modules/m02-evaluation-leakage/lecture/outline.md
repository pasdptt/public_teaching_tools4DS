# Lecture outline — Evaluation and leakage (module m02)

**Slides:** [m02 lecture deck](https://claude.ai/artifact/9beCW6rFFS5z4sSCfPPFzL) (24 slides, for projection). The deck and this outline match section for section; the slide numbers are given in each section heading. Change both together.

**Length:** 2 hours, delivered in Thai with English slides and terms. **Lab:** [Lab 2](../lab/lab2_evaluation_leakage.ipynb), **graded lab G1** (guided run-through in the session; each student then does the lab as homework, and the homework is marked).

Every number in this outline was produced by the Lab 2 code and is the same in both CI environments (see [`../EXECUTION-REPORT.md`](../EXECUTION-REPORT.md)), unless marked as a made-up illustration. Reference keys such as [KN23] point to [`../references.md`](../references.md). The misconception checks (MC1–MC6) are in [`../exercises/misconception-checks.md`](../exercises/misconception-checks.md).

| Time | Section | Purpose |
|---|---|---|
| 0:00–0:10 | §1 What an evaluation must answer | New data, a baseline, uncertainty |
| 0:10–0:35 | §2 Splits that mimic deployment | Hold-out, k-fold, grouped, time-ordered, nested |
| 0:35–0:55 | §3 Baselines and intervals | Majority baseline; the Wilson interval |
| 0:55–1:05 | Break | |
| 1:05–1:35 | §4 Leakage | Definition, six types, how large it is |
| 1:35–1:50 | §5 Class imbalance is a fitted step | Metrics; resampling inside cross-validation |
| 1:50–2:00 | §6 AI audit, and graded lab G1 | Target leakage in an AI analysis; how G1 works |

---

## §1 What an evaluation must answer (10 min) · slide 3

An evaluation estimates how a model will perform **on the data it will meet in use**. Every evaluation in this course answers three questions:

1. **What is "new" data here?** New rows, new patients, next month, new nodes in a network? The validation split must imitate it.
2. **Better than what?** A model is only useful relative to a simple **baseline**.
3. **How sure are we?** A test score is an estimate from a finite sample; report its **uncertainty**.

A fourth condition makes the first three meaningful: **nothing from the test data may influence training or model choice** (no leakage).

## §2 Splits that mimic deployment (25 min) · slides 4–6

**2.1 The basic schemes.**

| Scheme | What it does | Use when |
|---|---|---|
| Hold-out (train/test) | One split; the test set is used once, at the end | Large data; a final report |
| k-fold CV | k splits; every row is tested once | Small or medium data |
| Repeated / stratified k-fold | Several k-fold runs; class shares kept in each fold | Unstable estimates; imbalanced classes |
| Grouped k-fold (`GroupKFold`) | Whole groups (patients, schools, customers) go to one side | Rows within a group are related |
| Time-ordered (`TimeSeriesSplit`) | Train on the past, test on the future | Forecasting (module m08) |
| Nested CV | An inner loop chooses settings; the outer loop estimates performance | Any tuning, e.g. choosing $k$ in PCA (module m04) [VS06] |

**The rule:** the split must imitate how the model will be used [Rob17].

**2.2 Worked example: grouped data (Lab 2, Part 2).** 40 patients × 10 measurements; the outcome is a property of the patient. A 1-nearest-neighbour classifier scores:

| Split | Accuracy |
|---|---|
| `KFold` (rows split at random) | **1.000** |
| `GroupKFold` (patients kept together) | **0.578** |

With rows split at random, each test row has nine rows of the same patient in training: the model recognises the patient, not the disease. For new patients, only the grouped estimate is honest.

> **MC1** (grouped data) here.

## §3 Baselines and intervals (20 min) · slides 7–10

**3.1 A baseline first.** Digits recoded as "is it a 9?" has 180 nines among 1,797 images (10.0%). A classifier that always says "not 9" is 90% accurate.

**3.2 The Wilson interval** for a proportion $\hat p = k/n$ [Wil27]:

$$\frac{\hat p + \frac{z^2}{2n}}{1 + \frac{z^2}{n}} \;\pm\; \frac{z}{1 + \frac{z^2}{n}}\sqrt{\frac{\hat p(1-\hat p)}{n} + \frac{z^2}{4n^2}}, \qquad z = 1.96 \text{ for } 95\%.$$

It stays inside $[0, 1]$ and keeps close to its nominal coverage for small $n$ and for $\hat p$ near 0 or 1, where the textbook (Wald) interval $\hat p \pm z\sqrt{\hat p(1-\hat p)/n}$ fails [BCD01]. For $k = 0$ the Wald interval is $[0, 0]$; the Wilson interval for 0 out of 10 is $[0, 0.278]$.

**3.3 Worked example (Lab 2, Part 1).** 450 test images:

| | Accuracy | 95% Wilson interval |
|---|---|---|
| Baseline (majority class) | 0.900 | 0.869 – 0.924 |
| Logistic regression | **0.973** | 0.954 – 0.985 |

The intervals do not overlap: the gain is larger than the test-set noise. The width shrinks like $1/\sqrt{n}$: with 40 test images instead of 450, the intervals would be about three times wider and would overlap.

> **MC2** (intervals) here.

## §4 Leakage (30 min) · slides 12–16 (slide 11: break)

**4.1 Definition.** Leakage is information that would not be available when the model is used, but enters its training or its selection [Kau12; KN23]. Leakage makes the estimate optimistic, and no amount of extra resampling detects it: the leaked information is in every split.

**4.2 Six types.**

| Type | Example |
|---|---|
| Preprocessing | A fitted step (scaling, feature selection, PCA, imputation, resampling) fitted on all data before the split |
| Target | A feature recorded after, or derived from, the outcome |
| Temporal | Future information used to predict the past (random splits of a time series) |
| Group | Related rows on both sides of the split (§2.2) |
| Graph | Edges or node features computed with test nodes (module m07) |
| Test-set reuse | Many models compared on one test set and the best one reported |

**4.3 How large is it? (Lab 2, Part 3).** Pure noise: 100 cases, 1,000 features, random labels, so every honest estimate is about 0.5. Repeated 5-fold CV (5 repeats) of logistic regression:

| Fitted step | Fitted on all data, before CV | Fitted inside the pipeline |
|---|---|---|
| `SelectKBest(k=20)` (uses $y$) | **0.776** | 0.410 |
| `StandardScaler()` (no $y$) | 0.506 | 0.516 |

A step that uses $y$ leaks a lot: it picks the noise features that happen to match the test folds' labels too [AM02]. A step without $y$ leaks little here, but the rule is the same for every fitted step: **fit it inside the pipeline**, because unsupervised steps can leak noticeably elsewhere (small samples, imputation, time series). The inside score below 0.5 is a small-sample artefact of cross-validation on noise.

**4.4 From this course's old notebooks.** The audit found a feature-extraction notebook that fitted LDA on all the data before splitting (audit issue E1, [evidence audit](../../../docs/audit/01-evidence-audit.md)): the same error as row 1 of the table, with a supervised step.

**4.5 Leakage in published research.** Kapoor and Narayanan reviewed machine-learning-based science across many fields, found leakage to be a widespread cause of irreproducible results, and proposed a taxonomy of leakage types [KN23].

> **MC3** (unsupervised steps) and **MC4** (test-set reuse) here.

## §5 Class imbalance is a fitted step (15 min) · slides 17–19

**5.1 Metrics.** At 10% positives, accuracy rewards ignoring the minority class. Use a metric that looks at the positives (F1 of the positive class, precision and recall, balanced accuracy) and use the **same** metric and the **same** splits for every method compared.

**5.2 Resampling is fitted.** SMOTE creates synthetic minority points by interpolating between neighbours [CBHK02]. Like any fitted step, it must see only the training folds: use `imblearn.pipeline`, which applies resamplers during `fit` only.

**5.3 Worked example (Lab 2, Part 4).** "Is it a 9?", 5-fold stratified CV, F1 of the positive class:

| Method | F1 |
|---|---|
| Plain logistic regression | 0.937 |
| `class_weight="balanced"` | 0.872 |
| SMOTE inside the pipeline | 0.894 |
| SMOTE on all data, then CV | **0.990** (invalid) |

The invalid score is wrong twice: test folds contain synthetic points interpolated from training points, and the test folds are balanced instead of 10% positive. Among the honest results, neither remedy improved on the plain model here: resampling changes the precision–recall trade-off; it is not a free gain.

> **MC5** (SMOTE) here.

## §6 AI audit, and graded lab G1 (10 min) · slides 20–23 (slide 24: references)

**Worked example (Lab 2, Part 5).** A clinic wants to predict a diagnosis **at the first visit**. An AI assistant fitted a model on all recorded columns and reported a cross-validated accuracy of **0.935**. One column, `treatment_started`, is recorded **after** the diagnosis. Without it the honest accuracy is **0.663**, against a majority baseline of **0.515**.

**The question for every feature:** would I have this value, measured this way, at the moment of prediction? More folds or a separate test set would not have caught this: the leaking column is in every split.

> **MC6** (target leakage) here.

**Graded lab G1 (Lab 2).** Five parts: baseline and Wilson interval; grouped data; leakage on noise; imbalance inside CV; the AI audit. In the lab session we run through the ideas together; each student then does the lab **on their own as homework**, from a fresh copy, and uploads the `.ipynb` to the G1 assignment in Teams. The homework is what is marked: the notebook is re-run and checked with hidden tests (3 + 1 points), and staff mark the written answers (2 + 2 points).

**Independent work this week (5 h):** do Lab 2 and submit it (about 2.5 h); read [KN23] (about 1 h); the core items of the [problem set](../exercises/problem-set.md) (about 1 h); project teams: agree on a dataset and check its licence (about 0.5 h).
