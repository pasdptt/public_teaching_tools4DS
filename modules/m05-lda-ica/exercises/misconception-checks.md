# Misconception checks — module m05 (formative, in lecture)

Use these with a show of hands or a polling tool (for example a Microsoft Forms quiz in the class team). Students answer individually, discuss in pairs for one minute, then re-vote. Each item names the misconception it targets. Answers and discussion notes are kept with the instructor material.

**MC1 — K − 1 directions** (lecture §1). A dataset has 50 variables and 4 classes. How many discriminant directions can LDA find?
A. 50 · B. 4 · C. 3 · D. as many as there are observations

**MC2 — Labels** (lecture §2). Which reduction uses the class labels?
A. PCA · B. LDA · C. ICA · D. all three

**MC3 — LDA before the split** (lecture §2). True or false: *"LDA is only a linear transformation, so fitting it on all the data before cross-validation is harmless."* Explain in one sentence.

**MC4 — Ambiguities** (lecture §3). FastICA returns a recovered component that is −2 times the true source. Is the method wrong?
A. yes: the scale should be 1 · B. yes: the sign is wrong · C. no: ICA cannot determine scale or sign · D. no, but only because the data were whitened

**MC5 — Gaussian sources** (lecture §5). ICA is applied to mixtures of three independent Gaussian sources. What will happen?
A. perfect recovery, because the sources are independent · B. the components are arbitrary rotations; different runs disagree · C. ICA returns the PCA components exactly · D. ICA cannot run at all

**MC6 — Uncorrelated vs independent** (lecture §3). After whitening, the components are uncorrelated with unit variance. True or false: *"So they are independent, and ICA has nothing left to do."* Explain.
