# Syllabus — 040563107 Tools for Statistical Data Science

**Status:** draft for lecturer approval. Items marked **[P]** are proposals that change the approved TQF3 (2/2563) and need the department's TQF revision process.

## Course information

| Item | Value | Source |
|---|---|---|
| Code and title | 040563107 เครื่องมือสำหรับวิทยาศาสตร์ข้อมูลเชิงสถิติ / Tools for Statistical Data Science | TQF3 |
| Programme | B.Sc. Applied Statistics, Faculty of Applied Science, KMUTNB; core courses of the major | TQF3 |
| Credits | 3 (2-3-5): 30 h lecture, 45 h practice, 75 h self-study | TQF3 |
| Semester and year | Semester 2, year 3 | TQF3 |
| Prerequisite / co-requisite | None (TQF3). Linear algebra and introductory statistical inference are **assumed** (blueprint §10.2). | TQF3 |
| Instructor | Dr. Pasd Putthapipat (TQF3, 2/2563); to be confirmed for the coming term | TQF3 |
| Workspace | Google Colab (primary); pinned local Python environment (fallback) | Lecturer decision |

## Course description (TQF3, unchanged)

> การลดมิติข้อมูล การวิเคราะห์องค์ประกอบหลัก การวิเคราะห์องค์ประกอบที่เป็นอิสระ การหาคุณลักษณะพิเศษ การวิเคราะห์เครือข่าย การปรับเรียบและการรวมตัว การประยุกต์ใช้คอมพิวเตอร์สมรรถนะสูง สตรีมมิ่งอัลกอริทึมในการวิเคราะห์ชุดข้อมูลขนาดใหญ่
>
> Dimension reduction, principal component analysis, independent component analysis, feature extraction, network analysis, smoothing and aggregation, application of high performance computing and streaming algorithms to the analysis of large data sets.

## Course learning outcomes [P]

| CLO | On completion, students can… |
|---|---|
| CLO1 | **derive and explain** PCA, LDA and ICA as optimisation problems (objective, constraints, solution, assumptions) and **compute** small cases by hand |
| CLO2 | **construct** reproducible Colab workflows in which every fitted operation is fitted inside the training folds, and **detect and correct** data leakage, including temporal and graph-specific leakage |
| CLO3 | **compare** feature-selection, feature-extraction and representation methods against simple baselines with appropriate resampling and uncertainty, distinguishing visualisation quality from predictive usefulness |
| CLO4 | **represent** relational data as graphs and **compute and interpret** paths, centrality and community structure relative to a null model |
| CLO5 | **apply** smoothing and temporal aggregation, **select** smoothing parameters by forward-chaining validation, and **compare** with naive baselines |
| CLO6 | **measure** computational cost and **apply** laptop-scale high-performance and one-pass streaming algorithms, quantifying the accuracy–resource trade-off |
| CLO7 | **communicate** an end-to-end analysis with limitations and failure analysis, and **document** AI assistance verifiably |

The mapping to the TQF3 learning domains (1.1, 2.1, 2.2, 3.1, 3.2, 4.1, 5.1, 5.2) is in blueprint §4 and §6.

## Teaching pattern

* **Each week:** a 2-hour lecture, a 3-hour lab in Colab, and 5 hours of independent work.
* **Every lab** ends with a failure-analysis task and a written interpretation.
* **Examinations** are scheduled by the university in the midterm and final periods, outside the 15 teaching weeks.

See the [schedule](schedule.md).

## Assessment (weights unchanged from the TQF3)

| Component | Weight | Summary |
|---|---|---|
| Practical work | 20% | Labs L2–L14; best 10 of 13 count (2% each); L1 is a pass/fail prerequisite **[P]** |
| Project | 25% | Teams of 2–3; five milestones M1–M5 **[P]** |
| Midterm examination | 20% | In person; closed book with one A4 double-sided sheet; weeks 1–7 **[P: examination mode]** |
| Final examination | 35% | In person; closed book with one A4 double-sided sheet; cumulative, about 30% pre-midterm and 70% post-midterm |

Details: [assessment](assessment.md) · [rubrics](rubrics.md) · [project brief](project-brief.md).

## Policies

* **AI assistance:** permitted in labs and the project with disclosure and verification; not permitted in examinations. See the [AI policy](ai-policy.md).
* **Academic integrity:** the faculty's existing regulations apply. This syllabus does not restate them.
* **Reproducibility:** submitted notebooks must run top to bottom in a fresh session (the "restart and run all" rule).
* **Late work, attendance and make-up examinations:** *to be set by the lecturer in line with university regulations (not specified here).*

## Language

English technical terms are used in all materials, with an [English–Thai glossary](glossary.md). The language of lecture delivery and of examinations is a lecturer decision (blueprint Q-L1).

## References

**Course texts [P]:** module reading lists replace the TQF3's general texts. Each module lists its references, and every reference is checked against its DOI before it is assigned. The PCA module's list is in [`../modules/w05-w06-pca/references.md`](../modules/w05-w06-pca/references.md).

**TQF3 recommended texts (retained as supplementary):**
* C. Severance, *Python for Everybody: Exploring Data in Python 3*, 2016.
* C. N. Knaflic, *Storytelling with Data*, Wiley, 2015.
