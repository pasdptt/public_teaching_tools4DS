# Problem set — module m06 (independent work)

This week's independent work is: **redo Lab 6 on your own and upload it in Teams** (about 1.5 hours) and **midterm revision** (about 3.5 hours). The items below are practice for the final examination (item 3); items marked *(optional)* are extra practice. Not graded. Items marked **[hand]** are the kind that appear on the paper final.

**P1 [hand] — A false neighbour.** In a 2-D view, the 3 nearest neighbours of point A are B, C and D. In the original space, B and C are A's 1st and 2nd nearest neighbours, and D is its 9th. With $k = 3$, what does A contribute to the sum in the trustworthiness formula (lecture §3)? Which point is the false neighbour?

**P2 [hand] — Linear autoencoder and PCA.** A linear autoencoder with code size $k$ reconstructs $\hat x = D E x$, with $E$ of size $k \times p$ and $D$ of size $p \times k$. What is the largest possible rank of $DE$? Use the Eckart–Young theorem to explain why its squared reconstruction error on the training data cannot be below PCA($k$)'s.

**P3 [hand] — The softmax bound.** A test image has pixel intensities (divided by 16) that sum to 19.5, with $p = 64$. Show that any output $\hat x$ with $\sum_j \hat x_j = 1$ has mean squared error per pixel of at least $(18.5/64)^2$, and compute it. Compare with PCA(10)'s test MSE of 0.0196.

**P4 [hand] — Which tool?** For each goal, choose t-SNE, PCA or an autoencoder, and say what you would report: (a) a figure showing 10,000 customer profiles for a management report; (b) features for a churn model that will score new customers every week; (c) compressing images to 20 numbers each and reconstructing them as well as possible, where a 15-second CPU training is acceptable.

**P5 — Perplexity** *(optional)*. Rerun Lab 6's t-SNE with perplexity 5 and 100. Compare the pictures and the trustworthiness values with perplexity 30. Does a higher trustworthiness mean a "better" perplexity for every purpose?

**P6 — Two more views** *(optional)*. Add kernel PCA (RBF) and LLE (10 neighbours) to Parts 1 and 2 of Lab 6. Report trustworthiness and held-out 5-NN accuracy for each. Which has the highest accuracy with two coordinates?

**P7 — Code size** *(optional)*. Repeat Lab 6 Part 4 for $k = 2, 5, 20$. Plot test MSE against $k$ for PCA and the tanh autoencoder. Where is the autoencoder's advantage largest, relative to PCA?

**P8 — Reading** *(optional)*. Wattenberg, Viégas and Johnson (2016), *How to use t-SNE effectively* ([references](../references.md)). Which of its warnings did Lab 6 demonstrate?

**P9 — Midterm revision.** Teaching weeks 1–6 ([assessment](../../../course/assessment.md)); use the problem sets of modules m01–m05, starting with the items marked [hand].
