# Assessment

The weights are unchanged from the TQF3: **practical work 20%, project 25%, midterm 20%, final 35%**. The formats below were decided on 9 November 2026 ([decision log](../docs/decisions.md)).

## Practical work (20%): six graded labs, all count

| Graded lab | Module | Weight |
|---|---|---|
| G1 | [m02 Evaluation and leakage](../modules/m02-evaluation-leakage/) | 3⅓% |
| G2 | [m04 PCA, Lab 4B](../modules/m04-pca/) | 3⅓% |
| G3 | [m05 LDA and ICA](../modules/m05-lda-ica/) | 3⅓% |
| G4 | [m07 Networks, Lab 7B](../modules/m07-networks/) | 3⅓% |
| G5 | [m08 Smoothing and temporal evaluation](../modules/m08-smoothing-temporal/) | 3⅓% |
| G6 | [m10 Streaming (with an HPC task)](../modules/m10-streaming/) | 3⅓% |

* **Marking is designed for about 100 students.**
  * Code tasks are **auto-checked** by hidden tests, alongside the visible self-checks.
  * A restart-and-run-all check is automated.
  * Short written answers (at most 100 words each) are marked with the [lab rubric](rubrics.md#lab-rubric-graded-labs).
  * Each graded lab is marked out of 8 and scaled to 3⅓%.
* **All other labs are practice labs.** They are not graded; they have self-checks, and their solutions are discussed in class.
* **Missing a graded lab:** all six count, so a make-up or excused-absence rule is needed. *To be set by the lecturer under university regulations.*

## Project (25%)

* **Teams:** 5–6 students, with **at most 20 teams**.
* **Individual marks:** the team mark is multiplied by a **peer-assessment factor between 0.8 and 1.1**, collected anonymously at M3 and M4. The lecturer may override it.

| Milestone | Teaching week | Weight | Deliverable |
|---|---|---|---|
| M1 Proposal | 3 | 2% | One page: question, dataset with verified licence and citation, unit of analysis, intended methods, team roles |
| M2 Data audit and baseline | 6 | 5% | Colab notebook: data audit (missingness, sentinels, leakage risks) and a baseline with a valid protocol and uncertainty |
| M3 Method comparison | 10 | 6% | At least one dimension-reduction or feature method **and** at least one of network / smoothing / HPC / streaming, against the baseline, with failure analysis |
| M4 Final repository and report | end of 12 | 8% | Reproducible notebooks and a report of 8 pages or fewer, with an AI-use appendix |
| M5 Presentation and Q&A | adjustment week A2 | 4% | 8-minute live talk + 6-minute Q&A in which **two randomly chosen members** explain code cells |

Full requirements: [project brief](project-brief.md).

## Examinations

Both examinations are **in person, on paper**: closed book, with one A4 sheet of notes (both sides). No AI tools or internet. Papers are **bilingual**: Thai instructions with English technical terms. There are **no bonus points**, and papers are written fresh each term from a private item bank.

### Midterm (20 points = 20%; covers teaching weeks 1–6, may be adjusted)

| Item | Type | CLO | Points |
|---|---|---|---|
| 1 | Hand computation: summary statistics with a sentinel value; 2×2 covariance → eigenvalues, explained variance, PC1 | 1 | 5 |
| 2 | Derivation: PCA variance maximisation, *or* the LDA Fisher criterion | 1 | 5 |
| 3 | Code review: find and fix the leakage in a short printed excerpt | 2 | 4 |
| 4 | Interpretation: scree and loadings output; selection vs extraction | 3 | 3 |
| 5 | PCA vs ICA on a described mixing scenario | 1 | 3 |

### Final (35 points = 35%; cumulative: 11 points weeks 1–6, 24 points week 7 onwards)

| Item | Type | CLO | Points |
|---|---|---|---|
| 1 | PCA, LDA or ICA computation and interpretation | 1 | 6 |
| 2 | Validation design for a new scenario, including grouped or temporal splits | 2, 3 | 5 |
| 3 | Visualisation vs predictive usefulness of a nonlinear embedding (week 7) | 3 | 4 |
| 4 | Network: Dijkstra by hand with a correctness justification; centrality against a null model | 4 | 5 |
| 5 | Smoothing: SES or EWMA by hand; parameter choice; temporal leakage | 5 | 5 |
| 6 | Streaming and HPC: Welford, reservoir or Count-Min reasoning; complexity and memory trade-off | 6 | 6 |
| 7 | **Individual project reflection** | 7 | 4 |
