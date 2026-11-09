# Syllabus — 040563107 Tools for Statistical Data Science

**Status:** decisions of 9 November 2026 applied ([decision log](../docs/decisions.md)). The schedule, learning outcomes and assessment formats are used **informally this term**; the formal TQF3 revision is deferred. The course description, credits and assessment weights are unchanged.

## Course information

| Item | Value | Source |
|---|---|---|
| Code and title | 040563107 เครื่องมือสำหรับวิทยาศาสตร์ข้อมูลเชิงสถิติ / Tools for Statistical Data Science | TQF3 |
| Programme | B.Sc. Applied Statistics, Faculty of Applied Science, KMUTNB; core courses of the major | TQF3 |
| Credits | 3 (2-3-5): 30 h lecture, 45 h practice, 75 h self-study | TQF3 |
| Semester and year | Semester 2, year 3 | TQF3 |
| Prerequisite / co-requisite | None (TQF3). Linear algebra and introductory statistical inference are **assumed**. | TQF3 |
| Instructor | Dr. Pasd Putthapipat (TQF3, 2/2563); to be confirmed for the coming term | TQF3 |
| Expected enrolment | About 100 students (lecturer, 9 Nov 2026) | Decision log |
| Workspace | Google Colab (primary); pinned local Python environment (fallback) | Decision log |

## Course description (TQF3, unchanged)

> การลดมิติข้อมูล การวิเคราะห์องค์ประกอบหลัก การวิเคราะห์องค์ประกอบที่เป็นอิสระ การหาคุณลักษณะพิเศษ การวิเคราะห์เครือข่าย การปรับเรียบและการรวมตัว การประยุกต์ใช้คอมพิวเตอร์สมรรถนะสูง สตรีมมิ่งอัลกอริทึมในการวิเคราะห์ชุดข้อมูลขนาดใหญ่
>
> Dimension reduction, principal component analysis, independent component analysis, feature extraction, network analysis, smoothing and aggregation, application of high performance computing and streaming algorithms to the analysis of large data sets.

## Course learning outcomes

| CLO | On completion, students can… |
|---|---|
| CLO1 | **derive and explain** PCA, LDA and ICA as optimisation problems (objective, constraints, solution, assumptions) and **compute** small cases by hand |
| CLO2 | **construct** reproducible Colab workflows in which every fitted operation is fitted inside the training folds, and **detect and correct** data leakage, including temporal and graph-specific leakage |
| CLO3 | **compare** feature-selection, feature-extraction and representation methods against simple baselines with appropriate resampling and uncertainty, distinguishing visualisation quality from predictive usefulness |
| CLO4 | **represent** relational data as graphs and **compute and interpret** paths, centrality and community structure relative to a null model |
| CLO5 | **apply** smoothing and temporal aggregation, **select** smoothing parameters by forward-chaining validation, and **compare** with naive baselines |
| CLO6 | **measure** computational cost and **apply** laptop-scale high-performance and one-pass streaming algorithms, quantifying the accuracy–resource trade-off |
| CLO7 | **communicate** an end-to-end analysis with limitations and failure analysis, and **document** AI assistance verifiably |

## Teaching pattern

* **12 teaching weeks**, each with a 2-hour lecture, a 3-hour lab in Colab and 5 hours of independent work.
* **3 adjustment weeks** for holidays, catch-up, and the project presentations.
* Every lab ends with a failure-analysis task and a written interpretation.
* Examinations are scheduled by the university outside the 15 weeks.

See the [schedule](schedule.md).

## Assessment (weights unchanged from the TQF3)

| Component | Weight | Summary |
|---|---|---|
| Practical work | 20% | Six graded labs (G1–G6), all count, 3⅓% each; code auto-checked, short written answers marked; other labs are practice |
| Project | 25% | Teams of 5–6 (at most 20 teams); milestones M1–M5; peer-assessment factor 0.8–1.1; live presentation with random-member Q&A |
| Midterm examination | 20% | In person, paper, closed book with one A4 double-sided sheet; covers teaching weeks 1–6 |
| Final examination | 35% | In person, paper; cumulative; includes a 4-point individual project-reflection item |

Details: [assessment](assessment.md) · [rubrics](rubrics.md) · [project brief](project-brief.md).

## Language

* Lectures are delivered in **Thai**.
* Slides, notebooks, code and technical terms are in **English**, with an [English–Thai glossary](glossary.md).
* Examination papers are **bilingual**: Thai instructions, English technical terms.

## Policies

* **AI assistance:** permitted in labs and the project with disclosure and verification; not permitted in examinations. See the [AI policy](ai-policy.md).
* **Academic integrity:** the faculty's existing regulations apply. This syllabus does not restate them.
* **Reproducibility:** submitted notebooks must run top to bottom in a fresh session (the "restart and run all" rule).
* **Missed graded labs, attendance and make-up examinations:** *to be set by the lecturer in line with university regulations.* All six graded labs count, so an excused-absence rule is needed.

## Scope notes

* **Class imbalance (e.g. SMOTE)** appears only inside the evaluation module, as an example of resampling as a fitted operation; it is not a standalone topic.
* **Distributed computing (Spark)** is out of scope; it belongs to 040563105. High-performance computing is taught at laptop scale.

## References

Module reading lists replace general texts. Every reference is checked against its DOI before it is assigned; see, for example, [`../modules/m04-pca/references.md`](../modules/m04-pca/references.md).

TQF3 recommended texts, retained as supplementary:
* C. Severance, *Python for Everybody: Exploring Data in Python 3*, 2016.
* C. N. Knaflic, *Storytelling with Data*, Wiley, 2015.

## Licence of these materials

Code is released under the MIT licence; text and teaching materials under CC BY 4.0. See [`../LICENSE`](../LICENSE) and [`../LICENSE-CONTENT.md`](../LICENSE-CONTENT.md).
