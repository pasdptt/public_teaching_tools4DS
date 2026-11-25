# Module m06 — Nonlinear and learned representations (bounded)

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Built** (25 Nov 2026): lecture, Lab 6, exercises, references, execution report. The Thai-text segment waits for a verified corpus (backlog B20) | No (practice; includes an AI-audit task) | B11 | CLO1, CLO3 | see the [schedule](../../course/schedule.md) |

**Workspace:** Google Colab (open the lab with the badge below); a pinned local environment is the fallback.

| Material | Link |
|---|---|
| **Lecture slides** (21 slides, for projection; match the outline section for section) | [m06 lecture deck](https://claude.ai/artifact/2WT3SBevvPAYmwKyn42mbh) |
| Lecture outline (2 h, with timings and worked examples) | [`lecture/outline.md`](lecture/outline.md) |
| Lab 6 — Nonlinear and learned representations (practice, with an AI-audit task; run-through in the session, then redone as homework) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m06-nonlinear-representations/lab/lab6_nonlinear_representations.ipynb) [`lab/lab6_nonlinear_representations.ipynb`](lab/lab6_nonlinear_representations.ipynb) |
| Problem set (independent work) | [`exercises/problem-set.md`](exercises/problem-set.md) |
| Misconception checks (in lecture) | [`exercises/misconception-checks.md`](exercises/misconception-checks.md) |
| References (each verified against its DOI record, or as stated) | [`references.md`](references.md) |
| Execution report | [`EXECUTION-REPORT.md`](EXECUTION-REPORT.md) |

The solution, answer keys and marking notes are kept in the private instructor material.

## Objectives

By the end of this module a student can:

| ID | Objective (observable) | Evidence |
|---|---|---|
| m06-O1 | **Explain** what kernel PCA, Isomap, LLE and t-SNE each preserve, and **why** t-SNE is not a feature extractor. | Lab 6 T1, T3, Q1–Q2; problem set P4; final item 3 |
| m06-O2 | **Compute** trustworthiness and held-out k-NN accuracy to **separate** visualisation quality from predictive usefulness. | Lab 6 T1–T2, Q1; problem set P1 |
| m06-O3 | **Train** a small CPU autoencoder with a correct output layer and loss, and **compare** its reconstruction error with PCA. | Lab 6 T4–T5, Q3; problem set P2–P3 |
| m06-O4 | **Evaluate** precomputed pretrained embeddings of Thai text as features against a baseline. | **Waits for backlog B20** (a Thai corpus with a verified open licence); not yet taught or assessed |

## Lecture (2 h per teaching week)

* Kernel PCA, Isomap, LLE, t-SNE: what is preserved, what is not
* Trustworthiness and neighbourhood preservation
* A picture is not a feature: held-out prediction and the AI-audit case
* Autoencoders as nonlinear PCA (one bounded session; CPU only)
* Pretrained embeddings as a modern representation (concept only until B20 is done)

## Lab (3 h per teaching week)

**Lab 6 (practice):** PCA, Isomap and t-SNE views of the digits with trustworthiness; held-out 5-NN accuracy of 2-D and 10-D representations; an AI-generated pipeline that uses t-SNE coordinates as features; linear and tanh autoencoders (`MLPRegressor`, CPU, about 15 s) against PCA on held-out reconstruction error; the softmax output bound. Five tasks with self-checks, three written answers.

**Failure analysis (required in every lab):** the softmax autoencoder of the old notebook (audit M9): any softmax output has test MSE of at least 0.085, over four times PCA(10)'s 0.020. **AI-audit task:** t-SNE coordinates as features (audit M11): 0.99 accuracy within one t-SNE run, 0.29 on a second run of the same images.

## Independent work (5 h per teaching week)

Redo Lab 6 on your own (1.5 h); midterm revision (3.5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Digits (registry) | CC BY 4.0 (verified) |
| Openly licensed Thai text corpus, embeddings precomputed once | **To source and verify** (backlog B20; decision D25) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| FeatureExtraction notebook (N05): LLE, t-SNE, autoencoder parts | Revised and bounded: the loss is fixed (M9); t-SNE for display only (M11); transductive fits named (E3) |

## Assessment links

Practice lab; final item 3 (examined in the final, not the midterm).

## Production notes

No additional dependencies: the autoencoder is scikit-learn's `MLPRegressor` (no TensorFlow, no GPU). The Thai-text segment (objective m06-O4) is added when backlog B20 provides a corpus with a verified licence and CPU-precomputed embeddings.
