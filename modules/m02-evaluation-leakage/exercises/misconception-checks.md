# Misconception checks — module m02 (formative, in lecture)

Use these with a show of hands or a polling tool (for example a Microsoft Forms quiz in the class team). Students answer individually, discuss in pairs for one minute, then re-vote. Each item names the misconception it targets. Answers and discussion notes are kept with the instructor material.

**MC1 — Grouped data** (lecture §2). A hospital has 8 chest images per patient for 300 patients. A classifier scores 0.95 in 5-fold cross-validation with rows split at random. The model will be used on new patients. Which statement is correct?
A. 0.95 is a fair estimate, because 5-fold CV uses every image · B. the estimate is probably optimistic; split by patient (`GroupKFold`) · C. use 10 folds instead of 5 · D. stratify the folds by diagnosis

**MC2 — Intervals** (lecture §3). On 25 test cases a new model is correct 23 times (0.92); the majority baseline is correct 22 times (0.88). Which conclusion is justified?
A. the new model is 4 points better · B. the new model is better, because 0.92 > 0.88 · C. the test set is too small to tell them apart · D. the baseline is better, because it is simpler

**MC3 — Unsupervised steps** (lecture §4.3). True or false: *"Standardising the features before cross-validation is fine, because the scaler never looks at the labels."* Explain in one sentence.

**MC4 — Test-set reuse** (lecture §4.2). A team tries 20 model settings, scores each on the same test set, and reports the best test score. The reported score is most likely:
A. unbiased · B. optimistic · C. pessimistic · D. unbiased if the test set is large

**MC5 — SMOTE** (lecture §5). A student applies SMOTE to the whole dataset, then runs 5-fold cross-validation and gets F1 = 0.99. Which is the main problem?
A. SMOTE should use more neighbours · B. synthetic points made from test cases are in the training folds, and the test folds no longer have the real class balance · C. F1 is the wrong metric for imbalance · D. nothing, if the folds are stratified

**MC6 — Target leakage** (lecture §6). To predict which customers will cancel a subscription next month, a model uses the column `days_since_cancellation_request`. Accuracy is 0.98. What is the most likely explanation?
A. an excellent model · B. the column is only known once the outcome has happened · C. the classes are imbalanced · D. too many features
