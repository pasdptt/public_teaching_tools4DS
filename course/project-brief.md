# Project brief

**Weight:** 25% · **Teams:** 5–6 students, at most 20 teams · **Workspace:** Google Colab, with the repository layout below.

## Goal

Answer one substantive question with a dataset of your choice using the course's tools. A good project shows that you can:

* use at least one **dimension-reduction or feature method** (selection, PCA, LDA, ICA, nonlinear embedding) **and**
* use at least one of **network analysis**, **smoothing and aggregation**, **high-performance computing** or **streaming**,
* inside a **valid evaluation design**, compared against a **simple baseline**, with honest **failure analysis**.

## Team roles

Each team names, in M1, one person responsible for each role. Roles rotate at least once (at M3), so that every member can explain any part of the code at the presentation.

| Role | Responsible for |
|---|---|
| Data steward | Source, licence, data audit, the loading code and its checksums |
| Evaluation lead | Splits, baselines, leakage checks, uncertainty |
| Methods lead (one or two people) | Dimension-reduction or feature methods; the second method family |
| Reproducibility lead | Seeds, environment, restart-and-run-all, the README rerun instructions |
| Report editor | Report, figures, AI-use log consolidation |

## Data requirements

* The data must be openly licensed or provided with written permission; state the licence and citation in M1.
* No personal or sensitive data without anonymisation and lecturer approval.
* Access must be reproducible: a public URL or a file you are allowed to share. Each data-loading cell records the download source and its checksum.
* Kaggle-only or login-only datasets need lecturer approval, because markers must be able to rerun your work.

## Milestones and deliverables

| Milestone | Teaching week | Weight | Deliverable | Must include |
|---|---|---|---|---|
| **M1** Proposal | 3 | 2% | One page (PDF or Markdown) | Question; dataset with licence and citation; unit of analysis; intended methods; team roles; one sentence on what would count as "the method helped" |
| **M2** Data audit and baseline | 6 | 5% | Colab notebook | Missing values and sentinels; duplicates; leakage risks (time, groups, graph); baseline with a valid protocol and uncertainty; restart-and-run-all clean |
| **M3** Method comparison | 10 | 6% | Colab notebook | Required methods (above) compared against the baseline; every fitted step inside validation; at least one failure analysis; anonymous peer-assessment form |
| **M4** Final repository and report | end of 12 | 8% | Repository (or zipped folder) plus a report of 8 pages or fewer | The layout below; README rerun instructions; AI-use appendix; anonymous peer-assessment form |
| **M5** Presentation and Q&A | adjustment week A2 | 4% | 8-minute live talk + 6-minute Q&A | The examiner picks **two members at random**; each explains a cell of the team's code that the examiner chooses |

## Individual marks

* **Project mark** = team mark × peer-assessment factor (between 0.8 and 1.1, from the anonymous forms at M3 and M4; the lecturer may override it).
* The **final examination** contains a 4-point individual reflection question about your own project.

## Required repository layout for M4

```
project/
├── README.md        question, data source with licence and citation, how to rerun (Colab link), results summary, team roles
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

Marking: [rubrics](rubrics.md).
