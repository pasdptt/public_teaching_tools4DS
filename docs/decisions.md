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
| D12 (Q-A4) | Practical work | **Six graded labs, all count (3⅓% each)**: code auto-checked by hidden tests, short written answers (at most 100 words) marked with the rubric; other labs are practice | Assessment, rubrics, module status tables; PCA Lab 4B graded (G2), Lab 4A practice | Build hidden-test auto-checking (backlog B19); set the rule for missed graded labs |
| D13 (Q-A2) | Project reflection item in the final | **Keep, 4 points** | Final blueprint unchanged | — |
| D14 | Midterm coverage | **Teaching weeks 1–6** ("leave room to adjust") | Assessment; nonlinear representations (week 7) examined in the final | — |
| D15 (Q-S2) | Class imbalance / SMOTE | **Only inside the evaluation module**, as an example of a fitted operation | Module m02, syllabus scope notes | — |
| D16 (Q-S3) | Spark | **Leave out entirely** (it belongs to 040563105) | Module m09; the old PCA-on-Spark notebook retired | — |
| D17 (Q-AI1) | AI assistance in labs and the project | **Allowed with disclosure** (AI-use log; explain any cell) | AI policy | — |
| D18 (Q-R1) | Licences for this public repository | **MIT for code, CC BY 4.0 for teaching content** | `LICENSE`, `LICENSE-CONTENT.md` | Confirm the copyright holder name ("Pasd Putthapipat" assumed) and whether KMUTNB policy requires a different holder |
| D19 (Q-D2) | Embeddings example in module m06 | **An openly licensed Thai text corpus** | Module m06 | Find a corpus with a verified open licence, precompute embeddings on CPU, add it to the registry, and seek lecturer approval |
| D20 | How labs are held (one session or sections) | **Not decided yet** | Materials kept neutral (Colab in the browser works either way) | Decide with the department |
