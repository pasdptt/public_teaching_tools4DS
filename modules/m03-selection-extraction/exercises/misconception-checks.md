# Misconception checks — module m03 (formative, in lecture)

Use these with a show of hands or a polling tool (for example a Microsoft Forms quiz in the class team). Students answer individually, discuss in pairs for one minute, then re-vote. Each item names the misconception it targets. Answers and discussion notes are kept with the instructor material.

**MC1 — Distances in high dimension** (lecture §1). A 1-nearest-neighbour classifier works well with 5 informative features. 995 pure-noise features are added. What happens most likely?
A. nothing: the nearest neighbour is still the most similar case · B. accuracy drops, because noise dimensions swamp the distances · C. accuracy rises, because there is more information · D. it depends only on the number of cases

**MC2 — What extraction saves** (lecture §2). A hospital wants to measure fewer blood markers per patient. Which reduction helps?
A. PCA to 5 components · B. selecting 5 of the markers · C. either: both give 5 variables · D. neither

**MC3 — Selection inside CV** (lecture §3). True or false: *"RFE is a wrapper method, so it can be run once on the whole dataset before cross-validation without bias."* Explain in one sentence.

**MC4 — One run's selected set** (lecture §4). A report says: "LASSO selected age, income and region, so these are the three drivers of churn." Which is the most important missing information?
A. the value of the penalty · B. how often each variable is selected when the data are resampled · C. the number of iterations · D. the software version

**MC5 — Impurity importance** (lecture §5). A random forest ranks `customer_id` (a unique number per customer) as the most important feature. The most likely explanation is:
A. customers with high IDs behave differently · B. impurity importance favours variables with many distinct values · C. the forest needs more trees · D. IDs carry hidden information about the outcome

**MC6 — Importance on training data** (lecture §5). Permutation importance computed on the **training** data says a noise feature matters (0.28). On the test data it is 0. Which number describes how the model will use the feature on new cases?
A. the training value · B. the test value · C. their average · D. neither: permutation importance is meaningless
