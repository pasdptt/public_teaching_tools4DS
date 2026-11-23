# Rubrics

## Lab rubric (graded labs)

Each graded lab is marked out of 8 and scaled to 3⅓% of the course mark.

| Criterion | Max | How it is assessed | 4 Exemplary | 3 Proficient | 2 Developing | 1 Beginning |
|---|---|---|---|---|---|---|
| **Correctness and validity** | 3 | **Auto-checked** by hidden tests (fitted steps inside validation, correct values, baseline present) | All hidden tests pass | Minor failures that do not change conclusions | A validation flaw or a missing baseline | Leakage or a wrong method |
| **Reproducibility** | 1 | **Auto-checked**: restart-and-run-all in a fresh kernel; consecutive execution counts | Runs clean | Runs after a trivial fix | Runs only out of order | Does not run |
| **Failure analysis** | 2 | Written answer, at most 100 words, marked by staff | Diagnoses the mechanism and the fix with evidence | Identifies the failure and its fix | Names a failure without evidence | Missing |
| **Interpretation** | 2 | Written answer, at most 100 words, marked by staff | Precise; states limitations; separates visualisation from prediction | Mostly precise | Descriptive only | Missing or wrong |

**Converting levels to marks:** level 4 earns the criterion's maximum. Levels 3, 2 and 1 earn ¾, ½ and ¼ of it.

The visible self-checks help students but are not the grading tests. The hidden tests check the same properties on different inputs, so hard-coding an answer that passes a self-check does not earn the marks.

**How the two auto-checked criteria are scored.** The auto-checker re-runs each submitted notebook from top to bottom in a fresh Python session, then runs the hidden tests.

* **Correctness (3):** 3 × the share of hidden-test points passed, rounded down to a multiple of 0.25 (so any failed test costs at least 0.25). Each task's tests and their points are listed in the feedback, with the reason any test failed.
* **Reproducibility (1):** 1 if the fresh run has no errors and the submitted file was run top to bottom (execution counts 1, 2, 3, …); ¾ if the fresh run has no errors but the file was not restarted and run in order before submitting; ½ if exactly one cell fails in the fresh run; ¼ if more cells fail; 0 if the file cannot be opened or is a different lab.
* Staff review every flagged submission (a changed given or self-check cell, missing task cells, an answer over 100 words, an empty AI-use log) before marks are released.

## Project report rubric (M4, scaled to 8%)

| Criterion | Weight | Exemplary looks like |
|---|---|---|
| Problem framing and data provenance | 15% | A precise question; licence and citation verified; the unit of analysis and the population stated |
| Validity of the evaluation design | 25% | All fitted steps inside validation; splits match the data structure (time, groups, graph); baseline and uncertainty |
| Methodological depth and correctness | 20% | Methods justified by assumptions; parameters chosen by a stated criterion |
| Failure analysis and limitations | 15% | At least one failure found, diagnosed and fixed with evidence; limitations bound the claims |
| Reproducibility | 15% | A clean rerun from the README instructions; seeds; pinned environment; no hidden state |
| Communication | 10% | Claims supported by the reported outputs; clear figures; concise |

## Presentation and Q&A rubric (M5, 4%; team mark)

| Criterion | Weight | Evidence |
|---|---|---|
| Clarity and structure of the 8-minute talk | 30% | Question, design, results and limitations within time |
| Code explanation by two randomly chosen members | 50% | Each explains an examiner-chosen cell: what it does, why it is valid, what would break it |
| Handling of limitations and questions | 20% | Honest limits; answers grounded in the team's outputs |

Individual differentiation comes from the peer-assessment factor (0.8–1.1) and the individual reflection item in the final examination.
