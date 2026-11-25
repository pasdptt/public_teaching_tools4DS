# Module m05 — Supervised vs unsupervised extraction: LDA and ICA

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Built** (25 Nov 2026): lecture, Lab 5 with hidden tests, exercises, references, execution report | **Yes — graded lab G3** | B09 | CLO1, CLO2, CLO3 | see the [schedule](../../course/schedule.md) |

**Workspace:** Google Colab (open the lab with the badge below); a pinned local environment is the fallback.

| Material | Link |
|---|---|
| **Lecture slides** (22 slides, for projection; match the outline section for section) | [m05 lecture deck](https://claude.ai/artifact/4iBUWamfM5VpLR3oh2tZkS) |
| Lecture outline (2 h, with timings and worked examples) | [`lecture/outline.md`](lecture/outline.md) |
| Lab 5 — LDA and ICA (**graded lab G3**; run-through in the session, then done as homework and submitted in Teams) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m05-lda-ica/lab/lab5_lda_ica.ipynb) [`lab/lab5_lda_ica.ipynb`](lab/lab5_lda_ica.ipynb) |
| Problem set (independent work; midterm practice) | [`exercises/problem-set.md`](exercises/problem-set.md) |
| Misconception checks (in lecture) | [`exercises/misconception-checks.md`](exercises/misconception-checks.md) |
| References (each verified against its DOI record) | [`references.md`](references.md) |
| Execution report | [`EXECUTION-REPORT.md`](EXECUTION-REPORT.md) |

The solution, hidden tests, answer keys and marking notes are kept in the private instructor material.

## Objectives

By the end of this module a student can:

| ID | Objective (observable) | Evidence |
|---|---|---|
| m05-O1 | **Derive** Fisher's criterion, **solve** the generalised eigenproblem and **explain** the bound of at most K − 1 directions. | Lab 5 T1, Q1; problem set P1–P2; midterm item 2 |
| m05-O2 | **State** the ICA model, the role of whitening, and why non-Gaussianity identifies the sources. | Lab 5 Q3; problem set P3 |
| m05-O3 | **Recover** known sources from linear mixtures with FastICA and **compare** with PCA. | Lab 5 T4; midterm item 5 |
| m05-O4 | **Demonstrate** ICA's identifiability failure with Gaussian sources and **name** the remaining ambiguities (scale, sign, order). | Lab 5 T5, Q4; problem set P4 |
| m05-O5 | **Fit** LDA inside a pipeline and **compare** LDA+classifier with PCA+classifier against a baseline. | Lab 5 T2–T3, Q2 |

## Lecture (2 h per teaching week)

* LDA: Fisher criterion, generalised eigenproblem, K−1 directions, LDA as classifier vs projection
* ICA: latent-source model, whitening, non-Gaussianity (kurtosis, negentropy), FastICA
* Identifiability; PCA vs ICA on the same mixtures

## Lab (3 h per teaching week)

**Graded lab G3 (Lab 5):** Fisher directions from the generalised eigenproblem (checked against scikit-learn); LDA(2) vs PCA(2) features on Wine against baselines; LDA fitted before the split on noise; blind source separation of three known signals (FastICA vs PCA); Gaussian sources. Five tasks with self-checks and hidden tests, four written answers.

**Failure analysis (required in every lab):** Gaussian sources (recovery about 0.80 for every seed, and runs disagree), and LDA fitted before the split (0.810 on noise vs 0.310 inside; audit E1).

## Independent work (5 h per teaching week)

Lab 5 and submit it (2 h); midterm revision with the [problem set](exercises/problem-set.md) (1.5 h); **project M2** data audit and baseline (1.5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Synthetic source signals and noise (generated in the lab with the course seed) | n/a |
| Wine (registry) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| FeatureExtraction notebook (N05): ICA and LDA parts | Revise: replace ICA on one-hot mushroom data (M8); derive LDA (M10); fit inside the pipeline (E1) |
| Mushroom data (D06) | Retire as a comparison benchmark (ceiling effect, E5); keep only as a 'too-easy data' case |

## Assessment links

**Graded lab G3**; midterm items 2 and 5; **project M2 due** this week.

## Production notes

No additional dependencies. Hidden tests for G3: private repository, `grading/hidden/m05-lda-ica/`.
