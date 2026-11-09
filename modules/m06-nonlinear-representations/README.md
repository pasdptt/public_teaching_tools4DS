# Module m06 — Nonlinear and learned representations (bounded)

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Planned**: structure only; content not yet produced | No (practice; includes an AI-audit task) | B11 | CLO1, CLO3 | see the [schedule](../../course/schedule.md) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Explain** what kernel PCA, LLE/Isomap and t-SNE each preserve, and **why** t-SNE is not a feature extractor.
2. **Compute** trustworthiness and held-out k-NN accuracy to **separate** visualisation quality from predictive usefulness.
3. **Train** a small CPU autoencoder with a correct output layer and loss, and **compare** its reconstruction error with PCA.
4. **Evaluate** precomputed pretrained embeddings of Thai text as features against a baseline.

## Lecture (2 h per teaching week)

* Kernel PCA, LLE, Isomap, t-SNE: what is preserved, what is not
* Trustworthiness and neighbourhood preservation
* Autoencoders as nonlinear PCA (one bounded session; CPU only)
* Modern representations: precomputed embeddings of an openly licensed Thai text corpus; no model training

## Lab (3 h per teaching week)

**Lab 6 (practice):** t-SNE vs PCA views of digits with trustworthiness and held-out k-NN; a time-capped CPU autoencoder vs PCA reconstruction error; Thai-text embeddings against a bag-of-words baseline.

**Failure analysis (required in every lab):** The softmax plus binary cross-entropy autoencoder from the old notebook (M9); 'beautiful clusters, useless features' (M11). **AI-audit task:** an AI-generated t-SNE pipeline that uses t-SNE coordinates as features.

## Independent work (5 h per teaching week)

Midterm revision (5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Digits (registry) | CC BY 4.0 (verified) |
| Openly licensed Thai text corpus, embeddings precomputed once | **To source and verify** (decision: Thai text) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| FeatureExtraction notebook (N05): LLE, t-SNE, autoencoder parts | Revise and bound: fix the loss (M9); t-SNE for display only (M11); fit on training data (E3) |

## Assessment links

Practice lab; final item 3 (examined in the final, not the midterm).

## Production notes

Prefer scikit-learn's `MLPRegressor` for the autoencoder (no TensorFlow). Find a Thai corpus with a verified open licence and precompute embeddings on CPU; record it in the registry.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot (`m04-pca`): `lecture/outline.md`, `lab/lab<module><part>_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
