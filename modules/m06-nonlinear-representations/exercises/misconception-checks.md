# Misconception checks — module m06 (formative, in lecture)

Use these with a show of hands or a polling tool (for example a Microsoft Forms quiz in the class team). Students answer individually, discuss in pairs for one minute, then re-vote. Each item names the misconception it targets. Answers and discussion notes are kept with the instructor material.

**MC1 — Reading a t-SNE plot** (lecture §2). In a t-SNE plot of customers, cluster A is far from cluster B, and cluster C looks twice as large as the others. What can you safely conclude?
A. A and B are the most different groups · B. C has the most variation · C. points within one cluster are similar to each other · D. all of A–C

**MC2 — Trustworthiness** (lecture §3). A 2-D view has trustworthiness 0.99 at $k = 10$. What does that tell you?
A. features from this view will predict well · B. the view brings together few points that are far apart in the original space · C. all distances are preserved · D. the classes are well separated

**MC3 — t-SNE features** (lecture §4). True or false: *"Using t-SNE coordinates fitted on all the data as features is fine, as long as the classifier is evaluated with cross-validation."* Explain in one sentence.

**MC4 — Linear autoencoder** (lecture §5). A linear autoencoder with a 10-unit code is trained with squared error on the same training images as PCA(10). Its test reconstruction error is:
A. lower than PCA's, because it is a neural network · B. at best equal to PCA's · C. always higher than PCA's · D. not comparable with PCA's

**MC5 — Output layer** (lecture §5). The inputs are standardised (mean 0, sd 1, many negative values). Which output layer should the autoencoder use?
A. softmax · B. sigmoid · C. identity (linear) · D. ReLU

**MC6 — Transforming new points** (lecture §1). In scikit-learn, which of these can map **new** observations after fitting: PCA, kernel PCA, Isomap, LLE, t-SNE?
A. only PCA · B. PCA and kernel PCA · C. all except t-SNE · D. all five
