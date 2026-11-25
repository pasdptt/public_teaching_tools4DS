# Lecture outline — Feature selection vs feature extraction (module m03)

**Slides:** m03 lecture deck (link added when the deck is published). The deck and this outline match section for section; the slide numbers are given in each section heading. Change both together.

**Length:** 2 hours, delivered in Thai with English slides and terms. **Lab:** [Lab 3](../lab/lab3_selection_extraction.ipynb) (3-hour guided run-through, then redone as homework; practice). **Project:** the proposal (M1) is due this week.

Every number in this outline was produced by the Lab 3 code and is the same in both CI environments (see [`../EXECUTION-REPORT.md`](../EXECUTION-REPORT.md)). Reference keys such as [Str07] point to [`../references.md`](../references.md). The misconception checks (MC1–MC6) are in [`../exercises/misconception-checks.md`](../exercises/misconception-checks.md).

| Time | Section | Purpose |
|---|---|---|
| 0:00–0:15 | §1 Why reduce dimension | Distances lose contrast; noise, cost, interpretation |
| 0:15–0:35 | §2 Selection or extraction | Keep variables or make new ones; Wine compared with a baseline |
| 0:35–0:55 | §3 Three families of selection | Filter, wrapper, embedded; always inside CV |
| 0:55–1:05 | Break | |
| 1:05–1:25 | §4 Is the selection stable? | Selection frequencies and Jaccard similarity across folds |
| 1:25–1:50 | §5 Importance measures | Coefficients, impurity, permutation on held-out data |
| 1:50–2:00 | §6 Lab 3 and the project proposal | What to do this week |

---

## §1 Why reduce dimension (15 min)

**1.1 Distances lose contrast.** For 500 random points in the unit cube $[0,1]^p$, the relative contrast of the distances from one point to all others, $(d_{\max} - d_{\min})/d_{\min}$, is:

| $p$ | 2 | 10 | 100 | 1000 |
|---|---|---|---|---|
| Contrast | 50.3 | 2.39 | 0.37 | 0.10 |

At $p = 1000$ the farthest point is only about 10% farther than the nearest, so "nearest neighbour" carries little information [Bey99]. Methods built on distances (nearest neighbours, clustering, kernels) suffer first.

**1.2 Other reasons.** Every irrelevant feature adds noise to a fitted model; features cost money to measure; and a model on 5 variables is easier to explain than one on 500. Reduction is a **fitted step**: it must be validated like any other (module m02).

> **MC1** (distances in high dimension) here.

## §2 Selection or extraction (20 min)

**2.1 Definitions.**

| | Feature selection | Feature extraction |
|---|---|---|
| Output | A **subset** of the original variables | **New** variables, combinations of the originals |
| Example | Keep 5 of Wine's 13 measurements | 5 principal components (module m04) |
| Interpretation | Direct: the original units | Indirect: through the loadings |
| Measurement cost | Only the kept variables are needed | Every original variable is still needed |

**2.2 Worked example: Wine (Lab 3, Part 2).** 178 wines, 13 measurements, 3 cultivars; repeated 5-fold CV (5 repeats, 25 scores); every fitted step inside the pipeline.

| Model | Mean accuracy | SD over 25 folds |
|---|---|---|
| Majority baseline | 0.399 | 0.015 |
| All 13 features | **0.980** | 0.023 |
| `SelectKBest(k=5)` (filter) | 0.975 | 0.029 |
| `RFE` to 5 features (wrapper) | 0.969 | 0.032 |
| `PCA(5)` (extraction) | 0.967 | 0.030 |

Reducing 13 features to 5 costs at most 0.013 here, well inside one fold-to-fold SD, and every model is far above the baseline. The choice between them is therefore about **interpretation and cost**, not accuracy.

> **MC2** (what extraction saves) here.

## §3 Three families of selection (20 min)

| Family | How it chooses | Example | Cost |
|---|---|---|---|
| Filter | A statistic per feature, ignoring the model | `SelectKBest(f_classif)`: one-way ANOVA F | Cheap; ignores interactions and redundancy |
| Wrapper | Refits the model on candidate subsets | Recursive feature elimination (RFE) [Guy02] | Expensive; can overfit the selection |
| Embedded | Selection is part of fitting | L1 (lasso) penalty; tree-based models | Moderate; tied to one model |

