# Problem set — module m05 (independent work)

This week's independent work is: **do Lab 5 (graded lab G3) on your own and submit it in Teams** (about 2 hours), **midterm revision** (about 1.5 hours; the core items below, P1–P5, are midterm practice), and **project M2** with your team (about 1.5 hours). Items marked *(optional)* are extra practice. Not graded. Items marked **[hand]** are the kind that appear on the paper midterm.

**P1 [hand] — A Fisher direction.** Two classes have means $\bar x_0 = (1, 2)$ and $\bar x_1 = (3, 3)$ and pooled within-class scatter $S_W = \begin{pmatrix}4 & 2\\ 2 & 3\end{pmatrix}$. Compute the direction $w \propto S_W^{-1}(\bar x_1 - \bar x_0)$ and normalise it. Interpret it: which variable separates the classes once the within-class correlation is taken into account?

**P2 [hand] — Why K − 1.** Show that $\sum_k n_k(\bar x_k - \bar x) = 0$, and explain why this limits the rank of $S_B$ to $K - 1$.

**P3 [hand] — Kurtosis.** The excess kurtosis of a uniform variable is −1.2, and of a variable equal to ±1 with probability ½ each it is −2. Verify the second value from $E[y^4]/E[y^2]^2 - 3$. Which of the two is "further from Gaussian"?

**P4 [hand] — Ambiguities.** In $x = As$, replace $s_1$ by $3 s_1$. What must happen to $A$ for $x$ to stay the same? Use your answer to explain why ICA cannot recover the scale of a source.

**P5 [hand] — Which method?** For each goal, choose PCA, LDA or ICA, and say what the method needs: (a) separate two overlapping voices in two microphone recordings; (b) reduce 30 correlated survey items to a few summary scores without using any outcome; (c) find two directions that best separate three customer segments.

**P6 — LDA as a classifier** *(optional)*. Use `LinearDiscriminantAnalysis()` itself as the classifier on standardised Wine, with the repeated CV of Lab 5. Compare with LDA(2) + logistic regression.

**P7 — One Gaussian source** *(optional)*. Add a fourth, Gaussian source to the three Lab 5 signals and mix with a $4\times 4$ matrix. Can FastICA still recover all four? Relate your answer to the assumption "at most one Gaussian source".

**P8 — Reading** *(optional)*. Hyvärinen and Oja (2000), sections on non-Gaussianity and FastICA ([references](../references.md)).

**P9 — Project M2.** With your team, write the data audit (missingness, sentinels, leakage risks) and a baseline with a valid protocol and uncertainty, in a Colab notebook ([project brief](../../../course/project-brief.md)). One member uploads it to the M2 assignment in Teams.
