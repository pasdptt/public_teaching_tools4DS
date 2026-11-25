# Problem set — module m03 (independent work, about 1 hour)

This week's independent work is: **redo Lab 3 on your own and submit it in Teams** (about 1.5 hours), the **core** items below (P1–P5; about 1 hour) and the **project proposal M1** with your team (about 2.5 hours). Items marked *(optional)* are extra practice. Not graded; answers are discussed at the start of the next session. Items marked **[hand]** are the kind that appear on the paper midterm.

**P1 [hand] — Contrast.** Three points: $A = (0, 0)$, $B = (1, 0)$, $C = (0, 3)$. Compute the distances from $A$ to $B$ and $C$ and the relative contrast $(d_{\max} - d_{\min})/d_{\min}$. Without computing, would you expect the contrast of 3 random points in 1,000 dimensions to be larger or smaller? Why?

**P2 [hand] — Classify.** Is each a filter, wrapper or embedded selection method, or an extraction method? (a) keeping the 10 features with the highest correlation with $y$; (b) PCA to 3 components; (c) L1-penalised logistic regression; (d) forward stepwise selection by cross-validated accuracy; (e) dropping features whose variance is below 0.01.

**P3 [hand] — Jaccard.** Two folds selected {alcohol, proline, flavanoids, hue, colour intensity} and {alcohol, proline, flavanoids, OD280, magnesium}. Compute the Jaccard similarity.

**P4 [hand] — Units.** In a model of monthly spending, income has a coefficient of 0.002 (income in baht). (a) What is the coefficient if income is measured in thousands of baht? (b) Why should coefficients be compared only after standardising?

**P5 [hand] — Which importance?** For each question, choose impurity importance, permutation importance on training data, or permutation importance on held-out data, and explain: (a) "Which features does my model rely on for new customers?" (b) "How did my fitted trees split?"

**P6 — An embedded method** *(optional)*. Fit an L1-penalised logistic regression on standardised Wine features inside the same repeated CV as Lab 3, for C = 0.05, 0.1 and 1. Record the mean accuracy and the average number of features with a non-zero coefficient. (Recent scikit-learn versions may warn that the L1 argument is being renamed; follow the message.)

**P7 — Shallower trees** *(optional)*. Repeat Lab 3 Part 4 with `RandomForestClassifier(max_depth=3)`. How do the impurity importances and the test accuracy change? Explain.

**P8 — Reading** *(optional)*. Read Strobl et al. (2007) ([references](../references.md)). In two sentences, explain why impurity importance favours variables with many split points.

**P9 — Project proposal M1.** With your team, write the one-page proposal ([project brief](../../../course/project-brief.md)): question, dataset with verified licence and citation, unit of analysis (what "new data" is), intended methods, team roles, and one sentence on what would count as "the method helped". One member uploads it to the M1 assignment in Teams.