**The one rule for all three:** the selection uses the outcome $y$, so it must happen **inside** cross-validation. Module m02 showed the cost of breaking it: on pure noise, selecting 20 of 1,000 features before CV gave 0.776 instead of about 0.5.

> **MC3** (selection inside CV) here.

## §4 Is the selection stable? (20 min)

A selection method run on different training folds can pick different features. If it does, the set from one run should not be presented as "the important features" [KPH07].

**4.1 Two measures.** The **selection frequency** of a feature is the share of folds in which it is selected. The **Jaccard similarity** of two selected sets is $|A \cap B| / |A \cup B|$; its mean over all pairs of folds summarises stability (1 = identical every time).

**4.2 Worked example (Lab 3, Part 3).** Selecting 5 of Wine's 13 features on each of the 25 training folds:

| Feature | `SelectKBest` | `RFE` |
|---|---|---|
| alcohol, proline, flavanoids | 1.00 each | 1.00 each |
| colour intensity | 0.88 | 0.96 |
| OD280/OD315 | 1.00 | 0.24 |
| hue | 0.12 | 0.80 |
| **Mean Jaccard** | **0.927** | **0.868** |

Both agree on a stable core of four features; the fifth depends on the method, because correlated features can substitute for each other. Report frequencies, not one run's set. **Stability selection** turns this idea into a method with error control [MB10].

> **MC4** (one run's selected set) here.

## §5 Importance measures (25 min)

**5.1 Coefficients.** A regression coefficient is per unit of its variable: 0.002 per baht and 2 per thousand baht are the same effect. Compare coefficients only on standardised variables, and distrust them under collinearity, where correlated variables share or swap the effect.

**5.2 Impurity importance** (`feature_importances_` of a random forest [Bre01]) sums how much each feature's splits reduced impurity **on the training data**. It favours variables with many possible split points, such as continuous variables and ID numbers [Str07].

**5.3 Permutation importance** on **held-out** data: shuffle one feature's values in the test set and measure how much the score drops. A feature the model does not use, or uses only to fit noise, scores about 0.

**5.4 Worked example (Lab 3, Parts 4–5).** A known truth: `signal` (0/1) changes $P(y = 1)$ from 0.30 to 0.70; `noise_cont`, `noise_id` and `noise_bin` are pure noise. Random forest, 300 trees; train accuracy 1.000, test accuracy 0.633.

| Feature | Impurity (training) | Permutation, training data | Permutation, **test** data |
|---|---|---|---|
| signal | 0.159 | 0.314 | **0.119** |
| noise_cont | **0.402** | 0.281 | 0.000 |
| noise_id | **0.411** | 0.291 | 0.021 |
| noise_bin | 0.028 | 0.134 | −0.026 |

Fully grown trees memorise the training data, splitting many times on the continuous and ID noise. Impurity importance, and permutation importance computed on the **training** data, both reward that memorisation. Only the test-data permutation importance identifies the real signal. The course's old notebook computed permutation importance on the training data (audit issue M12).

**What permutation importance is not:** it measures how much **this model** uses a feature, not whether the feature causes the outcome; correlated features can share or hide importance.

> **MC5** (impurity importance) and **MC6** (importance on training data) here.

## §6 Lab 3 and the project proposal (10 min)

**Lab 3 (practice).** Five parts: distance contrast; selection vs extraction against a baseline; stability across folds; impurity vs permutation importance; the failure analysis of training-data importance. In the lab session we run through it together; each student then does it again on their own as homework and uploads it to the Lab 3 practice assignment in Teams.

**Project proposal (M1) due this week:** one page with the question, the dataset with its verified licence and citation, the unit of analysis, the intended methods, team roles, and one sentence on what would count as "the method helped" ([project brief](../../../course/project-brief.md)); one member uploads it to the M1 assignment in Teams.

**Independent work this week (5 h):** redo Lab 3 on your own and submit it (about 1.5 h); the core items of the [problem set](../exercises/problem-set.md) (about 1 h); write the project proposal M1 with your team (about 2.5 h).
