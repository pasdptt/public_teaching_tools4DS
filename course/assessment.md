# Assessment [P]

The weights are unchanged from the TQF3: **practical work 20%, project 25%, midterm 20%, final 35%**. The formats and the internal breakdown are proposals.

## Practical work (20%)

* There are 14 labs. **L1** (week 1) is a pass/fail prerequisite. **L2–L14** are graded; the best **10 of 13** count, at 2% each.
* Each graded lab is marked out of 8 with the [lab rubric](rubrics.md#lab-rubric-each-graded-lab-8--2): correctness and validity 3, reproducibility 1, failure analysis 2, interpretation 2.
* A submission must run top to bottom after a restart, and must include the AI-use log ([AI policy](ai-policy.md)).

## Project (25%)

| Milestone | Week due | Weight | Deliverable |
|---|---|---|---|
| M1 Proposal | 4 | 2% | One page: question, dataset with verified licence and citation, unit of analysis, intended methods |
| M2 Data audit and baseline | 7 | 5% | Colab notebook: data audit (missingness, sentinels, leakage risks) and a baseline with a valid protocol and uncertainty |
| M3 Method comparison | 11 | 6% | At least one dimension-reduction or feature method **and** at least one of network / smoothing / HPC / streaming, against the baseline, with failure analysis |
| M4 Final repository and report | 15 | 8% | Reproducible notebooks and a report of 8 pages or fewer, with an AI-use appendix |
| M5 Presentation and oral defence | 15 | 4% | 10-minute team presentation, then 5 minutes of individual questions on the team's code |

Individual marks are adjusted by the M5 oral score and a peer-assessment factor between 0.8 and 1.1 (decision Q-A3). Full requirements: [project brief](project-brief.md).

## Examinations

Both examinations are **in person**, closed book, with one A4 sheet of notes (both sides). The format of the A4 sheet continues current practice. No AI tools or internet access are permitted. There are **no bonus points**.

### Midterm (20 points = 20%; covers weeks 1–7)

| Item | Type | CLO | Points |
|---|---|---|---|
| 1 | Hand computation: summary statistics with a sentinel value; 2×2 covariance → eigenvalues, explained variance, PC1 | 1 | 5 |
| 2 | Derivation: PCA variance maximisation, *or* the LDA Fisher criterion | 1 | 5 |
| 3 | Code review: find and fix the leakage in a short printed excerpt | 2 | 4 |
| 4 | Interpretation: scree and loadings output; selection vs extraction | 3 | 3 |
| 5 | PCA vs ICA on a described mixing scenario | 1 | 3 |

### Final (35 points = 35%; cumulative: 11 points pre-midterm, 24 post-midterm)

| Item | Type | CLO | Points |
|---|---|---|---|
| 1 | PCA, LDA or ICA computation and interpretation (pre-midterm) | 1 | 6 |
| 2 | Validation design for a new scenario, including grouped or temporal splits (pre-midterm) | 2, 3 | 5 |
| 3 | Visualisation vs predictive usefulness of a nonlinear embedding | 3 | 4 |
| 4 | Network: Dijkstra by hand with a correctness justification; centrality against a null model | 4 | 5 |
| 5 | Smoothing: SES or EWMA by hand; parameter choice; temporal leakage | 5 | 5 |
| 6 | Streaming and HPC: Welford, reservoir or Count-Min reasoning; complexity and memory trade-off | 6 | 6 |
| 7 | Individual project reflection | 7 | 4 |

Papers are written fresh each term from a private item bank. No item is reused verbatim across terms.
