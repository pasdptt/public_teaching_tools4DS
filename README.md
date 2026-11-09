# 040563107 Tools for Statistical Data Science

KMUTNB · Faculty of Applied Science · Department of Applied Statistics · third-year B.Sc. Applied Statistics · 3 credits (2-3-5).

Dimension reduction, PCA, ICA, feature extraction, network analysis, smoothing and aggregation, high-performance computing and streaming algorithms, taught with reproducible Python workflows in **Google Colab**.

> **Status:** course revamp in progress. The audit, blueprint and course structure are complete, and the lecturer's decisions of 9 November 2026 are applied ([decision log](docs/decisions.md)): 12 teaching weeks plus 3 adjustment weeks, about 100 students, six graded labs, and teams of 5–6. The **PCA module (m04) is built as a pilot**; the other modules are structured and planned. The revised schedule is used informally this term; the TQF3 description and assessment weights are unchanged.

## Students: start here

1. [Getting started](course/getting-started.md): opening labs in Colab, the setup cell, submitting.
2. [Syllabus](course/syllabus.md) · [Schedule](course/schedule.md) · [Assessment](course/assessment.md) · [Rubrics](course/rubrics.md)
3. [Project brief](course/project-brief.md) · [AI-use policy](course/ai-policy.md) · [English–Thai glossary](course/glossary.md)
4. Weekly material: [`modules/`](modules/)

## Repository map

| Path | Contents |
|---|---|
| [`course/`](course/) | Operational course documents (syllabus, schedule, assessment, rubrics, project brief, AI policy, getting started, glossary) |
| [`modules/`](modules/) | One folder per topic module (`m01`–`m11`; weeks are assigned only in the schedule): lecture outline, Colab lab(s), exercises, references, execution report |
| [`src/tsds/`](src/tsds/) | Course helper package: environment check, course seed, licensed and checksum-verified dataset registry |
| [`datasets/`](datasets/) | Dataset policy and the registry overview (no data files are committed) |
| [`environment/`](environment/) | Pinned environments: local fallback and Colab proxy |
| [`tests/`](tests/) | Notebook execution tests and repository-structure tests |
| [`tools/`](tools/) | Notebook builder (`nbbuild.py`) and the audit harness |
| [`docs/audit/`](docs/audit/) | Evidence audit of the previous course materials, with execution results |
| [`docs/blueprint/`](docs/blueprint/) | Curriculum blueprint: outcomes, weekly plan, assessment design, backlog, decisions |
| [`docs/decisions.md`](docs/decisions.md) | Lecturer decisions (9 Nov 2026); these take precedence over the blueprint |
| [`docs/authoring-guide.md`](docs/authoring-guide.md) | How staff produce a module that meets the definition of done |

**Instructor material** (lab sources, solutions, answer keys, examination items) is kept out of this public repository. It moves to a private GitHub repository (decision D1); until then the `instructor/` folder is git-ignored.

**Licence:** code is under the [MIT licence](LICENSE); teaching content is under [CC BY 4.0](LICENSE-CONTENT.md). Datasets keep their own licences.

## Staff and reviewers

* Decisions taken and follow-ups: [decision log](docs/decisions.md)
* Production backlog: [blueprint §9](docs/blueprint/03-curriculum-blueprint.md#9-prioritised-production-backlog-and-acceptance-criteria)
* CI: [`.github/workflows/notebooks.yml`](.github/workflows/notebooks.yml) runs every test in both pinned environments on each push and weekly.
