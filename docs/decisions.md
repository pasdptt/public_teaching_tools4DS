# Decision log

Decisions taken by the course lecturer on **9 November 2026**, in answer to the open questions in [blueprint §10.1](blueprint/03-curriculum-blueprint.md#101-decisions-requiring-the-lecturer-with-my-recommendation) and the follow-up questions they raised. Where a decision differs from the blueprint's proposal, **this log takes precedence**. The operational documents in [`../course/`](../course/) reflect it.

| ID | Question | Decision | What changed | Follow-up |
|---|---|---|---|---|
| D1 (Q-R1) | Where instructor-only material lives | **A private GitHub repository** (created by the lecturer; access on request) | `/instructor` stays git-ignored here; staff clone the private repository into it. **Done 11 Nov 2026:** material moved, and the private repository's own CI runs the solution and mutation tests against this repository | — |
| D2 (Q-L1) | Teaching language | **Lectures in Thai; slides, notebooks and technical terms in English; bilingual examination papers** | Syllabus, assessment, glossary | Confirm the proposed Thai renderings in the glossary |
| D3 (Q-A1) | Examination mode | **In person, on paper**: closed book with one A4 sheet; no AI or internet; fresh paper each term | Assessment | — |
| D4 (Q-D1) | Thai local-government revenue file | **Lecturer to confirm source and licence later**; kept out of public materials until then | None (labs use UCI Wine) | Lecturer sends the source |
| D5 (Q-S1) | Revised schedule vs approved TQF3 plan | **Adopt informally this term**; formal TQF3 revision deferred | Status notes in the syllabus and schedule | Prepare the TQF3 revision later |
| D6 | Teaching weeks | **About 12 teaching weeks; keep 3 weeks as adjustment room** | 12 + 3 schedule. The intro and the Python/SQL refresher are merged (m01); smoothing and temporal evaluation are merged into one week (m08) | — |
| D7 | Module naming | Module folders named **by topic sequence (`m01`–`m11`)**, with week numbers only in `course/schedule.md`, so weeks can move without renaming | All module folders renamed; PCA labs become Lab 4A / 4B | — |
| D8 | Class size | **About 100 students** (30–40 two years ago) | Marking and project design scaled | — |
| D9 (Q-A3) | Project teams | **Teams of 5–6, at most 20 teams**, with named, rotating roles | Project brief, assessment | — |
| D10 | Individual project marks | **Peer-assessment factor 0.8–1.1** (anonymous forms at M3 and M4; lecturer override) | Project brief, rubrics | Prepare the peer-assessment form |
| D11 | Presentations | **Live, in one adjustment week**: up to 20 teams × 15 min (8-minute talk + 6-minute Q&A in which two randomly chosen members explain code) | Module m11, rubrics; individual 5-minute orals dropped | — |
| D12 (Q-A4) | Practical work | **Six graded labs, all count (3⅓% each)**: code auto-checked by hidden tests, short written answers (at most 100 words) marked with the rubric; other labs are practice | Assessment, rubrics, module status tables; PCA Lab 4B graded (G2), Lab 4A practice | Auto-checker built for G2 (backlog B19, 23 Nov 2026); scoring rule confirmed (D21); missed-lab rule set (D22) |
| D13 (Q-A2) | Project reflection item in the final | **Keep, 4 points** | Final blueprint unchanged | — |
| D14 | Midterm coverage | **Teaching weeks 1–6** ("leave room to adjust") | Assessment; nonlinear representations (week 7) examined in the final | — |
| D15 (Q-S2) | Class imbalance / SMOTE | **Only inside the evaluation module**, as an example of a fitted operation | Module m02, syllabus scope notes | — |
| D16 (Q-S3) | Spark | **Leave out entirely** (it belongs to 040563105) | Module m09; the old PCA-on-Spark notebook retired | — |
| D17 (Q-AI1) | AI assistance in labs and the project | **Allowed with disclosure** (AI-use log; explain any cell) | AI policy | — |
| D18 (Q-R1) | Licences for this public repository | **MIT for code, CC BY 4.0 for teaching content** | `LICENSE`, `LICENSE-CONTENT.md` | Holder confirmed 24 Nov 2026 (D24) |
| D19 (Q-D2) | Embeddings example in module m06 | **An openly licensed Thai text corpus** | Module m06 | Find a corpus with a verified open licence and precompute embeddings on CPU; the lecturer approved the approach on 24 Nov 2026 (D25) |
| D20 | How labs are held | **Decided 24 Nov 2026 (D26)** | See D26 | — |

## Decisions of 24 November 2026

| ID | Question | Decision | What changed | Follow-up |
|---|---|---|---|---|
| D21 | Auto-checker scoring rule | **Confirmed**: correctness = 3 × the share of hidden-test points, rounded down to 0.25; reproducibility levels 1 / ¾ / ½ / ¼ / 0 as in the [lab rubric](../course/rubrics.md#lab-rubric-graded-labs) | Rubric (already stated) | — |
| D22 | Late or missed graded labs | **Late submissions are accepted; a graded lab that is not submitted scores 0** | Assessment, getting started | No late penalty was set. Announce the final cut-off after which a lab counts as not submitted |
| D23 | Submission channel | **Microsoft Teams** (assignment per lab; upload the `.ipynb`) | Getting started, assessment | Create the class team and one assignment per graded lab |
| D24 | Copyright holder | **Pasd Putthapipat**, for academic purposes | `LICENSE`, `LICENSE-CONTENT.md` (holder unchanged; purpose noted) | If "academic purposes" is meant to forbid commercial reuse, switch the content licence to CC BY-NC 4.0 |
| D25 | Thai text corpus for m06 (D19) and the Thai revenue file (D4) | **Approved** | Backlog B20 can proceed | The lecturer still sends the revenue file's source; the corpus licence must be verified before use |
| D26 (D20) | How labs are held | **The lab session is a guided run-through** of the lab with the lecturer; students then **do the lab again on their own as homework** and submit it | Schedule, syllabus, getting started, assessment; m01 lecture, lab, problem set and run sheet | For graded labs, decide how much of the graded tasks the run-through may show (recommendation: run through on a parallel example and leave the graded tasks for homework) |
| — | Calendar dates, peer-assessment form, glossary review | **Left for now** | — | Revisit before week 3 (project M1) |
