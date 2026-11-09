# Project brief [P]

**Weight:** 25% · **Teams:** 2–3 students (decision Q-A3) · **Workspace:** Google Colab, with the repository layout below.

## Goal

Answer one substantive question with a dataset of your choice using the course's tools. A good project shows that you can:

* use at least one **dimension-reduction or feature method** (selection, PCA, LDA, ICA, nonlinear embedding) **and**
* use at least one of **network analysis**, **smoothing and aggregation**, **high-performance computing** or **streaming**,
* inside a **valid evaluation design**, compared against a **simple baseline**, with honest **failure analysis**.

## Data requirements

* The data must be openly licensed or provided with written permission; state the licence and citation in M1.
* No personal or sensitive data without anonymisation and lecturer approval.
* Access must be reproducible: a public URL or a file you are allowed to share. Each data-loading cell records the download source and its checksum.
* Kaggle-only or login-only datasets need lecturer approval, because classmates and markers must be able to rerun your work.

## Milestones and deliverables

| Milestone | Week | Weight | Deliverable | Must include |
|---|---|---|---|---|
| **M1** Proposal | 4 | 2% | One page (PDF or Markdown) | Question; dataset with licence and citation; unit of analysis; intended methods; one sentence on what would count as "the method helped" |
| **M2** Data audit and baseline | 7 | 5% | Colab notebook | Missing values and sentinels; duplicates; leakage risks (time, groups, graph); baseline with a valid protocol and uncertainty; restart-and-run-all clean |
| **M3** Method comparison | 11 | 6% | Colab notebook | Required methods (above) compared against the baseline; every fitted step inside validation; at least one failure analysis |
| **M4** Final repository and report | 15 | 8% | Repository (or zipped folder) plus a report of 8 pages or fewer | The layout below; README rerun instructions; AI-use appendix |
| **M5** Presentation and oral defence | 15 | 4% | 10-minute team talk; 5-minute individual questions | Each member explains any cell the examiner chooses |

## Required repository layout for M4

```
project/
├── README.md        question, data source with licence and citation, how to rerun (Colab link), results summary
├── notebooks/       01_data_audit.ipynb, 02_baseline.ipynb, 03_methods.ipynb (each restart-and-run-all clean)
├── report.pdf       8 pages or fewer
└── ai-use.md        AI-use log for the whole project (see the AI policy)
```

## Report structure (8 pages or fewer)

1. Question and data (provenance, licence, unit of analysis).
2. Evaluation design (splits, baseline, metrics, uncertainty), with a justification of why it fits the data structure.
3. Methods (assumptions, parameter choices and the criterion used for each).
4. Results compared with the baseline.
5. Failure analysis: what went wrong, the evidence, the fix.
6. Limitations and what you would do next.

Marking: [rubrics](rubrics.md). The final examination's project-reflection item (4 points) is answered individually.
