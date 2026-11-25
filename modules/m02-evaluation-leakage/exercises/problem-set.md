# Problem set — module m02 (independent work, about 1.5 hours)

This week's independent work is: **do Lab 2 (graded lab G1) on your own and submit it in Teams** (about 2.5 hours), read Kapoor and Narayanan (2023) (about 1 hour), the **core** items below (P1–P5; about 1 hour) and the project task P9 (about 0.5 hours). Items marked *(optional)* are extra practice. Not graded; answers are discussed at the start of the next session. Items marked **[hand]** are the kind that appear on the paper midterm.

**P1 [hand] — A Wilson interval.** A model is correct on 45 of 50 test cases. (a) Compute the 95% Wilson interval ($z = 1.96$). (b) Compute the Wald interval $\hat p \pm z\sqrt{\hat p(1-\hat p)/n}$ and compare. (c) The majority baseline would be correct on 40 of the 50. Is the model clearly better?

**P2 [hand] — Width and sample size.** Roughly how many test cases are needed to halve the width of an interval for an accuracy near 0.9, compared with 100 test cases? Explain.

**P3 [hand] — Choose the split.** For each scenario, name the validation scheme and say what the groups or the time order are: (a) 12 photos per plant for 200 plants, to classify new plants' diseases; (b) monthly sales of 50 shops, to forecast next month; (c) exam results of students in 40 schools, to predict results in new schools; (d) tuning the number of neighbours of a k-NN classifier and reporting its accuracy.

**P4 [hand] — Name the leakage.** Classify each case by type (preprocessing, target, temporal, group, graph, test-set reuse): (a) missing values imputed with column means computed on all the data, then 5-fold CV; (b) a loan-default model that uses "number of collection calls"; (c) a stock-return model validated with shuffled k-fold on daily data; (d) node features computed from a network that includes the test nodes; (e) the best of 50 random seeds reported.

**P5 [hand] — Code review** (the format of midterm item 3). Find the leakage and rewrite the lines so the estimate is honest:

```python
X_scaled = StandardScaler().fit_transform(X)
X_sel = SelectKBest(f_classif, k=10).fit_transform(X_scaled, y)
scores = cross_val_score(LogisticRegression(), X_sel, y, cv=5)
print(scores.mean())
```

**P6 — Leakage grows with the search** *(optional)*. Repeat Lab 2 Part 3 with `SelectKBest` keeping $k$ = 5, 20 and 100 of the 1,000 noise features, fitted before CV. How does the leaked accuracy change with $k$? Explain.

**P7 [hand] — Metrics at 10% positives** *(optional)*. A classifier on 500 cases has TP = 30, FP = 10, FN = 15, TN = 445. Compute accuracy, precision, recall and F1 of the positive class. What accuracy does "always negative" get?

**P8 — Reading** *(optional)*. From Kapoor and Narayanan (2023), choose one type of leakage in their taxonomy and describe how it could occur in a project you might do in this course.

**P9 — Project.** With your team (5–6 students), choose a candidate dataset and record its source, licence and citation. Say what "new data" would mean for it, and which split from P3 would imitate that.
