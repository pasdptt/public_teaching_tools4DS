# Lecture outline — Reproducible workflow, statistics refresher and SQL (module m01, week 1)

**Slides:** [m01 lecture deck](https://claude.ai/artifact/Erv2PRZxAsxNxXpYNVXjMN) (34 slides, for projection). The deck and this outline match section for section; the slide numbers are given in each section heading. Change both together.

**Length:** 2 hours, delivered in Thai with English slides and terms. **Lab:** [Lab 1](../lab/lab1_workflow_refresher.ipynb) (3-hour guided run-through, then redone as homework; practice).

Every number in this outline was produced by the Lab 1 code and is the same in both CI environments (see [`../EXECUTION-REPORT.md`](../EXECUTION-REPORT.md)). Reference keys such as [Rul19] point to [`../references.md`](../references.md). The misconception checks (MC1–MC6) are in [`../exercises/misconception-checks.md`](../exercises/misconception-checks.md).

| Time | Section | Purpose |
|---|---|---|
| 0:00–0:20 | §1 How this course works | Outcomes, assessment, graded labs on Microsoft Teams, project teams, AI policy |
| 0:20–0:45 | §2 Notebooks as documents | Hidden state, execution order, seeds, environments |
| 0:45–0:55 | §3 Where data come from | Provenance, licences, citations; the `tsds` registry |
| 0:55–1:05 | Break | |
| 1:05–1:30 | §4 Statistics refresher | Which mean, `ddof`, sentinels and missing values, floating point |
| 1:30–1:50 | §5 SQL for statisticians | `GROUP BY`, NULLs, window functions in DuckDB |
| 1:50–2:00 | §6 AI-assisted coding, and the lab | Verification as the skill; what to do in Lab 1 |

---

## §1 How this course works (20 min) · slides 3–8

**What the course is for.** Methods that make high-dimensional, relational, temporal or large data analysable: dimension reduction (PCA, LDA, ICA), feature selection and extraction, network analysis, smoothing and aggregation, laptop-scale high-performance computing and streaming. The common thread is **valid evaluation**: every result is compared with a simple baseline, under a validation protocol that does not leak information, with an honest account of how it can fail.

**Course learning outcomes** (from the [syllabus](../../../course/syllabus.md)): CLO1 derive and compute PCA, LDA and ICA; CLO2 reproducible workflows without leakage; CLO3 compare methods against baselines with uncertainty; CLO4 graphs; CLO5 smoothing and temporal validation; CLO6 computational cost, HPC and streaming; CLO7 communicate, including failure analysis and AI disclosure.

**Assessment** ([details](../../../course/assessment.md)):

| Component | Weight | Format |
|---|---|---|
| Practical work | 20% | **Six graded labs** (G1–G6), 3⅓% each, all count. Code is re-run and auto-checked by hidden tests; written answers (at most 100 words each) are marked with the [lab rubric](../../../course/rubrics.md#lab-rubric-graded-labs). |
| Project | 25% | Teams of 5–6 (at most 20 teams); five milestones; peer-assessment factor 0.8–1.1; live presentation with code questions to two random members |
| Midterm | 20% | In person, on paper, closed book with one A4 sheet; weeks 1–6 |
| Final | 35% | In person, on paper; cumulative |

**Practical rules to state on day 1:**
* All labs run in **Google Colab**; nothing to install. Open from the module page, then **File → Save a copy in Drive**.
* Submit the `.ipynb` file to the lab's **Microsoft Teams** assignment. **Late submissions are accepted; a graded lab that is never submitted scores 0.**
* Before submitting: **Runtime → Restart session and run all**. The grader re-runs your notebook from the top in a fresh session; a notebook that only works out of order loses the reproducibility mark.
* Do not change the given cells or the self-check cells.
* **Every lab week:** the lab session is a guided **run-through**; you then do the lab **again on your own as homework** and submit it in Teams. For graded labs, the homework is what is marked.
* Lab 1 (this week) is **practice**, in exactly the format of the graded labs: use it to rehearse, including the Teams upload.
* **Project:** teams of 5–6 form in weeks 1–2; the proposal (M1) is due in week 3.

**AI policy** ([full text](../../../course/ai-policy.md)): AI tools are **allowed in labs and the project with disclosure** (the AI-use log at the end of every notebook), you must be able to explain any cell you submit, and examinations are without AI. Verification, not prompting, is the skill: "it looked right" is not verification.

## §2 Notebooks as documents (25 min) · slides 9–13

**2.1 The notebook's hidden state.** A Jupyter/Colab kernel keeps every variable you created, in the order you **ran** cells, not the order they **appear**. So the same file can produce different results, or none, depending on its run history. A large study of public notebooks found that only a minority could be re-executed to reproduce their stored results [Pim19].

**2.2 Worked example (the Lab 1 Part 1 cells).** Three cells:

```python
# cell 0
raw = np.array([52.0, 61.0, 70.0, 85.0, 47.0])   # exam scores in percent
# cell 1
summary = {"mean": round(float(prop.mean()), 4), "sd": round(float(prop.std(ddof=1)), 4)}
# cell 2
raw = raw / 100       # percent -> proportion
prop = raw
```

| Run history | Result |
|---|---|
| 0, 2, 1 (what the author did) | `{"mean": 0.63, "sd": 0.1512}` |
| 0, 1, 2 (*Restart and run all*) | `NameError: name 'prop' is not defined` |
| 0, 2, 2, 1 (cell 2 run twice, e.g. after editing a comment) | `{"mean": 0.0063, "sd": 0.0015}` |

Two different defects: an **out-of-order dependency** (caught by *Restart and run all*) and a cell that **overwrites its own input** (not caught by a fresh run, but it makes any result in a live session depend on how many times you clicked). The fixes: define before use, and never reassign an input (`prop = raw / 100`), so every cell can be rerun safely.

**2.3 The course's evidence.** The audit of this course's previous notebooks ([evidence audit §1.5](../../../docs/audit/01-evidence-audit.md)) found an instructor answer key that fails in a fresh top-to-bottom run because a cell uses a variable before it is defined, notebooks whose numbers changed on every run because no random seed was set, and notebooks broken by newer package versions.

**2.4 What the course does about it.**
* **Restart and run all** before every submission; the grader checks it.
* **One seed:** the setup cell sets `SEED` and `rng`; pass `random_state=SEED` wherever a function takes one.
* **Pinned environments:** every lab is tested in CI against a pinned local environment and a Colab-like one; the setup cell prints your versions and warns if one is outside the tested range.
* **Rules worth adopting** for your project notebooks: tell a story with markdown, keep cells short and rerunnable, record dependencies, and share data with provenance [Rul19]; practical habits for scientific computing more broadly are in [Wil17].

> **MC1** (hidden state) and **MC2** (restart and run all) here.

## §3 Where data come from (10 min) · slides 14–15

* Every dataset used in required work has a **verified licence**, a **citation** and either ships with scikit-learn or is downloaded with a **SHA-256 checksum** ([dataset policy](../../../datasets/README.md)). No Google Drive mounts, no Kaggle tokens.
* `tsds.data.info("air_quality")` prints the licence and citation; `tsds.data.load("air_quality")` downloads the UCI file, checks its checksum and returns it **raw**.
* **This week's data:** Air Quality, hourly averages from a chemical multisensor device in an Italian city, March 2004 – April 2005, 9,357 hours [DeV08; Vit08]. Licence CC BY 4.0, which requires attribution: cite the dataset whenever you use it.
* For your project (M1): the proposal must name the dataset's licence and citation. "I found it on Kaggle" is not a licence.

## §4 Statistics refresher (25 min) · slides 17–23 (slide 16: break)

**4.1 Which mean?** The question decides the mean.

| Question | Mean | Lab 1 example | Value |
|---|---|---|---|
| Average amount | Arithmetic $\bar x = \frac1n\sum x_i$ | monthly returns 10%, −5%, 20%, −15%, 8% | 3.60% |
| Constant growth rate with the same total | Geometric: $\left(\prod (1+r_i)\right)^{1/n} - 1$ | same returns | **2.86%** |
| Constant rate over equal distances | Harmonic: $n / \sum (1/x_i)$ | 60 km legs at 30, 60, 90 km/h | **49.09 km/h** |

The investment grew by a factor of $\prod(1+r_i) = 1.1512$. Compounding the arithmetic mean, $1.036^5 = 1.193$, overstates it; compounding the geometric mean reproduces it exactly. The trip spends more **time** on the slow leg, so the average speed (total distance / total time = 180 km / 3.667 h) is below the arithmetic mean of 60 km/h. For positive data, $\text{HM} \le \text{GM} \le \text{AM}$, with equality only when all values are equal.

**4.2 `ddof`: which standard deviation?** For $x = (52, 61, 70, 85, 47)$:

| Call | Divisor | Value |
|---|---|---|
| `np.std(x)` | $n$ | 13.5204 |
| `pd.Series(x).std()`, `np.std(x, ddof=1)` | $n-1$ | 15.1162 |

numpy and pandas have **different defaults**. For a sample, the $n-1$ divisor makes the variance unbiased; always write `ddof=` explicitly so the reader does not need to know the library default.

**4.3 Missing values and sentinel codes.** A *sentinel* is a valid-looking number that means "missing". Air Quality codes missing values as **−200**: the raw file has 366 temperatures of −200 °C.

| Temperature | Mean | Minimum |
|---|---|---|
| Raw (−200 treated as data) | 9.78 °C | −200 °C |
| After recoding −200 → NaN | 18.32 °C | −1.9 °C |

Nothing raises an error: −200 is a perfectly good float. Defences: read the data documentation, and run **range checks** (`describe()`; an impossible minimum is a red flag) before any summary. After recoding, report **coverage**: the non-methane hydrocarbon column is 90.2% missing, CO 18.0%, temperature 3.9%.

**4.4 Floating point.** `0.1 + 0.2 == 0.3` is `False` in binary floating point; `(x / 100).mean()` above gives `0.6299999999999999`. Compare decimals with `np.isclose`, never `==` [Gol91].

> **MC3** (mean choice), **MC4** (`ddof`) and **MC5** (sentinels) here.

## §5 SQL for statisticians (20 min) · slides 24–28

**Why SQL in a statistics course.** Most organisational data live in databases; SQL is how you get a correct summary out of them. DuckDB is an analytical SQL engine that runs inside Python, on a laptop or in Colab, directly on a pandas DataFrame, with no server [RM19]. In week 11 it returns as a tool for data larger than memory.

**5.1 Aggregation.** Daily mean CO and the number of valid hours:

```sql
SELECT CAST(ts AS DATE) AS day,
       AVG(co)          AS co_mean,
       COUNT(co)        AS n_valid
FROM aq_tbl
GROUP BY day
ORDER BY day;
```

391 days; 36 of them have **no** valid CO reading, so their `co_mean` is NULL.

**5.2 NULL semantics.** `AVG(col)` and `COUNT(col)` **skip NULL**; `COUNT(*)` counts rows. pandas' `NaN` arrives in SQL as NULL. Writing `COUNT(*)` for "valid hours" silently counts missing hours as valid.

A small made-up example: four hours with `co` = 2.0, NULL, 3.0, 4.0 give `COUNT(*)` = 4, `COUNT(co)` = 3 and `AVG(co)` = 3.0 (the mean of the three valid values).

**5.3 Window functions.** A window function returns one value **per row**, computed from neighbouring rows, without collapsing groups:

```sql
SELECT ts,
       AVG(co) OVER (ORDER BY ts ROWS BETWEEN 23 PRECEDING AND CURRENT ROW) AS co24
FROM aq_tbl ORDER BY ts;
```

This 24-row trailing mean equals pandas' `aq["co"].rolling(24, min_periods=1).mean()`. Without `min_periods=1`, pandas returns NaN whenever any hour in the window is missing, whereas SQL averages the valid ones. Twenty-four **rows** are twenty-four **hours** only because the index has no gaps (checked in Lab 1); otherwise use a time-based window. Rolling means return in week 10 (smoothing).

**5.4 Two methods as a test.** Computing the same summary in pandas and in SQL and checking they agree is one of the cheapest strong tests of an analysis.

## §6 AI-assisted coding, and the lab (10 min) · slides 29–33 (slide 34: references)

**Worked example (Lab 1 Part 5).** Asked "using `aq`, compute the daily mean CO concentration", an AI assistant answered:

```python
daily_ai = aq.groupby(aq.index.day)["co"].mean()
```

It runs, returns sensible-looking CO values labelled by "day", and is **wrong**: `.day` is the day of the **month**, so it averages all the 1sts together and returns 31 values instead of 391 daily means. A test written *before* reading the answer, "one value per calendar day: 391", exposes it at once.

**The verification habit for this course:**
1. State a checkable property before you read the code (a row count, one value computed by hand, agreement with a second method).
2. Turn it into an `assert`.
3. Record what you checked in the AI-use log.

> **MC6** (AI audit) here.

**Lab 1:** environment check (Part 0), hidden state (Part 1), means and `ddof` (Part 2), Air Quality sentinels (Part 3), pandas vs DuckDB (Part 4), AI audit (Part 5). In the lab session we run through it together; then you do it again on your own as homework, from a fresh copy, finish with *Restart session and run all*, and upload it to the Lab 1 practice assignment in Teams. It is not graded, but it has the same structure, self-checks and AI-use log as the graded labs.

**Independent work this week (5 h):** redo Lab 1 on your own and submit it (about 2 h); the core items of the [problem set](../exercises/problem-set.md) (about 2 h); read [Rul19] and the [AI policy](../../../course/ai-policy.md) (about 1 h); start forming a project team of 5–6.
