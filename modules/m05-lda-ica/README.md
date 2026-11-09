# Module m05 — Supervised vs unsupervised extraction: LDA and ICA

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Planned**: structure only; content not yet produced | **Yes — graded lab G3** | B09 | CLO1, CLO2, CLO3 | see the [schedule](../../course/schedule.md) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Derive** Fisher's criterion and **solve** the generalised eigenproblem; **explain** the bound of at most K−1 directions.
2. **State** the ICA model, the role of whitening, and why non-Gaussianity identifies the sources.
3. **Recover** known sources from linear mixtures with FastICA and **compare** with PCA.
4. **Demonstrate** ICA's identifiability failure with Gaussian sources and **name** the remaining ambiguities (scale, sign, order).
5. **Fit** LDA inside a pipeline and **compare** LDA+classifier with PCA+classifier against a baseline.

## Lecture (2 h per teaching week)

* LDA: Fisher criterion, generalised eigenproblem, K−1 directions, LDA as classifier vs projection
* ICA: latent-source model, whitening, non-Gaussianity (kurtosis, negentropy), FastICA
* Identifiability; PCA vs ICA on the same mixtures

## Lab (3 h per teaching week)

**Graded lab G3:** blind source separation of synthetic signals with known ground truth (PCA vs FastICA); LDA inside a pipeline vs PCA plus classifier.

**Failure analysis (required in every lab):** Gaussian sources (ICA cannot separate them); LDA fitted before the split (audit E1).

## Independent work (5 h per teaching week)

Midterm revision (3 h); **project M2** data audit and baseline (2 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Synthetic source signals (seeded) | n/a |
| Wine (registry) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| FeatureExtraction notebook (N05): ICA and LDA parts | Revise: replace ICA on one-hot mushroom data (M8); derive LDA (M10); fit inside the pipeline (E1) |
| Mushroom data (D06) | Retire as a comparison benchmark (ceiling effect, E5); keep only as a 'too-easy data' case |

## Assessment links

**Graded lab G3**; midterm items 2 and 5; **project M2 due** this week.

## Production notes

No additional dependencies expected.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot (`m04-pca`): `lecture/outline.md`, `lab/lab<module><part>_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
