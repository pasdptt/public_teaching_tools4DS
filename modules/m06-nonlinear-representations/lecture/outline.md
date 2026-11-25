# Lecture outline — Nonlinear and learned representations (module m06)

**Slides:** [m06 lecture deck](https://claude.ai/artifact/2WT3SBevvPAYmwKyn42mbh) (21 slides, for projection). The deck and this outline match section for section; the slide numbers are given in each section heading. Change both together.

**Length:** 2 hours, delivered in Thai with English slides and terms. **Lab:** [Lab 6](../lab/lab6_nonlinear_representations.ipynb), practice with an AI-audit task (guided run-through in the session; each student then redoes the lab as homework).

Every number in this outline was produced by the Lab 6 code or by the module's key-numbers script, and is the same in both CI environments (see [`../EXECUTION-REPORT.md`](../EXECUTION-REPORT.md)), except where two values are given. Data: the digits (1,797 images of 8 × 8 pixels, intensities divided by 16). Reference keys such as [WVJ16] point to [`../references.md`](../references.md). The misconception checks (MC1–MC6) are in [`../exercises/misconception-checks.md`](../exercises/misconception-checks.md).

| Time | Section | Purpose |
|---|---|---|
| 0:00–0:20 | §1 Beyond linear projections | Curved structure; kernel PCA, Isomap, LLE in one idea each |
| 0:20–0:45 | §2 t-SNE: what it preserves | Neighbour probabilities, perplexity; what the picture does not show |
| 0:45–0:55 | §3 Measuring a view: trustworthiness | A number for "false neighbours"; five methods compared |
| 0:55–1:05 | Break | |
| 1:05–1:25 | §4 A picture is not a feature | Held-out prediction; no transform; the AI-audit case |
| 1:25–1:50 | §5 Autoencoders as nonlinear PCA | Linear AE = PCA; a tanh AE beats it; the softmax failure |
| 1:50–2:00 | §6 Pretrained embeddings, Lab 6, midterm | Where representations come from today; this week's work |

---

## §1 Beyond linear projections (20 min) · slides 3–4

**1.1 Why go nonlinear.** PCA finds the best *flat* subspace. If the data lie near a curved surface (a "manifold"), for example images of one digit written with smoothly varying thickness and slant, a flat projection folds distant parts of the surface on top of each other.

**1.2 Three ideas.**

| Method | Idea | Preserves | New points? |
|---|---|---|---|
| Kernel PCA [SSM98] | PCA after an implicit nonlinear feature map, computed through a kernel $k(x, x')$ | Variance in the feature space | Yes |
| Isomap [TSL00] | Distances measured *along* a $k$-nearest-neighbour graph (geodesic), then classical scaling | Global geodesic distances | Yes (approximate) |
| LLE [RS00] | Each point as a weighted combination of its neighbours; keep the same weights in 2-D | Local linear structure | Yes (approximate) |

All three are fitted to data and can transform new points in scikit-learn, so they can sit inside a pipeline.

> **MC6** (which methods have a transform) here.

## §2 t-SNE: what it preserves (25 min) · slides 5–7

**2.1 The method** [vdMH08]. In the original space, turn distances into neighbour probabilities $p_{j|i}$ with a Gaussian centred on $x_i$; its width is set so that each point has a chosen **perplexity** (an effective number of neighbours, typically 5–50). In 2-D, use a heavy-tailed Student-$t$ kernel for $q_{ij}$, and move the points to minimise the Kullback–Leibler divergence $\mathrm{KL}(P\,\|\,Q)$ by gradient descent from a random or PCA start.

**2.2 What the picture shows and does not show** [WVJ16].

* **Shows:** which points are neighbours. Well-separated groups in the data appear as separate clusters.
* **Does not show:** the distances *between* clusters, the *sizes* of clusters, or a density. The heavy tail spreads clusters apart, and the per-point bandwidth equalises their sizes.
* **Depends on:** perplexity and the random start. Different runs give different coordinates (rotated, reflected, rearranged).

> **MC1** (reading a t-SNE plot) here.

## §3 Measuring a view: trustworthiness (10 min) · slides 8–9

**3.1 Definition** [VK01]. For each point $i$, let $U_k(i)$ be its $k$ nearest neighbours **in the view**, and $r(i, j)$ the rank of $j$ among $i$'s neighbours **in the original space**. A false neighbour has $r(i, j) > k$. Then

$$T(k) = 1 - \frac{2}{n k (2n - 3k - 1)} \sum_{i=1}^{n} \sum_{j \in U_k(i)} \max\bigl(0,\ r(i, j) - k\bigr),$$

between 0 and 1; 1 means no false neighbours. It is `sklearn.manifold.trustworthiness`.

**3.2 Worked example (Lab 6, Part 1 and key numbers).** Digits, $k = 10$:

| View (2-D) | Trustworthiness |
|---|---|
| PCA | 0.830 |
| Kernel PCA (RBF) | 0.828 |
| Isomap ($k = 10$) | 0.837 |
| LLE ($k = 10$) | 0.925 |
| **t-SNE** (perplexity 30) | **0.993** |

t-SNE's picture is the most trustworthy at the local scale; it was built for exactly this. Perplexity 5, 30 and 100 give 0.991, 0.993 and 0.991 (0.990 in the Colab environment).

> **MC2** (what trustworthiness measures) here.

## §4 A picture is not a feature (20 min) · slides 11–13 (slide 10: break)

**4.1 Held-out prediction (Lab 6, Part 2).** A 5-nearest-neighbour classifier, 5-fold CV, every fitted step inside the pipeline:

| Representation | Accuracy |
|---|---|
| Majority baseline | 0.101 |
| All 64 pixels | 0.986 |
| PCA(2) | 0.620 |
| Kernel PCA(2) | 0.635 |
| Isomap(2) | 0.776 |
| LLE(2) | 0.868 |
| PCA(10) | 0.974 |
| t-SNE(2) | cannot be evaluated: no transform for new points |

Two coordinates are too few for prediction, whatever the picture looks like; ten PCA components lose almost nothing.

**4.2 The AI-audit case (Lab 6, Part 3).** An AI-generated pipeline embeds **all** images with t-SNE, then cross-validates a random forest on the coordinates: accuracy **0.991**. The course's old notebook did the same (audit M11), and the fit uses the test rows (audit E3). But a new image can only be placed by re-running t-SNE, and a re-run moves everything. A forest trained on one run (random start, `random_state=SEED`) and tested on the **same** test images embedded by a second run (`random_state=SEED + 1`):

| Test coordinates from | Accuracy |
|---|---|
| The same t-SNE run | 0.991 (0.984 in the Colab environment) |
| A second t-SNE run | **0.289** (0.287) |

**Rule:** use t-SNE to **look**, report trustworthiness, and never feed its coordinates to a model. Transductive use is acceptable only when nothing new will ever be embedded, as in a figure.

> **MC3** (t-SNE features and CV) here.

## §5 Autoencoders as nonlinear PCA (25 min) · slides 14–17

**5.1 The model.** An encoder maps $x \in \mathbb{R}^{64}$ to a code $z \in \mathbb{R}^k$; a decoder maps $z$ back to $\hat x$; training minimises reconstruction error on the **training** images only [HS06]. On a CPU, scikit-learn's `MLPRegressor` trained with $X$ as both input and target is enough; its output layer is the identity and its loss is squared error.

**5.2 Linear autoencoder = PCA.** With identity activations and squared error, the best $k$-dimensional code spans the same subspace as the first $k$ principal components [BH89]; it cannot do better (Eckart–Young). Lab 6, Part 4, $k = 10$, test-set MSE per pixel:

| Model | Test MSE |
|---|---|
| PCA(10) | 0.0196 |
| Linear autoencoder (10) | 0.0196 |
| **tanh autoencoder** (64, 10, 64) | **0.0101** |

The nonlinear autoencoder halves the error (about 15 s on a CPU). By code size (key numbers): $k = 2$: PCA 0.0529, AE 0.0366; $k = 5$: 0.0333, 0.0178; $k = 20$: 0.0080, 0.0045.

**5.3 Failure analysis: the softmax output (audit M9).** The old notebook used a **softmax** output with binary cross-entropy. A softmax row is non-negative and sums to 1; the test pixel rows sum to 19.52 on average (11.56 to 26.69). By Cauchy–Schwarz, $\lVert x - \hat x\rVert^2 \ge (\sum_j x_j - 1)^2 / p$, so **any** softmax autoencoder has test MSE of at least **0.0848**, over four times PCA(10)'s. The notebook never compared against PCA, so this went unnoticed.

| Inputs | Output layer | Loss |
|---|---|---|
| Intensities in [0, 1] | Sigmoid, or identity | Binary cross-entropy, or squared error |
| Standardised (can be negative) | Identity | Squared error |

> **MC4** (linear AE vs PCA) and **MC5** (output layer) here.

## §6 Pretrained embeddings, Lab 6, midterm (10 min) · slides 18–20 (slide 21: references)

**6.1 Pretrained embeddings.** Today most representations of text and images are not fitted to the data at hand: a large model trained elsewhere maps each item to a vector, and we use those vectors as features. The same rules apply: compare against a simple baseline (for text, bag-of-words), with every fitted step inside CV, and check what the model was trained on. The worked example on an openly licensed Thai text corpus is added once the corpus licence is verified (backlog B20).

**6.2 Lab 6 (practice, with an AI-audit task).** Five parts: three views with trustworthiness; held-out prediction; the AI-generated t-SNE pipeline; autoencoders vs PCA; the softmax bound. In the session we run through it together; each student then **redoes it on their own as homework** and uploads it to the Lab 6 practice assignment in Teams.

**Midterm:** in person, on paper, covering teaching weeks 1–6 ([assessment](../../../course/assessment.md)); this module is examined in the final (item 3).

**Independent work this week (5 h):** redo Lab 6 (about 1.5 h); midterm revision (about 3.5 h).
