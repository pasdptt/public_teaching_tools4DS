# Week 8 — Nonlinear and learned representations (bounded)

| Status | Backlog item | Course CLOs | Blueprint |
|---|---|---|---|
| **Planned**: structure only; content not yet produced | B11 | CLO1, CLO3 | [weekly plan](../../docs/blueprint/03-curriculum-blueprint.md#5-weekly-lecture-and-lab-plan-p) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Explain** what kernel PCA, LLE/Isomap and t-SNE each preserve, and **why** t-SNE is not a feature extractor.
2. **Compute** trustworthiness and held-out k-NN accuracy to **separate** visualisation quality from predictive usefulness.
3. **Train** a small CPU autoencoder with a correct output layer and loss, and **compare** its reconstruction error with PCA.
4. **Evaluate** precomputed pretrained embeddings as features against a baseline.

## Lecture (2 h per week)

* Kernel PCA, LLE, Isomap, t-SNE: what is preserved, what is not
* Trustworthiness and neighbourhood preservation
* Autoencoders as nonlinear PCA (one bounded session; CPU only)
* Modern representations: precomputed embeddings; no transformer training

## Lab (3 h per week)

**L8:** t-SNE vs PCA views of digits with trustworthiness and held-out k-NN; a time-capped CPU autoencoder vs PCA reconstruction error.

**Failure analysis (required in every lab):** The softmax plus binary cross-entropy autoencoder from the old notebook (M9); 'beautiful clusters, useless features' (M11).

## Independent work (5 h per week)

Midterm revision (5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Digits (registry) | CC BY 4.0 (verified) |
| Precomputed embeddings of a small open corpus | **TBD** (decision Q-D2) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| FeatureExtraction notebook (N05): LLE, t-SNE, autoencoder parts | Revise and bound: fix the loss (M9); t-SNE for display only (M11); fit on training data (E3) |

## Assessment links

L8; final item 3.

## Production notes

Prefer scikit-learn's `MLPRegressor` for the autoencoder to avoid a TensorFlow dependency; decide the embeddings corpus (Q-D2).
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot: `lecture/outline.md`, `lab/labNN_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
