# Lecture outline — Supervised vs unsupervised extraction: LDA and ICA (module m05)

**Slides:** [m05 lecture deck](https://claude.ai/artifact/4iBUWamfM5VpLR3oh2tZkS) (22 slides, for projection). The deck and this outline match section for section; the slide numbers are given in each section heading. Change both together.

**Length:** 2 hours, delivered in Thai with English slides and terms. **Lab:** [Lab 5](../lab/lab5_lda_ica.ipynb), **graded lab G3** (guided run-through in the session; each student then does the lab as homework, and the homework is marked).

Every number in this outline was produced by the Lab 5 code and is the same in both CI environments (see [`../EXECUTION-REPORT.md`](../EXECUTION-REPORT.md)), except where two values are given. Reference keys such as [HO00] point to [`../references.md`](../references.md). The misconception checks (MC1–MC6) are in [`../exercises/misconception-checks.md`](../exercises/misconception-checks.md).

| Time | Section | Purpose |
|---|---|---|
| 0:00–0:35 | §1 LDA: a supervised projection | Fisher's criterion, the generalised eigenproblem, at most K − 1 directions |
| 0:35–0:50 | §2 LDA or PCA features? | Wine against baselines; LDA must be inside the CV |
| 0:50–1:00 | Break | |
| 1:00–1:25 | §3 ICA: the model | Independent non-Gaussian sources; whitening; ambiguities; FastICA |
| 1:25–1:40 | §4 Worked example: three signals | ICA recovers, PCA does not |
| 1:40–1:50 | §5 When ICA fails: Gaussian sources | Identifiability |
| 1:50–2:00 | §6 Graded lab G3, midterm, project M2 | This week's work |

---

## §1 LDA: a supervised projection (35 min) · slides 3–6

**1.1 Fisher's criterion.** For $K$ classes with means $\bar x_k$, overall mean $\bar x$ and $n_k$ observations:

$$S_W = \sum_k \sum_{i\in k}(x_i - \bar x_k)(x_i - \bar x_k)^\top, \qquad S_B = \sum_k n_k(\bar x_k - \bar x)(\bar x_k - \bar x)^\top .$$

Fisher looked for the direction $w$ that maximises between-class spread relative to within-class spread [Fis36]:

$$J(w) = \frac{w^\top S_B w}{w^\top S_W w}.$$

**1.2 Solution.** $J$ is unchanged by rescaling $w$, so fix $w^\top S_W w = 1$ and maximise $w^\top S_B w$. The Lagrangian condition is the **generalised eigenproblem**

$$S_B w = \lambda S_W w ,$$

and at a solution $J(w) = \lambda$: the best direction has the largest generalised eigenvalue. With two classes, $w \propto S_W^{-1}(\bar x_1 - \bar x_0)$.

**1.3 At most $K-1$ directions.** $S_B$ is a sum of $K$ rank-one matrices whose deviations satisfy $\sum_k n_k(\bar x_k - \bar x) = 0$, so $\operatorname{rank}(S_B) \le K - 1$. Wine has 3 cultivars, hence 2 discriminant directions, however many variables are measured.

**1.4 Worked example (Lab 5, Part 1).** Wine, 13 standardised variables: generalised eigenvalues **9.08** and **4.13**. Along the first direction the cultivar means are spread about nine times as much as the within-cultivar scatter. Projections computed from `scipy.linalg.eigh(S_B, S_W)` agree with scikit-learn's `LinearDiscriminantAnalysis` up to sign and scale (correlation 1.000).

**1.5 Projection and classifier.** LDA is also a classifier: with Gaussian classes sharing one covariance matrix, the Bayes rule is linear, and Rao gave the multi-class formulation [Rao48]. Here we use LDA as a **feature extractor** feeding another classifier.

> **MC1** (K − 1 directions) here.

## §2 LDA or PCA features? (15 min) · slides 7–9

**2.1 Worked example (Lab 5, Part 2).** Wine, two features each, repeated 5-fold CV (25 scores), every fitted step inside the pipeline:

| Model | Mean accuracy | SD |
|---|---|---|
| Majority baseline | 0.399 | 0.015 |
| All 13 variables | 0.980 | 0.023 |
| PCA(2) + logistic regression | 0.961 | 0.031 |
| **LDA(2)** + logistic regression | **0.988** (0.986 in the Colab environment) | 0.016 (0.018) |

LDA's two directions are chosen to separate the cultivars; PCA's are chosen for total variance. LDA matches the full model with two features; PCA(2) loses about two points.

**2.2 LDA uses $y$, so it must be inside the CV.** The course's old feature-extraction notebook fitted LDA on all the data before splitting (audit issue E1). On pure noise (100 cases, 200 variables, 3 random classes; chance ≈ 0.33):

| LDA(2) fitted | Accuracy |
|---|---|
| On all rows, then CV | **0.810** |
| Inside the pipeline | 0.310 |

> **MC2** (labels) and **MC3** (LDA before the split) here.

## §3 ICA: the model (25 min) · slides 11–15 (slide 10: break)

**3.1 The latent-source model.** Observed signals are linear mixtures of unobserved sources: $x = A s$, with $A$ an unknown square mixing matrix [Com94]. Assumptions: the sources are **statistically independent** and **non-Gaussian** (at most one may be Gaussian), and $A$ is invertible. The classic picture: three microphones record three speakers; ICA recovers the voices.

**3.2 What can never be identified.** If $s_j$ is multiplied by $c$ and column $j$ of $A$ divided by $c$, $x$ is unchanged; the same holds for reordering. ICA therefore cannot determine each source's **scale, sign or order**.

**3.3 Whitening.** Transform $x$ so that its covariance is the identity (for example with PCA and rescaling). After whitening, the remaining unmixing is a **rotation**. PCA stops here: any rotation of whitened data is still uncorrelated, so second-order statistics cannot choose among rotations.

**3.4 Non-Gaussianity picks the rotation.** A sum of independent variables is "more Gaussian" than its parts (central-limit effect), so the rotation that makes the outputs as **non-Gaussian** as possible undoes the mixing. Measures: excess kurtosis $E[y^4]/E[y^2]^2 - 3$ (0 for a Gaussian), and negentropy. **FastICA** maximises an approximation to negentropy with a fixed-point iteration [Hyv99; HO00]; an information-maximisation approach is [BS95].

> **MC4** (ambiguities) and **MC6** (uncorrelated vs independent) here.

## §4 Worked example: three signals (15 min) · slides 16–17

Lab 5, Part 4: a sine, a square wave and a sawtooth (2,000 samples; excess kurtosis **−1.365, −1.991, −1.200**) mixed by a fixed $3\times 3$ matrix. Recovery score: for each true source, the largest absolute correlation with any recovered component, averaged (1 = perfect; it ignores scale, sign and order).

| Method | Recovery |
|---|---|
| FastICA | **0.998** |
| PCA | 0.745 |

PCA returns uncorrelated mixtures; ICA returns the signals.

## §5 When ICA fails: Gaussian sources (10 min) · slides 18–19

Replace the sources with independent Gaussian noise and mix with the same matrix. A rotation of independent standard Gaussians is again independent Gaussian, so no rotation is "more non-Gaussian" than another (Lab 5, Part 5; FastICA with random seeds 0–4):

| Sources | Recovery, five seeds | Agreement between runs |
|---|---|---|
| Non-Gaussian | 0.998 every time | identical |
| Gaussian | 0.815, 0.815, 0.799, 0.791, 0.816 | 1.000, 0.849, 0.877, 1.000 with run 0 |

FastICA may also warn that it did not converge. In real data, check the kurtosis of the outputs (near 0 is a warning sign) and rerun with several seeds.

> **MC5** (Gaussian sources) here.

## §6 Graded lab G3, midterm, project M2 (10 min) · slides 20–21 (slide 22: references)

**Graded lab G3 (Lab 5).** Five parts: Fisher directions; LDA vs PCA features; LDA before the split; ICA vs PCA; the Gaussian failure. In the lab session we run through the ideas on other examples; each student then does the lab **on their own as homework** and uploads the `.ipynb` to the G3 assignment in Teams. The homework is what is marked (3 + 1 points auto-checked, 2 + 2 points written answers).

**Midterm:** in person, on paper, covering teaching weeks 1–6 ([assessment](../../../course/assessment.md)). **Project M2** (data audit and baseline) is due this week ([project brief](../../../course/project-brief.md)).

**Independent work this week (5 h):** Lab 5 and submit it (about 2 h); midterm revision (about 1.5 h); project M2 with your team (about 1.5 h).
